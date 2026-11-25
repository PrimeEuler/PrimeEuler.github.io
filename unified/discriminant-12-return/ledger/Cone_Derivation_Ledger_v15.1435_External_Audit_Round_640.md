# Cone Derivation Ledger v15.1435 — External Audit Round 640

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1433, v15.1434 (Lane A) — two more Suzuki R4 direct-restart 64-state right extensions (arcs 5290–5353 and 5354–5417)
**Verdict:** Both CONFIRMED. Independently re-executed both exact committed producers; both regenerated certificates' SHA-256 match the committed certificates exactly, bit-for-bit. All quoted numbers and coverage arithmetic check out.

## v15.1433 (arcs 5290–5353): CONFIRMED

Verified `sha256sum` on the producer (`5c88ace3...a38`) and certificate (`8696683b...e50`) against both the ledger's claimed hashes and the entry's own manifest — all match, including the two frozen-dependency rows (v15.842, v15.800) against the files actually present in `research-notes/`. Loaded the certificate JSON directly: every field quoted in the ledger prose (`max d_nnz=160`, `max_entry_discrepancy_vs_direct=2.4424906541753444e-15`, `max_cumulative_arithmetic=1.98988305569565e-09`, `max_rebase_arithmetic=1.996808973252575e-10`, `max_sweep_minus_direct_b4=1.4562004935214645e-08`, direct/propagated fourth roots `3.9209983014986762`/`3.920998301539172`, `max_propagated_outward_b4=236.36687677717404 < 282.5761`, and the 16 rebase arcs `{5290,5294,...,5350}`) matches exactly, with `all_pass=True` across all 64 states. Ran `research-notes/lane_a_v15_1433_suzuki_r4_direct_restart_64_right_extension.py` exactly as committed, letting it resolve the unchanged frozen dependency chain: `STATUS=R4_BLOCK_COVERAGE_PASS`, and the regenerated `certificate_sha256` (`8696683bbd6ef00a2a97cffd9598c774396b75f431269feaf0f4220e6f4fae50`) matches the committed certificate's own hash exactly, bit-for-bit. Coverage arithmetic verified by hand: `{3177,...,4008}` (832 arcs) ∪ `{4010,...,5353}` (1344 arcs) = 2176 of 8019; `8019-2176=5843` uncovered — matches exactly.

## v15.1434 (arcs 5354–5417): CONFIRMED

Same checks, same result. Hashes verified (producer `6ef8c13c...1b`, certificate `4d14a312...77`) against both the ledger and the manifest. Certificate fields match the ledger prose exactly (`max_propagated_outward_b4=229.15326765244998 < 282.5761`, fourth roots `3.890733762287924`/`3.890733762305533`, 16 rebase arcs `{5354,5358,...,5414}`, `all_pass=True`). Ran the exact committed producer: `STATUS=R4_BLOCK_COVERAGE_PASS`, regenerated `certificate_sha256` (`4d14a312f98447ea15670144c96869ab6a4ee2b5e2472402daab14fa39212277`) matches the committed hash exactly, bit-for-bit. Coverage arithmetic verified by hand: `{3177,...,4008}` (832) ∪ `{4010,...,5417}` (1408) = 2240 of 8019; `8019-2240=5779` uncovered — matches exactly.

## Adjacency and chain integrity

Verified the three consecutive blocks (v15.1430: 5226–5289; v15.1433: 5290–5353; v15.1434: 5354–5417) tile contiguously with no gap or overlap: `5289/5290` and `5353/5354` are the stated adjacent boundaries, confirmed by the actual `min_arc`/`max_arc` fields in each certificate. The frozen `weight_sha256` (`466af76483...ea4`) and `weight_condition` (`25.619807022162554`) are identical across all three certificates, confirming the same frozen anchor weight was reused unchanged throughout, exactly as claimed.

## Collision check

No filename or version-number collisions: `v15.1435` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `d15747b`).

## Summary for Lane A/Sandbox/Gravity

Both new R4 blocks are confirmed bit-for-bit from committed producer bytes. Coverage now stands at 2,240 of 8,019 arcs (5,779 remaining), continuing contiguously from v15.1430 with no gaps. Scope disclaimers and the Round 627 Lane A reclassification continue to be stated accurately in both entries.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
