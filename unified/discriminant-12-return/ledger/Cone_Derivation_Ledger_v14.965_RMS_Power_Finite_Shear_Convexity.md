# Cone Derivation Ledger v14.965 — RMS power analogy and finite-strain mean-gap convexity limit

Date 2026-10-26. Parent v14.964. Research note research-notes/Finite_Shear_RMS_Convexity_and_Electrical_Power.md commit 45558ed68e76bab8f3d8889c2cd9f177e76ea2aa. Prewrite live HEAD 45558ed68e76bab8f3d8889c2cd9f177e76ea2aa. Owner per-gate protocol, additive gravity-only; Suzuki spectral-quarter weld PARKED, protected Suzuki/far-tail untouched.

[D] Ohmic electrical average power <P>=R_el<I²>=R_el I_RMS², <I²>=<I>²+Var(I). Exact mathematical parallel for B eigenvalues is Q_B²=A_B²+Var(λ), J(B)=Var(λ)/(3A_B²). This reveals squared-anisotropy energy term in our elastic action but does NOT identify strain with electrical current or gravitational source power.

[D] On positive-definite volume-preserving family B(s)=β diag(e^{2s},e^−s,e^−s), det B=β³ and t=e^{3s}, J(s)=(t²+2)/(t+2)²−1/3≥0. J''(s)=36 t(−t²+6t−2)/(t+2)^4. Thus J''(0)=4/3 and J(s)=2s²/3+O(s³), positive near isotropy; but becomes NEGATIVE at finite deformation t>3+sqrt7 or 0<t<3−sqrt7. Hence mean-gap shear energy with η>0 is *not globally convex along this natural volume-preserving logarithmic strain path*, despite nonnegative J. Shear J saturates: J→2/3 for t→∞ and 1/6 for t→0.

[I/O] This pathwise nonconvexity is not a demonstration of loss of Legendre-Hadamard rank-one ellipticity or fully coupled gravitational instability; those are distinct tests. Prior local stability window 3/8<η≤3/2 near isotropy remains valid at the established scope. Additional harmonic-mean penalties would be extra model selection, not a deduction from RMS analogy. Charge and physical G unfixed.

Flags: rms_variance_identity=EXACT; RMS_electrical_power_analogy=STRUCTURAL_ONLY; finite_shear_local_curvature=POSITIVE; fixed_volume_logstrain_global_convexity=FALSE; rank_one_ellipticity=OPEN; source_selection=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: finite-strain-RMS-convexity
parent: v14.965
status: open
action: Independently verify t parametrization, d²J/ds² thresholds and small-s coefficient, and distinguish pathwise nonconvexity from rank-one convexity, plus electrical RMS analogy.
deliverable: scoped verdict.

NEXT: genuine finite-deformation rank-one acoustic/Legendre-Hadamard test of full material action; assess separately Sandbox coupled-SVT results before importing any claim.
