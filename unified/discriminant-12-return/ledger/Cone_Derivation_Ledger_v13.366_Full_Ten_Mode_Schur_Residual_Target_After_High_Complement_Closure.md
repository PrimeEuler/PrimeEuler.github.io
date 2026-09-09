# Cone Derivation Ledger v13.366 — Full Ten-Mode Schur Residual Target After High-Complement Closure

## Starting point

v13.365 closes positivity of the entire even-sector high complement

\[
\mathcal D=\overline{\operatorname{span}}\{\psi_n:n\ge21,\ n\text{ odd}\}.
\]

A rounded lower bound is

\[
\gamma_D
=0.22-\frac{0.994^2}{4.6732}
>0.00857.
\]

Thus

\[
\boxed{\|A_{DD}^{-1}\|<116.7}.
\]

## Exact inertia reduction

Let

\[
\mathcal C_{10}=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\}.
\]

Because \(A_{DD}>0\), block Gaussian elimination gives exact inertia reduction to

\[
\boxed{
S_{10}=A_{CC}-A_{CD}A_{DD}^{-1}A_{DC}.
}
\]

Therefore every nonpositive direction of the full even operator lies in this ten-dimensional Schur complement.

## Residual-certified solve

For a point approximation \(X\) to

\[
X_*=A_{DD}^{-1}A_{DC},
\]

define

\[
R=A_{DC}-A_{DD}X.
\]

Then

\[
\|X_*-X\|\le\frac{\|R\|}{\gamma_D},
\]

and hence

\[
\|A_{CD}A_{DD}^{-1}A_{DC}-A_{CD}X\|
\le
\frac{\|A_{CD}\|}{\gamma_D}\|R\|.
\]

The earlier finite-buffer effective-core diagnostic placed the fifth ordered Schur eigenvalue near

\[
4.3\times10^{-8}.
\]

This remains targeting data only; the full \(S_{10}\) may shift.  Nevertheless it indicates that the final inertia certificate should aim for total Schur error below roughly

\[
10^{-8},
\]

preferably

\[
\boxed{3\times10^{-9}}.
\]

For \(\|A_{CD}\|\) of order one, this means a solve residual around

\[
10^{-11}\text{--}10^{-10},
\]

which is routine for high-precision structured arithmetic.

## Next target

1. Build the full low/high coupling \(A_{CD}\) using the exact Cauchy scalar sequence.
2. Solve the ten high-complement right-hand sides with the structured high-block machinery plus the certified infinite-tail correction.
3. Form \(\widehat S_{10}\).
4. Certify \(\|S_{10}-\widehat S_{10}\|<\eta\).
5. Prove the fifth ordered eigenvalue of \(S_{10}\) is positive, equivalently that the global nonpositive index is at most four.

## Guardrail

This is an exact reduction plus a certification target, not yet the final ten-mode inertia certificate.  No exact-zero, RH, or GRH claim follows.
