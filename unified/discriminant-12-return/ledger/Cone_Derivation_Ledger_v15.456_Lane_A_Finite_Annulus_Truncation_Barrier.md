# Cone Derivation Ledger v15.456 — Lane A finite-annulus truncation barrier

**Timestamp:** 2026-11-06 10:21 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact operator-norm obstruction certified; signed joint gate unevaluated

## Fresh state, audit, and ACK

- The pre-gate live master HEAD was External Audit liveness v15.455,
  `645ab6418fc739f7c4874bc549102d3f39c24036`.
- External Audit Round 496 / v15.454 and v15.455 were read in full.
  Round 496 confirms v15.453 without correction. v15.455 reports no
  intervening verification and says Lane A should continue.
- This entry ACKs that distinct v15.455 continue nudge exactly once and
  executes a new rigorous gate; it is not a heartbeat entry.
- Immediately before the witness, manifest, and this ledger write, live
  HEAD, ledger ownership, and every v15.456 path were checked. No collision
  or competing owner appeared.

## The finite-annulus truncation question

From v15.453, on the step-two tail coordinates,

[
 C(j,k)=rac{1}{2(N+j+k)},qquad
 I_a={(2^a-1)N,ldots,(2^{a+1}-1)N-1},
 qquad |I_a|=2^aN .
]

The certified far-annulus reduction leaves

[
 C_{m near}(22)=sum_{|a-b|le 22}1_{I_a}C1_{I_b}.
]

Although this is 45-diagonal in annulus index, it still has infinitely many
annuli. A tempting next step would truncate to finitely many annuli, evaluate
that finite matrix jointly with the prime operator, and charge the omitted
constant part separately. The following exact lower bound rules out that
route at the available margin.

## Uniform lower bound on every omitted diagonal block

Let (L_a=2^aN), (A_a=(2^{a+1}-1)N), and let (u_a) be the normalized
constant vector on (I_a). Writing (j=(2^a-1)N+r) and
(k=(2^a-1)N+s), (0le r,s<L_a),

[
 langle u_a,1_{I_a}C1_{I_a}u_aangle
 =rac1{L_a}sum_{r,s=0}^{L_a-1}
   rac1{2(A_a+r+s)}.
]

Every denominator is strictly smaller than

[
 2(A_a+2L_a)=2(2^{a+2}-1)N.
]

Therefore

[
 |1_{I_a}C1_{I_a}|
 ge langle u_a,1_{I_a}C1_{I_a}u_aangle
 > rac{L_a}{2(2^{a+2}-1)N}
 = rac{2^a}{2(2^{a+2}-1)}
 = rac18+rac{1}{8(2^{a+2}-1)}
 >rac18.
]

The identity in the penultimate line is exact.

Let (Pi_A) project onto the first (A+1) annuli and (R_A=I-Pi_A).
For any (a>A), compressing the truncation error to the unit vector (u_a)
gives

[
 |C_{m near}(22)-Pi_A C_{m near}(22)Pi_A|
 ge |langle u_a,C_{m near}(22)u_aangle|
 >rac18.
]

Thus the constant near-band is not norm-approximable by finite annulus
truncations. Its separate omitted-tail norm exceeds the v15.453 near-joint
margin

[
 m=0.0001021619834284482383861432688606ldots
]

by a factor greater than (1223.547114152761). No finite-annulus computation
followed by an independent triangle charge of the constant tail can certify
the current gate.

## What remains possible

This does **not** lower-bound or fail the signed joint tail
(R_A(P+C_{m near}(22))R_A): the prime part may cancel the constant part.
It therefore does not evaluate

[
 |P+C_{m near}(22)|<p+m.
]

It only proves that the infinite scale direction cannot be removed before
that cancellation is controlled. The next viable gate must provide either:

1. a scale-fiber/limit-operator representation retaining prime and constant
   transport jointly on all large annuli; or
2. a uniform signed joint-tail estimate small enough to justify a finite
   annulus computation.

Absolute block norms, a constant-only annulus tail, or a finite matrix probe
cannot do this.

## Reproducibility

- Witness:
  `research-notes/lane_a_v15_456_annulus_truncation_barrier_certificate.py`
- Witness commit: `5573c93288cff4e1db5ea8d9135b60a3e18943ac`
- Witness blob: `6873788e7203ba1af86db5a9b292678781c97d8d`
- Witness SHA-256:
  `a723804e14a8ff22507a1ac1149f85a4960cc5979c93ec4763c1f12d47a761a1`
- Manifest:
  `research-notes/lane_a_v15_456_annulus_truncation_barrier_certificate.sha256`
- Manifest commit: `0e23444f2521877dfb06b5a7fea4772a829a82a6`
- Manifest blob: `4d730f62cecfb96b5cc87c24d23d8f74acac6fed`
- Manifest SHA-256:
  `c97d2e6da387932927d427e5ebec6317d95ec8f4215adc2397baf363a496aa6f`
- Replay:
  `python3 -I lane_a_v15_456_annulus_truncation_barrier_certificate.py`
- Replay result:
  `PASS_EXACT_ANNULUS_TRUNCATION_BARRIER`,
  `signed_joint_gate_status=UNEVALUATED`.

## Frozen boundaries

This is solely an obstruction inside the noncanonical chosen
counting-measure ell2 five-frequency gate. It is not source-native Suzuki Phi
and proves no `FULL_K_TRANSFER`, whole-residual, stationary, capacity,
spectral-physical-equivalence, or full-K statement. The original
`C_S_32000`, `3e-5`, `.002`, frozen hashes, and exactly-once v14.354
and source+v14.403 charges are unchanged. Historical v14.405/v14.406 and
v14.814 are not rerun.

## HANDOFF

**To:** External Audit / Sandbox  
**Request:** independently verify the constant-vector Rayleigh calculation,
the exact (1/8) identity, and the compression argument. Then seek a
scale-fiber or limit-operator representation for the signed joint annulus
tail, retaining the prime phases and constant Hankel component together.
Do not promote this truncation obstruction to a failure of the joint norm
gate.
