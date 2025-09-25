# Índice

1. Placa base (motherboard)
   1.1. Introducción
   1.2. Factor de forma (form factor)
   1.3. Socket (zócalo de CPU)
        1.3.1. Intel (sobremesa y workstation recientes)
        1.3.2. AMD (sobremesa y HEDT recientes)
   1.4. Chipset (PCH)
        1.4.1. Intel (consumo)
        1.4.2. AMD (AM5)
   1.5. VRM y alimentación
   1.6. Bancos de memoria (DIMM)
   1.7. Ranuras PCI Express
   1.8. Almacenamiento: M.2 y SATA
        1.8.1. Zócalos M.2
        1.8.2. Puertos SATA
   1.9. Puertos traseros e internos (headers)
   1.10. Firmware UEFI (BIOS moderna)
   1.11. Sensores y diagnóstico
   1.12. Diseño del PCB y calidad
   1.13. Selección rápida según uso
   1.14. Listados de referencia (2024–2025)
        1.14.1. Chipsets destacados
        1.14.2. Sockets más relevantes
   1.15. Checklist de montaje y verificación

2. BIOS, memoria CMOS, Dual BIOS y sistemas de reseteo — guía exhaustiva (España)
   2.1. Introducción
   2.2. BIOS vs UEFI
   2.3. Memoria CMOS, RTC y NVRAM
   2.4. Dual BIOS (BIOS principal + respaldo)
   2.5. Sistemas de reseteo (restablecer ajustes)
        2.5.1. Desde la UEFI
        2.5.2. Botón Clear CMOS (CLR_CMOS)
        2.5.3. Jumper CLR_CMOS (2/3 pines)
        2.5.4. Retirar la pila CR2032
        2.5.5. BIOS Flashback / Q-Flash Plus / Flash BIOS Button
        2.5.6. Arranque de rescate en Dual BIOS
        2.5.7. Borrar contraseñas de BIOS
   2.6. Actualización del firmware (flasheo) con seguridad
   2.7. Diagnóstico y síntomas típicos

# 1. Placa base (motherboard): guía exhaustiva 2025 (España)

> Objetivo: explicar **para qué sirve** cada elemento de una placa base y cómo elegir con criterio técnico (Intel y AMD, 2024–2025). Redacción en español de España.

---

## 1.1. Introducción

La **placa base** es el circuito impreso principal del PC. Sirve para:

- **Interconectar** CPU, memoria, almacenamiento y periféricos mediante buses de alta y baja velocidad (PCIe, USB, SATA, audio, red).
- **Distribuir y regular** la energía (VRM) para que llegue con la tensión y estabilidad correctas.
- **Aportar servicios de plataforma** (chipset/PCH): puertos USB, SATA, líneas PCIe adicionales, RAID, etc.
- **Inicializar y configurar** el hardware (firmware UEFI) y aplicar políticas de seguridad (Secure Boot, TPM/fTPM).
- **Anclar físicamente** los componentes y encajar en el chasis según un **factor de forma**.
