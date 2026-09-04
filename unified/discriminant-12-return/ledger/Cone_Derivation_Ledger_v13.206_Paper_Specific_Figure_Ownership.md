# Cone Derivation Ledger v13.206 — Paper-Specific Figure Ownership

Date: 2026-09-04

## Status

Publication-pipeline cleanup. No mathematical theorem is changed by this entry.
The purpose is to prevent one paper's figure generator from overwriting or
silently redefining another paper's publication asset.

## Problem found

Paper A and `Discriminant_12_Return_v0.3.3.tex` both referenced
`fig_divisor_summatory_11_3panel.png`, even though the two papers have distinct
publication purposes and visual baselines. The principal Discriminant-12 paper
also referenced `fig_cutting_plane_tangent_circle_audit.pdf`, whose generator
had been removed during a Paper A cleanup even though the figure remained an
active Discriminant-12 publication asset.

## Resolution

### Paper A ownership

Paper A retains its own canonical generators and outputs:

- `fig_cutting_plane_3panel.py` -> `fig_cutting_plane_3panel.pdf/png`
- `fig_divisor_summatory_11_3panel.py` ->
  `fig_divisor_summatory_11_3panel.pdf/png`
- `fig_area_measure_11_2panel.py` -> `fig_area_measure_11_2panel.pdf/png`

The Paper A divisor display remains the audited `n=11` visualization with
`D(11)=29`, `A_11=37`, `T_11=66` and the corrected positive-factor side mesh.

### Discriminant-12 ownership

The principal paper now has independent generators:

- `discriminant12_tangent_null_rays_3panel.py` ->
  `discriminant12_tangent_null_rays_3panel.pdf/png`
- `discriminant12_divisor_summatory_11_3panel.py` ->
  `discriminant12_divisor_summatory_11_3panel.pdf/png`
- `make_mod12_v4_cone_triple.py` -> `mod12_v4_cone_triple.png`

The tangent/null-ray generator explicitly preserves the v0.3.3 publication
feature

\[
TANGENT\_LEVELS=(5,6,7),
\]

so the highlighted factor parabolas are tangent to the fixed-`T` circles at

\[
T=5/2,\quad 3,\quad 7/2,
\]

with tangent/null-generator points

\[
(X,Y)=(\pm u/2,0),\qquad (X,T)=(\pm u/2,u/2).
\]

## Historical-source guardrail

`Discriminant_12_Return_v0.3.3.tex` is retained as the historical publication
source and still contains its original figure filenames. The isolated build
script

`papers/build_discriminant12_v0.3.3.sh`

regenerates the new paper-specific assets and stages a temporary TeX copy in
which only the two historical figure references are remapped to the unique
Discriminant-12 filenames. The staged build therefore does not overwrite Paper
A outputs.

A future principal-paper version should reference the paper-specific filenames
directly in its TeX source rather than relying on staging substitution.

## Reproducibility rule

Related mathematical geometry does not imply shared publication assets.
Whenever Paper A and the principal Discriminant-12 paper require different
visual emphases, their generators and output filenames must remain distinct.
