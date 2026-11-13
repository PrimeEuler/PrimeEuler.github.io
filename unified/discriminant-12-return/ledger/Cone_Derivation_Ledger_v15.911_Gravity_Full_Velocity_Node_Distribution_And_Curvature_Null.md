# Cone Derivation Ledger v15.911 — Full velocity-node distribution, coherent dark node, and curvature-null comparator

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** Paper C SU(2) Fock dictionary, Sandbox diameter–secant machine, Gravity v15.884–885 SI velocity axis, Gravity v15.906–910 multi-rung amplitudes, local product-circle curvatures and conditional dynamics. **Live HEAD immediately before ledger write:** e3707e58e779dc0ca0d24df5158924ac8625efa6. Target path checked absent. Strict additive-only, no older certified/Audit/Sandbox/Suzuki content changed.

**Question:** Under a physically calibrated m/s X axis and an explicit transverse EM/tidal coupling, how does the *entire* fixed-diameter velocity-node ladder evolve? Does each `sqrt(nk)` local action circle/parabola introduce any dynamical effect beyond ordinary SU(2) transition amplitudes?

**Status:** [D] exact finite-dimensional unitary SU(2) dynamics and velocity-node probabilities; [N] full numerical checks and a non-SU(2) comparator; [N] no independent curvature-selected coupling/clock; [O] on-shell K4/Maxwell field interaction producing any nonstandard link weighting.

## Gate 612 — all nodes in a single dynamical model

Fix a diameter D=n+k, u>0 measured in **m/s** and Paper C's D states `|a,D−1−a>`, a=0..D−1. Physical velocity-label operator is **Xhat=u(J_z+1/2)** with eigenvalues **v_a=u[a−(D−2)/2]**. Adjacent nodes are uniformly separated by **u**. Transition link `a→a+1` has geometric local action-circle radius **R_a=u sqrt[(a+1)(D−a−1)]**; its normalized Schwinger coefficient is `R_a/u`. The link is an edge of the state graph; it is not itself a measured acceleration, a spatial lever arm, or a temporal period. The endpoint link degenerates at k=0.

With a single *externally sourced* transverse interaction **H=hbar g J_x** and dimensionless time **tau=g t**, the complete probability at velocity node a is

**P_a(tau)=|<a| exp(−i tau J_x)|a_0>|²**.

Every transition is included; the evolution is strictly unitary and preserves D and probability. Magnetic J_y instead of J_x gives exactly the same probabilities for a single initial J_z number state; this follows from a diagonal azimuthal basis rotation (their complex amplitudes differ). A distinguishable magnetic/tidal relative phase requires a second reference or a simultaneous noncommuting drive.

## Gate 613 — D=5, initial pair (4,1): interference and exact revival

Set D=5, a_0=3, Fock |3,1> corresponding to Cone pair (4,1), whose X=1.5u and outgoing raising amplitude is sqrt4=2. In ascending a order the five Cone pair labels are **(1,4), (2,3), (3,2), (4,1), (5,0)** and their velocities are **−1.5u, −0.5u, 0.5u, 1.5u, 2.5u**. At selected tau values, the exact populations are:

- tau=0: **(0,0,0,1,0)**.
- tau=pi/2: **(1/4,1/4,0,1/4,1/4)**. In particular the central (3,2) node is **dark** despite its geometric local radius sqrt6 u being nonzero.
- tau=pi: **(0,1,0,0,0)**: mirrored state (2,3) with velocity −0.5u.
- tau=2pi: **(0,0,0,1,0)**, exact probability revival (state may acquire a spin-dependent global phase).

At tau=pi/4, numerically **(0.0107233047,0.125,0.375,0.125,0.3642766953)**. Every normalized distribution conserves total probability. The dark node at tau=pi/2 is standard coherent SU(2) interference; it is not an inferred gravity resonance or evidence that the (3,2) product circle vanishes.

Exact mean velocity in this model is

**<X>(t)/u=1/2 + [a_0−(D−1)/2] cos(gt)=1/2+cos(gt)**

for D=5 and initial a_0=3, consistent with v15.910. Important physical distinction: the continuous mean arises from quantum superposition/ensemble readout over discrete velocity-labelled basis states, not from a classically moving particle traversing every node at a deterministic rate.

## Gate 614 — curvature weighting test and positive/negative discrimination

All link strengths **sqrt[(a+1)(D−a−1)]** are exactly ordinary SU(2) amplitudes and are also normalized local product-circle radii. The local geometric osculating curvature varies as **1/[u sqrt((a+1)(D−a−1))]**; this does not add an independent term to H=hbar g J_x. Consequently, *under the physical comparator supplied*, there is **no additional Cone curvature dynamical signal beyond standard angular-momentum algebra**.

As a diagnostic, we deliberately perturb each link coefficient by the Hermitian factor

**w_a = 1 + epsilon (1/sqrt[(a+1)(D−a−1)] − 1/2)**,

using epsilon=0.15 for D=5. This is merely an **arbitrary hypothetical curvature-dependent Hamiltonian**; it is NOT derived from K4, general relativity, a local action, or the velocity-axis units. At tau=pi/2, it yields a nonzero central-node population approximately **0.000390086394** instead of the exact SU(2) zero. Thus the node is a sensitive *null comparator* for non-SU(2) link structures, but no prediction of epsilon is made, and other ordinary perturbations can also lift the dark node. An observation alone would not establish novel gravity.

The period remains T=2pi/g (probability revival for any integer/half-integer j), requiring independent g in s^-1. Rescale g→s g: all same velocity nodes, local circle radii, curvatures and probability functions of tau survive, but laboratory timing scales by 1/s. The real units on X do not themselves select physical acceleration or frequency.

## Gate 615 — verification and next gate

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_full_velocity_ladder_distribution_v15_911.py`, commit e3707e58e779dc0ca0d24df5158924ac8625efa6. Local Python/SciPy checks executed with PASS for D=2,3,4,5,7,10; 51 phases per shell, commutator, normalization to 1e−12, equivalence J_x vs J_y probabilities, exact mean waveform, 2pi probability revival, exact D=5 dark distribution and mirrored state, and the arbitrary Hermitian perturbation's dark-node lifting. Independent Audit pending.

**NEXT:** Require the original K4/Maxwell or GR tidal field action, detector physical coordinates, and a specified source to derive g and/or a real non-SU(2) correction to w_a. Compare field-induced transition observables at independently calibrated g against ordinary Wigner D-matrix predictions, retaining both the outer-circle crown parabola and the link-local rest-circle parabolas as distinct geometric constructions. No Cone-specific dimensionless gravity prediction or intrinsic n+1 physical frequency is yet established.

**HANDOFF Audit/Muse:** independently check D=5 exact probability vector at pi/2, index/velocity centering shift X=u(Jz+1/2), state mirror at pi, and the fact that local circle nonzero curvature does not prevent a coherently dark node. Existing Audit Round571 missing standalone reproducibility scripts v15.888,890,895,897 remain open.
