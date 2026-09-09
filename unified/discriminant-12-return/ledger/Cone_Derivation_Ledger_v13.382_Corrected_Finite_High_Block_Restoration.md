# Cone Derivation Ledger v13.382 — Corrected Finite High-Block Restoration

Date: 2026-09-09

Status labels: **[D]** exact derived, **[N-cert]** validated-computational, **[Audit]** correction/limitation, **[O]** open.

## Result

External Audit Rounds 20-21 invalidated the legacy rank-2 off-diagonal arch reconstruction and therefore invalidated the old v13.362 factorization transcript as a certificate for the intended operator.

The corrected operator has displacement rank at most four.  Using the exact centered arch generator gauge from v13.377, the corrected full 7991-mode midpoint factor has

\[
d_{\min}=0.25547908458536\ldots
\]

at mode 29, with

\[
\||L|\|_1<43.027,
\qquad
\||L|\|_\infty<3.727,
\qquad
y_{\max}<18.137.
\]

The forward inverse majorant gives

\[
\|L^{-1}\|_2^2\le7991\,y_{\max}^2,
\]

so a sufficient residual threshold is

\[
\frac{d_{\min}}{7991\,y_{\max}^2}>9.71\times10^{-8}.
\]

The corrected centered rank-4 local roundoff replay from v13.381 gives

\[
\|E_{\rm arith}\|_2<1.43\times10^{-8}.
\]

The exact-vs-polynomial arch uncertainty remains dimension-free after the audit correction because it is a kernel-level statement.  From

\[
\|h-h_{32}\|_\infty<6.1\times10^{-14}
\]

and Schur's test for the convolution kernel on \([-1,1]\),

\[
\|\Delta K_{\rm arch}\|_2<1.22\times10^{-13}.
\]

The prime/cusp scalar enclosures are unchanged by the arch formula correction and are over-resolved relative to this scale.  Retain the rounded total exact-vs-nominal matrix budget

\[
\|E_{\rm matrix}\|_2<2\times10^{-13}.
\]

Therefore

\[
\|E_{\rm total}\|_2<1.43002\times10^{-8}<9.71\times10^{-8}.
\]

Hence, under the stated validated-computational arithmetic and scalar-enclosure model,

\[
\boxed{A_{0,[21,16001]}\succeq0.22I.}
\]

A conservative transformed margin is still larger than 0.217.

## Audit reconciliation

**[Audit→resolved]** The old v13.362 conclusion is restored only through the corrected rank-4 architecture.  None of the superseded rank-2 factorization transcript is used as evidence for the repaired operator.

**[D]** The dimension-free arch matrix uncertainty survives because it is derived from the underlying kernel perturbation, not from the erroneous formula for individual off-diagonal entries.

## Remaining bottleneck

**[O]** This does not yet restore positivity of the full infinite high complement.  The remaining ingredients are:

1. outward certification of the corrected full cross norm, target \(<0.995\);
2. corrected tail coercivity at the interface \(N=16003\).

No exact-zero, RH, or GRH conclusion follows.
