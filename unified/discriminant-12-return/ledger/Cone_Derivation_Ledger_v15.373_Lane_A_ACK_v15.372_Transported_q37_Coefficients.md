# Cone Derivation Ledger v15.373 — Lane A: ACK v15.372 and transported q=3,7 coefficient certificate

Date: 2026-11-04 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.364–v15.372. Status: [D] exact transported q=3,7 same-translation coefficient construction and scoped self-adjoint cross-block Schur bound below 0.492; [O] remaining frequency pairs and justified multi-frequency Cotlar/Gram assembly.

## Fresh reads and ACK

Lane A read External Audit Round 468 (v15.371) and v15.372 in full. Round 468 independently confirmed v15.370's q=2,5 certificate and frozen hashes and closed with `action: none`; no correction is required. v15.372 is a distinct standing continue nudge. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.372 exactly once and applies the audited transported-coefficient method to q=3,7.

## Exact transported pair construction

Set `A=log(3)`, `B=log(7)`. At translation `tau B-sigma A`, combine the two equal-translation coefficients

`G_(sigma,tau)(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

`                  +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`

before taking absolute values. The witness generates every discontinuity from `0`, `-sigma A`, `tau B`, and `tau B-sigma A` modulo two, certifies their order using 320-bit rational enclosures, and performs all sawtooth reductions symbolically in `Q[A,B]`.

Each of the four translation groups has four exact pieces. Their union gives nine common cells; on every cell the witness certifies all four coefficient signs before forming the row sum.

## Exact common-partition maximum

The exact row maximum is

`sup_x sum_(sigma,tau)|G_(sigma,tau)(x)| = 12-4B`.

Restoring `alpha_3 alpha_7=AB/(4sqrt(21))` yields

`B_37 = AB(3-B)/sqrt(21)`

with exact-rational outward enclosure

`0.491 < B_37 < 0.492`

and printed value approximately `0.4917396414482828`. Self-adjointness supplies the matching column bound by the same opposite-translation relabeling already audited in Rounds 466–468.

This is the fourth separate coefficient-sensitive pair result. No scalar sum of `B_23`, `B_25`, `B_35`, and `B_37` is asserted: a valid cross-pair operator-combination rule is still missing. This entry is not a full five-frequency commutator, complete-tail, stationary, or infinite-capacity certificate.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_373_q37_transported_coefficient_certificate.py`

Witness commit: `1a7c9e5435dc27678289b65febc9964e6f121473`

Git blob: `ac2b87432314d37c79a815d9816999382ba63b68`

SHA-256: `f162322a6ee91659eb6a1537784a2fa2b500b1131401135992fe5c967178fe1d`

The witness uses exact symbolic polynomials and 320-bit rational outward enclosures. Floating-point conversion is used only as a provisional cut-order sort key; exact interval assertions certify every accepted order and claim.

No Pages workflow or queued/running CI is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. The five-frequency frontier remains `3.273` against target `2.535946`. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q37-transported-signed-coefficient-certificate
parent: v15.373
status: OPEN_AUDIT
action: replay the exact witness; independently verify the discontinuity set/order, symbolic branch reductions, nine-cell maximum `12-4log(7)`, self-adjoint row/column identification, normalization, frozen hashes, and `0.491<B_37<0.492` scope.
deliverable: confirmation/correction or another exact pair extension / rigorously justified multi-frequency Cotlar matrix. Do not combine the four pair bounds without a proved operator rule, and do not promote this pair result to full commutator or complete-tail closure.

