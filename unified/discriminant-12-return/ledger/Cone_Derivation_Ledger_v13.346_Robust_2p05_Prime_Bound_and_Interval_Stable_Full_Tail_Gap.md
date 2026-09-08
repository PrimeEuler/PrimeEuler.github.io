# Cone Derivation Ledger v13.346 — Robust 2.05 Prime Bound and Interval-Stable Full-Tail Gap

## Purpose

The six-dimensional full-tail bridge of v13.345 had a large positive margin, but its analytic tail gap still inherited the old non-interval decimal

\[
\|B_{\rm prime}\|\le 2.044764260347282\ldots.
\]

This checkpoint deliberately weakens that constant to a rounded certification target

\[
\boxed{\|B_{\rm prime}\|<2.05}
\]

and checks that the full bridge remains strongly positive at the design level.

## Why 2.05 is easy to certify

The exact finite k=16 power-Schur reduction from v13.310 gives the ordinary floating midpoint value

\[
\sup_x (A^{16}\mathbf 1)(x)\approx 93388.18411213082.
\]

By comparison,

\[
2.05^{16}\approx 97288.5603556106.
\]

Therefore the finite verification has absolute slack

\[
\boxed{97288.5603556106-93388.18411213082\approx3900.37624}.
\]

This is far larger than any reasonable outward-rounding allowance.

The 16th sweep has 3345 intervals.  The smallest midpoint spacing between consecutive breakpoints is approximately

\[
\boxed{9.51946\times10^{-5}}.
\]

Each breakpoint is of the form

\[
\pm1+\sum_q c_q\log q,
\]

with integer coefficients and total path length at most 16.  Hence enclosing every required logarithm with radius \(10^{-10}\) gives endpoint radii below \(2\times10^{-9}\), more than four orders of magnitude below the minimum observed separation.  The breakpoint ordering is therefore a numerically easy interval task.

The remaining finite maximum evaluation uses only positive weighted sums.  A final proof-grade implementation should evaluate the same 3345-interval sweep with outward rational intervals and check directly that the upper endpoint of \(\sup A^{16}\mathbf1\) remains below \(2.05^{16}\).

## Robust N=155 tail gap

Replace the old prime constant in the analytic v13.312 tail margin by 2.05:

\[
\alpha_N
=
\log(N/4)-\frac\pi2-2.05-\beta_{\rm cusp}(N)-\beta_{\rm arch}(N).
\]

At \(N=155\), the existing analytic localized bounds give approximately

\[
\beta_{\rm arch}(155)\approx0.0106562051,
\qquad
\beta_{\rm cusp}(155)\approx0.0007285328,
\]

and therefore

\[
\boxed{\alpha_{155}\approx0.0249496912>0.}
\]

Thus the working tail split remains coercive even after intentionally degrading the prime norm bound.

## Effect on the v13.345 six-dimensional full-tail bridge

For the fixed rational protected subspace candidate \(W\), use the conservative combined coupling scale

\[
\beta_{\rm total}\approx8.871\times10^{-3}.
\]

Then the full adverse Schur penalty is bounded at the design level by

\[
\frac{\beta_{\rm total}^2}{\alpha_{155}}
\approx3.16\times10^{-3}.
\]

Against the finite pole-free protected minimum

\[
\lambda_{\min}(W^TA_{0,FF}W)\approx0.1874455915,
\]

this leaves approximately

\[
\boxed{0.1843}
\]

of positive margin.

So the proof no longer depends on the delicate decimal \(2.0447642603\ldots\).  A coarse rigorous bound \(2.05\) is more than sufficient.

## Structural consequence

The main infinite-dimensional bridge now has a deliberately robust certification target:

1. certify the finite power-Schur inequality \(\sup A^{16}\mathbf1<2.05^{16}\);
2. conclude \(\alpha_{155}>0.0249\) from analytic cusp/arch tails;
3. certify the fixed rational six-plane finite quadratic form and finite 155..3001 Frobenius coupling;
4. append the analytic \(n\ge3003\) remainder;
5. retain a final margin of order \(10^{-1}\), not \(10^{-8}\).

This makes the final bridge insensitive to small interval overestimates.

## Guardrails

- The 2.05 power-Schur inequality is not yet interval-instantiated in this checkpoint; the finite midpoint slack and breakpoint separation show that certification should be straightforward.
- The finite rational \(77\times6\) witness still needs direct interval evaluation.
- No exact zero mode, \(\lambda_1=0\), RH, or GRH conclusion follows.
