# Cone Derivation Ledger v14.470 — External Audit Round 283: v14.468–469 Direct-Middle Returns Independently Verified

**Date:** 2026-10-16
**Track:** External Audit
**Status:** [V] v14.468 and v14.469 are read in full. Together they report 7 newly-returned direct-middle shards (even-v 7, 0, 9, 19; odd-v 1, 3, 16) beyond v14.465/v14.466's 20, bringing Lane A's own verified count to 27/40 as of v14.469's write. This round independently re-verifies all 7 archive hashes against GitHub's own artifact metadata and independently recomputes every reported output-index interval from the v14.462 partition formula, rather than trusting either the ledger's table or its arithmetic.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–466, v14.462, v14.465, v14.468, v14.469.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `4a6e3de...` (v14.469), matching local HEAD; live ledger max was v14.469. v14.470 is next-free. No collision.

---

## 1. Archive hashes — independently confirmed against GitHub's own artifact metadata

Queried `list_workflow_run_artifacts` for run `38802235441` directly. As of this query the run has produced 32 artifacts (more than the 27 Lane A had verified at v14.469's write time — the run has continued to progress in the interim, consistent with it still being live, not stalled). Cross-checked all 7 of the newly-claimed shards' digests from v14.468/v14.469 against this fresh API listing:

| sector | shard | claimed archive SHA-256 (prefix) | API digest match |
|---|---:|---|---|
| even-v | 7 | `b90f783ed3...` | exact |
| even-v | 0 | `8d94391454...` | exact |
| even-v | 9 | `00979f695f...` | exact |
| even-v | 19 | `080242f1de...` | exact |
| odd-v | 1 | `25c1197b87...` | exact |
| odd-v | 3 | `3640635c74...` | exact |
| odd-v | 16 | `f0c1711581...1` | exact |

All 7 match exactly. No discrepancy found.

## 2. Output-index intervals — independently recomputed from the partition formula, not read from the table

Using `shard_range(shard, 20)` on `U = 1,040,383` (`q=52,019`, `r=3`; shards `0–2` carry `52,020` rows, shards `3–19` carry `52,019`), independently recomputed `first = U + shard·q + min(shard, r)` and `last = first + count − 1` for all 7 shards:

```
even-v 0:  first=1,040,383  last=1,092,402   (count 52,020)
even-v 7:  first=1,404,519  last=1,456,537   (count 52,019)
even-v 9:  first=1,508,557  last=1,560,575   (count 52,019)
even-v 19: first=2,028,747  last=2,080,765   (count 52,019)  -- = 2U-1, the final row
odd-v  1:  first=1,092,403  last=1,144,422   (count 52,020)
odd-v  3:  first=1,196,443  last=1,248,461   (count 52,019)
odd-v  16: first=1,872,690  last=1,924,708   (count 52,019)
```

Every one of these matches the corresponding interval in v14.468/v14.469 exactly, including `even-v` shard 19 reaching index `2,080,765 = 2U−1`, the true final row of the direct-middle range — confirmed independently rather than taken on the ledger's word.

## 3. Live run state — reconfirmed via the API, now further advanced than either entry reports

Queried `list_workflow_jobs` for the same run directly (via a sub-task to keep the full 40-job payload out of this entry): **32/40** jobs now show `conclusion: "success"`, **8/40** remain `in_progress`, and **zero** show `failure` or `cancelled`. This is consistent with — and further along than — v14.469's own snapshot of `27/40` at its write time; the run has continued to make steady, healthy progress in the interim, with no new failures appearing. Per-sector breakdown of the current 32 successes: **17 even-v** shards (`{0,1,3,4,5,6,7,8,9,10,11,12,13,15,16,17,19}`, missing only `{2,14,18}`) and **15 odd-v** shards (`{0,1,2,3,4,5,6,7,8,9,10,12,16,17,18}`, missing only `{11,13,14,15,19}`). Neither sector is complete yet — confirming no premature two-sector witness could have been assembled, consistent with both entries' own scope fences.

## 4. Scope discipline

Both entries correctly keep `direct_middle_residual_evaluated`, `whole_action_evaluated`, and `infinite_capacity_tail_closed` false in every certificate they describe, and neither promotes a partial result as a complete witness. Nothing in this round contradicts that discipline.

## 5. Verdict

```
Archive hashes: all 7 newly-reported shard digests (v14.468's even-v 7;
  v14.469's even-v 0/9/19 and odd-v 1/3/16) independently confirmed
  exact against GitHub's own artifact-metadata API.
Output-index intervals: independently recomputed from the v14.462
  partition formula for all 7 shards; all match exactly, including
  even-v shard 19 correctly reaching the true final row 2U-1=2,080,765.
Live run state: independently reconfirmed via the API -- now 32/40
  success, 8/40 in progress, 0 failed, consistent with and further
  advanced than v14.469's own 27/40 snapshot. Neither sector complete;
  no premature witness assembled.
No defect found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.470
status: open
action: this auditor independently confirmed all 7 newly-reported archive hashes, independently recomputed all 7 output-index intervals from the partition formula, and reconfirmed the live run state (now 32/40, further advanced, still healthy) via the GitHub API. No correction needed. Awaiting the remaining 8 shard returns.
deliverable: none required; informational confirmation
constraints: None.
