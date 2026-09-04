# Cone Derivation Ledger v13.207 — Canonical Figure Generator Naming

## Scope

This checkpoint completes the publication-figure naming cleanup inside
`unified/discriminant-12-return/figures/`.

## Rule

Every active publication-facing Python figure generator must identify its
owning paper or note in the filename. Generic Python generator names are not
active canonical sources.

## Paper A

Canonical generator implementations are now:

- `paperA_cutting_plane_3panel.py`
- `paperA_divisor_summatory_11_3panel.py`
- `paperA_area_measure_11_2panel.py`

The former generic Python sources
`fig_cutting_plane_3panel.py`, `fig_divisor_summatory_11_3panel.py`, and
`fig_area_measure_11_2panel.py` were removed after their implementations were
moved into the Paper-A-named files.

`foundations/build_paper_a.sh` calls the two Paper A generators directly.
`foundations/build_area_paper.sh` calls the Paper A area-companion generator
directly.

Output asset names remain stable for the existing Paper A / area-note TeX
sources at this checkpoint; this cleanup changes generator ownership, not
publication content.

## The Discriminant-12 Return

Canonical generator implementations are:

- `discriminant12_tangent_null_rays_3panel.py`
- `discriminant12_divisor_summatory_11_3panel.py`
- `discriminant12_mod12_v4_cone_triple.py`

The former generic `make_mod12_v4_cone_triple.py` was removed after its full
implementation was moved into `discriminant12_mod12_v4_cone_triple.py`.

`papers/build_discriminant12_v0.3.3.sh` calls all three paper-owned generators.
The tangent/null-ray generator retains the emphasized `u=5,6,7` parabola
family required by the v0.3.3 publication baseline.

## Other papers

`foundations/build_paper_b.sh` has no figure-generation stage and therefore had
no generator rename to perform. Paper C has no active publication generator in
`figures/` at this checkpoint.

## Result

There is now one unambiguous active Python source name per publication figure
family. Running or editing a Paper A generator no longer requires tracing
through a generic wrapper, and the principal Discriminant-12 generator names
are likewise paper-specific.
