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
- `figures/` — Canonical project figure generators and generated figure assets,
  including all figures used by the foundation papers.
- `ledger/` — Derivation, audit, publication, and checkpoint ledger entries.

Before any GitHub write, verify that the target path begins with
`unified/discriminant-12-return/`. Foundation-paper edits in particular must
begin with `unified/discriminant-12-return/foundations/`.

## Foundation papers

The `foundations/` directory contains the **authoritative project-local working
versions** of the foundation material for this branch. In particular, the
current Paper A source is:

- `PaperA_ConicTheorem_v2.4.tex` — factor-cone and conic geometry with the
  two-sided projection `Y^2=xy`;
- `PaperB_EigenCoordinates.tex` / `PaperB_EigenCoordinates_v2.tex` — Lorentz
  dynamics and eigenframe working sources;
- `PaperC_QuantumRealizations.tex` — compact/noncompact oscillator realizations
  and Casimir completion;
- companion area and geometry notes.

Figure generators do **not** belong in `foundations/`. Foundation TeX files read
publication figures from `../figures/`, and build scripts must invoke generators
from that directory. This prevents stale local figure files from shadowing the
canonical generated assets.

Files of the same or similar names in the parent `unified/` directory may be
retained as historical/original sources, but they are **not** the working copies
for the discriminant-12-return project and must not be updated as part of this
project.

## Papers

- `Discriminant_12_Return_v0.1.tex` and `.pdf` — initial theorem-first opening.
- `Discriminant_12_Return_v0.2.tex` and `.pdf` — earlier principal-paper draft.
- `Discriminant_12_Return_v0.3.3.tex` and `.pdf` — current principal-paper
  publication baseline used for the paper-specific geometry audit.
- `Casimir_Null_Diamond_Standalone_v2_Audited.tex` and `.pdf` — companion note
  containing the null-edge/Casimir quarter theorem, cyclotomic-quarter
  comparison, and ramified Boolean return.

## Research notes

- `Divisor_Summatory_V4_Mod12_Findings.md`
- `Jx_Jy_V4_Quarter_Shift_Findings.md`

These are retained as source research notes rather than cited as completed
theorems.

## Figures

Figure generators are **paper-owned publication sources** even though they all
live in the shared `figures/` directory. A generator or output used by one paper
must not be silently reused as the publication asset for another paper merely
because the underlying geometry is related. Each publication pipeline should
have its own generator/output names whenever the visual purpose differs.

### Paper A

Paper A uses:

- `fig_cutting_plane_3panel.py` — self-contained Paper A cutting-plane generator.
  It draws every fixed-sum shell `K=1,...,12`, the complete two-sided row/column
  parabolas and reflected ellipse cuts, the exact `u=5,6,7` tangent-circle
  examples, and the correctly clipped positive-factor row/column mesh in the
  `(X,T)` side view. It writes `fig_cutting_plane_3panel.pdf/png`.
- `fig_divisor_summatory_11_3panel.py` — Paper A's `n=11` divisor-summatory
  figure. Its displayed `(X,Y)` and 3D views intentionally use the upper branch
  `Y=+sqrt(xy)` as a one-sided visualization; Paper A's underlying geometry is
  the two-sided relation `Y^2=xy`. It writes
  `fig_divisor_summatory_11_3panel.pdf/png`.
- `fig_area_measure_11_2panel.py` — companion area-note figure generator.

`foundations/build_paper_a.sh` generates Paper A's publication figures from
`figures/` before compiling `PaperA_ConicTheorem_v2.4.tex`. The area-paper build
likewise invokes its figure generator from `figures/`.

### The Discriminant-12 Return

The principal Discriminant-12 paper now has independent publication generators:

- `discriminant12_tangent_null_rays_3panel.py` — reproduces the v0.3.3
  parabola-circle/null-ray figure with the complete `K=1,...,12` fixed-`T`
  family and emphasized `u=5,6,7` row/column parabola tangencies. It writes
  `discriminant12_tangent_null_rays_3panel.pdf/png`.
- `discriminant12_divisor_summatory_11_3panel.py` — independent `n=11` divisor
  figure for the principal paper. It writes
  `discriminant12_divisor_summatory_11_3panel.pdf/png` and does not overwrite
  Paper A's divisor assets.
- `make_mod12_v4_cone_triple.py` — three-panel realization of the unit residues
  `{1,5,7,11}` in factor-cone coordinates, writing `mod12_v4_cone_triple.png`.

`papers/build_discriminant12_v0.3.3.sh` regenerates the Discriminant-12-owned
figures and compiles an isolated staging copy of v0.3.3 whose two historical
figure references are remapped to the new paper-specific filenames. The
historical v0.3.3 source is therefore preserved while the current build no
longer overwrites Paper A figure outputs.

The mod-12 figure realizes the four modular labels geometrically. Their `V_4`
operation remains multiplication modulo 12, not adjacency in the drawing.

## Ledger

The `ledger/` directory preserves the audited derivation trail and publication
checkpoints for this project. The highest valid checkpoint should be treated as
the current baseline; earlier files are retained so the development can be
reconstructed.

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
