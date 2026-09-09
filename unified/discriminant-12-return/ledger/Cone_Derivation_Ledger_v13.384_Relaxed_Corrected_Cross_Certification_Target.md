# Cone Derivation Ledger v13.384 — Relaxed Corrected Cross Certification Target

Date: 2026-09-09

Status labels: **[D]** exact derived, **[N]** numerical, **[O]** open, **[Audit]** limitation.

## Why the target can be relaxed

After v13.382 and v13.383, the corrected pole-free high complement has block lower bounds

\[
A_F\succeq0.22I,
\qquad
A_T\succeq4.6733I,
\]

with

\[
F=\{21,23,\ldots,16001\},
\qquad
T=\{16003,16005,\ldots\}.
\]

For the cross block \(G=A_{F,T}\), Schur positivity requires only

\[
\|G\|^2<0.22\cdot4.6733.
\]

Thus the admissible threshold is

\[
\boxed{\|G\|<1.01396548\ldots}.
\]

There is no mathematical need to retain the earlier aesthetic target \(<1\).

## Current corrected cross budget

The repaired rank-4 midpoint/analytic reconstruction gives

\[
\|G\|_{\rm midpoint,power-tail}\approx0.9927951.
\]

The remaining analytic tails are bounded by

\[
R_U<5.64\times10^{-4},
\qquad
R_{\rm geom}<3.7\times10^{-10},
\qquad
R_{\rm arch}<2.0\times10^{-10}.
\]

Hence before finite numerical-enclosure padding,

\[
\|G\|<0.99336+E_{\rm val}.
\]

The room to the exact Schur threshold is therefore larger than

\[
1.6\times10^{-2}.
\]

A deliberately loose outward validation bound

\[
E_{\rm val}<0.01
\]

would already imply

\[
\|G\|<1.00336<1.01,
\]

and at the rounded target \(\|G\|<1.01\), the Schur margin would still be

\[
0.22-\frac{1.01^2}{4.6733}>0.00171.
\]

## Guardrail

**[O]** The \(0.01\) finite-arithmetic/scalar validation envelope is a design target, not yet a proved outward enclosure.  Therefore this checkpoint does **not** yet restore global high-complement positivity.

The next proof object should be a deterministic corrected Gram/subspace calculation with an explicit outward error bound below \(0.01\).  The much larger allowed envelope means this can be intentionally conservative.

No exact-zero, RH, or GRH conclusion follows.
