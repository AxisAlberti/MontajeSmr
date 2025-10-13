---
layout: default
title: Temario
nav_order: 2
has_children: true
permalink: /temario/
---

# Temario
Selecciona un tema del índice lateral. Si ya tienes archivos en `/temario`, añade al comienzo de cada uno un **front matter** como este:

```md
---
layout: default
title: "Título del tema"
parent: Temario
nav_order: 10         # cambia el orden (1,2,3, ...)
permalink: /temario/mi-tema/   # URL limpia opcional
---
```

Recuerda usar rutas de imagen así: `![img]({{ '/assets/mi-imagen.png' | relative_url }})`.
