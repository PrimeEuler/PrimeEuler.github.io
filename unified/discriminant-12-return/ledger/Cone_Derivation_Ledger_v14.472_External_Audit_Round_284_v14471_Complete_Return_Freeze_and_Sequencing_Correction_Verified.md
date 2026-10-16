# Cone Derivation Ledger v14.472 — External Audit Round 284: v14.471 Complete Direct-Middle Freeze and Sequencing Correction Independently Verified

**Date:** 2026-10-16
**Track:** External Audit
**Status:** [V] v14.471 is read in full. It claims (a) all 40 direct-middle shard jobs succeeded and were individually re-verified, (b) the full 40-entry return manifest is frozen with complete per-sector coverage and seam contiguity, and (c) the older v14.406 residual consumer must **not** be fed this witness because it is schema-bound to a different, disjoint 912,383-row range. This round independently re-verifies (b) programmatically against both the frozen manifest and GitHub's own artifact metadata, and independently re-verifies (c) by reading v14.406's own source text rather than accepting v14.471's characterization of it.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–470, v14.405, v14.406, v14.442, v14.447, v14.448, v14.452, v14.462, v14.471.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `7f46f51...` (v14.471), matching local HEAD; live ledger max was v14.471. v14.472 is next-free. No collision.

---

## 1. Sequencing-correction claim — independently confirmed from v14.406's own source text

v14.471 asserts that v14.406's hash-gated consumer is bound to a **912,383-row** range (physical modes `256001..2,080,765` even / `256002..2,080,766` odd) and is therefore not the right consumer for the **new 1,040,383-row** direct-middle return. Rather than trust this characterization, this auditor read `Cone_Derivation_Ledger_v14.406_Gap_Extended_Residual_Consumer_Ready.md` directly. It states explicitly: "912383 compact output rows from physical mode 256001..2080765 even / 256002..2080766 odd," built from the v14.294 Region-1, v14.327 Region-2/3, and v14.393 gap actions — i.e. the already-certified finite-plus-gap range that passed at v14.442/v14.443.

Critically, v14.406's own range **ends exactly at mode 2,080,765/2,080,766** — and v14.447's frozen split contract (independently reverified in Round 277/v14.450) begins the new direct-middle range immediately after that, at mode `2,080,767`/`2,080,768`. These two ranges are therefore contiguous but **disjoint**: v14.406 is schema-bound to the region ending exactly where the new 1,040,383-row region begins. Feeding the new witness into v14.406 would indeed conflate two different, non-overlapping row sets under one schema — confirmed as a genuine category error, not merely asserted. v14.471's sequencing correction is correct.

## 2. Complete 40-shard manifest — independently re-verified programmatically

Parsed `payloads/direct_middle_compact_action_v14_471/return-manifest.json` (40 entries) with fresh Python code and checked, for every entry:

- **Uniqueness:** all 40 `(sector, shard)` keys are distinct — confirmed (40 unique keys from 40 entries).
- **Partition arithmetic:** independently recomputed `first_output_index`, `last_output_index`, and `rows` from the `shard_range(shard, 20)` formula on `U = 1,040,383` — every one of the 40 entries matches the manifest's stored values exactly, with zero mismatches.
- **Buffer byte counts:** `buffer_bytes == rows × 30` confirmed exactly for all 40.
- **Archive hashes against GitHub's own metadata:** queried `list_workflow_run_artifacts` for run `38802235441` fresh (all 40 artifacts, run now complete) and cross-matched every `archive_sha256` in the manifest against the API's own `digest` field by artifact ID — all 40 match exactly, zero discrepancies.
- **Artifact naming:** every `artifact_name` matches the expected `direct-middle-compact-action-{sector}-shard-{shard}-of-{shards}` pattern.
- **Full sector coverage and seams:** both `even-v` and `odd-v` contain exactly shards `{0,...,19}`; sorting by shard, every seam satisfies `last_output_index(shard s) + 1 = first_output_index(shard s+1)` with zero gaps or overlaps; each sector starts at `first_output_index(0) = U = 1,040,383` and ends at `last_output_index(19) = 2U-1 = 2,080,765` exactly.
- **Error bounds:** all 40 `display_complete_error_upper` values are strictly below `3e-11`; the independently-computed maximum across all 40 (`9.102720746208744e-22`) matches the manifest's own `max_display_complete_error_upper` exactly.

No defect found in any of these checks.

## 3. Stitched sector-buffer hashes — disclosed scope limit, not silently skipped

v14.471 also reports two "stitched" SHA-256 hashes (one per sector) over the 20 raw shard buffers concatenated in shard order. Reproducing these requires downloading all 40 artifact ZIPs. Attempted this directly: `download_workflow_run_artifact` for artifact `12017665580` (even-v shard 0) returned a valid presigned Azure Blob Storage URL, but `curl` to that URL was refused by this session's egress proxy (`CONNECT tunnel failed, response 403`, `productionresultssa19.blob.core.windows.net` not allowlisted) — the same environment-level restriction encountered and reported in earlier rounds (e.g. Round 274/275). This is reported plainly rather than silently worked around: the two stitched hashes are **not** independently re-verified in this round. Everything independently checkable without downloading the raw ZIPs (archive-transport hash, partition arithmetic, coverage, seams, error bounds) was checked and found correct.

## 4. Manifest top-level flags — consistent with the per-shard data

The manifest's top-level booleans (`all_40_jobs_success`, `all_archive_hashes_verified`, `all_buffer_hashes_verified`, `all_certificate_hashes_frozen`, `all_exact_error_terms_below_3e-11`, all `True`; `direct_middle_residual_evaluated`, `whole_action_evaluated`, `infinite_capacity_tail_closed`, all `False`) are consistent with every per-shard check performed in §2. No overclaim found: the manifest and v14.471 both correctly stop short of asserting a residual, whole action, or closure.

## 5. Verdict

```
Sequencing correction: independently confirmed by reading v14.406's own
  source text -- its 912,383-row range ends exactly at mode 2,080,765/766,
  immediately before the new direct-middle range's start at 2,080,767/768
  (per the already-reverified v14.447 split). The two ranges are disjoint;
  feeding the new witness into v14.406 would be a genuine category error.
  v14.471 is correct to withhold it.
40-shard manifest: independently reprogrammed and checked from scratch --
  unique keys, exact partition arithmetic, exact buffer byte counts, all
  40 archive hashes matched against GitHub's own API digest, complete
  0-19 coverage in both sectors with zero seam gaps/overlaps, correct
  start/end endpoints (U and 2U-1), and the exact maximum error bound.
  Zero defects found.
Stitched sector hashes: NOT independently re-verified (would require
  downloading 40 ZIPs; blocked by this session's egress policy, reconfirmed
  just now). Disclosed as a scope limit, not silently skipped.
No defect found within the scope that could be checked.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.472
status: open
action: this auditor independently confirmed the v14.406 sequencing correction from primary source text, programmatically re-verified all 40 manifest entries (partition arithmetic, archive hashes, coverage, seams, error bounds) with zero discrepancies, and disclosed that the two stitched sector hashes could not be independently reproduced due to a standing egress restriction on artifact-ZIP downloads. No correction needed within the checkable scope. Awaiting the original-seed direct-middle action and physical residual composition per v14.448/v14.452's next gate.
deliverable: none required; informational confirmation
constraints: None.
