# Cone Derivation Ledger v13.357

## Dimension-Free High-Block Matrix Uncertainty and Separation of Proof Budgets

This checkpoint sharpens the v13.355-v13.356 a-posteriori LDL strategy for the shifted pole-free high block

\[
B=A_{0,[21,16001]}-0.22I.
\]

The sufficient factor-residual target from v13.356 is approximately

\[
\|B-LDL^T\|_2<3.15\times10^{-6}.
\]

The new point is that the uncertainty in the exact matrix itself is many orders of magnitude smaller and does not scale badly with the 7991-dimensional truncation.

### 1. Archimedean truncation is dimension-free

From the degree-64 polynomial construction,

\[
\|h-h_{32}\|_{\infty}<6.1\times10^{-14}
\]

on \([0,2]\).  The induced convolution-kernel perturbation on \([-1,1]\) obeys Schur's test:

\[
\sup_x\int_{-1}^{1}|\delta h(|x-y|)|\,dy
\le 2(6.1\times10^{-14})
=1.22\times10^{-13}.
\]

Therefore every orthogonal compression, including the full 7991-mode block, satisfies

\[
\boxed{\|\Delta K_{\rm arch}\|_2\le1.22\times10^{-13}.}
\]

No factor of 7991 appears.

### 2. Prime/cusp scalar constants can be over-resolved

The prime block is reconstructed from five certified logarithms/base trigonometric constants and Chebyshev recurrences.  The cusp block is reconstructed from rational/series certificates for \(\operatorname{Si}(n\pi)\) and \(\operatorname{Ci}(n\pi)\).

For the final checker one may simply enclose all scalar constants far more tightly than needed, e.g. at radius \(10^{-30}\).  Even the crude matrix conversion

\[
\|\Delta A\|_2\le N\max_{ij}|\Delta A_{ij}|,
\qquad N=7991,
\]

then contributes less than \(8\times10^{-27}\) when the reconstructed entry radii are below \(10^{-30}\).

### 3. Separated proof budgets

A convenient global exact-vs-nominal target is therefore

\[
\boxed{\|B_{\rm exact}-B_{\rm nominal}\|_2<2\times10^{-13}.}
\]

This is more than seven orders of magnitude below the available LDL residual allowance

\[
3.15\times10^{-6}.
\]

Hence the final high-block proof should treat two logically distinct errors:

1. exact operator vs. high-precision nominal matrix: target \(<2\times10^{-13}\);
2. nominal matrix vs. point structured factorization: target comfortably below \(3\times10^{-6}\).

The first budget is essentially closed analytically.  The remaining work is a certified backward-error bound for the high-precision point generator-LDL arithmetic.

### Guardrail

This checkpoint does not yet certify positivity of the 7991-dimensional shifted block.  It only removes matrix-entry uncertainty as a meaningful bottleneck.  No exact-zero, RH, or GRH claim follows.
