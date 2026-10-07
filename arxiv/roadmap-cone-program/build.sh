#!/bin/bash
# Build script for roadmap-cone-program - per repo convention
# Rebuilds the PDF from .tex source (figures are pre-built PDFs in this dir)
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "Roadmap_ConeProgram_v1.0.tex" > /dev/null
pdflatex -interaction=nonstopmode "Roadmap_ConeProgram_v1.0.tex" 2>&1 | grep "Output written"
