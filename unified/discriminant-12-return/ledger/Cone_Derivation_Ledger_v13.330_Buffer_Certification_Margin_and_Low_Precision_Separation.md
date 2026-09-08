# Cone Derivation Ledger v13.330 — Buffer Certification Margin and Low-Precision Separation

## Result

For the finite certification split at N=155,

\[
B=\{21,23,\ldots,153\}
\]

has dimension 67.

A fresh floating assembly using the exact cusp/prime formulas, smooth 1-D arch quadrature, and positive pole term gives representative values

\[
\lambda_{\min}(A_{BB})\approx0.27201476,
\]

\[
\lambda_2\approx0.72326416,\qquad
\lambda_3\approx0.76765720,
\]

and

\[
\lambda_{\max}\approx5.11993439.
\]

The 2-norm condition number is therefore only about

\[
\kappa_2(A_{BB})\approx18.82.
\]

The minimum diagonal of the ordinary Cholesky factor is about 0.74916.  These are numerical diagnostics, not interval certificates, but they show that the buffer is far from the delicate scale of the effective core.

## Perturbative interval target

If an interval assembly encloses every symmetric buffer entry with radius at most epsilon, then the perturbation matrix E satisfies the crude bound

\[
\|E\|_2\le67\epsilon.
\]

Using half of the observed spectral gap as a design margin gives

\[
\epsilon_{target}=\frac{0.27201476}{2\cdot67}
\approx2.03\times10^{-3}.
\]

Thus even a very coarse ~1e-3 entrywise rigorous enclosure should be enough to certify the 67x67 buffer positive.  This is a major scale separation: the buffer does not require anything resembling the 1e-17 precision demanded by the unresolved effective-core signs.

## Consequence

The finite certification task naturally splits into two precision regimes:

1. **coarse rigorous buffer certification** at roughly 1e-3 entry accuracy;
2. **extreme-precision 10x10 Schur certification** after the buffer has been eliminated.

This means a full 77x77 ultra-high-precision interval diagonalization is unnecessary and would obscure the actual structure.

## Next target

Derive rigorous entry enclosures for each component of A_BB at the 1e-4--1e-3 level, certify A_BB>0 perturbatively, and then propagate those enclosures through a verified linear solve to bound the 10x10 Schur correction.

## Guardrail

All spectral values in this checkpoint are ordinary floating diagnostics used only to set certification tolerances.  No positivity theorem for the full operator, exact zero mode, lambda_1=0, RH, or GRH conclusion is made.