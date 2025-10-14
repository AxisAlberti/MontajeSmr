#!/usr/bin/env python3
"""
Añade front matter mínimo a todos los .md en temario/ que no lo tengan.
Uso:
  python tools/add_front_matter.py
"""
import os, re, io

ROOT = os.path.dirname(os.path.dirname(__file__))
TEMARIO = os.path.join(ROOT, "temario")

FM_TMPL = """---
layout: default
title: "{title}"
parent: Temario
nav_order: {order}
permalink: /temario/{slug}/
---

"""

def slugify(name):
    s = name.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s or "tema"

def has_front_matter(text):
    return text.lstrip().startswith("---")

def main():
    order = 1
    for root, _, files in os.walk(TEMARIO):
        for fn in sorted([f for f in files if f.endswith(".md")]):
            path = os.path.join(root, fn)
            with io.open(path, "r", encoding="utf-8") as f:
                txt = f.read()
            if has_front_matter(txt):
                continue
            base = os.path.splitext(fn)[0]
            title = base.replace("_", " ").replace("-", " ").strip().title()
            slug = slugify(base)
            fm = FM_TMPL.format(title=title, order=order, slug=slug)
            with io.open(path, "w", encoding="utf-8") as f:
                f.write(fm + txt)
            print("Front matter añadido a:", path)
            order += 1

if __name__ == "__main__":
    main()
