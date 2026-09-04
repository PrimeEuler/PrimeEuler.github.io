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

The current audited Paper A source is `PaperA_ConicTheorem_v2.4.tex`.
The current audited Paper B source is `PaperB_EigenCoordinates_v2.1.tex`.
Paper B v2.1 is the continuous Lorentz/projective foundation: it uses the
two-sided Paper-A cone, the metric-dual cutting normal, the normalized generator
`Ghat=G/(2sqrt(|ab|))`, intrinsic projective normal forms `|z|=1` and
`xi_+ xi_-=1`, and distinguishes intrinsic orbit powers from chosen-equation
level-raising powers. `PaperB_EigenCoordinates_v2.tex/.pdf` are historical
predecessors after this promotion.

The current audited Paper C source is `PaperC_QuantumRealizations_v1.1.tex`,
with compiled snapshot `PaperC_QuantumRealizations_v1.1.pdf`. Paper C v1.1 is
the quantum-realization foundation downstream of Paper B v2.1. It uses the
global positive-discrete-series convention `k=(|n1-n2|+1)/2`, distinguishes the
conserved signed number-difference coordinate from the Bargmann label, corrects
the squeezing/classical parameter match, treats the `B_X` result as a scoped
Gaussian obstruction rather than an unproved universal no-go, and proves the
generic elliptic revival using `A^2=-ab I`. The former
`PaperC_QuantumRealizations.tex/.pdf` pair is historical after this promotion.

`Casimir_Null_Diamond_Standalone_v2.1.tex` is an active audited foundation.
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
`papers/Discriminant_12_Return_v0.3.4.tex` / `.pdf`. The v0.3.4 source is the
foundation-reconciled revision of v0.3.3: it separates ramified-ideal
coefficients from factor coordinates, uses the Paper-A v2.4 two-sided cone and
row/column convention, and distinguishes literal residue-field multiplication
from the transported mod-2 Pell action. In particular, multiplication by
`zeta_12` reduces literally to multiplication by `omega` on `F_4`, while the
mod-2 Pell matrix on `p_2/2p_2` becomes Frobenius only after the explicit
additive `F_2`-linear identification with `F_4`; direct residue multiplication
by `lambda=2+sqrt(3)` is the identity.

The v0.3.4 publication build completed successfully in GitHub Actions run
`33904189663` and committed the compiled paper and generated publication
figures in commit `92faf441e08e61fe8cd4359c7b6b0a63e7cdd22a`.

`Discriminant_12_Return_v0.3.3.tex/.pdf` and
`build_discriminant12_v0.3.3.sh` are retained as the preceding historical
publication snapshot and reproducible historical build. Earlier v0.1 and v0.2
sources are also retained as historical drafts. Companion publication material
is kept in the same `papers/` directory.

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

The area companion writes paper-specific outputs
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

`papers/build_discriminant12_v0.3.4.sh` calls all three Discriminant-12-owned
generators. The build stages a temporary copy whose historical tangent/divisor
figure names are remapped to the paper-specific outputs. The staged source must
be first on `TEXINPUTS` so TeX does not bypass the remapped copy and compile the
unstaged source. Paper A assets are not overwritten. The v0.3.3 build script
remains available only for reproducing the historical v0.3.3 snapshot.

The mod-12 geometry carries the four modular labels; the `V_4` operation remains
multiplication modulo 12, not adjacency in the drawing.

### Other foundation papers

`foundations/build_paper_b.sh` contains no figure-generation step; it compiles
`PaperB_EigenCoordinates_v2.1.tex`.

`foundations/build_paper_c.sh` contains no figure-generation step; it compiles
`PaperC_QuantumRealizations_v1.1.tex`. Paper C currently has no active
publication figure generator in `figures/`.

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
- `build-paper-b.yml` -> `foundations/build_paper_b.sh` -> `PaperB_EigenCoordinates_v2.1.tex`
- `build-paper-c.yml` -> `foundations/build_paper_c.sh` -> `PaperC_QuantumRealizations_v1.1.tex`
- `build-casimir-null-diamond.yml` -> `foundations/build_casimir_null_diamond.sh` -> `Casimir_Null_Diamond_Standalone_v2.1.tex`
- `build-discriminant12-paper.yml` -> `papers/build_discriminant12_v0.3.4.sh` -> `Discriminant_12_Return_v0.3.4.tex`

Publication workflows that invoke Matplotlib with LaTeX rendering install the
same TeX support used by the local generators, including `cm-super`. The
principal Discriminant-12 Matplotlib pipeline also requires `dvipng` for
LaTeX-rendered PNG output on the GitHub runner. Generated PDF/PNG binaries are
produced and committed by GitHub Actions; connector-side binary-write
limitations are not part of the CI build path.

Paper C v1.1's CI build completed successfully and committed
`foundations/PaperC_QuantumRealizations_v1.1.pdf` in commit
`edf120b01daf520c86d00adbc6a7fe179a536767`.

Principal paper v0.3.4's CI build completed successfully and committed
`papers/Discriminant_12_Return_v0.3.4.pdf` in commit
`92faf441e08e61fe8cd4359c7b6b0a63e7cdd22a`.

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
