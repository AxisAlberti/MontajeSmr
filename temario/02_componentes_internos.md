## 📚 Mantenimiento y Montaje de Equipos Informáticos

## TEMA 2. COMPONENTES INTERNOS FUNDAMENTALES

- [0. **Definición y Función General (Placa base)**](#0-definición-y-función-general-placa-base)
- [1 **Vocabulario Fundamental**](#1-vocabulario-fundamental)
- [2. **Factor de forma**](#2-factor-de-forma)
  - [2.1 Concepto y importancia](#21-concepto-y-importancia)
  - [2.2 Factores de forma más utilizados (2025)](#22-factores-de-forma-más-utilizados-2025)
  - [2.3 Detalle de factores actuales](#23-detalle-de-factores-actuales)
  - [2.4 Tabla comparativa resumida](#24-tabla-comparativa-resumida)
  - [2.5 Recomendaciones](#25-recomendaciones)
- [3 **Chasis o Caja del pc**](#3-chasis-o-caja-del-pc)
  - [3.1 Partes principales modernas](#31-partes-principales-modernas)
  - [3.2 Factor de Forma y Tipos](#32-factor-de-forma-y-tipos)
  - [3.3 Paneles y cableado moderno](#33-paneles-y-cableado-moderno)
  - [3.4 Consejos prácticos](#34-consejos-prácticos)
- [4. **Conectores**](#4-conectores)
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
- [7 **Ranuras RAM y Arquitectura Multicanal**](#7-ranuras-ram-y-arquitectura-multicanal)
  - [7.1 Tipos de ranuras y módulos](#71-tipos-de-ranuras-y-módulos)
  - [7.2 Número de ranuras](#72-número-de-ranuras)
  - [7.3 Arquitectura de canales (Channel Architecture)](#73-arquitectura-de-canales-channel-architecture)
  - [7.4 Cómo aprovechar la arquitectura multicanal](#74-cómo-aprovechar-la-arquitectura-multicanal)
  - [7.5 Ejemplo de configuración óptima para gaming 2025](#75-ejemplo-de-configuración-óptima-para-gaming-2025)
  - [7.6 Consejos prácticos](#76-consejos-prácticos)
- [8. **Slots de expansión**](#8-slots-de-expansión)
  - [8.1 El Bus PCI Express (PCIe): Funcionamiento y Estructura](#81-el-bus-pci-express-pcie-funcionamiento-y-estructura)
    - [8.1.1 Estructura y concepto de "líneas" (lanes):](#811-estructura-y-concepto-de-líneas-lanes)
    - [8.1.2 Ventajas técnicas de PCIe:](#812-ventajas-técnicas-de-pcie)
    - [8.1.3 Versiones PCIe y ancho de banda por línea:](#813-versiones-pcie-y-ancho-de-banda-por-línea)
    - [8.1.4 Cómo afecta al usuario:](#814-cómo-afecta-al-usuario)
    - [8.1.5 Tipos físicos de slots y ejemplos de uso](#815-tipos-físicos-de-slots-y-ejemplos-de-uso)
  - [8.2 M.2](#82-m2)
    - [8.2.1 Ejemplo de configuración](#821-ejemplo-de-configuración)
    - [8.2.2 Consejos técnicos y consideraciones](#822-consejos-técnicos-y-consideraciones)
- [9. **VRM (Voltage Regulator Module)**](#9-vrm-voltage-regulator-module)
  - [9.1. Concepto y función esencial](#91-concepto-y-función-esencial)
  - [9.2.  Estructura de un VRM moderno](#92--estructura-de-un-vrm-moderno)
  - [9.3. Importancia del VRM en 2025](#93-importancia-del-vrm-en-2025)
  - [9.4. Número de fases y su relevancia](#94-número-de-fases-y-su-relevancia)
  - [9.5. Consejos de usuario y técnico](#95-consejos-de-usuario-y-técnico)
- [10. **Nuevas tecnologías**](#10-nuevas-tecnologías)
- [11. **Instalación y mantenimiento**](#11-instalación-y-mantenimiento)



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
