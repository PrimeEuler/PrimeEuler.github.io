# Cone Derivation Ledger v13.514 — M16001 Structured-Solve Residual Transcript

Date: 2026-09-16

Status: **[N-cert arithmetic] / [Audit]**. Source uncertainty remains separately handled by the shifted-nominal enclosure; no inertia promotion in this entry.

## 0. Synchronization

Live head checked at start and immediately before write. Parallel arithmetic work advanced the numbered ledger to v13.513. v13.514 was free.

## 1. Source-faithful residual action

New helper:

`research-notes/suzuki_M16001_structured_solve_residual_transcript.py`

commit `2909a58d3880a6d2c237df5d1453385929c72f07`.

For the 7991-dimensional finite-high block, it reconstructs

\[
R_F=A_{FF}X-A_{FC}
\]

rowwise from the canonical displacement off-block formula, exact stored diagonal payload, and full even PSD rank-one pole. No dense 7991x7991 matrix is stored.

Every 7991-term reduction is charged by

\[
\gamma_{7991}\sum_j |a_{ij}x_{jr}|,
\qquad
\gamma_{7991}=4.3319297801658348\times10^{-16},
\]

with separate gamma charges for `c_F^T X`, pole multiplication/addition, and final RHS subtraction.

## 2. Replayed arithmetic transcript

Independent execution of the same source-faithful formulas gives

- `max sum_j |A0_ij X_jr| = 1.1209247268485288`;
- maximum 7991-term dot-product gamma charge
  `4.855767205559396e-16`;
- maximum point residual entry
  `4.2394473348528194e-15`;
- point Frobenius residual
  `7.802341177110749e-15`.

After adding the computed reduction/pole/subtraction gamma charges entrywise and then taking the Frobenius norm,

\[
\boxed{\|R_F\|_2\le\|R_F\|_F<9.55035036608530\times10^{-15}}.
\]

This radius is derived from the operation transcript; it is not an empirical double/long-double discrepancy and has no post-hoc safety multiplier.

## 3. Scope guardrail

The residual bound certifies arithmetic consistency of the structured finite solve against the nominal source-faithful M16001 matrix payload. Exact-vs-nominal source uncertainty remains separate and is handled by the established shifted-operator construction. This entry does not yet propagate the new residual radius through the Q/N, remote-Gram, and far-tail transcript to a final seven-plane endpoint.

Certified theorem therefore remains

\[
\boxed{\operatorname{ind}_{\le0}(A_{\rm even}(1))\le4}.
\]

Next: feed this derived `9.55035036608530e-15` residual enclosure together with the transcripted finite projection, remote Gram, and far moments into one fail-closed final seven-plane perturbation propagation.