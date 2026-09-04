# Foundations Directory Inventory

Status: structural audit baseline, reconciled 2026-09-04 through Paper C v1.1 promotion.

This manifest records the role and publication status of tracked material in `unified/discriminant-12-return/foundations/`. The authoritative project scope remains `unified/discriminant-12-return/`; similarly named files in the parent `unified/` directory are legacy/original sources only.

## Status vocabulary

- **ACTIVE / AUDITED BASELINE** — current authoritative foundation source, reconciled to the present framework.
- **ACTIVE COMPANION** — current supporting geometry/measure note.
- **HISTORICAL** — superseded source or compiled snapshot retained for provenance.
- **COMPANION / NEEDS PLACEMENT REVIEW** — mathematically useful supporting note whose directory placement remains open.
- **UTILITY / MISPLACED** — computational audit code that should eventually move out of `foundations/`.
- **BUILD SCRIPT / ACTIVE** — canonical publication build entry point.

## Core foundation papers

| File | Role | Status | Audit note |
|---|---|---|---|
| `PaperA_ConicTheorem_v2.4.tex` | Paper A: cutting-plane/conic theorem and two-sided factor-cone geometry | **ACTIVE / AUDITED BASELINE** | Current Paper A source; built by `build_paper_a.sh`. |
| `PaperA_ConicTheorem_v2.3.tex/.pdf` | Immediate Paper A predecessor | **HISTORICAL** | Pre-v2.4/two-sided reconciliation snapshot. |
| `PaperA_ConicTheorem_v2.2.tex/.pdf` | Earlier Paper A | **HISTORICAL** | Superseded. |
| `PaperA_ConicTheorem_v2.tex/.pdf` | Earlier Paper A | **HISTORICAL** | Superseded. |
| `PaperB_EigenCoordinates_v2.1.tex/.pdf` | Paper B: signed-cone Lorentz orbits, normalized eigen-coordinates, and intrinsic/chosen-equation power-map layers | **ACTIVE / AUDITED BASELINE** | Current authoritative Paper B. Incorporates the v13.213 audit and v13.214 promotion; built by `build_paper_b.sh`. |
| `PaperB_EigenCoordinates_v2.tex/.pdf` | Immediate Paper B predecessor | **HISTORICAL** | Core Lorentz geometry survives, but projective normalization/cutting-normal notation were superseded by v2.1. |
| `PaperB_EigenCoordinates.tex/.pdf` | Original Paper B formulation | **HISTORICAL** | Contains stronger canonical/universal power-map language later corrected. |
| `PaperC_QuantumRealizations_v1.1.tex/.pdf` | Paper C: two-oscillator `SU(2)`/`SU(1,1)` realizations and quantum comparison with Paper-B dynamics | **ACTIVE / AUDITED BASELINE** | Current authoritative Paper C. Incorporates v13.215 audit: `k=(|n1-n2|+1)/2`, exact number-difference conservation, corrected squeezing parameter match, scoped `B_X` Gaussian obstruction, distinct quantum-generator notation, and exact revival proof from `A^2=-ab I`. CI successfully built the PDF in commit `edf120b01daf520c86d00adbc6a7fe179a536767`. |
| `PaperC_QuantumRealizations.tex/.pdf` | Original Paper C formulation | **HISTORICAL** | Superseded by v1.1; retains stale universal power-map framing and the pre-audit Bargmann/revival wording. |
| `Casimir_Null_Diamond_Standalone_v2.1.tex/.pdf` | Exact Casimir completion / primitive null-edge bridge | **ACTIVE / AUDITED BASELINE** | Authoritative null-diamond source; incorporates the v13.209/v13.212 corrections and relocation. |

Audit trail: Paper B v13.213/v13.214; Paper C v13.215/v13.216 and promotion checkpoint v13.217; null-diamond v13.209/v13.212.

## Geometry and area companion notes

| File | Role | Status | Audit note |
|---|---|---|---|
| `Note_AreaDistortion_AMGM_Cone_v1.1.tex/.pdf` | Exact area/Jacobian companion to Paper A | **ACTIVE COMPANION** | Current geometry-only area source; built by `build_area_paper.sh`. |
| `Note_AreaDistortion_AMGM_Cone_v1.0.tex` | Earlier area companion | **HISTORICAL** | Superseded by v1.1. |
| `Note_Parabola_Secant_Divisor_Chamber_v1.0.tex` | Focused positive-factor chamber note | **COMPANION / NEEDS PLACEMENT REVIEW** | Studies `x,y>=1`, `xy<=n`; placement can be reviewed later. |

### Semiclassical/LQG branch — intentionally outside foundations

`Note_SemiclassicalArea.tex` is not a foundation source. Ledgers v13.196, v13.200, v13.201, and v13.211 establish that its geometry was extracted into the area-distortion companion and its LQG material remains exploratory. The live source is:

`../research-notes/Note_SemiclassicalArea.tex`

The former foundation-local TeX/PDF were removed; Git history preserves them.

## Computational utility

| File | Role | Status | Audit note |
|---|---|---|---|
| `discrete_staircase_pushforward.py` | Exact-formula numerical audit of staircase push-forward areas | **UTILITY / MISPLACED** | Candidate later move to `research-notes/` or project-local `tools/`. |

## Build scripts

| File | Target | Status |
|---|---|---|
| `build_paper_a.sh` | `PaperA_ConicTheorem_v2.4.tex` plus Paper-A-owned figures | **BUILD SCRIPT / ACTIVE** |
| `build_area_paper.sh` | `Note_AreaDistortion_AMGM_Cone_v1.1.tex` plus area figure | **BUILD SCRIPT / ACTIVE** |
| `build_paper_b.sh` | `PaperB_EigenCoordinates_v2.1.tex` | **BUILD SCRIPT / ACTIVE** |
| `build_paper_c.sh` | `PaperC_QuantumRealizations_v1.1.tex` | **BUILD SCRIPT / ACTIVE** |
| `build_casimir_null_diamond.sh` | `Casimir_Null_Diamond_Standalone_v2.1.tex` | **BUILD SCRIPT / ACTIVE** |

The matching active GitHub workflows are recorded in the project README and must remain synchronized with these targets.

## Removed transient and relocated material

Paper-A v2.2 TeX byproducts `.aux`, `.log`, and `.out` were removed as reproducible build state. The semiclassical/LQG source was moved to `research-notes/` and its old foundation-local PDF removed. The former live null-diamond v2 TeX/PDF in `papers/` were removed after v2.1 was promoted into `foundations/`. All remain recoverable through Git history.

## Current foundation dependency order

The working dependency order is:

1. **Paper A v2.4** — audited geometric/conic foundation.
2. **Area note v1.1** — one-sided measure companion to Paper A.
3. **Paper B v2.1** — audited continuous Lorentz/projective foundation.
4. **Paper C v1.1** — audited quantum-realization foundation downstream of Paper B.
5. **Casimir / Null-Diamond v2.1** — active audited discrete/oscillator bridge; its core theorem is independently established and its interfaces are now consistent with Paper C v1.1.

The semiclassical/LQG note is deliberately excluded from this chain. The principal Discriminant-12 paper is downstream publication material; the null-diamond bridge independently rederives the discriminant-12 cyclotomic/Boolean interface used there.

## Remaining deliberate cleanup

No current theorem source should be silently discarded or relocated. Remaining structural cleanup is optional and should be separately audited:

1. decide whether historical Paper A/B/C versions remain beside active foundations or move to a project-local archive;
2. move `discrete_staircase_pushforward.py` to `research-notes/` or `tools/` if desired;
3. decide the long-term placement of `Note_Parabola_Secant_Divisor_Chamber_v1.0.tex`;
4. audit downstream principal-paper references against the now-complete A/B/C/null-diamond foundation chain before changing the principal publication baseline.
