#!/bin/bash
# Build script for note-bicone-dipole-alpha - per repo convention
# Rebuilds the PDF from .tex source (figures are pre-built PDFs in this dir)
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "Note_BiconeDipole_FineStructure_v1.0.tex" > /dev/null
pdflatex -interaction=nonstopmode "Note_BiconeDipole_FineStructure_v1.0.tex" 2>&1 | grep "Output written"
