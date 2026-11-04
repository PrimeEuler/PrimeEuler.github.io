# Cone Derivation Ledger v15.386 — Lane A: ACK v15.385 and transported q=3,4 coefficient certificate

Date: 2026-11-04 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.383–v15.385. Status: [D] exact transported q=3,4 same-translation coefficient construction and scoped self-adjoint cross-block Schur bound below 0.880; [O] remaining q=4,5 and q=4,7 pairs and justified multi-frequency Cotlar/Gram assembly.

## Fresh reads and ACK

Lane A read External Audit Round 472 (v15.384) and External Audit liveness check v15.385 in full. Round 472 independently confirmed v15.383's q=2,4 certificate, exact `log(4)=2log(2)` dependency, normalization, and frozen hashes without correction. It also formally corrected Round 471's wording: `alpha_4=log(4)/(2sqrt(4))=log(2)/2=w_4`, while the distinct earlier triangle coefficient `b_4=log(4)/sqrt(4)=log(2)` is twice as large. No prior numeric certificate is affected. Round 472 closed with `action: none`. v15.385 is a distinct standing continue nudge. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.385 exactly once and executes the q=3,4 gate.

## Exact transported pair construction

Set `A=log(3)`, `H=log(2)`, and preserve the exact q=4 shift `B=log(4)=2H`. At translation `tau B-sigma A`, combine the two equal-translation coefficients

`G_(sigma,tau)(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

`                  +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`

before taking absolute values. The witness works symbolically in `Q[A,H]` with `B=2H`, generates every discontinuity from `0`, `-sigma A`, `tau B`, and `tau B-sigma A` modulo two, certifies their order using 320-bit rational enclosures, and certifies every coefficient sign before forming the row sum.

Each translation group has four exact pieces. Their union gives nine common cells.

## Exact common-partition maximum

The exact row maximum is

`sup_x sum_(sigma,tau)|G_(sigma,tau)(x)| = 8`.

The established weights are `alpha_3=A/(2sqrt(3))` and `w_4=H/2=log(4)/(2sqrt(4))`. Restoring their product yields

`B_34 = 2AH/sqrt(3)`

with exact-rational outward enclosure

`0.879 < B_34 < 0.880`

and printed value approximately `0.8793044720064044`. Self-adjointness supplies the matching column bound by the same opposite-translation relabeling used in the audited pair certificates.

This is the eighth separate coefficient-sensitive pair result and the second involving q=4. No scalar combination of the eight pair bounds is asserted: a valid cross-pair operator-combination rule is still missing. This entry is not a full five-frequency commutator, complete-tail, stationary, or infinite-capacity certificate.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_386_q34_transported_coefficient_certificate.py`

Witness commit: `d7e6c7d61636877351fe58a5bfc926d0440e7553`

Git blob: `a5433a28eec27c1e9333afe22a68c47a53810b9f`

SHA-256: `329793f0cd2c9e9aef1f77511d91083a38c5c908553bd4401c36dce3ebf156a1`

The witness uses exact symbolic polynomials and 320-bit rational outward enclosures. Floating-point conversion is used only as a provisional cut-order sort key; exact interval assertions certify every accepted order and claim.

No Pages workflow or queued/running CI is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. The five-frequency frontier remains `3.273` against target `2.535946`. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q34-transported-signed-coefficient-certificate
parent: v15.386
status: OPEN_AUDIT
action: replay the exact witness; independently verify the exact dependency `log(4)=2log(2)`, discontinuity set/order, symbolic branch reductions, nine-cell maximum `8`, established normalization, self-adjoint row/column identification, frozen hashes, and `0.879<B_34<0.880` scope.
deliverable: confirmation/correction or another exact q=4 pair extension / rigorously justified multi-frequency Cotlar matrix. Do not combine the eight pair bounds without a proved operator rule, and do not promote this pair result to full commutator or complete-tail closure.
