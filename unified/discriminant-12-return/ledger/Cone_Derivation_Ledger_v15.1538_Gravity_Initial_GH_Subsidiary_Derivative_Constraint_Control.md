# Cone Derivation Ledger v15.1538 — Initial GH subsidiary velocity versus Einstein constraints: continuum control passes, native-grid constrained-data discrepancy

**Date:** 2026-11-26. **Lane:** Gravity/Cone. **Status:** actual local Python diagnostic and exact continuum derivation; canonical equivalent source committed, independent Audit pending. Parent v15.1537 unrestricted N32 evolution through T=.08. Starting live HEAD 912a0fa14afd7903659f3734c5e027ebb04306b4. No changes to Suzuki/Sandbox or earlier objects. N40 matched-time evolution was not performed this gate.

## Gate 1426: continuum identity

Write E_ab=G_ab-κT_ab, C^a=g^bc Γ^a_bc, C_a=g_ab C^b. For the undamped harmonic-reduced trace-reversed Einstein equations, E_ab=∇_(a C_b)-(1/2)g_ab∇_c C^c. On an initial unit-lapse zero-shift slice with C_a identically zero as a function of spatial coordinates, all spatial derivatives of C_a vanish and connection terms multiplying C vanish. Hence E_00=(1/2)∂t C_0, E_0i=(1/2)∂t C_i. With K_ij=-L_n γ_ij/2, Hamiltonian residual H=R^(3)+K²-K_ij K^ij-2κρ and momentum residual M_i=D_j K^j_i-D_i K-κj_i, the Gauss/Codazzi projections give E_00=H/2 and E_0i=-M_i. Thus **∂t C_0=H, ∂t C_i=-2M_i**. This initial identity is conditional on exact C=0 across the slice, not simply a small native-node max. On-shell matter conservation and contracted Bianchi give the usual subsidiary wave equation for C_a. No damping or numerical propagation theorem follows from the identity alone.

## Gate 1427: independently differentiate contracted GH vector

Actually executed /mnt/data/cone_gh/gate1538.py with local gh3d.py, single-thread BLAS. Form C^a as inverse-divergence contraction of g and first derivatives, then differentiate every factor analytically using g_t=p, (g^{-1})_t=-g^{-1} p g^{-1}, and the metric accelerations from unrestricted GH RHS. Lower the differentiated vector with ∂t C_a=g_ab∂t C^b+p_ab C^b. No temporal finite differences or independent resetting of constraints. Compare maximum norms with separate ADM monitor.

| N | max C | max H | max M | max |∂t C_0| | max |∂t C_i| |
|---:|---:|---:|---:|---:|---:|
| 16 | 9.7579348844e-12 | 4.2169427672e-6 | 2.0800234790e-9 | 1.0542400922e-6 | 4.4537714977e-9 |
| 24 | 8.6593808736e-13 | 1.1058912067e-8 | 9.7207733230e-12 | 2.7651084182e-9 | 3.0653331154e-11 |
| 32 | 1.0508199264e-14 | 1.5010531183e-10 | 2.9005505078e-14 | 3.7498157306e-11 | 1.2489457639e-13 |

Both initial subsidiary derivative norms decrease substantially with resolution, but the even-grid temporal max is approximately H/4, NOT H; spatial max also fails exact 2M equality. These comparisons are maxima, not pointwise residual identities. Odd grid exploratory runs N15,17,23,25,31,33 do not reproduce a universal quarter ratio (e.g. N17 H=2.55149e-11, temporal derivative=2.63463e-11; N33 H=3.46760e-13, temporal derivative=2.53181e-13). The mismatch is consistent with noncommuting discrete operations (possible Nyquist handling, nonlinear product aliasing, spatial derivatives of small nonzero C), but the cause is **not isolated**. Do not identify the numerical ratio with Cone quarter-grid physics.

Independent positive control: N17, smooth ψ=.005 cos x cos y, γ=e^(2ψ)δ, lapse 1, shift 0, K=0, sigma zero; initialize g_0i,t=-∂iψ, other velocities zero. Deliberately violate Hamiltonian while preserving initial harmonic condition. Exact conformal formula H=e^(-2ψ)(-4Δψ-2|∇ψ|²). Measured max C=1.50693e-15, H=0.039709029111449384, max ∂t C_0=0.03970902911145216, **pointwise max difference 7.11306e-14**, spatial derivative max zero, independent ADM H=0.039709029111455636, M=0. This rejects a universal quarter coefficient and validates the temporal continuum identity in a resolved smooth numerical control; it does not test nonzero momentum sign pointwise.

Canonical additive equivalent script research-notes/k4_gh_initial_subsidiary_derivative_v15_1538.py commit 741b7e86279d385dc39dc478128fa5733a981738 imports repaired v15.1485. It includes the three even-grid norm tests and smooth control; odd-grid diagnostics were local only. Exact committed bytes not executed this turn.

**Next/Audit:** independently replay and derive signs. Compare full pointwise E_ab projections computed from a single metric jet with ADM curvature evaluated using matched Hessians, isolate Nyquist conventions (first derivative of real even-grid Nyquist mode vs direct second derivative), nonlinear product differentiation and small spatial C derivatives. Then evaluate subsidiary residual □C_a+R_ab C^b on actual evolved data with controlled derivative errors. N40 T=.08 and matched temporal refinement remain open. No new physical coupling, G-free observable or full subsidiary propagation certificate claimed.
