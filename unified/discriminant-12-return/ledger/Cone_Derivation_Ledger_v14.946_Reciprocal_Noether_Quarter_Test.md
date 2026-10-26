# Cone Derivation Ledger v14.946 — Reciprocal factor Noether current and quarter-Casimir charge test
Date 2026-10-26. Parents v13.364/367/583, v14.944–945. Research note research-notes/Reciprocal_Factor_Noether_Current_Quarter_Charge_Test.md commit eb6b2ce9922364bf4c517299d7b0e1aa47dde948. Prewrite HEAD eb6b2ce9922364bf4c517299d7b0e1aa47dde948. Owner ledger-every-gate protocol; additive gravity only, Suzuki quarter correspondence PARKED; no Suzuki/far-tail edits.

[D, conditional action] Positive scalar factor fields u,v define rho=sqrt(uv), s=1/2 ln(u/v); reciprocal scaling (u,v)→(e^αu,e^-αv) keeps rho fixed and shifts s→s+α. Choose covariant action S=∫√−g[1/2(∂rho)²+1/2F(rho)(∂s)²−V(rho)], F>0. This ACTION IS A MODEL INPUT, not uniquely forced by AMGM. It has exact continuous shift symmetry and corresponding on-shell Noether current Jμ=F(rho)∇μs with ∇μJμ=0. In K4 FLRW metric a=τ/√3 the radial current obeys ∂τ(a³χ²F ∂τs)−∂χ(aχ² F∂χs)=0 and its outgoing spatial flux dilutes with spherical area under fixed-flux conditions.

[D, charge NONSELECTION] For e.g. F=F0>0 constant and V'(rho0)=0, homogeneous s obeys ∂τ(a³F0 dot s)=0, so arbitrary integration constant Qdensity=a³F0 dot s arises for any fixed lattice M_F²=δ²/4 and representation label C=j(j+1). Thus neither fixed local quarter nor fixed SU2 Casimir fixes amplitude of the shift Noether charge without added microscopic identification and boundary/initial conditions. A conserved Casimir eigenvalue is not generally a spacetime flux integral. Gravitational backreaction, source regularity and charge quantization remain untested.

[O] Candidate bridge needs a source-faithful mapping from oscillator pair/carrier to physical factor fields and canonical momenta and an independently derived Ward identity/constraint that relates Q to representation data. Choosing Q=q0 C would be a postulate, not this gate's result. F, V, physical metric/action, κ/G unfixed. Do not conflate with parked Suzuki spectral quarter.

Flags: factor_reciprocal_shift_symmetry=EXACT; chosen_covariant_action=CONSTRUCTED; local_Noether_current=DERIVED_ON_SHELL; quarter_fixes_Noether_charge=FALSE_WITHOUT_EXTRA_ASSUMPTIONS; source_magnitude=INITIAL_BOUNDARY_DATA; physical_gravity=NOT_DERIVED; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: reciprocal-factor-Noether-charge-versus-Casimir
parent: v14.946
status: open
action: Independently vary scalar factor action, confirm current and FLRW divergence factors; verify counterexample arbitrary shift charge at fixed Casimir/quarter with consistency of rho equation; distinguish geometric invariance from dynamical Noether conservation.
deliverable: scoped verdict.

NEXT: search for a representation-faithful oscillator-to-factor-field canonical map and action-selected charge quantization, not merely another numerical quarter match; continue scalar/vector Sandbox separately.
