#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode -halt-on-error Casimir_Null_Diamond_Standalone_v2.1.tex
pdflatex -interaction=nonstopmode -halt-on-error Casimir_Null_Diamond_Standalone_v2.1.tex
