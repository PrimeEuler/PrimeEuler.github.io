# Cone Derivation Ledger v15.013 — Corrected ADM infrared multiplier gap

Date 2026-10-27. Parents v14.996 corrected action, v15.011 Hamiltonian and v15.012 External Audit. Research note research-notes/K4_Corrected_Constraint_Infrared_Multiplier_Gap.md commit 982713284024ced102df68b14569ab3b4c4b3caf. Latest HEAD checked before write. Additive gravity only, Suzuki physical quarter weld PARKED; protected other lanes untouched.

[D] Linear ADM Hamiltonian pivot −12H² permits algebraic lapse solving at fixed τ>0 without k⁻², but inverse ∝τ² must be estimated at late times. Corrected fully physical scalar/vector kinetic AS=√3τ³/[54(k²+1)], AV=√3τ³/[18(3k²+4)] have positive finite k→0 limits. These are kinetic coefficients, NOT certified determinant factors for the raw constraint operator.

[D] Corrected vector auxiliary V=4√3τ dotπT/(9k³+12k) yields kV=4√3τ dotπT/[3(3k²+4)] and explicit bound |kV|≤τ|dotπT|/√3 at every k≠0, with finite formal k→0 multiplier. In logarithmic time τdotπ=∂sπ. This controls a differentiated shift but not undifferentiated V or homogeneous gauge sector.

[O] Second-order sources including bilinear p2 and gravity Π∂h may lack output-K factors; full gauge-fixed coupled scalar/shift/Hamiltonian quadratic constraint matrix and time-weighted nonlinear convolution estimates remain OPEN. Linear positive denominators do not imply fully nonlinear uniform inverse bounds or future stability.

Flags: linear_lapse_pivot=NONZERO_FOR_TAU_POSITIVE; vector_differentiated_shift_bound=EXACT; scalar_reduced_IR_kinetic=FINITE_POSITIVE; raw_scalar_constraint_det=NOT_DERIVED; nonlinear_joint_constraint_IR=OPEN; future_global_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: corrected-linear-ADM-infrared-multiplier-gap
parent: v15.013
status: open
action: Verify vector kV denominator and bound against v14.996, distinguish reduced kinetic factors from raw constraint determinant, and confirm late-time and k=0 caveats.
deliverable: scoped verdict.

NEXT: independently reconstruct gauge-fixed scalar constraint auxiliary matrix from machine-built corrected action and test uniform low-k inverse on actual second-order sources, with a fixed topology/gauge.
