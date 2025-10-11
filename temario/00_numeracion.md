---
layout: Default
title: 📚 Mantenimiento y Montaje de Equipos Informáticos
---


## TEMA 0. SISTEMAS DE NUMERACIÓN

1. [Introducción](#1-introducción)  
2. [Teorema Fundamental de la Numeración (TFN)](#2-teorema-fundamental-de-la-numeración-tfn)  
   - 2.1 [Enunciado](#21-enunciado)  
   - 2.2 [Idea de la demostración (existencia y unicidad)](#22-idea-de-la-demostración-existencia-y-unicidad)  
   - 2.3 [Corolarios algorítmicos](#23-corolarios-algorítmicos)  
3. [Sistemas de numeración](#3-sistemas-de-numeración)  
   - 3.1 [Posicionales vs. no posicionales](#31-posicionales-vs-no-posicionales)  
   - 3.2 [Representación en base b](#32-representación-en-base-b)  
   - 3.3 [Partes enteras y fraccionarias](#33-partes-enteras-y-fraccionarias)  
4. [Conversiones de bases — enteros](#4-conversiones-de-bases--enteros)  
   - 4.1 [Decimal → base b (divisiones sucesivas)](#41-decimal--base-b-divisiones-sucesivas)  
   - 4.2 [Base b → decimal (Horner)](#42-base-b--decimal-horner)  
   - 4.3 [Pseudocódigo de conversiones (enteros)](#43-pseudocódigo-de-conversiones-enteros)  
5. [Conversiones con parte fraccionaria](#5-conversiones-con-parte-fraccionaria)  
   - 5.1 [Decimal → base b (multiplicación por b)](#51-decimal--base-b-multiplicación-por-b)  
   - 5.2 [Base b → decimal (potencias negativas)](#52-base-b--decimal-potencias-negativas)  
   - 5.3 [Finita o periódica: criterio](#53-finita-o-periódica-criterio)  
6. [Conversiones entre bases potencia (2, 8, 16)](#6-conversiones-entre-bases-potencia-2-8-16)  
7. [Números con signo y complementos](#7-números-con-signo-y-complementos)  
   - 7.1 [Signo y magnitud](#71-signo-y-magnitud)  
   - 7.2 [Complemento a 1](#72-complemento-a-1)  
   - 7.3 [Complemento a 2](#73-complemento-a-2)  
   - 7.4 [Overflow y extensión de signo](#74-overflow-y-extensión-de-signo)  
8. [Coma fija y coma flotante](#8-coma-fija-y-coma-flotante)  
   - 8.1 [Coma fija (Qm.n)](#81-coma-fija-qmn)  
   - 8.2 [IEEE 754 (32 bits, simple precisión)](#82-ieee-754-32-bits-simple-precisión)  
   - 8.3 [Ejemplos de conversión IEEE-754](#83-ejemplos-de-conversión-ieee-754)  
   - 8.4 [Redondeo y errores comunes](#84-redondeo-y-errores-comunes)  
9. [Aritmética en base b](#9-aritmética-en-base-b)  
10. [Aplicaciones](#10-aplicaciones)  
11. [Tablas rápidas](#11-tablas-rápidas)   
12. [Bibliografía y recursos](#14-bibliografía-y-recursos)  

---

## 1. Introducción
Los **sistemas de numeración** son fundamentales para representar y manipular datos en matemáticas, ingeniería e informática. Comprenderlos permite:  
- Convertir entre diferentes bases numéricas.  
- Representar números de forma **única** (TFN) y **eficiente**.  
- Conectar teoría con aplicaciones (direcciones IP, colores web, memoria, etc.).

---

## 2. Teorema Fundamental de la Numeración (TFN)

### 2.1 Enunciado
Para cualquier entero N ≥ 0 y base entera b > 1, existen dígitos aₖ, …, a₀ con 0 ≤ aᵢ < b y aₖ ≠ 0 tales que:  

N = aₖ bᵏ + aₖ₋₁ bᵏ⁻¹ + … + a₁ b + a₀.
  
La representación es **única**.

### 2.2 Idea de la demostración (existencia y unicidad)
- **Existencia:** aplicar **división euclídea** repetida de N por b. Los restos son los dígitos desde el menos significativo (LSB) al más significativo (MSB).  
- **Unicidad:** si hubiese dos expansiones distintas, su diferencia sería una combinación no trivial de potencias de b igual a 0 con coeficientes acotados ⇒ contradicción.

### 2.3 Corolarios algorítmicos
- **Divisiones sucesivas**: decimal → base b (enteros).  
- **Evaluación/Horner**: base b → decimal (enteros).  

---

## 3. Sistemas de numeración

### 3.1 Posicionales vs. no posicionales
- **Posicionales:** el valor depende de la posición y la base (decimal, binario, octal, hex).  
- **No posicionales:** reglas aditivas/substractivas (romanos, etc.).

### 3.2 Representación en base b
Ejemplos:  
- 234₁₀ = 2·10² + 3·10¹ + 4·10⁰  
- 1101₂ = 1·2³ + 1·2² + 0·2¹ + 1·2⁰ = 13₁₀  
- 3A₁₆ = 3·16 + 10 = 58₁₀

### 3.3 Partes enteras y fraccionarias
La parte fraccionaria en base b: 0.a₁ a₂ a₃\b = a₁ b⁻¹ + a₂ b⁻² + ·s.  
No toda fracción decimal es finita en otra base y viceversa (§5.3).

---

## 4. Conversiones de bases — enteros

### 4.1 Decimal → base b (divisiones sucesivas)
**Ejemplo:** 45₁₀ a binario  
```
45 ÷ 2 = 22 resto 1
22 ÷ 2 = 11 resto 0
11 ÷ 2 = 5  resto 1
5  ÷ 2 = 2  resto 1
2  ÷ 2 = 1  resto 0
1  ÷ 2 = 0  resto 1
```
Lectura de restos de abajo a arriba → **101101₂**.

**Ejemplo:** 255₁₀ a hex  
```
255 ÷ 16 = 15 (F), resto 15 (F)
15 ÷ 16  = 0,  resto 15 (F)
```
Resultado: **FF₁₆**.

### 4.2 Base b → decimal (Horner)
**Esquema:** recorrer dígitos de izquierda a derecha:  
```
valor = 0
para cada dígito d:
    valor = valor * b + d
```
**Ejemplo:** 101101₂ \to 45₁₀.

### 4.3 Pseudocódigo de conversiones (enteros)
**Decimal → base b**
```text
function to_base_b(n, b):
  if n == 0: return "0"
  digits = []
  while n > 0:
    r = n mod b
    digits.append(symbol(r))   # 10→'A', 11→'B', ...
    n = n div b
  return reverse(join(digits))
```
**Base b → decimal**
```text
function from_base_b(s, b):
  val = 0
  for ch in s:                 # izquierda a derecha
    d = value(ch)              # 'A'→10, ...
    val = val * b + d
  return val
```

---

## 5. Conversiones con parte fraccionaria

### 5.1 Decimal → base b (multiplicación por b)
Para fracción f \in [0,1): multiplicar por b, tomar parte entera como dígito y repetir con la fracción.  
**Ejemplo:** 0.625₁₀ a binario  
```
0.625×2 = 1.25  → 1
0.25 ×2 = 0.5   → 0
0.5  ×2 = 1.0   → 1
```
Resultado: **0.101₂**.

**Ejemplo periódico:** 0.1₁₀ a binario ⇒ **0.0001100110011…₂**.

### 5.2 Base b → decimal (potencias negativas)
**Ejemplo:** 0.101₂ = 1·2⁻¹ + 0·2⁻² + 1·2⁻³ = 0.625.

### 5.3 Finita o periódica: criterio
La fracción  \frac{p}{q}  (reducida) es **finita** en base b **ssi** los factores primos de q están contenidos en los de b.  
- En decimal (b=10=2·5): 1/8 finita, 1/3 periódica.  
- En binario (b=2): 1/8 finita, 1/5 periódica.

---

## 6. Conversiones entre bases potencia (2, 8, 16)
- **Binario ↔ Hex (×4 bits):** agrupar desde la derecha (entera) y desde la izquierda de la coma (fracción).  
  Ej.: 1101\,0110\,1111\,1001₂ = D6F9₁₆.  
- **Binario ↔ Octal (×3 bits):** p.ej. 111\,010\,101₂ = 725₈.

---

## 7. Números con signo y complementos

### 7.1 Signo y magnitud
Bit de signo (0/1). Dos ceros (+0 y −0). Aritmética compleja.

### 7.2 Complemento a 1
Negar bits. Persiste ±0. Manejo de acarreo final.

### 7.3 Complemento a 2 (estándar)
Para negar: **invertir** bits y **sumar 1**.  
Rango con n bits: [-2ⁿ⁻¹,\ 2ⁿ⁻¹-1].

**Ejemplo (8 bits):**  
- +13 = 0000\,1101  
- -13: invertir → 1111\,0010, +1 → **1111\,0011**

**Suma C2 (8 bits):** +25 (0001 1001) + (-13) (1111 0011)  
```
  0001 1001
+ 1111 0011
-----------
  0000 1100   → 12
```

### 7.4 Overflow y extensión de signo
- **Overflow:** al sumar operandos de **igual signo** y el resultado cambia de signo.  
- **Extensión de signo:** replicar el bit de signo al ampliar anchura (ej. de 8 a 16 bits).

---

## 8. Coma fija y coma flotante

### 8.1 Coma fija (Qm.n)
Se fija cuántos bits corresponden a la fracción. Operaciones requieren reescalado y cuidado con overflow.

### 8.2 IEEE 754 (32 bits, simple precisión)
- **Signo (1 bit)**, **Exponente (8 bits, sesgo 127)**, **Fracción/Mantisa (23 bits)**.  
- Valor normalizado: (-1)ˢ × 1.\text{mantisa} × 2ᵉ⁻¹²⁷.  
- Casos especiales: subnormales (e=0,f≠0), ±∞ (e=255,f=0), NaN (e=255,f≠0).

### 8.3 Ejemplos de conversión IEEE-754
**A) 13.25₁₀ → binario IEEE-754 simple**  
1) 13.25₁₀ = 1101.01₂ = 1.10101₂ × 2³  
2) e = 3 + 127 = 130 \Rightarrow 10000010₂  
3) Mantisa: `10101` + ceros hasta 23 bits  
4) Signo s=0  
**Resultado:** `0 10000010 10101000000000000000000` (hex `0x41540000`).

**B) 0xC2480000 → decimal**  
- s=1 (negativo), e=`10000100`₂=132 ⇒ e-127=5.  
- Mantisa ≈ `1.1001000…` ⇒ valor ≈ -1.5625 × 2⁵ = -50.

### 8.4 Redondeo y errores comunes
- Modo por defecto: **round to nearest, ties to even**.  
- Decimales como 0.1 no son exactos en binario ⇒ acumulación de error.  
- Evitar `==` con floats; usar tolerancia (ε).

---

## 9. Aritmética en base b
- **Suma:** de derecha a izquierda con **acarreo**.  
- **Resta:** con **préstamo**.  
- **Multiplicación:** sumas de productos parciales desplazados.  
- En binario, multiplicar es eficiente (AND + desplazamientos).

**Ejemplo:** 1011₂ (11) × 110₂ (6)  
```
      1011
    ×  110
    ------
      0000
     1011
+   1011
-----------
   1000010   (= 66)
```

---

## 10. Aplicaciones
- **Redes:** máscaras IPv4 (/24, /26), conteo de hosts en binario.  
- **Colores web:** `#RRGGBB` (hex).  
- **Memoria/direcciones:** offsets en hex.  
- **Codificación:** ASCII/Unicode.  
- **Criptografía:** operaciones modulares y grandes enteros binarios.

---

## 11. Tablas rápidas

### 11.1 Potencias de 2
| Potencia | Valor | Comentario |
|---------:|------:|------------|
| 2⁸       | 256   | 8 bits     |
| 2¹⁰      | 1024  | ≈ 1 KiB    |
| 2¹⁶      | 65536 | 16 bits    |
| 2²⁰      | 1,048,576 | ≈ 1 MiB |

### 11.2 Mapa binario ↔ hex (nibbles)
| Bin | Hex | Bin | Hex | Bin | Hex | Bin | Hex |
|----|-----|----|-----|----|-----|----|-----|
|0000|0|0100|4|1000|8|1100|C|
|0001|1|0101|5|1001|9|1101|D|
|0010|2|0110|6|1010|A|1110|E|
|0011|3|0111|7|1011|B|1111|F|

### 11.3 Prefijos
- **Decimal:** k=10³, M=10⁶, G=10⁹…  
- **Binario:** Ki=2¹⁰, Mi=2²⁰, Gi=2³⁰…

---

## 12. Bibliografía y recursos
- Knuth, D. E. *The Art of Computer Programming, Vol. 2*.  
- Tanenbaum, A. S. *Structured Computer Organization*.  
- IEEE 754-2008/2019 (resumenes docentes y notas de referencia).  
- [Markdown Guide](https://www.markdownguide.org/) para sintaxis y buenas prácticas.

---
**Autor:** _(José Manuel González Castillo)_  
**Fecha:** _(13/09/2025)_

