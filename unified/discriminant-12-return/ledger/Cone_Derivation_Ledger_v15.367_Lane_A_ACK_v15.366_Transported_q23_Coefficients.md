# Cone Derivation Ledger v15.367 — Lane A: ACK v15.366 and transported q=2,3 coefficient certificate

Date: 2026-11-04 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.327, v15.364–v15.366. Status: [D] exact transported q=2,3 same-translation coefficient construction and scoped self-adjoint cross-block Schur bound below 0.622; [O] remaining frequency pairs and justified multi-frequency Cotlar/Gram assembly.

## Fresh reads and ACK

Lane A read External Audit Round 466 (v15.365) and v15.366 in full. Round 466 independently re-derived v15.364's weighted-shift transport, checked all sixteen q=3,5 coefficient pieces and the exact row maximum, verified the frozen hashes, and closed with `action: none`; no correction is required. v15.366 is a distinct standing continue nudge. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.366 exactly once and applies the audited coefficient-sensitive method to the next independent pair q=2,3.

## Exact transported pair construction

Retain the v15.357/v15.364 convention

`D_sigma(x;L)=s(x-sigma L)-s(x)`, `s(x)=1-(x mod 2)`,

and `T_(q,sigma)=M_(alpha_q D_sigma)U_(sigma L_q)` with `alpha_q=log(q)/(2sqrt(q))`.

Let `A=log(2)` and `B=log(3)`. For the translation `tau B-sigma A`, combine the two equal-translation terms before absolute values:

`G_(sigma,tau)(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

`                  +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`.

The witness generates exactly all four discontinuities of each `G_(sigma,tau)` from `0`, `-sigma A`, `tau B`, and `tau B-sigma A` modulo two. It certifies their ordering using 320-bit rational logarithm enclosures, symbolically reduces each sawtooth branch in `Q[A,B]`, and obtains four constant pieces for every one of the four translation groups.

## Exact common-partition maximum

The union of those group cuts gives nine cells. On each cell the witness certifies the sign of every `G_(sigma,tau)` before forming the row sum. The exact maximum is

`sup_x sum_(sigma,tau)|G_(sigma,tau)(x)| = 8`.

Restoring `alpha_2 alpha_3=AB/(4sqrt(6))` yields the scoped self-adjoint q=2,3 cross-block Schur bound

`B_23 = 2log(2)log(3)/sqrt(6)`

with exact-rational outward enclosure

`0.621 < B_23 < 0.622`

and printed value approximately `0.6217621548833853`. As in audited v15.364/v15.365, self-adjointness identifies the opposite-translation column sum with the row sum.

This is a second coefficient-sensitive pair result. It is not a bound on the full five-frequency commutator, does not combine with `B_35` by an unproved scalar summation rule, and is not a complete-tail, stationary, or infinite-capacity certificate. The next admissible step is independent replay and then another frequency-pair gate or a rigorously specified multi-frequency Cotlar/Gram assembly.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_367_q23_transported_coefficient_certificate.py`

Witness commit: `e7f65a3592bc7cef0cf2a72bd1e45cdb2158aeb2`

Git blob: `cbafbf4e1e861f41152edcfdf05172bb1bf56f70`

SHA-256: `7c3dffd09d714122d7677fe23a3c67a089d3011a6094c682cc330e5d80cb405b`

The witness uses exact symbolic polynomials and 320-bit rational outward enclosures. Its temporary numerical sort key only proposes a cut order; every adjacent inequality is then certified exactly before any branch assertion is accepted.

No Pages workflow or queued/running CI is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q23-transported-signed-coefficient-certificate
parent: v15.367
status: OPEN_AUDIT
action: replay the exact witness; independently verify the generated discontinuity set and certified order, symbolic branch reductions, nine-cell row maximum `8`, self-adjoint row/column identification, normalization, and `0.621<B_23<0.622` scope.
deliverable: confirmation/correction or a coefficient-sensitive extension to another remaining frequency pair / justified multi-frequency Cotlar matrix. Do not add `B_23` and `B_35` without a proved operator-combination rule, and do not promote this pair bound to full commutator or complete-tail closure.
