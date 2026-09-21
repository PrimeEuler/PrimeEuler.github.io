# Cone Derivation Ledger v13.627 — chi_-4 Friedrichs-Galerkin Zero-Branch A-Robustness Test

Date: 2026-09-21

Status: direct zero-branch sweep executed. The domain-faithful Galerkin repair does **not** remove the strong A-dependent box branch. Fail closed for arithmetic zero identification.

## 0. Live collision/relevance check

The live ledger was checked before construction and again immediately before this write. During execution the magnetic-driver lane advanced to v13.626, so v13.627 is the next free slot. Relevant chi_-4 chain: v13.620, v13.621, v13.623, v13.625. No intervening entry changes the frozen chi_-4 kernel or finite-lambda protocol.

## 1. Test

Compute zeros directly from the independently assembled Friedrichs-Galerkin characteristic, not from the discarded bare-Jz nodal carrier.

For A=1.5,2,2.5 refine both:
- Galerkin dimension N=8,12,16;
- assembly quadrature q=80,120,160.

Use the same finite-safe lambda as the preceding chi_-4 gates and theta convention used in the common comparison. Locate ordered positive real zeros of -i W(pi;z) by dense bracketing and Brent refinement.

## 2. Finest-grid roots

At N=16, q=160:

A=1.5:
2.095841362, 4.204075559, 6.088038478, 8.380862846, 10.310664530,
12.869069904, 14.716062888, 16.510443273, 18.467634684, 21.286283216

A=2.0:
1.571642107, 3.147948732, 4.754602038, 6.080064632, 7.883314203,
9.790948074, 10.592618666, 12.839393325, 13.942563279, 16.058574794

A=2.5:
1.256928889, 2.514818751, 3.780789053, 5.074154632, 6.069127325,
7.509693132, 8.802174066, 10.210673645, 11.334193556, 12.890925365

The first roots are therefore

[
r_1(1.5)=2.095841,quad r_1(2)=1.571642,quad r_1(2.5)=1.256929.
]

Multiplying by A gives approximately 3.143762, 3.143284, 3.142322: an extremely clear pi/A box scale.

## 3. Refinement

Maximum ordered-root shifts q=120 -> 160 at N=16:
- A=1.5: 5.13e-3
- A=2.0: 1.98e-2
- A=2.5: 6.11e-3

Maximum ordered-root shifts N=12 -> 16 at q=160:
- A=1.5: 4.29e-2
- A=2.0: 1.23e-1
- A=2.5: 4.37e-2

Thus the higher roots are not yet fully converged in N, especially at A=2, but the low branch and its cross-A scale are far too separated to be explained by these refinement errors.

For the first root, the cross-A range is 0.8389 (relative range about 0.511). The first ten ordered roots all retain cross-A relative ranges about 0.47–0.53.

## 4. Decision

The catastrophic A-dependent zero drift survives the domain-faithful repair:

[
oxed{	ext{Friedrichs-Galerkin characteristic zeros fail the A-robustness gate.}}
]

Indeed the first branch sharpens to

[
oxed{r_1(A)approx pi/A.}
]

Therefore the earlier box-like behavior was not solely an artifact of bare Jz quadrature nodes. v13.620 correctly rejected that carrier discretization, while v13.623/v13.625 repaired and certified the finite operator representation; nevertheless the current finite characteristic/finite-lambda construction itself still carries a box branch.

This is a negative audit result and must not be tuned away by selecting A.

## 5. Arithmetic comparison

The first Dirichlet-beta ordinate is about 6.0209489047. At each A there are multiple lower box roots, and the ordered finite roots move strongly with A. Therefore there is no A-independent indexing of these finite zeros by beta zeros in the tested construction.

No GRH consequence follows.

## 6. Reproducer

research-notes/suzuki_chi4_friedrichs_zero_branch_sweep.py

## 7. Guardrails / next question

1. The chi_-4 screw-function normalization remains frozen but not independently source-certified.
2. Lambda is finite-pair safe, not a certified continuous lambda below the spectral bottom.
3. The failure is for the present finite characteristic at fixed finite A; Suzuki's arithmetic statement involves the correctly normalized limiting construction, so finite box roots may require a renormalized/limit-aware comparison rather than direct ordered-root identification.
4. Next audit should identify analytically/numerically the origin of the pi/A branch: separate endpoint/free-box zeros from kernel-dependent zeros, inspect normalization/phase and lambda dependence, and determine what object should be tracked under A->infinity before any further beta-zero comparison.
