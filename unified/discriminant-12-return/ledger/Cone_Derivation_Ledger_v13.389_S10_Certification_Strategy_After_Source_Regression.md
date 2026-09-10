# Cone Derivation Ledger v13.389 — S10 Certification Strategy After Source Regression

Date: 2026-09-10

Status labels: **[D]** exact derived, **[N]** numerical, **[N-cert]** validated computational, **[O]** open, **[Audit]** limitation/correction.

## 1. Context

v13.387 resolved External Audit Round 20's overlap mistake and restored the source-faithful rank-two archimedean formula. v13.388 then reproduced the historical finite-section `S10` pattern: four numerical-zero-scale directions, a fifth small positive direction near `4e-8`, and a sixth positive direction near `2e-4`.

The present checkpoint asks which route can realistically certify the exact infinite ten-mode Schur complement

\[
S_{10}=A_{CC}-A_{CD}A_{DD}^{-1}A_{DC},
\qquad C=\{1,3,\ldots,19\},\quad D=\{21,23,\ldots\}.
\]

## 2. A crude finite-cutoff tail bound is too weak

The existing exact fixed-core prime-tail estimate gives

\[
\|P_TB_{\rm prime}P_C\|\le \|\cdot\|_{HS}
\]

with

\[
\|P_TB_{\rm prime}P_C\|_{HS}
\le
\left[
\sum_{m\in C}
\left(\frac{4C_m/\pi}{1-(m/N)^2}\right)^2
S_2(N)
\right]^{1/2}.
\]

At the established interface `N=16003`, direct evaluation of this analytic formula gives

\[
\boxed{\|P_TB_{\rm prime}P_C\|_{HS}<0.10881.}
\]

This is already many orders of magnitude larger than the observed fifth finite-Schur eigenvalue (`~4e-8`). Adding cusp, archimedean and pole tail bounds cannot improve this basic scale mismatch.

**[Audit/strategy]** Therefore a uniform operator-norm estimate for
`S10 - S10^(M)` is not a sensible route to certifying the fifth direction. A finite-section convergence plot is useful as a regression diagnostic but cannot carry the proof.

## 3. Required route: residual-certified infinite solve

Because the high complement `A_DD` is positive under the source-faithful v13.362/v13.365 validated-computational chain, compute ten high-precision approximate solution columns

\[
X\approx A_{DD}^{-1}A_{DC}.
\]

For the residual

\[
R=A_{DC}-A_{DD}X,
\]

positivity gives

\[
\|X_*-X\|\le \|A_{DD}^{-1}\|\,\|R\|.
\]

Hence

\[
\|A_{CD}A_{DD}^{-1}A_{DC}-A_{CD}X\|
\le
\|A_{CD}\|\,\|A_{DD}^{-1}\|\,\|R\|.
\]

This is the correct certification object: the residual of the **full high-complement equation**, not the difference between successive finite Schur complements.

## 4. Numerical target

Using the source-faithful high-complement lower margin from the pre-audit chain,

\[
\gamma_D>0.22-0.994^2/4.6732\approx8.57\times10^{-3},
\]

so

\[
\|A_{DD}^{-1}\|<116.7.
\]

To resolve an `S10` eigenvalue of order `4e-8`, a practical total Schur-matrix error target remains

\[
\boxed{\eta_{S10}<3\times10^{-9}}.
\]

For a certified coupling norm `Cnorm=||A_CD||` of order one this asks for solve residuals at roughly the `1e-11` scale, compatible with the existing high-precision structured machinery.

## 5. Diagnostic extrapolation only

The source-faithful fifth finite-section values

\[
4.47,4.29,4.14,4.05,4.00\times10^{-8}
\]

at cutoffs `99,199,399,599,799` show slow downward drift. Simple non-rigorous fits place a possible limiting scale around `3.6e-8` to `4.0e-8`, but **no extrapolation is used as proof**.

## 6. Next implementation target

Build a source-faithful rank-two structured solver that returns:

1. the ten approximate high-complement columns;
2. a certified `||A_CD||` bound;
3. a full-equation residual enclosure for each column;
4. the resulting ten-dimensional Schur matrix with a total operator error below `3e-9`;
5. an interval/Weyl inertia statement only if the fifth and sixth directions remain separated from zero after that error is charged.

## 7. Guardrail

The four numerical-zero-scale directions are not exact kernels. The positive fifth finite-section eigenvalue is not yet an infinite-dimensional theorem. No RH, GRH, exact-zero, or final inertia claim follows from this checkpoint.
