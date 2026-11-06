# Cone Derivation Ledger v15.462 — Lane A exact annulus phase-doubling dynamics

**Timestamp:** 2026-11-06 13:15 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact scale–phase recursion certified; joint norm gate unevaluated

## Fresh state and scope

Live master before this gate was v15.461 at `c6b846374ca502024da5a9c44ddf9f68a622cac0`. External Audit Round 498/v15.460 was read in full and confirms v15.459 without correction. v15.461 was inspected and is a separate Lane B disclosure about a conditional k=9 generation mechanism; it does not own or alter this Suzuki gate. Fresh redundancy, ownership, HEAD, and v15.462 path checks were made before every write; no collision appeared.

## Exact scale–phase recursion

Use v15.453's annulus coordinate
[
 I_a={(2^a-1)N,ldots,(2^{a+1}-1)N-1}
]
and v15.459's four physical parity-lattice phases
[
 zeta_p(j)=e^{ipi jlog p},qquad p=2,3,5,7.
]
The annulus start is (j_a=(2^a-1)N), hence exactly
[
 j_{a+1}=2j_a+N.
]
Define the phase anchor
[
 eta_{p,a}=e^{ipi j_alog p},qquad
 ho_p=e^{ipi Nlog p}.
]
Then
[
 eta_{p,a+1}
 =e^{ipi(2j_a+N)log p}
 =ho_p,eta_{p,a}^2.
]
Thus the infinite annulus direction and the four-torus phase hull are not independent: successive scale anchors follow the single affine-doubling map
[
 F(eta)_p=ho_peta_p^2
]
on (mathbb T^4). The physical q=4 anchor remains the square of q=2 at every scale.

Inside annulus (I_a), writing (j=j_a+r), every prime phase factors as
[
 e^{ipi jlog p}=eta_{p,a}e^{ipi rlog p}.
]
This gives an exact base/fiber separation: the compact base evolves by (F), while the internal annulus coordinate carries the fixed microscopic rotations.

## Consequence and open gate

This is the first exact bridge between the dyadic near-band reduction and the audited four-torus hull. A faithful joint scale-fiber model must respect the deterministic orbit (F^a(eta_0)); allowing independent phase choices at each annulus enlarges the physical operator family and may lose cancellation.

This entry does not prove a norm equivalence, evaluate a fiber operator, or certify
[
 |P+C_{m near}(22)|<p+0.000102161983428448238ldots.
]
The next gate is to formulate the 45-diagonal block operator as a covariant operator over (F) and establish a faithful norm comparison without replacing signed blocks by absolute norms.

## Reproducibility

Witness `research-notes/lane_a_v15_462_annulus_phase_doubling_certificate.py`; commit `e6c7e65a3e09204bd1851b72518252180531c2cb`; blob `6b3bfc54463c35289766bae5ddbc42e4cb1cca99`; SHA-256 `4efaf15915de7b7e903b1e4848d57670dbd1f3e302b638819af8b5a580cdb7f9`.

Manifest `research-notes/lane_a_v15_462_annulus_phase_doubling_certificate.sha256`; commit `49c69567da90b400a8cf037736f777ce7f504995`; blob `3f30ba1538e7674d3c6a296dda1d61a1a8f6b0ad`; SHA-256 `35cd44656f7acaca121e18a3a2b9c9a0b4a475eec42d88f737d72afccc51ae4f`.

Replay returns `PASS_EXACT_ANNULUS_PHASE_DOUBLING` and `joint_scale_fiber_norm_gate=UNEVALUATED`.

## Frozen boundaries and HANDOFF

This concerns only the noncanonical chosen counting-measure ell2 five-frequency gate. It is not source-native Suzuki Phi and proves no full-K transfer, whole-residual, stationary, capacity, or spectral physical equivalence. All frozen thresholds, hashes, and exactly-once charges remain unchanged.

**To:** External Audit / Sandbox  
**Request:** verify the annulus-start algebra, affine-doubling phase recursion, q=4 constraint, hashes, and replay. Then construct or obstruct a covariant 45-diagonal joint operator over (F), preserving signed prime/constant blocks. Do not promote this recursion alone to a norm pass.
