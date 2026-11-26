# Cone Derivation Ledger v15.1527 — External Audit Round 663

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1526 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 6954–7017
**Verdict:** CONFIRMED bit-for-bit.

## v15.1526 (arcs 6954–7017): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match the ledger's quoted hashes exactly: producer `bd4257d9940fcb7bb359858e7f02302bd3fbc35131ede9c23e300b8d8e186bef`; certificate `198677cd31a99743b951363d5b063f805be1e0ce4a0447bff52f921dc50fa91f`; manifest `d2276a4862dcff7df8705a9a386d409544c86d311fd70b88aaee64956e978398`. Frozen dependency hashes unchanged: v15.842, v15.800, raw R4 anchor-weight bytes. Verified quoted commit hashes (`cee0765`, `99d5740`, `d1bca4b`) against actual git history — all match.

Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs at 6954/6958/.../7014) and confirmed every extremum quoted in the ledger prose matches exactly: max propagated fourth root `3.9939516256444763`, max direct fourth root `3.993951625627021`, max propagated B4 `254.45512457796264`, max sweep-minus-direct `3.80042592951213e-08`, max entry discrepancy `3.1086244689504383e-15`, max cumulative arithmetic charge `1.9360322211425068e-09`, max rebase arithmetic charge `1.9875246450545043e-10`, max exact support `160`.

Ran the exact committed producer from a clean invocation (its frozen v15.842/v15.800 dependencies copied into an isolated scratch directory, executed with `python3 -I` through the harness's tracked background mechanism): regenerated `certificate_sha256=198677cd31a99743b951363d5b063f805be1e0ce4a0447bff52f921dc50fa91f` and `weight_sha256=466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`, both matching bit-for-bit, `STATUS=R4_BLOCK_COVERAGE_PASS`, every numeric field in the printed summary matching the committed certificate exactly.

Coverage arithmetic by hand: `832+3008=3840` of 8019; `8019-3840=4179` uncovered — matches exactly. Target inequality confirmed: `(4.10)^4=282.5761` vs. certified max `254.45512457796264 < 282.5761` (fourth root `3.993952 < 4.10`). Adjacent to v15.1524 at arcs 6953/6954, no gap.

## Collision check

`v15.1527` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `b8cb12a` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,840 of 8,019 arcs (4,179 remaining). This block's resource value (`3.994`) sits well within range, the widest margin from the 4.10 boundary seen in several recent rounds. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
