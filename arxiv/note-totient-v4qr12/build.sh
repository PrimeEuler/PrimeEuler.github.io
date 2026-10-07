#!/bin/bash
# Build script for note-totient-v4qr12 - per repo convention
# Rebuilds the PDF from .tex source (figures are pre-built PDFs in this dir)
set -e
cd "$(dirname "$0")"
pdflatex -interaction=nonstopmode "Note_TotientHyperbolas_V4QR12_v1.0.tex" > /dev/null
pdflatex -interaction=nonstopmode "Note_TotientHyperbolas_V4QR12_v1.0.tex" 2>&1 | grep "Output written"
