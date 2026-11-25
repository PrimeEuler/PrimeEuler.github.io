# Cone Derivation Ledger v15.1442 — External Audit Round 643

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1441 (Lane A) — Suzuki R4 direct-restart 64-state right extension (arcs 5546–5609)
**Verdict:** CONFIRMED. Independently re-executed the exact committed producer; the regenerated certificate's SHA-256 matches the committed certificate exactly, bit-for-bit.

## What was checked

Verified `sha256sum` on the producer (`e56f30cf...aac`) and certificate (`62cf1123...ccf`) against the ledger's claimed hashes and the entry's own manifest — all match, including the unchanged frozen-dependency rows. Loaded the certificate JSON directly: every number quoted in the ledger prose (`max d_nnz=160`, `max_entry_discrepancy_vs_direct=2.6645352591003757e-15`, `max_cumulative_arithmetic=2.07879664957218e-09`, `max_rebase_arithmetic=1.997355922615438e-10`, `max_sweep_minus_direct_b4=2.3480822619603714e-08`, direct/propagated fourth roots `3.911526078677253`/`3.9115260787160686`, `max_propagated_outward_b4=234.09110969427778 < 282.5761`, and the 16 rebase arcs `{5546,5550,...,5606}`) matches exactly, with `all_pass=True` across all 64 states.

Ran `research-notes/lane_a_v15_1441_suzuki_r4_direct_restart_64_right_extension.py` exactly as committed, resolving the unchanged frozen dependency chain: `STATUS=R4_BLOCK_COVERAGE_PASS`, and the regenerated `certificate_sha256` (`62cf112350c97f6c0766b9008da95e73aea33212b295a2c7eb23f0f9d864accf`) matches the committed certificate's own hash exactly, bit-for-bit.

Coverage arithmetic verified by hand: `{3177,...,4008}` (832 arcs) ∪ `{4010,...,5609}` (1600 arcs) = 2432 of 8019; `8019-2432=5587` uncovered — matches exactly. The new block is adjacent to v15.1438 at arcs 5545/5546, extending the contiguous tiling with no gap; the frozen `weight_sha256`/`weight_condition` remain identical to every prior block in this chain.

## Collision check

No filename or version-number collisions: `v15.1442` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `aa83549`).

## Summary for Lane A/Sandbox/Gravity

Confirmed bit-for-bit. Coverage now stands at 2,432 of 8,019 arcs (5,587 remaining), continuing the contiguous tiling with no gaps. Scope disclaimers and the Round 627 reclassification continue to be stated accurately.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
