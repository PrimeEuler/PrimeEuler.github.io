# Cone Derivation Ledger v13.353

## Matrix-Free N=16001 Finite Gap and the 0.22 Global Target

### Status
Midpoint numerical audit plus updated certification target.  Final interval LDL/inertia proof remains pending.

## 1. Matrix-free finite high-block solve
For the pole-free operator

\[
A_0=C_{\rm cusp}+B_{\rm prime}+K_{\rm arch},
\]

on the finite high block

\[
F=\{21,23,\ldots,16001\},
\]

the dimension is 7991.

The off-diagonal action uses the exact unified sequence

\[
Z_n=2A_n+\operatorname{Si}(n\pi)+2H_n,
\]

with

\[
(A_0)_{mn}
=-\frac2\pi\frac{nZ_m-mZ_n}{n^2-m^2},\qquad m\ne n.
\]

The diagonal uses the exact cusp and prime formulas plus the degree-64 quadrature-free archimedean polynomial recurrence from v13.339.

A Lanczos solve through a matrix-free operator gives

\[
\boxed{\lambda_{\min}(A_{0,[21,16001]})\approx0.227114802018.}
\]

The final Ritz residual is

\[
\|A_0v-\lambda v\|_2\approx3.1\times10^{-8}.
\]

This confirms the earlier finite-gap extrapolation numerically but is not, by itself, a lower-bound certificate.

## 2. Updated proof target
The earlier working target

\[
A_{0,[21,16001]}\succeq0.225I
\]

is unnecessarily aggressive.  Replace it by

\[
\boxed{A_{0,[21,16001]}\succeq0.22I.}
\]

The midpoint slack is then

\[
0.227114802018-0.22
\approx
\boxed{7.11\times10^{-3}}.
\]

This is more than three times the slack available at the 0.225 target.

## 3. Compatibility with the N=16003 cross certificate
From v13.351-v13.352,

\[
\alpha_{16003}\approx4.67326749,
\]

and the full finite-to-tail cross midpoint norm is

\[
\|G\|\approx0.99284.
\]

Use the rounded certification target

\[
\boxed{\|G\|<1.00}.
\]

Then the full high-complement Schur lower bound becomes

\[
0.22-\frac{1^2}{4.67326749}
\approx
\boxed{6.02\times10^{-3}}>0.
\]

Thus the deliberately weakened finite target still proves positivity of the entire high complement once both finite and cross inequalities are certified.

## 4. Exact displacement structure remains the finite-proof mechanism
The shifted matrix

\[
A_{0,[21,16001]}-0.22I
\]

retains the exact displacement identity

\[
XA-AX=\frac2\pi(uv^T-vu^T),
\]

because subtracting a scalar multiple of the identity does not change the commutator with \(X=\operatorname{diag}(n^2)\).

The final positivity certificate should therefore use a verified structured LDL/inertia computation or a near/far admissible hierarchical factorization, not a dense 7991-dimensional interval eigensolver.

## 5. Current global theorem target
If the following three inequalities are certified:

\[
\boxed{A_{0,[21,16001]}\succeq0.22I},
\]

\[
\boxed{\|A_{0,[21,16001],[16003,\infty)}\|<1},
\]

\[
\boxed{A_{0,[16003,\infty)}\succeq4.673I},
\]

then

\[
\boxed{A_0|_{\mathcal D}>0}
\]

for the whole high complement \(\mathcal D\).  Since the pole term is PSD, adding it back preserves positivity.  Exact Schur-complement inertia then reduces the full infinite problem to the ten low modes.

### Guardrails
- The 0.227114802018 value is midpoint numerical data.
- The Ritz residual only certifies that a nearby eigenvalue exists; it does not exclude a lower eigenvalue.
- The final finite lower bound still requires verified inertia/LDL.
- No exact-zero, kernel, RH, or GRH claim follows.
