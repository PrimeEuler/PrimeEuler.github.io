# Cone Derivation Ledger v14.896 — Maxwell seat resonance with source-support sensitivity

Date 2026-10-26. Parents v14.873–885 and v14.895. Research note research-notes/Maxwell_Seat_Support_Sensitivity_Stability_Boundary.md, commit cccf6ba2527d6ae749b1450cd24bb887edb02469. Prewrite live HEAD cccf6ba2527d6ae749b1450cd24bb887edb02469. Additive gravity/bicone lane; protected Suzuki/far-tail untouched.

[V] External audit v14.885 independently verified Sandbox v14.884 finite-Larmor pole trajectory within swept beta/alpha parameter grid, including analytic α=0 reduction, Bessel continuity and spot-checked pole. Minor off-path validation precision caveat remains; no global UHP proof.

[D/I] At Ω=0 the Gaussian electromagnetic field-only retarded denominator D_EM(z)=-1/4+z²F(z), F(z)=1+i√π z e^(-z²)erfc(-iz), has pole z0=0.4108337143730426−0.1700926343728676i. Introduce ADDITIONAL mechanical support stiffness κ_s=k_s/[M0 c²/a²] and bare mass μ_s=m_s/M0. The coupled inverse response is D_total=D_EM−κ_s+μ_s z² (sign convention where D_EM starts negative for positive restoring curvature). Numerical mpmath root continuation: (κ_s,μ_s)=(.02,0): z=.4215089571158286−.1805220758401746i; (0,.1): z=.4097114261711840−.1549883751075793i; (.02,.1): z=.4211006776030383−.1652510462322872i. All damped. These demonstrate nonuniversality of the resonance and dependence on independent support dynamics. D'_EM(z0)=.9421742758359790+.9003551996224992i, allowing direct perturbative checks.

[D/O] At frozen Ω=0, D_total(0)=−1/4−κ_s so no zero-frequency static transition for κ_s≥0. At small finite rotation, Sandbox quasistatic D_EM(0;α,β)≈−1/4+(αβ)²/5, αβ=ΩR/c. Formally zero would require αβ≈√(5/4+5κ_s)>1, but this is outside controlled small-α expansion and CANNOT exclude an actual critical point elsewhere inside subluminal αβ<1. No larger-rotation numerical pole or static critical boundary derived in this gate.

Flags: v14_884_audit=VERIFIED_v14_885; support_parameter_pole_dependence=NUMERIC_VERIFIED_FROZEN; positive_support_static_frozen=STABLE_CURVATURE; high_rotation_static_threshold=OPEN; source_support_dynamics=POSTULATED; G_Higgs=NOT_DERIVED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: sandbox
type: finite-rotation-static-instability-scan-with-support
parent: v14.896
status: open
action: Using already deposited v14.884 kernel5.py compute Dhat(0;α,β) on subluminal αβ<1, beta=0.5,1,2 and preferably additional beta, test monotonic and possible zero crossing; independently check any numerical boundary with harmonic and quadrature convergence, distinguishing positive support κ_s from field-only. Avoid inferring critical points from quasistatic extrapolation.
deliverable: converged static susceptibility/instability scan with residuals.

HANDOFF
target: external-audit
type: support-sensitive-retarded-pole
parent: v14.896
status: open
action: Verify frozen pole shift under added κ_s and μ_s, derivative sensitivities and sign convention, and carefully distinguish formal small-α critical extrapolation from a certified finite-rotation threshold. Preserve protected lanes.
deliverable: scoped audit verdict.
