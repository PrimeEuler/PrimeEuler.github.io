# Cone Derivation Ledger v14.948 — SU(1,1) canonical squeeze bridge: passed kinematics, failed automatic source selection

Date 2026-10-26. Parents v13.583, v14.944–947. Research note research-notes/SU11_Canonical_Squeeze_Reciprocal_Factor_Noether_Test.md commit 8cc1fb1760b5386d24a15660e3e1ff6af7516575. Live prewrite HEAD 8cc1fb1760b5386d24a15660e3e1ff6af7516575. Owner ledger every substantive gate; additive gravity only, Suzuki-quarter physical weld parked; no Suzuki/far-tail modification.

[D] A genuine unitary symplectic reciprocal dilation exists. Let [q,p]=iℏ, D=(qp+pq)/2, U(α)=exp(−iαD/ℏ). Then U†qU=e^αq and U†pU=e^−αp, preserving [q,p], and D is invariant under its generated transformation. In the standard one-oscillator metaplectic su(1,1) algebra K0=(q²+p²)/(4ℏ), K1=(q²−p²)/(4ℏ), K2=D/(2ℏ), the quadratic commutators close su(1,1), Casimir K0²−K1²−K2²=−3/16 (Bargmann k=1/4 or 3/4). These are NOT the Schwinger SU2 Casimir j(j+1), nor the centered +1/4 offset itself.

[D / key obstruction] A unitary generator of a transformation need not commute with the physical Hamiltonian. For Hosc=(p²+q²)/2, [Hosc,D]=iℏ(q²−p²)≠0, so D is NOT conserved. Moreover (q,p) are noncommuting canonical variables, not positive commuting Cone factor fields or Schwinger occupation eigenvalues. Thus the action-derived factor-field shift Noether current Jμ=F(ρ)∇μs in v14.946 has not been shown to be the spacetime localization of D. No Ward map or physical Q normalization/κ/G follows from the SU11 algebra. PASS: exact reciprocal canonical realization. OPEN: conserved physical gravitational source, physical carrier map and charge quantization.

[O] Next test whether a canonical transformation can identify factor-space log-ratio s with a squeeze coordinate and show π_s=D (or prove obstruction) while preserving symplectic form, positive domain and state-space interpretation. Need independently selected scale-symmetric action, local current and coupling to stress-energy before asserting gravitational source. Distinct from parked Suzuki-quarter identification.

Flags: SU11_reciprocal_canonical_dilation=EXACT; squeeze_generator_D=EXACT; SU11_Casimir=minus_3_over_16_in_metaplectic_rep; D_conserved_under_Hosc=FALSE; D_equals_factor_field_Noether_charge=NOT_DERIVED; gravitational_flux_strength=NOT_FIXED; Newton_G=NOT_DERIVED; Suzuki_quarter_weld=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: su11-canonical-squeeze-vs-Noether-charge
parent: v14.948
status: open
action: Check symplectic/unitary squeeze conjugation, su11 algebra and its −3/16 Casimir with explicit conventions, harmonic-oscillator commutator, and why neither D conservation nor identification with a spacetime reciprocal-factor Noether current is automatic. Preserve parked Suzuki-quarter work.
deliverable: independent scoped verdict.

NEXT: explicit canonical (ρ,s) or product/log-ratio factor map and momentum; test relation to squeeze D and current Q, with microscopic state-space guardrails.
