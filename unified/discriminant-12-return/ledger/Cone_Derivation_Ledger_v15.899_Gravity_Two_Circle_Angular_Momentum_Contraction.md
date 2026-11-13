# Cone Derivation Ledger v15.899 — Two-circle angular-momentum contraction and kinetic-energy gain

**Date:** 2026-11-13 US Eastern. **Lane:** Gravity. **Parents:** v15.895–898 two-circle geometry, outer acceleration parabola and conditional SR energy dictionary. **Live HEAD before ledger write:** 9e4b7b302d9273eacbad556f779cadc33e226236. Target path checked absent; additive-only, no historical/Audit/Sandbox/Suzuki objects changed.

**User proposal:** A conserved-angular-momentum skater contracts from the outer n+1 circle to the inner sqrt(n) circle and spins faster. Does this intrinsic mechanism generate acceleration and increased kinetic energy?

**Status:** [D] exact rotational spin-up and work ratios for a specified mass distribution; [C] map geometric Cone radii to *physical lever-arm* radii; [N] conservation does not furnish inward contraction force, rate, or EM/G coupling.

## Gate 573 — exact radius-ratio to spin-up

At normalized shell n>0, sector u>0, with *physical length* conversion ell_*>0, candidate ring radii are r_o=ell_*u(n+1)/2 and r_i=ell_*u sqrt(n), ratio gamma_n=r_o/r_i=(n+1)/(2sqrt(n))=cosh[(ln n)/2]. In a thin rigid ring of constant total mass M with no external axial torque, I=M r², L=I omega is conserved. Thus:

**omega_i/omega_o=I_o/I_i=gamma_n²=(n+1)²/(4n)**.

For n>1 the candidate inward contraction raises omega, with equality n=1. If r(t) is any prescribed smooth contracting radius, **omega_dot=−2omega r_dot/r**. This is angular acceleration caused by contraction, but not a law that determines r_dot. For a different shape I(r)=I_fixed+M r², ratio becomes (I_fixed+M r_o²)/(I_fixed+M r_i²), so gamma_n² requires negligible fixed central inertia and a specified ringlike mass distribution.

## Gate 574 — kinetic-energy, tangential-speed and centripetal ratios

At fixed L, K_rot=L²/(2I), hence

**K_i/K_o=gamma_n²; (K_i−K_o)/K_o=gamma_n²−1=(n−1)²/(4n)=sinh²[(ln n)/2]**.

Tangential speed v_t=L/(Mr), so v_i/v_o=gamma_n. For the associated centripetal acceleration a_c=v_t²/r, **a_c,i/a_c,o=gamma_n³**. These are exact ring-model identities; the acceleration is not automatically the Cone field's radial restoring acceleration.

For n=2,4,9,16, omega and K ratios are respectively 1.125, 1.5625, 25/9≈2.77778, 289/64≈4.515625. The earlier v15.898 conditional SR kinetic excess is **K_rel/(mc²)=gamma_n−1**, NOT gamma_n²−1. This distinguishes two different physical mappings of exactly the same Euclidean radii. Their numerical agreement is not asserted.

Under inward radial displacement, dK_rot/dr=−L²/(M r³). An external/internal constraint must supply inward work; conservation of angular momentum does not provide free spin-up energy. The unconstrained ring effective radial energy at fixed L is U_eff=L²/(2Mr²)+V(r), so without an additional attractive or binding V(r) the centrifugal effect resists inward contraction. Radial motion and possible return oscillations require an independently derived restoring law. A physical velocity-space radius (in m/s) cannot simultaneously serve as the ring's lever arm (in meters) without a length/velocity conversion or separate mapping.

## Gate 575 — selector status / potential physical test

The two-circle pair supplies a *dimensionless* predicted spin-up ratio in the stipulated ring model, independent of u. That follows immediately from angular-momentum conservation and is standard rotor mechanics; it is not yet a new gravity prediction. Neither the rate of contraction nor the actual radial potential, angular phase-locking between circles, Newton G, Compton clock, or an EM/G interaction is fixed.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_two_circle_angular_momentum_v15_899.py`, commit 9e4b7b302d9273eacbad556f779cadc33e226236. Symbolic verification of all main formulae and n-samples passed; independent Audit pending.

**Next gate:** seek a physical radial kinetic term and restoring potential from the frozen Cone/K4 action, then test the Routh-reduced dynamics `M r_ddot=L²/(M r³)−V'(r)`, and compare the resulting time-dependent angular phase against the outer circle's intrinsic acceleration parabola. Require independent velocity/length units and distinguish Newtonian rotor versus relativistic kinematics.

**HANDOFF Audit/Muse:** independently verify gamma², gamma³, the work sign, fixed-core-inertia correction, and the velocity-radius/lever-arm unit fork.
