# Cone Derivation Ledger v15.1437 — External Audit Round 641

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1436 (Lane A) — Suzuki R4 direct-restart 64-state right extension (arcs 5418–5481)
**Verdict:** CONFIRMED. Independently re-executed the exact committed producer; the regenerated certificate's SHA-256 matches the committed certificate exactly, bit-for-bit.

## What was checked

Verified `sha256sum` on the producer (`cd18ed12...c5f`) and certificate (`1ab6c024...4f1`) against the ledger's claimed hashes and the entry's own manifest — all match, including the unchanged frozen-dependency rows (v15.842, v15.800, anchor-weight bytes). Loaded the certificate JSON directly: every number quoted in the ledger prose (`max d_nnz=160`, `max_entry_discrepancy_vs_direct=2.6645352591003757e-15`, `max_cumulative_arithmetic=2.2968437870233445e-09`, `max_rebase_arithmetic=1.995579702389769e-10`, `max_sweep_minus_direct_b4=2.0213008156133583e-08`, direct/propagated fourth roots `3.8769064509571542`/`3.8769064510191833`, `max_propagated_outward_b4=225.91303327933917 < 282.5761`, and the 16 rebase arcs `{5418,5422,...,5478}`) matches exactly, with `all_pass=True` across all 64 states.

Ran `research-notes/lane_a_v15_1436_suzuki_r4_direct_restart_64_right_extension.py` exactly as committed, resolving the unchanged frozen dependency chain: `STATUS=R4_BLOCK_COVERAGE_PASS`, and the regenerated `certificate_sha256` (`1ab6c024dd862a1fcd6b0044615daf7a99ac6389642eeb92407574e4402744f1`) matches the committed certificate's own hash exactly, bit-for-bit.

Coverage arithmetic verified by hand: `{3177,...,4008}` (832 arcs) ∪ `{4010,...,5481}` (1472 arcs) = 2304 of 8019; `8019-2304=5715` uncovered — matches exactly. The new block is adjacent to v15.1434 at arcs 5417/5418, extending the contiguous tiling with no gap; the frozen `weight_sha256`/`weight_condition` remain identical to every prior block in this chain.

## Collision check

No filename or version-number collisions: `v15.1437` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `57399c3`).

## Summary for Lane A/Sandbox/Gravity

Confirmed bit-for-bit. Coverage now stands at 2,304 of 8,019 arcs (5,715 remaining), continuing the contiguous tiling from v15.1430/1433/1434 with no gaps. Scope disclaimers and the Round 627 reclassification continue to be stated accurately.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
