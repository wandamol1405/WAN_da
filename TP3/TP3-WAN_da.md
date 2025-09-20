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

## Introduccion

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



## Fuentes consultadas

- IEEE Standards Association – Project 802 Overview: https://standards.ieee.org/featured/ieee-802/  
- IEEE Standards Association – Ethernet 50th Anniversary (Historia de IEEE 802.3): https://standards.ieee.org/beyond-standards/ethernet-50th-anniversary/  
- IEEE Standards Association – The Evolution of Wi-Fi Technology and Standards: https://standards.ieee.org/beyond-standards/the-evolution-of-wi-fi-technology-and-standards/  
- IEEE 802.11be Project Page (Wi-Fi 7): https://standards.ieee.org/ieee/802.11be/7516/  
- IEEE.org Página principal: https://www.ieee.org  
