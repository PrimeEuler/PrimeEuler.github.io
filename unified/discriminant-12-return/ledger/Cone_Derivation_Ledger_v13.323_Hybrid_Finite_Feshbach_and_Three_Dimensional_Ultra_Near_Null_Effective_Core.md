# Cone Derivation Ledger v13.323

## Hybrid finite Feshbach and three-dimensional ultra-near-null effective core

This checkpoint continues v13.322.  The remote-tail analysis had isolated a fully protected active line, but the finite/stiff complement had not yet been eliminated consistently.  Here we eliminate the finite buffer first while retaining a high-precision low-core block.

Let

\[
\mathcal C=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\},
\qquad
\mathcal B_M=\operatorname{span}\{\psi_{21},\psi_{23},\ldots,\psi_M\}.
\]

For the finite principal block, define

\[
F_M=A_{CC}^{(hp)}-A_{CB}A_{BB}^{-1}A_{BC}.
\]

The Schur correction is assembled from the semi-analytic finite matrix of v13.316/v13.317, while \(A_{CC}^{(hp)}\) is reconstructed from the 60–70 digit low-core eigenbasis.  This is necessary because a fully double-precision assembly develops an artificial floor in the \(10^{-11}\)–\(10^{-12}\) range whose sign changes when the archimedean quadrature order is varied.

## Buffer remains numerically gapped

At \(M=399\),

\[
\lambda_{\min}(A_{BB})\approx 0.26725945796,
\qquad
\|\Delta_{399}\|_2\approx0.71241283923.
\]

Thus the finite buffer itself remains far from singular; the small scales arise in the low-dimensional Schur complement.

## Effective low-core spectrum

Using 1200-point Gauss–Legendre quadrature for the smooth archimedean matrix and a high-precision 10x10 core reconstruction, the first six eigenvalues of \(F_M\) are numerically:

| M | lambda1 | lambda2 | lambda3 | lambda4 | lambda5 | lambda6 |
|---:|---:|---:|---:|---:|---:|---:|
|101| -1.68e-20 | 3.26e-19 | 1.77e-17 | 1.72307e-12 | 4.45730e-8 | 2.68941e-4 |
|151| -1.05e-19 | 4.75e-19 | 1.38e-17 | 1.50754e-12 | 4.32796e-8 | 2.55219e-4 |
|201| -5.64e-20 | 4.61e-19 | 1.24e-17 | 1.46686e-12 | 4.28109e-8 | 2.49128e-4 |
|237| -5.74e-20 | 2.67e-20 | 1.47e-17 | 1.46110e-12 | 4.24764e-8 | 2.44858e-4 |
|301| -3.98e-20 | 5.09e-19 | 1.68e-17 | 1.45201e-12 | 4.19596e-8 | 2.39295e-4 |
|351| -4.86e-20 | 8.11e-19 | 1.36e-17 | 1.44543e-12 | 4.16416e-8 | 2.36391e-4 |
|399| -4.62e-19 | 2.94e-19 | 1.51e-17 | 1.43993e-12 | 4.13976e-8 | 2.34349e-4 |

The signs and exact values of the first three entries are **not certified**: they lie beneath the numerical reliability scale of the finite Schur assembly.  The correct interpretation is

\[
\boxed{\text{a three-dimensional ultra-near-null effective subspace}}
\]

followed by a fourth scale near \(1.4\times10^{-12}\), then scales near \(4.1\times10^{-8}\) and \(2.3\times10^{-4}\).

## Quadrature stability check

Changing the archimedean quadrature from 500 to 1200 nodes changes the raw fully assembled double-precision floor and can flip its sign, confirming that the naive full-matrix tiny eigenvalues are not trustworthy.  However, the hybrid Schur hierarchy above is stable in its resolved levels; at \(M=399\), for example,

\[
\lambda_4\approx1.440\times10^{-12},\quad
\lambda_5\approx4.140\times10^{-8},\quad
\lambda_6\approx2.3435\times10^{-4}.
\]

The three deeper directions remain below the trustworthy sign scale under both quadrature choices.

## Structural consequence

The finite buffer does not destroy the multiscale near-null core.  After exact finite elimination at the numerical level, the low-dimensional Schur complement becomes *more sharply stratified*:

\[
\boxed{
\text{3D ultra-near-null}
\oplus
10^{-12}
\oplus
10^{-8}
\oplus
10^{-4}
\oplus
\text{stiff directions}.
}
\]

This supersedes the earlier intuition that the fully protected line by itself was the final active object.  The remote-tail channel analysis remains valuable, but the correct next reduced problem is at least the three-dimensional ultra-near-null Schur subspace (and probably the first four effective directions until interval bounds separate the fourth scale).

## Guardrails

- This is a finite-section numerical Feshbach audit, not an interval-certified proof.
- Tiny signs at \(10^{-17}\) and below are unresolved and must not be interpreted as negative eigenvalues or exact zeros.
- No conclusion about \(\lambda_1=0\), RH, or GRH follows.
- The remote-tail certificate of v13.322 must be recomputed in the **effective Feshbach eigenbasis**; the earlier protected line was defined before finite complement elimination.

## Next target

Compute the first four effective eigenvectors of \(F_{399}\), project the exact prime/cusp/arch remote-tail channels onto that basis, and determine whether the three-dimensional ultra-near-null effective subspace inherits the same channel compression seen in v13.318–v13.322.  This is the correct order of operations: finite Feshbach first, remote-tail channel reduction second.
