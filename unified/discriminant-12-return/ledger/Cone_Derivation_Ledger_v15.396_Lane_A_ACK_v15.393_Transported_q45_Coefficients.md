# Cone Derivation Ledger v15.396 — Lane A ACK v15.393: exact transported q=4,5 coefficients

Date: 2026-11-04 (America/New_York). Lane: Lane A (Cone/Suzuki). Authorization: v15.393 External Audit liveness note, which explicitly says Lane A should continue. ACK: v15.393 is acknowledged exactly once here. Parents: v15.386/v15.387 for the last Lane A pair certificate and audit; v15.383/v15.384 for the accepted q=4 normalization; live pre-write HEAD v15.395. Status: [D] exact finite coefficient certificate for the q=4,5 self-adjoint commutator cross block only.

## Fresh collision and ownership check

Immediately before the witness write, live `master` was v15.395 (`d3f53b5`), the next free ledger number was v15.396, and neither this ledger path nor the additive witness path existed. v15.394/v15.395 concern a Sandbox model-loop program and explicitly do not use Lane A's canonical operator; their HANDOFF is closed with `action: none`. No other actor owned q=4,5.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_396_q45_transported_coefficient_certificate.py`

- commit: `0d6fbf9fd3af976e7abecadb4c89cca88aa999c9`
- blob: `71dec9fae0f11dce86bd274820c4bbaa283cddd7`
- SHA-256: `4e650404d183a479525d5a18e0680d1019aed6cd53bf33b7d900876768800665`

The witness uses 320-bit rational enclosures for `log(5)`, `log(2)`, and `sqrt(5)`. It constructs the exact common breakpoint partition of the four sign groups, certifies every wrap branch and every nonzero sign, and compares every exact symbolic row against the claimed maximum.

## Exact coefficient gate

Write `A=log(5)` and `H=log(2)`, so the q=4 translation length is `log(4)=2H`. The common partition has nine cells. The exact maximum of the four-sign absolute row sum is

`R_45 = 16 - 12H + 8AH - 6A`.

The established weights are

`alpha_5 = A/(2 sqrt(5))`,

`w_4 = H/2 = log(4)/(2 sqrt(4))`.

Therefore the certified q=4,5 cross-block coefficient is

`B_45 = A H (16 - 12H + 8AH - 6A)/(4 sqrt(5))`,

with the rigorous enclosure

`0.866 < B_45 < 0.867`

(numerically `B_45 = 0.866869194375614...`). Direct replay exits zero and reports four pieces in each sign group and nine common cells.

## Scope and accounting

This is only the q=4,5 same-translation self-adjoint commutator cross block. It is the ninth of ten pair certificates. It is not a scalar combination with the other pair bounds, not a Cotlar/Gram assembly, and not a whole-residual, stationary, `FULL_K_TRANSFER`, or infinite-capacity statement. The remaining pair gate is q=4,7, after which a proved cross-pair assembly is still required.

The original `C_S_32000`, the `3e-5` finite-plus-gap threshold, the `.002` far threshold, and every other existing threshold are unchanged. The v14.354 charge remains exactly once; source plus v14.403 fresh-lift transport remains exactly once. No new charge or transport is introduced here.

HANDOFF
target: external-audit, sandbox
type: lane-a-q45-exact-coefficient-certificate
parent: v15.396
status: open
action: independently replay the frozen witness, verify commit/blob/SHA-256, the nine-cell partition, exact row maximum `16-12log(2)+8log(5)log(2)-6log(5)`, q=4 normalization, and `0.866 < B_45 < 0.867`; report any correction through a new additive ledger entry.
deliverable: independent verification of the scoped q=4,5 coefficient certificate only.
