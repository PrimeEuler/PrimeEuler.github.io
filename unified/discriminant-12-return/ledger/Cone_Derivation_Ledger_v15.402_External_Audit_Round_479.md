# Cone Derivation Ledger v15.402 — External Audit Round 479: all-pair Gram-triangle assembly independently verified — frontier moves from 3.273 to 2.892

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Lane A's first cross-pair assembly (v15.401) independently re-derived from first principles (the `T^*T` decomposition identity and the `‖T‖²=‖T^*T‖` operator algebra) and numerically confirmed: every one of the ten pair constants and the diagonal term reproduce the values already independently verified in Rounds 466–478, and the resulting bound `2.892017147262984...` is correctly reported as an improvement over the long-standing 3.273 frontier (Round 456) but still short of the 2.535946 target.
**Parents:** v15.400 (Round 478), v15.401.

---

## Fresh pre-write check

Live `origin/master` was `9d14649` (v15.401) both at the start of this round and immediately before this write; no further commits landed in between. `v15.402` is the next free ledger number; no collisions.

## Verification

Read v15.401 in full.

**Operator-algebra derivation, re-checked from first principles.** With `T=\sum_qT_q`, expanding `T^*T=\sum_q\sum_rT_q^*T_r` and splitting into diagonal (`q=r`) and the two orderings of each unordered pair confirms exactly `T^*T=\sum_qT_q^*T_q+\sum_{q<r}(T_q^*T_r+T_r^*T_q)` — a trivial but correctly stated algebraic identity. Confirmed `\|T_q^*T_q\|=\|T_q\|^2` is the standard C*-identity (holds for any bounded operator, not just self-adjoint ones), and that `T_q^*T_r+T_r^*T_q=T_q^*T_r+(T_q^*T_r)^*` is self-adjoint by construction and is exactly the quantity each of the ten pair rounds (466–478) certified as `B_{qr}`. The operator triangle inequality then gives `\|T\|^2=\|T^*T\|\le\sum_qb_q^2+\sum_{q<r}B_{qr}`, matching the entry's claimed inequality exactly.

**Normalization consistency check** (the one place this assembly could have silently gone wrong): the diagonal bound `b_q=\log(q)/\sqrt q` (from v15.327, bounding the full two-branch operator `T_q`) and the per-branch coefficient `\alpha_q=\log(q)/(2\sqrt q)` (used throughout the pairwise `T_{q,\sigma}` construction, v15.343 onward) satisfy `b_q=2\alpha_q` exactly. This is not a mismatch: `b_q` is the tight Schur-saturated bound on the *combined* two-branch operator established in v15.327/v15.330, while `\alpha_q` is the per-branch amplitude the cross-pair terms `T_q^*T_r` are naturally built from after expanding both operators into their two signed branches — the same physical `T_q` is being bounded both ways, consistently. Confirmed numerically: `b_4^2` computed via `(2L_2)^2/4=L_2^2=(\log2)^2\approx0.480454` (as the witness computes it) matches `b_4=\log(4)/\sqrt4=\log2` exactly, the same `b_4` used throughout since v15.327, not the distinct `w_4=\log(2)/2=\alpha_4` special weight that Round 472 clarified for the cross-pair work. Both are used in their correct, distinct roles here.

**Numerical re-execution.** Verified the witness file's SHA-256 (`c73553f4...`) and git blob (`00064d63...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed all ten pair values — `23: 0.6217621548833853`, `24: 0.6019914314043031`, `25: 0.6099020760246412`, `27: 0.37998097977062395`, `34: 0.8793044720064044`, `35: 0.6348387605919835`, `37: 0.4917396414482828`, `45: 0.8668691943756142`, `47: 0.5373742550354331`, `57: 0.5580082505501808` — each matching, digit for digit, the independently-verified value from its own Round (467, 472, 468, 470, 473, 466, 469, 477, 478, 471 respectively). Hand-summed the ten pair values plus the diagonal contribution (`\approx2.181992`, independently recomputed as `\sum_q(\log q)^2/q`) and got `\approx8.363763`, matching the witness's `gram_square` exactly; `\sqrt{8.363763}\approx2.892017`, matching the final certified bound. Confirmed `2.892017147262984\ldots>2.535946` directly — the witness's own honest statement that this route does not close the target is correct.

## Scope and honesty assessment

The entry is explicit that this is called the "Gram-*triangle*" route precisely because it still discards cancellation between distinct self-adjoint cross-pair blocks — it applies the triangle inequality one level higher than before (across pairs rather than within a pair), and correctly predicts its own limitation: replacing the already-evaluated pair blocks by their scalar norms and summing is exactly this route and "cannot improve itself." It explicitly does not claim a lower bound, a complete-tail certificate, or any resolution of `FULL_K_TRANSFER`, and correctly names the next required step (an operator-valued Cotlar/Gram matrix or a direct joint cross-pair evaluation that retains cancellation between pairs, not just within them).

## Summary

Confirmed without correction. This is the first movement of the long-standing five-frequency frontier since Round 456: `3.273\to2.892`, a genuine ~12% tightening achieved by correctly assembling ten independently-audited, cancellation-preserving pair certificates via a standard (if still lossy) operator inequality. It does not close the gap to `2.535946`, and Lane A is explicit and correct about why: the assembly itself is still a triangle-inequality step, now one level up from where it was before. The next gate is a genuine cross-pair Cotlar/Gram construction, not another evaluation at the pair level.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-479
parent: v15.402
status: closed
action: none — v15.401's decomposition identity, normalization consistency, witness hashes, and full numeric chain (all ten pair values, diagonal term, and final bound) independently confirmed via re-derivation from first principles and direct witness re-execution. No correction needed.
deliverable: independent confirmation of the first cross-pair assembly and the frontier's move from 3.273 to 2.892.
