# Cone Derivation Ledger v13.393

## M=3999 Six-Direction Full-Tail Hybrid Margin

### Status
**[N] + [D-tail] certification target.** The infinite tail beyond two million is bounded analytically, but the finite `M=3999` solve/eigenbasis is still midpoint floating point and has not yet received an interval/backward-error replay. No exact-zero, final inertia, RH, or GRH claim.

## 1. Context

v13.392 reinstated the source-faithful high-complement positivity chain and gave the Schur-tail lower floor

\[
\boxed{\delta_T>0.18225976374175623}.
\]

v13.390 identified the sharper terminal criterion on the six candidate-positive low-core directions

\[
W=\operatorname{span}\{v_5,\ldots,v_{10}\}:
\qquad
\delta_T>
\lambda_{\max}\!\left(S_W^{-1/2}R_W^*R_WS_W^{-1/2}\right).
\]

The present checkpoint computes this object deeply enough in the tail to determine whether a finite validation effort has realistic margin.

## 2. Stable source-faithful assembly

For high off-diagonal entries the exact compressed rank-two formula is used:

\[
(A_0)_{mn}=-\frac2\pi\frac{nZ_m-mZ_n}{n^2-m^2},
\]

with

\[
Z_n=2A_n+
\Im\psi\!\left(\frac14+i\frac{n\pi}{4}\right)
+n\pi\sum_{k\ge0}
\frac{e^{-2a_k}}{a_k^2+(n\pi/2)^2},
\qquad a_k=2k+\frac12.
\]

This reproduces the canonical component assembler to machine precision on tested pairs.

A numerical implementation issue was also isolated: ordinary adaptive quadrature for the highly oscillatory archimedean diagonal begins to fail at sufficiently large modes. Replacing it by weighted sine/cosine quadrature restores stable high-mode diagonal values. This is a numerical-assembly correction, not a change in the mathematical formula.

## 3. Finite Schur data at M=3999

Take

\[
F=\{21,23,\ldots,3999\}.
\]

The source-faithful finite Schur spectrum begins approximately

\[
(\text{four numerical-zero-scale levels},
\ 3.85764944\times10^{-8},
\ 2.16204593\times10^{-4},
\ 0.771253097,\ldots).
\]

As throughout this audit, the first four values are not interpreted as exact zero modes.

## 4. Explicit residual-Gram accumulation

Project the finite-to-tail residual into the finite Schur directions `5..10` and form the generalized residual Gram.

The accumulation behaves as follows:

\[
\begin{array}{c|c}
\text{tail stop}&\delta_{\rm crit}^{(\le \text{stop})}\\\hline
100000&0.1709676572\\
200000&0.1747741174\\
500000&0.1770639238\\
1000000&0.1778281916\\
2000000&0.1782105139
\end{array}
\]

The successive increments are already decaying in the expected leading-channel manner.

## 5. Analytic tail beyond two million

For fixed finite mode `m`, the full off-diagonal entry has the large-`n` expansion

\[
A_{nm}=\frac{L_m}{n}+O(n^{-2}),
\]

with exact leading coefficient

\[
L_m=-\frac2\pi Z_m+
\frac{8\cosh(1/2)}{\pi}c_m.
\]

After the finite solve and projection to the six-dimensional generalized coordinates, the leading `1/n` channel has midpoint squared coefficient norm

\[
\|q_{\rm norm}\|^2\approx1530.0464582084574.
\]

Using the exact geometric denominator remainder together with `|Z_n|<8`, the residual row remainder is bounded in the form

\[
\|e_n\|\le \frac{a}{n^2}+\frac{b}{n^3}.
\]

A deliberately componentwise absolute-value evaluation at

\[
N=2,000,001
\]

gives the remaining generalized-Gram envelope

\[
\boxed{\Delta_{>2\mathrm{m}}<8.938359453827081\times10^{-4}}.
\]

Therefore

\[
\delta_{\rm crit}^{\rm full}
<0.17821051391005885+0.0008938359453827081
\]

and hence

\[
\boxed{\delta_{\rm crit}^{\rm full}<0.17910434985544155}
\]

at the present hybrid midpoint/analytic level.

## 6. Margin against the reinstated certified floor

Compare with v13.392:

\[
0.18225976374175623-0.17910434985544155
=
\boxed{0.003155413886314684}.
\]

This is the central result of the checkpoint. The terminal six-direction validation problem no longer asks us to protect a raw `~4e-8` eigenvalue by a uniform operator error. After anisotropic residual projection and analytic tail completion, the remaining finite validation has approximately a `3e-3` margin.

## 7. What remains open

The following midpoint-dependent objects still need validation:

1. the `M=3999` finite solve;
2. the six-dimensional finite Schur subspace/eigenbasis, or an equivalent basis-free interval formulation;
3. the projected residual Gram through `n=2,000,000`;
4. the finite constants entering the analytic tail envelope.

A validated replay need not reproduce the midpoint to many digits. It only needs to keep the total outward error below roughly `3e-3`.

This is several orders of magnitude more forgiving than the earlier uniform `S10` target near `3e-9`.

## 8. Guardrails

- The first four low-core directions remain unresolved and are not exact kernels.
- The positive fifth finite-section value is not by itself an infinite-dimensional theorem.
- v13.393 is not a completed interval/MPFR certificate.
- No RH, GRH, exact-zero, or final inertia conclusion follows.

## 9. Next target

Replace the `M=3999` eigenspace-dependent calculation by a basis-stable verified formulation. Two acceptable routes are:

1. high-precision residual-certified finite Schur eigenspace plus interval Gram replay; or
2. a six-dimensional generalized LDL/Cholesky test that avoids explicitly interval-enclosing eigenvectors.

The second route is preferred if it preserves the current `~3.2e-3` margin cleanly.
