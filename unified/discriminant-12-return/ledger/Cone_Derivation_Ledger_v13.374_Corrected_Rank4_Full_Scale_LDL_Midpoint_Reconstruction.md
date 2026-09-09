# Cone Derivation Ledger v13.374 — Corrected Rank-4 Full-Scale LDL Midpoint Reconstruction

Date: 2026-09-09

## Status

This checkpoint is the first full-scale structured-LDL rerun after the v13.373 audit reconciliation.  It uses the corrected archimedean off-diagonal formula and the resulting displacement-rank-at-most-four generator system.  Values here are midpoint numerical diagnostics; the renewed a-posteriori arithmetic residual replay is still required before the finite block is re-certified.

## Corrected generator pairs

For

\[
U_n=\operatorname{Si}(n\pi)+2A_n,
\qquad
Y_n=nH_n,
\]

the corrected off-diagonal matrix is

\[
(A_0)_{mn}
=\frac{2}{\pi}\frac{nU_m-mU_n}{m^2-n^2}
+\pi mn\frac{Y_n-Y_m}{m^2-n^2}.
\]

Thus with \(X=\operatorname{diag}(n^2)\), one may use two skew generator pairs

\[
(U,n),\qquad (n,n^2H_n),
\]

with coefficients \(2/\pi\) and \(\pi\), respectively.  Every scalar Schur step updates all four generator vectors by the same multiplier column.

## Dense end-to-end cross-check

The canonical dense assembler from v13.373 and the rank-four recurrence were compared on odd modes \(21..399\).  Their scalar LDL pivots agree to about

\[
4.3\times10^{-10}.
\]

The remaining difference is consistent with using direct numerical quadrature for the canonical arch data versus the degree-65 polynomial reconstruction in the structured recurrence.  Entrywise corrected generator reconstruction agrees with the canonical matrix at ordinary machine precision at tested off-diagonal pairs.

## Full 7991-pivot midpoint run

For odd modes

\[
21,23,\ldots,16001
\]

and shift \(0.22I\), the corrected structured recurrence gives

\[
\boxed{\min_j d_j\approx0.255479084585364}
\]

at

\[
\boxed{n=29}.
\]

For comparison, the legacy wrong-matrix recurrence had minimum pivot

\[
0.254299623644300.
\]

Thus the audit correction slightly **increases** the midpoint pivot margin.

Factor-growth diagnostics for the corrected run are

\[
\boxed{\||L|\|_1\approx43.02617},
\qquad
\boxed{\||L|\|_\infty\approx3.72623},
\]

with largest individual multiplier about \(1.01021\).  These are slightly smaller than the legacy factor-growth values used by the old residual certificate.

Late pivots remain \(O(8)\); no midpoint pivot approaches zero.

## Consequence and proof status

The corrected finite matrix is numerically at least as well conditioned for a residual certificate as the legacy matrix.  However, v13.362 remains superseded until the arithmetic replay is rerun on the four-generator recurrence.  No old residual transcript is being reused automatically.

The next finite-block target is therefore unchanged in form:

\[
A_{0,[21,16001]}^{\rm corrected}\succeq0.22I,
\]

but it must be established from a fresh corrected-factor residual bound.

After that, the cross operator must also be recomputed using the corrected two-channel Cauchy form; the v13.365 six-plane numbers are not transferable.

## Guardrail

This does not restore global high-complement positivity yet.  It is a corrected full-scale midpoint reconstruction showing that the finite-block part is likely salvageable with comfortable margin.
