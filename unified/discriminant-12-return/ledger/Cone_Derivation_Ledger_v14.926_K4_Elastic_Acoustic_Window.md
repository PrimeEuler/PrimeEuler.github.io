# Cone Derivation Ledger v14.926 — K4 elastic modulus and acoustic stability interval

Date 2026-10-26. Parents v14.818, 820–825, 916–925. Research note research-notes/K4_Elastic_Shear_Modulus_Acoustic_Window.md commit 7614d99ba3a50f3c92a82c89deb066b35b66e7db. Live prewrite HEAD 7614d99ba3a50f3c92a82c89deb066b35b66e7db. Owner ledger-every-substantive-gate protocol; additive gravity only; Suzuki quarter parked, Suzuki/far-tail untouched.

[D] For matter rho(B)=C b^(2/3)[1+ηJ], J=tr(B²)/(tr B)²−1/3=tr(B_dev²)/(tr B)², at isotropy B=B0(I+2ε+O(ε²)), exact quadratic expansion J=(4/9)tr ε_dev²+O(ε³). At fixed volume the shear energy has conventional coefficient μ=(4/9)rho η. The same flat linearly-coasting four-factor background p=−rho/3 holds for every η; no symmetry has selected η.

[D, conditional high-frequency elastic-acoustic standard model] For isotropic barotropic elasticity rho+p=2rho/3 and dp/dρ=−1/3, transverse and longitudinal principal sound squares are c_T²=μ/(rho+p)=2η/3 and c_L²=dp/dρ+4μ/[3(rho+p)]=−1/3+8η/9. Necessary strict positive/sub-luminal acoustic interval 3/8<η≤3/2. For example η=3/4 gives c_T²=1/2 and c_L²=1/3. This resolves the *local principal-gradient* obstruction of fluid η=0 by adding shear response, but only as a parametrized candidate. No full coupled gravity+elastic scalar/vector/tensor Hamiltonian analysis, gauge constraint algebra, global cosmological stability, microcausality, or observational viability proved.

[O] The elastic coupling η, gravitational κ and physical factor-coordinate interpretation still unfixed. Next test: derive complete perturbation theory and seek an independently selected η from factor geometry rather than treating acoustic admissibility as value selection. Pantheon+ full covariance from v14.923 still open.

Flags: shear_expansion=EXACT; mu_over_rho=(4_over_9)_eta; cT2=(2_over_3)_eta; cL2=minus_one_third_plus_(8_over_9)_eta; high_k_acoustic_window=(3_over_8,3_over_2]; full_gravity_matter_stability=OPEN; eta_selected=FALSE; G_derived=FALSE; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-elastic-acoustic-interval
parent: v14.926
status: open
action: Recompute quadratic trace invariant J at isotropy including strain normalization, derive μ/ρ and cT²,cL² from relativistic elasticity independently, test admissible endpoints and scope. No Suzuki/far-tail edits.
deliverable: scoped verdict.

NEXT: full coupled perturbative ghost/gradient/constraint test and search for extra physical principle fixing η; separately wait for official Pantheon+ covariance likelihood.
