# Cone Derivation Ledger v13.394

## Preconditioned Six-Direction Verifier Contract

### Status
**[Design / proof contract].** This checkpoint converts the v13.393 hybrid midpoint margin into a finite validated-computational target. It is not itself the completed verifier run. No exact-zero, final inertia, RH, or GRH claim.

## 1. Inputs from the source-faithful chain

v13.392 gives the certified Schur-tail floor

\[
\delta_T>0.18225976374175623.
\]

v13.393 gives the hybrid midpoint-plus-analytic generalized residual target

\[
\delta_{\rm crit}^{\rm hyb}<0.17910434985544155,
\]

leaving normalized midpoint slack

\[
1-\frac{0.17910434985544155}{0.18225976374175623}
\approx
\boxed{0.0173127}.
\]

The purpose of the verifier is to replace the finite midpoint ingredients in v13.393 by outward enclosures without spending this slack unnecessarily.

## 2. Six-dimensional pencil

Freeze a six-column point basis \(Q\) spanning the finite candidate-positive sector and define

\[
B=Q^TS_FQ,
\qquad
G=R_Q^*R_Q,
\]

where the latter includes the explicit remote residual Gram plus the analytic PSD tail envelope.

The terminal positivity condition is

\[
\boxed{G<\delta_TB}.
\]

This formulation is basis-stable: \(Q\) need not itself be an interval eigenspace. It may be treated as exact dyadic/rational verifier input provided its span captures the intended finite six-dimensional sector and the resulting \(B\) is itself certified positive.

## 3. Why direct LDL of \(\delta_TB-G\) is poorly scaled

At \(M=3999\), the smallest finite candidate-positive Schur scale is only about

\[
3.86\times10^{-8}.
\]

Consequently the raw matrix \(\delta_TB-G\) can contain pivots at roughly the \(10^{-10}\) scale even though the normalized generalized margin is percent-level.

This is a conditioning issue, not a tail-size issue.

## 4. Preconditioned verifier

Let a verified Cholesky factorization of \(B\) be

\[
B=LL^T.
\]

Then form

\[
T=L^{-1}GL^{-T}.
\]

The target becomes

\[
\lambda_{\max}(T)<\delta_T,
\]

or equivalently

\[
\delta_TI-T\succ0.
\]

The normalized matrix has \(O(10^{-3})\) absolute slack rather than \(O(10^{-10})\) raw pivots.

## 5. Design tolerances

A conservative normalized outward-error budget is

\[
\boxed{\eta_{\rm norm}=0.005},
\]

which is less than one third of the midpoint normalized slack.

The finite \(B\) certification is a separate high-precision task. A reasonable initial absolute target is

\[
\boxed{\|\Delta B\|<10^{-10}},
\]

comfortably below the observed fifth finite scale.

The residual-Gram / normalized solve stage can be much coarser because its natural comparison margin is percent-level.

## 6. Required replay stages

1. Store/freeze the six-column point basis \(Q\) as exact verifier input.
2. Enclose the source-faithful \(M=3999\) finite Schur matrix \(S_F\).
3. Form/enclose \(B=Q^TS_FQ\) and certify \(B\succ0\).
4. Enclose the projected residual Gram through \(n=2,000,000\).
5. Add the v13.393 analytic PSD tail envelope beyond two million.
6. Precondition by the certified factor of \(B\).
7. Certify \(\delta_TI-T\succ0\) by interval LDL or a residual/Weyl bound.

## 7. Guardrails

- This does not certify the first four near-zero directions.
- The finite fifth Schur value remains a finite object until the above pencil inequality is validated.
- No exact-zero, final inertia, RH, or GRH conclusion follows.
