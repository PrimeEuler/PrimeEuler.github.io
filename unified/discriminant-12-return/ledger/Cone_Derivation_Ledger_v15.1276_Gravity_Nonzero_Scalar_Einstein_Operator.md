# Cone Derivation Ledger v15.1276 — Independent scalar Fourier-mode Einstein constraint operators from the four-metric

**Date:** 2026-11-21 Eastern. **Lane:** Gravity/Cone. **Prewrite live HEAD:** a71f599abe5464ed34f2316150891b63c6c5b9dc. **Classification:** [D] direct first-order Einstein geometry for a Newtonian-gauge nonzero scalar Fourier mode on the coasting FLRW K4 background, calculated independently by Christoffels/Ricci rather than by archived sourced tidal operators; [C] symbolic zero residual for five mixed Einstein-tensor components; [OPEN] full sourced Einstein–K4 residual, vector and tensor metric, combined time-dependent constraint propagation, causal photon/mirror/clock, independent quarter-grid physical coupling. Strictly additive; original Maxwell/K4, Audit, Suzuki, Muse and Sandbox untouched.

## Gate 1230 — direct four-metric linear Einstein tensor

Use the scalar Newtonian-gauge metric from historical v15.729/v15.787, `ds²=-(1+2Φ_N e^{ikz})dτ² + a²(1-2Ψ_N e^{ikz})δij dxi dxj` with `a=τ/√3` and signature (-+++). Perturb the *full metric* first, compute inverse perturbation `δg^μν=-g0^μα h_αβ g0^βν`, all `δΓ^μ_νρ`, `δR_μν`, `δR` and `δG^μ_ν`, retaining every first-order background-metric cross-term including the mixed-index inverse perturbation contribution. This calculation does not start from the archived electric tidal field.

Independent SymPy symbolic calculation yields for k>0:

`δG^0_0=6[k² Ψ_N + τ Ψ_N' + Φ_N]/τ²`;
`δG^0_z=-2 i k [τ Ψ_N' + Φ_N]/τ`;
`δG^z_z=2[τ² Ψ_N'' + τ Φ_N' + 3τ Ψ_N' + Φ_N]/τ²`;
`δG^x_x=δG^z_z + 3k²(Ψ_N-Φ_N)/τ²`;
`δG^x_y=0`.

The background scalar curvature is `R_background=6/τ²`. These identities were checked independently by direct first-order symbolic Christoffel-to-Einstein calculation and all five component differences simplified **exactly to zero** in an actually executed local Python/SymPy script. This verifies the sign and normalization of the *geometrical* k>0 00/momentum/spatial operators for the chosen gauge. They are not yet the Einstein **matter-coupled** equations.

## Gate 1231 — constraint inversion and independent checks now available

Write `Q=τ Ψ_N'+Φ_N`. Then the two scalar metric constraints are `δG^0_z=-2ik Q/τ` and `δG^0_0=6(k² Ψ_N+Q)/τ²`. With a physically supplied combined Maxwell+solid perturbative source `S^μ_ν=κ δT^μ_ν` in the **same mixed-index sign and background**, the geometry gives independently testable relations:

`Q= -τ S^0_z/(2ik)`,
`Ψ_N= [τ² S^0_0/6 - Q]/k²`, for k>0.

This is **not** an independent solution of K4 constraints, since the perturbed K4 material stress generally depends on the scalar metric, solid displacement P and its derivatives; that dependence must be computed from the original frozen action. The exact independently audited v15.729 sourced Bardeen map should predict `Φ_N,Ψ_N`; plug those into these operators and compare against **an independently varied, identically sourced** Einstein+K4 stress. Do not substitute Maxwell-only stress on the RHS and falsely label the residual gravitational failure: the ordinary solid response is necessary. For the same reason, the nonzero tensor and transverse shift components must be independently checked before claiming the full Einstein equations.

## Gate 1232 — numerical integration protocol and explicit open boundary

Use the v15.1274 shared dealiased/retained Fourier `rho,F,Tij` (not the aliased v15.1267 source) at matching N,time and the v15.1275 homogeneous Bianchi-I `u,β` from the same Maxwell initial source. Recompute all scalar/vector/tensor histories from these common source coefficients, recover `Φ_N,Ψ_N,B_i,γ_ij` using their archived gauge conventions and source Ward identities, derive physical `T^μ_ν` of the original K4 solid by varying its action at the **same metric**, and evaluate `δG^μ_ν-κδT^μ_ν` on a common time grid. Report maximum/relative mode errors, time interpolation errors and field-resolution convergence. Tests must include `k>0` scalar 00,0longitudinal, spatial trace/shear, transverse momentum, TT and the proper homogeneous background. This gate supplies the scalar geometry operator necessary for the calculation; it **does not** provide a coupled solver or report a sourced Einstein constraint residual.

## Reproducibility and Audit

The local independent SymPy calculation actually executed, produced exact zero symbolic discrepancies and printed all five operators. The additive standalone source `research-notes/k4_scalar_metric_einstein_operator_v15_1276.py` committed as SHA a71f599abe5464ed34f2316150891b63c6c5b9dc recomputes direct background/linearized connections, Ricci, Einstein tensors and asserts the five geometric identities. The exact byte-original committed script awaits independent External Audit replay. No prior source was changed; no certified Suzuki work affected.

**AUDIT HANDOFF:** replay v15.1276; check mixed 0z sign under (-+++), δg inverse contribution to δG^μ_ν and background R=6/τ². Then audit source-dependent δT_solid with exactly v14.935/v15.711–729 conventions, explicitly including Maxwell four-stress and v15.1274 Fourier projection. The crucial next gate is a *nonzero sourced* Hamiltonian/momentum residual, not a second proof of this operator identity.

**Scientific boundary:** Einstein–Maxwell coupled to the ordinary specified K4 solid; no independently selected physical quarter-grid/Casimir interaction or Newton-G-free new dimensionless observable.
