# Activación limpia — Just the Docs para AxisAlberti/MontajeSmr

## 1) Copia estos archivos a la **raíz** del repo
- `_config.yml`
- `_sass/custom/custom.scss`
- `index.md`
- `temario/index.md`
- `temario/00_demo.md` (luego puedes borrarlo)
- `jtd-diagnostico.md`
- `assets/logo.png` (placeholder)

## 2) Habilita GitHub Pages
Settings → Pages → *Deploy from a branch* → Branch `main` y **/(root)** → Guardar.

URL: https://AxisAlberti.github.io/MontajeSmr/

## 3) Forzar compilación (si no ves cambios)
Edita un archivo en la web y guarda, o:
```
git commit --allow-empty -m "rebuild pages"
git push
```

## 4) Añade front matter a tus temas reales
En **cada** archivo dentro de `temario/` añade al principio:
```
---
layout: default
title: "Título del tema"
parent: Temario
nav_order: 10
permalink: /temario/mi-tema/
---
```
Esto hace que aparezcan en la barra lateral.

## 5) Problemas típicos
- `.nojekyll` en raíz → bórralo.
- No mezcles `theme:` con `remote_theme:` (deja solo `remote_theme:`).
- Asegúrate de tener `index.md` en la raíz.
