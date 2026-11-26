# Cone Derivation Ledger v15.1525 — External Audit Round 662

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1524 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 6890–6953
**Verdict:** CONFIRMED bit-for-bit.

## v15.1524 (arcs 6890–6953): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match the ledger's quoted hashes exactly: producer `0dabd3b00104752ed4fa078f3f13aea5e0d9a0635f09c9049bae99668d00f41a`; certificate `06e8138e9003a9cb33f701b7260adf4a2b314501139184ccc2b8fad6e07ef574`; manifest `07071cca4daab2f3313f403f466418b278d577cd1897cf822e6d40aadac29279`. Frozen dependency hashes unchanged: v15.842, v15.800, raw R4 anchor-weight bytes. Verified quoted commit hashes (`2daf417`, `2ba94f4`, `de00a44`) against actual git history — all match.

Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs at 6890/6894/.../6950) and confirmed every extremum quoted in the ledger prose matches exactly: max propagated fourth root `4.017847246165207`, max direct fourth root `4.01784724608675`, max propagated B4 `260.5995643990118`, max sweep-minus-direct `2.7660917112370953e-08`, max entry discrepancy `3.1086244689504383e-15`, max cumulative arithmetic charge `2.4375799837472486e-09`, max rebase arithmetic charge `1.9943895512187042e-10`, max exact support `160`.

Ran the exact committed producer from a clean invocation (its frozen v15.842/v15.800 dependencies copied into an isolated scratch directory, executed with `python3 -I`, tracked through the harness's background mechanism this time): regenerated `certificate_sha256=06e8138e9003a9cb33f701b7260adf4a2b314501139184ccc2b8fad6e07ef574` and `weight_sha256=466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`, both matching bit-for-bit, `STATUS=R4_BLOCK_COVERAGE_PASS`, every numeric field in the printed summary matching the committed certificate exactly.

Coverage arithmetic by hand: `832+2944=3776` of 8019; `8019-3776=4243` uncovered — matches exactly. Target inequality confirmed: `(4.10)^4=282.5761` vs. certified max `260.5995643990118 < 282.5761` (fourth root `4.017847 < 4.10`). Adjacent to v15.1522 at arcs 6889/6890, no gap.

## Collision check

`v15.1525` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `016f6bf` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,776 of 8,019 arcs (4,243 remaining). This block's resource value (`4.018`) sits comfortably within range. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
