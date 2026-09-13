# Cone Derivation Ledger v13.407 — Odd Finite-High Midpoint Replay

Date: 2026-09-13

Status labels: **[D]** exact derived, **[N-replay]** independently reproduced numerical, **[O]** open.

## 1. Purpose

Continue the fail-closed odd-sector audit after v13.406 by independently reconstructing the finite high block

\[
F=\{22,24,\ldots,4000\}
\]

from the source-faithful scalar formulas, rather than importing the stored v13.404/v13.405 finite-high constants.

The new replay artifact is

`research-notes/suzuki_odd_M4000_finite_high_midpoint_replay.py`.

It is intentionally a midpoint regression artifact, not yet an outward interval certificate.

## 2. Source-faithful matrix reconstructed

The replay uses the canonical post-IBP same-parity formula

\[
(A_0)_{mn}
=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2},
\qquad m\ne n,
\]

with

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n,
\]

and the canonical cusp, prime, and archimedean diagonal formulas.

For the odd-v/even-index sector it adds the positive sinh pole channel

\[
2dd^T,
\qquad
 d_n=\frac{2k_n\sinh(1/2)}{k_n^2+1/4},
\qquad
 k_n=\frac{n\pi}{2}.
\]

Thus the replay does not read the stored finite-high eigenvalue, Cholesky residual, or inverse-factor norm.

## 3. Independent numerical reproduction

A fresh execution of the reconstructed 1990x1990 block gives

\[
\boxed{
\lambda_{\min}(A_{FF})
=0.5337449990275\ldots
}
\]

(the last displayed digits depend slightly on the adaptive quadrature run).

The historical transcript value was

\[
0.53374499902694\ldots,
\]

so the independent source reconstruction agrees at roughly the `10^{-12}` scale.

For

\[
B_F=A_{FF}-0.53I,
\]

the replay gives

\[
\boxed{
\lambda_{\min}(B_F)
=0.0037449990275\ldots
}
\]

and a binary64 Cholesky factorization with Frobenius reconstruction residual

\[
\boxed{
\|B_F-LL^T\|_F
\approx4.04\times10^{-14}.
}
\]

The implied midpoint inverse scale is

\[
\boxed{
\lambda_{\min}(B_F)^{-1/2}
=16.34083126\ldots,
}
\]

reproducing the stored transcript value `16.34083126127326`.

## 4. What this closes

This independently validates the **provenance and numerical reproducibility** of the finite-high transcript.  In particular, the `0.533745` value is not an unexplained decimal copied only from the old theorem checkpoint.

The visible midpoint distance above the desired floor is

\[
0.5337449990-0.53
\approx3.745\times10^{-3},
\]

which is enormous compared with the `10^{-13}` source-operator uncertainty scale used in the even-sector validated backend.

## 5. What remains open

The new replay still uses adaptive numerical quadrature and binary64 linear algebra.  Therefore this checkpoint does **not** by itself promote

\[
A_{FF}\succeq0.53I
\]

as a validated outward statement.

The next finite-block step is to transplant the already-audited scalar interval / exact-polynomial machinery from the even-sector high-block verifier to the even-index set `22..4000`, include the odd positive rank-one pole channel, and charge the factor arithmetic explicitly.  Because the shifted midpoint floor is about `3.745e-3`, the expected validation margin is very large.

The cross bound and frozen-eight-direction residual Gram remain independently open as stated in v13.406.

## 6. Guardrails

- This is an independent numerical replay, not an interval proof.
- No odd-sector inertia theorem is promoted here.
- The first two tiny odd-sector directions remain unresolved.
- No exact-zero, RH, or GRH conclusion follows.
