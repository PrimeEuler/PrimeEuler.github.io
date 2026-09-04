# Foundations Directory Inventory

Status: structural audit baseline, 2026-09-04.

This manifest records what each tracked item in `unified/discriminant-12-return/foundations/` is for, which files are active, which are historical, and which require further mathematical reconciliation. The authoritative project scope remains `unified/discriminant-12-return/`; similarly named files in the parent `unified/` directory are legacy sources only.

## Status vocabulary

- **ACTIVE / AUDITED BASELINE** — current source used by the project and already reconciled to the present foundation framework.
- **ACTIVE / NEEDS AUDIT** — current working source, but mathematical reconciliation remains before it should be treated as publication-authoritative.
- **COMPANION** — focused note supporting a foundation paper; not itself one of Papers A/B/C.
- **HISTORICAL** — superseded source or compiled snapshot retained for provenance.
- **EXPLORATORY** — useful research material whose claims are deliberately more tentative or physics-adjacent than the core foundation chain.
- **UTILITY** — computational audit code rather than publication source.
- **BUILD SCRIPT** — operational build entry point.

## Core foundation papers

| File | Role | Status | Audit note / next action |
|---|---|---|---|
| `PaperA_ConicTheorem_v2.4.tex` | Paper A: cutting-plane/conic theorem and two-sided factor-cone geometry | **ACTIVE / AUDITED BASELINE** | Current Paper A source. Uses `Y^2=xy`, distinguishes factor exchange from cone-side reflection, preserves the v2.3 edge-case/area corrections, and is the source built by `build_paper_a.sh`. |
| `PaperA_ConicTheorem_v2.3.tex` | Immediate predecessor of Paper A v2.4 | **HISTORICAL** | Retain as the pre-two-sided/reconciliation publication snapshot. |
| `PaperA_ConicTheorem_v2.3.pdf` | Compiled v2.3 snapshot | **HISTORICAL** | Useful visual/provenance baseline; do not use as current source. |
| `PaperA_ConicTheorem_v2.2.tex` | Earlier Paper A working source | **HISTORICAL** | Superseded by v2.3/v2.4. |
| `PaperA_ConicTheorem_v2.2.pdf` | Compiled v2.2 snapshot | **HISTORICAL** | Retain only for provenance if desired. |
| `PaperA_ConicTheorem_v2.tex` | Earlier major Paper A source | **HISTORICAL** | Superseded. |
| `PaperA_ConicTheorem_v2.pdf` | Earlier major Paper A compiled snapshot | **HISTORICAL** | Superseded. |
| `PaperB_EigenCoordinates_v2.tex` | Paper B: signed-cone Lorentz orbits, eigen-coordinates, power-map framework | **ACTIVE / NEEDS AUDIT** | Current build target. Already corrects several overclaims from the original Paper B, but still needs the planned projective normalization/global-orbit audit before publication-authoritative status. |
| `PaperB_EigenCoordinates_v2.pdf` | Current compiled Paper B v2 snapshot | **ACTIVE SNAPSHOT / NEEDS AUDIT** | Regenerate after the next Paper B mathematical audit. |
| `PaperB_EigenCoordinates.tex` | Original Paper B power-map/orbit formulation | **HISTORICAL / SUPERSEDED** | Contains stronger claims later weakened in v2 (canonical power map, parabolic obstruction, global-orbit language). Keep for provenance only. |
| `PaperB_EigenCoordinates.pdf` | Compiled original Paper B | **HISTORICAL / SUPERSEDED** | Provenance only. |
| `PaperC_QuantumRealizations.tex` | Paper C: SU(2)/SU(1,1) oscillator realizations and quantum fate of the power map | **ACTIVE FOUNDATION MATERIAL / NEEDS RECONCILIATION** | Its opening premise cites the older Paper B claim that every generator carries an exact power map. Its two-mode SU(1,1) section also needs the positive-discrete-series convention corrected globally to `k=(|n1-n2|+1)/2`, with `k=X` only in the oriented `n1>=n2` sector. Paper C must be reconciled downstream of the final Paper B audit before being treated as authoritative. |
| `PaperC_QuantumRealizations.pdf` | Compiled Paper C snapshot | **HISTORICAL SNAPSHOT / NEEDS REBUILD AFTER AUDIT** | Do not treat as synchronized with the eventual corrected Paper B framework. |

## Audited foundation candidate currently in `papers/`

| File | Role | Status | Audit note / next action |
|---|---|---|---|
| `../papers/Casimir_Null_Diamond_Standalone_v2_Audited.tex` | Exact Casimir completion / primitive null-edge bridge, with oscillator-cell and discriminant-12 interfaces | **AUDITED CORE / FOUNDATION PROMOTION RECOMMENDED** | Core determinant--Lorentz, midpoint-quarter, SU(2), SU(1,1), oscillator-cell, cyclotomic-normalization, and Boolean-return calculations pass the v13.209 audit. Create a corrected next version in `foundations/` rather than moving v2 unchanged. Required corrections are source-status wording, the global positive-discrete-series convention, transition-cell/state-point clarification, and a Farey projective-orientation qualification. Preserve the v2 TeX/PDF in `papers/` as the historical audited snapshot. |

See `../ledger/Cone_Derivation_Ledger_v13.209_Casimir_Null_Diamond_Audit.md` for the full mathematical audit.

## Geometry and area companion notes

| File | Role | Status | Audit note / next action |
|---|---|---|---|
| `Note_AreaDistortion_AMGM_Cone_v1.1.tex` | Exact area/Jacobian companion to Paper A | **ACTIVE COMPANION** | Current area-note source: exact flat Jacobian, induced cone area, hyperbola/secant partition, rapidity-angle compactification, and inverse weighted measure. `build_area_paper.sh` builds this version with the paper-specific `paperA_area_measure_11_2panel` figure. |
| `Note_AreaDistortion_AMGM_Cone_v1.1.pdf` | Compiled area-note snapshot | **ACTIVE SNAPSHOT** | Rebuilt by the area workflow. |
| `Note_AreaDistortion_AMGM_Cone_v1.0.tex` | Earlier area-note version | **HISTORICAL** | Superseded by v1.1. |
| `Note_Parabola_Secant_Divisor_Chamber_v1.0.tex` | Focused positive-factor chamber note | **COMPANION / NEEDS PLACEMENT REVIEW** | Studies the `x,y>=1`, `xy<=n` chamber, whose boundaries become two parabolas plus the secant `Y=sqrt(n)`. Mathematically related to the area branch; decide later whether it belongs in `foundations/`, a companion-notes subdirectory, or `research-notes/`. |
| `Note_SemiclassicalArea.tex` | Cone-band vs loop-quantum-gravity area-scaling comparison | **EXPLORATORY COMPANION** | Explicitly a normalization/consistency comparison rather than a derivation. It also depends on Paper C's oscillator dictionary, so it should remain downstream and non-core until Paper C is reconciled. |
| `Note_SemiclassicalArea.pdf` | Compiled semiclassical note | **EXPLORATORY SNAPSHOT** | Retain for provenance; rebuild only after upstream Paper C audit if the note remains in the publication branch. |

## Computational utility

| File | Role | Status | Audit note / next action |
|---|---|---|---|
| `discrete_staircase_pushforward.py` | Exact-formula numerical audit of staircase push-forward areas `W_T`, `W_H`, `W_D`, `W_A` | **UTILITY / MISPLACED** | Not a publication figure generator and not a foundation paper. Recommend moving to `research-notes/` or a project-local `tools/` directory after the directory-structure decision. |

## Build scripts

| File | Role | Status | Audit note / next action |
|---|---|---|---|
| `build_paper_a.sh` | Regenerates Paper A-owned figures and builds `PaperA_ConicTheorem_v2.4.tex` | **BUILD SCRIPT / ACTIVE** | Canonical Paper A build entry point. |
| `build_paper_b.sh` | Builds `PaperB_EigenCoordinates_v2.tex` | **BUILD SCRIPT / ACTIVE** | No figure-generation stage at present. |
| `build_area_paper.sh` | Regenerates the Paper A area-companion figure and builds area note v1.1 in isolation | **BUILD SCRIPT / ACTIVE** | Uses paper-specific `paperA_area_measure_11_2panel.pdf/png`; historical TeX filename is remapped only in the staging build. |

## Removed transient build files

The following TeX byproducts had been committed for Paper A v2.2 and were removed during this audit because they are reproducible transient build state, not source or publication artifacts:

- `PaperA_ConicTheorem_v2.2.aux`
- `PaperA_ConicTheorem_v2.2.log`
- `PaperA_ConicTheorem_v2.2.out`

## Current foundation dependency order

The working dependency order is:

1. **Paper A v2.4** — audited geometric/conic foundation.
2. **Area note v1.1** — one-sided measure companion to Paper A.
3. **Paper B v2** — Lorentz/eigen-coordinate extension; current but still under audit.
4. **Paper C** — quantum realization downstream of Paper B; requires reconciliation after Paper B is finalized.
5. **Casimir / Null-Diamond bridge** — core theorem audited; corrected next version recommended for `foundations/` after the Paper-C convention guardrails are incorporated.
6. **Semiclassical area note** — exploratory downstream comparison relying on the geometric and quantum dictionaries.

The principal Discriminant-12 paper is downstream publication material, but the null-diamond bridge independently rederives the discriminant-12 cyclotomic/Boolean interface it uses, so its core theorem does not logically depend on the principal paper.

`Note_Parabola_Secant_Divisor_Chamber_v1.0` is a focused geometric/area companion and does not alter this dependency chain.

## Recommended next cleanup, after review

No mathematical source was deleted during this structural audit. The next directory cleanup should be deliberate rather than automatic:

1. Create the corrected next Casimir/null-diamond source version directly in `foundations/`, while retaining the audited v2 TeX/PDF in `papers/` for provenance.
2. Decide whether historical Paper A/B versions stay in `foundations/` or move to a project-local `archive/` subdirectory.
3. Move `discrete_staircase_pushforward.py` out of `foundations/` into `research-notes/` or `tools/`.
4. Decide whether the two specialized notes (`Note_Parabola_Secant_Divisor_Chamber_v1.0` and `Note_SemiclassicalArea`) should live in a `companions/` subdirectory rather than beside Papers A/B/C.
5. Complete the Paper B v2 audit before changing the broader Paper C power-map discussion; then reconcile Paper C against the corrected Paper B definitions and invariants.
6. Add a Paper C build script only after its current authoritative source version is settled.
