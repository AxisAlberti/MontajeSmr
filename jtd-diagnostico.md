---
layout: default
title: JTD — Diagnóstico
nav_exclude: true
permalink: /jtd-diagnostico/
---

# Diagnóstico rápido

**Variables del sitio**
- `site.url` = `{{ site.url }}`
- `site.baseurl` = `{{ site.baseurl }}`
- `site.remote_theme` = `{{ site.remote_theme }}`

**Comprobaciones**
1) Esta página usa `layout: default`. Si ves cabecera de Just the Docs, el tema está **activo**.
2) Sidebar: debería mostrarse *Temario* y debajo **00 · Demo de tema**.

**Pruebas de imagen** (funciona aunque no subas ninguna):
```
![]({{ "'/assets/ejemplo.png' | relative_url" }})
![](/REPO_NAME/assets/ejemplo.png)
```
Sustituye `REPO_NAME` por tu repo si quieres probar una imagen real.
