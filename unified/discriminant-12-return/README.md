# The Discriminant-12 Return

This folder collects the algebraic discriminant-12 branch of the Cone project
and the audited derivation trail used to build it.

## Project working root — authoritative scope

For this project, **all active research, edits, generated figures, paper revisions,
and ledger updates must remain inside**:

`unified/discriminant-12-return/`

The parent `unified/` directory is **not** an active working location for this
project. Files with similar names outside `unified/discriminant-12-return/` are
legacy/original sources only and must not receive project updates.

Use these project-local locations:

- `foundations/` — Foundation papers A, B, C and companion foundation notes.
- `papers/` — Principal discriminant-12 paper and companion publication drafts.
- `research-notes/` — Exploratory findings and source research notes.
- `figures/` — Canonical project figure generators and generated figure assets.
- `ledger/` — Derivation, audit, publication, and checkpoint ledger entries.

Before any GitHub write, verify that the target path begins with
`unified/discriminant-12-return/`. Foundation-paper edits in particular must
begin with `unified/discriminant-12-return/foundations/`.

## Foundation papers

The `foundations/` directory contains the authoritative project-local working
versions of the foundation material. Its file-by-file role and status are
recorded in `foundations/FOUNDATIONS_INVENTORY.md`; consult that manifest before
renaming, moving, archiving, or treating a foundation source as authoritative.

The current Paper A source is `PaperA_ConicTheorem_v2.4.tex`. Paper B's current
build target is `PaperB_EigenCoordinates_v2.tex`, which remains under audit.
`PaperC_QuantumRealizations.tex` is downstream foundation material that must be
reconciled after Paper B because its present formulation still inherits parts
of the older power-map framework.

`Casimir_Null_Diamond_Standalone_v2.1.tex` is now an active audited foundation.
It is the sole live authoritative null-diamond source. The former
`papers/Casimir_Null_Diamond_Standalone_v2_Audited.tex/.pdf` artifacts were
removed after v2.1 was established; Git history preserves that historical
version. v2.1 incorporates the audit guardrails on Farey representative
orientation, Paper-C source status, the two-mode positive-discrete-series
convention, and the distinction between a state transition vertex and the
four-corner cell center.

Figure generators do **not** belong in `foundations/`. Foundation TeX files read
publication figures from `../figures/`, and build scripts invoke the paper-owned
generators from there when figures are required.

## Papers

The principal paper publication baseline is
`papers/Discriminant_12_Return_v0.3.3.tex` / `.pdf`. Earlier v0.1 and v0.2
sources are retained as historical drafts. Companion publication material is
kept in the same `papers/` directory.

## Figure ownership and naming

Every publication-facing Python figure generator in `figures/` must identify
its owning paper or note in its filename. Generic Python builder names are not
used for active generators. Related papers may use related geometry, but they
must not silently share a generator when their publication purpose differs.

### Paper A and its area companion

Canonical implementations:

- `paperA_cutting_plane_3panel.py`
- `paperA_divisor_summatory_11_3panel.py`
- `paperA_area_measure_11_2panel.py`

`foundations/build_paper_a.sh` calls the first two before compiling
`PaperA_ConicTheorem_v2.4.tex`. `foundations/build_area_paper.sh` calls the area
companion generator before compiling `Note_AreaDistortion_AMGM_Cone_v1.1.tex`.

The area companion now writes paper-specific outputs
`paperA_area_measure_11_2panel.pdf/png`; its build script stages the historical
v1.1 TeX with that filename so the source snapshot can remain unchanged. Paper
A's cutting-plane and divisor output names are still the names referenced by
its current TeX source and can be normalized separately if desired.

### The Discriminant-12 Return

Canonical implementations:

- `discriminant12_tangent_null_rays_3panel.py`
- `discriminant12_divisor_summatory_11_3panel.py`
- `discriminant12_mod12_v4_cone_triple.py`

The tangent/null-ray generator preserves the complete `K=1,...,12` fixed-`T`
family and the emphasized `u=5,6,7` parabola tangencies. The divisor generator
is independent of Paper A's divisor generator. The mod-12 generator realizes
`U(12)={1,5,7,11}` geometrically.

`papers/build_discriminant12_v0.3.3.sh` calls all three Discriminant-12-owned
generators. Because v0.3.3 is retained as a historical publication source, the
build stages a temporary copy whose historical tangent/divisor figure names are
remapped to the paper-specific outputs. Paper A assets are not overwritten.

The mod-12 geometry carries the four modular labels; the `V_4` operation remains
multiplication modulo 12, not adjacency in the drawing.

### Other foundation papers

`foundations/build_paper_b.sh` contains no figure-generation step; it only
compiles `PaperB_EigenCoordinates_v2.tex`. Paper C likewise has no active
publication figure generator in `figures/` at this checkpoint.

`foundations/build_casimir_null_diamond.sh` compiles
`Casimir_Null_Diamond_Standalone_v2.1.tex`; the null-diamond paper currently has
no publication figure generator.

## CI / publication workflow invariant

The GitHub Actions workflows in `.github/workflows/` are part of the publication
pipeline and must be kept synchronized with the project-local build scripts.
Whenever an authoritative TeX version changes, a figure generator is renamed,
a build script changes target, or a generated publication output is renamed,
the corresponding workflow must be updated in the same change set.

Current active mappings are:

- `build-paper-a.yml` -> `foundations/build_paper_a.sh` -> `PaperA_ConicTheorem_v2.4.tex`
- `build-area-paper.yml` -> `foundations/build_area_paper.sh` -> `Note_AreaDistortion_AMGM_Cone_v1.1.tex`
- `build-paper-b.yml` -> `foundations/build_paper_b.sh` -> `PaperB_EigenCoordinates_v2.tex`
- `build-casimir-null-diamond.yml` -> `foundations/build_casimir_null_diamond.sh` -> `Casimir_Null_Diamond_Standalone_v2.1.tex`
- `build-discriminant12-paper.yml` -> `papers/build_discriminant12_v0.3.3.sh` -> `Discriminant_12_Return_v0.3.3.tex`

Publication workflows that invoke Matplotlib with LaTeX rendering install the
same TeX support used by the local generators, including `cm-super`. Generated
PDF/PNG binaries are produced and committed by GitHub Actions; connector-side
binary-write limitations are not part of the CI build path.

## Research notes

- `Divisor_Summatory_V4_Mod12_Findings.md`
- `Jx_Jy_V4_Quarter_Shift_Findings.md`
- `STATUS_2026-09-03_Operator_Cone_Unification.md`
- `Note_SemiclassicalArea.tex` — exploratory LQG branch retained for possible future work; its geometry-only content was superseded for foundation purposes by `foundations/Note_AreaDistortion_AMGM_Cone_v1.1.tex`.

These are retained as source research notes rather than cited as completed
theorems unless a later audit explicitly promotes a result.

## Ledger

The `ledger/` directory preserves the audited derivation trail and publication
checkpoints for this project. The highest valid checkpoint should be treated as
the current baseline; earlier files are retained so development can be
reconstructed.

The expected startup chain for a future working session is:

**README -> current structure/rules -> `foundations/FOUNDATIONS_INVENTORY.md` -> highest ledger checkpoint -> actual source/build/workflow files.**

## Scope

The principal algebraic chain is

\[
K=H^{-1}
\Longleftrightarrow \sigma=2
\Longrightarrow \Delta_g=12
\Longrightarrow \mathbb Q(\sqrt3)
\Longrightarrow \mathbb Q(\zeta_{12})
\Longrightarrow \text{ramified Boolean factor exchange}.
\]

The algebraic theorem does not depend on zeta zeros, numerical certification,
or the Riemann hypothesis. The certified Suzuki crossing and the larger
Clark/Cauchy/Fisher/Berry development remain separate analytic work.
