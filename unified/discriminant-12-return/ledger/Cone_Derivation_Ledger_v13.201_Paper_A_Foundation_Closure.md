# Cone Derivation Ledger v13.201 — Paper A Foundation Closure

Date: 2026-09-03

## Scope

This entry returns from the frozen area branch to the main publication path and closes the two outstanding Paper A source issues while redirecting its area citation to the geometry-only companion.

## [Audit] Conic-classification edge case

The prior Paper A theorem classified every case with `ab<0` as a hyperbola. This omitted the apex case `c=0`.

For

\[
ax+by=0,\qquad ab<0,
\]

solving for `y` gives

\[
Y^2=xy=-\frac ab x^2.
\]

Thus the full algebraic cone section factors into two generator lines. On the positive-factor sheet/quadrant only one generator ray remains. The publication statement is now:

- `ab>0`: ellipse;
- `ab=0`: parabola;
- `ab<0, c\ne0`: nondegenerate hyperbola;
- `ab<0, c=0`: degenerate pair of cone generators in the full algebraic section, with one positive-factor generator ray.

Status: **[D] exact correction**.

## [Audit] n=11 triangular-domain wording

The anti-diagonal `x+y=12` itself does not contain 66 positive lattice cells. It bounds the triangular domain

\[
x+y\le12,
\]

which contains

\[
T_{11}=1+2+\cdots+11=66.
\]

Paper A now says explicitly that `x+y=12` is the smallest integer anti-diagonal **bounding** the positive divisor region and that the triangular region `x+y<=12` contains the 66 cells.

The matching comment in `fig_divisor_summatory_11_3panel.py` was corrected at the same time. No plotted geometry or numerical assertion changed.

Status: **[D] exact wording correction**.

## [S] Area citation consolidation

Paper A previously cited the historical semiclassical/LQG note for its non-area-preservation remark. The area branch has now produced a geometry-only foundation:

`foundations/Note_AreaDistortion_AMGM_Cone_v1.0.tex`

Paper A's bibliography now cites

> *Area Distortion and Exact Band Geometry of the AM--GM Cone* (2026)

and its area remark points specifically to the exact Jacobian, band areas, hyperbola/secant transport, and inverse weighted circle measure. No LQG interpretation is required by Paper A.

Status: **[S] source architecture correction**.

## [D] Exact area bridge retained as companion material

The geometry-only area companion establishes

\[
dX\,dY=\frac{T}{2Y}\,dx\,dy,
\]

and the inverse transported factor-area measure

\[
dx\,dy=2\cos\theta\,dX\,dY
       =2\operatorname{sech}s\,dX\,dY.
\]

The parabola–secant divisor chamber is retained in its focused foundation note and is not imported into Paper A's elementary proof chain.

## [Audit] Publication boundary

The area branch is now frozen unless a new theorem-level connection appears. The temporary normalized estimator

\[
\widetilde W_L(n)=\frac{8}{3\pi}(n-1)\sqrt n
\]

is not promoted: its apparent improvement at `n=11` is finite-scale and fails asymptotically. The exact weighted measure, not a constant normalization, is the publication-safe result.

## Main-path status

Paper A now has:

1. a corrected conic-classification theorem including the degenerate `ab<0,c=0` case;
2. corrected `n=11` triangular-domain wording;
3. a geometry-only area reference;
4. unchanged exact row/column, tangency, ellipse, Fermat, and divisor-summatory results;
5. a clean stopping boundary before arithmetic/operator material.

Next main-path task: begin the ground-up Paper B audit against the unified notation and the discriminant-12 return architecture.
