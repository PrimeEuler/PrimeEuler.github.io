# Cone Derivation Ledger v14.952 — Square-root hyperbola and Hessian-selected shape scaling

Date 2026-10-26. Parents original K2 cone, v14.941, 944–950; v14.951 External Audit Round 367 read from latest HEAD. Research note research-notes/K2_Sqrt_n_Hyperbola_Hessian_Shape_Kinetic.md committed 5a53ceb948d89d06aa530e8a72c1bea5308b9a9e. Prewrite live HEAD 5a53ceb948d89d06aa530e8a72c1bea5308b9a9e. Owner ledger every substantive gate. Additive gravity only; Suzuki quarter weld PARKED, protected Suzuki/far-tail untouched.

[D] For positive factor product n=uv, hyperbola uv=n admits u=√n e^s,v=√n e^-s with ρ=√uv=√n and s=1/2ln(u/v). Reciprocal scaling is s translation, fixes n. Product Hessian metric Hess(uv): dℓ²=2du dv=2dρ²−2ρ² ds². Thus *geometry selects coefficient proportional to ρ²=n* in the shape metric; it does not select a matter action's positive F or source amplitude. For Hessian-geodesic L=dotρ²−ρ² dot s², p_s=−2ρ² dot s is conserved on-shell by shape translation. This is a dynamical conserved quantity for a chosen geodesic L, NOT a quantum SU2 Casimir / gravitational Gauss source.

[D] For K4 P4=uvcd with x3=c>0,x4=d>0 fixed, induced Hessian quadratic form is 2cd(dρ²−ρ²ds²), and fixed-product shape line metric is −2P4ds². Important: Hessians as raw second derivatives under nonlinear coordinate changes are not tensors; result uses pullback of Hessian metric defined originally in linear factor coordinates. Sign: shape is negative within Lorentzian factor metric, so naive target-metric matter kinetic contains wrong-sign scalar relative to radial field under (+---); choosing healthy F>0 needs added prescription (flip shape sign, alternative action or constraint), not automatically justified by AMGM.

[O] User's sqrt exponent correctly locates geometric-mean hyperbola scale; no identification of factor-space ρ with physical-space areal R is yet derived. Inverse-area law v14.944 remains from O(3) spherical current conservation, not a consequence of sqrt(n) alone. Charge magnitude, Einstein coupling κ, η and stable source action still OPEN. This is distinct from physically parked Suzuki quarter.

Flags: sqrt_n_hyperbola_parameterization=EXACT; Hessian_shape_coefficient=proportional_to_n; reciprocal_shape_geodesic_charge=CONDITIONAL; healthy_matter_F_selected=FALSE; source_charge_fixed=FALSE; Newton_G=NOT_DERIVED; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: sqrt-n-hyperbola-hessian-shape
parent: v14.952
status: open
action: Check Hessian pullback, canonical shape momentum and its sign, K4 fixed-pair embedding, and whether selected shape coefficient alone supplies a healthy scalar field action or physical radial source (it does not).
deliverable: scoped verdict.

NEXT: test a covariant Hessian-derived sigma-model candidate versus ghost sign and background constraints, and whether a canonical source normalization can be obtained without extra physics.
