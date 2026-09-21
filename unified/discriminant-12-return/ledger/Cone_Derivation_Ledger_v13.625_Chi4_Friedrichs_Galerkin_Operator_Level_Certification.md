# Cone Derivation Ledger v13.625 — chi_-4 Friedrichs Galerkin Operator-Level Certification

Date: 2026-09-21

Status: operator-level quadrature refinement executed. Frozen-kernel Galerkin operator/spectrum passes; inverse/resolvent convergence is visible but slower because the first-kind systems remain ill-conditioned.

## 0. Live collision/relevance check

The live ledger was fetched before construction and again immediately before this write. It advanced through v13.624, a weighted-path/tetrahedral entry that does not alter the chi_-4 lane. The relevant chain remains v13.614–v13.616 and v13.620–v13.623. v13.625 is free.

## 1. Gate

For A=1.5,2,2.5 and N=8,12,16, independently assemble the endpoint-adapted even/odd Galerkin operator at tensor Gauss-Legendre orders q=40,60,80,120,160. Use q=160 as the refinement reference.

Track:
- augmented first-kind condition numbers and smallest singular values;
- relative Frobenius operator-block changes;
- relative 2-norm changes of inverse augmented systems;
- relative changes of eigenvalues of symmetrized parity operator blocks.

The finite lambda is the same common j=10 finite-pair value used in v13.621–v13.623.

## 2. N=16 conditioning

At q=160:
- A=1.5: cond(e,o)=(6.930e4,4.005e3), smin=(2.981e-5,5.015e-4)
- A=2.0: cond(e,o)=(4.229e4,7.188e3), smin=(6.309e-5,6.031e-4)
- A=2.5: cond(e,o)=(5.069e4,9.408e3), smin=(6.486e-5,8.888e-4)

Thus no finite system is singular, but the first-kind even sector is substantially ill-conditioned.

## 3. q=120 -> 160 refinement

Worst discrepancies over every tested A and N:
- even operator relative Frobenius change: 6.879e-4
- odd operator relative Frobenius change: 3.032e-4
- even symmetrized-spectrum relative change: 2.847e-4
- odd symmetrized-spectrum relative change: 9.013e-5
- even inverse/resolvent relative change: 1.954e-2
- odd inverse/resolvent relative change: 2.343e-2

At N=16 specifically, q=40 -> 60 -> 80 -> 120 -> 160 gives systematic reduction in operator and spectral discrepancies for all three A values. Example A=2.5:
- operator even: 1.175e-2, 4.957e-3, 2.522e-3, 6.879e-4, 0
- operator odd: 4.940e-3, 2.107e-3, 1.062e-3, 3.032e-4, 0
- spectrum even: 4.742e-3, 1.914e-3, 9.320e-4, 2.847e-4, 0
- spectrum odd: 1.428e-3, 5.332e-4, 2.928e-4, 8.061e-5, 0
- inverse even: 1.792e-1, 1.136e-1, 5.127e-2, 1.689e-2, 0
- inverse odd: 2.584e-1, 1.368e-1, 7.693e-2, 2.343e-2, 0

## 4. Decision

The frozen-kernel operator-level gate passes with a conditioning caveat.

The operator blocks and their finite spectra are stable under independent quadrature refinement at sub-1e-3 scale by q=120 relative to q=160. The augmented inverse/resolvent is necessarily more sensitive and is only at roughly 2 percent refinement agreement in the worst q=120 -> 160 case. Crucially, that inverse discrepancy decreases systematically with quadrature order rather than plateauing or diverging.

Therefore the positive characteristic convergence in v13.623 is not hiding an operator assembly instability.

Promoted numerical statement:

\[
\boxed{\text{the domain-faithful chi}_{-4}\text{ Galerkin operator is quadrature-stable at the tested finite }N,}
\]

with the explicit qualification

\[
\boxed{\text{first-kind inverse/resolvent convergence is slower and remains the main conditioning sensitivity.}}
\]

This is numerical certification of the frozen finite construction, not a proof of continuous operator-norm/resolvent convergence.

## 5. Reproducer

Added:
`research-notes/suzuki_chi4_friedrichs_operator_certification.py`

## 6. Next gate

The discretization lane is now strong enough to resume a characteristic zero/A-robustness experiment using the independently solved Friedrichs Galerkin construction rather than bare Jz nodes. Before interpreting arithmetic zero agreement, the standing chi_-4 source-normalization caveat should still be kept explicit or independently re-derived.
