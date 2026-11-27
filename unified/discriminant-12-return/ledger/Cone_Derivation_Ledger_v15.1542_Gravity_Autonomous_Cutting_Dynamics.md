# Gravity v15.1542 — Autonomous cutting parameter: bounded Hamiltonian witness and crossing barrier

Date 2026-11-26. Parent v15.1541; Audit Round 668 independently confirmed v15.1540 and v15.1541 (2d1c5a3c5caf446978df7b9d796d75e5c5f4ae2c). Prewrite HEAD 0c6d8279cb03fffdaf14792486a47be3a4cf1685. Additive geometric side gate, no other lanes modified.

## Gates 1435–1437

For fixed lambda the affine generator X''=h+lambda X, X(0)=X'(0)=0 gives Y=X', Y²=2hX+lambda X². Negative, zero and positive lambda yield elliptic, parabolic and hyperbolic phase curves. If lambda varies, I=Y²−2hX−lambda X² obeys I'=-lambda' X². This is prescribed-parameter exchange, not an autonomous action.

Candidate autonomous dimensionless Lagrangian L=(X'²+M lambda'²)/2−V with V=k(lambda−lambda0)²/2+g X⁴/4−hX−lambda X²/2. M,k>0. Equations X''=h+lambda X−gX³; M lambda''=−k(lambda−lambda0)+X²/2. Exact total energy E=(X'²+M lambda'²)/2+V conserved; I'=-lambda' X²−2gX³X'. Quartic stabilization modifies the exact fixed-conic trajectory, so sign lambda labels the *linear coefficient*, not literal instantaneous conic orbit or proven moving physical plane.

Complete square: V=k/2 [lambda−lambda0−X²/(2k)]²+(g/4−1/(8k))X⁴−lambda0 X²/2−hX. Sufficient coercivity g>1/(2k), giving bounded finite-energy trajectories. Without stabilization g=0 this potential is unbounded below. No stability selection of h=1/2 or 1/4 follows.

Numerical witness: M=k=g=1, lambda0=-1/2, initial X=X'=lambda'=0, lambda=lambda0, energy zero. Integrate s=0..20 via scipy solve_ivp rtol 1e-11 atol 1e-13 max_step .03, sample 4001 points. Actual local Python execution, exact symbolic energy and I derivative assertions passed.

| h | min lambda | max lambda | sampled sign crossings | max abs energy drift |
|---|---:|---:|---:|---:|
|1/4|-.7671251111|-.0974217398|0|3.323e-12|
|1/2|-.8140620926|.2883718088|6|1.444e-11|
|1| -1.1049923046|.8042823773|5|6.982e-11|
|2/3|-.5547455380|.4802383958|5|2.745e-11|

Crossing count sampled, not event-certified. These are arbitrary illustrative model coefficients, not inferred from Cone action or physical data. Analytic barrier: at lambda=0, minimum V over X is k lambda0²/2−(3/4)h^(4/3)g^(-1/3) for h>0. Zero-energy crossing requires h≥(2k lambda0²/3)^(3/4)g^(1/4), here (1/6)^(3/4). Thus h=1/4 cannot reach lambda=0 in this chosen model, whereas h=1/2 is energetically permitted; permission is not sufficiency. Threshold varies continuously with coefficients; no universal mesh selector.

Reproducer research-notes/k4_autonomous_cutting_dynamics_v15_1542.py commit 8860cfb0f67bc66db47aae5732c1848b657b7388, same source executed locally /mnt/data/cone_cutting_dynamics.py. Independent Audit pending. Next: determine whether existing action-circle degrees of freedom yield the coupling and stabilizer rather than introducing them, test phase-dependent energy exchange and compare to actual GH tidal observables. No physical G-free prediction. Previous GH subsidiary and N40 gates remain open.