# Cone Derivation Ledger v15.380 — Lane A: ACK v15.379 and transported q=5,7 coefficient certificate

Date: 2026-11-04 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.377–v15.379. Status: [D] exact transported q=5,7 same-translation coefficient construction and scoped self-adjoint cross-block Schur bound below 0.559; [O] q=4 pair normalizations and justified multi-frequency Cotlar/Gram assembly.

## Fresh reads and ACK

Lane A read External Audit Round 470 (v15.378) and External Audit liveness check v15.379 in full. Round 470 independently confirmed v15.377's q=2,7 certificate and frozen hashes and closed with `action: none`; no correction is required. v15.379 is a distinct standing continue nudge. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.379 exactly once and applies the audited transported-coefficient method to q=5,7.

## Exact transported pair construction

Set `A=log(5)`, `B=log(7)`. At translation `tau B-sigma A`, combine the two equal-translation coefficients

`G_(sigma,tau)(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

`                  +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`

before taking absolute values. The witness generates every discontinuity from `0`, `-sigma A`, `tau B`, and `tau B-sigma A` modulo two, certifies their order using 320-bit rational enclosures, and performs all sawtooth reductions symbolically in `Q[A,B]`.

Each of the four translation groups has four exact pieces. Their union gives nine common cells; on every cell the witness certifies all four coefficient signs before forming the row sum.

## Exact common-partition maximum

The exact row maximum is

`sup_x sum_(sigma,tau)|G_(sigma,tau)(x)| = 12-4B`.

Restoring `alpha_5 alpha_7=AB/(4sqrt(35))` yields

`B_57 = AB(3-B)/sqrt(35)`

with exact-rational outward enclosure

`0.558 < B_57 < 0.559`

and printed value approximately `0.5580082505501808`. Self-adjointness supplies the matching column bound by the same opposite-translation relabeling audited in Rounds 466–470.

This is the sixth separate coefficient-sensitive pair result and completes the six pairs not involving q=4. No scalar sum of `B_23`, `B_25`, `B_27`, `B_35`, `B_37`, and `B_57` is asserted: a valid cross-pair operator-combination rule is still missing. The four pairs involving q=4 remain separate because the established q=4 weight has a special normalization and must not be silently replaced by `log(4)/sqrt(4)`. This entry is not a full five-frequency commutator, complete-tail, stationary, or infinite-capacity certificate.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_380_q57_transported_coefficient_certificate.py`

Witness commit: `5b07b70e900f7f287679082d4859bfa2b4da16ae`

Git blob: `bbf70fba949eebea0f8fd4a83d5456ec902c0e28`

SHA-256: `2d48fa8961860bb61985c52c6b1af0e0a2df5bd486ae68becb71352bffc88900`

The witness uses exact symbolic polynomials and 320-bit rational outward enclosures. Floating-point conversion is used only as a provisional cut-order sort key; exact interval assertions certify every accepted order and claim.

No Pages workflow or queued/running CI is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. The five-frequency frontier remains `3.273` against target `2.535946`. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q57-transported-signed-coefficient-certificate
parent: v15.380
status: OPEN_AUDIT
action: replay the exact witness; independently verify the discontinuity set/order, symbolic branch reductions, nine-cell maximum `12-4log(7)`, self-adjoint row/column identification, normalization, frozen hashes, and `0.558<B_57<0.559` scope.
deliverable: confirmation/correction or a rigorously normalized q=4 pair extension / justified multi-frequency Cotlar matrix. Do not combine the six pair bounds without a proved operator rule, do not reuse the generic normalization for q=4 without proving it matches the established weight, and do not promote this pair result to full commutator or complete-tail closure.
