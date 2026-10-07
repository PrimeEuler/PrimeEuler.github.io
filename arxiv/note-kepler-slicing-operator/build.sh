#!/bin/bash
# Build script for note-kepler-slicing-operator - per repo convention
# Rebuilds the PDF from .tex source (figures are pre-built PDFs in this dir)
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "DynamicSlicingOperator_AMGM_Cone.tex" > /dev/null
pdflatex -interaction=nonstopmode "DynamicSlicingOperator_AMGM_Cone.tex" 2>&1 | grep "Output written"
