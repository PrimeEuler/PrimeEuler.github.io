# Cone Derivation Ledger v14.827 — Hyperbola-pendulum elastic-medium subgate

Date 2026-10-24. Gravity lane. Parents v14.626 and v14.821–826. Research note research-notes/Hyperbola_Pendulum_Coupled_Rotor_Elasticity_Test.md committed 0aefd5591f8c33bc218c18f2c7274a0e7ea896ad. Additive only; no Suzuki/far-tail modifications.

## Coupled rotor lattice [D]

Use inertia I>0, onsite restoring torsion K=M g_local l>=0 (from prior pendulum), positive new nearest-neighbor coupling J and spacing ℓ:
\[
L=\sum_n [I\dotθ_n²/2-Kθ_n²/2-(J/2)\sum_{\alpha=1}^3(θ_{n+\hat\alpha}-θ_n)²].
\]
Exact dispersion \(\omega²(q)=K/I+(4J/I)\sum_\alpha\sin²(q_\alpha\ell/2)\), giving real frequencies for K,J>=0. Continuum angular-gradient stiffness J/ℓ is NOT automatically a mechanical shear modulus.

## Conditional shear mapping [D/I]

Additional kinematic identification for a single displacement polarization θ_n=u_x(n)/ℓ and a gradient along y gives bond strain θ_{n+ŷ}-θ_n≈∂_yu_x. Shear energy density \(W=(J/(2\ell³))(\partial_yu_x)²\), hence \(\mu=J/\ell³\), inertial density \(I/\ell^5\), transverse speed \(v_T²=J\ell²/I\). This is an explicit one-polarization construction, not a derived full isotropic relativistic elastic solid. Onsite pendulum K pins displacement and breaks pure translation invariance if imposed on all sites: a genuine full-medium completion must separate local rotation from acoustic translations.

## Conditional isotropic relativistic stability [D/O]

For a separately assumed isotropic relativistic elastic continuum with p=-ρ/3, standard \(c_T²=\mu/(\rho+p)=3\mu/(2ρ)\) and \(c_L²=dp/dρ+4\mu/[3(\rho+p)]=-1/3+2\mu/ρ\). Nonnegative subluminal squared speeds imply \(\rho/6\le\mu\le2\rho/3\). Substituting μ=J/ℓ³ is allowed only after an isotropic and relativistic constitutive completion with independently identified ρ; no value of J or Newton G is predicted from the pendulum.

Next: construct a translation-invariant coupled rotation-displacement continuum with all longitudinal and transverse spectra and check covariance/energy; do not call a positive rotor frequency proof of full fluid scalar stability.

Flags: rotor_lattice_dispersion=EXACT; angular_gradient_stiffness=J_over_ell; shear_modulus=CONDITIONAL_LOCKING; isotropic_completion=OPEN; fluid_scalar_stability=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-coupled-rotor-elasticity-check
parent: v14.827
status: open
action: Check lattice dispersion, continuum dimensions, conditional displacement shear mapping and its pinning/translation drawback, and the relativistic stability interval. Do not modify Suzuki/far-tail.
deliverable: scoped independent verdict.
