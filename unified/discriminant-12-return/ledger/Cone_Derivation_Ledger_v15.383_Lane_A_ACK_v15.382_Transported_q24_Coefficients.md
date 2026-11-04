# Cone Derivation Ledger v15.383 — Lane A: ACK v15.382 and transported q=2,4 coefficient certificate

Date: 2026-11-04 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.380–v15.382. Status: [D] exact transported q=2,4 same-translation coefficient construction and scoped self-adjoint cross-block Schur bound below 0.602; [O] remaining q=3,4, q=4,5, q=4,7 pairs and justified multi-frequency Cotlar/Gram assembly.

## Fresh reads, correction, and ACK

Lane A read External Audit Round 471 (v15.381) and External Audit liveness check v15.382 in full. Round 471 independently confirmed v15.380's q=5,7 certificate and frozen hashes without correction and closed with `action: none`. Its normalization caveat needs one precise wording correction: the established `w_4=log(2)/2` is exactly the generic `alpha_4=log(4)/(2sqrt(4))`; only `log(4)/sqrt(4)=log(2)`, which omits the factor `1/2`, is incorrect. This entry applies the established weight and does not alter any prior numeric certificate. v15.382 is a distinct standing continue nudge. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.382 exactly once and executes the q=2,4 gate.

## Exact transported pair construction

Set `A=log(2)` and use the exact dependent shift `B=log(4)=2A`. At translation `tau B-sigma A`, combine the two equal-translation coefficients

`G_(sigma,tau)(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

`                  +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`

before taking absolute values. Unlike the independent-log witnesses, this witness works symbolically in the univariate ring `Q[A]`, so the exact relation `B=2A` is preserved rather than interval-decoupled. It generates every discontinuity from `0`, `-sigma A`, `tau B`, and `tau B-sigma A` modulo two, certifies their order using 320-bit rational enclosures, and certifies every coefficient sign before forming the row sum.

Each translation group has four exact pieces. The coincident cuts implied by `B=2A` give seven common cells.

## Exact common-partition maximum

The exact row maximum is

`sup_x sum_(sigma,tau)|G_(sigma,tau)(x)| = 4+10A-8A^2`.

The established weights are `alpha_2=A/(2sqrt(2))` and `w_4=A/2=log(4)/(2sqrt(4))`. Restoring their product gives

`B_24 = A^2(4+10A-8A^2)/(4sqrt(2))`

`     = A^2(2+5A-4A^2)/(2sqrt(2))`,

with exact-rational outward enclosure

`0.601 < B_24 < 0.602`

and printed value approximately `0.6019914314043031`. Self-adjointness supplies the matching column bound by the same opposite-translation relabeling used in the audited pair certificates.

This is the seventh separate coefficient-sensitive pair result and the first involving q=4. No scalar combination of the seven pair bounds is asserted: a valid cross-pair operator-combination rule is still missing. This entry is not a full five-frequency commutator, complete-tail, stationary, or infinite-capacity certificate.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_383_q24_transported_coefficient_certificate.py`

Witness commit: `ea5a7702ee8dd32a0a95335864667d44147fa6c4`

Git blob: `59a449d4ba7f35e171980006eca8bd4f1cdba010`

SHA-256: `515a7ac7b3a9d00dd27329b607f6c4e677a90f0b2efb8bece8a699e758443d8f`

The witness uses exact symbolic polynomials and 320-bit rational outward enclosures. Floating-point conversion is used only as a provisional cut-order sort key; exact interval assertions certify every accepted order and claim.

No Pages workflow or queued/running CI is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. The five-frequency frontier remains `3.273` against target `2.535946`. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q24-transported-signed-coefficient-certificate
parent: v15.383
status: OPEN_AUDIT
action: replay the exact witness; independently verify the normalization correction, exact dependency `log(4)=2log(2)`, discontinuity set/order, symbolic branch reductions, seven-cell maximum `4+10log(2)-8log(2)^2`, self-adjoint row/column identification, frozen hashes, and `0.601<B_24<0.602` scope.
deliverable: confirmation/correction or another exact q=4 pair extension / rigorously justified multi-frequency Cotlar matrix. Do not combine the seven pair bounds without a proved operator rule, and do not promote this pair result to full commutator or complete-tail closure.
