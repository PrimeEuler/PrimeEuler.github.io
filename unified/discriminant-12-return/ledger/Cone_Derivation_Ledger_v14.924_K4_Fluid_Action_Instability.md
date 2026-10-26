# Cone Derivation Ledger v14.924 — Covariant fluid completion and instability gate

Date 2026-10-26. Parents v14.818, 820–825, 916–923. Research note research-notes/K4_Covariant_Fluid_Background_and_Scalar_Gradient_Instability.md commit 8f08a3530912457f8b35c2733196b946e3d63695. Live prewrite HEAD 8f08a3530912457f8b35c2733196b946e3d63695. Additive gravity lane only; Suzuki/far-tail untouched; Suzuki-quarter weld remains parked. Owner's ledger-every-substantive-gate protocol active.

[I/D] A covariant candidate completion with INDEPENDENT metric g and fluid-label fields phi^I has action ∫√−g[R/(2κ)−C b^(2/3)]d⁴x, b=sqrt(det[−g^μν ∂μφ^I∂νφ^J]); κ>0,C>0 are free theory parameters. Its fluid has rho=C b^(2/3) and p=−rho/3. On comoving phi^I=z^I flat FLRW b=a^(-3), Friedmann gives a_dot²=κC/3 and branch a=sqrt(κC/3) τ. At κ C=1 the exact previously derived k4 Hessian background a=τ/√3 is recovered. This does not uniquely select that background or derive κ. Unlike the constrained vierbein v14.825, g remains independently varied, so TT spin-2 propagation is not algebraically removed.

[D/OBSTRUCTION] The minimal barotropic perfect fluid is adiabatically scalar-gradient unstable: c_s²=dp/dρ=−1/3, and subhorizon ω²≈−k_phys²/3. Therefore this candidate is NOT a healthy microscopic gravitational source despite exact background matching. Extra microphysics needed and must be derived/justified, not appended as an unexplained new parameter.

[O] Native four-factor symmetry/uniqueness and viable source dynamics unresolved; G not derived and physical photon coupling not established. Cosmological data diagnostic separately v14.923 (no full covariance). Do not use this source as validation of observed gravity.

Flags: k4_covariant_background_action=CONSTRUCTED_CONDITIONAL; k4_FLRW_background=EXACT_SOLUTION_given_κC_1; metric_independent_spin2=NOT_ALGEBRAICALLY_FROZEN; minimal_fluid_sound_speed_squared=NEGATIVE_ONE_THIRD; minimal_fluid_gradient_instability=FAIL; stable_matter_microphysics=OPEN; G_derived=FALSE; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-fluid-action-instability
parent: v14.924
status: open
action: Independently vary covariant comoving-fluid action, derive p=-rho/3 and flat FLRW a_dot²=κC/3, verify negative adiabatic c_s² and subhorizon gradient instability; distinguish independent Einstein-Hilbert dynamical metric from full stability proof. Keep Suzuki-quarter parked and far-tail untouched.
deliverable: scoped verdict.

NEXT: test whether native permutation/scaling/homogeneity AM-GM symmetries select a stable dynamical source rather than an arbitrary completion; await full-covariance Pantheon+ handoff separately.
