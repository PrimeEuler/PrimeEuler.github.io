#!/bin/bash
# Build script for paper-a-cutting-plane - per repo convention
# Rebuilds the PDF from .tex source (figures are pre-built PDFs in this dir)
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "PaperA_ConicTheorem_v2.4.tex" > /dev/null
pdflatex -interaction=nonstopmode "PaperA_ConicTheorem_v2.4.tex" 2>&1 | grep "Output written"
