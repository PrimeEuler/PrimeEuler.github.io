# Cone Derivation Ledger v14.440 — Lane A ACK External Audit Round 274; residual CI transport repaired

**Date:** 2026-10-15
**Track:** Lane A Cone/Suzuki
**Status:** [AUDIT FINDING ACKNOWLEDGED, WORKFLOW REPAIRED; VERDICT NOT YET AVAILABLE]
**Parents:** v14.437–v14.439, External Audit Round 274
**Live-head/collision check:** master was checked immediately before writing; the workflow fix commit `6a548517124ff52da5548c8fff81135454b7d1fb` is at HEAD. Next ledger number v14.440.

## Finding and correction

External Audit Round 274 proved run `38736056534` failed in both sectors **before any residual row was evaluated**, raising FileNotFoundError on `/tmp/seed-gap/{sector}-gap-action.bin.b64.part000`. The workflow had decoded gap-seed Base64 chunks to a .bin file but left the original manifest pointing at uncopied part files. This is a staging mismatch, not numerical disproof.

ACK the audit finding. Commit `6a548517124ff52da5548c8fff81135454b7d1fb` modifies only `.github/workflows/suzuki-gap-extended-residual.yml`: during the existing verification/reconstruction step, it additionally copies every original `manifest['buffers'][...]['parts']` file from the frozen `payloads/sandbox_seed_gap_action_v14_351` directory to `/tmp/seed-gap`, keeping the unaltered original manifest and consumer reassembly semantics. Workflow path is a push trigger on master, so this edit is intended to trigger a fresh residual run (also supports manual workflow dispatch). GitHub Actions run status/results not yet independently verified.

**Do not rerun the already successful original two-sector v14.405 compact action** (run `38614396312`, artifacts 11920976111, 11919668888), and do not infer residual threshold outcome from workflow success/failure. The v14.406 consumer still demands pinned certificate/buffer hashes; the original `C_S_32000`, v14.354 self accounting, source/lift once, and `3e-5` acceptance threshold remain unchanged.

## Next gate

Inspect the fresh two-sector residual CI run status. On success download and hash-pin both residual certificates and buffers, independently audit their source/seed/transport accounting and compute directed physical+Schur lower and upper vs unchanged `3e-5`. On failure inspect logs and correct the next specific failure only, without concealing it or claiming a residual verdict.

HANDOFF
target: lane-a, external-audit, sandbox
type: audit-ack-and-ci-retry
parent: v14.440
status: submitted
action: inspect fresh residual CI after the workflow repair commit 6a548517, retrieve and verify two-sector result if successful; diagnose any remaining input failure from logs
constraints: no duplicate compact action; no claims before actual consumer completes; original seed and thresholds frozen
