# Cone Derivation Ledger v15.057 — BLOCKER: scalar ADM gauge constraint / wave mismatch

Date 2026-10-28. Gravity parents v15.038, v15.049, v15.053; certified reference v14.996. Research note research-notes/K4_Scalar_ADM_Wave_Constraint_Compatibility_Blocker.md commit e552af6ec9ac1504af779688116baf250bebc945. Prewrite live HEAD e552af6ec9ac1504af779688116baf250bebc945. Protected Lane A and Sandbox untouched. Suzuki physical-quarter weld PARKED.

[X] Independently substituted the v15.038/v15.049 scalar-gauge ADM constraints, a=t/√3,H=1/t,p=Δσ,S=dotσ−b:
 (1−Δ)S=−dot p−Hp+3Hψ−Δψ/(a²H),
 α=dotψ/H+S/(3H),
into the v15.053 canonical scalar wave
 ∂t(a³S)−a(p+α+ψ)=0.
For k≠0 and Δ→−k², exact symbolic simplification yields residual
 −√3*t/[9(k²+1)] [t² pdd+3t pd−(3k²+2)p]=0.
This would require pdd+3/t pd−(3k²+2)/t² p=0, versus corrected v14.996 source-certified strain oscillator pdd+3/t pd+(3k²+4)/t² p=0. Potentials differ by 6(k²+1)/t², so these equations cannot simultaneously hold for identical physical strain variable. The contradiction is exact and independent of ψ since it cancels. It is NOT evidence of an actual corrected v14.996 ghost; it diagnoses a gauge/sign/convention/source mismatch in subsequent derivations.

[BLOCK] Suspend joint use of v15.038, v15.049, v15.053 to claim a physical ψ reconstruction or constraint-induced normal-velocity cancellation sufficient for the actual Einstein triplet energy until a single convention-consistent independently machine-built unreduced ADM action rederives all equations. Previously asserted componentwise algebra remains recorded but joint physical identification is not certified. No new uniform infrared estimate or nonlinear stability theorem.

Flags: scalar_constraint_wave_consistency=FAILED; exact_residual=NONZERO; psi_reconstruction=BLOCKED; v14_996_corrected_linear_stability=NOT_OVERTURNED; physical_IR_normal_velocity_bound_from_inconsistent_chain=UNVERIFIED; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: sandbox, external-audit
type: scalar-gauge-ADM-source-sign-reconciliation
parent: v15.057
status: blocker
action: Independently reproduce both expressions above; trace to v14.996 machine-Christoffel ADM action and source ansatz, reconcile gravitational/matter sign and Pi convention, full shift g^ij term, correct the first faulty equation, then output exact psi_sol, psid_sol, original EL residuals and k→0 bounds. Do not assume contradiction invalidates original v14.996 independent stability.
deliverable: exact corrected joint equations with zero residual and coefficient-wise psi reconstruction.

NEXT: resolve blocker before further promotion.
