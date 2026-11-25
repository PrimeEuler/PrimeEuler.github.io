# Cone Derivation Ledger v15.1439 — External Audit Round 642

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1438 (Lane A) — Suzuki R4 direct-restart 64-state right extension (arcs 5482–5545)
**Verdict:** CONFIRMED. Independently re-executed the exact committed producer; the regenerated certificate's SHA-256 matches the committed certificate exactly, bit-for-bit.

## What was checked

Verified `sha256sum` on the producer (`bf3f09a1...551`) and certificate (`e59ecced...fb0`) against the ledger's claimed hashes and the entry's own manifest — all match, including the unchanged frozen-dependency rows. Loaded the certificate JSON directly: every number quoted in the ledger prose (`max d_nnz=160`, `max_entry_discrepancy_vs_direct=2.6645352591003757e-15`, `max_cumulative_arithmetic=2.3987155308802454e-09`, `max_rebase_arithmetic=1.9973559226154377e-10`, `max_sweep_minus_direct_b4=2.639711738083861e-08`, direct/propagated fourth roots `3.8792825238823845`/`3.8792825239586812`, `max_propagated_outward_b4=226.46737167292702 < 282.5761`, and the 16 rebase arcs `{5482,5486,...,5542}`) matches exactly, with `all_pass=True` across all 64 states.

Ran `research-notes/lane_a_v15_1438_suzuki_r4_direct_restart_64_right_extension.py` exactly as committed, resolving the unchanged frozen dependency chain: `STATUS=R4_BLOCK_COVERAGE_PASS`, and the regenerated `certificate_sha256` (`e59eccedee89cff9e39e8907c988ef00750c14f7aba292ec12547bcb87d49fb0`) matches the committed certificate's own hash exactly, bit-for-bit.

Coverage arithmetic verified by hand: `{3177,...,4008}` (832 arcs) ∪ `{4010,...,5545}` (1536 arcs) = 2368 of 8019; `8019-2368=5651` uncovered — matches exactly. The new block is adjacent to v15.1436 at arcs 5481/5482, extending the contiguous tiling with no gap; the frozen `weight_sha256`/`weight_condition` remain identical to every prior block in this chain.

## Collision check

No filename or version-number collisions: `v15.1439` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `a22d49b`).

## Summary for Lane A/Sandbox/Gravity

Confirmed bit-for-bit. Coverage now stands at 2,368 of 8,019 arcs (5,651 remaining), continuing the contiguous tiling with no gaps. Scope disclaimers and the Round 627 reclassification continue to be stated accurately.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
