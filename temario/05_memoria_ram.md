---
layout: default
title: "TEMA 5. MEMORIA DDR"
nav_order: 7
---


# Memoria RAM
- [1. **Vocabulario Fundamental**](#1-vocabulario-fundamental)
- [0. **Definición y Función General (Memoria RAM)**](#0-definición-y-función-general-memoria-ram)
- [1. **Conceptos Esenciales**](#1-conceptos-esenciales)
- [2. **Generaciones y Formatos (DDR3/DDR4/DDR5; DIMM/SO-DIMM; ECC/RDIMM)**](#2-generaciones-y-formatos-ddr3ddr4ddr5-dimmsodimm-eccrdimm)
- [3. **Organización y Rendimiento (Canales, Ranks, Bank Groups, Interleaving)**](#3-organización-y-rendimiento-canales-ranks-bank-groups-interleaving)
- [4. **Tabla comparativa de memorias DDR**](#4-tabla-comparativa-de-memorias-ddr)
- [5. **Instalación y Puesta en Marcha (Checklist)**](#5-instalación-y-puesta-en-marcha-checklist)
- [6. **Fallos Típicos y Diagnóstico**](#6-fallos-típicos-y-diagnóstico)
- [7. **RAM, Memoria Virtual y Swap**](#7-ram-memoria-virtual-y-swap)
- [8. **Pirámide Jerárquica de Memorias**](#8-pirámide-jerárquica-de-memorias)
- [9. **Recomendaciones de Compra**](#9-recomendaciones-de-compra)
- [10. **Actividades y Prácticas**](#10-actividades-y-prácticas)


# 1. **Vocabulario Fundamental**

> | Término | Definición | Nota rápida |
> |---|---|---|
> | **RAM** | Memoria de acceso aleatorio, **volátil**. | Donde “vive” lo que usas ahora. |
> | **DIMM / SO-DIMM** | Formato de módulo (escritorio / portátil). | No intercambiables entre generaciones. |
> | **MT/s** | Transferencias por segundo (DDR). | Ej.: DDR4-3200 ⇒ 3200 MT/s. |
> | **MHz (reloj)** | Frecuencia interna (no confundir con MT/s). | DDR transfiere en flancos ↑↓. |
> | **Ancho de banda** | GB/s disponibles. | ≈ MT/s × 8 B × nº canales / 10⁹. |
> | **CL (CAS)** | Latencia al **primer dato** (en ciclos). | A igual MT/s, **CL menor** = mejor. |
> | **Timings** | Conjunto de latencias (CL-tRCD-tRP-tRAS…). | Afectan respuesta y estabilidad. |
> | **Canal** | Rutas paralelas (single/dual/quad). | 2 módulos = **doble canal**. |
> | **Rank** | Grupo lógico de chips en un DIMM. | Intercala accesos; influye compatibilidad. |
> | **SPD** | Datos del módulo (perfiles, fabricante). | Leídos por la UEFI/BIOS. |
> | **XMP/EXPO** | Perfiles de frecuencia/timings del fabricante. | Actívalos en UEFI si tu placa/CPU lo soportan. |
> | **ECC** | Detección/corrección de errores. | Requiere placa y CPU compatibles. |
> | **RDIMM/UDIMM** | Registrada / sin registrar. | RDIMM típico de **servidor**. |
> | **PMIC** | Regulación de voltaje **en el módulo** (DDR5). | Estabiliza y simplifica la placa. |
> | **Subcanal (DDR5)** | 2×32-bit por DIMM en DDR5. | Mejora eficiencia/colisiones. |
> | **Swap** | Memoria virtual en disco. | Mucho más lenta que RAM; evita saturación. |

---
---

# 0. Definición y Función General (Memoria RAM)
La **RAM** es la memoria de trabajo del sistema: el sistema operativo, los programas y los datos activos se cargan aquí. Es **volátil** (se borra al apagar), ofrece **latencia muy baja** y **alto ancho de banda** frente al almacenamiento masivo.

---

# 1. Conceptos Esenciales
- **Capacidad**: 8/16/32 GB… Más capacidad reduce paginación a disco.  
- **Transferencia (MT/s)**: p. ej. DDR4-3200 (3200 MT/s), DDR5-5600…  
- **Ancho de banda** (por canal): `MT/s × 64 bits ÷ 8 = GB/s`. Doble canal ≈ **×2**.  
- **Latencia CAS (CL)** y **timings**: influyen en la respuesta inicial; a cargas largas, **MT/s** manda más.  
- **Perfiles SPD/XMP/EXPO**: en UEFI aplica el perfil del fabricante para lograr velocidades publicitadas (si hay soporte).

---

# 2. Generaciones y Formatos (DDR3/DDR4/DDR5; DIMM/SO-DIMM; ECC/RDIMM)
- **DDR3 → DDR4 → DDR5**: distintas muescas, voltajes y límites eléctricos (no son intercambiables).  
- **Form factor**: **DIMM** (escritorio/servidor) y **SO-DIMM** (portátil/mini-PC).  
- **ECC / Paridad** y **RDIMM** (registrada): típicos en servidores/estaciones; **requieren** placa/CPU compatibles.  
- **Novedades DDR5**: **PMIC** en el módulo, **dos subcanales** de 32-bit por DIMM y **on-die ECC** (corrección interna al chip).

---

# 3. Organización y Rendimiento (Canales, Ranks, Bank Groups, Interleaving)
- **Canales**: Single/Dual/Quad. Instala **2 módulos iguales** en zócalos alternos para doble canal.  
- **Ranks**: permiten intercalar accesos; pueden ayudar (ligeramente) al rendimiento/compatibilidad.  
- **Bank groups** (DDR4/DDR5) y **prefetch**: más paralelismo interno.  
- **Interleaving**: la controladora reparte direcciones entre bancos/ranks/canales para subir el rendimiento efectivo.

---

# 4. Tabla comparativa de memorias DDR
> Valores **JEDEC típicos** (no overclock). Algunos límites pueden variar por fabricante/plataforma.

| Generación | Año aprox. JEDEC | Pines **DIMM** / **SO-DIMM** | Voltaje nominal | Data rate JEDEC (MT/s) | Organización del bus | **PMIC** | **On-die ECC** | Notas |
|---|---:|---:|---:|---:|---|:--:|:--:|---|
| **DDR3** | 2007 | 240 / 204 | 1.5 V *(1.35 V DDR3L)* | 800–1600 *(+1866/2133 tardíos)* | 64-bit por DIMM | No | No | Fin de ciclo en plataformas modernas. |
| **DDR4** | 2014 | 288 / 260 | 1.2 V | 1600–3200 | 64-bit por DIMM | No | No | Estándar actual en muchas placas; **XMP 2.0**. |
| **DDR5** | 2020 | 288 / 262 | 1.1 V | 3200–6400 | **2×32-bit por DIMM** | **Sí** | **Sí** *(interno)* | Mayor densidad; **XMP 3.0 / EXPO**. |

---

# 5. Instalación y Puesta en Marcha (Checklist)
1. **Descarga ESD** y equipo **apagado**.  
2. Alinea la **muesca** y presiona hasta el **clic** de las pestañas.  
3. Coloca por **pares** en zócalos recomendados (colores alternos).  
4. En **UEFI**, verifica capacidad/velocidad y activa **XMP/EXPO** si procede.  
5. **Prueba** con Memtest86+ si sospechas inestabilidad.

---

# 6. Fallos Típicos y Diagnóstico
- **POST con pitidos/bucle** → asiento incorrecto, zócalo dañado o módulo incompatible.  
- **Cuelgues/BSOD** → baja un escalón de **MT/s**, relaja **timings** o sube un poco el **voltaje** (según plataforma).  
- **XMP/EXPO inestable** → actualiza UEFI, mejora ventilación VRM, o usa perfiles más conservadores.

---

# 7. RAM, Memoria Virtual y Swap
- La **memoria virtual** amplía la RAM con **swap/pagefile** en disco: evita errores por falta de memoria pero es **mucho más lenta**.  
- Señales de saturación: disco al 100% con **Lecturas/Escrituras pequeñas**, interfaz “congelada”, apps que tardan en cambiar de ventana.

---

# 8. Pirámide Jerárquica de Memorias

