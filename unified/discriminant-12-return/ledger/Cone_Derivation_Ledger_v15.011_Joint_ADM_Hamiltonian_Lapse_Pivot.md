# Cone Derivation Ledger v15.011 — Joint Hamiltonian–momentum constraints and regular lapse pivot

Date 2026-10-27. Parent v15.010. Research note research-notes/K4_Joint_ADM_Hamiltonian_Momentum_Lapse_Pivot.md committed 133cabce81ea0dc95533a1b91a18e6f1b08e3d78. Prewrite live HEAD 133cabce81ea0dc95533a1b91a18e6f1b08e3d78. Additive gravity only; unrelated Muse, Suzuki/far-tail untouched, physical quarter weld PARKED.

[D] Exact Hamiltonian constraint R3+K²−KijKij=2κρ_n with ρ_n=(C/3)Σ[(dotφI−N^j∂jφI)²/N²+h^ij∂iφI∂jφI]. Canonical momentum constraint H_i=−2hijDkΠjk+pI∂iφI=0 from v15.003/010. On coasting background a=τ/√3, φI=zi, κC=1, linear ADM perturbations h=a²(δ+ε), N=1+α, contrav N^i=β^i, φ=zi+π have
H_GR(1)=a^-2(∂i∂jεij−Δtrε)+2Hdot(trε)−4H divβ−12H²α−4H²divπ+2H²trε=0.
Lapse coefficient -12H² nonzero for τ>0; solving linear lapse does not demand division by k². The same coefficient of α2 appears in degree-two Hamiltonian equation, with additional known bilinear sources and unknown second-order spatial metric/scalar/shift. This is a scoped algebraic lapse pivot, NOT proof of joint gauge-fixed constraint invertibility or time-uniform bounds.

[OPEN] Need explicit full degree-two curvature/extrinsic/matter source, combined scalar+vector constraint inversion and low-K weighted norms; H→0 at late times means inverse lapse coefficient ∝τ² can still obstruct future bootstrap. Zero mode and noncompact-gradient boundary conditions remain delicate. Full nonlinear future stability NOT DERIVED.

Flags: Hamiltonian_constraint_exact=YES; linear_Hamiltonian_formula=DERIVED; lapse_pivot_minus_12H2=NONZERO_TAU_POSITIVE; scalar_shift_IR_inverse_bound=OPEN; quadratic_joint_constraints=NOT_FULLY_REDUCED; future_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: joint-ADM-hamiltonian-lapse-pivot
parent: v15.011
status: open
action: Check Hamiltonian sign/convention, scalar normal density, linear curvature/extrinsic terms and -12H² lapse pivot, and flag time-dependent inverse and unproved complete constraint inversion.
deliverable: scoped verdict.

NEXT: build full gauge-fixed scalar/vector ADM constraint matrix and compute elliptic low-momentum weighted estimates, checking sources and homogeneous modes rather than only algebraic α.
