#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
FIG="$ROOT/figures"
PAPER="Discriminant_12_Return_v0.3.3.tex"

printf '==> generating publication figures\n'
python3 "$FIG/make_mod12_v4_cone_triple.py"
python3 "$FIG/fig_cutting_plane_tangent_circle_publication.py"
python3 "$FIG/fig_divisor_summatory_11_3panel.py"

printf '==> compiling %s\n' "$PAPER"
cd "$HERE"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"

printf '==> build complete: %s\n' "${PAPER%.tex}.pdf"
