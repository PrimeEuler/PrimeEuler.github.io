# Cone Derivation Ledger v14.956 — K4 Killing-momentum conservation and central-flux obstruction

Date 2026-10-26. Parent v14.955; research note research-notes/K4_Killing_Momentum_Currents_Radial_Flux_Obstruction.md commit 5047cebc57bd5e4eed32d31120fb716aaea252c3. Live prewrite HEAD 5047cebc57bd5e4eed32d31120fb716aaea252c3. Owner per-gate additive ledger protocol. Independent Suzuki-quarter physical weld PARKED, Suzuki/far-tail untouched.

[D] K4 product-Hessian metric g=dτ²−a(τ)²Σdzi², a=τ/√3, admits three spatial translation Killing vectors ξ_i=∂zi. For any symmetric, covariantly conserved matter stress tensor T^{μν}, currents J_i^μ=T^{μν} ξ_{iν}=T^μ{}_i obey ∇μJ_i^μ=0 on matter equations. Integrated charges ∫Σa³J_i^τd³z are conserved for appropriate decay. Example canonical test scalar L=1/2(∂Ψ)²−V has T^μ{}_i=∂^μΨ∂iΨ−δ^μ_i L, while test-field Hamiltonian has positive kinetic and spatial-gradient terms; negative spatial metric does not cause a matter ghost.

[D/OBSTRUCTION] The translation charges are THREE VECTOR momentum components, not a rotational scalar point-source charge. For a spherical scalar Ψ(τ,χ) total vector momenta vanish by angular cancellation. The outward radial vector n^i∂zi is NOT itself Killing; a radial projection of vector currents cannot be conflated with v14.944's radial conserved scalar charge. Thus the spatial Killing currents do not fix a nonzero isotropic flux amplitude Φ nor yield Newton gravity. A scalar internal-shift charge would require additional matter dynamics and freely set initial/source data. Expanding metric ∂τ is not a timelike Killing direction.

[O] Next: test conformal/homothetic spacetime symmetry, deriving ∇μ(T^{μν}Hν)=1/2 T^{μν} L_H gμν. If H is homothetic, divergence is proportional to trace; for traceless matter a conserved dilation charge may exist. Distinguish from Killing momentum and scalar source. No physical G nor fixed charge. Prior Pantheon+ mismatch and full SVT stability open.

Flags: K4_spatial_Killing_vectors=THREE_EXACT; Killing_momentum_currents=CONDITIONALLY_CONSERVED; isotropic_central_charge_from_translation=NOT_DERIVED; radial_direction_Killing=FALSE; Newton_G=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: k4-Killing-current-vs-central-flux
parent: v14.956
status: open
action: Check current divergence, sign of covariant spatial momentum, spherical total momentum cancellation and radial direction not Killing. Confirm no scalar charge normalization derived.
deliverable: scoped verdict.

NEXT: compute homothetic dilation current and stress-tensor trace obstruction for massless conformal matter in K4; separate Sandbox coupled scalar/vector work.
