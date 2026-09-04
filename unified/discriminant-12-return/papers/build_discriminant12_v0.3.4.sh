#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIG="$HERE/../figures"
SRC="Discriminant_12_Return_v0.3.4.tex"
BUILD="$HERE/.build_discriminant12_v0.3.4"
STAGED="$BUILD/Discriminant_12_Return_v0.3.4.tex"

printf '==> generating Discriminant-12 publication figures\n'
python3 "$FIG/discriminant12_tangent_null_rays_3panel.py"
python3 "$FIG/discriminant12_divisor_summatory_11_3panel.py"
python3 "$FIG/discriminant12_mod12_v4_cone_triple.py"

printf '==> staging %s with paper-specific figure names\n' "$SRC"
rm -rf "$BUILD"
mkdir -p "$BUILD"

sed \
  -e 's/{fig_cutting_plane_tangent_circle_audit\.pdf}/{discriminant12_tangent_null_rays_3panel.pdf}/g' \
  -e 's/{fig_divisor_summatory_11_3panel\.png}/{discriminant12_divisor_summatory_11_3panel.png}/g' \
  "$HERE/$SRC" > "$STAGED"

printf '==> compiling isolated Discriminant-12 v0.3.4 build\n'
cd "$BUILD"
TEXINPUTS="$HERE:$FIG:" pdflatex -interaction=nonstopmode -halt-on-error "$(basename "$STAGED")"
TEXINPUTS="$HERE:$FIG:" pdflatex -interaction=nonstopmode -halt-on-error "$(basename "$STAGED")"

cp "$BUILD/Discriminant_12_Return_v0.3.4.pdf" "$HERE/Discriminant_12_Return_v0.3.4.local-build.pdf"

printf '==> build complete: %s\n' "$HERE/Discriminant_12_Return_v0.3.4.local-build.pdf"
printf '    Paper A figure outputs were not overwritten.\n'
