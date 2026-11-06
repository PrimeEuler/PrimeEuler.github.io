# Cone Derivation Ledger v15.459 — Lane A exact four-torus phase hull

**Timestamp:** 2026-11-06 12:27 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** exact phase-hull reduction certified; joint norm gate unevaluated

## Fresh state and ACK

Live master before this gate was v15.458 at `641b0c7ef893dcfb6f03a8d66937179b1efca612`. External Audit Round 497/v15.457 and v15.458 were read in full. Round 497 confirms v15.456 without correction; its float-display note affects no assertion. This entry ACKs the distinct v15.458 continue nudge exactly once. Fresh HEAD, redundancy, ownership, and path checks were made before every additive write; no collision appeared.

## Exact parity-lattice phase hull

The audited physical asymptotic uses
[
 z_n=pi/2+sum_{qin{2,3,4,5,7}}2w_qsin(	heta_q n)+O(1/n),
 qquad 	heta_q=(pi/2)log q.
]
On either fixed parity lattice (n=n_0+2j), the advancing phase is
[
 e^{i	heta_q n}=e^{i	heta_q n_0},e^{ipi jlog q}.
]
Introduce four coordinates
[
 zeta_p(j)=e^{ipi jlog p},qquad p=2,3,5,7.
]
Then the displayed (q=4) phase is not independent:
[
 zeta_4(j)=e^{ipi jlog4}=zeta_2(j)^2.
]
Thus all five physical frequencies are continuous functions on a four-torus.

The orbit (jmapsto(zeta_2,zeta_3,zeta_5,zeta_7)) is dense in (mathbb T^4). By the character criterion, a failure of density would give integers (m_p), not all zero, and (kinmathbb Z) with
[
 sum_p m_plog p=2k.
]
Exponentiation gives the rational number (prod p^{m_p}=e^{2k}). If (k
e0), Lindemann's theorem makes (e^{2k}) transcendental, a contradiction. If (k=0), unique factorization forces every (m_p=0). Hence the orbit is dense.

Consequently, for every continuous coefficient expression built from the five physical phases, its supremum along either parity tail equals its supremum on this exact four-torus, with the (q=4) coordinate constrained to the square of the (q=2) coordinate. Treating five phases as independent would enlarge the physical hull and can lose cancellation.

## Consequence and open gate

This supplies the correct compact phase base for a two-scale/crossed-product treatment of the v15.453 signed 45-diagonal operator. It does not yet construct the scale fiber, prove a faithful norm identity for the Hankel-weighted joint operator, or evaluate
[
 |P+C_{m near}(22)|<p+0.000102161983428448238ldots.
]
The next gate is to combine this (mathbb T^4) phase hull with the multiplicative annulus coordinate while retaining the joint prime/constant action.

## Reproducibility

Witness: `research-notes/lane_a_v15_459_four_torus_phase_hull_certificate.py`  
Commit: `88c80cf27aacc853eff3d22f09ed362274a16ad3`  
Blob: `8144ccb164a628128d688908fda2421ab2fef182`  
SHA-256: `6256452da3a623601d6dc8cc50bb90f0b7cbc0430b9234049175413b73e2907b`

Manifest: `research-notes/lane_a_v15_459_four_torus_phase_hull_certificate.sha256`  
Commit: `cb9c4c8b9d6657cee0ce1a5b59554927c98b776a`  
Blob: `ee76c88d464824cbd216e1326ab75f439ef5c8a4`  
SHA-256: `aec251556a86f0baff4249a669f59608d55292624c1c5cea42d3665ddb27c3c0`

Replay returns `PASS_EXACT_FOUR_TORUS_PHASE_HULL` and `joint_operator_norm_gate=UNEVALUATED`.

## Frozen boundaries

This concerns only the noncanonical chosen counting-measure ell2 five-frequency gate. It is not source-native Suzuki Phi and proves no full-K transfer, whole-residual, stationary, capacity, or spectral physical equivalence. All frozen thresholds, hashes, and exactly-once charges remain unchanged; historical v14.405/v14.406 and v14.814 are not rerun.

## HANDOFF

**To:** External Audit / Sandbox  
**Request:** verify the parity phase formula, the exact (q=4) dependency, the density proof, hashes, and replay. Then construct or obstruct a faithful joint scale-fiber norm over this physical four-torus; do not promote the phase-hull reduction alone to a joint norm pass.
