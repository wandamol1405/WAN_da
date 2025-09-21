# Capas de Acceso en Redes Locales, Protocolos y Fundamentos

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

22 de septiembre de 2025

---

### Información de los autores

- **Información de contacto**:

  _francisco.gomez.neimann@mi.unc.edu.ar_

  _martina.juri@mi.unc.edu.ar_

  _wanda.molina@mi.unc.edu.ar_

  _mmoran@mi.unc.edu.ar_

---
## Resumen

En este trabajo se estudiará la evolución de los métodos de transmisión de datos y el rol de la IEEE en la estandarización de tecnologías de red. Se abordarán los estándares IEEE 802.3 (Ethernet) y IEEE 802.11 (Wi-Fi), identificando sus campos de aplicación y principales características. Además, se analizarán aspectos prácticos como la compatibilidad entre dispositivos y protocolos, la relación entre seguridad y versiones de Wi-Fi, y la clasificación de las versiones más recientes de estos protocolos (Wi-Fi 5, 6 y 7). Finalmente, se vincularán estos conceptos con otras tecnologías de comunicación, destacando la importancia de las capas de acceso en redes locales.

## Introducción

Las redes de datos constituyen hoy en día la base de la comunicación digital, permitiendo la interconexión de dispositivos, personas y servicios en todo el mundo. Sin embargo, ¿cómo logramos que sistemas tan diversos hablen un mismo “idioma” y mantengan la compatibilidad a lo largo del tiempo?  

En este trabajo práctico se abordará la evolución de los estándares definidos por el **IEEE**, en particular **IEEE 802.3 (Ethernet)** y **IEEE 802.11 (Wi-Fi)**, que han sido fundamentales para el desarrollo de las redes cableadas e inalámbricas. Se analizarán sus características, compatibilidad, seguridad y las últimas versiones en uso (Wi-Fi 5/6/7), buscando comprender cómo las decisiones de estandarización influyen directamente en la calidad y seguridad de las comunicaciones actuales.


**Palabras Clave**

## Marco teórico

### IEEE 802.3 y IEEE 802.11 — Historia y campo de aplicación

#### IEEE 802.3 (Ethernet)

- En 1983, el estándar Ethernet fue adoptado oficialmente como parte del proyecto IEEE 802 del comité LAN/MAN (Local Area/Metropolitan Area Networks) del IEEE.  
- A lo largo de los años, el estándar ha evolucionado a través de múltiples enmiendas para soportar distintas velocidades físicas de transmisión, distintos medios físicos (cable coaxial, par trenzado, fibra óptica), diferentes longitudes de segmento, y mejoras en fiabilidad y eficiencia.  
- Actualmente, IEEE 802.3 es el estándar de facto para redes locales cableadas (LAN) y para muchas infraestructuras de backbone, centros de datos, conexiones de servidores, equipos de red, etc. Su campo de aplicación va desde redes hogareñas hasta campus universitarios y grandes corporaciones.  

#### IEEE 802.11 (Wi-Fi)

- IEEE 802.11 es el grupo de trabajo del IEEE para redes inalámbricas de área local (Wireless LAN). Fue uno de los primeros estándares del proyecto IEEE 802, creado para definir cómo se transmite información inalámbricamente en LANs.  
- Desde su primera versión (1997) ha habido múltiples revisiones y enmiendas: 802.11b, a, g, n, ac, ax, be, etc., cada versión agregando mejoras en velocidad, eficiencia espectral, manejo de interferencia, rango, bandas de frecuencia, etc.  
- Su campo de aplicación es toda red que necesite transmitir datos sin cables: redes domésticas, redes universitarias, oficinas, dispositivos móviles, IoT, espacios públicos, etc. Esencialmente permite conectividad inalámbrica dentro de un área cubierta por puntos de acceso (APs).

![Canales en 802.11(WiFi)](canales.png)

Figura 1.1: [Distribución de canales en la banda de 2.4 GHz para IEEE 802.11](https://www.adslzone.net/reportajes/wifi/canales-wifi/)


### ¿Qué sucede si una red Wi-Fi opera con determinado protocolo y un dispositivo viejo no lo soporta?

Cuando la red Wi-Fi está configurada para operar con una versión de protocolo determinada (por ejemplo IEEE 802.11ac o 802.11ax), pero un dispositivo (ej. una notebook vieja) solo tiene soporte para versiones anteriores (ej. 802.11b/g/n), ocurren varios posibles escenarios:

- Si la red y el punto de acceso (AP) tienen soporte **retrocompatible** (“backward compatibility”), el dispositivo viejo se conectará usando la versión más antigua común entre lo que la red/AP soporta y lo que el dispositivo puede usar. Por ejemplo, si la red soporta 802.11ac y también modo 802.11n/g, el dispositivo que solo tiene 802.11n se conectará mediante 802.11n.  
- Si no hay compatibilidad (por ejemplo, la red fue configurada para **rechazar** conexiones con versiones antiguas, o el dispositivo no soporta las bandas usadas), el dispositivo **no podrá conectarse**.  
- La velocidad, el rendimiento y la estabilidad estarán limitados a lo que el dispositivo antiguo pueda manejar: menor tasa de datos, mayor latencia, posiblemente mayor pérdida de paquete o degradación si la señal es débil.

### Cuadro comparativo

| Característica            | Wi-Fi 5                   | Wi-Fi 6                     | Wi-Fi 7                         |
|---------------------------|----------------------------|-------------------------------|----------------------------------|
| Versión IEEE              | IEEE 802.11ac™              | IEEE 802.11ax™                | IEEE 802.11be™ (enmienda de 802.11) |
| Tasa de datos máxima      | Alrededor de **3.5 Gbit/s** teóricos bajo condiciones ideales. | Hasta cerca de **9.6 Gbit/s** según IEEE. | Objetivo de ~**46 Gbit/s** teóricos; según IEEE 802.11be documentos recientes. |
| Banda(s)                   | Principalmente **5 GHz**  | 2.4 GHz y 5 GHz (y extensión a 6 GHz en algunos casos) | 2.4 GHz, 5 GHz, **6 GHz** y mejoras en multi-link operación; también soporte para bandas no licenciadas hasta 7.25 GHz en algunos sub-7.25 GHz. |
| Ancho de banda de canal   | Hasta **160 MHz**          | Hasta **160 MHz**, con posibilidades de combinación de canales (ej. 80+80 MHz) para mejorar rendimiento en ciertos contextos.  | Puede llegar a **320 MHz** de ancho de canal.  |
| Modulación                | Uso de OFDM, hasta **256-QAM** en Wi-Fi 5.  | Mejora con **1024-QAM**, eficiencia espectral mayor.  | Se espera uso de modulación de mayor orden aún (≥ 4096-QAM) como parte de mejoras de capacidad.  |
| Sistema de seguridad       | WPA2 (WPA2-Personal / WPA2-Enterprise) es lo usual con Wi-Fi 5. | Introduce soporte más extendido para WPA3, mejoras en autenticación, mejores protecciones frente a ataques modernos.  | Continuación de WPA3; mejoras inherentes al estándar nuevo, con mejores mecanismos de seguridad y compatibilidad hacia atrás.  |

Tabla 1: Cuadro comparativo Wi-Fi 5 / Wi-Fi 6 / Wi-Fi 7

![Timeline Wi-Fi 5/6/6E/7](timeline_wifi.png)
Figura 1.2: [Evolución de los estándares Wi-Fi según IEEE 802.11](https://www.arrow.com/es-mx/research-and-events/articles/the-evolution-of-wi-fi-technologies-wi-fi-7)

## Resultados

### 1. Versión del protocolo 802.11 en redes abiertas de la Facultad

Para este apartado se realizó la prueba de conexión a la red **UNC-LIBRE**.  
Utilizando las herramientas de diagnóstico del sistema operativo Windows, se observó que el protocolo empleado es **Wi-Fi 5 (IEEE 802.11ac)**, operando en la **banda de 5 GHz**.  

Este resultado indica que la Facultad utiliza un estándar ampliamente difundido, que permite velocidades teóricas de varios Gbit/s y un mejor desempeño en ambientes con alta densidad de usuarios en comparación con versiones previas como 802.11n (Wi-Fi 4).  

El estándar IEEE 802.11 evoluciona en cada versión no solo en cuanto a tasas de datos y eficiencia espectral, sino también en mecanismos de seguridad.  

En este caso, la red **UNC-LIBRE** presenta el tipo de seguridad: **Open** (red abierta, sin cifrado). Esto implica que la comunicación no cuenta con mecanismos de autenticación ni de cifrado de datos, lo cual expone la información transmitida a posibles ataques de interceptación.  

Comparando con versiones más seguras:  
- Un sistema **WPA2 (Wi-Fi Protected Access 2)** hubiera permitido el uso de cifrado AES-CCMP, protegiendo la confidencialidad del tráfico.  
- Con **WPA3**, introducido junto a 802.11ax (Wi-Fi 6), se agregarían mejoras como autenticación más robusta (SAE) y protección frente a ataques de diccionario.  

Por lo tanto, aunque la red utiliza un estándar moderno en la capa física (802.11ac), la falta de seguridad en la configuración (Open) reduce considerablemente la protección de los usuarios.  

**Tabla comparativa de sistemas de seguridad en Wi-Fi:**

| Sistema de seguridad | Año de introducción | Características principales | Vulnerabilidades / Limitaciones |
|-----------------------|---------------------|-----------------------------|---------------------------------|
| **WEP (Wired Equivalent Privacy)** | 1997 (IEEE 802.11 original) | Primer intento de seguridad en Wi-Fi, basado en RC4 y claves estáticas. | Muy inseguro, fácilmente vulnerable a ataques de descifrado; obsoleto. |
| **WPA (Wi-Fi Protected Access)** | 2003 (transición) | Mejora sobre WEP con TKIP (Temporal Key Integrity Protocol). | Solo parche temporal; aún vulnerable a ataques modernos. |
| **WPA2** | 2004 (IEEE 802.11i) | Introduce AES-CCMP, más robusto que TKIP; ampliamente adoptado en la industria. | Vulnerable a ataques como KRACK; depende de configuraciones seguras. |
| **WPA3** | 2018 (Wi-Fi Alliance, compatible con IEEE 802.11ax) | Uso de SAE (Simultaneous Authentication of Equals), cifrado individualizado, mejor resistencia a ataques de diccionario. | Más seguro, pero algunos dispositivos antiguos no son compatibles. |

Tabla 2: Evolución de los sistemas de seguridad en redes Wi-Fi según IEEE 802.11 y Wi-Fi Alliance

### 3. Protocolos de comunicación y medios de transmisión
a. En el siguiente cuadro se puede visualizar los protocolos inalambricos mas comunes y se detalla aquellos que estan estadarizados:
| Protocolo    | ¿Está estandarizado? | Estándares|
|--------------|----------------------|-----------|
| Wi-Fi  | Si | IEEE 802.11 (última: IEEE 802.11ax, también llamado Wi-Fi 6/6E)|
| Bluetooth | Si |IEEE 802.15.1 (mantiene base, pero ahora gestionado por Bluetooth SIG – última versión Bluetooth 5.4) |
| ZigBee  | Si | IEEE 802.15.4 (última versión: ZigBee PRO 2023 basado en 802.15.4-2020) |
| NFC | Si | ISO/IEC 18092, ISO/IEC 14443, ISO/IEC 15693 (últimas actualizaciones en ISO/IEC 18092:2019)|
| LTE | Si | 3GPP Release 8 en adelante (última evolución: Release 17, LTE-Advanced Pro) |
| GSM | Si | ETSI/3GPP GSM 900/1800 (última versión: 3GPP TS 45 series, Release 17 – aunque en desuso)|
| 5G | Si | 3GPP Release 15 en adelante (última Release 17 en 2022, avanzando a Release 18/5G-Advanced) |
| LoRa | Si | LoRaWAN está estandarizado por LoRa Alliance (última versión: LoRaWAN 1.0.4 de 2020 y 1.1.1 en 2023) |
| NB-IoT | Si | 3GPP Release 13 en adelante (última Release 17) |
| SigFox | No | Tecnología propietaria de SigFox, no estandarizada por IEEE/3GPP |
| Z-Wave | Si | Estándar abierto gestionado por la Z-Wave Alliance bajo ITU-T G.9959 (última versión 2020)|

b. La relación Data rate vs Distancia se realizo mediante el script contenido en [data_rate_vs_distance](data_rate_vs_distance.ipynb):

![alt text](data_rate_vs_distance.png)

Figura 3.1: Relación Data Rate vs Distancia. Fuente Propia

De este gráfico se puede concluir lo siguiente:
- **Relación inversa entre alzance y data rate**: Los protocolos de alto throughput, como Wi-Fi, LTE o 5G, ofrecen velocidades muy altas pero con un alcance limitado, al contrario de los protocolos de largo alcance, como LoRa, SigFox, NB-IoT o  GSM, que sacrifican velocidad para poder transmitir a mayores distancias.
- **Protocolos de corto alcance y alta velocidad**: Wi-Fi y 5G son ideales para aplicaciones que requieren gran capacidad de transmisión como streaming, IoT de alto volumen, etc.
- **Protocolos de corto alcance y baja velocidad**: NFC se utiliza en aplicaciones de proximidad como pagos móviles o de identificación, mientras que Bluetooth, ZigBee y Z-Wave cubren un rango de decenas de metros y son útiles en redes personales.
- **Protocolos de largo alzance pero muy baja velocidad**: LoRa y SigFox llegan hasta decenas de km pero sus tasas son de apenas kbps o menos, por lo que su uso esta orientado a IoT masivo como sensores, telemetría, etc.
- **Protocolos celulares**: Se observa la evolución tecnológica en esta área:
  1. GSM tiene una baja velocidad pero largo alcance.
  2. LTE tiene mayor data rate y mantiene una distancia de varios km.
  3. 5G combina muy alta velocidad con cobertura urbana.

c. La siguiente tabla muestra las caracteristicas d elos sigueintes medios de transmisión:
| **Característica**                               | **UTP**                                                  | **Fibra Óptica**                                       | **Wi-Fi 802.11be (Wi-Fi 7)**                          | **Bluetooth 5.4**                                 | **5G**                                                     |
| ------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------- |
| **Ancho de banda**                               | Hasta 1–10 Gbps (Cat 5e/6/6a), hasta 40–100 Gbps (Cat 8) | Hasta 400 Gbps–1 Tbps                                  | Hasta 40 Gbps teóricos                                | Hasta 2 Mbps                                      | Hasta 10 Gbps (teórico, dependiendo de banda)              |
| **Distancias**                                   | Hasta 100 m                                              | Hasta decenas de km (monomodo), \~2 km multimodo       | \~10–100 m                                            | \~1–100 m                                         | \~1–10 km (dependiendo de despliegue y frecuencia)         |
| **Inmunidad a EMI / RFI**                        | Baja (susceptible a interferencias)                      | Muy alta (inmune, al ser luz)                          | Baja (susceptible a interferencias de radio)          | Baja (2.4 GHz congestionada)                      | Media/Alta (usa múltiples bandas y técnicas de mitigación) |
| **Costos de medios / conectores / dispositivos** | Bajo (cable económico, conectores RJ-45 baratos)         | Alto (fibra y transceptores más costosos)              | Medio (APs y tarjetas Wi-Fi son accesibles)           | Muy bajo (chipsets baratos, integrado en móviles) | Alto (infraestructura costosa, dispositivos más caros)     |
| **¿Disponible en Packet Tracer?**                | Sí                                                       | Sí (limitado, enlaces de fibra entre switches/routers) | Sí (APs inalámbricos 802.11ac/ax, aunque 11be aún no) | No                                                | No                                                         |

---

## Fuentes consultadas

- IEEE Standards Association – Project 802 Overview: https://standards.ieee.org/featured/ieee-802/  
- IEEE Standards Association – Ethernet 50th Anniversary (Historia de IEEE 802.3): https://standards.ieee.org/beyond-standards/ethernet-50th-anniversary/  
- IEEE Standards Association – The Evolution of Wi-Fi Technology and Standards: https://standards.ieee.org/beyond-standards/the-evolution-of-wi-fi-technology-and-standards/  
- IEEE 802.11be Project Page (Wi-Fi 7): https://standards.ieee.org/ieee/802.11be/7516/  
- IEEE.org Página principal: https://www.ieee.org  
