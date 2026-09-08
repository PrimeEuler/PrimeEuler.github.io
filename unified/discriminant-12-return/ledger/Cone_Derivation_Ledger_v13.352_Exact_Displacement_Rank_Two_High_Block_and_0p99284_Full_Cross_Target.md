# Cone Derivation Ledger v13.352

## Exact Displacement-Rank-Two High Block and the 0.99284 Full-Cross Target

### Status
Exact algebraic structure plus midpoint numerical targeting.  The final interval certificates are still pending.

## 1. Correct global route
The even sector is split as

\[
\mathcal H_{\rm even}=\mathcal C_{10}\oplus\mathcal D,
\]

where \(\mathcal C_{10}\) contains odd modes \(1,3,\ldots,19\) and

\[
\mathcal D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\text{ odd}\}.
\]

The global inertia reduction is valid only after certifying \(A|_{\mathcal D}>0\).

## 2. N=16003 cross audit closes numerically
At the working split

\[
F=\{21,23,\ldots,16001\},\qquad T=\{16003,16005,\ldots\},
\]

the exact pole-free off-diagonal formula is controlled by

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n.
\]

A direct matrix-free midpoint power iteration gives

\[
\|G_{16003:60003}\|_2\approx0.94323.
\]

The remote block \(n\ge60005\) is represented by the rank-two-per-order Cauchy expansion.  A rank-12 truncation gives

\[
\|G_{\rm far}\|_2\approx0.39904,
\]

with a very small geometric truncation remainder.

Using the **actual combined Gram operator** rather than the worst-case square-sum estimate gives

\[
\boxed{\|G_{[21,16001],[16003,\infty)}\|_2\approx0.99284.}
\]

Thus the rounded certification target

\[
\boxed{\|G\|<1.00}
\]

is numerically realistic.

With the robust tail gap

\[
\alpha_{16003}\approx4.67326749
\]

and the deliberately coarse finite-block target

\[
A_{0,[21,16001]}\succeq0.225I,
\]

the resulting high-complement margin would be

\[
0.225-\frac{1}{4.67326749}
\approx
\boxed{0.01102}>0.
\]

So the cross side is no longer the dominant obstacle.

## 3. Exact displacement-rank-two structure
For \(m\ne n\),

\[
(A_0)_{mn}
=-\frac{2}{\pi}\frac{nZ_m-mZ_n}{n^2-m^2}.
\]

Let

\[
X=\operatorname{diag}(n^2),\qquad u=(Z_n),\qquad v=(n).
\]

Then

\[
(XA_0-A_0X)_{mn}
=(m^2-n^2)(A_0)_{mn}
=\frac{2}{\pi}(Z_m n-m Z_n).
\]

The diagonal of the commutator is zero, so the full finite matrix satisfies

\[
\boxed{
XA_0-A_0X
=\frac{2}{\pi}(uv^T-vu^T).
}
\]

Hence the finite high block is an **exact Cauchy-like matrix of displacement rank at most two**.

## 4. Consequence for the finite positivity certificate
The finite block has dimension

\[
\frac{16001-21}{2}+1=7991.
\]

A dense interval Cholesky is therefore undesirable, but the displacement structure makes it unnecessary.

For separated index blocks,

\[
\frac1{n^2-m^2}
=
\frac1{n^2}\sum_{k\ge0}\left(\frac mn\right)^{2k},
\]

so every separated off-diagonal block has rank at most two per retained order, with an explicit geometric remainder.

This supports a recursive/HODLR certification architecture:

1. partition \(21,\ldots,16001\) dyadically;
2. certify small dense diagonal leaves directly;
3. represent separated interactions by low-rank Cauchy factors;
4. propagate Schur complements through verified low-rank updates;
5. prove the final lower bound \(A_{0,[21,16001]}\succeq0.225I\).

The same low-rank formulas can be reused for both the finite high-block LDL certificate and the infinite cross certificate.

## 5. Current bottleneck
The global route has now narrowed to one concrete certification problem:

\[
\boxed{A_{0,[21,16001]}\succeq0.225I.}
\]

The midpoint spectrum through smaller cutoffs strongly suggests a limiting gap near \(0.227\), so this target leaves roughly \(2\times10^{-3}\) of finite-block slack.  It remains numerical targeting until the hierarchical interval LDL is instantiated.

### Guardrails
- v13.347's six-dimensional infinite positive-subspace argument was not sufficient for a global index bound and remains superseded by the corrected v13.348+ route.
- The 0.99284 full-cross value is numerical midpoint data, not an interval certificate.
- The displacement-rank-two identity is exact algebra.
- No exact-zero, kernel, RH, or GRH conclusion follows.
