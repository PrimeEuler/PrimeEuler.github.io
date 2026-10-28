# Cone Derivation Ledger v15.044 — Scalar reduced mode is strain, not uniform displacement

Date 2026-10-28. Parent gravity v15.043. Corrected source payload v14.996 scalar_adm2.py and scalar_final2.py inspected directly. Research note research-notes/K4_Scalar_Reduced_Mode_Displacement_Infrared_Map.md commit 96c828d1ae7a4de2d2a2ae9d0f5a83f1ca2f2d9b. Prewrite live HEAD 96c828d1ae7a4de2d2a2ae9d0f5a83f1ca2f2d9b. Protected Lane A, external audit, Suzuki physical quarter weld untouched/PARKED.

[D] Corrected scalar source ansatz φ3=z+e π(t) sin(kz)/k, so reduced dynamical π amplitude denotes longitudinal STRAIN ∂zδφ3=π cos(kz), whereas actual scalar displacement amplitude is π/k. scalar_final2.py reduces to π equation ddotπ+3τ⁻¹dotπ+(3k²+4)τ⁻²π=0 (confirmed reconciliation). At each fixed k≠0, π=τ⁻¹u with bounded oscillator u(s) implies displacement=(τ⁻¹/k)u, but NO uniform k→0 control of displacement from ordinary H^r of π. Velocity term in v15.043 quadratic fixed-metric ρ2 scales as |dotπ|²/k². Thus integrable e^-2s conditional weighted Hamiltonian source bound additionally needs |k|⁻¹(u_s−u) controlled, or equivalent constraint/gauge cancellation. For T³ fixed torus positive minimal nonzero k allows box-dependent bound; R³ requires low-frequency weighted norms / physical reconstruction.

This is a normalization refinement to v15.043, whose conditional assumption already required coordinate displacement decay and was not established. It does not invalidate the corrected reduced mode's linear stability, and neither IR divergence of actual full constrained physical system nor nonlinear future stability is proved.

Flags: corrected_scalar_reduced_pi_is_strain=SOURCE_VERIFIED; displacement_scalar_fourier_inverse_k=EXACT; uniform_displacement_decay_from_unweighted_pi=FALSE; matter_energy_IR_weight_requirement=IDENTIFIED; full_nonlin_constraint_cancellation=OPEN; global_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: corrected-scalar-strain-displacement-map
parent: v15.044
status: open
action: Verify scalar_adm2.py ansatz pi/k and scalar_final2.py reduction, demonstrate physical displacement velocity IR factor 1/k, distinguish fixed-k decay from uniform R³ bound and retain v15.043 conditional status.
deliverable: scoped verdict.

NEXT: derive constraint-compatible low-k condition for longitudinal velocity and physical energy in terms of reduced strain variable; test cancellations from metric/lapse/shift and H^-1 weighted norms, not assume uniform displacement norm.
