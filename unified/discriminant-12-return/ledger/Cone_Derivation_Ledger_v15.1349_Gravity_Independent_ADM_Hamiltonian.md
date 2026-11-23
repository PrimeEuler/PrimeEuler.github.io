# Cone Derivation Ledger v15.1349 — Independently reconstructed ADM Hamiltonian from the assembled Einstein–Maxwell–K4 four-metric

**Date:** 2026-11-23 Eastern. **Track:** Gravity/Cone. **Immediately pre-ledger live HEAD:** c08032dbdbec4740f8330f17b9636bc36ac9f075. **Status:** [N PASS, scoped] independent position-space, *linearized* ADM Hamiltonian reconstruction from three neighboring fully assembled S/V/physical-TT+Bianchi metric slices compared to separately reconstructed Maxwell plus determinant-K4 energy; [PASS] second-order time-difference refinement and no-solid/no-Maxwell negative controls; [OPEN] the other nine Einstein tensor components, full nonlinear metric variation, spatial continuum convergence, detector optics, original quarter-mesh novelty. Strictly additive, no frozen files altered. Audit Round 627 (canonical **v15.1348**, SHA 18b780c83bea8e6b4f3dd96a4dba1e69a0306237) landed during this calculation and independently replayed Gravity v15.1345/1347 successfully. Accordingly canonical v15.1349 was selected and the exact targets checked absent before creation.

## Gate 1264 — truly geometric ADM quantity, not a replay of the sourced scalar ODE

Use v15.1347's *complete numerical real-space first-order metric*, including k>0 sourced scalar lapse/spatial potential, transverse vector shift, **physically signed** two-helicity TT strain, and the k=0 Bianchi-I isotropic correction u and shears beta, all driven by the **same v15.1274 dealiased Maxwell stress**. Require a weak-field amplitude A=0.1, and evaluate at t=1.08 on a periodic box L=4pi. Reconstruct **three separate complete metric solutions**, at t-dt, t, t+dt, with common initial time t0=1. This differs substantively from v15.1347's on-shell equations because the geometric constraint is now built from **spatial derivatives of the independently assembled position-space g_ij** and **finite differences of g_ij at distinct full histories**, not from the P, f, h mode-equation accelerations used to evolve fields.

Set a=t/sqrt3, s_ij=g_ij/a²-delta_ij, phi=-(g00+1)/2, and shift N_i=g0i. Compute linear spatial ADM curvature
`delta R^(3)=[partial_i partial_j s_ij - nabla² (tr s)]/a²`,
with FFT derivatives on the final spatial grid. From the physical ADM extrinsic curvature `Kij=[-dot(gij)+D_i N_j+D_j N_i]/(2N)`, background `K^i_j=-delta^i_j/t`, obtain the **linearized** Hamiltonian geometry
`delta[R^(3)+K²-KijKij] = delta R^(3) + (2/t) dot(tr s) - 12phi/t² - (4/t)(partial_i N_i/a²)`.
Calculate `dot(tr s)` from the *separately reconstructed* t±dt spatial metrics with a centered difference, not from the scalar sourced evolution equation. The transverse shift divergence is independently measured and negligible (~1e-19).

The **matter comparator is not defined as a rearrangement of this geometry**. It uses Maxwell conformal energy `rho_conf(x)=rho_mean+IFFT(r_k)` from the **same** 2N-dealiased and strictly projected stress used by all metric sectors; physical energy `rho_EM=9rho_conf/t⁴`. From the original K4 action `F(B)=C(det B)^(1/3)[1+eta_s J(B)]` and scalar material labels `phi^I=x^I+partial^I P`, the independent linear material energy is `delta rho_K4=(-6u+6Psi_N-2 k² P)/t²` for kappa C=1. The Bianchi-I tracefree beta and physical TT strain do not contribute to the first-order solid energy. Compare directly, point by point in real 3D space:
`C_ADM = delta[R^(3)+K²-KijKij] - 2[9rho_conf/t⁴+delta rho_K4]`.

The equation and the full reconstructed metric are linearized, not exact nonlinear constraints. No quadratic shift, shear, Maxwell gravitational backreaction, or higher-order gravitational terms may be called tested here.

## Gate 1265 — actual independently executed 12³–24³ numerical results

Use 13 common source-time samples within each assembled-metric trajectory from t0=1 to each endpoint, fourth-order RK4 and cubic Maxwell stress interpolation, with the physical TT sign fixed by v15.1343 and with electric field amplitude A=0.1. The following results come from the **actually executed independent local Python/NumPy/SciPy reproducer**; `max_residual` is absolute real-space local Hamiltonian residual, not a Fourier-mode on-shell identity:

| Grid | centered half step dt | max |geometric term| | max |matter energy term| | max |C_ADM| | max |C_ADM|/max |energy| |
|---|---:|---:|---:|---:|---:|
| 12³ | 0.0050 | 0.0044867581753876215 | 0.004486563664115481 | 2.9074232985634284e-7 | 6.480289852605095e-5 |
| 12³ | 0.0025 | 0.0044866122934391250 | 0.004486563664115481 | 7.271270258200468e-8 | 1.6206769373089875e-5 |
| 16³ | 0.0030 | 0.014804484445608439 | 0.01480532384681883 | 8.394012103920406e-7 | 5.669590338426808e-5 |
| 24³ | 0.0025 | 0.08172597005122743 | 0.08172370455020797 | 2.42267625191403e-6 | 2.9644718937399965e-5 |

At 12³, **halving dt reduces the max residual by ~3.998**, strongly indicating leading **O(dt²)** truncation error in the independently calculated geometric time derivative. The absolute max differs across grids because the compact initial Maxwell source is imperfectly resolved at N=12/16; this table **does not prove spatial continuum convergence** or that the model is physically realistic.

### Falsification controls

If the separately varied K4 solid energy is **omitted**, the max Hamiltonian residual jumps from 2.907e−7 to 0.00172349995 at 12³ (dt=.005), and from 2.423e−6 to 0.01448473984 at 24³. If the Maxwell energy is omitted, it instead jumps to 0.00612489468 and 0.09587967273. Both matter terms are load-bearing, and the agreement is not a vacuous vacuum constraint. All shift divergences are <=6.4e−19 on these grids because the source and shift are transverse.

## Gate 1266 — provenance, independent Audit, next genuinely new field equation

Locally executed standalone code: `/mnt/data/cone_gate/k4_independent_adm_hamiltonian_v15_1348.py` (local scratch filename reflects initial pre-Audit number; **canonical ledger is v15.1349**, do not treat it as authoritative v15.1348). This file incorporates the original assembled metric numerical core and independently computes finite-difference ADM spatial curvature and extrinsic-curvature trace, with assertions for weak residual, dt² ratio, solid omission and Maxwell omission. An additive GitHub script from the audited v15.1347 source core with the same separate ADM procedure is committed at `research-notes/k4_independent_adm_hamiltonian_v15_1349.py`, SHA **c08032dbdbec4740f8330f17b9636bc36ac9f075**. The original v15.1347 core was **not modified**; the new GitHub script's exact post-commit bytes have not been independently replayed. Local numerical values above come from the actual executed equivalent local standalone source, not Audit results. Audit must run the new exact committed file and check that its values and dt refinement agree, noting the different source-core implementation might have small rounding differences.

**AUDIT HANDOFF:** execute exact committed v15.1349 source; independently derive the coefficient/signs of the linearized Hamiltonian `delta R3+2 trsd/t−12phi/t²−4 div N/(t a²)` from the ADM normal/signature convention and independently vary original solid energy at fixed material labels. Verify correct k0 u, beta and source energy zero-mode, including projection of high Maxwell frequencies, and test dt→dt/2. The geometric constraint is still only **linearized** and tests only 00 normal-normal. Then independently derive momentum constraints from `D_j(K^j_i−δ^j_i K)`, spatial evolution components from metric time derivatives and 3D Ricci, and compare all to independently varied Maxwell+K4, **not to a rearrangement of the mode equations**. Test N=32/40/48 and observer-oriented gauge-invariant optical transfer after the full constraints pass.

**Scientific boundary:** Einstein–Maxwell plus exactly the same specified K4 relativistic solid; no new quarter-grid field coupling or G-free dimensionless observable selected, despite strong local numerical constraint evidence.
