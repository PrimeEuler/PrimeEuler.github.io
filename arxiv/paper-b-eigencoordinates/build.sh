#!/bin/bash
# Build script for paper-b-eigencoordinates - per repo convention
# Rebuilds the PDF from .tex source (figures are pre-built PDFs in this dir)
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "PaperB_EigenCoordinates_v2.1.tex" > /dev/null
pdflatex -interaction=nonstopmode "PaperB_EigenCoordinates_v2.1.tex" 2>&1 | grep "Output written"
