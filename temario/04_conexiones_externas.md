---
layout: default
title: 📚 Mantenimiento y Montaje de Equipos Informáticos
---
## TEMA 4. CONECTORES EXTERNOS.

- [1. Vocabulario](#1-vocabulario)
- [2. Conceptos básicos: qué es un *header* y qué aporta](#2-conceptos-básicos-qué-es-un-header-y-qué-aporta)
- [3. USB en placa: headers y funcionamiento](#3-usb-en-placa-headers-y-funcionamiento)
  - [3.1 Recordatorio rápido: cómo funciona USB](#31-recordatorio-rápido-cómo-funciona-usb)
  - [3.2 Header **USB 2.0 (9 pines, 2×5 con guía)**](#32-header-usb-20-9-pines-25-con-guía)
  - [3.3 Header **USB 3.x (IDC 19/20 pines)** para 2× USB‑A frontales](#33-header-usb-3x-idc-1920-pines-para-2×-usb‑a-frontales)
  - [3.4 Header **Type‑E (Key‑A/Key‑B) de 20 pines** para **USB‑C** frontal](#34-header-type‑e-key‑akey‑b-de-20-pines-para-usb‑c-frontal)
  - [3.5 **USB Power Delivery (PD)** en puertos frontales](#35-usb-power-delivery-pd-en-puertos-frontales)
  - [3.6 Longitud de cableado interno y *signal integrity*](#36-longitud-de-cableado-interno-y-signal-integrity)
- [4. Audio frontal: header **HD Audio/AAFP**](#4-audio-frontal-header-hd-audioaafp)
  - [4.1 Para qué sirve](#41-para-qué-sirve)
  - [4.2 Cómo funciona (detección de jack, muteo y rutas)](#42-cómo-funciona-detección-de-jack-muteo-y-rutas)
  - [4.3 Pinout típico 10‑1 y recomendaciones de montaje](#43-pinout-típico-10‑1-y-recomendaciones-de-montaje)
- [5. **Front Panel** (F_PANEL/SYS_PANEL): botones y LEDs del chasis](#5-front-panel-f_panelsys_panel-botones-y-leds-del-chasis)
  - [5.1 Para qué sirve](#51-para-qué-sirve)
  - [5.2 Cómo funciona (lógica, EC/PCH y polaridad)](#52-cómo-funciona-lógica-ecpch-y-polaridad)
  - [5.3 Identificación del pin 1 y orden típico](#53-identificación-del-pin-1-y-orden-típico)
- [6. **COM** (serial RS‑232) en header interno](#6-com-serial-rs‑232-en-header-interno)
  - [6.1 Para qué sirve](#61-para-qué-sirve)
  - [6.2 Cómo funciona y niveles eléctricos](#62-cómo-funciona-y-niveles-eléctricos)
  - [6.3 Pinout común (2×5, 9 pines activos) y correspondencia DB‑9](#63-pinout-común-2×5-9-pines-activos-y-correspondencia-db‑9)
  - [6.4 Cableado **recto** vs **null‑modem** y *handshaking*](#64-cableado-recto-vs-nullmodem-y-handshaking)
- [7. **LPT/Parallel** (legado) en header 26 pines](#7-lptparallel-legado-en-header-26-pines)
  - [7.1 Para qué sirve hoy](#71-para-qué-sirve-hoy)
  - [7.2 Cómo funciona (registros y líneas de control)](#72-cómo-funciona-registros-y-líneas-de-control)
- [8. **Thunderbolt/USB4 headers** para tarjetas AIC](#8-thunderboltusb4-headers-para-tarjetas-aic)
  - [8.1 Para qué sirven](#81-para-qué-sirven)
  - [8.2 Cómo funcionan (no son USB de datos)](#82-cómo-funcionan-no-son-usb-de-datos)
  - [8.3 USB4 v2.0 y requisitos prácticos](#83-usb4-v20-y-requisitos-prácticos)
- [9. Otros headers que exponen funciones al exterior](#9-otros-headers-que-exponen-funciones-al-exterior)
  - [9.1 **UART debug** (TTL) y *service headers*](#91-uart-debug-ttl-y-service-headers)
  - [9.2 **Conectores de alimentación auxiliar** para USB‑C PD alto](#92-conectores-de-alimentación-auxiliar-para-usb‑c-pd-alto)
- [10. Procedimiento de montaje y verificación](#10-procedimiento-de-montaje-y-verificación)
- [11. Diagnóstico de fallos frecuentes](#11-diagnóstico-de-fallos-frecuentes)

---

## 1. Vocabulario

| Término                | Definición                                                                                         |
|------------------------|----------------------------------------------------------------------------------------------------|
| Header                 | Bloque de pines en placa que expone señales a un módulo externo (frontal o bracket).              |
| Pin 1                  | Primer pin de un header, señalado por triángulo/pad cuadrado/serigrafía.                          |
| Clave/Key              | Posición sin pin o muesca que evita conectar al revés.                                            |
| SuperSpeed             | Familia de velocidades USB 3.x (5/10/20 Gb/s).                                                    |
| Type‑E                 | Conector interno diseñado para llevar USB‑C (o USB‑A) al frontal preservando señal de alta velocidad.  |
| AAFP / HD Audio        | Header de audio frontal con detección de jack y retornos de sense.                                |
| F_PANEL                | Header de botones/LEDs del chasis (Power, Reset, HDD LED, Power LED, Speaker).                    |
| AIC (Add‑In Card)      | Tarjeta PCIe adicional (p. ej., Thunderbolt/USB4) que requiere un header de control.              |
| PD (Power Delivery)    | Protocolo de negociación de potencia sobre USB‑C.                                                 |
| Retimer/Redriver       | Chips para regenerar/amplificar señales de alta velocidad.                                        |
| RS‑232 / UART TTL      | Serie “clásica” a ±V (RS‑232) frente a lógica 3,3/5 V (TTL); no son compatibles directos.         |

---

## 2. Conceptos básicos: qué es un *header* y qué aporta
Un **header** es un conjunto de **pines** en la placa base que permite llevar **señales y alimentación** hacia el **frontal del chasis** o a **brackets** que salen al exterior (sin usar el panel trasero). Suelen estar:
- **Claveados** (pin ausente o carcasa con muesca) para evitar inversión.
- **Serigrafiados** con nombres como *F_USB1*, *AAFP*, *F_PANEL*, *COM1*, *TB_HEADER*…
- Con **pin 1** marcado (triángulo, pad cuadrado o serigrafía).

**Funcionamiento general**: el header actúa como **punto de transición** entre el PCB de la placa y el **cableado** hacia el exterior. En enlaces de **alta velocidad** (USB 3.x/USB4), su diseño conserva **impedancia** y **apantallado**; en enlaces **analógicos** (audio) gestiona **masas** y **retornos** para minimizar ruido; en **control** (F_PANEL) expone **entradas/salidas** de la PCH/EC.

---

## 3. USB en placa: headers y funcionamiento

### 3.1 Recordatorio rápido: cómo funciona USB
- **USB** (Universal Serial Bus) es un estándar de conexión para la transmisión de datos y energía entre computadoras y periféricos. Su propósito es simplificar la conectividad y sustituir diversos puertos antiguos por uno universal, facilitando el intercambio y alimentación de dispositivos.
- **Topología**: **host** (PC) → **hubs** → **dispositivos** (árbol). El host **planifica** el bus.

## Tabla comparativa de versiones USB

| Versión USB      | Año de lanzamiento | Velocidad máxima teórica | Nombre comercial      | Retrocompatible | Características principales                 |
|------------------|-------------------|-------------------------|----------------------|-----------------|---------------------------------------------|
| USB 1.0/1.1      | 1996 / 1998       | 12 Mbps (Full Speed)    | USB Full Speed       | Sí              | Simplifica conexiones, reemplaza legacy     |
| USB 2.0          | 2000              | 480 Mbps (High Speed)   | USB High Speed       | Sí              | Muy extendida, mejora energía y velocidad   |
| USB 3.0          | 2008              | 5 Gbps (SuperSpeed)     | USB 3.1 Gen 1        | Sí              | Más potencia eléctrica, cable azul          |
| USB 3.1 Gen 2    | 2013              | 10 Gbps (SuperSpeed+)   | USB SuperSpeed+      | Sí              | Doble velocidad, mejor gestión de energía   |
| USB 3.2          | 2017              | 20 Gbps (SuperSpeed+)   | USB 3.2 Gen 2x2      | Sí              | Multiplica líneas en USB‑C, todavía cable azul/turquesa |
| USB4             | 2019              | 40 Gbps                 | USB4                 | Parcialmente    | Basado en Thunderbolt 3, requiere USB‑C     |

> Las velocidades son máximas teóricas y dependen del cable y dispositivo.
> USB4 solo funciona con conector USB‑C y permite multitarea y mejor gestión de energía.

### 3.2 Header **USB 2.0 (9 pines, 2×5 con guía)**
**Para qué sirve**: hasta **2 puertos USB 2.0** (dos USB‑A frontales o un USB interno + lector).  
**Cómo funciona (detalle)**:
- Cada puerto usa **VBUS (5 V)** con protección de **sobre‑corriente**, par **D+/D−** (diferencial) y **GND**.  
- La **guía** (pin ausente) evita inversión; el pinout divide el header en **Puerto 1** y **Puerto 2**.  
- La placa puede **deshabilitar** un puerto tras eventos OC# o en suspensión S3/S5.

### 3.3 Header **USB 3.x (IDC 19/20 pines)** para 2× USB‑A frontales
**Para qué sirve**: **dos puertos** frontales **SuperSpeed**.  
**Cómo funciona (detalle)**:
- Integra **pares diferenciales SuperSpeed** **TX/RX** por puerto y, además, las líneas **USB 2.0** (D+/D−) para compatibilidad.  
- Añade señal de **Over‑Current (OC#)** y líneas de **detect** para presencia del módulo.  
- Requiere **cableado blindado** de baja pérdida entre header y módulo frontal.

### 3.4 Header **Type‑E (Key‑A/Key‑B) de 20 pines** para **USB‑C** frontal
**Para qué sirve**: llevar **USB‑C** al frontal preservando integridad de señal.  
**Funcionamiento**:
- **Key‑A** normalmente alimenta **1× USB‑C** (SS 10 Gb/s; algunas placas ofrecen **20 Gb/s** Gen 2×2).  
- **Key‑B** expone **2× USB‑A** (no USB‑C).  
- El conector **blindado** y el cable **de impedancia controlada** minimizan pérdidas y **diafonía**.

**Aclaración**: **Type‑C ≠ USB4**. Para USB4/Alt Modes (DisplayPort/TB), la placa debe incluir **controlador** y, a menudo, **retimers**; si no, el Type‑C frontal será solo USB 3.x/2.0.

### 3.5 **USB Power Delivery (PD)** en puertos frontales
**Conceptos clave**:
- En USB‑C sin PD, las resistencias **Rp/Rd** en **CC1/CC2** anuncian **corriente** disponible (Default/1,5 A/3 A a 5 V).
- Con **PD 3.0/3.1**, *Source* y *Sink* negocian **PDOs** (Power Data Objects): **tensión** (5/9/15/20/28/36/48 V) y **corriente**.  
- **EPR** (Extended Power Range) permite hasta **240 W** (48 V×5 A) con **cable E‑Marker** adecuado.

**En la práctica en placas**:
- Algunas incluyen **alimentación auxiliar** (p. ej. conector PCIe 6‑pin en la placa) para sostener **60–140 W** en el **Type‑C frontal**.  
- El módulo de la caja puede incorporar **controlador PD**; otros dependen del **controlador de la placa**.

### 3.6 Longitud de cableado interno y *signal integrity*
- Mantén los latiguillos **cortos**, **apantallados**, con **radio de curvatura** generoso.  
- Evita **extensores** sin **redriver/retimer** a 10–20 Gb/s.  
- Asegura **masa de chasis** y **tornillería** para reducir EMI.

---

## 4. Audio frontal: header **HD Audio/AAFP**

### 4.1 Para qué sirve
Lleva **micrófono** y **auriculares** al frontal con **detección de jack** y **conmutación** entre salidas frontal/trasera.

### 4.2 Cómo funciona (detección de jack, muteo y rutas)
- El códec (Realtek/otros) usa **PRESENCE#** y líneas **SENSE_SEND/RETURN** para saber si hay **módulo** y **jack insertado**.  
- Al detectar inserción, el driver puede **mutear** trasera, **redirigir** flujo a frontal o **duplicar** (según ajuste).  
- Señales de audio salen **AC‑acopladas** (condensadores) y con cuidado de **masas** para reducir **hum**.  
- Algunos códecs detectan **impedancia** de auriculares y ajustan **ganancia**.

### 4.3 Pinout típico 10‑1 y recomendaciones de montaje
| Pin | Señal | Función |
|---|---|---|
| 1 | MIC_L / PORT1L | Micrófono L (o mono) |
| 2 | GND | Tierra analógica |
| 3 | MIC_R / MIC_BIAS | Micrófono R o polarización |
| 4 | PRESENCE# / control | Detección de módulo |
| 5 | HP_R / FPOUT_R | Auriculares R |
| 6 | SENSE_R / RETURN_R | Retorno/detección R |
| 7 | SENSE_SEND | Línea de sensado |
| 8 | KEY (sin pin) | Clave mecánica |
| 9 | HP_L / FPOUT_L | Auriculares L |
| 10 | SENSE_L / RETURN_L | Retorno/detección L |

**Buenas prácticas**: usar el cable **HD Audio** (no AC’97), rutear lejos de VRM y cables de alta corriente, fijar el conector sin tensión.

---

## 5. **Front Panel** (F_PANEL/SYS_PANEL): botones y LEDs del chasis

### 5.1 Para qué sirve
Conectar **PWR SW**, **RESET SW**, **HDD LED**, **PWR LED**, **SPEAKER** (beeper) y, a veces, **CHASSIS INTRUSION** al sistema.

### 5.2 Cómo funciona (lógica, EC/PCH y polaridad)
- **PWRBTN#** y **RESET#** se leen por el **EC** (Embedded Controller) o la **PCH**; un pulso corto ordena **S0↔S5** o **reset**.  
- **Debounce** por hardware/firmware evita rebotes.  
- **LEDs**: respetan **polaridad**; si no lucen, invertir. **HDD LED** suele parpadear por actividad SATA/NVMe vía señal del chipset.

### 5.3 Identificación del pin 1 y orden típico
- Header **2×5** con **pin 10** a veces ausente (clave).  
- El **pin 1** se marca con triángulo/pad cuadrado; consulta el **manual** para el mapeo exacto (varía por fabricante/modelo).

---

## 6. **COM** (serial RS‑232) en header interno

### 6.1 Para qué sirve
Exponer **DB‑9** en un **bracket** para equipos industriales, consolas serie, UPS, CNC, routers, etc.

### 6.2 Cómo funciona y niveles eléctricos
- En placas con **Super I/O**, el header entrega **RS‑232** a ±3–15 V (no TTL).  
- Velocidades típicas **9600–115200 baudios** (8N1).  
- Señales de ***handshake*** (RTS/CTS, DTR/DSR) permiten control de flujo por hardware.

### 6.3 Pinout común (2×5, 9 pines activos) y correspondencia DB‑9
| Pin header | Señal RS‑232 | DB‑9 | Descripción |
|---:|---|---:|---|
| 1 | DCD | 1 | Carrier Detect |
| 2 | RXD | 2 | Recibir |
| 3 | TXD | 3 | Transmitir |
| 4 | DTR | 4 | Data Terminal Ready |
| 5 | GND | 5 | Tierra |
| 6 | DSR | 6 | Data Set Ready |
| 7 | RTS | 7 | Request to Send |
| 8 | CTS | 8 | Clear to Send |
| 9 | RI  | 9 | Ring Indicator |
| 10 | KEY (sin pin) | — | Clave/ausente |

### 6.4 Cableado **recto** vs **null‑modem** y *handshaking*
- **Recto**: PC ↔ equipo DCE (p. ej., módem).  
- **Null‑modem**: PC ↔ PC (cruza TX/RX y líneas de control).  
- Si hay **desbordes**, activa **RTS/CTS** o usa **XON/XOFF** (software).

---

## 7. **LPT/Parallel** (legado) en header 26 pines

### 7.1 Para qué sirve hoy
Entornos industriales/legado: impresoras antiguas, instrumentación, PLC. Se saca a **DB‑25** mediante **bracket**.

### 7.2 Cómo funciona (registros y líneas de control)
- Tres registros clásicos: **DATA (8 bits)**, **STATUS** y **CONTROL**.  
- Líneas **STROBE**, **BUSY**, **ACK**, **AUTOFEED**, **INIT**, **SELECTIN** coordinan la transferencia.  
- El header suele ser **2×13** con clave; usa cable plano apantallado.

---

## 8. **Thunderbolt/USB4 headers** para tarjetas AIC

### 8.1 Para qué sirven
Sincronizar/controlar una **AIC Thunderbolt/USB4**. El header (**TB_HEADER/USB4_HEADER**) **no** lleva datos USB: expone **GPIO/sideband** (p. ej., **FORCE_PWR**, **WAKE#**, señales de seguridad/permiso).

### 8.2 Cómo funcionan (no son USB de datos)
- La AIC se inserta en **PCIe** y puede enlazar **DisplayPort** desde la GPU para *Alt Mode*.  
- El header establece **presencia**, **alimentación forzada**, **wake** y estados S3/S4; sin AIC, el header **no habilita** USB4 por sí solo.

### 8.3 USB4 v2.0 y requisitos prácticos
- Hasta **80 Gb/s** (simétrico) o **120/40** (asimétrico, PAM3).  
- Requiere **cables** y **retimers** de alta calidad; longitudes internas **mínimas**.

---

## 9. Otros headers que exponen funciones al exterior

### 9.1 **UART debug** (TTL) y *service headers*
- Consola de servicio a **3,3 V**; conectar mediante **adaptador USB‑TTL** (no RS‑232 directo).  
- Útil para diagnóstico/recuperación en placas industriales/ITX.

### 9.2 **Conectores de alimentación auxiliar** para USB‑C PD alto
- Algunas placas añaden **PCIe 6‑pin/Molex** en placa para sostener **60–140 W** en el **Type‑C frontal**.  
- Verifica **calibre del cable**, **protecciones** y **límites** del manual.

---

## 10. Procedimiento de montaje y verificación

1. **Planifica**: identifica *F_USB*, *TYPE‑E*, *AAFP*, *F_PANEL*, *COM*, *LPT*, *TB_HEADER*.  
2. **Orientación**: localiza **pin 1** o **clave** en header y conector.  
3. **Conecta** sin forzar; si no entra, revisa **orientación**.  
4. **Asegura** los cables (bridas/guías) sin tensiones ni dobleces cerradas.  
5. **Pruebas**:
   - **USB**: pendrive 2.0 y SSD/pendrive 3.x para validar HS y SuperSpeed; *benchmark*.
   - **PD**: wattímetro USB‑C; verifica que el cable admite la potencia.
   - **Audio**: mic y cascos; prueba **jack‑detect** y niveles.  
   - **F_PANEL**: encendido/reset/LEDs (invierte si no lucen).  
   - **COM**: terminal 115200 8N1; verifica **RTS/CTS** si procede.  
   - **LPT**: *loopback* o impresión de prueba (si aplica).  
   - **TB/USB4**: presencia de la AIC, *firmware* y *pass‑through* DP.

---

## 11. Diagnóstico de fallos frecuentes

- **USB frontal lento/no detecta SuperSpeed**: cable Type‑E incorrecto, conectado a header **Gen 1**; ruta larga; falta **retimer**; interferencias/masa floja.  
- **USB‑C frontal sin PD/altos W**: falta **alimentación auxiliar** o cable no **E‑Marker**; límite de la placa.
- **Sin audio frontal**: conector **AC’97** en vez de **HD Audio**; jack‑detect desactivado; masa mal rutada.  
- **LED HDD no enciende**: polaridad invertida o mapeo distinto al manual.  
- **COM mudo**: confusión **RS‑232 vs TTL**; BIOS deshabilitado; necesitabas **null‑modem**.  
- **TB/USB4 sin funcionar**: no hay **AIC** instalada, falta cable **DP in**, *drivers/firmware* desactualizados.


