#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIG="$HERE/../figures"
PAPER="Note_AreaDistortion_AMGM_Cone_v1.1.tex"

printf '==> generating area-paper figure\n'
python3 "$FIG/fig_area_measure_11_2panel.py"

printf '==> compiling %s in foundations/\n' "$PAPER"
cd "$HERE"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"

printf '==> build complete: %s\n' "$HERE/${PAPER%.tex}.pdf"
