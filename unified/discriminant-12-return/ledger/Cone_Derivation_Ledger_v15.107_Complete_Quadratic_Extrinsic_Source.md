# Cone Derivation Ledger v15.107 — Complete quadratic extrinsic term in conformal ADM gauge

Date 2026-10-29. Parent gravity v15.102. External Audit R401 checked gravity v15.094–v15.102; collision renumbering v15.106 preserved. Research note research-notes/K4_Full_Quadratic_Extrinsic_Hamiltonian_Source.md committed ece8315e6edd6dd5a4cbf2f13b76638522a1f267. Prewrite live HEAD ece8315e6edd6dd5a4cbf2f13b76638522a1f267. Separate lanes untouched; Suzuki physical quarter weld PARKED.

[D] h_ij=a²(1−2ψ)δij, lapse N=1+α, contrav shift N^i=β^i; Sij=(∂iβj+∂jβi)/2, θ=div β. Exact mixed K^i_j=N^-1{[H+(dot f−β·∇f)/(2f)]δ^i_j−S^i_j}, f=1−2ψ. Exact K²−KijKij=6A²−4A tr(S/N)+(tr(S/N))²−tr((S/N)²). Expansion to degree two:
𝒦2=6dotψ²+24Hαdotψ+18H²α²−24Hψdotψ+12Hβ·∇ψ+4dotψ θ+8Hαθ+θ²−SijSij.
Recover v15.096 α=β=0 expression; exact α-only expansion also checked.

[D] Complete degree-two Hamiltonian SOURCE generated solely by first-order fields in this conformal spatial gauge:
𝓗2[U1]=a^-2(16ψΔψ+6|∇ψ|²)+𝒦2−(2/3)|dotπ−β|²−(2/(3a²))(|∇π|²+4ψ divπ+12ψ²).
Actual order-two constraint is 𝓗1[U2]+𝓗2[U1]=0, so generic nonzero zero-mode of 𝓗2 is not independently a contradiction. No full second-order source evaluation on actual constrained first-order oscillator modes or zero-mode solvability theorem yet. This closes the missing extrinsic SOURCE expansion at quadratic order in specified gauge, not future nonlinear stability.

Flags: full_quadratic_extrinsic_invariant=DERIVED; conformal_quadratic_Hamiltonian_source=ASSEMBLED; first_order_constraint_substitution=OPEN; full_second_order_zero_mode_solvability=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: conformal-quadratic-extrinsic-Hamiltonian
parent: v15.107
status: open
action: Independently verify Lie-derivative K mixed formula, 𝒦2 all coefficients and limiting tests; check assembled 𝓗2 against full canonical triplet normal energy and intrinsic curvature, distinguish source from complete H1[U2]+H2[U1].
deliverable: scoped verdict.

NEXT: substitute certified constrained first-order scalar reconstruction α,β,ψ; calculate full low-output-K quadratic Hamiltonian source and second-order compatibility, with weighted Sobolev and gauge checks.
