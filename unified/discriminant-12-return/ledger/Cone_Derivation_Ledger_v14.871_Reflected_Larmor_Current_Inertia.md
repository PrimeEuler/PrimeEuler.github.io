# Cone Derivation Ledger v14.871 — Conserved reflected-Larmor current and regulated inertia

Date 2026-10-25. Parents v14.863 and v14.870. Research note research-notes/Reflected_Larmor_Conserved_Current_Quasistatic_Inertia.md commit eb203b71946c20808d0c115cacde167c89d26915. Live prewrite HEAD eb203b71946c20808d0c115cacde167c89d26915. Additive only; Suzuki/far-tail untouched.

[I/D] Choose explicit equal-width Gaussian charge blobs ±q at reflected Larmor-circle positions r±=(±Rξ,R sqrt(1−ξ²)cosφ,R sqrt(1−ξ²)sinφ), ξ=δ/u. The distribution ρ=Σqσ f_a(r−rσ), J=Σqσ rdotσ f_a(r−rσ) obeys ∂tρ+∇·J=0 EXACTLY, with total charge zero and electric dipole p=2qRξ xhat. This neutral pair is NOT itself a Coulomb charge monopole; the charge assignments are model choices rather than deductions from bicone algebra.

[D, quasistatic frozen-orbit approximation] At first order in δ, in local comoving frame, P=gδ f_a xhat, g=2qR/u; ρ=−∇·P and J=∂tP. In Coulomb gauge transverse J_T gives positive magnetic near-field energy E_B=1/2 M_T δdot² with
M_T=μ0 g² ∫d³k/(2π)³ (1−kx²/k²)e^(−a²k²)/k²
=μ0 (2qR/u)²/[6π^(3/2)a].
This is finite for a>0, strictly positive, scales as 1/u² at fixed q,R,a; normalized ξ inertia u-independent. It is NOT the full regulator-independent electromagnetic contribution to particle mass, which requires complete fields, supporting stresses and retarded treatment.

[D, far-field leading dipole] When source speeds and sizes permit electric-dipole approximation, P_rad=g² δddot²/(6π ε0 c³). For finite φdot, full radiation and effective response contain further Larmor-driven terms not computed. Maxwell stress-energy gravitates through standard GR but does not thereby prove an independent gravity monopole coupling or a Higgs field.

[O] Derive the actual bicone source assignment instead of positing ±q blobs, retain rotating phase and causal nonlocal retarded Maxwell kernel, add conserved monopole sector separately, and test full gravitational stress-energy response. No Newton G/alpha extraction.

Flags: charge_conservation=EXACT; neutral_pair_total_charge=ZERO; seat_electric_dipole=2qRdelta_over_u; quasistatic_transverse_inertia=POSITIVE_REGULATOR_DEPENDENT; full_physical_inertia=NOT_DERIVED; source_from_bicone=POSTULATED; gravity_shared_seat=OPEN; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: reflected-larmor-conserved-current-inertia
parent: v14.871
status: open
action: Verify continuity equation for moving blobs, dipole and leading radiation, Gaussian transverse-field Fourier integral and coefficient, regulator dependence, and nonidentification with net charge monopole or full inertial/gravitational mass.
deliverable: scoped independent verdict.
