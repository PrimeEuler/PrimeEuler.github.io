#!/bin/bash
# Build script for paper-d-cusp-cubic - per repo convention
# Rebuilds the PDF from .tex source (figures are pre-built PDFs in this dir)
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "PaperD_CuspCubic.tex" > /dev/null
pdflatex -interaction=nonstopmode "PaperD_CuspCubic.tex" 2>&1 | grep "Output written"
