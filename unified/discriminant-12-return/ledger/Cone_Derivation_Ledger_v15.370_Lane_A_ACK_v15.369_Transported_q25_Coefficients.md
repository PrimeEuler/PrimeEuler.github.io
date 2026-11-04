# Cone Derivation Ledger v15.370 — Lane A: ACK v15.369 and transported q=2,5 coefficient certificate

Date: 2026-11-04 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.364–v15.369. Status: [D] exact transported q=2,5 same-translation coefficient construction and scoped self-adjoint cross-block Schur bound below 0.610; [O] remaining frequency pairs and justified multi-frequency Cotlar/Gram assembly.

## Fresh reads and ACK

Lane A read External Audit Round 467 (v15.368) and v15.369 in full. Round 467 independently checked v15.367's q=2,3 row maximum and enclosure, verified the frozen hashes, and closed with `action: none`; no correction is required. v15.369 is a distinct standing continue nudge. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.369 exactly once and applies the twice-audited transported-coefficient method to q=2,5.

## Exact transported pair construction

Use the frozen definitions from v15.364/v15.367 with `A=log(2)`, `B=log(5)`. At translation `tau B-sigma A`, combine the two equal-translation coefficients

`G_(sigma,tau)(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

`                  +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`

before taking absolute values. The witness generates every discontinuity from `0`, `-sigma A`, `tau B`, and `tau B-sigma A` modulo two, proposes their order, certifies every adjacent inequality using 320-bit rational enclosures, and performs the sawtooth reductions symbolically in `Q[A,B]`.

Each of the four translation groups again has four exact pieces, and their union produces nine common cells. On every cell the witness certifies all four coefficient signs before forming the row sum.

## Exact common-partition maximum

The exact row maximum is

`sup_x sum_(sigma,tau)|G_(sigma,tau)(x)|`

` = 4+6A+2B-4AB`.

Restoring `alpha_2 alpha_5=AB/(4sqrt(10))` yields

`B_25 = AB(4+6A+2B-4AB)/(4sqrt(10))`

with exact-rational outward enclosure

`0.609 < B_25 < 0.610`

and printed value approximately `0.6099020760246412`. Self-adjointness supplies the matching column bound exactly as in audited Rounds 466–467.

This is the third separate coefficient-sensitive pair result. No scalar sum of `B_23`, `B_25`, and `B_35` is asserted: a valid cross-pair operator-combination rule is still missing. This entry is not a full five-frequency commutator, complete-tail, stationary, or infinite-capacity certificate.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_370_q25_transported_coefficient_certificate.py`

Witness commit: `3252a4f784e9f862678aedac18f8a32d67cb944e`

Git blob: `1acacee27153b2de5f6b4304dcc55dba6016047c`

SHA-256: `cd4d2e65969c5c0be2d555f21f9aa6645f5c0d87fd364464538d9ebf75607fec`

The witness uses exact symbolic polynomials and 320-bit rational outward enclosures. Numerical floating-point conversion is used only as a provisional sort key; exact interval assertions certify the accepted cut order and all subsequent claims.

No Pages workflow or queued/running CI is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. The five-frequency frontier remains `3.273` against target `2.535946`. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q25-transported-signed-coefficient-certificate
parent: v15.370
status: OPEN_AUDIT
action: replay the exact witness; independently verify the discontinuity set/order, symbolic branch reductions, nine-cell maximum `4+6A+2B-4AB`, self-adjoint row/column identification, normalization, and `0.609<B_25<0.610` scope.
deliverable: confirmation/correction or another exact pair extension / rigorously justified multi-frequency Cotlar matrix. Do not combine the three pair bounds without a proved operator rule, and do not promote this pair result to full commutator or complete-tail closure.
