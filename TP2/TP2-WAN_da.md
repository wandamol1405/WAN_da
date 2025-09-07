# Más conceptos fundamentales de capa física y capa de enlace de datos.

**Nombres**

- _Francisco Gomez Neimann_

- _Martina Juri_

- _Maria Wanda Molina_

- _Marcos Morán_

**Nombre del grupo**

WAN_da

**Nombre del centro educativo o institución**

Facultad de Ciencias Exactas, Físicas y Naturales

**Nombre del curso o materia**

Comunicaciones de Datos

**Profesores**

Santiago M. Henn

**Fecha**

06 de septiembre de 2025

---

### Información de los autores

- **Información de contacto**:

  _francisco.gomez.neimann@mi.unc.edu.ar_

  _martina.juri@mi.unc.edu.ar_

  _wanda.molina@mi.unc.edu.ar_

  _mmoran@mi.unc.edu.ar_

---
## Resumen

El trabajo práctico N°2 tiene como objetivo consolidar y expandir los conocimientos en las capas más fundamentales de las redes de computadoras: la Capa Física y la Capa de Enlace de Datos. Además de los conceptos teóricos, el trabajo introduce una herramienta práctica esencial para el análisis de redes, WireShark, y fomenta la familiarización con su uso.

## Introducción

En el presente trabajo práctico se abordan conceptos fundamentales relacionados con la capa física y la capa de enlace de datos dentro del modelo de referencia OSI. Se busca comprender fenómenos físicos que afectan la transmisión de señales, tales como el efecto Doppler, la atenuación y la relación señal-ruido, y analizar cómo influyen en la calidad de la comunicación.

Asimismo, se introduce la herramienta Wireshark, un analizador de protocolos que permite observar y estudiar el tráfico de red en tiempo real. De este modo, los ejercicios propuestos integran tanto el estudio teórico de los fenómenos de transmisión como la aplicación práctica en el análisis de tramas de datos y protocolos de red.

**Palabras Clave**

## Marco teórico

### Capa Física

La capa física del modelo OSI se encarga de la transmisión de bits a través de un medio físico, ya sea guiado (cableado) o no guiado (inalámbrico). Sus funciones incluyen la codificación de la señal, la modulación, la sincronización y la definición de las características eléctricas, ópticas o radioeléctricas del medio. Dentro de esta capa se analizan fenómenos como:

- **Efecto Doppler**: variación aparente de la frecuencia de una onda debido al movimiento relativo entre transmisor y receptor. Tiene especial impacto en comunicaciones móviles y satelitales.

- **Atenuación**: pérdida de potencia de la señal a medida que se propaga por el medio.

- **Ruido e interferencia electromagnética**: perturbaciones externas que afectan la calidad de la señal.

- **Relación Señal-Ruido (SNR)**: indicador que mide la proporción entre la potencia de la señal y el ruido presente en el canal.

### Capa de Enlace de Datos

La capa de enlace se sitúa sobre la capa física y tiene como función principal garantizar una comunicación libre de errores entre nodos adyacentes. Sus principales tareas son:

- *Encapsulación de tramas*: organización de la información en bloques con cabecera y control de errores.

- *Detección y corrección de errores*: a través de mecanismos como CRC o bits de paridad.

- *Control de flujo*: coordinación entre emisor y receptor para evitar pérdidas de datos.

- *Direccionamiento físico*: mediante el uso de direcciones MAC únicas para cada dispositivo.

### Wireshark

Wireshark es una herramienta de software que permite capturar, visualizar y analizar paquetes de red en tiempo real. Es fundamental para estudiar cómo se estructuran las tramas, qué protocolos intervienen y cómo se comporta el tráfico en diferentes escenarios. Entre sus utilidades se encuentran:

- Filtrado de paquetes por direcciones IP o protocolos.

- Visualización de tramas Ethernet, IP y TCP/UDP.

- Exportación y documentación de capturas para su análisis posterior.
---

## Resultados
### 1. Fenómeno físico representado y sus características (a)
a. El fenómeno representado es el efecto Doppler, que consiste en la variación aparente de la frecuencia de una onda debido al movimiento relativo entre el transmisor y el receptor.
Sus características principales son:

- La frecuencia recibida aumenta cuando emisor y receptor se acercan, y disminuye cuando se alejan.

- La magnitud del desplazamiento depende de la velocidad relativa y de la frecuencia de la portadora (a mayor frecuencia, mayor efecto Doppler).

- Tiene especial relevancia en comunicaciones satelitales y sistemas móviles, donde hay desplazamiento constante.

- Puede dificultar la demodulación de la señal y aumentar la tasa de error, por lo que los sistemas aplican compensación de Doppler para garantizar la correcta recepción.

![alt text](efecto_doppler.png)

Figura 1.1: [Efecto Doppler](https://drive.google.com/drive/u/0/folders/1VmlirVlTplG6luMhQwEFXqqF9nYieI9d)

b. Los tipos de transmisión más afectados son:
- Transmisiones analógicas y de banda angosta, donde un pqeueño cambio de frecuencia altera significativamente la señal.
- Comunicaciones de alta freceucnia, ya que el desplazamiento Dopple es proporcional a la frecuencia portadora.
- Sistemas moviles terrestres: telefonía celular, enlaces entre estaciones base y dsipositivos en movimiento rápido.

Las transmisiones mas resilientes son: 
- Señales digitales de banda ancha (OFDM, como LTE o WiFi), que toleran mejor los pequeños desplazamientos de frecuencia.
- Fibra óptica: no se ve afectado al ser un medio guiado.
- Satelites geoestacionarios, ya que suposicion relativa respecto a la Tierra es fija, minimizando el Doppler.

c. Se recomienda utilizar el modo avion cuando se esta a bordo de un avión debido a la interferencia electromagnética emitida por los celulares. Emiten en multiples bandas de freceuncia que pueden afectar la instrumentación de navegacion y comunicación del avión. Ademas, a gran altura, el celular intenta conectarse a varias antenas terrestres a la vez, lo que incrementa la potencia de transmision y el riesgo de interferencia. 
En relación con el efecto Doppler, existe un vínculo entre la restricción de utilizar el celular en el avión y éste fenómeno. El movimiento de un avión a alta velocidad genera un desplazamiento Doppler significativo en las señales del celulcar, lo que puede producir errores de frecuencia e inestabilidad en las comunicacion. Esto, sumado a la posibilidad de interferencia con los sistemas de a bordo, refuerza la restricción.

---

### 2. Fenómeno físico representado y sus características (b)

a. El fenomeno representado en la figura es la interferencia o ruido en la señal durante la transmisión. La señal inicialmente limpia se ve distorsionada en cierto tramo (ruido o perturbación). Esto puede deberse a fenómenos como:

- **Ruido electromagnético:** Introducido por otras fuentes de energía eléctrica o radiación.
- **Desvanecimiento (fading):** Variaciones en la amplitud y fase de la señal debido a obstáculos, reflexión o dispersión multipath.

![alt text](ruido.png)

Figura 2.1: [Ruido en transminsión de señal](https://drive.google.com/drive/u/0/folders/1VmlirVlTplG6luMhQwEFXqqF9nYieI9d)

#### Características principales del fenómeno

- Se manifiesta como distorsión o “picos” en la señal original.
- Es aleatorio y puede variar en el tiempo y espacio.
- Afecta la calidad de la señal recibida y puede degradar la información transmitida.

En la figura, el operario con la pistola representa la introducción de ruido o interferencia durante la transmisión.

b. Bandas de transmisión y susceptibilidad

Recordando las bandas vistas en TP01:

- **Baja frecuencia (LF, MF, HF):** Menos afectadas por desvanecimiento rápido; penetran obstáculos mejor.
- **Alta frecuencia (VHF, UHF, SHF, EHF):** Más susceptibles a interferencias y desvanecimiento multipath, especialmente microondas y comunicaciones móviles.

#### Conclusión:
Afecta más: Transmisiones de alta frecuencia (por ejemplo, celular, Wi-Fi, microondas).
Más resilientes: Transmisiones de baja frecuencia, por ejemplo AM de radio, que pueden atravesar obstáculos con menor degradación.

c. SNR y relación con BER

**SNR (Signal-to-Noise Ratio):** Es la relación entre la potencia de la señal útil y la potencia del ruido.
- Se mide en decibelios (dB).
- Una SNR alta indica que la señal es mucho más fuerte que el ruido → mejor calidad de transmisión.
- Una SNR baja indica que el ruido domina → mayor probabilidad de errores.

**BER:** Proporción de bits erróneos recibidos respecto a los transmitidos.

Relación con BER (Bit Error Rate):
- Si la SNR disminuye, la probabilidad de que los bits se interpreten mal aumenta → BER alta.
- Por lo tanto, SNR y BER están directamente relacionados: mayor SNR → menor BER y viceversa.

![alt text](ber_ser.png)



### 3. 


a. 
Ethernet es una de las dos tecnologías LAN utilizadas hoy en día, siendo la otra LAN inalámbricas (WLAN). Ethernet utiliza comunicaciones por cable, incluyendo pares trenzados, enlaces de fibra óptica y cables coaxiales.

Ethernet funciona en la capa de enlace de datos y en la capa física. Es una familia de tecnologías de red definidas en los estándares IEEE 802.2 y 802.3. Ethernet soporta los siguientes anchos de banda de datos:

10 Mbps
100 Mbps
1000 Mbps (1 Gbps)
10.000 Mbps (10 Gbps)
40,000 Mbps (40 Gbps)
100,000 Mbps (100 Gbps)

Los protocolos IEEE 802 LAN/MAN, incluyendo Ethernet, utilizan las dos subcapas independientes siguientes de la capa de enlace de datos para operar. Son el Control de enlace lógico (LLC) y el Control de acceso a medios (MAC)

Subcapa LLC - Esta subcapa IEEE 802.2 se comunica entre el software de red en las capas superiores y el hardware del dispositivo en las capas inferiores. Coloca en la trama información que identifica qué protocolo de capa de red se utiliza para la trama. Esta información permite que múltiples protocolos de Capa 3, como IPv4 e IPv6, utilicen la misma interfaz de red y medios.

Subcapa MAC - Esta subcapa se implementa en hardware y es responsable de la encapsulación de datos y control de acceso a medios. Proporciona direccionamiento de capa de enlace de datos y está integrado con varias tecnologías de capa física.

Encapsulación de datos

La encapsulación de datos IEEE 802.3 incluye lo siguiente:

Trama de Ethernet - Esta es la estructura interna de la trama Ethernet.
Direccionamiento Ethernet - la trama Ethernet incluye una dirección MAC de origen y destino para entregar la trama Ethernet de NIC Ethernet a NIC Ethernet en la misma LAN.
Detección de errores Ethernet - La trama Ethernet incluye un avance de secuencia de verificación de trama (FCS) utilizado para la detección de errores.
El tamaño mínimo de trama de Ethernet es de 64 bytes, y el máximo es de 1518 bytes. Esto incluye todos los bytes del campo de dirección MAC de destino a través del campo de secuencia de verificación de trama (FCS). El campo preámbulo no se incluye al describir el tamaño de una trama.

![alt text](tramadedatos.png)

Las diferencias principales entre Ethernet, Fast Ethernet y Gigabit Ethernet radican en la velocidad de transmisión de datos, la cual ha evolucionado significativamente a lo largo del tiempo. 🚀

Ethernet (10BASE-T)
Velocidad: 10 Mbps (megabits por segundo).

Contexto: Fue la tecnología original y estándar para las redes de área local (LAN) a principios de la década de 1990.

Características: Utiliza cables de par trenzado (Cat 3 o superior) y tiene una velocidad muy limitada para los estándares actuales. Aunque ya no se usa comúnmente para redes modernas, sentó las bases para los estándares posteriores.

Fast Ethernet (100BASE-T)
Velocidad: 100 Mbps.

Contexto: Surgió a mediados de la década de 1990 como una respuesta a la creciente necesidad de mayor ancho de banda en las redes.

Características: Es diez veces más rápido que el Ethernet original y se convirtió en el estándar de facto para las redes de escritorio durante muchos años. Utiliza cables de par trenzado de categoría 5 (Cat 5) o superior.

Gigabit Ethernet (1000BASE-T)
Velocidad: 1,000 Mbps o 1 Gbps (gigabit por segundo).

Contexto: Introducido a finales de la década de 1990, fue una mejora masiva que permitía velocidades mucho más altas, necesarias para transferencias de archivos grandes, multimedia y servidores de alto rendimiento.

Características: Es la velocidad estándar para las redes cableadas domésticas y empresariales en la actualidad. Es cien veces más rápido que el Ethernet original y diez veces más rápido que Fast Ethernet. Utiliza cables de categoría 5e (Cat 5e) o superiores, lo que lo hace compatible con la infraestructura de cableado existente.



b.
El cableado de par trenzado no blindado (UTP) es el medio de red más común. El cableado UTP, que se termina con conectores RJ-45, se utiliza para interconectar hosts de red con dispositivos intermediarios de red, como switches y routers.

En las redes LAN, el cable UTP consta de cuatro pares de hilos codificados por colores que están trenzados entre sí y recubiertos con un revestimiento de plástico flexible que los protege contra daños físicos menores. El trenzado de los hilos ayuda a proteger contra las interferencias de señales de otros hilos.

Cuando se utiliza como medio de red, el cableado (UTP) consta de cuatro pares de hilos codificados por colores que están trenzados entre sí y recubiertos con un revestimiento de plástico flexible. Su tamaño pequeño puede ser una ventaja durante la instalación.

Los cables UTP no utilizan blindaje para contrarrestar los efectos de la EMI y la RFI. En cambio, los diseñadores de cable han descubierto otras formas de limitar el efecto negativo del crosstalk:

Anulación - Los diseñadores ahora emparejan los hilos en un circuito. Cuando dos hilos en un circuito eléctrico están cerca, los campos magnéticos son exactamente opuestos entre sí. Por lo tanto, los dos campos magnéticos se anulan y también anulan cualquier señal de EMI y RFI externa.

Variando el número de vueltas por par de hilos - Para mejorar aún más el efecto de anulación de los pares de hilos del circuito, los diseñadores cambian el número de vueltas de cada par de hilos en un cable. Los cables UTP deben seguir especificaciones precisas que rigen cuántas vueltas o trenzas se permiten por metro (3,28 ft) de cable. 

Los cables UTP dependen exclusivamente del efecto de anulación producido por los pares de hilos trenzados para limitar la degradación de la señal y proporcionar un autoblindaje eficaz de los pares de hilos en los medios de red.

Según las diferentes situaciones, es posible que los cables UTP necesiten armarse según las diferentes convenciones para los cableados. Esto significa que los hilos individuales del cable deben conectarse en diferente orden para distintos grupos de pins en los conectores RJ-45.

Cable directo de Ethernet - El tipo más común de cable de red. Por lo general, se utiliza para interconectar un host con un switch y un switch con un router.

Cable cruzado Ethernet - El cable utilizado para interconectar dispositivos similares. Por ejemplo, para conectar un switch a un switch, un host a un host o un router a un router. Sin embargo, los cables de cruce ahora se consideran heredados, ya que las NIC utilizan cruzado de interfaz dependiente medio (Auto-MDIX) para detectar automáticamente el tipo de cable y realizar la conexión interna.

c.
Datos extraidos de realizar ping hacia la puerta de enlace capturados usando Wireshark:
0000   30 9c 23 07 ef 58 b8 d6 f6 53 a5 a1 08 00 45 00
0010   00 3c 63 e6 00 00 40 01 93 83 c0 a8 01 01 c0 a8
0020   01 06 00 00 54 cc 00 01 00 8f 61 62 63 64 65 66
0030   67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76
0040   77 61 62 63 64 65 66 67 68 69

d. Direccion MAC del dispositivo: 

![alt text](macadress.png)

Información del dispositivo:

![alt text](deviceinformation.png)

e. Apartados c y d pero comunicandonos con otro PC:
Datos:
0000   b8 d6 f6 53 a5 a1 30 9c 23 07 ef 58 08 00 45 00
0010   00 3c f7 ad 00 00 80 01 b5 b3 c0 a8 01 06 b5 5b
0020   16 56 08 00 4c c2 00 01 00 99 61 62 63 64 65 66
0030   67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76
0040   77 61 62 63 64 65 66 67 68 69

Direccion Mac:
![alt text](macadress2.png)
Informacion de la empresa: al ser la misma direccion MAC que en el apartado anterior la documentacion es la misma que en el apartado d.


### 4. Reflexiones finales y conclusiones

El análisis con Wireshark mostró que la dirección MAC funciona como un identificador único de la tarjeta de red y, aunque no se transmite a través de Internet, sí es visible en la red local. Esto implica que otros equipos o el propio router pueden reconocer y seguir la actividad de un dispositivo, e incluso identificar su fabricante a partir del **OUI**. Por lo tanto, la privacidad del usuario dentro de una LAN es limitada: la MAC permite rastrear y asociar la presencia del dispositivo en el tiempo, lo que representa un punto crítico en la trazabilidad y en la exposición de datos en entornos compartidos.

*Similitudes entre el IMEI y la dirección MAC.*

El **IMEI** (International Mobile Equipment Identity) es un número único de 15 dígitos asignado a cada dispositivo móvil. Se utiliza para identificar y autenticar el dispositivo en la red móvil. Es crucial para la seguridad, ya que permite a los operadores bloquear dispositivos robados o perdidos, evitando su uso en la red.

La **dirección MAC** (Media Access Control) es también un identificador único, pero aplicado a las interfaces de red (Wi-Fi, Bluetooth, Ethernet). Está grabada en la tarjeta de red del dispositivo y sirve para que las redes lo reconozcan dentro de una LAN o en conexiones inalámbricas.

Son similares en varios aspectos:
- Ambos son identificadores únicos a nivel de hardware.
- Se asignan por el fabricante y no cambian al reiniciar o reinstalar software.
- Permiten identificar y controlar el acceso de un dispositivo a una red (IMEI en redes móviles; MAC en redes locales).


*¿Una VPN oculta la dirección MAC del dispositivo?*

Una **VPN** no oculta la dirección **MAC** del dispositivo, porque la MAC es un identificador físico grabado en la tarjeta de red y solo se utiliza dentro de la red local para que el router sepa a qué equipo entregar los datos, lo que realmente hace la VPN es cifrar el tráfico y reemplazar la dirección IP pública por la del servidor remoto, de modo que los sitios web o servicios externos solo ven esa IP de la VPN y no la de la conexión real, mientras que la MAC sigue siendo visible únicamente para la red local o el proveedor de Internet.
