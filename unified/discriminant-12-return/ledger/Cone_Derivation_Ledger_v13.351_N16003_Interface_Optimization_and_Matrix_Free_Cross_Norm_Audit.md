# Cone Derivation Ledger v13.351

## N=16003 Interface Optimization and Matrix-Free Cross-Norm Audit

### Status
Numerical targeting / architecture audit only.  The values below are not yet interval-certified.

### Global inertia guardrail
A six-dimensional positive subspace of an infinite-dimensional operator does **not** imply nonpositive index <=4.  The correct global route remains:

1. split the even sector as the ten low modes plus the high complement
   \(D=\overline{\mathrm{span}}\{\psi_n:n\ge21,\ n\text{ odd}\}\);
2. certify the entire high complement positive;
3. use exact Schur-complement inertia to reduce the infinite operator to the ten-dimensional low core;
4. only then use a six-dimensional positive subspace of the ten-dimensional Schur core to conclude a nonpositive-index bound <=4.

No exact-zero, RH, or GRH conclusion follows.

## Unified pole-free Cauchy sequence
For the pole-free operator

\[
A_0=C_{\rm cusp}+B_{\rm prime}+K_{\rm arch},
\]

define

\[
Z_j=2A_j+\operatorname{Si}(j\pi)+2H_j.
\]

Then for \(m\ne n\),

\[
\boxed{
(A_0)_{mn}=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2}.
}
\]

This identity permits matrix-free application of the finite-to-tail cross block without constructing a dense matrix.

## N=10003 midpoint audit
For finite side \(21\le m\le10001\):

- tail \(10003\le n\le30003\):
  \[
  \|G\|_2\approx0.89074;
  \]
- tail \(10003\le n\le60003\):
  \[
  \|G\|_2\approx0.92771;
  \]
- separate remote band \(60005\le n\le120003\):
  \[
  \|G\|_2\approx0.22266.
  \]

The N=10003 interface remains plausible, but once the full remote tail is included its safe certification margin is narrower than initially hoped.

## N=16003 midpoint audit
Move the interface to

\[
F=\{21,23,\ldots,16001\},\qquad T=\{16003,16005,\ldots\}.
\]

A matrix-free power iteration on the exact Cauchy formula gives, for the truncated tail \(16003\le n\le60003\),

\[
\boxed{\|G_{16003:60003}\|_2\approx0.94323.}
\]

The robust tail coercivity model based on the rounded prime bound \(\|B_{\rm prime}\|<2.05\) gives

\[
\alpha_{16003}
\approx
\alpha_{10003}+\log(16003/10003)
\approx
\boxed{4.67326749}.
\]

If the finite high block is certified with the deliberately coarse target

\[
\boxed{A_{0,[21,16001]}\succeq0.225I},
\]

then the admissible full cross norm is

\[
\sqrt{0.225\,\alpha_{16003}}
\approx
\boxed{1.02542}.
\]

That is materially more forgiving than the roughly 0.97 admissible cross scale at N=10003.

## Next certification target
The remaining remote cross \(n\ge60005\) should be handled by the v13.349 low-rank expansion

\[
\frac1{n^2-m^2}
=
\frac1{n^2}\sum_{k\ge0}(m/n)^{2k},
\]

which yields rank-two terms at every order.  At the N=16003 interface and remote start 60005,

\[
\frac{16001}{60005}<0.267,
\]

so the geometric expansion is substantially better conditioned than at the earlier 6001/16005 split.

A practical rounded target is now

\[
\boxed{\|G_{[21,16001],[16003,\infty)}\|<1.00}.
\]

If this and the finite lower bound 0.225 are certified, then

\[
0.225-\frac{1^2}{4.67326749}>0.0110,
\]

which proves positivity of the full high complement with a small but clean margin.

### Interpretation
The interface optimization materially improves the global proof architecture.  The high-complement problem is no longer pinned to a marginal N=10003 split; moving to N=16003 gives a larger logarithmic tail gap while preserving a numerically manageable finite-to-tail cross norm.
