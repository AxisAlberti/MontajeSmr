---
layout: default
title: 📚 Chipset — Mantenimiento y Montaje de Equipos Informáticos
---

- [1. El Chipset](#1-el-chipset)  
  - [1.1 Concepto General](#11-concepto-general)  
  - [1.2 Funciones Principales](#12-funciones-principales)  
  - [1.3 Comunicación CPU–Chipset](#13-comunicación-cpu–chipset)  
  - [1.4 Chipsets Intel (Actualizados a 2025)](#14-chipsets-intel-actualizados-a-2025)  
  - [1.5 Chipsets AMD (Actualizados a 2025)](#15-chipsets-amd-actualizados-a-2025)  
  - [1.6 Elección del Chipset](#16-elección-del-chipset)  
  - [1.7 Importancia actual del Chipset](#17-importancia-actual-del-chipset)  
  - [1.8 Resumen Técnico](#18-resumen-técnico)

# 1. El Chipset

El **chipset** es el **centro de control de la placa base**, responsable de coordinar la comunicación entre el **procesador, la memoria RAM, los dispositivos de almacenamiento y los periféricos**.  
Su diseño determina qué tecnologías soporta una placa, su capacidad de expansión y el rendimiento global del sistema.

---

## 1.1 Concepto General

El chipset actúa como un **controlador inteligente** que dirige el flujo de datos dentro del ordenador. Aunque no ejecuta instrucciones como la CPU, es esencial para que todos los componentes puedan comunicarse correctamente.

Originalmente se dividía en:
- **Northbridge:** gestionaba la CPU, la memoria y la GPU.  
- **Southbridge:** controlaba los periféricos, puertos y almacenamiento.  

Hoy día, esas funciones se integran en un solo chip:
- En **Intel**, se denomina **PCH (Platform Controller Hub)**.  
- En **AMD**, se conoce como **Promontory** o **FCH (Fusion Controller Hub)**.

---

## 1.2 Funciones Principales

| Función | Descripción |
|----------|--------------|
| **Gestión de buses** | Control de los canales de comunicación (PCIe, SATA, USB, etc.). |
| **Conectividad** | Define cuántos puertos USB, M.2 o PCIe puede tener la placa base. |
| **Gestión energética** | Supervisa el consumo y regula los estados de suspensión. |
| **Almacenamiento** | Administra discos SATA, NVMe y configuraciones RAID. |
| **Red y audio integrados** | Controla interfaces Ethernet, Wi-Fi, Bluetooth y códecs de sonido. |

El chipset **determina el potencial real** del sistema: qué procesadores admite, cuántos dispositivos puede conectar y qué rendimiento máximo se puede obtener.

---

## 1.3 Comunicación CPU–Chipset

La CPU y el chipset se comunican mediante **buses de alta velocidad**:

| Fabricante | Enlace de comunicación | Velocidad estimada | Descripción |
|-------------|------------------------|--------------------|--------------|
| **Intel** | **DMI 3.0 / 4.0 (Direct Media Interface)** | 3.93–7.86 GB/s | Conecta la CPU con el PCH. |
| **AMD** | **Infinity Fabric** | 18–64 GB/s | Interconecta CPU, GPU y chipset con baja latencia. |

---

## 1.4 Chipsets Intel (Actualizados a 2025)

| Chipset | Gama | Plataforma | Características principales |
|----------|------|-------------|-----------------------------|
| **Z890** | Alta | LGA1851 (Intel 15ª Gen) | Soporte DDR5-8800, PCIe 5.0 total, Thunderbolt 5, OC avanzado. |
| **Z790** | Alta | LGA1700 (12ª–14ª Gen) | Overclocking, PCIe 5.0, DDR5, 24 puertos USB, 20 líneas PCIe extra. |
| **B760** | Media | LGA1700 | DDR5/DDR4, PCIe 5.0 (x16), sin OC, gran equilibrio rendimiento/precio. |
| **H770** | Media | LGA1700 | Similares al B760 pero con más líneas PCIe y USB 4.0 opcional. |
| **H610** | Básica | LGA1700 | PCIe 4.0, DDR4, conectividad limitada, ideal para equipos de oficina. |
| **W790** | Profesional | LGA4677 (Xeon) | Hasta 112 líneas PCIe 5.0, DDR5 ECC, 4 canales, ideal para servidores. |
| **Q670 / Q870** | Empresarial | LGA1700/LGA1851 | Seguridad empresarial (Intel vPro), gestión remota y fiabilidad. |
| **Z690 / B660 / H670** | Generación anterior | LGA1700 (12ª Gen) | DDR4/DDR5, PCIe 5.0 parcial, soporte NVMe múltiple. |

---

## 1.5 Chipsets AMD (Actualizados a 2025)

| Chipset | Gama | Plataforma | Características principales |
|----------|------|-------------|-----------------------------|
| **X870E** | Alta | AM5 (Ryzen 9000 / 8000 / 7000) | PCIe 5.0 completo, DDR5-8000, USB4, OC avanzado, doble chipset físico. |
| **X870** | Alta | AM5 | PCIe 5.0 parcial, DDR5, USB 4.0, soporte para Smart Access Storage. |
| **B850E** | Media-alta | AM5 | PCIe 5.0 para GPU y SSD, DDR5, eficiencia térmica mejorada. |
| **B850** | Media | AM5 | DDR5, PCIe 4.0/5.0 parcial, buen rendimiento con bajo consumo. |
| **A620** | Básica | AM5 | DDR5, PCIe 4.0, sin overclocking, bajo coste y gran estabilidad. |
| **X670E / X670 / B650E / B650** | Generaciones previas | AM5 | Soporte DDR5, PCIe 5.0 opcional, USB 4.0 y BIOS actualizables. |
| **WRX90 / TRX50** | Profesional | sTR5 (Threadripper) | Hasta 128 líneas PCIe 5.0, 8 canales DDR5 ECC, para estaciones de trabajo. |

---

## 1.6 Elección del Chipset

| Tipo de usuario | Recomendación | Motivo |
|------------------|---------------|--------|
| **Gaming / Creativo** | Intel Z790 / AMD X870E | Máximo rendimiento, OC, conectividad PCIe 5.0 y DDR5. |
| **Desarrollo y programación** | Intel B760 / AMD B850 | Gran rendimiento, bajo consumo, amplia conectividad. |
| **Ofimática / Educación** | Intel H610 / AMD A620 | Simplicidad, bajo coste, estabilidad y consumo reducido. |
| **Estaciones de trabajo** | Intel W790 / AMD WRX90 | Máximo número de líneas PCIe, DDR5 ECC, fiabilidad profesional. |

---

## 1.7 Importancia actual del Chipset

El chipset moderno:
- Determina **qué procesadores y memorias** puede usar la placa base.  
- Define el número de **puertos y líneas PCIe** disponibles.  
- Controla el **rendimiento energético** y la **eficiencia térmica**.  
- Asegura la **compatibilidad futura** mediante actualizaciones de BIOS y firmware.  
- Permite el uso de tecnologías **PCIe 5.0, DDR5, USB 4.0 y Thunderbolt 5**.  

En la práctica, el chipset es **la pieza que decide el futuro del equipo**: su velocidad, capacidad de expansión y compatibilidad con hardware emergente.

---

## 1.8 Resumen Técnico

- El chipset actúa como **núcleo lógico y controlador de datos**.  
- Es vital para **la estabilidad, la compatibilidad y el rendimiento global**.  
- Los chipsets modernos integran **tecnologías de conectividad avanzada**.  
- Su elección debe adaptarse al **uso profesional o formativo** del sistema.  

---

*Actualizado — Octubre 2025*

