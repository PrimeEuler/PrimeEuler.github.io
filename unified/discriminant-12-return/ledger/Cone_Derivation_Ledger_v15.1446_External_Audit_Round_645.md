# Cone Derivation Ledger v15.1446 — External Audit Round 645

**Date:** 2026-11-25
**Track:** External Audit
**Subject:** v15.1445 (Lane A) — Suzuki R4 direct-restart 64-state right extension (arcs 5674–5737)
**Verdict:** CONFIRMED. Independently re-executed the exact committed producer; the regenerated certificate's SHA-256 matches the committed certificate exactly, bit-for-bit.

## What was checked

Verified `sha256sum` on the producer (`60ce72ed...808`) and certificate (`f9e5b2e7...574`) against the ledger's claimed hashes and the entry's own manifest — all match, including the unchanged frozen-dependency rows. Loaded the certificate JSON directly: every number quoted in the ledger prose (`max d_nnz=160`, `max_entry_discrepancy_vs_direct=3.1086244689504383e-15`, `max_cumulative_arithmetic=2.09145402072614e-09`, `max_rebase_arithmetic=1.9799485646939115e-10`, `max_sweep_minus_direct_b4=1.4449256013904233e-08`, direct/propagated fourth roots `3.932319155094835`/`3.9323191551126566`, `max_propagated_outward_b4=239.1085111741955 < 282.5761`, and the 16 rebase arcs `{5674,5678,...,5734}`) matches exactly, with `all_pass=True` across all 64 states.

Ran `research-notes/lane_a_v15_1445_suzuki_r4_direct_restart_64_right_extension.py` exactly as committed, resolving the unchanged frozen dependency chain: `STATUS=R4_BLOCK_COVERAGE_PASS`, and the regenerated `certificate_sha256` (`f9e5b2e7fc605cece0e24b57ce1ae04e7b7babe8ef8064693b852e6b6dd5c574`) matches the committed certificate's own hash exactly, bit-for-bit.

Coverage arithmetic verified by hand: `{3177,...,4008}` (832 arcs) ∪ `{4010,...,5737}` (1728 arcs) = 2560 of 8019; `8019-2560=5459` uncovered — matches exactly. The new block is adjacent to v15.1443 at arcs 5673/5674, extending the contiguous tiling with no gap; the frozen `weight_sha256`/`weight_condition` remain identical to every prior block in this chain. This entry also correctly self-detected and avoided a version-slot collision with Round 644 by advancing its own provisional slot from v15.1444 to v15.1445 before writing, consistent with the standing collision-avoidance protocol.

## Collision check

No filename or version-number collisions: `v15.1446` was free immediately before this write (confirmed via fresh `git fetch origin master`, HEAD still `7246244`).

## Summary for Lane A/Sandbox/Gravity

Confirmed bit-for-bit. Coverage now stands at 2,560 of 8,019 arcs (5,459 remaining), continuing the contiguous tiling with no gaps. Scope disclaimers and the Round 627 reclassification continue to be stated accurately.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
