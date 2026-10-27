# Cone Derivation Ledger v15.001 — Corrected ADM infrared shift cancellation, nonlinear constraint gap

Date 2026-10-27. Parent v14.996, v14.998, v15.000. Research note research-notes/K4_Corrected_ADM_Infrared_Shift_Regularity.md at commit 8b5bc2f1202910bc974c7e191d4fc56cc2ecd239. Live prewrite HEAD 8b5bc2f1202910bc974c7e191d4fc56cc2ecd239. Read corrected v14.996 reconciliation payload. Suzuki physical-quarter weld PARKED; unrelated lanes untouched.

[D] From corrected v14.996 reduced SVT coefficients: A_S=√3τ³/[54(k²+1)] and A_V=√3τ³/[18(3k²+4)]. Their formal k→0 limits √3τ³/54 and √3τ³/72 finite and positive, so there is no IR pole in either corrected physical quadratic kinetic coefficient. k=0 separate global/gauge caveat. Corrected vector shift V=4√3τ dotπ_T/(9k³+12k) formally diverges as 1/k, but its spatial derivative kV=4√3τ dotπ_T/(9k²+12) bounded at k=0; this is a concrete differentiated ADM-constraint cancellation, not proof all gauge components bounded.

[OPEN] True second-order ADM Hamiltonian/momentum sources involve Fourier convolutions, potentially with output k→0 even for finite nonzero input momenta. Linear cancellation of kV does not establish quadratic source divisibility by k², all-shift invertibility, or nonlinear log-time energy decay. Need compute explicit second-order source in a fixed regular gauge; do not promote global nonlinear stability.

Flags: corrected_scalar_kinetic_IR=FINITE_POSITIVE; corrected_vector_kinetic_IR=FINITE_POSITIVE; differentiated_vector_shift_IR=BOUNDED; raw_vector_shift_IR=ONE_OVER_K; second_order_constraint_IR=OPEN; global_nonlinear_future_stability=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: corrected-ADM-infrared-constraint-cancellation
parent: v15.001
status: open
action: Verify finite reduced kinetic limits and differentiated vector shift expression against v14.996; assess zero-mode exceptions and warn against extending linear IR cancellation to second-order convolutions.
deliverable: scoped verdict.

NEXT: derive concrete quadratic Hamiltonian/momentum constraint source (machine Christoffels and full inverse metric, v14.996 lesson), check whether its output low-k component is suppressed by momentum factors and whether constraints control all required derivatives.
