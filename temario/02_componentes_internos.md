## 📚 Mantenimiento y Montaje de Equipos Informáticos

## TEMA 2. COMPONENTES INTERNOS FUNDAMENTALES

## Índice

- [0. Definición y Función General (Placa base)](#0-definición-y-función-general-placa-base)
- [1 Vocabulario Fundamental](#1-vocabulario-fundamental)
- [2. Factor de forma](#2-factor-de-forma)
  - [2.1 Concepto y importancia](#21-concepto-y-importancia)
  - [2.2 Factores de forma más utilizados (2025)](#22-factores-de-forma-más-utilizados-2025)
  - [2.3 Detalle de factores actuales](#23-detalle-de-factores-actuales)
  - [2.4 Tabla comparativa resumida](#24-tabla-comparativa-resumida)
  - [2.5 Recomendaciones](#25-recomendaciones)
- [3 Chasis o Caja del computador](#3-chasis-o-caja-del-computador)
  - [3.1 Partes principales modernas](#31-partes-principales-modernas)
  - [3.2 Factor de Forma y Tipos](#32-factor-de-forma-y-tipos)
  - [3.3 Paneles y cableado moderno](#33-paneles-y-cableado-moderno)
  - [3.4 Consejos prácticos](#34-consejos-prácticos)
- [4. Conectores](#4-conectores)
  - [4.1 Conectores Externos](#41-conectores-externos)
  - [4.2 Conectores Internos (Desarrollado y Ampliado)](#42-conectores-internos-desarrollado-y-ampliado)
    - [4.2.1   SATA III (Serial ATA Revisado)**](#421---sata-iii-serial-ata-revisado)
    - [4.2.2   M.2 (Socket sobre placa base)**](#422---m2-socket-sobre-placa-base)
    - [4.2.3  PCI Express (PCIe)](#423--pci-express-pcie)
    - [4.2.4  Conectores de Alimentación internos](#424--conectores-de-alimentación-internos)
    - [4.2.5 Headers para el panel frontal y periféricos](#425-headers-para-el-panel-frontal-y-periféricos)
    - [4.2.6 Otros conectores relevantes](#426-otros-conectores-relevantes)
- [5 **Zócalo del Procesador (Socket)**](#5-zócalo-del-procesador-socket)
  - [5.1. Tipos de Socket](#51-tipos-de-socket)
  - [5.2 Principales sockets modernos (2022–2025)](#52-principales-sockets-modernos-20222025)
- [6 **Chipset**](#6-chipset)
- [7 Ranuras RAM y Arquitectura Multicanal](#7-ranuras-ram-y-arquitectura-multicanal)
  - [7.1 Tipos de ranuras y módulos](#71-tipos-de-ranuras-y-módulos)
  - [7.2 Número de ranuras](#72-número-de-ranuras)
  - [7.3 Arquitectura de canales (Channel Architecture)](#73-arquitectura-de-canales-channel-architecture)
  - [7.4 Cómo aprovechar la arquitectura multicanal](#74-cómo-aprovechar-la-arquitectura-multicanal)
  - [7.5 Ejemplo de configuración óptima para gaming 2025](#75-ejemplo-de-configuración-óptima-para-gaming-2025)
  - [7.6 Consejos prácticos](#76-consejos-prácticos)
- [8. Slots de expansión](#8-slots-de-expansión)
  - [8.1 El Bus PCI Express (PCIe): Funcionamiento y Estructura](#81-el-bus-pci-express-pcie-funcionamiento-y-estructura)
    - [8.1.1 **Estructura y concepto de “líneas” (lanes):**](#811-estructura-y-concepto-de-líneas-lanes)
    - [8.1.2 **Ventajas técnicas de PCIe:**](#812-ventajas-técnicas-de-pcie)
    - [8.1.3 **Versiones PCIe y ancho de banda por línea:**](#813-versiones-pcie-y-ancho-de-banda-por-línea)
    - [8.1.4 **Cómo afecta al usuario:**](#814-cómo-afecta-al-usuario)
    - [8.1.5 Tipos físicos de slots y ejemplos de uso](#815-tipos-físicos-de-slots-y-ejemplos-de-uso)
  - [8.2 M.2](#82-m2)
    - [8.2.1 Ejemplo de configuración](#821-ejemplo-de-configuración)
    - [8.2.2 Consejos técnicos y consideraciones](#822-consejos-técnicos-y-consideraciones)
- [9. VRM (Voltage Regulator Module)](#9-vrm-voltage-regulator-module)
  - [9.1. Concepto y función esencial](#91-concepto-y-función-esencial)
  - [9.2.  Estructura de un VRM moderno](#92--estructura-de-un-vrm-moderno)
  - [9.3. Importancia del VRM en 2025](#93-importancia-del-vrm-en-2025)
  - [9.4. Número de fases y su relevancia](#94-número-de-fases-y-su-relevancia)
  - [9.5. Consejos de usuario y técnico](#95-consejos-de-usuario-y-técnico)
- [10. Nuevas tecnologías](#10-nuevas-tecnologías)
- [11. Instalación y mantenimiento](#11-instalación-y-mantenimiento)



# 0. Definición y Función General (Placa base)
La **placa base** es la plataforma esencial donde se interconectan todos los componentes del ordenador: CPU, RAM, almacenamiento, tarjetas de expansión y periféricos. Determina compatibilidad, escalabilidad, rendimiento y posibilidades de actualización.


# 1 Vocabulario Fundamental
| **Término**         | **Definición**  |
|---------------------|----------------------------------|
| **Cuello de botella** | Limitación de rendimiento causada porque un componente (CPU, GPU, RAM, SSD) es más rápido que el resto de la cadena y la transmisión de datos se ve frenada; hoy afecta sobre todo a buses y almacenamiento en gaming de alta gama. |
| **Coma flotante**    | Notación para representar números reales con mucha precisión, clave en procesadores y sobre todo en IA moderna y tarjetas gráficas, que ahora realizan trillones de cálculos de coma flotante por segundo. |
| **Factor de forma**  | Estándar físico de placas base y chasis: ATX, MicroATX, MiniITX, y el nuevo BTF (Back To Front) en cableado oculto; las RAM CAMM2 empiezan a desplazar a SO-DIMM en portátiles. |
| **Fan (ventilador)** | Elemento crítico de refrigeración. Ahora mayoría incluyen control digital (PWM), sensores de temperatura y efecto RGB sincronizable. |
| **FSB**              | Bus frontal ya obsoleto, sustituido hoy por buses PCIe, DMI (Intel) o Infinity Fabric (AMD). |
| **Gigahercio (GHz)** | Unidad de frecuencia. CPUs actuales alcanzan más de 5.5 GHz. RAM DDR5 para gaming puede correr a 8000+ MHz. |
| **Memoria flash**    | Base de SSDs NVMe y UltraRAM, que superan en velocidad a discos SATA convencionales. |
| **Nanosegundo**      | Tiempo mínimo de acceso en chips RAM y SSD. Hoy se dan valores de 7–12 ns en memorias premium. |
| **Nanómetro**        | Milmillonésima parte de un metro; hace referencia al proceso de fabricación de chips: 3nm y 4nm dominan en CPUs y GPUs actuales. |

---
# 2. Factor de forma
El **factor de forma** define las dimensiones físicas, el diseño de los conectores y la organización interna de la placa base, lo que determina la compatibilidad con chasis, fuentes de alimentación y componentes. Elegir el adecuado afecta la capacidad de expansión, refrigeración, estética y futuro upgrade del sistema.

---

## 2.1 Concepto y importancia
- Un factor de forma es un estándar que dicta cómo se fabrican y disponen las placas base y sus componentes. Su objetivo es garantizar compatibilidad entre placas, torres y demás hardware modular.
- Afecta a:
  - Número y tipo de ranuras de expansión (PCIe, M.2, RAM).
  - Posiciones de puertos traseros, alimentación, refrigeradores.
  - Tamaño de la caja, facilidad de montaje y ventilación.

---

## 2.2 Factores de forma más utilizados (2025)
| Factor de forma   | Dimensiones (mm) | Puestos de expansión | Uso principal                | Compatibilidad chasis      |
|-------------------|------------------|----------------------|------------------------------|----------------------------|
| ATX               | 305 x 244        | 7 PCIe + 4–8 RAM     | Gaming, workstation, desktop | Universal                  |
| MicroATX          | 244 x 244        | 4 PCIe + 2–4 RAM     | Oficina, gaming compactos    | ATX/MicroATX               |
| MiniITX           | 170 x 170        | 1 PCIe + 2 RAM       | HTPC, ultracompactos, SFF    | Mini/micro ATX, ITX        |
| E-ATX             | 305 x 330        | 8 PCIe + 8 RAM       | Workstation, gaming extremo  | Full Tower, E-ATX          |
| XL-ATX            | Hasta 345 x 262  | 8+ PCIe + 8+ RAM     | Servidor         | Full Tower XL, server rack |
| DTX/Mini-DTX      | 203 x 244/170x203| 2 PCIe + 2 RAM       | SFF, embebidos, industria    | Mini/Micro ATX, DTX        |
| BTF/Back Connect  | Variable         | Mismas que ATX/ITX   | PC moderno cableado limpio   | Chasis BTF homologados     |
| CAMM2             | N/A (RAM modular)| —                    | Portátiles premium, SFF      | Cajas y disipadores específicos |

---

## 2.3 Detalle de factores actuales
**ATX:**  
El estándar dominante: admite sistemas exigentes de gaming y trabajo, multiGPU, muchas unidades M.2/SATA y RAM. Excelente ventilación.

**MicroATX:**  
Más compacto, ideal para equipos medios y oficinas; se puede instalar en cajas ATX. Permite menos expansión pero suficiente para la mayoría de usuarios.

**MiniITX:**  
El más pequeño en desktop. Ideal en builds minimalistas, HTPC y setups compactos. Limitación clara de expansión y refrigeración.

**E-ATX / XL-ATX:**  
Formato grande: más ranuras y espacio para refrigeración extrema, ideal para workstations, creadores, servidores domésticos.

**DTX / MiniDTX / NanoITX / PicoITX:**  
Formatos industriales y embebidos. Usados en IoT, robótica, aplicaciones custom. Limitación absoluta de expansión.

**BTF/Back Connect:**  
Concepto moderno donde el cableado va oculto en el reverso de la placa, facilitando airflow, limpieza visual y builds “premium”.

**CAMM2:**  
Solo para portátiles premium y workstations compactas. Permite módulos de RAM plug&play, máxima densidad y fácil instalación.

**Formato propietario:**  
Usado en OEM y all-in-one, dificultad de actualización e intercambios.

---

## 2.4 Tabla comparativa resumida
| Nombre     | Expansión Máx. | Dimensiones | Uso                       | Expansibilidad |
|------------|----------------|-------------|---------------------------|----------------|
| ATX        | Alta           | 305x244     | Gaming general, workstation| Muy alta        |
| MicroATX   | Media          | 244x244     | Oficina, gaming compacto  | Alta            |
| MiniITX    | Baja           | 170x170     | SFF, media center         | Media           |
| E-ATX      | Muy alta       | 305x330     | Workstation, multi-GPU    | Máxima          |
| BTF        | Variable       | Variable    | Builds cableado premium   | Muy alta        |
| CAMM2      | —              | —           | Portátiles premium        | Modular RAM     |

---

## 2.5 Recomendaciones
- Para gaming y workstation: ATX, E-ATX o BTF si buscas máxima capacidad y estética.
- Para oficinas o PCs compactos: MicroATX o MiniITX.
- Para portátiles o máquinas plug&play: verifica compatibilidad CAMM2 para upgrades futuros.
- Evita formatos propietarios salvo equipos OEM o necesidades muy específicas.

---

# 3 Chasis o Caja del computador
## 3.1 Partes principales modernas
- **Cubierta**: Acero galvanizado, paneles laterales de cristal templado, sistemas magnéticos y modulares.
- **Panel frontal**: Botones táctiles, displays LCD/AMOLED (monitoreo en tiempo real), puertos USB-C, USB 4.0, salida/entrada audio, pantalla de temperatura y carga.
- **Bahías internas**: Principalmente slots M.2 y 2.5"/3.5" (con tendencia a M.2). Las bahías externas (5,25") van desapareciendo.
- **Fuente alimentación**: Zona separada, formato ATX 3.0/SFX-L, modulable y con soporte para GPU PCIe 5.0.

## 3.2 Factor de Forma y Tipos
| Tipo                  | Fit/Expansión        | Ventajas                  | Limitaciones/Contexto                    |
|-----------------------|----------------------|---------------------------|------------------------------------------|
| Barebone/MiniPC       | 1–2 slots            | Compacto, bajo consumo    | Sin expansión, solo tareas ligeras       |
| Mini Torre/MiniITX    | 2–3 slots RAM, 1 GPU | Compacto y versátil       | Una sola GPU, limitada RL                |
| Mid Tower/Mediatorre  | 4–6 slots            | Balance expansión/tamaño  | Espacio justo para triple ventilador     |
| Torre/Full Tower      | 10+ slots, 3 GPU     | Workstation/gaming top    | Muy grande/pesada, para entusiastas      |
| Servidor/Rack         | Bayas U, redundantes | Eficiencia y redundancia  | Uso profesional, no doméstico            |

## 3.3 Paneles y cableado moderno
- **Panel trasero:** Salida múltiple para todos los periféricos.
- **Panel frontal:** Control RGB, pantalla LCD, puertos tipo C/a, quick charge, ranuras para docking SSD hot swap.
- **Paneles inteligentes:** Chasis actuales integran softwares propios y sensores.
- **Gestión cableado:** Sistema BTF y anclajes, todo oculto y preparado para montar/disponer fácil, seguro y exigente para IA y gaming de alto consumo.

---

## 3.4 Consejos prácticos
- **Airflow** primero: elige chasis con múltiples entradas/salidas de aire y zonas amplias para radiadores.
- **Compatibilidad**: Antes de comprar/montar, comprueba soportes de GPU largas, PSU potentes, y placas con headers modernizados.
- **RGB y monitoreo**: Aprovecha headers y software de placas/cajas modernas para crear un PC funcional y visualmente atractivo, además de seguro.

---

---
# 4. Conectores
## 4.1 Conectores Externos
| Conector        | Uso                    | Detalles técnicos        | Ejemplo de uso          |
|-----------------|------------------------|------------------------------|-------------------------|
| **RJ-45**       | Red LAN; Multi-Gig     | Hasta 10 GbE (Cat7/8)        | Conexión de red doméstica o profesional, transmisión 4K/8K |
| **Wi-Fi 6E/7**  | Inalámbrico            | Hasta 10 Gbps, baja latencia | Placas con antena integrada para gaming/pro y VR           |
| **USB-A/C/USB4**| Periféricos/alimentación| Hasta 80 Gbps (USB4 Type-C), Thunderbolt 4| Soporte para monitores, disks, móviles, hubs, carga rápida|
| **HDMI 2.1**    | Vídeo/audio digital    | Hasta 8K/120Hz, eARC         |
