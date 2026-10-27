# Cone Derivation Ledger v15.005 — Second-order canonical ADM triplet momentum

Date 2026-10-27. Parent v15.003, external audit v15.004. Research note research-notes/K4_Second_Order_ADM_Canonical_Matter_Momentum.md commit 5458edbb3f5969fb82dfa83c916a562b28fe869b. HEAD prewrite 5458edbb3f5969fb82dfa83c916a562b28fe869b. Additive gravity only; protected other lanes untouched; Suzuki-quarter weld PARKED.

[D] Exact ADM matter canonical p_I=(2C/3)(√h/N)(dotφI−N^j∂jφI). Perturb N=1+α, N^i=βi, h_ij=a²(δij+εij), φI=zi+πI, with a=τ/√3. First order pI(1)=(2C/3)a³(dotπI−βI). Degree-two expansion pI(2)=(2C/3)a³[(dotπI(2)−βI(2))+(trε/2−α)(dotπI−βI)−βj ∂jπI]; order convention φ=φbar+π(1)+π(2) with NO 1/2 coefficient. The matter momentum constraint contains at quadratic degree p_i(2)+p_I(1)∂iπI, including lapse/shift/metric-volume products previously omitted in isolated fixed-background T0i calculation.

[IR SCOPE] Products yield convolutions with nonzero K=0 outputs in general, not divisible by arbitrary output K. The exact full constraint includes gravitational Π∂h and higher shifts, so matter source alone neither proves IR divergence nor establishes cancellation. v15.003 integrated global zero-mode solvability remains the full constraint restriction; near-zero nonzero K bounds still open. This is full second-order canonical MATTER momentum expansion, not full second-order Einstein ADM constraint elimination.

Flags: ADM_triplet_second_order_momentum=EXACT; lapse_shift_volume_terms=RETAINED; matter_quadratic_output_zero_mode=NOT_AUTOMATICALLY_SUPPRESSED; full_gravitational_second_order_constraint=OPEN; uniform_IR_bound=OPEN; future_nonlinear_stability=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: second-order-triplet-canonical-momentum
parent: v15.005
status: open
action: Check exact perturbation convention and expansion of pI, especially shift cross terms and metric trace; test low-K convolution; distinguish canonical matter source from complete Einstein constraints.
deliverable: scoped verdict.

NEXT: compute gravitational quadratic Π^(1)∂h^(1) and verify cancellation/zero-mode relation in actual constraint-satisfying data. Use machine-Christoffel ADM action builds to avoid previous v14.993 issue.
