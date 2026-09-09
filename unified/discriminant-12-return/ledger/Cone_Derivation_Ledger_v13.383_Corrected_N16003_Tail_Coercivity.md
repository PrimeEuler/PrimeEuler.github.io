# Cone Derivation Ledger v13.383 — Corrected N=16003 Tail Coercivity

Date: 2026-09-09

Status labels: **[D]** exact derived, **[N-cert]** validated-computational, **[Audit]** correction/limitation, **[O]** open.

## Result

The tail coercivity estimate survives External Audit Rounds 20-21 because its archimedean part was derived directly from the convolution kernel \(K_r(x,y)=-h(|x-y|)\), not from the superseded off-diagonal formula.

Using the validated prime operator bound

\[
\|B_{\rm prime}\|<2.05,
\]

the cusp tail localization from the Hilbert decomposition, and the direct kernel estimate

\[
|(K_r)_{mn}|\le \frac{C_r}{k_mk_n},
\qquad
C_r=8.047038193418354\ldots,
\]

we have for odd modes \(n\ge N\)

\[
\alpha_N
=
\log(N/4)-\frac\pi2-2.05-\beta_{\rm cusp}(N)-\beta_{\rm arch}(N).
\]

At \(N=16003\),

\[
\beta_{\rm cusp}<6.395\times10^{-6},
\qquad
\beta_{\rm arch}<1.020\times10^{-4},
\]

and numerically from the explicit analytic formulas,

\[
\alpha_{16003}=4.6733324910\ldots.
\]

Retain the rounded certified target

\[
\boxed{A_{0,[16003,\infty)}\succeq4.6733I.}
\]

The pole term is positive semidefinite, so the corresponding full even-v tail lower bound is no worse.

## Audit reconciliation

**[Audit→resolved]** No legacy off-diagonal arch identity enters this estimate.  The correction discovered in Rounds 20-21 therefore does not alter the proof.

## Current high-complement ingredients

The corrected finite block from v13.382 gives

\[
A_{0,[21,16001]}\succeq0.22I.
\]

This checkpoint gives

\[
A_{0,[16003,\infty)}\succeq4.6733I.
\]

The only remaining ingredient for global high-complement positivity is a certified corrected cross bound.  The current midpoint/analytic-tail work targets

\[
\|G\|<0.995.
\]

If that target is certified, the Schur margin will be

\[
0.22-\frac{0.995^2}{4.6733}>0.00815.
\]

No exact-zero, RH, or GRH conclusion follows.
