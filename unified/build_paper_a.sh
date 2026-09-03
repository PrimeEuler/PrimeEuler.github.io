#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIG="$HERE/discriminant-12-return/figures"
PAPER="PaperA_ConicTheorem_v2.2.tex"

printf '==> generating Paper A figures\n'
python3 "$HERE/fig_cutting_plane_3panel.py"
python3 "$FIG/fig_divisor_summatory_11_3panel.py"

printf '==> compiling %s\n' "$PAPER"
cd "$HERE"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"

printf '==> build complete: %s\n' "${PAPER%.tex}.pdf"
