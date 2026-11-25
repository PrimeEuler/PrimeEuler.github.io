# Cone Derivation Ledger v15.1416 — First actual curved H² coupled Maxwell/sigma variational energy exchange in a frozen tidal-component reduction

**Date:** 2026-11-24 Eastern / GitHub UTC Nov 25. **Track:** Gravity/Cone. **Status:** [N PASS, actual nonlinear H² target] Maxwell and **both curved-hyperboloid sigma fields** evolved self-consistently from one real 1+1D Hamiltonian with a retained frozen curvature–F–area interaction component; [N PASS] conserved total canonical Hamiltonian to ≲1.8×10⁻9 relative, actual sourced photon-like A_z field with initially zero A and A_t, nonzero sigma and interaction energy changes, positive kinetic matrix in tested runs, N16/24 and g-halving/zero controls; [NEGATIVE] not the full Lorentz-covariant Weyl–F–H² operator or Einstein–K4 evolving metric, no physical photon count, no full stress/Bianchi Ward test and no G-free quarter coupling; [OPEN] full EFT principal symbol, gauge-consistent tensor truncation, complete metric variation and independent physical carrier. **Preledger verified script SHA** 771ac871fb9d912ff67f81d43052ed52a2f40730. Strict additive; protects all earlier certified work and Audit assets.

## Gate 1356 — write and Legendre-transform the nonlinear curved target local action

Take actual positive-sheet H² normalized coordinates `phi=(u,v)`. The exact target metric is `G_ab=δ_ab−phi_a phi_b/(1+u²+v²)` and its oriented target area `Ω_uv=1/sqrt(1+u²+v²)`. Let A=A_z(t,x), the transverse Maxwell potential in a 1+1D dimensional reduction of a theory with an additional dormant spatial z direction. Choose a fixed constant *one-component tidal coefficient* g, standing in for a freely selected local component of the Weyl–Maxwell–H² operator. The explicitly chosen reduced Lagrangian density is

`L=½(A_t²−A_x²)+½ G_ab(phi)(phi_t^a phi_t^b−phi_x^a phi_x^b)+g A_t Ω_uv(phi)(u_t v_x−u_x v_t)`.

This is a genuine *local variational* 3-field system and uses the **actual nonlinear hyperboloid target geometry**. But retaining only this A_t B_tx interaction term is **not a proven consistent tensor reduction of the complete dynamical Weyl curvature operator** (other contracted F and B components are omitted). The g strength has no G-free quarter-grid derivation and the representation-space q2 sector is not automatically the classical H² field. A pure fixed coefficient g alone cannot carry the full physical spacetime tidal dynamics.

Canonical momenta, with `D=1+u²+v²`, are

`p_A=A_t+g Ω(u_t v_x−u_x v_t)`,
`p_u=G_uu u_t+G_uv v_t+g Ω A_t v_x`,
`p_v=G_uv u_t+G_vv v_t−g Ω A_t u_x`.

They determine a symmetric velocity kinetic matrix

`M=[[1,gΩ v_x,−gΩ u_x],[gΩ v_x,G_uu,G_uv],[−gΩ u_x,G_uv,G_vv]]`.

The Hamiltonian density is `H=½(p_A A_t+p_u u_t+p_v v_t)+½ A_x²+½ G_ab phi_x^a phi_x^b`. In expanded field velocities `H=E_A+E_H²+E_mix` with `E_A=(A_t²+A_x²)/2`, `E_H²=G_ab(phi)(phi_t^a phi_t^b+phi_x^a phi_x^b)/2`, `E_mix=g A_t Ω(u_t v_x−u_x v_t)`. The interaction cross term can have either sign; the total kinetic part remains positive if M is positive definite, which we verify along the chosen evolution. The separate energy terms are a convenient decomposition of the chosen reduced theory, not universal gauge-invariant photon and gravity energies of the complete Einstein–Maxwell action.

## Gate 1357 — actual canonical numerical evolution and detailed conserved budget

On a periodic spatial grid x∈[0,2π), evaluate Fourier spectral spatial derivatives. Construct the discrete spatially averaged Hamiltonian exactly as written, and derive **all six** Hamilton equations with JAX 64-bit automatic differentiation, multiplying the derivative of the spatial mean by N to obtain the discrete canonical gradient. Integrate six real fields (three coordinates and their three momenta) with independent SciPy DOP853 `solve_ivp`; no Maxwell or sigma source is externally held fixed, and all three fields mutually respond. Initial data:

`A(0,x)=A_t(0,x)=0`,
`u(0,x)=.16 sin x,quad u_t(0,x)=.16 cos x`,
`v(0,x)=.13 sin(2x+.3),quad v_t(0,x)=−.13 cos(2x+.3)`.

The initial `p_A=g Ω(u_t v_x−u_x v_t)` is correctly nonzero although initial physical EM velocity `A_t=0`; the initial mechanical EM energy is zero. **Executed local file** `/mnt/data/cone_gate/h2_coupled_jax.py` produced:

| N | g | end t | initial H | max rel H drift | final A RMS |
|---:|---:|---:|---:|---:|---:|
| 16 | .12 | 1.6 | .033757373182929595 | 1.159×10⁻9 | .003978154206210483 |
| 16 | .06 | 1.6 | .03375737318292960 | 1.235×10⁻9 | .001989310376035920 |
| 16 | 0 | 1.6 | .033757373182929595 | 1.276×10⁻9 | 0 |
| 24 | .12 | 1.6 | .033757374301038603 | 1.705×10⁻9 | .003978154400100836 |

The min eigenvalue of full 3×3 kinetic M over the final spatial slice at N16,g=.12 is ~0.95483 (positive); all studied runs have positive kinetic eigenvalues. The N16,g=.12 final *separate budget* (same normalization) is

`E_A=1.7372540405506706×10⁻5`,
`E_H²=0.03374693677279759`,
`E_mix=−6.936130855019667×10⁻6`.

These sum to 0.033757373182348074, agreeing with the independently evaluated final H within ~floating precision, compared to initial 0.033757373182929595. The initial energy resides fully in the internal fields, but at end, A has a positive EM energy; the sigma energy and mixing energy have both adjusted so total H is unchanged. A second run g=.06 has A RMS half and E_A≈4.34360409149×10⁻6. At g=0 EM remains identically zero. N16 to N24 A RMS differs only ~2×10⁻10 absolute, while total H differs at ~10⁻9 due to spatial resolution of smooth initial data. This is strong **local reduced PDE numerical evidence**, not a rigorous mesh/continuum estimate or the full Weyl/EH dynamics.

**New canonical GitHub source:** `research-notes/k4_curved_h2_coupled_variational_energy_v15_1416.py`, commit **771ac871fb9d912ff67f81d43052ed52a2f40730**. It is equivalent to the actually executed local source and includes automatic gradients, positive kinetic and exact energy decomposition checks. Independent exact committed-byte Audit replay is pending; JAX installed in local execution environment, and Audit may need to install/enable 64-bit JAX explicitly.

## Gate 1358 — what the result says and does not say

Unlike the earlier one-way v15.1392 and v15.1414 Maxwell source tests, this is a mathematically *coupled backreaction* model: Maxwell field influences sigma fields and energy is conserved because **all fields are dynamical under one Hamiltonian**. Unlike v15.1396's four-complex-mode surrogate, the system uses the exact curved H² sigma metric and target area, spatial gradients and finite periodic Cauchy data. It is therefore a useful bridge toward a truly dynamical simulation.

The stronger conclusions remain **unproven**. The background gravitational tensor coupling is frozen and truncated rather than coming from the full metric's Weyl tensor; Einstein+K4 constraints, Weyl metric variation and Lorentz covariance of the truncation are absent. Its causal principal characteristics must be independently evaluated: even positive Hamiltonian does not certify causal wave propagation. That is the next v15.1417 gate, including a negative. Finally, the physical target radius r=1/4 still rescales against free sigma kinetic and g (v15.1387/1398); no physical G, new intrinsic gravitational force or unique coupling has emerged.

**AUDIT HANDOFF:** independently derive p_A,p_u,p_v and Hamiltonian from local L, replay committed JAX code, verify multiplication by N for spatially averaged H and correct positivity, test g0/half g and N16/24, independently compute final E_A,E_H²,E_mix and show initial A_t=0 despite p_A≠0. Check whether retaining only the frozen Weyl component is even a consistent gauge-covariant truncation and assess principal-symbol speeds. Do not mistake numerical Hamiltonian conservation of a chosen reduced theory for full Einstein–Maxwell–H² Noether/Bianchi certification.

**NEXT:** restore all Weyl tensor components and the actual Einstein+K4 metric variation, derive full coupled stress and principal symbol under controlled EFT cutoff, and evolve a finite localized packet while checking the same-action baseline and independent quarter-grid operator selector. Keep all negative results and nulls visible.
