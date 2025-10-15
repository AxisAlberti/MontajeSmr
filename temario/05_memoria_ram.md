---
layout: default
title: Memoria DDR
nav_order: 7
---

# Memoria DDR

La **memoria DDR** es la tecnología dominante de **DRAM** que se usa como **memoria principal** en PC y servidores. Se llama *Double Data Rate* porque **transfiere datos en los dos flancos del reloj** (subida y bajada), duplicando la tasa efectiva. Su misión es ofrecer un **espacio de trabajo** de baja latencia y alto ancho de banda entre la CPU (y su jerarquía de cachés) y el almacenamiento masivo (SSD/HDD).

> **Tabla — Vocabulario Fundamental**

| Término | Definición |
|---|---|
| **DDR (Double Data Rate)** | Familia de DRAM síncrona que transmite datos en ambos flancos del reloj para duplicar la tasa efectiva (MT/s). |
| **DDR2 / DDR3 / DDR4 / DDR5** | Generaciones con cambios en voltaje, prefetch, topología y señalización; **incompatibles** entre sí a nivel físico/eléctrico. |
| **Prefetch (2n/4n/8n/16n)** | Bits leídos internamente por acceso y puestos en cola hacia el bus externo; crece con cada generación para elevar el rendimiento. |
| **MT/s** | Mega-transferencias por segundo (tasa efectiva de DDR). Ej.: *DDR4-3200* = 3200 MT/s. |
| **Frecuencia (MHz)** | Reloj base de la DRAM/IMC; en DDR, **MT/s = 2 × MHz**. |
| **Burst Length (BL)** | Tamaño de ráfaga por operación de datos (BL8 típico en DDR3/4; BL16 en DDR5). |
| **Bank / Bank Group** | Particiones internas que permiten paralelismo; los *bank groups* reducen contención entre accesos. |
| **Canal de memoria** | Camino de 64-bit entre la controladora y la RAM; doble/quad canal multiplica el ancho de banda. |
| **Subcanal (DDR5)** | División lógica de cada DIMM en **2×32-bit**, mejorando eficiencia y concurrencia. |
| **Rank (SR/DR/QR)** | Conjunto lógico de chips direccionados como unidad en un DIMM; afecta interleaving y compatibilidad. |
| **Timings (CL-tRCD-tRP-tRAS)** | Latencias internas (en ciclos) que gobiernan apertura, lectura, pre-carga y cierre de filas. |
| **CL (CAS Latency)** | Ciclos desde la orden de lectura hasta llegar el primer dato. |
| **SPD** | EEPROM del módulo con parámetros JEDEC y perfiles de fabricante leídos por UEFI/BIOS. |
| **XMP / EXPO** | Perfiles (Intel/AMD) con frecuencia/timings/voltaje validados por el fabricante del kit. |
| **ECC (de sistema)** | Detección/corrección de errores a nivel de DIMM/IMC (p. ej., SECDED); requiere CPU+placa+módulos compatibles. |
| **On-die ECC (DDR5)** | Corrección **interna al chip DRAM**; no sustituye el ECC de sistema. |
| **UDIMM / RDIMM / LRDIMM** | Módulos sin registro / con registro / con búfer de carga reducida; RDIMM/LRDIMM predominan en servidores. |

---

## Índice
- [0. **Definición y Visión General (Memoria DDR)**](#0-definición-y-visión-general-memoria-ddr)
- [1. **Estructura y Funcionamiento (bancos, filas/columnas, prefetch, bursts)**](#1-estructura-y-funcionamiento-bancos-filascolumnas-prefetch-bursts)
- [2. **Generaciones DDR (de DDR a DDR5)**](#2-generaciones-ddr-de-ddr-a-ddr5)
- [3. **Formatos físicos (DIMM, SO-DIMM), pines y muescas**](#3-formatos-físicos-dimm-so-dimm-pines-y-muescas)
- [4. **Rendimiento: MT/s, timings y latencia absoluta (con ejemplos)**](#4-rendimiento-mts-timings-y-latencia-absoluta-con-ejemplos)
- [5. **Canales, Ranks, Bank Groups y Subcanales (DDR5)**](#5-canales-ranks-bank-groups-y-subcanales-ddr5)
- [6. **ECC, RDIMM/LRDIMM y fiabilidad**](#6-ecc-rdimmlrdimm-y-fiabilidad)
- [7. **Tabla comparativa de generaciones DDR**](#7-tabla-comparativa-de-generaciones-ddr)
- [8. **Pirámide jerárquica de memorias**](#8-pirámide-jerárquica-de-memorias)
- [9. **Compatibilidad, instalación y UEFI (checklist)**](#9-compatibilidad-instalación-y-uefi-checklist)
- [10. **Diagnóstico, pruebas y sintomatología típica**](#10-diagnóstico-pruebas-y-sintomatología-típica)
- [11. **Recomendaciones de compra y casos de uso**](#11-recomendaciones-de-compra-y-casos-de-uso)

---

# 0. Definición y Visión General (Memoria DDR)
**En qué consiste:** DDR es la tecnología con la que se fabrican los módulos de **memoria principal** (RAM) que usa el sistema para mantener **código** y **datos activos**. A diferencia del almacenamiento masivo (no volátil), la DDR es **volátil**: al cortar la energía, su contenido se pierde.  
**Por qué importa:** porque su **latencia baja** y **gran ancho de banda** permiten que CPU y GPU integrada trabajen sin cuellos de botella. La cantidad, organización (canales) y calidad (frecuencia/timings) de la DDR condicionan la **fluidez** y el rendimiento real.

---

# 1. Estructura y Funcionamiento (bancos, filas/columnas, prefetch, bursts)
**En qué consiste:** internamente, un chip DRAM es una **matriz** de celdas agrupadas en **bancos**; cada acceso abre una **fila** completa (tRCD), lee/escribe **columnas** (CL/tCWL) y, al terminar, **pre-carga** (tRP) para cerrar la fila.

- **Prefetch**: el chip extrae en bloque (2n/4n/8n/16n) y lo entrega en **ráfagas (bursts)** por el bus; así se aprovecha mejor cada activación de fila.  
- **Burst Length (BL)**: cuántos datos viajan por operación; BL8 típico en DDR3/DDR4, **BL16 en DDR5** (con *burst chop* para granularidad).  
- **Bank Groups**: particiones que permiten **atender en paralelo** bancos diferentes reduciendo conflictos.  
- **Controladora (IMC)**: vive en la CPU moderna; **programa timings**, **intercala** accesos y equilibra peticiones de núcleos/PCIe/iGPU.

> **Idea práctica:** los patrones de acceso del software importan. Lecturas **secuenciales** explotan mejor el prefetch; accesos muy **aleatorios** sufren más los costes de abrir/cerrar filas.

---

# 2. Generaciones DDR (de DDR a DDR5)
**En qué consiste:** cada generación aumenta la eficiencia con prefetch mayor, voltajes menores y mejoras de señalización/topología. Las generaciones **no son físicamente compatibles** (muesca, pines, voltajes).

- **DDR (1.x)**: 2n prefetch, 2.5 V, hasta ~400 MT/s. Punto de partida histórico.  
- **DDR2**: 4n, 1.8 V, *On-Die Termination* (ODT); ~400–800 MT/s (hasta 1066).  
- **DDR3**: 8n, 1.5 V (1.35 V DDR3L), topología *fly-by*; 800–1600 MT/s (hasta 2133 JEDEC).  
- **DDR4**: 8n, 1.2 V, **bank groups**, mejoras de entrenamiento y DBI; 1600–3200 MT/s.  
- **DDR5**: 16n, **1.1 V**, **PMIC** en el módulo, **2×32-bit subcanales por DIMM**, **on-die ECC**; 3200–6400 MT/s JEDEC (y superiores en kits comerciales).

> **Lectura del nombre**: *DDR5-5600* significa **5600 MT/s** (≈ 2800 MHz de reloj base en equivalencia DDR).

---

# 3. Formatos físicos (DIMM, SO-DIMM), pines y muescas
**En qué consiste:** los módulos se presentan en **DIMM** (escritorio/servidor) y **SO-DIMM** (portátil/SFF). El **número de pines** y la **posición de la muesca** evitan combinaciones incompatibles.

- **DIMM**: 240 pines (DDR3) → **288 pines (DDR4/DDR5)**.  
- **SO-DIMM**: 204 pines (DDR3) → **260 (DDR4)** → **262 (DDR5)**.  
- **UDIMM** (usuario/estación) vs **RDIMM/LRDIMM** (servidor): con registro/búfer para **mayor estabilidad/capacidad** por canal.

---

# 4. Rendimiento: MT/s, timings y latencia absoluta (con ejemplos)
**En qué consiste:** el rendimiento práctico depende de **dos ejes**: *tasa de transferencia* (MT/s → ancho de banda) y *latencias internas* (timings → tiempo de respuesta inicial).

### 4.1 Ancho de banda (por canal)
Fórmula (base 10):  
`BW (GB/s) ≈ MT/s × 8 ÷ 1000`  
Ejemplos:
- **DDR4-3200** → `3200 × 8 ÷ 1000 ≈ 25,6 GB/s` por canal → **≈ 51,2 GB/s** en **dual channel**.  
- **DDR5-5600** → `5600 × 8 ÷ 1000 ≈ 44,8 GB/s` por canal → **≈ 89,6 GB/s** en **dual channel**.

### 4.2 Latencia absoluta
Aproximación:  
`tCL (ns) ≈ (CL × 2000) ÷ MT/s`  
Ejemplos:
- **DDR4-3200 CL16** → `(16×2000)/3200 ≈ 10,0 ns`.  
- **DDR5-5600 CL36** → `(36×2000)/5600 ≈ 12,9 ns`.

**Interpretación:** más **MT/s** acelera transferencias largas; **timings** más ajustados reducen el tiempo hasta el **primer dato**. En la práctica, **capacidad suficiente** y **doble canal** tienen impacto mayor que micro-ajustes de timings.

---

# 5. Canales, Ranks, Bank Groups y Subcanales (DDR5)
**En qué consiste:** son “trucos de organización” para **aumentar el paralelismo** y aprovechar mejor el bus.

- **Canales**: 1×64-bit por canal. Con **dual channel** (2 módulos) doblas el caudal.  
- **Ranks** (SR/DR/QR): agrupaciones lógicas; más ranks pueden facilitar **interleaving** y mejorar ocupación del bus (dentro de los límites de la IMC).  
- **Bank Groups**: permiten servir operaciones solapadas en bancos distintos con menos contención.  
- **Subcanales (DDR5)**: cada DIMM se parte en **2×32-bit** independientes a ciertos efectos, lo que suaviza burbujas y mejora eficiencia en accesos pequeños.

---

# 6. ECC, RDIMM/LRDIMM y fiabilidad
**En qué consiste:** mecanismos para **detectar/corregir errores** y estabilizar señales cuando crecen densidades/capacidades.

- **ECC de sistema**: añade bits extra por palabra (72-bit por canal en ECC típico) y corrige errores de 1 bit (SECDED). Necesita **CPU + placa + módulos ECC** compatibles.  
- **On-die ECC (DDR5)**: corrige fallos **internos** del chip, transparente al sistema; **no** reemplaza al ECC de sistema.  
- **RDIMM/LRDIMM**: el **registro** y el **búfer** “limpian” señales y permiten **más módulos/capacidad** por canal; se usan en **servidores**.

---

# 7. Tabla comparativa de generaciones DDR
**En qué consiste:** resumen de parámetros oficiales (JEDEC) para entender **límites de diseño** y evolución de la tecnología.

| Generación | Prefetch | Voltaje nominal | Data rate JEDEC (MT/s) | Pines **DIMM / SO-DIMM** | Organización de bus | PMIC | On-die ECC | Rasgos distintivos |
|---|:--:|:--:|:--:|:--:|---|:--:|:--:|---|
| **DDR**  | 2n  | 2.5 V | 200–400 | 184 / —   | 64-bit por DIMM | No | No | Origen DDR; obsoleta. |
| **DDR2** | 4n  | 1.8 V | 400–800 *(~1066)* | 240 / 200 | 64-bit por DIMM | No | No | ODT; mejoras de señalización. |
| **DDR3** | 8n  | 1.5 V *(1.35 V L)* | 800–1600 *(~2133)* | 240 / 204 | 64-bit por DIMM | No | No | Topología *fly-by*; mayor densidad. |
| **DDR4** | 8n  | 1.2 V | 1600–3200 | 288 / 260 | 64-bit por DIMM | No | No | **Bank groups**, DBI, entrenamiento. |
| **DDR5** | 16n | 1.1 V | 3200–6400 | 288 / 262 | **2×32-bit por DIMM** | **Sí** | **Sí** | **PMIC**, subcanales, más densidad. |

> *Nota:* Los kits comerciales pueden anunciar velocidades **superiores** a JEDEC usando **XMP/EXPO**. La estabilidad depende de la plataforma (CPU/placa/UEFI).

---

# 8. Pirámide jerárquica de memorias
**En qué consiste:** una jerarquía por **latencia, ancho de banda, capacidad, coste/GB**. Cuanto más arriba, **más rápido y caro**; cuanto más abajo, **más grande y lento**.

