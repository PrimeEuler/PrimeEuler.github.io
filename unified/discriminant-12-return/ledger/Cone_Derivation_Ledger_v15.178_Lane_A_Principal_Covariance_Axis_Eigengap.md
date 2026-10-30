# Cone Derivation Ledger v15.178 — Lane A principal covariance-axis stability under a certified eigengap

**Date:** 2026-10-30. **Track:** Lane A, chosen counting-measure ell2 only. **Parents:** v15.158/v15.162, audited v15.174/v15.175, v15.177. **Status:** [D] exact conditional eigendirection perturbation criterion; [O] numerical instantiation and canonical Suzuki synthesis.

**Collision check:** live master HEAD immediately before writing `abe4d82af219b740cef47aefddb0fadff442e56b` (v15.177). v15.178 next free. Additive only.

## Setup and strict acceptance inequality

Let `C_R` and `C` be the finite real symmetric covariance matrices of one **separately frozen** family `T_1,...,T_m`, evaluated on the transported cutoff and full vectors per v15.174/v15.177. Set

`delta = 12*E_Gamma(R,S)*sum_i nu_i²`

where `E_Gamma<1` is itself certified and every bound is outward rounded. From v15.177, `||C-C_R||_op <= delta`.

Suppose `C_R` has a **simple** selected eigenvalue `lambda_R` with an outward-certified gap
`g_R = min_{mu in spec(C_R),mu != lambda_R} |lambda_R-mu| > 0`.

Require the strict **gap gate** `2 delta < g_R`. Weyl ordering then guarantees a unique matched eigenvalue `lambda` of C, with `|lambda-lambda_R|<=delta`, that is isolated from the remaining eigenvalues. Let `v_R,v` be normalized real eigenvectors, identified only up to sign, for `lambda_R,lambda`. Then

`sin(angle(v,v_R)) = ||(I-v_R v_R^T)v|| <= delta/(g_R-delta)`.

Proof: write `E=C-C_R`, `Q=I-v_R v_R^T`, and project `Cv=lambda v` onto `Ran Q`: `Q(C_R-lambda)Q(Qv)=-QEv`. The restricted resolvent has norm at most `1/(g_R-|lambda-lambda_R|) <= 1/(g_R-delta)`; `||QEv||<=delta`. This yields the bound. The sign-optimized Euclidean eigenvector error obeys

`min_{s=±1}||v-s v_R|| <= sqrt(2)*delta/(g_R-delta)`

(since `2(1-|v^T v_R|) <=2(1-|v^T v_R|²)`). All quantities are finite covariance-coordinate-space results. The gate does **not** give an absolute physical axis or a gravitational orientation without a source-native observable family.

If `2delta >= g_R`, no stability promotion is allowed; the test is inconclusive, not evidence that the axes differ.

## Numerical acceptance package / handoff

**HANDOFF:** target External Audit and Sandbox; type principal-covariance-eigenvector-gap; parent v15.178; status OPEN_AUDIT / NUMERICAL_NOT_INSTANTIATED.

Audit: verify the strict gap condition, projected eigenvector identity, sine and sign-optimized distance constants; ensure no accidental identification of the chosen ell2 coefficient axes with physical modes.

Sandbox: for a **previously frozen** ordered observable family, provide v15.162 certified parity contour and rank, exact replay paths/hashes, outward `E_Gamma<1`, norms `nu_i`, `delta`, rigorous eigenvalue enclosures for `C_R`, rigorous positive `g_R`, strict `2delta<g_R` boolean, and the computed angle/eigenvector-error enclosures. If no such frozen numerical data exist, report NOT_INSTANTIATED rather than fit a family or contour.

## Fence

The canonical Suzuki source-indexed synthesis `Phi_a` remains absent in the examined source (v15.125); v14.405 two-sector compact-action certificate still missing. No v14.406 consumer, full residual, stationarity or capacity claim. C_S_32000, 3e-5, .002 and exactly-once transport charges unchanged.
