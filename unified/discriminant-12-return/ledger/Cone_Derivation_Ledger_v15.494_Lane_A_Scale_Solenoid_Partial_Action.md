# Cone Derivation Ledger v15.494 — Lane A exact scale-solenoid partial action

**Timestamp:** 2026-11-06 21:41 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact partial-action groupoid base constructed; full signed operator membership and norm remain open

## Fresh state and audit

Live master, new commits, complete relevant ledger entries, ownership, frozen witnesses, and CI were checked before selecting this gate and immediately before every additive write. External Audit Round 507/v15.493 was read in full. It independently verified v15.491 and v15.492, including full Gram matrices, full projection idempotency, all tested refinement indices, the exact step-kernel identity, hashes, and replay. It made no correction and confirmed the v15.490 orphan requires no action.

No duplicate scale-solenoid partial-action construction or active owner was found. v15.494 was next-free. No CI status or workflow run is attached.

## Compact scale space

Define the compact scale space

T = {0} union {2^(−a) : a is a nonnegative integer}.

The physical annulus a is represented by t_a = 2^(−a), and t_a converges to the boundary point 0. Let Sigma be the four-torus natural-extension solenoid from v15.477, and let S be its shift automorphism.

Set X = T times Sigma and define

alpha(t,z) = (t/2, S z).

The range is X_1 = (T without {1}) times Sigma. Since every finite initial subset of T consists of isolated points, X_1 is clopen. Alpha is a homeomorphism from X onto X_1, with inverse

alpha_inverse(t,z) = (2t, S_inverse z)

defined exactly on X_1.

For n ≥ 0, alpha_n maps X homeomorphically onto

X_n = (T without {1, 1/2, ..., 2^(−n+1)}) times Sigma.

For n < 0, alpha_n is the corresponding inverse map with domain X_(−n). These maps satisfy the partial-action composition law wherever both sides are defined. They therefore define the canonical partial transformation groupoid for a partial Z-action on X.

## Physical and boundary orbits

Starting from scale 1, the forward orbit is exactly

(1,z), (1/2,Sz), (1/4,S^2 z), ...

Thus the groupoid carries precisely the nonnegative physical annuli and introduces no fictitious negative-scale fibers.

The boundary is invariant:

alpha(0,z) = (0,Sz).

Consequently the asymptotic large-annulus system is the solenoid automorphism itself, while the interior orbit retains the absolute scale coordinate required by v15.485.

On the Pontryagin dual Z[1/2]^4, pullback under S^n is multiplication by 2^n. The exact witness verifies this composition law for positive and negative n using rational dyadic labels.

## Continuous constant-Hankel coefficient field

For annulus offset d and x,y in [1,2], the squared rescaled constant-Hankel coefficient from v15.485 is

K_d(t;x,y)^2 = 2^d divided by 4 times (x + 2^d y − t)^2.

This is continuous on T, including t=0. Writing B = x + 2^d y and c = 2^d/4 gives the exact positive difference

K_d(t;x,y)^2 − K_d(0;x,y)^2
= c t (2B − t) divided by ((B − t)^2 B^2).

Hence the physical coefficients decrease monotonically to the boundary coefficient as a tends to infinity. The boundary is not an ad hoc approximation: it is the invariant groupoid fiber at t=0.

Together with v15.491, this supplies:

- a common exact Hilbert fiber for all annulus dimensions;
- an exact partial dynamical system carrying scale and solenoid phase together;
- a continuous constant-Hankel coefficient field with the correct physical orbit and boundary limit.

It does not yet prove that every signed prime step-kernel block forms a continuous or compactly supported section of the associated operator bundle. Therefore it does not yet place the full signed 45-diagonal operator in a completed groupoid algebra or evaluate its norm.

## Exact replay

Witness: research-notes/lane_a_v15_494_scale_solenoid_partial_action.py  
Commit: fc56f6fcab5af64cccae28d0c86aaf6622cc2977  
Blob: d27ff90f3d7129f417035c7cf3014a953dd372b8  
SHA-256: b866f116b333453ccc8ddf7f3956269ad11fccf02a27a889f81f3699178fe4d7

Manifest: research-notes/lane_a_v15_494_scale_solenoid_partial_action.sha256  
Commit: 0d50a44a8ae38f88f7a987cca6316b4cd1b5270a  
Blob: 42db9e50e6432d91eebf2607ca99130b5f52bd59  
SHA-256: f826d952b3dfe02d8bbf00f0a7fe4468b7911960be0855c2a379ea557eb57d55

Replay returns PASS_EXACT_SCALE_SOLENOID_PARTIAL_ACTION after 143 domain, 109 inverse, 1,408 partial-action composition, 507 solenoid-dual composition, 109 scale covariance, and 690 exact boundary-continuity checks.

## Boundaries and HANDOFF

This remains solely the noncanonical chosen-counting-measure ell2 five-frequency commutator gate. It is not whole K or source-native Suzuki Phi. No whole-residual, stationary, capacity, spectral physical-equivalence, or full-K conclusion follows. Original C_S_32000, all thresholds, frozen hashes, and exactly-once charges remain unchanged.

HANDOFF
target: external-audit, sandbox
type: exact-scale-solenoid-partial-action
parent: v15.494
status: open
action: independently verify the partial-action domains, boundary solenoid, and continuous constant-Hankel field. Then test whether the signed prime step-kernel family defines an admissible operator-bundle section over this groupoid; do not infer a joint-norm pass from the architecture alone.
