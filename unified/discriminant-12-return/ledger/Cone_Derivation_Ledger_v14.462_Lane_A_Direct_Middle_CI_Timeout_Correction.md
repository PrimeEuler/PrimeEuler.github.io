# Cone Derivation Ledger v14.462 — Lane A: Direct-Middle CI Timeout Diagnosed and Additively Corrected

**Date:** 2026-10-15
**Track:** Lane A (Cone/Suzuki)
**Status:** [C] Read External Audit v14.460 and continue nudge v14.461 in full. No correction is required to the mathematical specification. After those entries were written, v14.452 run `38768380331` reached its explicit 240-minute job limit: all eight sector/shard jobs were cancelled during `Evaluate direct-middle compact shard`, and no artifact was produced. The exact producer, frozen inputs, physical action, `C_S_32000`, and every acceptance threshold remain unchanged. A new additive v2 workflow partitions the same two-sector 1,040,383-row block into twenty shards per sector (forty jobs total), at most 52,020 rows per job, with a 330-minute envelope.
**Parents:** v14.447–452, v14.455, v14.459–461.
**Collision check:** immediately before this write, live `master` was `3801d0226d80578713382428592a749b58524819` (v14.461); the v14.462 ledger path and additive v2 workflow path were absent. v14.462 is next-free.

---

## 1. ACK v14.460–461

Received v14.460's independent confirmation of the then-live v14.459 CI state and v14.461's explicit instruction to continue. v14.460 found no defect in the state it observed. v14.461's liveness sentence became stale when GitHub cancelled the jobs at the configured limit, but its authorization to continue remains applicable. This entry records acceptance and executes the next feasible corrective step in the same run.

## 2. Exact failure diagnosis

Run `38768380331` began at approximately `2026-10-15T16:22Z` and each job was cancelled at approximately `20:22Z`, matching the workflow's explicit `timeout-minutes: 240`.

All prerequisite gates succeeded in every job:

- checkout and Python setup;
- exact convolution dependency;
- reconstruction and hash verification of the actual256 witnesses;
- finite-correction reconstruction;
- reconstruction of the v14.403 RHS, output-z caches, and lift.

The only interrupted step was the fresh physical output-z evaluation. Representative final progress markers ranged from 64,000 to 128,000 completed rows out of approximately 260,096 per old shard. Each producer writes its certificate and buffer only after completing the whole shard, so cancellation left no files for `upload-artifact`; the subsequent upload failures therefore report absence of completed output, not a certificate or mathematical failure.

No partial progress is promoted or frozen.

## 3. Additive correction

Published `.github/workflows/suzuki-direct-middle-compact-action-v2.yml` without altering the v14.452 producer.

The new exact partition uses `--shards 20` independently in both sectors:

- (U=1{,}040{,}383);
- quotient (52{,}019), remainder (3);
- shards 0–2 contain 52,020 rows;
- shards 3–19 contain 52,019 rows;
- the intervals are contiguous and disjoint from output index (U) through (2U-1=2{,}080{,}765).

The workflow timeout is 330 minutes. This is an operational repartition only: the producer's per-row `evaluate_remote_z(..., action_precision=True)`, physical interval-radius charge, four compact input components, disjoint-support rule, pole pairing, input pins, and (3\times10^{-11}) per-shard physical-error guard are unchanged.

## 4. Gate status

This correction launches computation; it does not certify a direct-middle result. Lane A remains blocked on all forty exact shard certificates and buffers. After they return, the next gate is to verify hashes, schemas, input pins, complete interval coverage, seams, and per-shard error charges; then assemble the two sector buffers and continue residual composition. No direct-middle residual, whole-residual, stationary, or infinite-capacity closure is claimed.

---

HANDOFF
target: external-audit, sandbox
type: lane-a-timeout-correction-and-ci-launch
parent: v14.462
status: running
source: v14.460, v14.461, run 38768380331
received: clean audit of prior CI liveness and explicit authorization to continue
diagnosis: all eight old jobs hit the configured 240-minute limit during fresh output-z evaluation; all prerequisite hash gates passed; no output artifact existed
correction: additive twenty-shard-per-sector workflow with at most 52,020 rows per job and 330-minute timeout; exact producer and mathematical inputs unchanged
next-action: independently inspect the new run and, only after all forty certified artifacts return, verify/freeze and assemble the two-sector direct-middle witness
constraints: preserve original C_S_32000 and all existing thresholds; no use of cancelled partial progress; no closure inference
