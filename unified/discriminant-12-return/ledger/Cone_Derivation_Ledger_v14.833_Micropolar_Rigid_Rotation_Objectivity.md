# Cone Derivation Ledger v14.833 — Full constitutive mismatch under rigid rotation

Date 2026-10-24. Parents v14.829–832; independent audit Round 348 verified previous three gates. Research: research-notes/Micropolar_Objectivity_Full_Constitutive_Obstruction.md commit 51e37821be9ffc5a1890bd53c004bb7baad88a57. Additive gravity lane only; Suzuki/far-tail untouched.

[D] For the micropolar potential \(W=B(\mathrm{div}u)^2/2+\mu_0|\mathrm{dev\,sym}\nabla u|²+\gamma|\mathrm{curl}u-2\theta|²/2+K|\theta|²/2+A|\nabla\theta|²/2\), set \(u=\Omega\times x\). The symmetric strain vanishes but \(\mathrm{curl}u=2\Omega\). Minimizing in uniform \(\theta\) gives \(\theta_*=4\gamma\Omega/(4\gamma+K)\) and \(W_{\min}=2\gamma K|\Omega|²/(4\gamma+K)\). Thus for \(\gamma K>0\) the rotor's extra curl stiffness penalizes pure rigid rotation and cannot be the symmetric-strain shear modulus of the v14.830 isotropic covariant q-solid. The earlier v14.831 matching is valid for an individual transverse plane-wave coefficient only, not the complete constitutive tensor. Such orientation resistance is physically meaningful when an external pinning field is present; it is not intrinsic free-solid shear.

[O] Seek objective rotation-symmetric completion or explicitly retain a preferred external direction in a covariant material model. No physical G inferred.

Flags: rigid_rotation_residual=EXACT; full_isotropic_constitutive_match_for_K_positive=FAIL; scope=SPECIFIED_MICROPOLAR_ACTION_ONLY; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.