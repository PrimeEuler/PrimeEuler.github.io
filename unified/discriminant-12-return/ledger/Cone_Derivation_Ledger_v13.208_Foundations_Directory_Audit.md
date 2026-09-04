# Cone Derivation Ledger v13.208 — Foundations Directory Audit

Date: 2026-09-04

## Scope

This checkpoint audits the tracked contents of
`unified/discriminant-12-return/foundations/` as a directory structure. It does
not certify every mathematical claim in every foundation paper. Its purpose is
to establish which files are current, historical, companion, exploratory,
operational, or misplaced before further Paper B/Paper C theorem auditing.

The authoritative file-by-file manifest is:

`foundations/FOUNDATIONS_INVENTORY.md`

## Area-companion output cleanup

The Paper A area-companion generator is

`figures/paperA_area_measure_11_2panel.py`.

It now writes only the paper-specific publication assets

- `paperA_area_measure_11_2panel.pdf`
- `paperA_area_measure_11_2panel.png`.

`foundations/build_area_paper.sh` builds `Note_AreaDistortion_AMGM_Cone_v1.1.tex`
in an isolated staging directory and remaps the historical figure reference to
the paper-specific output name. The GitHub area-paper workflow tracks the new
generator/output names. The obsolete generic area binaries
`fig_area_measure_11_2panel.pdf/png` were removed.

## Foundation classification

### Paper A

`PaperA_ConicTheorem_v2.4.tex` remains the active audited geometric baseline.
Earlier v2, v2.2, and v2.3 sources/compiled snapshots are historical provenance.
The v2.3 PDF remains particularly useful as a visual baseline for the publication
figures.

### Paper B

`PaperB_EigenCoordinates_v2.tex` is the current build target and is materially
improved over `PaperB_EigenCoordinates.tex`, but it remains under mathematical
audit. The original Paper B is classified as historical/superseded because its
canonical power-map and orbit claims are stronger than the corrected v2
formulation supports.

### Paper C

`PaperC_QuantumRealizations.tex` is retained as downstream foundation material,
but is not currently an audited publication baseline. Its introduction assumes
the older Paper B statement that every cone generator carries an exact power
map. Paper C must therefore be reconciled after the final Paper B audit.

### Companion notes

`Note_AreaDistortion_AMGM_Cone_v1.1.tex` is the active exact area/Jacobian
companion to Paper A. `Note_AreaDistortion_AMGM_Cone_v1.0.tex` is historical.

`Note_Parabola_Secant_Divisor_Chamber_v1.0.tex` is a focused geometric/area
companion studying the chamber bounded by the row-1/column-1 parabolas and the
constant-product secant.

`Note_SemiclassicalArea.tex` is explicitly exploratory downstream physics
material: it compares cone-band scaling with loop-quantum-gravity area scaling
and should not be folded into the core theorem chain.

### Utility and build scripts

`discrete_staircase_pushforward.py` is a numerical/exact-formula audit utility,
not a foundation paper or publication figure generator. It is marked as
misplaced pending a later move to `research-notes/` or a project-local tools
location.

The active operational scripts are `build_paper_a.sh`, `build_paper_b.sh`, and
`build_area_paper.sh`.

## Transient files removed

The following committed TeX build byproducts for Paper A v2.2 were deleted:

- `PaperA_ConicTheorem_v2.2.aux`
- `PaperA_ConicTheorem_v2.2.log`
- `PaperA_ConicTheorem_v2.2.out`

No mathematical source or historical PDF was deleted in this audit.

## Dependency order after audit

The working foundation dependency chain is now explicitly:

1. Paper A v2.4 — audited geometric/conic foundation.
2. Area note v1.1 — one-sided measure companion to Paper A.
3. Paper B v2 — Lorentz/eigen-coordinate extension, still under audit.
4. Paper C — quantum realization downstream of Paper B, requiring reconciliation.
5. Semiclassical area note — exploratory downstream comparison.

The parabola/secant chamber note is a focused companion and does not alter the
main dependency chain.

## Next audit

The next substantive theorem audit should be Paper B v2. Only after its
projective normalization, orbit-component, and power-map statements are settled
should Paper C be rewritten/reconciled. Directory moves or archival subfolders
should be performed after reviewing the new foundations manifest rather than by
blind filename cleanup.
