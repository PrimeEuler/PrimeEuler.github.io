# Cone Derivation Ledger v15.1277 — First k>0 sourced Einstein–Maxwell–K4 initial-slice Hamiltonian, momentum and scalar-shear closure

**Date:** 2026-11-21 Eastern. **Lane:** Gravity/Cone. **Immediately prewrite inspected HEAD:** d73fe9a1882d333790f8f8f24d301cbd909726e8. **Status:** [D] explicit initial-slice source/matter and scalar metric constraint identities for all nonzero Fourier modes, using the original K4 scalar Bardeen map and independent v15.1276 metric-to-Einstein operators; [N PASS] five-grid actually executed dealiased Maxwell+solid 00/longitudinal momentum/scalar-shear residuals to floating point; [NEGATIVE CONTROL] omitting the K4 solid energy produces a material Hamiltonian violation; [OPEN] evolved t>1 scalar constraints, full spatial trace, transverse vector momentum, tensor and off-diagonal Einstein equations, coupled entire metric, retarded optical apparatus and independently selected quarter-grid action. Strictly additive; Audit/Suzuki/Sandbox/Muse and frozen archived sources untouched.

## Gate 1233 — original compact source and a single conserved Fourier prescription

Use v15.1078 compact Maxwell E0, the v15.1267 discrete transverse Gauss projection and Nyquist-plane removal. At the initial slice tau=1, B=0 and Poynting flux F=0. Evaluate E on the **2N** zero-padded Fourier product mesh and form the quadratic conformal energy density rho=(E²)/2 and Tij=rho deltaij-EiEj there. Fourier transform the 2N products and project to the strictly nonzero, non-Nyquist native-N modes exactly as in v15.1274. This is the same conservation-preserving candidate source for each gravitational scalar mode.

For a mode with k>0, set `r=rho_hat` and `Tnn=n_i n_j Tij_hat`. The original sourced v15.1262 scalar P acceleration at initial P=P'=0 is `P''=9(3Tnn-r)/(2k²)`, with Maxwell B-source derivatives `J_B=0`, `J_B'=-3k² Tnn`. The v15.729 pressure-corrected lapse/spatial-potential transfer, with `J_Phi=J_psi=-sqrt(3)r/tau`, gives at tau=1:

`Psi_N=-3r/[2(1+k²)]`,
`Phi_N=[P''/3-3r-3J_B'/(2k²)]/(1+k²)`,
`Psi_N'=[-P''/3+3r+3J_B'/(2k²)]/(1+k²)`.

Consequently `Q=Psi_N'+Phi_N=0` **exactly** at the initial slice. This is a sourced initial-data consequence of the archived scalar equations and Maxwell stress, not a prediction about later momentum constraints.

## Gate 1234 — independent initial scalar Einstein source equations

The fresh v15.1276 independent metric-to-Einstein symbolic derivation gives, in the (-+++) Newtonian gauge at tau=1:
`delta G^0_0=6(k²Psi_N+Q)`, `delta G^0_long=-2ik Q`, and the scalar spatial transverse-minus-longitudinal difference `delta G^perp_perp-delta G^long_long=3k²(Psi_N-Phi_N)`.

The Maxwell mixed stress at initial slice is `delta T^0_0,EM=-9r`, `delta T^0_long,EM=0`, and the scalar anisotropy `delta T^perp_perp,EM-delta T^long_long,EM=9(r-3Tnn)/2` with a(tau=1)^-4=9. The original comoving degree-one K4 solid has `rho_s=C/a²`, and at initial P=P'=0 the scalar spatial metric perturbation yields `delta T^0_0,solid=-2C Psi_N/a²=-6Psi_N` for kappa C=1; its initial spatial STF stress vanishes (isotropic metric strain, zero material scalar displacement), and its initial momentum vanishes. Hence the **full** scalar source equations on that slice are

`C00 = 6(k²Psi_N+Q)+9r+6Psi_N=0`,
`C0long=-2ikQ=0`,
`Cshear=3k²(Psi_N-Phi_N)-9(r-3Tnn)/2=0`.

The last identity is not an assumed Weyl relation: inserting the archived source-first lapse and solid P acceleration gives `Psi_N-Phi_N=3(r-3Tnn)/(2k²)`. All three identities are algebraic consequences of the same physical source and original K4 action, and the numeric test checks the full projected 3D source, modes and normalizations. Note that this is **initial-slice, scalar-channel** Einstein closure only, not all Einstein equations or an independent proof of the entire K4 sourced evolution.

## Gate 1235 — five-grid 3D Fourier residuals and negative control

Run local Python/NumPy code using 2N Maxwell product evaluation at tau=1 for every retained k>0 mode:

| N³ | number of nonzero non-Nyquist modes | max abs C00 | max abs C0long | max abs Cshear | max abs C00 if solid omitted |
|---|---:|---:|---:|---:|---:|
| 16³ | 3374 | 5.421010862427522e-19 | 0 | 1.3010426069826053e-18 | 0.0024618686455495885 |
| 24³ | 12166 | 1.734723475976807e-18 | 0 | 2.6020852139652106e-18 | 0.005834105203256454 |
| 32³ | 29790 | 1.734723475976807e-18 | 0 | 2.168404344971009e-18 | 0.00548022496268236 |
| 40³ | 59318 | 1.734723475976807e-18 | 0 | 3.469446951953614e-18 | 0.005587044565902864 |
| 48³ | 103822 | 1.734723475976807e-18 | 0 | 2.6020852139652106e-18 | 0.005560023285683124 |

Mean source rho at N=48 is 0.0007786954245360609 and equals the v15.1274 Nyquist-clean Maxwell mean. The residuals are **model-normalized Fourier coefficient** differences, not physical SI errors. The solid omitted control isolates why the K4 constitutive energy response is necessary for the chosen scalar metric. The initial longitudinal momentum value is identically zero because flux, initial displacement/velocity and Q are zero: distinguish this identity from a dynamically propagated momentum constraint.

**Execution status:** the separate local exact Cauchy-field script `/mnt/data/cone_gate/k4_initial_scalar_constraints_v15_1277.py` was actually executed at all five N with the printed table and strict assertions. A new additive, functionally matching GitHub source `research-notes/k4_initial_scalar_constraints_v15_1277.py` is committed at SHA **d73fe9a1882d333790f8f8f24d301cbd909726e8**; its exact post-upload committed bytes await independent Audit replay. v15.1276 source operator committed at a71f599abe5464ed34f2316150891b63c6c5b9dc with ledger 557e894c01a073cb41df1a0d9acc094b607b810b.

## Gate 1236 — next independent physics and numerical obstructions

The advance is now from Maxwell Ward and homogeneous Einstein ODE regression to **actual k>0 initial scalar Einstein constraint closure against the Maxwell+K4 solid stress**. The next genuinely new falsification must evolve to tau>1 using one dealiased stress history for the scalar, transverse-vector and TT sectors, reconstruct `Phi_N,Psi_N,B_i,gamma_ij,u,beta_i` and independently compute `G_mu_nu-kappa(T_EM+T_K4)_mu_nu` with all spatial stress components, including derivatives of solid displacement in the same gauge. The initial spatial trace equation also remains untested in this gate; include it in the first time-dependent calculation. Constraint propagation should be tested at several tau and resolution, not inferred from algebraic initial cancellation. Preserve the original 2N product prescription and explicitly track excluded Nyquist metric modes.

**AUDIT HANDOFF:** independently derive the mixed-index Einstein signs from v15.1276, vary the exact original isotropic K4 material action to check the `-6Psi_N` initial solid energy contribution and vanishing initial solid STF and momentum, independently verify scalar-projected stress coefficient `9(r-3Tnn)/2`, and replay the exact v15.1277 committed code on all five grids. Check the initial-slice use of v15.729 sourced gauge transfer and Maxwell conservation identities. Do not conflate this initial-mode closure with a complete time-evolved Einstein solution.

**Scientific boundary:** all agreements are within standard Einstein–Maxwell with the specified ordinary K4 isotropic solid. No independently selected gravitational coupling from the mathematical 1/4/Casimir mesh or Newton-G-free dimensionless observable; identical-action GR comparator remains equal.
