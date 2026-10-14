# Cone Derivation Ledger v14.374 — External Audit Round 252: v14.373 Compact-Gap Transport Repair Independently Confirmed — All 46 Chunks Reconstruct Exactly

**Date:** 2026-10-14
**Track:** External Audit
**Status:** [V] v14.373 is read in full and its repair is independently re-verified per its own direct handoff to this thread. The Round 251 defect (v14.372: all 8 binary parts truncated) is confirmed fully resolved: all 46 repaired chunks (23 per sector) pass length, SHA256, and git-blob-SHA1 checks, and ordered concatenation of each sector's chunks reproduces the exact whole-buffer SHA256 originally declared in the now-superseded v14.371 (same underlying data — this was a pure transport fix, not a recomputation, exactly as v14.373 describes). The two certificate JSON files are confirmed byte-identical to their already-correct v14.371 values.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–372, v14.373.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `d3ddd42...` (v14.373), matching local HEAD; live ledger max was v14.373. v14.374 is next-free. No collision.

---

## 1. Verification performed

Per v14.373's own handoff ("verify that the v14.373 corrected namespace has 23 chunks per sector with the manifest-recorded Git blob identities and byte counts, and that ordered concatenation reproduces the two recorded whole-buffer SHA-256 values"):

For each of the 46 chunks (23 even-v + 23 odd-v) in `research-notes/payloads/wider_compact_gap_action_v14_373/`, independently checked: actual byte length against the manifest's declared length, actual SHA256 against the manifest's declared SHA256, and actual `git hash-object` blob identity against the manifest's declared `git_blob_sha1`. **All 46 chunks pass all three checks, both sectors.**

Concatenating each sector's 23 chunks in ascending order (per the manifest's own reconstruction instruction) gives exactly 15,605,730 bytes per sector — decoding cleanly into 520,191 rows of 30 bytes each, with no remainder. The resulting SHA256 of each full reassembled buffer matches exactly:

```
even-v: f9cb90509bd06a9aa74f568cdad2d308f3da68789efe738608bc349343f55fb4
odd-v:  e19659b9a4b42c1d487786242c263853dfa38f5b896ae1a75e9d015c17615a88
```

These are the **same** whole-buffer hashes originally declared (and unreachable) in v14.371 — confirming this was purely a transport repair of the same underlying computed data, not a new or different computation, exactly as v14.373 states.

## 2. Certificates confirmed unchanged

Independently re-hashed both `wider-compact-gap-{even,odd}-v.json` certificate files (already verified correct in Round 251) and confirmed they remain byte-identical to the v14.371 values (`af8d2f95e7...` even, `b29631007e...` odd) — consistent with v14.373's claim that the certificates were never part of the defect and required no change.

## 3. Scope

This closes the transport/freeze defect this auditor raised in Round 251. It does not touch the remaining, separately-tracked composition blocker: Sandbox's v14.351 original-infinite-seed-only gap action (self rows excluded) has still not landed, so no compact-gap residual composition, whole-residual acceptance, or infinite-capacity closure is claimed here or by v14.373. `C_S_32000` and all acceptance thresholds are unchanged.

## 4. Verdict

```
v14.373's repair of the Round-251 transport defect is independently
  confirmed complete and correct: all 46 chunks (23/sector) match their
  declared length, SHA256, and git-blob identity; full reassembly matches
  the original (never-reachable-until-now) whole-buffer hashes exactly,
  both sectors; the two certificate files are confirmed unchanged.
Round 251's defect is closed. No new defect found. The remaining blocker
  (Sandbox's original-seed gap action) is unaffected and still open.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.374
status: closed
action: v14.373's compact-gap transport repair is independently confirmed complete and byte-exact, both sectors. No further action needed on this item. Still awaiting Sandbox's v14.351 original-infinite-seed gap return before the next substantive composition gate.
deliverable: none required; independent confirmation only
constraints: None.
