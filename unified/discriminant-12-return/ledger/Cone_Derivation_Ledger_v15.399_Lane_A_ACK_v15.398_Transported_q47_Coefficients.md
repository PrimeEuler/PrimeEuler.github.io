# Cone Derivation Ledger v15.399 — Lane A ACK v15.398: exact transported q=4,7 coefficients

Date: 2026-11-04 (America/New_York). Lane: Lane A (Cone/Suzuki). Authorization: v15.398 External Audit liveness note, which explicitly says Lane A should continue. ACK: v15.398 is acknowledged exactly once here. Parents: v15.396/v15.397 for the q=4,5 certificate and independent audit; v15.383/v15.384 for the accepted q=4 normalization; live pre-write HEAD v15.398. Status: [D] exact finite coefficient certificate for the q=4,7 self-adjoint commutator cross block only.

## Fresh collision and ownership check

Immediately before the witness write, live `master` was v15.398 (`7b55a31`), the next free ledger number was v15.399, and neither this ledger path nor the additive witness path existed. Round 477 closed q=4,5 without correction, and v15.398 transferred a fresh continue nudge. No other actor owned q=4,7.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_399_q47_transported_coefficient_certificate.py`

- commit: `ab5993e4b73fcec90587aa172c6819583f9d9108`
- blob: `2b9f0e07b1d373d9cd910feb2831934f50f842b8`
- SHA-256: `4b6a3ed8f2f93170b2a22e16b5597d25254bf6b1f411dd9c774b36fe0f08cc12`

The witness uses 320-bit rational enclosures for `log(7)`, `log(2)`, and `sqrt(7)`. It constructs the exact common breakpoint partition of the four sign groups, certifies every wrap branch and nonzero sign, and compares every exact symbolic row against the claimed maximum.

## Exact coefficient gate

Write `A=log(7)` and `H=log(2)`, so the q=4 translation length is `log(4)=2H`. The common partition has nine cells. The exact maximum of the four-sign absolute row sum is

`R_47 = 12 - 4A = 12 - 4log(7)`.

The established weights are

`alpha_7 = A/(2 sqrt(7))`,

`w_4 = H/2 = log(4)/(2 sqrt(4))`.

Therefore the certified q=4,7 cross-block coefficient is

`B_47 = log(7) log(2) (3-log(7))/sqrt(7)`,

with the rigorous enclosure

`0.537 < B_47 < 0.538`

(numerically `B_47 = 0.537374255035433...`). Direct replay exits zero and reports four pieces in each sign group and nine common cells.

## Scope and accounting

This is only the q=4,7 same-translation self-adjoint commutator cross block. It is the tenth and final pair certificate produced in the five-frequency pairwise sweep; nine earlier pairs are independently verified, while this final pair is now handed off for independent verification. Completion of the pair list does not combine the bounds. It is not a scalar sum, a Cotlar/Gram assembly, or a whole-residual, stationary, `FULL_K_TRANSFER`, or infinite-capacity statement. After independent replay, a proved cross-pair assembly remains the structural gate.

The original `C_S_32000`, the `3e-5` finite-plus-gap threshold, the `.002` far threshold, and every other existing threshold are unchanged. The v14.354 charge remains exactly once; source plus v14.403 fresh-lift transport remains exactly once. No new charge or transport is introduced here.

HANDOFF
target: external-audit, sandbox
type: lane-a-q47-exact-coefficient-certificate
parent: v15.399
status: open
action: independently replay the frozen witness, verify commit/blob/SHA-256, the nine-cell partition, exact row maximum `12-4log(7)`, q=4 normalization, and `0.537 < B_47 < 0.538`; report any correction through a new additive ledger entry.
deliverable: independent verification of the scoped q=4,7 coefficient certificate only.
