# Cone Derivation Ledger v13.362

## Validated long-double high-block certificate and 0.22 finite closure

### Status

This checkpoint closes the finite pole-free block

\[
A_{0,[21,16001]}\succeq 0.22I
\]

under the explicitly stated validated software-arithmetic model.  It does **not** yet close the full infinite high complement.

### Exact structure

For odd modes and

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n,
\]

the pole-free off-diagonal matrix satisfies

\[
(A_0)_{mn}=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2}.
\]

Equivalently,

\[
XA_0-A_0X=\frac2\pi(uv^T-vu^T),
\quad X=\operatorname{diag}(n^2),\ u=(Z_n),\ v=(n).
\]

Scalar Schur complements preserve this rank-two displacement structure exactly, enabling an O(N^2)-arithmetic, O(N)-state no-pivot LDL recurrence for the 7991-dimensional block.

### Scalar-data enclosure

High-precision scalar midpoints were generated from the nonquadrature formulas developed in v13.338--v13.343:

- prime piece from high-precision log/sqrt/trigonometric evaluation;
- cusp piece from the explicit n>=21 asymptotic Si/Ci expansions and first-omitted bounds;
- archimedean piece from the exact rational h_32 polynomial and I_p/J_p recurrences.

A 60-digit `mpmath.iv` interval audit found:

\[
\max_{21\le n\le16001}\operatorname{rad}(A_n)<2.15\times10^{-56},
\]

prime diagonal radius <1.01e-56, cusp Si/Ci radius at n=21 <7.0e-30, and arch polynomial arithmetic radius <5e-62.

The dominant exact-vs-polynomial matrix uncertainty is therefore the analytic h_32 kernel tail:

\[
\boxed{\|\Delta K_{\rm arch}\|_2<1.2180332746458045\times10^{-13}}.
\]

### Arithmetic model

The structured LDL was run using NumPy `longdouble` on a runtime reporting a 64-bit significand, hence standard round-to-nearest unit roundoff

\[
u=2^{-64}.
\]

Each Schur update was charged with a conservative per-operation error model and inserted into the v13.359 local Frobenius-defect formula.  If \(\delta_k\) bounds the local defect, then

\[
\|E_{\rm arith}\|_2
\le \||L|\|_1\,\||L|\|_\infty\sum_k\delta_k.
\]

This is a validated computational certificate under the stated interval backend and IEEE-style round-to-nearest long-double model; it is not represented as a machine-independent formal proof kernel.

### Validated transcript

\[
\boxed{\min d_j=0.25429962364429952527}
\]

at mode n=29.

\[
\boxed{\||L|\|_1=43.63817093391197109},
\qquad
\boxed{\||L|\|_\infty=3.7433565044520330225}.
\]

\[
\boxed{\sum_k\delta_k=2.2801510695454563477\times10^{-11}}.
\]

Crude full-growth arithmetic residual:

\[
\boxed{\|E_{\rm arith}\|_2<3.7247004439625296\times10^{-9}}.
\]

Prefix-weighted version:

\[
\boxed{\|E_{\rm arith}\|_2<3.5190480723800256\times10^{-9}}.
\]

Adding the matrix uncertainty gives the conservative total

\[
\boxed{\|E_{\rm total}\|_2<3.724822247289995\times10^{-9}}.
\]

The earlier a-posteriori positivity allowance from v13.356 was

\[
\|E_{\rm total}\|_2<3.15\times10^{-6}.
\]

Thus the certificate has nearly three orders of magnitude of residual margin and also satisfies the stronger design guards

\[
\min d_j>0.25,\qquad
\|E_{\rm arith}\|_2<10^{-8},\qquad
\|E_{\rm matrix}\|_2<2\times10^{-13}.
\]

Therefore, under the stated validated-arithmetic model,

\[
\boxed{A_{0,[21,16001]}\succeq0.22I}.
\]

### What remains for the infinite high complement

For

\[
\mathcal D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\text{ odd}\},
\]

the remaining proof obligations are:

1. certify the interface cross norm
   \[
   \|A_{0,[21,16001],[16003,\infty)}\|<1;
   \]
2. certify the analytic tail lower bound at n>=16003, in particular harden the robust prime target
   \[
   \|B_{\rm prime}\|<2.05.
   \]

Once both hold, with \(\alpha_{16003}>4.673\), Schur complement gives a positive high-complement margin of roughly 0.006.

### Guardrail

This checkpoint does not establish positivity of the full infinite complement, does not yet reduce global inertia to the ten low modes, and makes no exact-zero, RH, or GRH claim.
