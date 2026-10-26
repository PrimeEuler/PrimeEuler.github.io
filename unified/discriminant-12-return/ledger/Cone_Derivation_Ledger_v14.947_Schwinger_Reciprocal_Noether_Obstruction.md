# Cone Derivation Ledger v14.947 — Schwinger Casimir / reciprocal Noether generator obstruction

Date 2026-10-26. Parents v13.583 Paper C centered oscillator dictionary and v14.944–946 radial-current and factor action. Research note research-notes/Schwinger_Casimir_Reciprocal_Noether_Generator_Obstruction.md commit 394c39283507c8a851789ac3e68b6d5b69fb3aff. Prewrite live HEAD 394c39283507c8a851789ac3e68b6d5b69fb3aff. Owner per-gate preservation active; Suzuki-quarter physical weld PARKED, unrelated Suzuki/far-tail untouched.

[S/D] Schwinger n1,n2 with total N=n1+n2, j=N/2, J_z=(n1−n2)/2 and SU2 C=j(j+1). Exact Paper C factor dictionary x=n1+1,y=n2 yields T=(x+y)/2=j+1/2 and X=(x−y)/2=J_z+1/2, so C=T²−1/4. The j=1 irrep has m=−1,0,1 with SAME Casimir C=2 but distinct J_z charges. [C,H]=0 for generator-algebra Hamiltonians while [J_z,H] requires extra rotational symmetry around z.

[D / OBSTRUCTION] Reciprocal positive-factor scaling (u,v)→(e^αu,e^−αv) preserves uv but not u+v generically: infinitesimal derivative of sum is u−v. In the Paper C x=n1+1,y=n2 dictionary the sum x+y=2j+1 is fixed in one spin-j irrep. Therefore continuous reciprocal scaling does NOT preserve the same SU2 irrep and cannot be equated to Schwinger J_z rotation (which rotates opposite oscillator phases without scaling occupations). A field action with s=1/2ln(u/v) shift symmetry gives Jμ=F(rho)∇μs on-shell (v14.946), but its Noether charge Q is NOT automatically operator SU2 Casimir C, quarter M_F², or J_z. Casimir's central conservation is not a local source flux.

[O] Build canonical/symplectic carrier map and Ward identity to identify Q with a physical oscillator generator, if one exists. An SU(1,1)-type squeeze is a candidate to *investigate*, not an established identification; squeeze on oscillator quadratures does not automatically scale occupation eigenvalues. Q normalization, physical source, G and independent metric selection remain undetermined; Suzuki log(n/4) weld stays parked.

Flags: SU2_Casimir_factor_dictionary=EXACT; Casimir_fixed_does_not_fix_Jz=PROVED; reciprocal_factor_scaling_not_SU2_fixed_j=PROVED; quarter_fixes_spacetime_flux=NOT_DERIVED; physical_gravity=NOT_DERIVED; Suzuki_quarter_weld=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: Schwinger-Casimir-reciprocal-Noether-obstruction
parent: v14.947
status: open
action: Verify exact SU2 factor dictionary, fixed Casimir/different magnetic states example, distinction between inverse-factor scaling and oscillator phase rotation, and lack of derived Noether normalization; independently examine SU11 squeeze as candidate without assuming success.
deliverable: scoped verdict.

NEXT: test canonical SU(1,1) squeeze versus factor-product invariance and explicitly derive its Noether generator; reject if product-preserving scaling is not canonically realized or still does not fix source strength.
