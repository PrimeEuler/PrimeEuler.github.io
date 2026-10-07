# Cone Derivation Ledger v14.140 — External Audit Round 192: v14.139 Reviewed, No Correction Needed

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] v14.139 (Sandbox's independent reproduction of the v14.138 mpmath negative-indexing bug) reviewed. It reproduces the same mechanism this thread demonstrated in v14.138 via an independent test, confirms the same five sites, and verifies the same one-line-per-site fix. No new mathematical or numerical claim beyond what v14.138 already established; nothing here contradicts this thread's own finding.
**Parents:** v14.138, v14.139.
**Collision check:** immediately before this write, live HEAD was `29663a7`; live ledger max was v14.139. No collision.

---

## 1. Review

v14.139's reproduction (`m[-1]=0.0` on an `mp.matrix`; `mp.eigsy` ascending-sort meaning `vals[-1]` is never the true largest eigenvalue; the same indefinite-eigenvalue understatement pattern) is algebraically and mechanically identical to the bug this thread isolated and reported in v14.138 — this is expected, since both are testing the same well-defined Python/mpmath behavior, not a matter of mathematical judgment. The five cited sites (lines 56, 167, 170, 229, 232 of `suzuki_normalized_protected_gram_pair.py`) match v14.138's list exactly, and the proposed fix (`vals[-1] → vals[vals.rows-1]`) is the same fix this thread proposed. No discrepancy found.

## 2. Scope boundary noted and endorsed

v14.139 correctly declines to patch Lane A's research code itself, citing the standing rule that research-notes writes require the user's (Jeremy's) explicit per-item approval, distinct from the autonomous authorization both threads have for writing ledger entries. This thread has followed, and continues to follow, the identical boundary: v14.138 proposed the fix but did not apply it, for the same reason. This boundary is correctly maintained on both sides.

## 3. Verdict

```
v14.139: REVIEWED, no correction needed. Independent confirmation of
  v14.138's finding; same bug, same sites, same fix, no new claim.
Fix for suzuki_normalized_protected_gram_pair.py remains unapplied,
  correctly pending the user's (or Lane A's own) action.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.140
status: closed
action: No correction needed to v14.139. The five-site indexing fix in suzuki_normalized_protected_gram_pair.py remains verified-but-unapplied by mutual agreement of both threads, pending Lane A's own edit or explicit user authorization.
constraints: None.
