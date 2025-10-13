# Activar Just the Docs desde cero

## 0) Si el repo ya existe en GitHub
Clónalo:
```
git clone git@github.com:USUARIO/REPO_NAME.git
# o: git clone https://github.com/USUARIO/REPO_NAME.git
cd REPO_NAME
```

## 1) Copia estos archivos a la raíz del repositorio
- `_config.yml`
- `index.md`
- `temario/index.md`
- `temario/00_demo.md`
- `jtd-diagnostico.md`

## 2) Edita `_config.yml`
Si es un **Project site** (URL tipo `https://USUARIO.github.io/REPO_NAME/`), cambia:
```
baseurl: "/REPO_NAME"
```
por el **nombre EXACTO** del repo.

> Si es un **User/Org site** (`https://USUARIO.github.io`): borra la línea `baseurl:` por completo.

## 3) Habilita GitHub Pages
En GitHub: **Settings → Pages → Build and deployment**
- **Source**: *Deploy from a branch*
- **Branch**: `main` y **/(root)**
- Guardar.

## 4) Sube cambios y fuerza el build
```
git add .
git commit -m "Activa Just the Docs"
git push
# (opcional) commit vacío para forzar rebuild:
git commit --allow-empty -m "rebuild pages" && git push
```

## 5) Verifica
- Portada: `https://USUARIO.github.io/REPO_NAME/`
- Diagnóstico: `https://USUARIO.github.io/REPO_NAME/jtd-diagnostico/`
- Debes ver la barra lateral con **Temario** y **00 · Demo de tema**.

## 6) Añade tus temas reales
En cada archivo de `/temario` pon al principio:
```
---
layout: default
title: "Título del tema"
parent: Temario
nav_order: 10
permalink: /temario/mi-tema/
---
```
Y usa rutas de imagen seguras:
```
![Figura]({{ '/assets/figura.png' | relative_url }})
```

## Problemas frecuentes
- `.nojekyll` en la raíz → bórralo.
- `_config.yml` con **ambos** `theme:` y `remote_theme:` → deja **solo** `remote_theme:`.
- Sin `index.md` → crea el de este pack.
- Plugins no permitidos → usa solo `jekyll-remote-theme` si compilas con Pages (rama).
- Branch/carpeta sin contenido → asegúrate de publicar `main` y **/(root)** o `/docs`.
