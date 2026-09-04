#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIG="$HERE/../figures"
SRC="Note_AreaDistortion_AMGM_Cone_v1.1.tex"
BUILD="$HERE/.build_area_paper_v1.1"
STAGED="$BUILD/$SRC"

printf '==> generating Paper A area-companion figure\n'
python3 "$FIG/paperA_area_measure_11_2panel.py"

printf '==> staging %s with paper-specific figure name\n' "$SRC"
rm -rf "$BUILD"
mkdir -p "$BUILD"
sed \
  -e 's/{fig_area_measure_11_2panel\.pdf}/{paperA_area_measure_11_2panel.pdf}/g' \
  "$HERE/$SRC" > "$STAGED"

printf '==> compiling isolated area-paper build\n'
cd "$BUILD"
TEXINPUTS="$HERE:$FIG:" pdflatex -interaction=nonstopmode -halt-on-error "$SRC"
TEXINPUTS="$HERE:$FIG:" pdflatex -interaction=nonstopmode -halt-on-error "$SRC"

cp "$BUILD/${SRC%.tex}.pdf" "$HERE/${SRC%.tex}.pdf"

printf '==> build complete: %s\n' "$HERE/${SRC%.tex}.pdf"
printf '    figure outputs: %s\n' "$FIG/paperA_area_measure_11_2panel.pdf"
printf '                    %s\n' "$FIG/paperA_area_measure_11_2panel.png"
