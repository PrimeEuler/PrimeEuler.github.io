# Cone Derivation Ledger v15.1515 — External Audit Round 658

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1514 (Lane A) — Suzuki R4 direct-restart 64-state right extension, arcs 6570–6633
**Verdict:** CONFIRMED bit-for-bit.

## v15.1514 (arcs 6570–6633): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest and the frozen dependency hashes — all match exactly. Verified every quoted live-HEAD/landing commit hash against actual git history — all match. Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs) and confirmed every extremum quoted in the ledger prose matches exactly. Ran the exact committed producer from a clean invocation: regenerated `certificate_sha256=adf002b5fcd6a184833bfc173d23a8a9ec5a4ee19c0fe474e328aa63ca6a0914`, matching bit-for-bit. Coverage arithmetic by hand: `832+2624=3456` of 8019; `8019-3456=4563` uncovered — matches exactly. Adjacent to v15.1512 at arcs 6569/6570, no gap.

The two-round narrowing trend flagged in Rounds 656–657 did not continue here: this block's maximum (`4.0395950443412065`) sits comfortably back below the two preceding values (`4.0864`, `4.0886`), confirming the ledger's own observation that the trend was a property of those specific blocks, not a systematic drift toward the boundary.

## Collision check

`v15.1515` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `25e2d13` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,456 of 8,019 arcs (4,563 remaining). The resource-value margin to the 4.10 target has widened back out after two narrower blocks, consistent with ordinary fluctuation rather than a trend. No Sandbox or Gravity activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
