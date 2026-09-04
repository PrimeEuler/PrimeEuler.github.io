#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIG="$HERE/../figures"
PAPER="PaperA_ConicTheorem_v2.4.tex"

printf '==> generating Paper A figures from figures/\n'
python3 "$FIG/fig_cutting_plane_3panel.py"
python3 "$FIG/fig_divisor_summatory_11_3panel.py"

printf '==> compiling %s in foundations/\n' "$PAPER"
cd "$HERE"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"

printf '==> build complete: %s\n' "$HERE/${PAPER%.tex}.pdf"
