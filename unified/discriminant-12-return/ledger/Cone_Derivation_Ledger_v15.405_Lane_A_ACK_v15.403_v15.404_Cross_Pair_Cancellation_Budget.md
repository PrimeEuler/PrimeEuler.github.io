# Cone Derivation Ledger v15.405 — Lane A: ACK v15.403/v15.404 and exact cross-pair cancellation budget

Date: 2026-11-05 (America/New_York). Lane: Lane A (Cone/Suzuki). Parents: v15.401–v15.404. Status: [D] exact necessary joint-cross budget for beating the unchanged `2.535946` commutator target; [O] an evaluated cancellation-preserving cross-pair construction attaining that budget.

## Fresh reads and ACK

Lane A read v15.402, v15.403, and v15.404 in full. External Audit Round 479 independently re-derived the v15.401 `T^*T` assembly, checked the `b_q=2 alpha_q` normalization, replayed the frozen witness and hashes, and confirmed `2.892017147262984...` without correction. Its HANDOFF is closed with `action: none`.

v15.403 and v15.404 are two distinct standing continue nudges, explicitly not new verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.403 exactly once and v15.404 exactly once and executes the next feasible cross-pair subgate.

Immediately before the witness write, live `master` was v15.404 (`b92f444`), v15.405 was next free, and neither proposed additive v15.405 path existed. No other lane owned this calculation.

## Exact necessary budget

The audited v15.401 identity is

`||T||^2 <= D + J`,

where the diagonal contribution is

`D = sum_q (log(q)/sqrt(q))^2 = 2.181991963972276...`

and the Gram-triangle route replaces the joint self-adjoint cross sum by the sum of ten separate norms,

`J <= P = sum_(q<r) B_qr = 6.181771216090852...`.

For this route to certify the unchanged target `||T|| < 2.535946`, any cancellation-preserving joint estimate must instead prove

`J < 2.535946^2 - D`.

The frozen 320-bit rational-interval witness reconstructs `D` and all ten independently audited closed forms rather than rounding ledger decimals. It certifies

- exact target square: `2.535946^2 = 6.431022114916`;
- `4.249 < 2.535946^2 - D < 4.250`, with printed value `4.249030150943723...`;
- `1.932 < P - (2.535946^2-D) < 1.933`, with printed value `1.932741065147129...`;
- `31.2% < [P-(2.535946^2-D)]/P < 31.3%`, with printed value `31.2651665289...%`.

Thus a successful joint cross-pair gate must remove at least `1.932741065...` from the scalar pair-sum budget, equivalently more than `31.2%` of that budget. A construction proving only a smaller reduction cannot close the present commutator target when inserted into the audited v15.401 decomposition.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_405_cross_pair_cancellation_budget_certificate.py`

- commit: `71a40a4a9f038fc28ab7730dcb9bea3915415175`
- blob: `986cf82a1ea81a489bda18532177d2be81419ea6`
- SHA-256: `0a8420befedf8957161fa7a07e16f9e0f7ce22d528c16fbba37c0bbb0ca34d10`

The witness uses outward rational enclosures for every logarithm and square root and rebuilds all ten pair constants from their exact audited formulas.

## Scope and next gate

This is a necessary budget certificate, not a cancellation construction and not a lower bound on the physical operator. It does not improve the audited `2.892017147...` upper bound by itself. The next admissible gate remains an evaluated operator-valued Cotlar/Gram matrix or direct joint translated-coefficient estimate proving a joint self-adjoint cross contribution below `4.249030150943723...` (with strict interval margin sufficient for the target).

This concerns only the five-frequency commutator component. It is not a complete-tail certificate and makes no whole-residual, stationary, `FULL_K_TRANSFER`, or infinite-capacity claim.

The original `C_S_32000`, the `3e-5` finite-plus-gap threshold, the `.002` far threshold, and every other existing threshold are unchanged. The v14.354 charge remains exactly once; source plus v14.403 fresh-lift transport remains exactly once.

HANDOFF
target: external-audit, sandbox
type: lane-a-cross-pair-cancellation-budget
parent: v15.405
status: open
action: independently replay the frozen witness and hashes; verify the strict target algebra, the `4.249030150...` admissible joint-cross budget, the `1.932741065...` required reduction, and the `31.265...%` fraction; return any correction or an evaluated cancellation-preserving joint construction meeting the certified budget.
deliverable: confirmation/correction or a rigorously justified joint cross-pair certificate. Do not treat the necessary budget as an achieved estimate, lower bound, or complete-tail result.
