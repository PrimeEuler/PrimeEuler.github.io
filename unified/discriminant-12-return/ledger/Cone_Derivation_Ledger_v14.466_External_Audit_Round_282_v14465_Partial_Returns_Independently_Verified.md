# Cone Derivation Ledger v14.466 — External Audit Round 282: v14.465 Partial Direct-Middle Returns Independently Verified

**Date:** 2026-10-15
**Track:** External Audit
**Status:** [V] v14.465 is read in full. It claims 20 of the 40 direct-middle v2 shard jobs have returned (11 even-v, 9 odd-v), with every certificate/buffer hash checked, all physical error bounds under `3e-11`, and no two-sector witness promoted. This round independently re-verifies the live CI state, the archive hashes, and the actual numerical content of two shards by pulling raw job logs directly — not by trusting v14.465's own manifest table.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–464, v14.462, v14.465.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `a2452a7...` (v14.465), matching local HEAD; live ledger max was v14.465. v14.466 is next-free. No collision.

---

## 1. Live job-state claim — independently confirmed via the GitHub Actions API

Queried `list_workflow_jobs` for run `38802235441` directly and parsed all 40 job records programmatically (not by reading the ledger's count): exactly `20` jobs have `status: "completed"` with `conclusion: "success"`, and exactly `20` have `status: "in_progress"` with no `conclusion` yet. Zero jobs show `failure` or `cancelled`. This matches v14.465's "20 completed successfully; 20 remain in progress; 0 failed or cancelled" exactly.

Breaking the 20 completed jobs down by sector independently: exactly `11` are `even-v` (shards `{1,4,5,6,8,10,11,12,13,15,17}`) and exactly `9` are `odd-v` (shards `{0,2,4,5,6,7,8,9,10}`) — matching v14.465's manifest table shard-for-shard, not merely in count.

## 2. Archive hashes — independently confirmed against GitHub's own artifact metadata

Queried `list_workflow_run_artifacts` for the same run directly: all 20 returned artifacts carry a `digest` field (GitHub's own SHA-256 of the uploaded ZIP, computed server-side at upload time). Cross-checked every one of the 20 digests against v14.465's manifest table by hand: all 20 match exactly (e.g. `odd-v` shard 2 → `6842c5757e...`, `even-v` shard 8 → `c508b0a0a5...`, `odd-v` shard 0 → `41e11a010d...`, and so on through all 20 rows). No discrepancy found.

## 3. Raw CI log content — independently pulled and checked against the claimed numbers, not read from the ledger

Fetched the actual job logs for two of the twenty completed jobs directly via `get_job_logs` (not reading any file Lane A summarized):

**even-v shard 8** (52,019 rows, confirmed by the log's own `"... rows 16000 / 52019"` progress lines): the script's final stdout line reads
```
{"complete_direct_middle_compact_action_error_upper": 9.102633253278207e-22,
 "final_row_rounding_charge_upper": 1.9697091828396992e-75,
 "offdiagonal_and_pole_parameter_charge_upper": 9.102633253278207e-22,
 "output_z_interval_action_charge_upper": 3.871705965075436e-48,
 "reciprocal_kernel_rounding_charge_upper": 3.144475002820732e-63}
```
`9.102633253278207e-22` rounds to `9.103e-22` — exactly the value v14.465 cites as "the largest displayed approximation among these 20 certificates." Independently confirmed from the raw log, not from the ledger's own statement, and also confirmed this is ~11 orders of magnitude below the `3e-11` per-shard gate, not a near-miss.

**odd-v shard 2** (52,020 rows, confirmed by its own `"... rows 16000 / 52020"` lines, consistent with shard 2 being one of the three oversized shards `{0,1,2}` in the 20-way partition): final stdout line reads `complete_direct_middle_compact_action_error_upper: 1.9129431594109862e-23` — also far under the gate, and consistent with shard-to-shard variation in the dominant `offdiagonal_and_pole_parameter_charge_upper` term (both shards show that term equal to the complete error to the displayed precision, with the interval/rounding terms many orders of magnitude smaller in both cases — an internally consistent error-budget shape across shards).

The upload step's own GitHub-computed SHA-256 for each ZIP (printed in-line in the raw log, e.g. `c508b0a0a5462bcf895641705bf0136a28ff4adb25b27ab8a352231f72f0b469` for even-v shard 8) matches both the artifact-API digest and v14.465's table — a third independent confirmation of the same hash from three different sources (raw upload log, artifact metadata API, ledger table), all agreeing.

## 4. Row-count coincidence — independently recomputed from the partition formula, confirmed exact

v14.465 notes the 20 returned shards "coincidentally" total exactly `U = 1,040,383` rows despite not being one complete sector. Recomputed independently from the 20-shard partition (shards `0–2` carry `52,020` rows each, shards `3–19` carry `52,019` each): even-v's 11 shards sum to `52,020 + 10×52,019 = 572,210`; odd-v's 9 shards sum to `2×52,020 + 7×52,019 = 468,173`. Total: `572,210 + 468,173 = 1,040,383 = U` exactly — confirmed as a genuine coincidence of this particular partial completion order, not an error in the ledger's count.

## 5. Scope discipline

Consistent with v14.465's own statement, no two-sector direct-middle witness, residual, or closure is claimed, and none is asserted here. `direct_middle_residual_evaluated`, `whole_action_evaluated`, and `infinite_capacity_tail_closed` all read `false` in both inspected certificates' underlying script output, matching the unchanged scope fence.

## 6. Verdict

```
Job-state claim (20 success / 20 in_progress / 0 failed): independently
  confirmed via the GitHub Actions API, including the exact per-sector
  shard-set breakdown (11 even-v, 9 odd-v), not just the totals.
Archive hashes: independently cross-checked against GitHub's own
  artifact-metadata digests for all 20 returned artifacts -- all match.
Raw numerical content: independently pulled from two raw job logs (not
  read from the ledger) -- even-v shard 8's error upper bound
  (9.1026e-22) exactly reproduces the claimed "largest ~9.103e-22" among
  the 20 certificates, and odd-v shard 2's (1.913e-23) is independently
  confirmed far under the 3e-11 gate as well.
Row-count coincidence: independently recomputed from the partition
  formula and confirmed exact (572,210 + 468,173 = 1,040,383 = U).
No defect found anywhere checked. No premature promotion of a partial
  result found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.466
status: open
action: this auditor independently confirmed the live job-state breakdown, cross-checked all 20 archive hashes against GitHub's own metadata, pulled two raw job logs directly to confirm actual numerical content (not merely the ledger's summary), and independently recomputed the row-count coincidence. No correction needed. Awaiting the remaining 20 shard returns.
deliverable: none required; informational confirmation
constraints: None.
