# Cone Derivation Ledger v15.1455 — Linear ADM Hamiltonian/momentum constraint propagation is a unit-speed wave system

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Status:** [EXACT D] standard vacuum linearized ADM Hamiltonian/momentum constraint propagation equations close as a symmetric hyperbolic system for constraint violations around Minkowski in unit lapse and zero shift; [N PASS] exact Fourier propagation with conserved constraint norm for three grid resolutions; [STRICT LIMIT] this is the *linear vacuum* propagation law, not the nonlinear Einstein–H² constraint propagation of v15.1453 and not a complete BSSN/gauge stability test; [OPEN] actual nonlinear 3+1 metric evolution and matter Bianchi closure, full Weyl EFT metric variation and physical q2 selector. Additive, preserves audited archive.

## Gate 1379 — derive constraint propagation from contracted Bianchi identity

Linearize ADM about Minkowski with α=1 and β^i=0. Define `H=∂i∂j h_ij−Δ tr(h)` and `M_i=∂j(k_ij−δij tr(k))`, with k_ij=−(1/2)∂t h_ij. The vacuum first-order linearized ADM evolution is `∂t h_ij=−2k_ij`, `∂t k_ij=R_ij[h]` (at leading order). The linearized spatial Ricci obeys `∂j R_ij=(1/2)∂i R`. Consequently,

`∂t H=−2∂i M_i`,
`∂t M_i=−(1/2)∂i H`.

For all smooth solutions, `∂t² H=ΔH` and the longitudinal momentum constraint also propagates by a unit-speed wave. The transverse part of M_i is constant in time at this linear order. Therefore if H=M_i=0 initially and the evolution solves these equations, the constraints remain zero. For nonzero initial violations, the quadratic integral `N=∫(H²+4 M_i M_i)d³x` is conserved on a flat periodic box; this can be verified by integration by parts:

`dN/dt=−4∫[H ∂i M_i+M_i ∂i H]dx=0`.

This is a standard ADM constraint propagation result, not a discovery of a new independent Cone/gravity degree of freedom.

## Gate 1380 — Fourier evolution and numerical controls

Choose N×N×N periodic x,y,z∈[0,2π), initial violation `H0=.01[sin(x+2y)+.3 cos(2x−z)]` and `M_i(0)=0`. Every Fourier mode evolves exactly as

`Hhat_k(t)=Hhat_k(0) cos(|k|t)` and `Mhat_i(k,t)=−(i/2)k_i Hhat_k(0) sin(|k|t)/|k|`, with continuous zero-k convention. The test at t=4 computes H,M via independent FFT inversion, checks both propagation equations spectrally and the conservation of N relative to N0:

| N³ | H RMS at t=4 | |M| RMS at t=4 | max propagation residual | relative N drift |
|---:|---:|---:|---:|---:|
| 16³ | .0065464355574 | .0017061785874 | 2.60e−17 | 2.22e−16 |
| 24³ | .0065464355574 | .0017061785874 | 5.20e−17 | 4.44e−16 |
| 32³ | .0065464355574 | .0017061785874 | 4.25e−17 | 2.22e−16 |

All these checks PASS and the stable norm is derived from the differential equations rather than chosen to fit the output. The Fourier reconstruction is analytically exact for the chosen low-frequency modes, so the tiny residuals mainly verify implemented algebra/FFT conventions; they are NOT a continuum error certification of nonlinear Einstein evolution.

Actual local script `/mnt/data/cone_gate/adm_linear_constraint_propagation_v15_1455.py` executed, and equivalent additive GitHub `research-notes/k4_adm_linear_constraint_propagation_v15_1455.py` SHA **5797208e3624766d1cd13ebf70bdde53ada69308** committed. Independent committed-byte Audit replay pending.

**AUDIT:** independently derive ∂tH and ∂tM_i from linearized ADM and Ricci Bianchi identities, verify overall signs and factor 2, Fourier source and 4 factor in N, note transverse momentum zero modes, and ensure no inhomogeneous nonlinear matter propagation is claimed.

**NEXT:** take the separately coupled Einstein homogeneous FLRW system from v15.1454 and evolve its Raychaudhuri equation **without imposing the Friedmann constraint algebraically at every time**; monitor whether the Friedmann residual propagates under full independent dynamics. After that, advance a gauge-fixed inhomogeneous BSSN or generalized-harmonic Einstein–H² evolution of the fully constrained initial data v15.1453, and require 3+1 Hamiltonian/momentum constraint monitoring plus the full interaction stress. No prediction of G from q2 geometry has been obtained.
