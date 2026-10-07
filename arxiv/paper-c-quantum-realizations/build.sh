#!/bin/bash
# Build script for paper-c-quantum-realizations - per repo convention
# Rebuilds the PDF from .tex source (figures are pre-built PDFs in this dir)
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "PaperC_QuantumRealizations_v1.1.tex" > /dev/null
pdflatex -interaction=nonstopmode "PaperC_QuantumRealizations_v1.1.tex" 2>&1 | grep "Output written"
