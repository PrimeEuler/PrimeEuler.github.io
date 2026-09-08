# Cone Derivation Ledger v13.334 — Uniform Midpoint Archimedean Buffer Enclosure

## Purpose

The v13.333 certification budget shows that the 67-dimensional finite buffer only needs roughly millesimal entrywise accuracy for positivity.  This checkpoint gives an elementary rigorous route for the only continuous matrix component: the smooth archimedean remainder.

For

\[
f_{mn}(t)=h(t)S_{mn}(t),\qquad 0\le t\le2,
\]

with odd modes \(m,n\le153\), the archimedean entry is

\[
(K_{\rm arch})_{mn}=-\int_0^2 f_{mn}(t)\,dt.
\]

## Uniform derivative bounds

Let

\[
k_{\max}=\frac{153\pi}{2}.
\]

Using the finite-frequency translation representation,

\[
|S_{mn}(t)|\le2,
\qquad
|S'_{mn}(t)|\le2k_{\max},
\qquad
|S''_{mn}(t)|\le2k_{\max}^2.
\]

From v13.311--v13.312,

\[
0<h(t)\le\frac14,
\qquad
|h'(t)|\le\frac1{48},
\qquad
|h''(t)|\le1.616
\]

is a convenient analytic majorant on \([0,2]\).

Therefore

\[
f''=h''S+2h'S'+hS'',
\]

and hence

\[
\boxed{
|f''_{mn}(t)|
\le
2(1.616)+\frac{k_{\max}}{12}+\frac{k_{\max}^2}{2}
<2.90\times10^4.
}
\]

## Composite midpoint certificate

For \(N\) equal panels on \([0,2]\), the midpoint rule satisfies

\[
|E_N|
\le
\frac{(2-0)^3}{24N^2}\sup|f''|
=
\frac{\sup|f''|}{3N^2}.
\]

Thus a uniform enclosure better than \(10^{-3}\) for **every** archimedean entry with \(m,n\le153\) is obtained with roughly

\[
\boxed{N\approx3200\text{ midpoint panels}.}
\]

The exact panel count from the rounded majorant is only a few thousand, not millions.

## Consequence

The pole can be dropped for lower bounds because it is PSD.  Prime entries are finite combinations of elementary trigonometric values.  Cusp entries use explicit Si/Ci formulas.  Therefore the full buffer positivity certificate no longer requires sophisticated adaptive quadrature:

\[
\boxed{
\text{coarse outward-rounded special-function evaluation}
+
\text{uniform 3200-panel midpoint enclosure}
}
\]

is already sufficient in principle for the archimedean part.

This is a major implementation simplification for the rigorous 67x67 buffer certificate.

## Guardrails

The derivative inequalities rely on the analytic h-bounds established in the earlier archimedean checkpoints.  A final proof implementation must outward-round every midpoint evaluation and the elementary/special-function constants.  No positivity of the full Suzuki operator, exact zero mode, lambda_1=0, RH, or GRH conclusion follows.

## Next target

Avoid verified inversion of the full 67x67 interval matrix.  Use a residual-certified solve: compute an approximate X for BX=C^T and certify it from the residual R=C^T-BX together with the lower bound B>=gamma I.  This should make the Schur correction enclosure depend only on ||R||/gamma rather than an interval inverse.