# Cone Derivation Ledger v15.1533 — External Audit Round 666

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1532 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 7146–7209
**Verdict:** CONFIRMED bit-for-bit.

## v15.1532 (arcs 7146–7209): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match the ledger's quoted hashes exactly: producer `381f802b9f37b4f93bc0208acae1513fde068dce0631b57f3ed7337f987f7b41`; certificate `8a5de19d1c0bb4306d0eddd3e1e0f040d0a524678b2037adc61dabd7c0a0ce5c`; manifest `b451946e83ecf81d7b7a1fd4912f9e12cf0b211c24cca7f0a3c3d208a4763315`. Frozen dependency hashes unchanged: v15.842, v15.800, raw R4 anchor-weight bytes. Verified quoted commit hashes (`3a05a58`, `ee8a7d9`, `07455a8`) against actual git history — all match.

Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs at 7146/7150/.../7206) and confirmed every extremum quoted in the ledger prose matches exactly: max propagated fourth root `3.987359219438579`, max direct fourth root `3.9873592194210783`, max propagated B4 `252.7792676600059`, max sweep-minus-direct `1.8612070107337786e-08`, max entry discrepancy `3.552713678800501e-15`, max cumulative arithmetic charge `2.1834565440672584e-09`, max rebase arithmetic charge `1.9846004839777586e-10`, max exact support `160`.

Ran the exact committed producer from a clean invocation (its frozen v15.842/v15.800 dependencies copied into an isolated scratch directory, executed with `python3 -I` through the harness's tracked background mechanism): regenerated `certificate_sha256=8a5de19d1c0bb4306d0eddd3e1e0f040d0a524678b2037adc61dabd7c0a0ce5c` and `weight_sha256=466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`, both matching bit-for-bit, `STATUS=R4_BLOCK_COVERAGE_PASS`, every numeric field in the printed summary matching the committed certificate exactly.

Coverage arithmetic by hand: `832+3200=4032` of 8019; `8019-4032=3987` uncovered — matches exactly, and confirms the halfway point of the 8,019-arc space (4,009.5) was crossed by this block, as anticipated in Round 665. Target inequality confirmed: `(4.10)^4=282.5761` vs. certified max `252.7792676600059 < 282.5761` (fourth root `3.987359 < 4.10`). Adjacent to v15.1530 at arcs 7145/7146, no gap.

## Collision check

`v15.1533` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `42f687a` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 4,032 of 8,019 arcs (3,987 remaining) — just past the halfway point. This block's resource value (`3.987`) sits comfortably within range. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
