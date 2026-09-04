#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

SRC="PaperC_QuantumRealizations_v1.1.tex"
OUT="PaperC_QuantumRealizations_v1.1.pdf"

pdflatex -interaction=nonstopmode -halt-on-error "$SRC"
pdflatex -interaction=nonstopmode -halt-on-error "$SRC"

test -f "$OUT"
echo "Built $ROOT/$OUT"
