# Placa base (motherboard): guía exhaustiva 2025 (España)

> Objetivo: explicar **para qué sirve** cada elemento de una placa base y cómo elegir con criterio técnico (Intel y AMD, 2024–2025). Redacción en español de España.

---

## 1) Introducción
La **placa base** es el circuito impreso principal del PC. Sirve para:
- **Interconectar** CPU, memoria, almacenamiento y periféricos mediante buses de alta y baja velocidad (PCIe, USB, SATA, audio, red).
- **Distribuir y regular** la energía (VRM) para que llegue con la tensión y estabilidad correctas.
- **Aportar servicios de plataforma** (chipset/PCH): puertos USB, SATA, líneas PCIe adicionales, RAID, etc.
- **Inicializar y configurar** el hardware (firmware UEFI) y aplicar políticas de seguridad (Secure Boot, TPM/ fTPM).
- **Anclar físicamente** los componentes y encajar en el chasis según un **factor de forma**.

---

## 2) Factor de forma (form factor)
**Para qué sirve:** determina tamaño, taladros, posición de ranuras y conectores; condiciona flujo de aire, opciones de expansión y facilidad de montaje.

- **ATX** (305×244 mm): 7 ranuras, espacio para VRM robusto, varios M.2 y muchos puertos. Ideal para sobremesa versátil.
- **microATX** (244×244 mm): hasta 4 ranuras; equilibrio precio/prestaciones para aulas y oficinas.
- **Mini-ITX** (170×170 mm): ultra-compacta (1× PCIe x16). Exige chasis bien ventilado y cableado limpio.
- **E-ATX / SSI-EEB**: formatos grandes para estaciones de trabajo (más fases de VRM, más M.2 y más puertos).

**Comprobaciones clave antes de comprar:** compatibilidad con el chasis (standoffs), altura del disipador, longitud de GPU, tamaño y tipo de PSU, ubicación de conectores para un cableado ordenado.

---

## 3) Socket (zócalo de CPU)
**Para qué sirve:** une la CPU a la placa tanto **mecánica** como **eléctricamente**. Define qué familias de procesadores son compatibles y el sistema de anclaje del disipador.

### Intel (sobremesa y workstation recientes)
- **LGA1851** → plataforma **Core Ultra (Series 2) Arrow Lake** de sobremesa; placas con chipsets **Z890 / B860 / H810**. Sustituye a LGA1700. Sirve para habilitar DDR5 y PCIe 5.0 en muchas configuraciones y mejorar potencia/IA en desktop. :contentReference[oaicite:0]{index=0}
- **LGA1700** → **Core 12.ª/13.ª/14.ª gen** (Alder/Raptor Lake) con **Z790/H770/B760**. Gran parque instalado; útil para reutilizar DDR4 (en algunas placas) o DDR5. :contentReference[oaicite:1]{index=1}

**Workstation/servidor de interés docente**
- **LGA4677** → **Xeon W-2400/W-3400** (chipset W790). Sirve para plataformas con muchos carriles PCIe y memoria en varios canales (estaciones de trabajo).

### AMD (sobremesa y HEDT recientes)
- **AM5 (LGA1718)** → **Ryzen 7000/8000/9000** (Zen 4/Zen 5). Sirve para DDR5 y PCIe 5.0; chipsets **X870E/X870/B850/B840**, además de **X670E/X670/A620**. :contentReference[oaicite:2]{index=2}
- **AM4** → **Ryzen 1000–5000** (DDR4; PCIe 3/4 según CPU/chipset). Sigue siendo útil por coste/stock en laboratorios.
- **sTR5** (TRX50/WRX90) → **Threadripper 7000/PRO**. Sirve para muchas líneas PCIe y 4 u 8 canales de memoria en estaciones de trabajo. :contentReference[oaicite:3]{index=3}

**Buenas prácticas:** comprobar la **QVL** de CPU del fabricante de la placa; confirmar **kit de anclaje** del disipador para el socket específico.

---

## 4) Chipset (PCH)
**Para qué sirve:** amplía E/S más allá de la CPU: puertos USB (y sus velocidades), puertos SATA, **líneas PCIe adicionales**, RAID, y en algunos casos **overclock**. Determina la **segmentación** (entrada, mainstream, entusiasta).

### Intel (consumo)
- **Serie 700 (LGA1700)**  
  **Z790** (entusiasta, OC CPU/RAM, I/O abundante), **H770** (gama media), **B760** (mainstream). Sirven para montar desde equipos avanzados con OC hasta máquinas equilibradas sin OC. :contentReference[oaicite:4]{index=4}
- **Plataforma LGA1851 (Arrow Lake)**  
  **Z890** (tope de gama), **B860** (mainstream), **H810** (entrada). Sirven para los **Core Ultra Series 2** y consolidan soporte de DDR5/PCIe 5.0 según placa. :contentReference[oaicite:5]{index=5}

### AMD (AM5)
- **X870E / X870**: alta gama con foco en PCIe 5.0 y conectividad moderna; ideales para Ryzen 9000/8000/7000. :contentReference[oaicite:6]{index=6}
- **B850 / B840**: mainstream; **B850** refuerza prestaciones (más conectividad y Gen5 en M.2 en muchos modelos), **B840** acota costes y características. :contentReference[oaicite:7]{index=7}
- **X670E / X670 / A620**: siguen vigentes; X670E para equipos entusiastas con PCIe 5.0; A620 como entrada económica. :contentReference[oaicite:8]{index=8}

> Nota docente: AMD está consolidando la gama en torno a **B850** (con retirada progresiva de **B650**); conviene revisar disponibilidad local y hojas técnicas del fabricante. :contentReference[oaicite:9]{index=9}

---

## 5) VRM y alimentación
**Para qué sirve:** el **VRM** convierte los 12 V de la fuente en tensiones **bajas y estables** para CPU, iGPU y memoria. Un VRM de calidad mantiene frecuencia bajo carga, evita caídas de rendimiento y posibilita **overclock** en placas y CPUs que lo permiten.

- **Elementos clave:** fases (controlador PWM, MOSFETs, chokes, condensadores), **disipadores** con pads térmicos, y sensores térmicos.
- **Conectores de energía en la placa:**  
  - **ATX 24-pin** (principal de la placa).  
  - **EPS 8-pin (4+4)** para CPU; algunas placas añaden un **segundo EPS** para CPUs de alto consumo.  
- **Buenas prácticas:** asegurar flujo de aire sobre el VRM; no confundir cables **EPS** y **PCIe** de la PSU.

---

## 6) Bancos de memoria (DIMM)
**Para qué sirven:** alojan los módulos **DDR4** o **DDR5**. La placa determina número de ranuras y **canales** (lo habitual en consumo: **doble canal**).

- **DDR5 (AM5, LGA1851 y muchas LGA1700):** frecuencias elevadas con perfiles **EXPO/XMP**; más ancho de banda por canal.
- **DDR4 (parte de LGA1700 y todo AM4):** aún común por coste y disponibilidad.
- **ECC:** en consumo, ECC suele ser **no-buffered (UDIMM)** y su soporte depende de CPU y placa; en HEDT/workstation (sTR5, LGA4677) se usan **RDIMM ECC** con 4–8 canales.
- **Para montar bien:** poblar primero las ranuras indicadas (normalmente **A2/B2**), activar EXPO/XMP y comprobar estabilidad. Revisar **QVL** de la placa.

---

## 7) Ranuras PCI Express
**Para qué sirve:** conectar **tarjetas de expansión** (gráficas, controladoras de almacenamiento, tarjetas de red, capturadoras, etc.) con ancho de banda escalable.

- **Tamaños:** x16 / x8 / x4 / x1 (longitud física).  
- **Generaciones:** 3.0 / 4.0 / **5.0** (más GB/s por línea). Retrocompatibles a la menor versión.  
- **Topologías típicas:** 1× x16 desde la CPU (GPU); bifurcación a **x8/x8** si se puebla una segunda ranura de alto ancho de banda. Varias x4/x1 desde el chipset.  
- **Consideración práctica (AM5):** algunas placas **B650** permitían de forma no oficial PCIe 5.0 en GPU y lo han retirado en BIOS recientes por estabilidad; en **B850/X870** la segmentación de PCIe 5.0 es más clara. :contentReference[oaicite:10]{index=10}

---

## 8) Almacenamiento: M.2 y SATA
### Zócalos **M.2**
**Para qué sirven:** conectar SSD **NVMe** (PCIe) de muy alto rendimiento y, en algunos zócalos, SSD **SATA** M.2. Eliminan cables de datos y mejoran el flujo de aire.

- **Claves (keys):** **M** (NVMe x4 habitual), **B** (NVMe x2 / SATA), **B+M** (compatibilidad física, a costa de rendimiento).  
- **Longitudes:** 2230 / 2242 / 2260 / **2280** / 22110.  
- **Generación PCIe:** 4.0 y **5.0** en placas modernas (el 5.0 exige disipadores adecuados).  
- **Importante:** algunos zócalos **comparten** líneas con SATA o con la ranura PCIe principal; al poblarlos, se desactiva un puerto o baja un enlace. Consultar el **mapa de líneas** de la placa.

### Puertos **SATA**
**Para qué sirven:** conectar SSD/HDD de 2,5″/3,5″ con coste por GB muy bajo. Ideales para bibliotecas de datos, copias y aulas.

---

## 9) Puertos traseros e internos (headers)
**Para qué sirven:** exponer conectividad al exterior y al panel frontal del chasis.

- **USB:**  
  - Traseros: USB-A y **USB-C** en velocidades que van de 5 Gb/s a 20 Gb/s e incluso 40 Gb/s en placas con **USB4/Thunderbolt**.  
  - Internos: **USB 2.0 (9 pines)**, **USB 3.x (19/20 pines)** y **Type-E** para **USB-C frontal**.
- **Vídeo integrado (HDMI/DisplayPort):** activo si la CPU tiene **gráfica integrada**; útil para diagnóstico o equipos de ofimática.
- **Red:** Ethernet **1G / 2.5G / 10G**; Wi-Fi **6/6E/7** en modelos con módulo inalámbrico y antenas SMA.
- **Audio:** códecs Realtek ALCxxx con salidas analógicas y **S/PDIF**; el diseño del PCB suele aislar la zona de audio para reducir interferencias.
- **Iluminación:** **ARGB 5 V 3-pin** y **RGB 12 V 4-pin** (no intercambiables).
- **Front-panel:** **PWR_SW**, **RESET_SW**, **PWR_LED**, **HDD_LED** para el frontal de la caja.
- **Ventiladores/bombas:** **CPU_FAN**, **CPU_OPT**, **AIO_PUMP**, **SYS_FAN** con control PWM/DC.

---

## 10) Firmware UEFI (BIOS moderna)
**Para qué sirve:** realizar el **POST**, detectar hardware, aplicar la configuración y arrancar el sistema operativo.

- **Ajustes habituales:** orden de arranque, perfiles **XMP/EXPO**, **curvas de ventiladores**, límites de potencia, opciones de **seguridad** (Secure Boot, fTPM/Intel PTT).  
- **Actualización:** utilidades como **Flashback / EZ-Flash** permiten flashear sin CPU o desde la propia UEFI. Conviene actualizar sólo cuando aporta **soporte o estabilidad** (por ejemplo, nuevas CPUs o memoria).  
- **Perfiles:** guarda perfiles de ventilación y memoria antes de actualizar.

---

## 11) Sensores y diagnóstico
**Para qué sirve:** monitorizar temperaturas, tensiones, velocidad de ventiladores y estado de arranque.

- **Q-LED / códigos POST / displays de dos dígitos:** ayudan a localizar fallos (RAM, CPU, VGA, BOOT).  
- **Botones de placa (Power/Reset/Clear-CMOS/Flashback):** facilitan pruebas en bancada.

---

## 12) Diseño del PCB y calidad de componentes
**Para qué sirve:** mantener **integridad de señal** y **durabilidad**.

- **Capas** y separación de zonas (alta velocidad, audio, RF) reducen interferencias.  
- **Blindajes** metálicos en controladoras sensibles (audio, red) y **backplate** en placas avanzadas mejoran rigidez y temperaturas.  
- **Protecciones ESD** y componentes de **grado sólido** alargan la vida útil.

---

## 13) Selección rápida según uso
- **Entusiasta/OC (Intel):** **Z790** (LGA1700) o **Z890** (LGA1851) con DDR5 y varias M.2; ideal para i7/i9 y gráficas de gama alta. :contentReference[oaicite:11]{index=11}  
- **Equilibrio (Intel):** **B760/H770** (14ª/13ª/12ª gen) o **B860** (Core Ultra Series 2). :contentReference[oaicite:12]{index=12}  
- **Entusiasta/OC (AMD):** **X870E/X670E** (AM5) para Ryzen 7/9 con PCIe 5.0 sólido y buena dotación de M.2. :contentReference[oaicite:13]{index=13}  
- **Equilibrio (AMD):** **B850** (mainstream moderno) con DDR5 y conectividad actual; **B840** como opción más económica. :contentReference[oaicite:14]{index=14}  
- **Workstation/HEDT:** **sTR5 TRX50/WRX90** (Threadripper) o **LGA4677/W790** (Xeon W): muchas líneas PCIe y memoria multicanal. :contentReference[oaicite:15]{index=15}

---

## 14) Listados de referencia (actualizados)

### 14.1 Chipsets destacados (2024–2025)
- **Intel:** **Z890**, **B860**, **H810** (LGA1851 / Arrow Lake); **Z790**, **H770**, **B760** (LGA1700 / Alder-Raptor). :contentReference[oaicite:16]{index=16}
- **AMD AM5:** **X870E / X870 / B850 / B840 / X670E / X670 / A620**. (AMD mantiene hoja oficial con especificaciones y carriles). :contentReference[oaicite:17]{index=17}

### 14.2 Sockets más relevantes hoy
- **Intel:** **LGA1851** (Core Ultra Series 2 / Arrow Lake), **LGA1700** (Core 12.ª–14.ª). :contentReference[oaicite:18]{index=18}  
- **AMD:** **AM5** (Ryzen 7000/8000/9000), **AM4** (Ryzen 1000–5000), **sTR5** (Threadripper 7000/PRO). :contentReference[oaicite:19]{index=19}


---
