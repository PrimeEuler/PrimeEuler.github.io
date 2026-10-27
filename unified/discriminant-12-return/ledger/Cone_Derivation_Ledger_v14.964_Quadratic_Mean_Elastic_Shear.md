# Cone Derivation Ledger v14.964 — Quadratic mean gap exactly equals elastic shear J

Date 2026-10-26. Parent v14.962, historical elastic-source v14.925–928 and current independent Sandbox scalar robustness return v14.963 (not modified). Research note research-notes/Quadratic_Mean_Gap_Exact_Elastic_J_Identity.md committed fd08acbfff5f3cfec5283081529e6de6a94a6254. Prewrite live HEAD fd08acbfff5f3cfec5283081529e6de6a94a6254. Owner additive ledger every gate; Suzuki-quarter physical weld PARKED; protected Suzuki/far-tail untouched.

[D] For positive-definite 3x3 material B with eigenvalues λ_i, arithmetic A=trB/3 and quadratic mean Q=sqrt(trB²/3). Previously used K4 elastic shear invariant J(B)=tr(B²)/(tr B)²−1/3 IDENTICALLY equals (Q²−A²)/(3A²). Therefore J≥0 (RMS-AM inequality), equality at λ1=λ2=λ3. This is exact globally on SPD B, not just perturbative. General n×n identity J_n=(Q²−A²)/(n A²). For original two-factor Cone with positive pair a,b, Q²−A²=((a−b)/2)²=X². These are structural relationships between mean dispersion and shape anisotropy.

[D] At B=β(I+E), trE=0, J=trE²/9 exactly. More generally J=[trE²−(trE)²/3]/9+O(E³). Thus the elastic material model S_m=−∫√−g C b^(2/3)(1+ηJ), b=√det B, has an *exact normalized RMS-AM gap* shear energy factor. η>0 penalizes anisotropy at fixed b locally; neither J≥0 nor the mean inequalities select η or establish full physical stability. Prior positive local elastic acoustic window 3/8<η≤3/2 and full-SVT open are separate dynamical claims. Source model is constructed, not uniquely enforced by Cone.

[O] Compare mean-gap energy convexity, local phonon principal speeds and full gravity SVT stability under exact fixed-determinant deformation. Check whether additional physical principle selects η; do not infer gravitational charge or Newton G from algebraic mean identities.

Flags: quadratic_mean_equals_shear_J=EXACT; J_nonnegative_for_SPD_B=TRUE; small_shear_coefficient=one_ninth_trace_E_squared; eta_selected_by_means=FALSE; full_SVT_healthy=OPEN; Newton_G=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: quadratic-mean-elastic-shear-identity
parent: v14.964
status: open
action: Independently verify J=(Q²−A²)/(3A²), general n identity, traceless perturbation factor 1/9, sign/normalization against elastic v14.925–928 and confirm mean inequality does not select η.
deliverable: scoped verdict.

NEXT: test finite-strain convexity and source stability of RMS-gap shear energy at fixed determinant; separately monitor full-SVT Sandbox scalar-sector robustness outcome.
