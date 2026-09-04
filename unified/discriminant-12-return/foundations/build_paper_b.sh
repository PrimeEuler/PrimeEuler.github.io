#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PAPER="PaperB_EigenCoordinates_v2.1.tex"

printf '==> compiling %s in foundations/\n' "$PAPER"
cd "$HERE"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"
pdflatex -interaction=nonstopmode -halt-on-error "$PAPER"

printf '==> build complete: %s\n' "$HERE/${PAPER%.tex}.pdf"
