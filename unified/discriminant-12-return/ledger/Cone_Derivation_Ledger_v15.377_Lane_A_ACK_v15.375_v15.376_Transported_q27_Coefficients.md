# Cone Derivation Ledger v15.377 — Lane A: ACK v15.375–v15.376 and transported q=2,7 coefficient certificate

Date: 2026-11-04 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.373–v15.376. Status: [D] exact transported q=2,7 same-translation coefficient construction and scoped self-adjoint cross-block Schur bound below 0.380; [O] remaining frequency pairs and justified multi-frequency Cotlar/Gram assembly.

## Fresh reads and ACK

Lane A read External Audit Round 469 (v15.374) and liveness notes v15.375–v15.376 in full. Round 469 independently confirmed v15.373's q=3,7 certificate and frozen hashes and closed with `action: none`; no correction is required. v15.375 and v15.376 are distinct standing continue nudges. After fresh HEAD/ledger/audit and collision checks, this entry ACKs each exactly once and applies the audited transported-coefficient method to q=2,7.

## Exact transported pair construction

Set `A=log(2)`, `B=log(7)`. At translation `tau B-sigma A`, combine the two equal-translation coefficients

`G_(sigma,tau)(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

`                  +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`

before taking absolute values. The witness generates every discontinuity from `0`, `-sigma A`, `tau B`, and `tau B-sigma A` modulo two, certifies their order using 320-bit rational enclosures, and performs all sawtooth reductions symbolically in `Q[A,B]`.

Each of the four translation groups has four exact pieces. Their union gives nine common cells; on every cell the witness certifies all four coefficient signs before forming the row sum.

## Exact common-partition maximum

The exact row maximum is

`sup_x sum_(sigma,tau)|G_(sigma,tau)(x)| = 12-4B`.

Restoring `alpha_2 alpha_7=AB/(4sqrt(14))` yields

`B_27 = AB(3-B)/sqrt(14)`

with exact-rational outward enclosure

`0.379 < B_27 < 0.380`

and printed value approximately `0.37998097977062395`. Self-adjointness supplies the matching column bound by the same opposite-translation relabeling audited in Rounds 466–469.

This is the fifth separate coefficient-sensitive pair result. No scalar sum of `B_23`, `B_25`, `B_27`, `B_35`, and `B_37` is asserted: a valid cross-pair operator-combination rule is still missing. This entry is not a full five-frequency commutator, complete-tail, stationary, or infinite-capacity certificate.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_377_q27_transported_coefficient_certificate.py`

Witness commit: `8e21de6038422284035fad6fe25f3b6f4384c0fd`

Git blob: `c8ca8527c0662eb933c9d3efd68d6d3cc3af4a52`

SHA-256: `0c22910aa86a5c83c86bf88dff814d87881c4a332ecb5a0bbb2cc8a3fe13f311`

The witness uses exact symbolic polynomials and 320-bit rational outward enclosures. Floating-point conversion is used only as a provisional cut-order sort key; exact interval assertions certify every accepted order and claim.

No Pages workflow or queued/running CI is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. The five-frequency frontier remains `3.273` against target `2.535946`. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q27-transported-signed-coefficient-certificate
parent: v15.377
status: OPEN_AUDIT
action: replay the exact witness; independently verify the discontinuity set/order, symbolic branch reductions, nine-cell maximum `12-4log(7)`, self-adjoint row/column identification, normalization, frozen hashes, and `0.379<B_27<0.380` scope.
deliverable: confirmation/correction or another exact pair extension / rigorously justified multi-frequency Cotlar matrix. Do not combine the five pair bounds without a proved operator rule, and do not promote this pair result to full commutator or complete-tail closure.

