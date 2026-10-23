"""Genera magnesio/paciente/index.html (solo modo paciente) a partir de magnesio/index.html.

Uso: python3 tools/build-paciente.py
Ejecutar después de cada cambio en magnesio/index.html.
"""
import re
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
s = (raiz / "magnesio/index.html").read_text(encoding="utf-8")

s, n1 = re.subn(r'  <div class="modebar">.*?\n  </div>\n</div></header>', '</div></header>', s, count=1, flags=re.S)
s, n2 = re.subn(r'<section class="wrap pro-only" style="padding-bottom:30px">.*?</section>\n', '', s, count=1, flags=re.S)
viejo = "<title>Ingesta de magnesio — Dra. Omidres Pérez de Carvelli</title>"
assert n1 == 1 and n2 == 1 and viejo in s, "La estructura de magnesio/index.html cambió: revisar este script"
s = s.replace(viejo, "<title>Calculadora de magnesio — Dra. Omidres Pérez de Carvelli</title>")

destino = raiz / "magnesio/paciente/index.html"
destino.write_text(s, encoding="utf-8")
print("Generado", destino.relative_to(raiz))
