# Cone Derivation Ledger v14.925 — Four-factor symmetry and elastic-source nonuniqueness

Date 2026-10-26. Parents v14.818, 820–825, 916–924. Research note research-notes/K4_Symmetry_Elastic_Solid_Nonuniqueness_Gate.md, commit a78cc5434e3ce464169db954745370eb0f2f943d. Prewrite live HEAD a78cc5434e3ce464169db954745370eb0f2f943d. Owner protocol: ledger every substantive gate. Additive gravity lane only; Suzuki/quarter weld parked and independent Suzuki/far-tail files untouched.

[D] Construct B^{IJ}=−g^{μν}∂μφ^I∂νφ^J for three comoving elastic solid labels. b=sqrt(det B), J=tr(B²)/(tr B)²−1/3>=0 for B positive definite, with equality precisely for isotropic B=b^(2/3)I. J is dimensionless, O(3)-invariant and homogeneous of degree zero. Crucially J=0 and first variation δJ=0 at an isotropic background. Thus the continuum of actions S_m(η)=−∫√−g C b^(2/3)[1+η J(B)] preserves EXACTLY the same flat linearly coasting FLRW background and first-variation stress energy as eta=0. Yet the quadratic anisotropic-strain action depends on η because δ²J≠0. This is an explicit obstruction to unique selection of matter microphysics by background AM-GM scaling/permutation/isotropy alone.

[CORRECTION TO COMPANION NOTE] For B eigenvalues λ_i, the exact identity is J=Σ_i(λ_i−λ̄)²/(Σ_i λ_i)², NOT the companion note's incidental formula with an extra factor of 3 in the denominator. The principal trace-based definition in the note is correct and is used here.

[D conditional classical elasticity] Given an isotropic relativistic solid with background p=−ρ/3 and independent shear modulus μ, high-frequency principal characteristic speeds are c_T²=3μ/(2ρ) and c_L²=−1/3+2μ/ρ in light-speed units. Necessary acoustic nonnegative subluminal window: ρ/6 ≤ μ ≤ 2ρ/3; strict c_L²>0 requires μ>ρ/6. This is a conditional formula, NOT a demonstrated existence/stability of the above η family for particular η, and not proof of ghost-free combined graviton/solid dynamics.

[O] Need compute μ(η) via the second variation of this exact action, including sign, then all scalar/vector/tensor quadratic perturbations, constraints and high-k stability. Factor Hessian geometry does not presently select η, κ, or gravitational source uniquely. Supernova full covariance from v14.923 separately open; no G derived.

Flags: symmetry_preserving_action_family=EXACT; background_metric_nonuniqueness=PROVED_BY_FAMILY; shear_parameter_undetermined=TRUE; conditional_acoustic_window=DERIVED; specific_eta_model_stability=UNTESTED; G_derived=FALSE; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-elastic-source-nonuniqueness
parent: v14.925
status: open
action: Independently derive vanishing first variation of J at isotropy, its positive quadratic shear term, correct eigenvalue identity, conditional acoustic speed interval and scope restrictions. No Suzuki/far-tail edits.
deliverable: scoped verdict.

NEXT: derive μ(η) and full linearized sound characteristics and test a stable parameter interval versus background geometry; continue official full-covariance Pantheon+ test independently.
