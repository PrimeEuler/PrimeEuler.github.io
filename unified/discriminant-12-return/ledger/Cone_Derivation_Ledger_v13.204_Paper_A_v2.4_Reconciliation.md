# Cone Derivation Ledger v13.204 — Paper A v2.4 Version Reconciliation

Date: 2026-09-04

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## 1. Version-history correction

**[Audit]** Paper A had two valid correction branches that were accidentally carried under inconsistent filenames:

1. `PaperA_ConicTheorem_v2.3.tex`, created by commit `92286f0dd974d1f9611f3782d5708169839a253a`, is the correct edge-case / area-companion baseline.
2. The later two-sided cone-projection work recorded in ledger v13.203 was mistakenly applied to `PaperA_ConicTheorem_v2.2.tex` rather than advancing the v2.3 source.

Therefore neither file alone was the correct current publication state.

## 2. Reconciled publication source

**[S]** The corrected current Paper A source is now

`foundations/PaperA_ConicTheorem_v2.4.tex`.

Creation commit:

`c3ee35d847513f5c5b332fafd022d31fa3273f1a`

This file takes v2.3 as the publication baseline and merges the exact two-sided projection results from v13.203.

## 3. Retained v2.3 corrections

**[S]** v2.4 retains the v2.3 corrections, including:

- the `ab<0, c=0` degenerate-generator edge case;
- the corrected statement that `x+y=12` bounds the triangular region `x+y<=12` containing `T_11=66` positive lattice cells;
- the geometry-only area companion citation and the explicit refusal of area preservation;
- the exact-area companion scope, including the flat Jacobian, induced cone-area factor, band geometry, hyperbola/secant partition, and inverse weighted circle measure.

## 4. Merged two-sided projection

**[D]** The fundamental Paper A projection is now

\[
\Pi_\pm(x,y)=
\left(
\frac{x-y}{2},\ \pm\sqrt{xy},\ \frac{x+y}{2}
\right),
\qquad Y^2=xy.
\]

The multiplication triangle is the flat carrier at `Y=0`, and each positive factor pair has two symmetric cone images.

## 5. Distinct involutions

**[D]** v2.4 keeps the two symmetries separate:

\[
(x,y)\leftrightarrow(y,x)
\quad\Longleftrightarrow\quad
X\mapsto-X,
\]

while

\[
\iota_Y:(X,Y,T)\mapsto(X,-Y,T)
\]

exchanges the two geometric cone lifts of the same factor pair.

These must not be conflated in Paper B or later work.

## 6. Complete conics and fixed-product levels

**[D]** With both signs of `Y` present:

- rows and columns are complete parabolas;
- fixed sums give complete circles;
- general linear cuts give the full `Y -> -Y` symmetric conic section;
- fixed products satisfy
  \[
  Y=\pm\sqrt N,
  \qquad T^2-X^2=N.
  \]

The `ab<0,c=0` case remains the degenerate pair of cone generators in the full algebraic section, with the positive-factor domain retaining the compatible generator ray.

## 7. Geometric complex conjugation

**[D]** On fixed-`T` circles,

\[
z=X+iY,
\qquad
z_-=\overline{z_+},
\qquad
z\bar z=T^2.
\]

**[Audit]** This is ordinary geometric complex conjugation only. No identification with the discriminant-12 cyclotomic/Galois conjugation is made without a separate theorem.

## 8. Area convention after reconciliation

**[Audit]** The Paper A conic geometry is two-sided, but the geometry-only area companion remains a single-valued upper-branch construction for planar transport. Its formulas are therefore one-sided unless explicitly doubled by reflection.

The v2.4 text preserves the v2.3 area-companion detail while making this one-sided convention explicit.

## 9. Figure provenance guardrail

**[Audit]** The Paper A figure generators and committed figure assets were **not changed** in the v2.4 reconciliation.

A straight Paper A recompilation must use the existing committed figure assets. Do not regenerate `fig_cutting_plane_3panel` or `fig_divisor_summatory_11_3panel` merely to rebuild the paper PDF, because regeneration can alter visual density/detail independently of the TeX corrections.

## 10. Current Paper A status

**[S]** Paper A v2.4 is now the authoritative source version for the discriminant-12-return project.

The earlier v2.2 and v2.3 files remain provenance snapshots and must not be treated as the current working source.

## 11. Paper B handoff

**[I]** Paper B must now be audited against Paper A v2.4, specifically:

- full two-sided cone geometry rather than an upper-half trace;
- distinction between factor exchange and cone-side reflection;
- complete conic sections, with connected-component and subgroup-transitivity questions still checked separately;
- no automatic identification of geometric complex conjugation with discriminant-12 arithmetic conjugation.

The next active foundation audit is Paper B from this v2.4 baseline.
