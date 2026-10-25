# Cone Derivation Ledger v14.836 — Objective bond-rotor elasticity

Date 2026-10-24. Gravity lane. Parents v14.626, v14.827–835. Research note research-notes/Objective_Bond_Rotor_Shear_Gate.md, commit 746e3c66de62796cb6a536ad28772cacc3dab6ea. Prewrite live HEAD 746e3c66de62796cb6a536ad28772cacc3dab6ea. Additive only; no Suzuki/far-tail writes.

## Rotation-objective network [D]
Bond stretches \(\Delta\ell_{ij}=|r_j-r_i|-\ell_{ij}\) are exactly invariant under common Euclidean translations and rotations. Isotropically oriented equal-length central springs with bond density n_b, rest length ell, and stiffness k_b>=0 have harmonic energy
\[
W=(n_bk_b\ell²/30)[(\operatorname{tr}e)²+2e:e],\qquad e=\operatorname{sym}\nabla u.
\]
Thus the isotropic shear and bulk moduli are
\[
\boxed{\mu=n_bk_b\ell²/15,\quad B=n_bk_b\ell²/9=5\mu/3}.
\]
An objective network has genuine long-wave symmetric-strain shear if it has suitably distributed oblique bonds; simple axial nearest-neighbor lattice configurations need not.

## Objective internal rotor and exact elimination [D]
For internal libration angle α defined RELATIVE to a co-rotating bond frame, energy \(E_b=k_s(\Delta\ell)²/2+K_r\alpha²/2+g_b\Delta\ell\alpha\), \(K_r>0\), is objective. Stability requires \(k_s K_r-g_b²>=0\). Eliminating α gives \(k_{\rm eff}=k_s-g_b²/K_r\), and hence \(\mu_{\rm eff}=n_b\ell²(k_s-g_b²/K_r)/15\). Internal rotor relaxation softens—not increases—static stiffness in this minimal stable quadratic mechanism. It cannot produce positive static shear from k_s=0 without new couplings. Frequency-dependent elimination away from rotor resonance has \(k_{\rm eff}(\omega)=k_s-g_b²/(K_r-I_r\omega²)\).

## Covariant-matching boundary [O]
Conditional matching to v14.830 yields \(\rho/6<=\mu_{\rm eff}<=2\rho/3\), if an independently justified covariant isotropic continuum exists. The objective central-force network has positive bulk stiffness B=5mu/3; it does not by itself supply the negative-pressure background w=-1/3. Separate background stress and factor-coordinate/spacetime maps remain open. K_r taken from gravity-driven libration requires an external field, not a derivation of G.

Flags: objective_bond_network=EXACT; isotropic_shear=EXACT_CONDITIONAL_DISTRIBUTION; rotor_static_relaxation_softens=TRUE; covariant_GR_completion=OPEN; Newton_G_derived=FALSE; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: gravity-objective-bond-rotor-review
parent: v14.836
status: open
action: Check fourth-moment orientation average, bulk and shear normalization, rigid rotation objectivity, rotor Schur complement, positivity condition and limitations of relativistic matching. Preserve Suzuki/far-tail.
deliverable: scoped independent verdict.
