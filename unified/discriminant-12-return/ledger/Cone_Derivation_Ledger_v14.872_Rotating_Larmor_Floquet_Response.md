# Cone Derivation Ledger v14.872 — Rotating reflected Larmor current and electromagnetic sidebands

Date 2026-10-25. Parents v14.870–871. Research note research-notes/Rotating_Reflected_Larmor_Floquet_Current_Response.md, commit 689d071919f1bd9054a07e85021ea90ee54d7e79. Live prewrite HEAD 689d071919f1bd9054a07e85021ea90ee54d7e79. Additive gravity side-lane; Suzuki/far-tail untouched.

[D within explicit model] For ±q Gaussian blobs at reflected centers rσ=c(t,ξ)+σRξ xhat with c=R sqrt(1−ξ²)(0,cosΩ_L t,sinΩ_L t), ξ=δ/u, the exact Fourier charge density is ρ(k,t)=−2iq e^(−a²k²/2)e^(−ik·c)sin(kxRξ). The exact Fourier current is J(k,t)=2q e^(−a²k²/2)e^(−ik·c)[R ξdot cos(kxRξ)xhat −i cdot sin(kxRξ)]. These satisfy ∂tρ+i k·J=0. Total charge remains zero and electric dipole p=2qR ξ xhat has no Larmor-rotation of its direction. Pure Ω sidebands therefore DO NOT appear in its leading electric dipole moment unless ξ varies at those frequencies.

[D] Beyond the leading dipole approximation e^(−ik·c0(t)) has a Jacobi–Anger/Bessel harmonic expansion, generating frequency channels ω+nΩ_L from a seat oscillation at ω. The transverse retarded Maxwell Green function has frequency-dependent denominators k²−[(ω+nΩ_L+i0)/c]². This indicates a periodically driven/Floquet response, not an established positive constant inertial mass across frequencies or a genuine eigenmode pole.

[D] At fixed nonzero ξ, rotating neutral pair has m(t)=−qR²ξΩ_L(0,cosΩ_Lt,sinΩ_Lt), a magnetic dipole rotating at Ω_L; its leading magnetic-dipole radiated power is μ0 q²R⁴ ξ² Ω_L^6/(6πc³) in the slow/long-wavelength regime, but quadrupole and other multipoles may also contribute. At ξ=0 opposing blobs cancel identically.

[O] v14.871 positive frozen-orbit quasistatic transverse coefficient remains a valid restricted result; no full causal retarded kernel, sign-definite physical inertial coefficient, or resonance established. Need complete Maxwell integration including charge density, rotating phases, stabilizing stresses, and charge assignment grounded in the bicone operator model. No new physical gravity monopole or Higgs state inferred.

Flags: Fourier_continuity=EXACT; electric_dipole_rotation_sideband=ABSENT_AT_LEADING_ORDER; finite_size_Larmor_sidebands=PRESENT; magnetic_dipole_rotation=PRESENT; full_frequency_dependent_mass=OPEN; true_resonance=NOT_DERIVED; Higgs_or_Newton_G=NOT_DERIVED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: rotating-larmor-floquet-current
parent: v14.872
status: open
action: Verify Fourier charge/current and continuity, linearization, leading E1 versus higher harmonic sidebands, constant-seat rotating magnetic dipole, and lack of a proven causal physical mass/resonance. Preserve Suzuki/far-tail.
deliverable: scoped verdict.
