# Cone Derivation Ledger v15.1463 — 2× spectral oversampling removes the nonlinear conformal Ricci alias floor before Einstein–H² evolution

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Status:** [ACTUALLY EXECUTED NUMERICAL PASS] evaluate the same full 3+1-spatial Christoffel–Ricci scalar using the identical bandlimited conformal initial metric but with nonlinear tensor products reconstructed on a 2× finer Fourier grid. At original grid nodes its disagreement with the *independent exact conformal scalar curvature identity* falls from 10^-6–10^-8 to 10^-13–10^-14. [NEGATIVE] 3× oversampling does not further improve the tested comparison because roundoff dominates; oversampling of a diagnostic Ricci calculation does **not** by itself certify the nonlinear ADM time evolution, dealiased Einstein constraints, longer-time stability, or any physically valid extra Weyl coupling. **Independent Audit:** Round 648 (v15.1461, commit 35d0af8660ee66f07d05816bbc0353ae25751b25) confirmed previous Gravity v15.1459–1460. **Sandbox:** v15.1462 G-trace independently found no new G-free selector in its density/acceleration network. All previous audited and Lane A objects untouched; this entry follows Sandbox v15.1462 without version collision.

## Gate 1387 — isolate geometry aliasing without time integration

Take the *same real H² sigma initial fields* and their leading elliptic conformal potential ψ from v15.1460. Define the mathematical reference for the spatial metric γ_ij=e^(2ψ)δ_ij by the exact 3D identity

`R_reference=e^(−2ψ)[−4Δψ−2|grad ψ|²]`.

At original N³ sampling resolution, independently form every 3D Christoffel symbol from FFT derivatives of γ, every derivative and quadratic product in the full Ricci tensor, then contract with γ^ij. That was the v15.1460 diagnostic and is sensitive to aliasing of the nonlinear exponentials and tensor products.

For each N=12,16,24, use **periodic Fourier interpolation** (SciPy resample on x,y,z in turn) to evaluate the *same bandlimited ψ* on a 2N×2N×2N internal grid. Recompute γ, all spatial derivatives, 27 Christoffels, their derivatives, full Ricci and scalar contraction **on the finer grid**. Restrict the final Ricci scalar to the original grid points by taking every second sample; compare with the original exact closed conformal reference. This is an oversampled nonlinear pseudospectral diagnostic, not a claim that every nonlinear product has compact Fourier bandwidth.

**Independently actually executed local tests:** (1) `/mnt/data/cone_gate/k4_oversampled_ricci_v15_1463.py`, containing the original 1×, 2× and 3× comparisons; (2) `/mnt/data/cone_gate/k4_oversampled_ricci_reproducer_v15_1463.py`, whose 1×/2× calculation is separately derived by transforming the audited v15.1460 baseline. Both programs PASS. **Additive GitHub canonical reproducible source:** `research-notes/k4_oversampled_full_ricci_v15_1463.py`, commit **e880575da5930ca7322b8ab6b8634b7b66ad5633**, constructed from the original audited v15.1460 GitHub source and new 2× oversampling operation; exact committed-byte independent Audit replay pending.

| original N³ | native max |R_full−R_reference| | 2×-oversampled max difference | 3×-oversampled (independent local) |
| ---: | ---:| ---:| ---:|
| 12³ | 3.0960006706e−7 | 3.7994252e−14 | 1.1185838e−13 |
| 16³ | 4.2170121349e−6 | 1.0422736e−13 | 2.6461366e−13 |
| 24³ | 1.1061443545e−8 | 2.6073669e−13 | 1.0450711e−12 |

The independent v15.1460 native calculations reproduce the earlier aliasing floor. This result improves the 16³ nonlinear Ricci diagnostic by ~4×10^7, but **NOT the previous N16 nonlinear Einstein momentum initial-data constraint error**: that was a separate aliased source solve, and merely oversampling Ricci does not cure the original momentum constraint. The oversampled result is an accurate **geometrical curvature evaluation at the original sample nodes**, not an assertion of the complete 16³ Einstein evolution satisfying both constraints. At a very small potential |ψ|~4e−6, larger 3× internal grids can accumulate more floating-point roundoff; requiring monotonic improvement beyond the roundoff floor is unjustified.

## Scope, audit and next gate

**AUDIT:** execute exact committed v15.1463 script and reproduce native and 2× results; independently check periodic Fourier resample normalization, point-node alignment, the metric inverse and Christoffel indexing, whether regridding psi at Nyquist is real/consistent, and monitor the 3× roundoff non-improvement from the local expanded test. Distinguish the leading Poisson ψ used for the geometry diagnostic from full nonlinear v15.1453 conformal initial-data solution. The 2× interpolation does not change physical initial data.

**NEXT:** implement and benchmark oversampled **entire ADM right-hand-side evaluations** (all Γ/curvature/matter products and nonlinear constraints), preferably with consistently projected nonlinear Fourier modes and an independent residual check on a high-resolution reference grid. Compare RK4 N24/N32 and N40 short-time stability, including **longer** T=.04 runs, against the previous native results, before upgrading to a strongly hyperbolic BSSN/Z4/generalized-harmonic formulation. Do not mistake fixed-lapse raw ADM for a generally well-posed long-time evolution. The complete Weyl–F–H² action remains higher-derivative and requires metric stress/EFT order reduction; quarter-grid Q=1/16, 3:1 null-affine geometry and historical ψ_D=45.310 still do not select κ=8πG or the freely chosen Weyl coupling. No G-free new observable claimed.
