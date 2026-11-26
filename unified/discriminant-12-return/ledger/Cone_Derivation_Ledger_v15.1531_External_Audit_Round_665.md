# Cone Derivation Ledger v15.1531 — External Audit Round 665

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1530 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 7082–7145
**Verdict:** CONFIRMED bit-for-bit.

## v15.1530 (arcs 7082–7145): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match the ledger's quoted hashes exactly: producer `457c67426cdfd0ef372595d714e82bd655c8ce6bf6d37f7cbd5dcaaeb69f573e`; certificate `f83bef9feb540685c8f884df0e26211d977cc990e083571f6e8af3e1f9e1151f`; manifest `04be92f3000aad6cd5e27cc60920d8f43993526e5bb0ddc2d1015a8d87057923`. Frozen dependency hashes unchanged: v15.842, v15.800, raw R4 anchor-weight bytes. Verified quoted commit hashes (`5dd7f56`, `9b1fb90`, `95bad52`) against actual git history — all match.

Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs at 7082/7086/.../7142) and confirmed every extremum quoted in the ledger prose matches exactly: max propagated fourth root `3.9932475852685614`, max direct fourth root `3.9932475852041858`, max propagated B4 `254.2757540348494`, max sweep-minus-direct `3.634974632404919e-08`, max entry discrepancy `2.220446049250313e-15`, max cumulative arithmetic charge `1.9624689743884317e-09`, max rebase arithmetic charge `1.996808973252574e-10`, max exact support `160`.

Ran the exact committed producer from a clean invocation (its frozen v15.842/v15.800 dependencies copied into an isolated scratch directory, executed with `python3 -I` through the harness's tracked background mechanism): regenerated `certificate_sha256=f83bef9feb540685c8f884df0e26211d977cc990e083571f6e8af3e1f9e1151f` and `weight_sha256=466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`, both matching bit-for-bit, `STATUS=R4_BLOCK_COVERAGE_PASS`, every numeric field in the printed summary matching the committed certificate exactly.

Coverage arithmetic by hand: `832+3136=3968` of 8019; `8019-3968=4051` uncovered — matches exactly. Target inequality confirmed: `(4.10)^4=282.5761` vs. certified max `254.2757540348494 < 282.5761` (fourth root `3.993248 < 4.10`). Adjacent to v15.1528 at arcs 7081/7082, no gap.

## Collision check

`v15.1531` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `d214a6b` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,968 of 8,019 arcs (4,051 remaining) — crossing the halfway point of the 8,019-arc space next block. This block's resource value (`3.993`) sits comfortably within range. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
