# Cone Derivation Ledger v15.1520 — External Audit Round 660

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1519 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 6698–6761
**Verdict:** CONFIRMED bit-for-bit.

## v15.1519 (arcs 6698–6761): CONFIRMED bit-for-bit

Verified `sha256sum` on producer, certificate, and manifest files — all match the ledger's quoted hashes exactly:

- producer: `4eca62767158b7de0a275829014ee54a39757ccfcbcf3d800a210058a8dd15e9`;
- certificate: `009e0f879b6fb4929cd0f908855a1a0334a982c3a7b5c2834a393ffe81dcf542`;
- manifest: `9bdfe502804e52fb44f2f03f6b2cc5e2a4e7aa24d9a94876e92503aab3af881d`.

Verified the frozen dependency hashes unchanged: v15.842 producer `cd84922908458f906a4d220cf1d5c73b3840fa33b4a162a33c72f85df9dfcf9a`; v15.800 producer `8d347d34fbd1671ca9b02eeb54d025ab78517875e9d4b4e582aadbed9691eecb`; raw R4 anchor-weight bytes `466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`. Confirmed every quoted commit hash (`f5a5703`, `709ab64`, `97151cf`) against actual git history, with commit timestamps (06:35 EST / 11:35 UTC) correctly landing after the audit's own liveness note `9e37a83` (11:27 UTC), consistent with the ledger's account that the first local replay collided with v15.1518 and was renamed to v15.1519 before any provisional artifact was published.

Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs at 6698/6702/.../6758) and confirmed every extremum quoted in the ledger prose matches exactly: max propagated fourth root `4.024237996730211`, max direct fourth root `4.024237996704354`, max propagated B4 `262.261553464276`, max sweep-minus-direct `1.6559312143726856e-08`, max entry discrepancy `3.1086244689504383e-15`, max cumulative arithmetic charge `2.090332318284404e-09`, max rebase arithmetic charge `1.9875619412558745e-10`, max exact support `160`.

Ran the exact committed producer from a clean invocation (copied with its frozen v15.842/v15.800 dependencies into an isolated scratch directory, executed with `python3 -I`): regenerated `certificate_sha256=009e0f879b6fb4929cd0f908855a1a0334a982c3a7b5c2834a393ffe81dcf542` and `weight_sha256=466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`, both matching bit-for-bit, with `STATUS=R4_BLOCK_COVERAGE_PASS` and every numeric field in the printed summary matching the committed certificate exactly.

Coverage arithmetic by hand: `832+2752=3584` of 8019; `8019-3584=4435` uncovered — matches exactly. Target inequality confirmed: `(4.10)^4=282.5761` vs. certified max `262.261553464276 < 282.5761` (fourth root `4.024238 < 4.10`). Adjacent to v15.1516 at arcs 6697/6698, no gap.

## Collision check

`v15.1520` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `2e266fb` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,584 of 8,019 arcs (4,435 remaining). This block's resource value (`4.024`) sits comfortably within range, consistent with ordinary fluctuation. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
