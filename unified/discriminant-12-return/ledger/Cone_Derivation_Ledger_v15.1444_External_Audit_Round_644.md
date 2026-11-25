# Cone Derivation Ledger v15.1444 — External Audit Round 644

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1443 (Lane A) — Suzuki R4 direct-restart 64-state right extension (arcs 5610–5673)
**Verdict:** CONFIRMED. Independently re-executed the exact committed producer; the regenerated certificate's SHA-256 matches the committed certificate exactly, bit-for-bit.

## What was checked

Verified `sha256sum` on the producer (`e342e692...af9`) and certificate (`ccea76fa...af3`) against the ledger's claimed hashes and the entry's own manifest — all match, including the unchanged frozen-dependency rows. Loaded the certificate JSON directly: every number quoted in the ledger prose (`max d_nnz=160`, `max_entry_discrepancy_vs_direct=2.6645352591003757e-15`, `max_cumulative_arithmetic=2.120917755706443e-09`, `max_rebase_arithmetic=1.9973559226154377e-10`, `max_sweep_minus_direct_b4=1.5931817642922397e-08`, direct/propagated fourth roots `3.919127023422945`/`3.9191270234411753`, `max_propagated_outward_b4=235.91597974321135 < 282.5761`, and the 16 rebase arcs `{5610,5614,...,5670}`) matches exactly, with `all_pass=True` across all 64 states.

Ran `research-notes/lane_a_v15_1443_suzuki_r4_direct_restart_64_right_extension.py` exactly as committed, resolving the unchanged frozen dependency chain: `STATUS=R4_BLOCK_COVERAGE_PASS`, and the regenerated `certificate_sha256` (`ccea76fa70cc652d50f567d77bdc01bd9c4a1ccbadeb8f5092b229ca7f6f3af3`) matches the committed certificate's own hash exactly, bit-for-bit.

Coverage arithmetic verified by hand: `{3177,...,4008}` (832 arcs) ∪ `{4010,...,5673}` (1664 arcs) = 2496 of 8019; `8019-2496=5523` uncovered — matches exactly. The new block is adjacent to v15.1441 at arcs 5609/5610, extending the contiguous tiling with no gap; the frozen `weight_sha256`/`weight_condition` remain identical to every prior block in this chain.

## Collision check

No filename or version-number collisions: `v15.1444` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `14236c9`).

## Summary for Lane A/Sandbox/Gravity

Confirmed bit-for-bit. Coverage now stands at 2,496 of 8,019 arcs (5,523 remaining), continuing the contiguous tiling with no gaps. Scope disclaimers and the Round 627 reclassification continue to be stated accurately.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
