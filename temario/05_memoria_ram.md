---
layout: default
title: "TEMA 5. MEMORIA DDR"
nav_order: 7
---


# Memoria RAM
- [1. **Vocabulario Fundamental**](#1-vocabulario-fundamental)
- [2. **Definición y Función General (Memoria RAM)**](#0-definición-y-función-general-memoria-ram)
- [3. **Conceptos Esenciales**](#1-conceptos-esenciales)
- [4. **Generaciones y Formatos (DDR3/DDR4/DDR5; DIMM/SO-DIMM; ECC/RDIMM)**](#2-generaciones-y-formatos-ddr3ddr4ddr5-dimmsodimm-eccrdimm)
- [5. **Organización y Rendimiento (Canales, Ranks, Bank Groups, Interleaving)**](#3-organización-y-rendimiento-canales-ranks-bank-groups-interleaving)
- [6. **Tabla comparativa de memorias DDR**](#4-tabla-comparativa-de-memorias-ddr)
- [7. **Instalación y Puesta en Marcha (Checklist)**](#5-instalación-y-puesta-en-marcha-checklist)
- [8. **Fallos Típicos y Diagnóstico**](#6-fallos-típicos-y-diagnóstico)
- [9. **RAM, Memoria Virtual y Swap**](#7-ram-memoria-virtual-y-swap)
- [10. **Pirámide Jerárquica de Memorias**](#8-pirámide-jerárquica-de-memorias)
- [11. **Recomendaciones de Compra**](#9-recomendaciones-de-compra)
- [12. **Actividades y Prácticas**](#10-actividades-y-prácticas)


# 1. **Vocabulario Fundamental**


---


# 2. Definición y Función General (Memoria RAM)
La **RAM** es la memoria de trabajo del sistema: el sistema operativo, los programas y los datos activos se cargan aquí. Es **volátil** (se borra al apagar), ofrece **latencia muy baja** y **alto ancho de banda** frente al almacenamiento masivo.

---

# 3. Conceptos Esenciales
- **Capacidad**: 8/16/32 GB… Más capacidad reduce paginación a disco.  
- **Transferencia (MT/s)**: p. ej. DDR4-3200 (3200 MT/s), DDR5-5600…  
- **Ancho de banda** (por canal): `MT/s × 64 bits ÷ 8 = GB/s`. Doble canal ≈ **×2**.  
- **Latencia CAS (CL)** y **timings**: influyen en la respuesta inicial; a cargas largas, **MT/s** manda más.  
- **Perfiles SPD/XMP/EXPO**: en UEFI aplica el perfil del fabricante para lograr velocidades publicitadas (si hay soporte).

---

# 4. Generaciones y Formatos (DDR3/DDR4/DDR5; DIMM/SO-DIMM; ECC/RDIMM)
- **DDR3 → DDR4 → DDR5**: distintas muescas, voltajes y límites eléctricos (no son intercambiables).  
- **Form factor**: **DIMM** (escritorio/servidor) y **SO-DIMM** (portátil/mini-PC).  
- **ECC / Paridad** y **RDIMM** (registrada): típicos en servidores/estaciones; **requieren** placa/CPU compatibles.  
- **Novedades DDR5**: **PMIC** en el módulo, **dos subcanales** de 32-bit por DIMM y **on-die ECC** (corrección interna al chip).

---

# 5. Organización y Rendimiento (Canales, Ranks, Bank Groups, Interleaving)
- **Canales**: Single/Dual/Quad. Instala **2 módulos iguales** en zócalos alternos para doble canal.  
- **Ranks**: permiten intercalar accesos; pueden ayudar (ligeramente) al rendimiento/compatibilidad.  
- **Bank groups** (DDR4/DDR5) y **prefetch**: más paralelismo interno.  
- **Interleaving**: la controladora reparte direcciones entre bancos/ranks/canales para subir el rendimiento efectivo.

---

# 6. Tabla comparativa de memorias DDR
> Valores **JEDEC típicos** (no overclock). Algunos límites pueden variar por fabricante/plataforma.

| Generación | Año aprox. JEDEC | Pines **DIMM** / **SO-DIMM** | Voltaje nominal | Data rate JEDEC (MT/s) | Organización del bus | **PMIC** | **On-die ECC** | Notas |
|---|---:|---:|---:|---:|---|:--:|:--:|---|
| **DDR3** | 2007 | 240 / 204 | 1.5 V *(1.35 V DDR3L)* | 800–1600 *(+1866/2133 tardíos)* | 64-bit por DIMM | No | No | Fin de ciclo en plataformas modernas. |
| **DDR4** | 2014 | 288 / 260 | 1.2 V | 1600–3200 | 64-bit por DIMM | No | No | Estándar actual en muchas placas; **XMP 2.0**. |
| **DDR5** | 2020 | 288 / 262 | 1.1 V | 3200–6400 | **2×32-bit por DIMM** | **Sí** | **Sí** *(interno)* | Mayor densidad; **XMP 3.0 / EXPO**. |

---

# 7. Instalación y Puesta en Marcha (Checklist)
1. **Descarga ESD** y equipo **apagado**.  
2. Alinea la **muesca** y presiona hasta el **clic** de las pestañas.  
3. Coloca por **pares** en zócalos recomendados (colores alternos).  
4. En **UEFI**, verifica capacidad/velocidad y activa **XMP/EXPO** si procede.  
5. **Prueba** con Memtest86+ si sospechas inestabilidad.

---

# 8. Fallos Típicos y Diagnóstico
- **POST con pitidos/bucle** → asiento incorrecto, zócalo dañado o módulo incompatible.  
- **Cuelgues/BSOD** → baja un escalón de **MT/s**, relaja **timings** o sube un poco el **voltaje** (según plataforma).  
- **XMP/EXPO inestable** → actualiza UEFI, mejora ventilación VRM, o usa perfiles más conservadores.

---

# 9. RAM, Memoria Virtual y Swap
- La **memoria virtual** amplía la RAM con **swap/pagefile** en disco: evita errores por falta de memoria pero es **mucho más lenta**.  
- Señales de saturación: disco al 100% con **Lecturas/Escrituras pequeñas**, interfaz “congelada”, apps que tardan en cambiar de ventana.

---

# 10. Pirámide Jerárquica de Memorias

