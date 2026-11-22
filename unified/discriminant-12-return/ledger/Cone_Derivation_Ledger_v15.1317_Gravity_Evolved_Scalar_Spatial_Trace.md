# Cone Derivation Ledger v15.1317 — Exact time-dependent scalar Einstein spatial trace and longitudinal/transverse pressure closure

**Date:** 2026-11-22 Eastern. **Lane:** Gravity/Cone. **Status:** [D PASS] exact symbolic sourced longitudinal and scalar-transverse-average spatial Einstein equations for all tau>0,k>0, with independently differentiated original K4 solid pressure and conserved Maxwell stress; [OPEN] complete vector/TT Einstein equations, spacetime four-metric and optical probe, numerical convergence, physical quarter-grid action. **Immediately pre-ledger live HEAD:** 28829c8eebbdf22ec138d3485d82a1224de04405. New target v15.1317 was checked absent before write. Audit Round 624 had just landed at SHA 25e6bfc0f3dcb66ce54306e9d23afc81f46b428d and **owns v15.1316**; thus Gravity deliberately skipped that number to avoid a collision. No historical content overwritten. All previous certified gravity, Audit, Suzuki, Muse/Sandbox and K4 source assets remain intact.

## Gate 1244 — independent scalar spatial pressure from the frozen K4 material action

Use exactly the existing material action `F=C(det B)^(1/3)[1+eta_s(tr B²/(tr B)²−1/3)]`, its pressure `p_i=−F+2B_i ∂F/∂B_i`, scalar metric `gij=a²(1−2Psi_N)δij` and material labels `phi^I=x^I+∂^I P`. Choose k in the z direction, with `Bx=By=a^-2(1+2Psi_N)`, `Bz=a^-2(1+2Psi_N−2k²P)`. Differentiate the full unexpanded F, then linearize its principal pressures; at `a=τ/sqrt3, eta_s=3/4, kappa C=1`:

`delta p_s,trans = -2 Psi_N/τ² + 4 k²P/(3τ²)`,
`delta p_s,long = -2 Psi_N/τ² - 2 k²P/(3τ²)`.

Their difference is `2k²P/τ²`, reproducing v15.1315's independently Audited shear and now fixing both *individual scalar-projected principal pressures*, not just the difference. Maxwell has `delta T^z_z=9Tnn/τ⁴`, `delta T^trans_trans=9(r−Tnn)/(2τ⁴)` in the scalar sector.

## Gate 1245 — sourced longitudinal and transverse spatial Einstein equations

The independently derived v15.1276 Newtonian metric-to-Einstein operator gives

`delta G^z_z = 2[Psi_N''+(3Psi_N'+Phi_N')/τ+Phi_N/τ²]`,
`delta G^trans_trans = delta G^z_z+3k²(Psi_N−Phi_N)/τ²`.

Use the same Maxwell pressure-corrected v15.729 Bardeen potentials as v15.1314–1315, the original sourced K4 P equation

`P''+3P'/τ+(2+k²)P/τ²=9(3Tnn−r)/(2k²τ⁴)`,

the dealiased-source Maxwell energy Ward `r'=-i sqrt3 k F_parallel/τ` and momentum Ward `F_parallel'=-i sqrt3 k Tnn/τ`, and their exact time derivatives. Compute `Phi_N'`, `Psi_N'`, `Psi_N''` **symbolically**, substituting the equation for P'' and its time derivative and the Maxwell energy/momentum laws. Both scalar-projected spatial Einstein residuals simplify **exactly** to zero:

`C_long = delta G^z_z − 9Tnn/τ⁴ + 2Psi_N/τ² + 2k²P/(3τ²) = 0`,

`C_trans = delta G^trans_trans − 9(r−Tnn)/(2τ⁴) + 2Psi_N/τ² − 4k²P/(3τ²) = 0`.

This closes the scalar spatial trace **and** longitudinal-versus-transverse scalar shear under the chosen K4/Maxwell mode equations. The derivation is independent in the sense that K4 *material principal pressures* were obtained directly from the original F(B) rather than inferred by subtracting geometry; however, both identities are **conditional on those same sourced K4 dynamical equations and Maxwell Ward identities**. They do not constitute an independent nonperturbative 3D Einstein solution.

## Gate 1246 — reproducibility and remaining obstruction

A local independently authored Python/SymPy script evaluated both symbolic residuals to exact zero and separately confirmed the K4 principal-pressure variations. The first local implementation expanded the solid action and Bardeen time-derivative substitutions together and proved computationally intractable; the final *mathematically equivalent* execution computes geometry and stress identities in separate stages, finishing successfully. This is a symbolic exact result, not a multi-grid numerical amplitude, and should not be mislabeled a spatial-convergence certificate.

New additive source `research-notes/k4_evolved_scalar_spatial_trace_v15_1317.py`, commit SHA **28829c8eebbdf22ec138d3485d82a1224de04405**, implements the same exact symbolic tests. The local executed file `/mnt/data/cone_gate/k4_evolved_scalar_spatial_trace_v15_1317.py` is available. The exact GitHub committed bytes still await independent External Audit replay.

Together with independently Audited v15.1314 Hamiltonian/longitudinal momentum and v15.1315 scalar shear, this establishes conditional **time-dependent scalar-sector first-order Einstein closure** for the specified conserved Maxwell source and frozen K4 material model. It does **not** prove vector transverse momentum, off-diagonal spatial constraints, tensor TT Einstein equations, simultaneous full metric and full physical Maxwell backreaction. Next derive and independently stress-check transverse-vector Einstein–K4 equations using the same dealiased source, then TT and the actual physical optical photon/free mirror/clock system. In particular do not claim a new Cone-only gravitational observable simply from the mathematical mesh.

**Audit handoff:** independently replay source; verify especially k/tau signs of `F_parallel'=-i sqrt3 k Tnn/τ`, source v15.729 mixed-index conventions, the full K4 pressure derivatives, and geometric spatial operators. Check the scalar-transverse-average projection against nonzero TT stress; do not mistake the projected scalar equation for full `G^x_x` when vector/tensor modes are present. Preserve Audit-owned v15.1316.

**Scientific boundary:** this remains standard Einstein–Maxwell coupled to the specified isotropic relativistic K4 solid, with the identical-action GR comparator indistinguishable. No independently justified quarter-grid coupling, SI scale or G-free gravitational prediction has emerged.
