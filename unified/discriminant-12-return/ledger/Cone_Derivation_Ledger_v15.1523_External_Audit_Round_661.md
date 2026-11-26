# Cone Derivation Ledger v15.1523 — External Audit Round 661

**Date:** 2026-11-26
**Track:** External Audit
**Subject:** v15.1521 (Lane A, arcs 6762–6825) and v15.1522 (Lane A, arcs 6826–6889)
**Verdict:** Both CONFIRMED bit-for-bit.

## Note on audit timing

v15.1521 was not audited promptly. A clean-rerun verification of its producer was launched correctly, but was started with `nohup ... &` rather than through the harness's own tracked background mechanism; it did not survive a gap in this session (likely a container restart) and left no output. By the time this was discovered, Lane A had already published v15.1522. Both are verified together here, using the harness-tracked background mechanism this time, so this does not recur.

## v15.1521 (arcs 6762–6825): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match the ledger's quoted hashes exactly: producer `3715631b3936acd6889b1513688700dd3bc422d466044386dfc4cc9277998662`; certificate `1a8494c4a915f5bdcdf38701bb96efa2c74f75e5022feac2a2aaba48482533cc`; manifest `7093322d50bd5a7e30a214b75f369918299aa279b6a70bfc00b24cd2912e20ad`. Frozen dependency hashes (v15.842, v15.800, anchor weight) unchanged. Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs at 6762/6766/.../6822) and confirmed every extremum quoted in the ledger prose matches exactly, including max propagated fourth root `4.017183597645953` and max propagated B4 `260.42742876571685`. Ran the exact committed producer from a clean invocation with its frozen v15.842/v15.800 dependencies: regenerated `certificate_sha256=1a8494c4a915f5bdcdf38701bb96efa2c74f75e5022feac2a2aaba48482533cc` and `weight_sha256=466af7648338f11d705ca3cc69cea1bcc8fe2049110130356a1ad3c977b5bea4`, both matching bit-for-bit, `STATUS=R4_BLOCK_COVERAGE_PASS`. Coverage by hand: `832+2816=3648` of 8019, `8019-3648=4371` uncovered — matches. Target inequality confirmed: `260.42742876571685 < 282.5761` (fourth root `4.017184 < 4.10`). Adjacent to v15.1519 at arcs 6761/6762, no gap.

## v15.1522 (arcs 6826–6889): CONFIRMED bit-for-bit

Verified `sha256sum` on producer/certificate/manifest — match exactly: producer `a268be002a3f377d2f5c73285af2e7fbe45c6c75ddb5be3bd9a876e86bd2f3ce`; certificate `49e6fee75806cbfd18b57c715cec2c11dce6c4165e5e2354e4e36dce1b3bd5bf`; manifest `b22f5610c0d562ab59082baeca596d1d55fa142d23afa72ad0799338c5bfa239`. Frozen dependency hashes unchanged. Read every field of the committed certificate JSON (64 states, all `pass: true`, 16 rebase arcs at 6826/6830/.../6886) and confirmed every extremum matches, including max propagated fourth root `4.027624896601748` and max propagated B4 `263.14557236836765`. Ran the exact committed producer from a clean invocation: regenerated `certificate_sha256=49e6fee75806cbfd18b57c715cec2c11dce6c4165e5e2354e4e36dce1b3bd5bf`, matching bit-for-bit, `STATUS=R4_BLOCK_COVERAGE_PASS`. Coverage by hand: `832+2880=3712` of 8019, `8019-3712=4307` uncovered — matches. Target inequality confirmed: `263.14557236836765 < 282.5761` (fourth root `4.027625 < 4.10`). Adjacent to v15.1521 at arcs 6825/6826, no gap.

## Minor observation (non-decisive)

Both v15.1521 and v15.1522 landed their producer/certificate/manifest files under a new `unified/discriminant-12-return/artifacts/` directory, rather than the `research-notes/` directory used through v15.1519. Both producer scripts' `SOURCE_CANDIDATES` logic correctly falls back to `../research-notes/` to locate the frozen v15.842/v15.800 dependency files, and both reruns succeeded from this layout without incident. This is a file-layout change only, not a defect, and does not affect either verdict.

## Collision check

`v15.1523` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `3e31615` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

Confirmed: Lane A's coverage now stands at 3,712 of 8,019 arcs (4,307 remaining), across v15.1521 and v15.1522 together. Both blocks' resource values (4.017, 4.028) sit comfortably within range. No Sandbox or Gravity activity to report this round. Audit apologizes for the delay on v15.1521 — noted above — and has corrected its own process (background verification now always uses the harness-tracked mechanism, not `nohup`) to prevent recurrence.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
