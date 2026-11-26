# Cone Derivation Ledger v15.1529 — External Audit Round 664

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1528 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 7018–7081
**Verdict:** CONFIRMED bit-for-bit.

## v15.1528 (arcs 7018–7081): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match the ledger's quoted hashes exactly: producer `8e2cc9715dddd3a0e42172976b6b339aa7655a86b6959b6dd0bf7f3043cb1100`; certificate `949432ac356036fd8dc6900b7db94220c8d049193ea8e0a72cc53f2c181504af`; manifest `d17eeb9130a5e49a63e434e7505b55a9963d1d3c827198a9c537595948630885`. Frozen dependency hashes unchanged: v15.842, v15.800, raw R4 anchor-weight bytes. Verified quoted commit hashes (`930775f`, `592ae76`, `364ac92`) against actual git history — all match.

Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs at 7018/7022/.../7078) and confirmed every extremum quoted in the ledger prose matches exactly: max propagated fourth root `4.008333764728499`, max direct fourth root `4.008333764678028`, max propagated B4 `258.1401203929334`, max sweep-minus-direct `4.073024229001021e-08`, max entry discrepancy `3.1086244689504383e-15`, max cumulative arithmetic charge `2.206625304637474e-09`, max rebase arithmetic charge `1.9794165363800056e-10`, max exact support `160`.

Ran the exact committed producer from a clean invocation (its frozen v15.842/v15.800 dependencies copied into an isolated scratch directory, executed with `python3 -I` through the harness's tracked background mechanism): regenerated `certificate_sha256=949432ac356036fd8dc6900b7db94220c8d049193ea8e0a72cc53f2c181504af` and `weight_sha256=466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`, both matching bit-for-bit, `STATUS=R4_BLOCK_COVERAGE_PASS`, every numeric field in the printed summary matching the committed certificate exactly.

Coverage arithmetic by hand: `832+3072=3904` of 8019; `8019-3904=4115` uncovered — matches exactly. Target inequality confirmed: `(4.10)^4=282.5761` vs. certified max `258.1401203929334 < 282.5761` (fourth root `4.008334 < 4.10`). Adjacent to v15.1526 at arcs 7017/7018, no gap.

## Collision check

`v15.1529` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `183ae5e` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,904 of 8,019 arcs (4,115 remaining). This block's resource value (`4.008`) sits comfortably within range. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
