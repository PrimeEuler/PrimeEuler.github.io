# Cone Derivation Ledger v13.379

## Corrected rank-4 remote cross completion and robust `<0.995` target

This checkpoint continues the Audit-Rounds-20/21 repair.  The old single-
`Z_n` cross formula is superseded.  The intended pole-free off-diagonal matrix
is

\[
G_{mn}=\frac{2}{\pi}\frac{nU_m-mU_n}{m^2-n^2}
+\pi mn\frac{Y_n-Y_m}{m^2-n^2},
\]

with

\[
U_n=\operatorname{Si}(n\pi)+2A_n,\qquad Y_n=nH_n.
\]

Use the exact centered gauge from v13.377,

\[
\widetilde Y_n=Y_n-c_\infty,
\qquad
c_\infty=\frac{2}{\pi}\frac{e^{-1}}{1-e^{-4}},
\]

so that the matrix is unchanged and \(\widetilde Y_n=O(n^{-2})\).

For \(m\le16001<n\), the geometric Cauchy expansion gives four separated
channels per order `k`:

\[
-\frac2\pi m^{2k}U_m\,n^{-(2k+1)},
\]

\[
+\frac2\pi m^{2k+1}\,U_n n^{-(2k+2)},
\]

\[
+\pi m^{2k+1}\widetilde Y_m\,n^{-(2k+1)},
\]

\[
-\pi m^{2k+1}\,\widetilde Y_n n^{-(2k+1)}.
\]

A fresh midpoint reconstruction on the corrected operator gives:

- direct near band `16003..60003`: top norm about `0.94349`;
- rank-32 (`K=8`) remote `60005..2,000,005`: standalone norm about `0.3926813`;
- coherent near+remote norm about `0.99113`;
- after analytic completion of the pure inverse-power Gram tails beyond
  `2,000,005`, the coherent midpoint norm is

\[
\boxed{0.9927951\ \text{(midpoint)}}.
\]

The remaining `U_n`-containing tail beyond `2,000,005` has the deliberately
coarse Hilbert-Schmidt bound

\[
\boxed{\|R_U\|<5.64\times10^{-4}},
\]

using only

\[
|U_n|
\le\frac\pi2+\frac1{n\pi}
+2\sum_{q\in\{2,3,4,5,7\}}\frac{\Lambda(q)}{\sqrt q}
<7.424.
\]

At the remote split,

\[
\rho=16001/60005<0.267.
\]

The `k>=8` geometric remainder of the cusp+prime channel is below about
`3.7e-10` in Hilbert-Schmidt norm.  The centered arch variable tail is of still
higher order; the coarse decay target

\[
|\widetilde Y_n|\le 10/n^2
\]

would make its final remote contribution below `1.5e-9`.  That decay constant
is not yet promoted here; it is the next analytic certification target.

Therefore the repaired cross geometry supports the robust rounded target

\[
\boxed{
\|A_{0,[21,16001],[16003,\infty)}\|<0.995.
}
\]

The current midpoint+analytic-tail budget is below approximately `0.99336`, so
the target leaves roughly `1.6e-3` for outward arithmetic, finite Gram
enclosures, and the final certified centered-arch decay estimate.

## Status

This checkpoint is **targeting evidence plus analytic tail reduction**, not the
final cross theorem.  It does not restore v13.365.  The remaining proof-grade
items are:

1. outward certify the centered-arch decay bound;
2. outward certify the finite projected/Gram arithmetic;
3. close the corrected finite high-block LDL residual transcript;
4. rederive/certify the corrected tail coercivity constant;
5. only then apply the high-complement Schur argument.

The separate prime-operator bound `||B_prime||<2.05` remains unaffected by the
audit.  No exact-zero, RH, or GRH conclusion follows.
