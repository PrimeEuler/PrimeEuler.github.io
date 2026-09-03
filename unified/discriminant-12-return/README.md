# The Discriminant-12 Return

This folder collects the algebraic discriminant-12 branch of the Cone project
and the audited derivation trail used to build it.

## Foundation papers

The `foundations/` directory contains the current repository versions of the
four papers on which this branch directly builds:

- `PaperA_ConicTheorem_v2.tex` and `.pdf` — factor-cone and conic geometry;
- `PaperB_EigenCoordinates.tex` and `.pdf` — Lorentz dynamics and eigenframe;
- `PaperC_QuantumRealizations.tex` and `.pdf` — compact/noncompact oscillator
  realizations and Casimir completion;
- `Note_SemiclassicalArea.tex` and `.pdf` — audited band-area comparison.

The Paper A snapshot is accompanied by `fig_cutting_plane_3panel.py` and its
generated PDF/PNG assets. The recovered generator reproduces the reflected
cuts \(8x+4y=32\) and \(4x+8y=32\) used in Paper A v2.

These are copied here as project-local reference snapshots. Their original
files remain in the parent `unified/` directory.

## Papers

- `Discriminant_12_Return_v0.1.tex` and `.pdf` — initial theorem-first opening.
- `Discriminant_12_Return_v0.2.tex` and `.pdf` — current principal-paper draft.
  It adds the geometric mod-12 unit shell between the Pell–Lorentz and
  cyclotomic packages.
- `Casimir_Null_Diamond_Standalone_v2_Audited.tex` and `.pdf` — companion note
  containing the null-edge/Casimir quarter theorem, cyclotomic-quarter
  comparison, and ramified Boolean return.

## Research notes

- `Divisor_Summatory_V4_Mod12_Findings.md`
- `Jx_Jy_V4_Quarter_Shift_Findings.md`

These are retained as source research notes rather than cited as completed
theorems.

## Figures

- `mod12_v4_cone_triple.png` — three-panel realization of the unit residues
  \(\{1,5,7,11\}\) in Paper-A cone coordinates;
- `make_mod12_v4_cone_triple.py` — portable figure generator.

The figure realizes the four modular labels geometrically. Their \(V_4\)
operation remains multiplication modulo 12, not adjacency in the drawing.

## Ledger

The `ledger/` directory preserves audited consolidation checkpoints v13.162
through v13.169. The latest checkpoint is the current baseline; earlier files
are retained so the development can be reconstructed.

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
