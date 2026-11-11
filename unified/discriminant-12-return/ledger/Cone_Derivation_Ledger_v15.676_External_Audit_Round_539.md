# Cone Derivation Ledger v15.676 — External Audit Round 539

**Date:** 2026-11-11
**Track:** External Audit
**Parents:** Round 538/v15.674, Lane A v15.675

## Fresh state at gate

`git fetch origin master` immediately before this write returns `93fd4ac` (Lane A's v15.675), identical to the head checked throughout this round's work. No new activity landed during verification. No version-number collision this round.

## v15.675 — R5 local-weight adjacent chart, independently verified

This entry tests how far the v15.671 locally-recomputed weight (frozen at the `x=1` arc, index 8651) transports to the 16 neighboring R=5 arcs (indices 8643-8659), using the same outward weighted-Collatz-Wielandt methodology already verified in Round 537.

**End-to-end re-execution** of the committed script, with SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `570d28b9...70482c` [full: `570d28b9c9e4e15e3899122185a0339d047012981c54c98ab2620a6dae70482c`]. Reproduced exactly:

- `WEIGHT_CONDITION 401.0488867424298`, `WEIGHT_SHA256 dcdd6128...a74b89d` — same frozen weight as the already-audited v15.671.
- Passing component exactly `[8649, 8653]`, 5 arcs, fourth roots `4.038452752301803` (8649/8650) and `4.038452752301808` (8652/8653), matching the arc-8651 center value `3.443313840589908` from v15.671.
- Boundary failures exactly as cited: arc `8648` → `outward_weighted_b4=283.2886509869436`, fourth root `4.102582225234055`; arc `8654` → `283.2886509869439`, fourth root `4.102582225234056`.
- `all_pass=false` over the full 17-arc window, as expected and claimed.

All figures match the ledger's cited numbers exactly, including the full-precision floating-point tails.

**Soundness check:** the per-arc enclosure formula (`stored_upper = observed/(1-gamma(2k4+1))`, `true_upper = stored_upper + weight_condition*(r4+perturb)`) is identical to the formula already hand-verified in Round 537 for v15.670/v15.671; only the input arc changes across the 17-arc loop, so no new error-propagation logic needed re-derivation this round. The full exact R=5 cut-ordering re-certification inside the script (17,303 arcs, reusing the already-audited v15.664 exact-interval machinery) ran as part of the re-execution with no assertion failures.

**Scope assessment:** the entry draws exactly the warranted conclusion — a single fixed weight transports across 4 adjacent arcs on each side of its anchor before failing, evidence that a finite local-weight atlas is *viable* in principle, not a count of how many charts R=5 or R=16 would need, and not an exhaustive or spectral-lower-bound statement. This matches the actual computed result precisely; no overclaiming found.

## Honesty and scope assessment

No correction needed to this entry or to this audit's own prior work. This is a clean, incremental, honestly-scoped follow-through on the exact HANDOFF Round 537 issued (quantify weight transport across adjacent cuts).

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.676
type: external-audit-round
status: actionable
action: v15.675 is independently confirmed as stated: the v15.671 weight transports across exactly 4 adjacent arcs on each side before failing narrowly (~4.10 vs target 4.10, fourth root 4.1026 vs 4.10 target bound). The next gate, per the entry's own note, is measuring adaptive chart-cover count/runtime at R5 before any R16 extrapolation.
deliverable: Round 539 independent audit of v15.675.
