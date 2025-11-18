"""
sensor_gateway.py

Simula varios sensores MQTT que publican en una jerarquía de tópicos
y una gateway central que los recoge en un CSV. Soporta comandos por
broadcast para arrancar/detener la simulación de los sensores.

Uso:
  - Configure variables de entorno en PowerShell (temporal):
      $env:MQTT_HOST='72ae2a86567a4d8c84c5d73a46ffee94.s1.eu.hivemq.cloud'
      $env:MQTT_PORT='8883'
      $env:MQTT_USER='hivemq.webclient.1763322866924'
      $env:MQTT_PASS='6BU>7udCZk3,lO9sLe.?'
  - Ejecutar: python .\sensor_gateway.py

"""

import os
import threading
import time
import random
import csv
import signal
from datetime import datetime

import paho.mqtt.client as paho
from paho import mqtt


# Configuration from environment (with sensible defaults)
MQTT_HOST = os.getenv('MQTT_HOST', '72ae2a86567a4d8c84c5d73a46ffee94.s1.eu.hivemq.cloud')
MQTT_PORT = int(os.getenv('MQTT_PORT', '8883'))
MQTT_USER = os.getenv('MQTT_USER')
MQTT_PASS = os.getenv('MQTT_PASS')

# Topics hierarchy
SENSOR_TOPICS = [
    'lan/sala1/sensor/temp',
    'lan/sala1/sensor/hum',
    'lan/sala2/sensor/temp',
]

# Broadcast and per-sensor command topic suffix
BROADCAST_TOPIC = 'lan/commands'
CMD_SUFFIX = 'cmd'  # per sensor: <topic>/cmd

# CSV file where gateway stores received data
CSV_FILE = 'gateway_data.csv'

RUN = True


class Sensor(threading.Thread):
    def __init__(self, topic, client_id=None, publish_interval=2.0):
        super().__init__()
        self.topic = topic
        self.client_id = client_id or f"sensor-{topic.replace('/', '_')}"
        self.publish_interval = publish_interval
        self._running = False
        self._stop_event = threading.Event()

        self.client = paho.Client(client_id=self.client_id, userdata=None, protocol=paho.MQTTv5)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # subscribe to broadcast and its own command topic
        self.cmd_topic = f"{self.topic}/{CMD_SUFFIX}"

    def connect(self):
        if MQTT_PORT == 8883:
            self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
            if not MQTT_USER or not MQTT_PASS:
                print(f"ERROR: MQTT_USER and MQTT_PASS must be set to connect with TLS to {MQTT_HOST}:{MQTT_PORT}")
                raise SystemExit(1)
            self.client.username_pw_set(MQTT_USER, MQTT_PASS)
        else:
            # attempt anonymous connect
            pass
        self.client.connect(MQTT_HOST, MQTT_PORT)

    def on_connect(self, client, userdata, flags, rc, properties=None):
        print(f"[{self.client_id}] connected (rc={rc})")
        # subscribe to broadcast and own command topic
        client.subscribe(BROADCAST_TOPIC, qos=1)
        client.subscribe(self.cmd_topic, qos=1)

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode('utf-8') if msg.payload else ''
        print(f"[{self.client_id}] CMD recv on {msg.topic}: {payload}")
        if payload.strip().lower() == 'start':
            self._running = True
        elif payload.strip().lower() == 'stop':
            self._running = False

    def publish_value(self):
        # simple generator depending on topic
        if 'temp' in self.topic:
            value = round(random.uniform(18.0, 26.0), 2)
        elif 'hum' in self.topic:
            value = round(random.uniform(30.0, 80.0), 2)
        else:
            value = random.random()
        payload = str(value)
        self.client.publish(self.topic, payload=payload, qos=1)
        print(f"[{self.client_id}] PUBLISHED {self.topic} -> {payload}")

    def run(self):
        # connect and start loop
        self.connect()
        self.client.loop_start()
        try:
            while not self._stop_event.is_set():
                if self._running:
                    self.publish_value()
                time.sleep(self.publish_interval)
        finally:
            self.client.loop_stop()
            self.client.disconnect()

    def stop(self):
        self._stop_event.set()


class Gateway:
    def __init__(self, csv_file=CSV_FILE):
        self.client = paho.Client(client_id='gateway-collector', userdata=None, protocol=paho.MQTTv5)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.csv_file = csv_file
        # ensure csv header
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'topic', 'payload'])

    def connect(self):
        if MQTT_PORT == 8883:
            self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
            if not MQTT_USER or not MQTT_PASS:
                print("ERROR: Gateway needs MQTT_USER/MQTT_PASS to connect via TLS")
                raise SystemExit(1)
            self.client.username_pw_set(MQTT_USER, MQTT_PASS)
        self.client.connect(MQTT_HOST, MQTT_PORT)

    def on_connect(self, client, userdata, flags, rc, properties=None):
        print(f"[gateway] connected (rc={rc}), subscribing to lan/+/sensor/#")
        client.subscribe('lan/+/sensor/#', qos=1)

    def on_message(self, client, userdata, msg):
        ts = datetime.utcnow().isoformat()
        payload = msg.payload.decode('utf-8') if msg.payload else ''
        print(f"[gateway] {ts} {msg.topic} -> {payload}")
        with open(self.csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([ts, msg.topic, payload])

    def start(self):
        self.connect()
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()

    def send_broadcast(self, cmd):
        self.client.publish(BROADCAST_TOPIC, payload=cmd, qos=1)

    def send_command_to_sensor(self, sensor_topic, cmd):
        cmd_topic = f"{sensor_topic}/{CMD_SUFFIX}"
        self.client.publish(cmd_topic, payload=cmd, qos=1)


def try_sniff_one_packet():
    """
    Intentar capturar un único paquete TCP hacia/desde el broker usando scapy.
    Esto es opcional y puede fallar si scapy no está instalado o no se tienen
    permisos (en Windows necesita Npcap y privilegios).
    """
    try:
        from scapy.all import sniff, hexdump
    except Exception as e:
        print("scapy no disponible o no se pudo importar; omitiendo captura.\nInstalar scapy y Npcap si desea captura desde el script.")
        return

    print(f"Intentando capturar 1 paquete TCP hacia/desde {MQTT_HOST}:{MQTT_PORT} (requiere permisos)...")
    bpf = f"tcp and host {MQTT_HOST} and port {MQTT_PORT}"
    try:
        pkts = sniff(filter=bpf, count=1, timeout=10)
    except Exception as e:
        print(f"Error al sniffear: {e}")
        return

    if not pkts:
        print("No se capturó ningún paquete en el tiempo dado.")
        return

    pkt = pkts[0]
    print("Packet summary:")
    print(pkt.summary())
    print("Hexdump: ")
    hexdump(pkt)
    with open('sniff_packet.txt', 'w', encoding='utf-8') as f:
        f.write(pkt.summary() + '\n')
        try:
            f.write(bytes(pkt).hex())
        except Exception:
            pass


def main():
    global RUN
    print('Starting sensor/gateway simulation')

    # create gateway
    gateway = Gateway()
    gateway.start()

    # create sensors
    sensors = []
    for t in SENSOR_TOPICS:
        s = Sensor(topic=t, publish_interval=2.0)
        s.daemon = True
        s.start()
        sensors.append(s)

    # give time to connect
    time.sleep(2)

    print('\nAvailable commands:')
    print('  broadcast start   -> start all sensors')
    print('  broadcast stop    -> stop all sensors')
    print('  sensor <topic> start|stop  -> command single sensor')
    print('  sniff             -> try to capture one packet (requires scapy/admin)')
    print('  exit              -> stop everything and quit')

    try:
        while True:
            cmd = input('> ').strip()
            if not cmd:
                continue
            parts = cmd.split()
            if parts[0] == 'broadcast' and len(parts) == 2:
                gateway.send_broadcast(parts[1])
                print(f"Broadcasted '{parts[1]}'")
            elif parts[0] == 'sensor' and len(parts) == 3:
                sensor_topic = parts[1]
                action = parts[2]
                gateway.send_command_to_sensor(sensor_topic, action)
                print(f"Sent '{action}' to {sensor_topic}")
            elif parts[0] == 'sniff':
                try_sniff_one_packet()
            elif parts[0] == 'exit':
                break
            else:
                print('Unknown command')
    except KeyboardInterrupt:
        print('\nInterrupted by user')
    finally:
        print('Stopping sensors and gateway...')
        for s in sensors:
            s.stop()
        # give threads time to stop
        time.sleep(1)
        gateway.stop()
        print('Stopped. CSV saved to', CSV_FILE)


if __name__ == '__main__':
    main()
