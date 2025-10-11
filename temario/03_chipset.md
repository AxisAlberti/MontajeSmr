---
layout: default
title: 📚 Chipset — Mantenimiento y Montaje de Equipos Informáticos
---



# Índice (TOC)

1. [Introducción](#introduccion)  
2. [¿Qué es un chipset?](#que-es-un-chipset)  
3. [Evolución histórica: Northbridge/Southbridge → PCH](#evolucion-historica)  
4. [Arquitectura general del chipset](#arquitectura-general)
   - [Enlace con la CPU (FSB, DMI, QPI/HT/IF)](#enlace-con-la-cpu)
   - [Hub interno y distribución de señales](#hub-interno)
   - [Relojes, temporización y latencias](#relojes-y-latencias)
5. [Compatibilidad de sockets y generaciones de CPU](#compatibilidad-de-sockets)
   - [Revisión de microcódigos y BIOS/UEFI](#microcodigos-y-uefi)
   - [Límites de TDP y soporte de características de la CPU](#limites-tdp)
6. [PCI Express](#pcie)
   - [Versión y retrocompatibilidad](#pcie-version)
   - [Reparto de líneas: CPU vs chipset](#pcie-reparto)
   - [Topologías típicas (x16, x8/x8, x4 para M.2, bifurcación)](#pcie-topologias)
7. [Almacenamiento](#almacenamiento)
   - [SATA (puertos, modos AHCI/RAID)](#sata)
   - [NVMe/M.2 (PCIe x4, bifurcación, disipación)](#nvme-m2)
   - [RAID/SRST, VMD y RAIDXpert (visión general)](#raid-y-vmd)
8. [Conectividad USB](#usb)
   - [Estándares (2.0/3.x/USB4) y velocidades](#usb-estandares)
   - [Tipo‑C, Alternate Mode y Power Delivery (PD)](#usb-tipo-c)
9. [Redes integradas](#redes)
   - [Ethernet (1/2.5/5/10 Gb)](#ethernet)
   - [Wi‑Fi/Bluetooth (CNVi/PCIe)](#wifi-bt)
10. [Audio y códecs integrados (ALC, S/PDIF, front panel)](#audio)
11. [Controladoras y E/S adicionales](#controladoras)
    - [Thunderbolt/USB4 (cuando procede)](#thunderbolt-usb4)
    - [Puertos legacy (SPI, UART, PS/2)](#puertos-legacy)
12. [Gestión de energía y térmicas](#energia-termicas)
    - [Estados C/P, ASPM y ahorro de energía](#aspm)
    - [VRM de placa y consideraciones térmicas del PCH](#vrm-pch)
13. [Overclock/Undervolt y límites de plataforma](#overclock-undervolt)
14. [Ejemplos de familias de chipsets (visión comparativa)](#familias-chipsets)
    - [Intel (series 300/400/500/600/700/800)](#intel-familias)
    - [AMD (AM4 y AM5: X670/B650 → X870/B850/B840)](#amd-familias)

---

<a id="introduccion"></a>
## 1. Introducción

El **chipset** es el “centro logístico” de la placa base: coordina el flujo de datos entre CPU, memoria, almacenamiento y periféricos. Determina **qué** puedes conectar (puertos disponibles) y **cómo de rápido** funcionará (versiones y anchos de banda). Elegir bien el chipset condiciona **vida útil**, **ampliaciones** y **estabilidad** del equipo. En plataformas modernas, la CPU asume funciones críticas (memoria y PCIe principal), mientras el chipset concentra **E/S** y servicios de **plataforma** (USB, SATA, audio, red, sensores, temporización, seguridad).

<a id="que-es-un-chipset"></a>
## 2. ¿Qué es un chipset?

Conjunto de controladores que integran la **lógica de plataforma**. En placas actuales suele ser un **único chip** (PCH en Intel; “chipset” o **Promontory** en AMD). Proporciona:
- **Líneas PCIe secundarias** (para M.2 y tarjetas), **USB** (hasta USB4 en gamas recientes), **SATA**, **audio**, **Ethernet**, **BT/Wi‑Fi** integrables, **firmware** (UEFI/BIOS), **TPM/fTPM**, **sensores**.
- Enlace de alta velocidad con la CPU (DMI/IF/QPI/HT), gestión de **relojes**, **energía** y **arranque**.

<a id="evolucion-historica"></a>
## 3. Evolución histórica: Northbridge/Southbridge → PCH

### 3.1. Arquitectura clásica (años 90–2000): Northbridge + Southbridge
Antes se usaban **dos chips**:
- **Northbridge (NB):** comunicado con la CPU por **FSB**; alojaba el **controlador de memoria** y el **bus gráfico** (AGP y, posteriormente, el primer PCIe x16).  
- **Southbridge (SB):** enlazado al NB; gestionaba **almacenamiento** (IDE→SATA), **USB**, **PCI/PCIe secundarios**, **audio**, **red**, **RTC**, **puertos legacy** (PS/2, serie, paralelo), **BIOS**, sensores.

```
CPU  <== FSB ==>  Northbridge  <== enlace interno ==>  Southbridge
 |                    |   \
 |                    |    \__ AGP / PCIe x16 (gráfica)
 |                    \__ Controlador de memoria (RAM)
```

**Implicaciones didácticas:**
- El **rendimiento de la RAM** dependía del **NB**; cada salto de CPU/RAM exigía un NB nuevo.
- La **GPU** se conectaba al NB para minimizar latencia con la CPU.
- La **E/S** “lenta y media” recaía en el **SB** (discos, USB, PCI), con más latencia.

### 3.2. Transición: integración en CPU y enlaces punto a punto
Con nuevas arquitecturas:
- El **controlador de memoria** se **integró en la CPU** (primero en AMD de escritorio, luego generalizado).
- El **FSB** se reemplazó por enlaces **punto‑a‑punto** de alta velocidad (QPI/DMI en Intel; HyperTransport/Infinity Fabric en AMD).
- La CPU asumió el **PCIe principal** (para GPU/M.2 rápidos); el NB perdió protagonismo.

### 3.3. Modelo moderno: PCH (Platform Controller Hub)
- La **CPU** integra: controlador de **memoria** y **líneas PCIe** principales (x16 para GPU, x4/x8 para M.2 rápidos), además de funciones de **seguridad** y aceleradores.
- El **PCH/chipset** aporta: **PCIe secundarios**, **USB**, **SATA**, **audio**, **Ethernet**, **firmware**, **TPM/fTPM**, **sensorística**; se comunica con la CPU por **DMI/IF**.

```
RAM <——> CPU  <== enlace de plataforma (DMI/IF) ==>  PCH (chipset)
         |  \_______________________________  USB, SATA, PCIe secundarios,
         \— PCIe CPU (GPU/M.2 rápidos)       audio, LAN, sensores, firmware…
```

### 3.4. ¿Por qué cambió?
- **Menos latencia, más rendimiento:** memoria y PCIe principal en la **CPU**.
- **Eficiencia energética/térmica:** menos saltos de chips → menos consumo/calor.
- **Escalabilidad:** enlaces punto‑a‑punto y asignación flexible de **PCIe**.
- **Simplificación de plataforma** y mayor **fiabilidad**.

> **Actividad de aula:** pide al alumnado que identifique, en fotos de placas antiguas, el NB (suele llevar disipador junto al zócalo y AGP) y el SB (cerca de conectores SATA/PCI). Luego comparar con una placa AM5/Intel reciente donde el “chipset” es un único PCH.

<a id="arquitectura-general"></a>
## 4. Arquitectura general del chipset

El chipset moderno funciona como **hub** de E/S:
- **Switching PCIe** hacia ranuras x1/x4 y M.2 secundarios.
- **Controladoras** USB 2.0/3.x/USB4, **SATA** para HDD/SSD, **audio** HD, **Ethernet** (MAC/PHY según placa), buses **SPI/I²C/UART** para firmware y sensores.
- **Relojería** (clocking) y **gestión de energía** (Estados C/P, ASPM) coordinadas con la CPU.

<a id="enlace-con-la-cpu"></a>
### 4.1. Enlace con la CPU (FSB, DMI, QPI/HT/IF)
- **Ayer:** **FSB** compartido (CPU↔NB).  
- **Hoy:** **DMI** (Intel) o **Infinity Fabric/HT** (AMD) como enlaces **punto‑a‑punto** dedicados, con varias **líneas** y **generaciones** (ej.: DMI 4.0 x8 en plataformas Intel 700).

<a id="hub-interno"></a>
### 4.2. Hub interno y distribución de señales
Multiplexa líneas **PCIe** y controla el **ancho de banda agregado** hacia la CPU por el enlace de plataforma. La placa decide cómo repartir las **líneas físicas** entre ranuras y M.2.

<a id="relojes-y-latencias"></a>
### 4.3. Relojes, temporización y latencias
Gestiona **relojes** de alta precisión y políticas de ahorro (ASPM, estados D), que influyen en **latencia** y **consumo**. Un mal ajuste puede provocar **throttling** o inestabilidad.

<a id="compatibilidad-de-sockets"></a>
## 5. Compatibilidad de sockets y generaciones de CPU

El chipset y el **socket** determinan qué **familias de CPU** puedes usar. Además, la **UEFI/BIOS** debe incluir **microcódigos** compatibles con la CPU para que arranque.

<a id="microcodigos-y-uefi"></a>
### 5.1. Revisión de microcódigos y BIOS/UEFI
Actualizaciones de UEFI aportan **soporte de nuevas CPUs**, arreglos de **estabilidad** y mejoras de **memoria** (XMP/EXPO).

<a id="limites-tdp"></a>
### 5.2. Límites de TDP y soporte de características de la CPU
Aunque la CPU encaje, la **alimentación (VRM)** y el **firmware** de la placa marcan límites (p. ej., curvas de potencia, opciones de overclock/undervolt).

<a id="pcie"></a>
## 6. PCI Express

<a id="pcie-version"></a>
### 6.1. Versión y retrocompatibilidad
PCIe es **retrocompatible** por versión y ancho de enlace. La **versión** (3.0/4.0/5.0/…) afecta al **rendimiento por carril**; el **ancho** (x1/x4/x8/x16) define el caudal total.

<a id="pcie-reparto"></a>
### 6.2. Reparto de líneas: CPU vs chipset
- **CPU:** líneas rápidas (normalmente x16 para GPU + x4/x8 para M.2 de altas prestaciones).  
- **Chipset:** líneas adicionales (x1/x2/x4) para M.2 extra, NICs, capturadoras, etc. Todo ese tráfico **compite** por el enlace CPU↔PCH.

<a id="pcie-topologias"></a>
### 6.3. Topologías típicas (x16, x8/x8, x4 para M.2, bifurcación)
- Bifurcación del x16 de la CPU en **x8/x8** (SLI/CrossFire antiguos) o **x8/x4/x4** para combinar **GPU + 2×M.2**.
- En chipsets con **USB4/Thunderbolt**, parte del ancho proviene de PCIe internos y PHYs dedicados.

<a id="almacenamiento"></a>
## 7. Almacenamiento

<a id="sata"></a>
### 7.1. SATA (puertos, modos AHCI/RAID)
Aún útil para HDD/SSD 2,5", pero limitado por **6 Gb/s** en SATA 3.0. Muchos chipsets ofrecen **RAID** por firmware.

<a id="nvme-m2"></a>
### 7.2. NVMe/M.2 (PCIe x4, bifurcación, disipación)
Los **NVMe** M.2 enlazados a la **CPU** rinden más (menos latencia) que los colgados del **chipset**. Requieren **disipación** por su densidad térmica.

<a id="raid-y-vmd"></a>
### 7.3. RAID/SRST, VMD y RAIDXpert (visión general)
- **Intel RST/VMD**: gestión avanzada de NVMe/RAID vía firmware/driver.  
- **AMD RAIDXpert**: solución análoga en plataformas AMD.

<a id="usb"></a>
## 8. Conectividad USB

<a id="usb-estandares"></a>
### 8.1. Estándares (2.0/3.x/USB4) y velocidades
- **USB 3.x** (5/10/20 Gb/s).  
- **USB4** reutiliza tecnología Thunderbolt para alcanzar **40 Gb/s** o más, con compatibilidad DP Alt Mode.

<a id="usb-tipo-c"></a>
### 8.2. Tipo‑C, Alternate Mode y Power Delivery (PD)
Type‑C permite **PD** (carga rápida) y **video** por **Alt Mode**; el soporte real depende del **controlador** y el **cableado** de la placa.

<a id="redes"></a>
## 9. Redes integradas

<a id="ethernet"></a>
### 9.1. Ethernet (1/2.5/5/10 Gb)
Cada vez más común **2.5GBASE‑T** nativo. En gamas altas aparecen **5/10 GbE** vía controladoras PCIe adicionales.

<a id="wifi-bt"></a>
### 9.2. Wi‑Fi/Bluetooth (CNVi/PCIe)
Módulos **M.2 Key E** (Intel/Realtek/Qualcomm) o soluciones **CNVi**/RFFE integradas según plataforma y placa.

<a id="audio"></a>
## 10. Audio y códecs integrados (ALC, S/PDIF, front panel)
Códecs **Realtek ALC** y similares, con soporte para **S/PDIF**, **jack frontales** y mejoras por **opamps**/aislamiento PCB en placas gaming/creator.

<a id="controladoras"></a>
## 11. Controladoras y E/S adicionales

<a id="thunderbolt-usb4"></a>
### 11.1. Thunderbolt/USB4 (cuando procede)
Algunas placas integran **USB4**/Thunderbolt (controladoras dedicadas + redriver/retimer).

<a id="puertos-legacy"></a>
### 11.2. Puertos legacy (SPI, UART, PS/2)
Aún presentes en placas orientadas a **empresa/industria** y para compatibilidad.

<a id="energia-termicas"></a>
## 12. Gestión de energía y térmicas

<a id="aspm"></a>
### 12.1. Estados C/P, ASPM y ahorro de energía
El chipset negocia **ASPM** y estados **D** de dispositivos. Afecta a consumo y latencia.

<a id="vrm-pch"></a>
### 12.2. VRM de placa y consideraciones térmicas del PCH
El **PCH** suele estar bajo un **disipador**; en placas con **USB4/PCIe 5** puede calentarse más. La calidad del **VRM** condiciona estabilidad.

<a id="overclock-undervolt"></a>
## 13. Overclock/Undervolt y límites de plataforma
Las opciones dependen de **CPU + chipset + UEFI**. En Intel serie Z es donde hay más control; en AMD, gamas **X8xx/B8xx** ofrecen OC de memoria/IF.

<a id="familias-chipsets"></a>
## 14. Ejemplos de familias de chipsets (visión comparativa)

<a id="intel-familias"></a>
### 14.1. Intel (series 300/400/500/600/700/800)
- **700 (Z790/B760/H770, etc.)**: enlace **DMI 4.0** (hasta x8), hasta **~28 líneas PCIe** en PCH, combinación **PCIe 4.0/3.0**, SATA y abundante USB.  
- **800 (Z890/H870/B860, etc.)** para **Arrow Lake**/**Core Ultra** de sobremesa: mayor integración, mejoras en **DMI** y asignación de **PCIe** en PCH, y soporte de nuevas funciones de plataforma (según placa).  
- Notas comunes: la **CPU** aporta PCIe para **GPU** y NVMe rápidos; el **PCH** añade puertos y líneas secundarias. Consulta siempre el **manual** de la placa para el reparto exacto.

<a id="amd-familias"></a>
### 14.2. AMD (AM4 y AM5: X670/B650 → X870/B850/B840)
- **AM4 (X570/B550, etc.)**: PCIe 4.0 generalizado en gamas X570; B550 con mezcla CPU‑PCIe 4 + PCH‑PCIe 3.  
- **AM5 600‑series (X670/X670E, B650/B650E, A620)**: salto a **DDR5** y **PCIe 5** (en “E” para GPU/SSD).  
- **AM5 800‑series (X870E/X870/B850/B840)**: estandarizan **DDR5**, empujan **USB4** en más modelos y consolidan **PCIe 5** (sobre todo para NVMe, y en **X870E** también para GPU). Cambios de segmentación frente a B650 (algunos B850 desactivan PCIe 5 x16 para GPU).

---

### Apéndice A — Actividades y evaluación sugeridas
1. **Identifica** NB y SB en una foto de placa (Pentium 4/Athlon XP).  
2. **Dibuja** el flujo de datos CPU↔NB↔SB vs. CPU↔PCH y **compara latencias** teóricas.  
3. **Mapa PCIe real**: elabora el diagrama de una placa AM5 reciente, indicando qué M.2 cuelga de CPU y de chipset.  
4. **Caso práctico**: ¿qué ocurre si saturas USB4 + 2×NVMe del chipset? Comenta el **cuello** en el enlace CPU↔PCH.

---

> **Nota**: La oferta exacta (USB4, nº de M.2, LAN 2.5/5/10 Gb) **depende de cada placa**. Revisa siempre el diagrama de bloques del fabricante.

