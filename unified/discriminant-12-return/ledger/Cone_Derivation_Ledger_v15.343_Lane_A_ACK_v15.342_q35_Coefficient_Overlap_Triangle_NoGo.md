# Cone Derivation Ledger v15.343 — Lane A: ACK v15.342 and q=3,5 coefficient-overlap triangle NO-GO

Date: 2026-11-03 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.340–v15.342. Status: [D] first exact off-diagonal coefficient-overlap pair evaluated; triangle summation of the four signed q=3,5 products is strictly worse than the generic block product; [O] cancellation-preserving cross-product or joint full-tail bound below 2.535946.

## Fresh reads and ACK

Lane A read External Audit Round 460 (v15.341) and the v15.342 liveness entry in full. Round 460 independently verifies v15.340 without correction and closes with `action: none`. v15.342 is a distinct continue nudge, explicitly a standing check-in rather than verification work. After fresh HEAD/ledger/audit and collision checks, this entry ACKs v15.342 exactly once and evaluates the first actual coefficient-shift overlap.

The frozen witness was added at `49c61601885c362fc5e006b2fe68a48afd38b9d0`. Immediately before this ledger write, live `master` was that witness commit, `v15.343` remained the next free ledger number, and the proposed additive ledger path was absent.

## Exact q=3,5 signed overlap geometry

Use the v15.327 signed weighted-shift coefficients with `L_q=log(q)` and `k_q=L_q/(2 sqrt(q))`. Since `1<L_3<L_5<2`, each signed coefficient has a high branch `k_q L_q` on its edge interval and a low branch `k_q(2-L_q)` elsewhere.

For both off-diagonal products `T_3^*T_5` and `T_3T_5^*`, translating the step intervals according to the signed shifts and taking the supremum of each of the four signed products yields exactly two high-high maxima and two low-high maxima. The signed-term triangle estimate is therefore

`C_35 = 2 k_3 k_5 [L_3 L_5 + (2-L_3)L_5]`

`= 4 k_3 k_5 L_5 = b_3 b_5 L_5`,

where `b_q=L_q/sqrt(q)` is the audited v15.327 block bound.

The exact-rational witness certifies

`0.456 < b_3 b_5 < 0.457`,

`0.734 < C_35 < 0.735`,

and specifically

`b_3 b_5 < C_35 = b_3 b_5 log(5)`.

The printed outward value is

`C_35 = 0.734762998873283335043993247382...`.

Thus replacing the q=3,5 block cross-product by the triangle sum of its four signed coefficient-overlap norms makes the Cotlar input worse by the exact factor `log(5)>1`. Its square-root Cotlar entry is likewise worse by `sqrt(log(5))`.

## Consequence and narrow scope

This is the first evaluated coefficient-overlap pair, but it closes only the route that takes norms of the four signed translated products separately and then sums them. It does not determine the norm of their signed operator sum. Cancellation among the four distinct cross translations may still reduce `T_3^*T_5` or `T_3T_5^*`, and retaining that cancellation is now mandatory. The other frequency pairs, nonconstant Fourier weights, and joint cancellation with the Hankel/anticommutator and remaining kernel pieces remain open.

The `0.734...` value is an upper estimate produced by this signed-term triangle route, not a lower bound on the actual cross-product norm or physical commutator. No full-tail conclusion follows.

## Frozen witness

Path: `unified/discriminant-12-return/research-notes/lane_a_v15_343_q35_coefficient_overlap_triangle_nogo.py`

Witness commit: `49c61601885c362fc5e006b2fe68a48afd38b9d0`

Git blob: `d824dec36eecbc9cea63bb75cbf6f0eb6f7c1942`

SHA-256: `07db2a946d16b79f8d536cedff3036ea6bc7a6192a4ca78a3f2c07f6a87242b9`

The witness uses 320-bit exact-rational outward enclosures for logarithms and square roots. The two-HH/two-LH branch geometry is the analytic part of the certificate.

`FULL_K_TRANSFER` remains INCONCLUSIVE. No finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 far FAIL, and the exactly-once v14.354 and source+v14.403 transport charges remain unchanged. Pages is not mathematical CI.

**HANDOFF**

target: external-audit, sandbox
type: q35-coefficient-overlap-triangle-nogo
parent: v15.343
status: OPEN_AUDIT
action: replay the exact-rational witness and verify the signed weighted-shift convention, translated step-interval geometry for both product orientations, two-HH/two-LH maxima, exact factor log(5), hashes, and narrow scope. Continue by retaining cancellation among the four cross translations rather than summing their norms.
deliverable: confirmation/correction or a cancellation-preserving q=3,5 cross-product norm bound useful in a full Cotlar matrix. Do not promote `C_35` to a lower bound or full-tail certificate.
