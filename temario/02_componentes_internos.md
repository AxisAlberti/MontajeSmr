# Índice

- **1. Placa base (motherboard): guía exhaustiva 2025 (España)**  :contentReference[oaicite:0]{index=0}
  - 1.1 Introducción
  - 1.2 Factor de forma (form factor)
  - 1.3 Socket (zócalo de CPU)
    - 1.3.1 Intel (sobremesa y workstation recientes)
    - 1.3.2 AMD (sobremesa y HEDT recientes)
  - 1.4 Chipset (PCH)
    - 1.4.1 Intel (consumo)
    - 1.4.2 AMD (AM5)
  - 1.5 VRM y alimentación
  - 1.6 Bancos de memoria (DIMM)
  - 1.7 Ranuras PCI Express
  - 1.8 Almacenamiento: M.2 y SATA
    - 1.8.1 Zócalos M.2
    - 1.8.2 Puertos SATA
  - 1.9 Puertos traseros e internos (headers)
  - 1.10 Firmware UEFI (BIOS moderna)
  - 1.11 Sensores y diagnóstico
  - 1.12 Diseño del PCB y calidad
  - 1.13 Selección rápida según uso
  - 1.14 Listados de referencia (2024–2025)
    - 1.14.1 Chipsets destacados
    - 1.14.2 Sockets más relevantes
  - 1.15 Checklist de montaje y verificación

- **2. BIOS, memoria CMOS, Dual BIOS y sistemas de reseteo — guía exhaustiva (España)**  :contentReference[oaicite:1]{index=1}
  - 2.1 Introducción
  - 2.2 BIOS vs UEFI
  - 2.3 Memoria CMOS, RTC y NVRAM
  - 2.4 Dual BIOS (BIOS principal + respaldo)
  - 2.5 Sistemas de reseteo (restablecer ajustes)
    - 2.5.1 Desde la UEFI
    - 2.5.2 Botón Clear CMOS (CLR_CMOS)
    - 2.5.3 Jumper CLR_CMOS (2/3 pines)
    - 2.5.4 Retirar la pila CR2032
    - 2.5.5 BIOS Flashback / Q-Flash Plus / Flash BIOS Button
    - 2.5.6 Arranque de rescate en Dual BIOS
    - 2.5.7 Borrar contraseñas de BIOS
  - 2.6 Actualización del firmware (flasheo) con seguridad
  - 2.7 Diagnóstico y síntomas típicos
  - 2.8 Procedimientos recomendados (paso a paso)
  - 2.9 Buenas prácticas en aula/taller

---

# 1. Placa base (motherboard): guía exhaustiva 2025 (España)

> Objetivo: explicar **para qué sirve** cada elemento de una placa base y cómo elegir con criterio técnico (Intel y AMD, 2024–2025). Redacción en español de España. :contentReference[oaicite:2]{index=2}

---

## 1.1 Introducción
La **placa base** es el circuito impreso principal del PC. Sirve para:
- **Interconectar** CPU, memoria, almacenamiento y periféricos mediante buses de alta y baja velocidad (PCIe, USB, SATA, audio, red).
- **Distribuir y regular** la energía (VRM) para que llegue con la tensión y estabilidad correctas.
- **Aportar servicios de plataforma** (chipset/PCH): puertos USB, SATA, líneas PCIe adicionales, RAID, etc.
- **Inicializar y configurar** el hardware (firmware UEFI) y aplicar políticas de seguridad (Secure Boot, TPM/fTPM).
- **Anclar físicamente** los componentes y encajar en el chasis según un **factor de forma**. :contentReference[oaicite:3]{index=3}

---

## 1.2 Factor de forma (form factor)
**Para qué sirve:** determina tamaño, taladros, posición de ranuras y conectores; condiciona flujo de aire, opciones de expansión y facilidad de montaje.

- **ATX** (305×244 mm): 7 ranuras, espacio para VRM robusto, varios M.2 y muchos puertos. Ideal para sobremesa versátil.
- **microATX** (244×244 mm): hasta 4 ranuras; equilibrio precio/prestaciones para aulas y oficinas.
- **Mini-ITX** (170×170 mm): ultra-compacta (1× PCIe x16). Exige chasis bien ventilado y cableado limpio.
- **E-ATX / SSI-EEB**: formatos grandes para estaciones de trabajo (más fases de VRM, más M.2 y más puertos).

**Comprobaciones clave antes de comprar:** compatibilidad con el chasis (standoffs), altura del disipador, longitud de GPU, tamaño y tipo de PSU, ubicación de conectores para un cableado ordenado. :contentReference[oaicite:4]{index=4}

---

## 1.3 Socket (zócalo de CPU)
**Para qué sirve:** une la CPU a la placa tanto **mecánica** como **eléctricamente**. Define qué familias de procesadores son compatibles y el sistema de anclaje del disipador.

### 1.3.1 Intel (sobremesa y workstation recientes)
- **LGA1851** → plataforma **Core Ultra (Series 2) Arrow Lake** de sobremesa; placas con chipsets **Z890 / B860 / H810**. Sustituye a LGA1700. Sirve para habilitar DDR5 y PCIe 5.0 en muchas configuraciones y mejorar potencia/IA en desktop.
- **LGA1700** → **Core 12.ª/13.ª/14.ª gen** (Alder/Raptor Lake) con **Z790/H770/B760**. Gran parque instalado; útil para reutilizar DDR4 (en algunas placas) o DDR5.

**Workstation/servidor de interés docente**
- **LGA4677** → **Xeon W-2400/W-3400** (chipset W790). Plataformas con muchos carriles PCIe y memoria en varios canales (estaciones de trabajo). :contentReference[oaicite:5]{index=5}

### 1.3.2 AMD (sobremesa y HEDT recientes)
- **AM5 (LGA1718)** → **Ryzen 7000/8000/9000** (Zen 4/Zen 5). DDR5 y PCIe 5.0; chipsets **X870E/X870/B850/B840**, además de **X670E/X670/A620**.
- **AM4** → **Ryzen 1000–5000** (DDR4; PCIe 3/4 según CPU/chipset). Muy presente por coste/stock en laboratorios.
- **sTR5** (TRX50/WRX90) → **Threadripper 7000/PRO**. Muchas líneas PCIe y 4 u 8 canales de memoria en estaciones de trabajo. :contentReference[oaicite:6]{index=6}

**Buenas prácticas:** comprobar la **QVL** de CPU del fabricante de la placa; confirmar **kit de anclaje** del disipador para el socket específico. :contentReference[oaicite:7]{index=7}

---

## 1.4 Chipset (PCH)
**Para qué sirve:** amplía E/S más allá de la CPU: puertos USB (y sus velocidades), puertos SATA, **líneas PCIe adicionales**, RAID, y en algunos casos **overclock**. Determina la **segmentación** (entrada, mainstream, entusiasta).

### 1.4.1 Intel (consumo)
- **Serie 700 (LGA1700)**: **Z790** (entusiasta, OC CPU/RAM, I/O abundante), **H770** (gama media), **B760** (mainstream).
- **Plataforma LGA1851 (Arrow Lake)**: **Z890** (tope de gama), **B860** (mainstream), **H810** (entrada). :contentReference[oaicite:8]{index=8}

### 1.4.2 AMD (AM5)
- **X870E / X870**: alta gama con foco en PCIe 5.0 y conectividad moderna; ideales para Ryzen 9000/8000/7000.
- **B850 / B840**: mainstream; **B850** refuerza prestaciones (más conectividad y Gen5 en M.2 en muchos modelos), **B840** acota costes y características.
- **X670E / X670 / A620**: siguen vigentes; X670E para equipos entusiastas con PCIe 5.0; A620 como entrada económica.

> Nota docente: AMD está consolidando la gama en torno a **B850** (retirada progresiva de **B650**); revisar disponibilidad y hojas técnicas del fabricante. :contentReference[oaicite:9]{index=9}

---

## 1.5 VRM y alimentación
**Para qué sirve:** el **VRM** convierte los 12 V de la fuente en tensiones **bajas y estables** para CPU, iGPU y memoria. Un VRM de calidad mantiene frecuencia bajo carga, evita caídas de rendimiento y posibilita **overclock** en placas y CPUs que lo permiten.

- **Elementos clave:** fases (controlador PWM, MOSFETs, chokes, condensadores), **disipadores** con pads térmicos, y sensores térmicos.
- **Conectores de energía en la placa:** **ATX 24-pin** (principal) y **EPS 8-pin (4+4)** para CPU; algunas placas añaden un **segundo EPS** para CPUs de alto consumo.
- **Buenas prácticas:** asegurar flujo de aire sobre el VRM; no confundir cables **EPS** y **PCIe** de la PSU. :contentReference[oaicite:10]{index=10}

---

## 1.6 Bancos de memoria (DIMM)
**Para qué sirve:** alojan los módulos **DDR4** o **DDR5**. La placa determina número de ranuras y **canales** (lo habitual en consumo: **doble canal**).

- **DDR5 (AM5, LGA1851 y muchas LGA1700):** frecuencias elevadas con perfiles **EXPO/XMP**; más ancho de banda por canal.
- **DDR4 (parte de LGA1700 y todo AM4):** aún común por coste y disponibilidad.
- **ECC:** en consumo, ECC suele ser **UDIMM** y su soporte depende de CPU y placa; en HEDT/workstation (sTR5, LGA4677) se usan **RDIMM ECC** con 4–8 canales.
- **Montaje:** poblar primero **A2/B2**, activar EXPO/XMP y comprobar estabilidad. Revisar **QVL** de la placa. :contentReference[oaicite:11]{index=11}

---

## 1.7 Ranuras PCI Express
**Para qué sirve:** conectar **tarjetas de expansión** (gráficas, controladoras de almacenamiento, tarjetas de red, capturadoras, etc.) con ancho de banda escalable.

- **Tamaños:** x16 / x8 / x4 / x1 (longitud física).  
- **Generaciones:** 3.0 / 4.0 / **5.0** (más GB/s por línea). Retrocompatibles a la menor versión.  
- **Topologías típicas:** 1× x16 desde la CPU (GPU); bifurcación a **x8/x8** si se puebla una segunda ranura de alto ancho de banda. Varias x4/x1 desde el chipset.  
- **Consideración (AM5):** en placas **B650** algunos fabricantes retiraron PCIe 5.0 para GPU por estabilidad en BIOS recientes; en **B850/X870** la segmentación Gen5 es más clara. :contentReference[oaicite:12]{index=12}

---

## 1.8 Almacenamiento: M.2 y SATA

### 1.8.1 Zócalos **M.2**
**Para qué sirve:** conectar SSD **NVMe** (PCIe) de muy alto rendimiento y, en algunos zócalos, SSD **SATA** M.2. Eliminan cables de datos y mejoran el flujo de aire.

- **Claves (keys):** **M** (NVMe x4 habitual), **B** (NVMe x2 / SATA), **B+M** (compatibilidad física, con menor rendimiento).  
- **Longitudes:** 2230 / 2242 / 2260 / **2280** / 22110.  
- **Generación PCIe:** 4.0 y **5.0** en placas modernas (el 5.0 exige disipadores adecuados).  
- **Mapa de líneas:** algunos zócalos **comparten** líneas con SATA o con la ranura PCIe principal; al poblarlos, se desactiva un puerto o baja un enlace. :contentReference[oaicite:13]{index=13}

### 1.8.2 Puertos **SATA**
Conectar SSD/HDD de 2,5″/3,5″ con coste por GB bajo. Ideales para bibliotecas de datos, copias y aulas. :contentReference[oaicite:14]{index=14}

---

## 1.9 Puertos traseros e internos (headers)
Conectividad exterior y del panel frontal del chasis.

- **USB:** traseros (USB-A/USB-C, 5–20 Gb/s y 40 Gb/s en USB4/Thunderbolt) e internos (**USB 2.0**, **USB 3.x**, **Type-E** para USB-C frontal).
- **Vídeo integrado (HDMI/DP):** activo si la CPU dispone de **gráfica integrada** (diagnóstico/ofimática).
- **Red:** Ethernet **1G/2.5G/10G**; Wi-Fi **6/6E/7** con antenas SMA según placa.
- **Audio:** códecs Realtek ALCxxx con salidas analógicas y **S/PDIF**; PCB con zona de audio aislada.
- **Iluminación:** **ARGB 5 V 3-pin** y **RGB 12 V 4-pin** (no intercambiables).
- **Front-panel:** **PWR_SW**, **RESET_SW**, **PWR_LED**, **HDD_LED**.
- **Ventiladores/bombas:** **CPU_FAN**, **CPU_OPT**, **AIO_PUMP**, **SYS_FAN** (PWM/DC). :contentReference[oaicite:15]{index=15}

---

## 1.10 Firmware UEFI (BIOS moderna)
Realiza **POST**, detecta hardware, aplica la configuración y arranca el SO.

- **Ajustes:** orden de arranque, **XMP/EXPO**, **curvas de ventiladores**, límites de potencia, **Secure Boot**, **fTPM/Intel PTT**.  
- **Actualización:** **Flashback / EZ-Flash / M-Flash / Q-Flash**; actualizar cuando aporte soporte/estabilidad.  
- **Perfiles:** guardar perfiles de ventilación y memoria antes de flashear. :contentReference[oaicite:16]{index=16}

---

## 1.11 Sensores y diagnóstico
- **Q-LED / códigos POST / displays** de dos dígitos para localizar fallos (RAM, CPU, VGA, BOOT).  
- **Botones en placa (Power/Reset/Clr-CMOS/Flashback)** para pruebas en bancada. :contentReference[oaicite:17]{index=17}

---

## 1.12 Diseño del PCB y calidad
- **Capas** y **zonas** aisladas (alta velocidad, audio, RF) para integridad de señal.  
- **Blindajes**, **backplate** y disipadores M.2 para rigidez y temperaturas.  
- **Protecciones ESD** y componentes de **grado sólido** para durabilidad. :contentReference[oaicite:18]{index=18}

---

## 1.13 Selección rápida según uso
- **Entusiasta/OC (Intel):** **Z790** (LGA1700) o **Z890** (LGA1851) con DDR5 y varias M.2; i7/i9 y GPU alta.  
- **Equilibrio (Intel):** **B760/H770** (12.ª–14.ª gen) o **B860** (Core Ultra Series 2).  
- **Entusiasta/OC (AMD):** **X870E/X670E** (AM5) para Ryzen 7/9 con PCIe 5.0 sólido y varios M.2.  
- **Equilibrio (AMD):** **B850** (mainstream) con DDR5 y conectividad actual; **B840** opción más económica.  
- **Workstation/HEDT:** **sTR5 TRX50/WRX90** (Threadripper) o **LGA4677/W790** (Xeon W): muchas líneas PCIe y memoria multicanal. :contentReference[oaicite:19]{index=19}

---

## 1.14 Listados de referencia (2024–2025)

### 1.14.1 Chipsets destacados
- **Intel:** **Z890**, **B860**, **H810** (LGA1851 / Arrow Lake); **Z790**, **H770**, **B760** (LGA1700 / Alder-Raptor).
- **AMD (AM5):** **X870E / X870 / B850 / B840 / X670E / X670 / A620**. :contentReference[oaicite:20]{index=20}

### 1.14.2 Sockets más relevantes
- **Intel:** **LGA1851** (Core Ultra Series 2 / Arrow Lake), **LGA1700** (Core 12.ª–14.ª).  
- **AMD:** **AM5** (Ryzen 7000/8000/9000), **AM4** (Ryzen 1000–5000), **sTR5** (Threadripper 7000/PRO). :contentReference[oaicite:21]{index=21}

---

## 1.15 Checklist de montaje y verificación
1. Actualiza UEFI **si** la placa lo requiere para tu CPU.  
2. Coloca **standoffs** en el chasis y atornilla la placa.  
3. Instala CPU y disipador (pasta térmica adecuada); RAM en **A2/B2**.  
4. Monta SSD M.2 con **disipador** y tornillo; respeta la longitud.  
5. Conecta **ATX 24-pin** y **EPS 8-pin**; añade GPU y periféricos.  
6. Conecta **front-panel** y **USB/Audio** frontales según manual.  
7. Primer POST con lo mínimo; activa **EXPO/XMP**, ajusta **curvas** y verifica temperaturas.  
8. Comprueba enlace de GPU (x16/x8) y que M.2 no desactive puertos que necesitas. :contentReference[oaicite:22]{index=22}

---

# 2. BIOS, memoria CMOS, Dual BIOS y sistemas de reseteo — guía exhaustiva (España)

> Objetivo: comprender qué es la BIOS/UEFI, cómo y dónde se guardan sus ajustes (CMOS/NVRAM), qué aporta **Dual BIOS** y cuáles son los **métodos de reseteo** y recuperación más seguros en placas base modernas. :contentReference[oaicite:23]{index=23}

---

## 2.1 Introducción
El **firmware** (BIOS clásica o **UEFI** moderna) inicializa el hardware, realiza el **POST**, aplica la configuración guardada (arranque, XMP/EXPO, potencia, seguridad) y entrega el control al sistema operativo.  
Históricamente, los ajustes residían en **CMOS RAM** alimentada por la **pila CR2032**; hoy gran parte vive en **flash SPI/NVRAM**, pero la pila sigue manteniendo el **RTC** (reloj en tiempo real) y ciertos estados. :contentReference[oaicite:24]{index=24}

---

## 2.2 BIOS vs UEFI
- **BIOS (Legacy):** INT 13h/MBR; limitaciones en discos >2 TB y arranque moderno.  
- **UEFI (moderna):** GPT, **Secure Boot**, utilidades gráficas integradas (flash, diagnóstico), drivers pre-arranque. El término “BIOS” se usa coloquialmente para UEFI.

**Ajustes típicos:** orden de arranque, **XMP/EXPO**, curvas de ventilador, límites de potencia/voltaje, **Secure Boot**, **fTPM/Intel PTT**, activación de periféricos y puertos SATA/M.2. :contentReference[oaicite:25]{index=25}

---

## 2.3 Memoria CMOS, RTC y NVRAM
- **CMOS RAM:** pequeña RAM de bajo consumo (equipos clásicos) que guardaba parámetros y hora; necesita **CR2032**.  
- **RTC:** reloj con cristal de 32,768 kHz que mantiene **fecha/hora** apagado el equipo.  
- **NVRAM / SPI flash (actual):** configuración y firmware en chip de **flash**; la pila mantiene el **RTC** y, según placa, algunos estados menores.

**Pila agotada:** hora/fecha incorrectas, “CMOS checksum error”, pérdida de ajustes (en placas antiguas). → Sustituir **CR2032** (polaridad “+” arriba) y reconfigurar UEFI. :contentReference[oaicite:26]{index=26}

---

## 2.4 Dual BIOS (BIOS principal + respaldo)
**Dual BIOS** integra dos chips de firmware: **principal** y **respaldo**.

- **Redundancia:** si la actualización falla o se corrompe el chip principal, el sistema puede **arrancar desde el respaldo** (automático o con **selector físico**).  
- **Copia espejo:** algunas utilidades permiten **replicar** la versión estable en el chip secundario.  
- **Uso docente:** ideal para enseñar actualización segura y recuperación tras fallos. :contentReference[oaicite:27]{index=27}

---

## 2.5 Sistemas de reseteo (restablecer ajustes)

### 2.5.1 Desde la UEFI
- **Load Optimized Defaults / Restore Defaults**. Útil cuando el equipo arranca pero está inestable.

### 2.5.2 Botón **Clear CMOS** (CLR_CMOS)
- En panel trasero o PCB. Procedimiento habitual: **apagar**, **cortar corriente**, **pulsar** 5–10 s, alimentar y arrancar.

### 2.5.3 **Jumper** CLR_CMOS (2/3 pines)
- Con el equipo sin corriente: mover el **jumper** (1–2 → 2–3) o **puentear** pines unos segundos y devolverlo. Consultar manual.

### 2.5.4 Retirar la **pila CR2032**
- Quitar 1–5 minutos (pulsar power unos segundos ayuda a descargar), volver a poner y arrancar. En placas modernas puede no borrar todo; combinar con CLR_CMOS.

### 2.5.5 **BIOS Flashback / Q-Flash Plus / Flash BIOS Button**
- Recuperación desde **USB** sin CPU/RAM/GPU (según modelo).  
  1) Descargar BIOS correcta. 2) USB **FAT32**, copiar/renombrar si procede.  
  3) Con alimentación, insertar en **puerto dedicado** y pulsar **Flashback** hasta parpadeo del LED.  
  4) Esperar fin del proceso.

### 2.5.6 Arranque de **rescate** en Dual BIOS
- Conmutar a **BIOS_B** (si hay selector) o dejar que el **failover** automático actúe tras varios fallos de POST. Luego reflashear **BIOS_A**.

### 2.5.7 Borrar **contraseñas** de BIOS
- En muchas placas, **CLR_CMOS** limpia Supervisor/Setup y Power-On. En portátiles/proprietarias puede requerir procedimientos específicos. :contentReference[oaicite:28]{index=28}

---

## 2.6 Actualización del firmware (flasheo) con seguridad
- **Actualizar cuando:** soporte de **CPU/memoria**, estabilidad o seguridad.  
- **Evitar cuando:** el equipo es estable y no necesitas cambios.  
- **Buenas prácticas:** usar **EZ-Flash/M-Flash/Q-Flash** o **Flashback**, no interrumpir energía, **Defaults** tras flasheo y restaurar perfiles guardados. :contentReference[oaicite:29]{index=29}

---

## 2.7 Diagnóstico y síntomas típicos
- **Pitidos/códigos POST** → apunta al subsistema (RAM, CPU, VGA, BOOT).  
- **Bucle de arranque** tras toquetear memoria/OC → **Clear CMOS**, un solo módulo en **A2**, Defaults, reactivar XMP/EXPO con prudencia.  
- **Hora reseteada** → **CR2032** agotada.  
- **Sin vídeo** tras actualizar → **Flashback** o **Dual BIOS**; revisar CSM/UEFI y orden de arranque.  
- **USB/SATA intermitentes** → Defaults y BIOS estable; revisar qué M.2 anula qué SATA. :contentReference[oaicite:30]{index=30}

---

## 2.8 Procedimientos recomendados (paso a paso)

**A) Restablecer rápido:**  
1) PSU en “O”, 2) **Clear CMOS** 5–10 s o **jumper**, 3) Defaults, hora/fecha, **XMP/EXPO**, orden de arranque.

**B) Recuperar BIOS corrupta (Flashback):**  
1) Descargar correcta, 2) USB **FAT32** y renombrado, 3) Puerto dedicado + botón, 4) Esperar fin, 5) Defaults y reconfigurar.

**C) Usar Dual BIOS tras fallo:**  
1) Selector → **BIOS_B** o esperar failover, 2) Reflashear **BIOS_A**, 3) Sincronizar respaldo si es posible. :contentReference[oaicite:31]{index=31}

---

## 2.9 Buenas prácticas en aula/taller
Manual a mano, USB **FAT32** preparado, versión probada, localizar **Clear CMOS**, documentar cambios, cambiar **CR2032** con síntomas, no confundir cables **EPS** (CPU) con **PCIe** (GPU), probar con **Defaults** y añadir ajustes paso a paso. :contentReference[oaicite:32]{index=32}
