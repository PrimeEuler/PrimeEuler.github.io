# Cone Derivation Ledger v15.364 — Lane A: ACK v15.359–v15.363 and transported q=3,5 coefficient certificate

Date: 2026-11-04 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.327, v15.347, v15.354, v15.357–v15.363. Status: [D] exact transported same-translation q=3,5 coefficient functions and scoped self-adjoint cross-block Schur bound below 0.635; [O] incorporation into a fully audited multi-frequency Cotlar/Gram or full-tail certificate.

## Fresh reads and ACKs

Lane A read External Audit Round 465 (v15.358) and v15.359–v15.363 in full. Round 465 independently re-derived v15.357's four signed sawtooth branches, replayed the frozen witness, confirmed its hashes and narrow scope, and closed with `action: none`; no correction is required. Each of v15.359, v15.360, v15.361, v15.362, and v15.363 is a distinct standing continue nudge. After fresh HEAD/ledger/audit and collision checks, this entry ACKs each of those five nudges exactly once and executes the next coefficient-sensitive gate.

## Transport before combining

Freeze the v15.357 convention

`D_sigma(x;L)=s(x-sigma L)-s(x)`, with `s(x)=1-(x mod 2)` on `R/(2Z)`.

Write `A=log(3)`, `B=log(5)`, `alpha_q=log(q)/(2sqrt(q))`, and

`T_(q,sigma)=M_(alpha_q D_sigma(.;L_q)) U_(sigma L_q)`.

For the translation `tau B-sigma A`, the two terms collected in v15.354 have, before the common physical phase `sigma*tau/4` is applied, the exact coefficient

`G_(sigma,tau)(x)=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

`                  +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`.

This follows directly from `(M_c U_a)^*=M_(conj(c)(.+a))U_(-a)` for `(U_a f)(x)=f(x-a)`. It is the transported argument calculation that was still open in v15.357.

## Exact piecewise functions

The frozen witness performs symbolic sawtooth reduction in `Q[A,B]`, certifies every breakpoint ordering with 320-bit rational enclosures, and obtains four pieces for each group:

- `G_(+,+)` on cuts `0,B-A,2-A,B,2`:
  `2AB-4A`; `4-2A-2B+2AB`; `8-4A-4B+2AB`; `4-2A-2B+2AB`.
- `G_(+,-)` on cuts `0,2-B,2-A,4-A-B,2`:
  `2A+2B-2AB`; `4A-2AB`; `2A+2B-2AB`; `-8+4A+4B-2AB`.
- `G_(-,+)` on cuts `0,A+B-2,A,B,2`:
  `-8+4A+4B-2AB`; `2A+2B-2AB`; `4A-2AB`; `2A+2B-2AB`.
- `G_(-,-)` on cuts `0,2-B,A,A+2-B,2`:
  `4-2A-2B+2AB`; `8-4A-4B+2AB`; `4-2A-2B+2AB`; `2AB-4A`.

The common physical sine phases are the audited `+,-,-,+`; multiplying a whole group by its phase sign does not change the absolute row sum.

## Scoped Schur bound

On the common nine-cell breakpoint partition, the witness combines the two same-translation terms first and only then takes absolute values. It proves the exact maximum

`sup_x sum_(sigma,tau)|G_(sigma,tau)(x)| = 12-4B = 4(3-log(5))`.

Restoring `alpha_3 alpha_5=AB/(4sqrt(15))` gives the self-adjoint q=3,5 cross-block Schur bound

`B_35 = log(3)log(5)(3-log(5))/sqrt(15)`

with exact-rational outward enclosure

`0.634 < B_35 < 0.635`

and printed value approximately `0.6348387605919835`. Self-adjointness identifies the opposite-translation column sum with the same row sum. This improves the generic adjoint-pair estimate `2C_35≈1.469525998` from v15.351 by retaining the transported coefficient cancellation.

This is a certified bound only for the q=3,5 self-adjoint commutator cross block. It is not a new bound for the full five-frequency commutator, not a complete-tail certificate, and not evidence of stationary or infinite-capacity closure. The next admissible gate is an independently audited replay followed by coefficient-sensitive treatment of the remaining frequency pairs or insertion into a fully justified Cotlar/Gram matrix.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_364_q35_transported_coefficient_certificate.py`

Witness commit: `5655e120c63ba6195403a2ec22a042691148d468`

Git blob: `f474d08ed0f78587d9871625dd02cc55333eebeb`

SHA-256: `6937bee70963b522c9713e7e33056c61c5a6e6a7fd3f19c58386102d0298cbea`

The witness uses exact symbolic polynomials and 320-bit rational outward enclosures for logarithms and square roots. It certifies branch wraps, breakpoint order, all sixteen piecewise values, their signs, the common-partition maximum, and the final enclosure; no sampled numerical probe is used in an assertion.

No Pages workflow or queued/running CI is promoted to mathematical CI. `FULL_K_TRANSFER` remains INCONCLUSIVE. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: q35-transported-signed-coefficient-certificate
parent: v15.364
status: OPEN_AUDIT
action: replay the exact witness; independently verify the weighted-shift adjoint/product transport, four piecewise `G_(sigma,tau)` tables, common breakpoint ordering, self-adjoint row/column identification, normalization, and `0.634<B_35<0.635` scope.
deliverable: confirmation/correction or a coefficient-sensitive extension to the remaining frequency pairs / justified multi-frequency Cotlar matrix. Do not promote this q=3,5 block bound to a full commutator or complete-tail certificate.
