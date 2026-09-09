# Cone Derivation Ledger v13.364 — Cross-Block Certificate Reduction to Dominant Subspace + Residual

## Context

After v13.362 and v13.363, the global pole-free high-complement proof has only one unresolved inequality:

\[
\boxed{\|G\|<1},
\qquad
G=A_{0,[21,16001],[16003,\infty)}.
\]

The other two ingredients are now available:

\[
A_{0,[21,16001]}\succeq0.22I,
\]

and

\[
A_{0,[16003,\infty)}\succeq \alpha_{16003}I,
\qquad \alpha_{16003}>4.6732.
\]

Thus \(\|G\|<1\) would give

\[
A_0|_{\mathcal D}\succeq
\left(0.22-\frac{1}{4.6732}\right)I>0.006I.
\]

## Exact cross formula

With

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n,
\]

all pole-free off-diagonal entries satisfy

\[
G_{mn}
=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2}.
\]

Equivalently,

\[
G_{mn}
=-\frac1\pi\left[
\frac{Z_m-Z_n}{n-m}+\frac{Z_m+Z_n}{n+m}
\right].
\]

This makes separated rectangles Cauchy-like and rapidly low-rank, but the adjacent interface still contains substantial coherent mass.

## Why pure block-norm aggregation is insufficient

A dense test of the immediately adjacent \(2000\times2000\) corner gives midpoint singular values approximately

\[
0.85593,\ 0.69447,\ 0.44637,\ldots
\]

so the full \(\approx0.99284\) norm is not produced by one isolated corner mode.

A coarse \(4\times4\) partition of the near cross block \([21,16001]\times[16003,60003]\) gives the block-norm majorant

\[
\|[\|G_{ij}\|]\|_2\approx1.0549,
\]

and an \(8\times8\) refinement gives approximately

\[
1.0630.
\]

Thus the inequality

\[
\|G\|\le\|[\|G_{ij}\|]\|_2
\]

is too lossy: it destroys the inter-block coherence/cancellation responsible for the true norm staying below one.

## Correct certification architecture

The cross proof should preserve the dominant coherent singular subspace explicitly.

Let \(Q\) be an orthonormal basis for a numerically determined dominant left singular subspace of the finite-near plus low-rank-remote cross operator. Decompose

\[
GG^T
=
Q(Q^TGG^TQ)Q^T
+
\text{off-subspace residual}
+
(I-QQ^T)GG^T(I-QQ^T).
\]

A proof-grade certificate can then consist of:

1. a small projected Gram matrix
   \[
   K=Q^TGG^TQ,
   \]
   enclosed entrywise or by a residual-certified matrix product;
2. a residual bound
   \[
   \|(I-QQ^T)GG^TQ\|;
   \]
3. an upper bound on the orthogonal complement
   \[
   \|(I-QQ^T)G\|;
   \]
   obtained from the separated Cauchy expansion and/or Frobenius/Schur bounds after the leading coherent modes are removed;
4. the already available low-rank analytic representation of the remote \(n\ge60005\) tail.

Because the midpoint full cross norm is approximately

\[
\boxed{0.99284},
\]

only about \(7\times10^{-3}\) absolute norm margin is needed. Scalar-data enclosure errors are many orders of magnitude below this scale, so the challenge is spectral compression, not transcendental arithmetic.

## Computational note

A direct matrix-free high-accuracy SVD of the full near block is too expensive for the present interactive environment. This is not a mathematical obstruction; it simply confirms that the final checker should exploit the low-rank/displacement structure rather than brute-force repeated full cross matvecs.

## Current global status

Closed:

\[
\boxed{A_{0,[21,16001]}\succeq0.22I},
\]

\[
\boxed{\|B_{\rm prime}\|<2.05},
\]

\[
\boxed{\alpha_{16003}>4.6732}.
\]

Still open:

\[
\boxed{\|G\|<1}.
\]

Only after this cross bound is certified can we conclude positivity of the entire high complement and move to the exact 10-dimensional low-mode Schur complement for global inertia.

## Guardrail

The midpoint value \(\|G\|\approx0.99284\) is not itself a certificate. No global inertia, exact-zero, RH, or GRH claim follows from this checkpoint.
