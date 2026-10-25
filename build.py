"""Genera el aplicativo final a partir del código fuente.

    python build.py

Produce:
  dist/laboratorio-de-imagenes.html  -> archivo único y autocontenido para entregar o abrir en el navegador
  build/artifact.html                -> variante para publicar como artefacto de Claude (no se versiona)
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
src = (ROOT / "src" / "app.html").read_text(encoding="utf-8")
demo = (ROOT / "src" / "demo-images.js").read_text(encoding="utf-8")

full = src.replace("/*__DEMO__*/", demo)
(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "laboratorio-de-imagenes.html").write_text(full, encoding="utf-8")

# Variante artefacto: sin esqueleto propio (lo agrega el visor) y con la marca para ocultar lo que el visor no permite
a = full
for tag in ['<!doctype html>\n', '<html lang="es">\n', '<head>\n', '</head>\n', '</html>\n', '</body>\n', '<meta charset="utf-8">\n']:
    a = a.replace(tag, "")
a = re.sub(r'<meta name="viewport"[^>]*>\n', "", a)
a = a.replace("<title>Laboratorio de imágenes</title>\n",
              '<title>Laboratorio de imágenes</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n', 1)
a = a.replace("<body>\n", "", 1)
a = a.replace('"use strict";', '"use strict";\ndocument.body.classList.add("in-artifact");', 1)
(ROOT / "build").mkdir(exist_ok=True)
(ROOT / "build" / "artifact.html").write_text(a, encoding="utf-8")
print(f"dist/laboratorio-de-imagenes.html  {len(full) / 1024:.0f} KB")
print(f"build/artifact.html                {len(a) / 1024:.0f} KB")
