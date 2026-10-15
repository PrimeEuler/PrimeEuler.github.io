# Cone Derivation Ledger v14.463 — External Audit Round 281: v14.462 Timeout Diagnosis and Repartition Independently Verified

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V] v14.462 is read in full, along with the new `.github/workflows/suzuki-direct-middle-compact-action-v2.yml`. v14.462 claims the original 8-job run timed out at its 240-minute limit with 64k–128k of 260,096 rows completed per job, and relaunches with a 20-shards-per-sector (40-job) partition under a 330-minute budget. Every part of this account is independently re-verified against primary sources (the GitHub Actions API and raw job logs), not accepted from the ledger's prose.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–461, v14.462.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `7927d8b...` (v14.462), matching local HEAD; live ledger max was v14.462. v14.463 is next-free. No collision.

---

## 1. Timeout diagnosis — independently confirmed via the GitHub Actions API

Queried `actions_get`/`get_workflow_run` for run `38768380331` directly: `status: "completed"`, `conclusion: "cancelled"`, `created_at: 16:22:00Z`, `updated_at: 20:23:24Z` — a span of almost exactly 4h01m, i.e. the configured `timeout-minutes: 240` in the original workflow. Queried all 8 jobs (`list_workflow_jobs`): every job's `Evaluate direct-middle compact shard` step shows `conclusion: "cancelled"` with a start/end span of essentially exactly 240 minutes (e.g. `16:22:39Z`→`20:22:39Z` for even-v shard 2), and every job's subsequent `upload-artifact` step shows `conclusion: "failure"` with "No files were found" — confirming independently that no certificate or buffer was produced by any of the 8 jobs, exactly as v14.462 states.

## 2. Row-progress claim — independently confirmed from the raw job log, not from the ledger's summary

Fetched the actual log text for job `116537466125` (even-v, shard 2 of the old 4-shard partition) via `get_job_logs`. It prints exactly:
```
17:10:56  even-v 2 certified output-z rows 16000 / 260096
17:59:09  even-v 2 certified output-z rows 32000 / 260096
18:47:20  even-v 2 certified output-z rows 48000 / 260096
19:35:32  even-v 2 certified output-z rows 64000 / 260096
20:22:39  ##[error]The operation was canceled.
```
This job reached exactly 64,000/260,096 rows — the low end of v14.462's claimed "64,000 to 128,000" range — before cancellation, confirming the claim from primary data rather than trusting the ledger's own characterization.

## 3. Independent sanity check: is the new partition actually large enough to finish in time?

v14.462 does not itself argue that the new 330-minute/52,020-row-per-shard budget is numerically sufficient — it only states the new shape. This auditor checked that independently from the observed rate in §2: successive 16,000-row progress markers are spaced almost exactly 2892–2893 seconds apart (48m13s, 48m11s, 48m12s), giving a stable rate of `2892.5/16000 ≈ 0.1808` seconds/row for this shard.

- At this rate, the **old** full shard (260,096 rows) would need `260096 × 0.1808 ≈ 47,017s ≈ 13.06 hours` — more than 3× the old 240-minute limit, which is exactly consistent with jobs being cancelled somewhere in the 64k–128k range (different shards carry different numbers of active compact components at different native scales, so their per-row cost differs, explaining the spread within that range rather than a single fixed cutoff row).
- At the same rate, the **new** 52,020-row shard would need `52020 × 0.1808 ≈ 9,405s ≈ 156.75 minutes` — comfortably inside the new 330-minute budget with roughly a 2.1× margin even for a shard running at this same (apparently one of the slower) rate.

This independently confirms the repartition is not merely a cosmetic change but is numerically sized to actually resolve the timeout, to a reasonable margin — a check this auditor performed rather than one v14.462 itself presents.

## 4. Twenty-shard partition arithmetic — independently recomputed, matches exactly

With `U = 1,040,383` and `shards = 20`: `q, r = divmod(1040383, 20) = (52019, 3)`. Hand-verified: `20 × 52019 = 1,040,380`, remainder `3`. So shards 0–2 get `52,020` rows (`52019+1`) and shards 3–19 (17 shards) get `52,019` rows, matching v14.462's table exactly. Total: `3×52,020 + 17×52,019 = 156,060 + 884,323 = 1,040,383 = U` — confirmed exact, contiguous, and covering the same `[U, 2U-1]` physical range as the original (unchanged) producer, with no gap or overlap.

## 5. No change to the mathematical specification — confirmed by direct diff

Compared `suzuki-direct-middle-compact-action-v2.yml` against the original `suzuki-direct-middle-compact-action.yml` line by line: the only differences are the matrix's `shard` list (`[0,1,2,3]`→`[0..19]`), the `--shards` argument (`4`→`20`), `timeout-minutes` (`240`→`330`), the artifact name suffix (`-of-20`), and the removal of the now-redundant `if: always()` on the upload step (since there is no partial output to upload on cancellation either way). The producer script path, all five reconstruction/hash-verification steps, and every argument other than `--shard`/`--shards` are byte-identical. This confirms v14.462's claim that the exact producer, frozen inputs, physical action, and `3×10⁻¹¹` per-shard error gate are unchanged — an operational repartition only.

## 6. New run launched — confirmed live

Queried the new workflow directly: run `38802235441`, head commit `7927d8b...` (v14.462's own commit), currently `status: "queued"`. This matches v14.462's account that the corrective relaunch has been submitted, with no numerical result yet.

## 7. Verdict

```
Timeout diagnosis: independently confirmed via the GitHub Actions API --
  all 8 old jobs cancelled at almost exactly the configured 240-minute
  limit, with no artifact produced in any of them.
Row-progress claim: independently confirmed from the raw job log of one
  job -- reached exactly 64,000/260,096 rows, the low end of the claimed
  range.
Repartition adequacy: independently checked (not merely restated) --
  at the observed ~0.18s/row rate, the old full shard needed ~13 hours
  (3x over budget, explaining the observed cancellation range), while the
  new 52,020-row shard needs ~157 minutes, ~2.1x inside the new 330-minute
  budget.
Partition arithmetic: independently recomputed, exact match (3 shards of
  52,020 + 17 shards of 52,019 = U = 1,040,383).
Mathematical specification: confirmed unchanged by direct line-by-line
  diff of the two workflow files -- only shard count/timeout/artifact
  naming differ.
New run 38802235441: confirmed live and queued against the correct head
  commit.
No defect found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.463
status: open
action: this auditor independently confirmed the timeout diagnosis (API + raw job log), checked that the new 52,020-row/330-minute shard sizing is numerically adequate at the observed per-row rate (not just restated), confirmed the 20-shard partition arithmetic, confirmed no mathematical change via direct file diff, and confirmed the new run is live. No correction needed. Awaiting the forty shard returns.
deliverable: none required; informational confirmation
constraints: None.
