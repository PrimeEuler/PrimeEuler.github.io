# Cone Derivation Ledger v13.210 — CI Workflow Reconciliation

Date: 2026-09-04

## Purpose

Reconcile the GitHub Actions publication workflows with the current authoritative build scripts, TeX versions, figure-generator names, and generated output paths under `unified/discriminant-12-return/`.

This checkpoint establishes that CI workflow maintenance is part of the publication-source change set rather than a later cleanup task.

## Findings

### Paper A

The existing `build-paper-a.yml` was stale. It still watched `PaperA_ConicTheorem_v2.3.tex`, referenced retired generic generator paths, and attempted to commit `PaperA_ConicTheorem_v2.3.pdf` even though `foundations/build_paper_a.sh` now builds `PaperA_ConicTheorem_v2.4.tex` using:

- `figures/paperA_cutting_plane_3panel.py`
- `figures/paperA_divisor_summatory_11_3panel.py`

The workflow was updated to the v2.4 pipeline and now tracks the compiled Paper A PDF together with its generated cutting-plane and divisor PDF/PNG assets.

### Area companion

`build-area-paper.yml` already matched `foundations/build_area_paper.sh`, `Note_AreaDistortion_AMGM_Cone_v1.1.tex`, and `paperA_area_measure_11_2panel.py`. The dependency installation was hardened for Matplotlib LaTeX rendering by explicitly installing `cm-super`, and the output commit step was normalized.

### Paper B

`build-paper-b.yml` is already synchronized with:

- `foundations/build_paper_b.sh`
- `foundations/PaperB_EigenCoordinates_v2.tex`
- `foundations/PaperB_EigenCoordinates_v2.pdf`

No figure-generator stage exists for Paper B at this checkpoint, so no workflow target change was required.

### Principal Discriminant-12 paper

The existing `build-discriminant12-paper.yml` was stale. It still invoked `papers/build_principal_paper.sh`, whose generator calls refer to retired generic publication scripts.

The authoritative reproducible v0.3.3 build is now:

- `papers/build_discriminant12_v0.3.3.sh`
- `figures/discriminant12_tangent_null_rays_3panel.py`
- `figures/discriminant12_divisor_summatory_11_3panel.py`
- `figures/discriminant12_mod12_v4_cone_triple.py`

The workflow was updated to call that build, promote the staged local-build PDF to the tracked canonical `Discriminant_12_Return_v0.3.3.pdf`, and commit the paper-owned generated figure assets.

## Dependency normalization

Workflows that run publication figure generators using Matplotlib `text.usetex=True` now install:

- `python3-numpy`
- `python3-matplotlib`
- `cm-super`
- `texlive-latex-base`
- `texlive-latex-recommended`
- `texlive-latex-extra`
- `texlive-fonts-recommended`

This mirrors the TeX support required by the audited local figure pipeline more closely and avoids relying on connector-side binary-writing capabilities. GitHub Actions itself can generate and commit PDF/PNG binaries normally.

## Bot-loop guard

Publication workflows use `if: github.actor != 'github-actions[bot]'` at the build-job level so generated-output commits do not recursively rebuild the same publication pipeline.

## Project invariant added to README

Whenever any of the following changes:

1. authoritative TeX version,
2. figure-generator filename,
3. build-script target,
4. generated publication output filename,

the corresponding `.github/workflows/*.yml` file must be reviewed and, when necessary, updated in the same change set.

Current active mapping:

- `build-paper-a.yml` -> `foundations/build_paper_a.sh` -> `PaperA_ConicTheorem_v2.4.tex`
- `build-area-paper.yml` -> `foundations/build_area_paper.sh` -> `Note_AreaDistortion_AMGM_Cone_v1.1.tex`
- `build-paper-b.yml` -> `foundations/build_paper_b.sh` -> `PaperB_EigenCoordinates_v2.tex`
- `build-discriminant12-paper.yml` -> `papers/build_discriminant12_v0.3.3.sh` -> `Discriminant_12_Return_v0.3.3.tex`

## Status

CI/publication workflow reconciliation complete for all four currently active workflows.

This checkpoint does not alter any mathematical theorem statement. It restores reproducible build provenance and removes known stale workflow references from the active CI path.
