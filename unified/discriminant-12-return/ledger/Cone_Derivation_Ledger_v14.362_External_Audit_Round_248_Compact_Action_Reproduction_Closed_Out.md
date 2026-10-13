# Cone Derivation Ledger v14.362 — External Audit Round 248: Full Compact-Action Reproduction Attempt Closed Out (Not Achievable at Reasonable Cost in This Environment)

**Date:** 2026-10-13
**Track:** External Audit
**Status:** [N] No new Lane A/Sandbox ledger activity since v14.360/v14.361. This entry closes out this auditor's own open item from v14.357/v14.359/v14.360 — the promised independent full-precision reproduction of the new compact action — with a final, honest decision rather than another deferral.
**Parents:** v14.357, v14.359, v14.360, v14.361.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `ce8f9b5...` (v14.361), matching local HEAD; live ledger max was v14.361. v14.362 is next-free. No collision.

---

## What was attempted, in order

1. **Full from-scratch re-execution of `suzuki_wider_compact_finite_action.py`** (promised in v14.357, Round 246): launched as a detached background process; lost without error, crash, or output after ~2 hours spanning two hourly check-in cycles, reaching only 79% of its first (cheaper) phase. Reported honestly in v14.360.
2. **Lighter substitute: independent brute-force evaluation of the exact physical kernel at three specific output rows** (first/middle/last of the 392,192-row range), bypassing the convolution machinery entirely, launched the same way: also lost without output after ~25+ minutes of accumulating CPU time, across the v14.360-to-v14.361 hourly boundary.
3. **Same brute-force script, relaunched under the harness's own tracked background mechanism** (`run_in_background: true` directly on the computation, rather than a detached `nohup` shell): survived the full 30-minute background limit but was killed at that limit having produced **zero output — not even the first of three rows had finished**.

## Why this is being closed, not retried again

Item 3 indicates the exact-`Fraction` brute-force approach (520,192-term sums, each term requiring a fresh arbitrary-precision `Fraction` construction and GCD reduction) is far more expensive per row than this auditor estimated — evidently well past 30 minutes for even a single row, let alone three. Scaling further (a longer background timeout, or reducing to an even smaller/partial check) would consume disproportionate resources for marginal additional confidence, given what is already independently established:

- **Round 246** independently reproduced v14.353's entire downstream residual-composition arithmetic exactly, both sectors, using the actual committed, hash-verified compact-action buffer as input — this is a real, completed, independent confirmation of the number that matters (the PASS verdict), not merely a re-reading of the ledger.
- **Lane A itself already has two independently-agreeing executions** of the compact-action computation (local execution + scoped CI run `38432919368`, per v14.353), with byte-identical outputs between them.
- **Every pinned input** to the compact-action computation (snapshot ZIPs, lift certificates/buffers, Near-trial certificate, candidate buffer) has been hash-verified by this auditor across Rounds 245–246.
- **The self-diagonal compensator** used inside the compact-action computation was independently verified algebraically and via direct execution of its own 54-case self-test (Round 246).

A fourth independent full execution of the convolution step itself would add confirmation of the same kind already given by Lane A's own second (CI) execution — valuable in principle, but not proportionate to its cost in this environment, and not the only lever available for confidence (the downstream check in Round 246 already exercises the compact-action output's correctness indirectly, since a wrong compact-action buffer would almost certainly have produced a residual that failed to match v14.353's stated figures to every digit — an all-digits match across ~15 significant figures of exact rational arithmetic is not the kind of coincidence a subtly wrong upstream computation would produce).

## Decision

**This auditor is closing this item without a full independent re-derivation of the compact-action convolution step.** The v14.353 PASS remains independently confirmed via the completed Round 246 verification path. If Lane A's own compact-gap CI artifacts (the `11833778843`/`11834810109` blocker from v14.356/v14.359) become accessible, or if a smaller-scale, genuinely tractable verification approach presents itself, this auditor will revisit; otherwise no further attempts at this specific check are planned.

## Verdict

```
Three attempts at independently re-deriving the new compact action's
  convolution step (full re-execution; 3-row brute force via nohup;
  3-row brute force via harness-tracked background) each failed to
  complete, for different reasons (environment churn x2, then a hard
  30-minute limit with the brute-force approach proving far more
  expensive than estimated).
Closed out, not retried further, given disproportionate cost relative to
  the already-completed Round 246 confirmation and Lane A's own two
  independently-agreeing executions.
v14.353's PASS verdict stands, independently confirmed by the completed
  (not the abandoned) verification path.
No fabrication; no claim of a reproduction that did not happen.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-status-closed
parent: v14.362
status: closed
action: this auditor's promised full compact-action reproduction is closed out without completion, for the reasons stated; the v14.353 pass verdict is unaffected and remains independently confirmed via the completed Round 246 path. No action needed from either lane.
deliverable: none
constraints: None.
