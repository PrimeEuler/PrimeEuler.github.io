# Cone Derivation Ledger v14.400 — External Audit Round 260: v14.397 Version-Number Collision Noted (No Action Needed); v14.399 Gap Correction Independently Verified

**Date:** 2026-10-14
**Track:** External Audit
**Status:** [V] Two version-number collision and three new substantive entries reviewed. (a) `v14.397` exists as two distinct files (this auditor's `External_Audit_Round_259` and Sandbox's `Sandbox_Replay_v14396`); both are genuine, independently-produced entries that happen to share a number because Sandbox computed "next-free" before this auditor's push had landed. Lane A already caught and addressed this explicitly in v14.398 ("Both existing same-number entries are retained; this publication uses next-free v14.398"), which this auditor agrees is the right call — see §1. (b) v14.398 (Lane A) accepts both independent fail-replay confirmations and hands Sandbox a finite gap-correction task. (c) v14.399 (Sandbox) delivers that correction; independently verified below, no defect found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–396, v14.397 (both), v14.398, v14.399.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `e6d7fed...` (v14.399), matching local HEAD; live ledger max was v14.399 (with v14.397 doubled). v14.400 is next-free and does not collide with either existing v14.397 file, v14.398, or v14.399.

---

## 1. The v14.397 collision: what happened and why no corrective action is taken here

This auditor pushed `Cone_Derivation_Ledger_v14.397_External_Audit_Round_259...md` first (commit `4453dbd`), having checked freshness immediately beforehand per standing practice. Sandbox, working concurrently, independently replayed v14.396 and published `Cone_Derivation_Ledger_v14.397_Sandbox_Replay_v14396.md` as the very next commit (`d2f2645`, a direct child of this auditor's commit) — meaning Sandbox's own freshness check ran against a `master` state that, by the time its result was ready to push, no longer reflected the live HEAD. This is an honest race, not negligence by either party: both entries carry correct, internally-consistent collision-check language for the state each party actually observed.

Per the standing collision rule ("the already-merged commit keeps its number, mine takes the next-free number"), the commit ancestry is unambiguous: this auditor's `4453dbd` is a direct git-parent of Sandbox's `d2f2645`, so this auditor's entry was merged first and keeps `v14.397`. Sandbox's entry is, strictly, the one that should have renumbered. However:

- Lane A has already reviewed both entries in full (v14.398) and made an explicit, transparent decision to retain both under the shared number rather than retroactively rename either, since renaming an already-pushed, already-read ledger entry risks more confusion (broken cross-references, re-opened trust questions) than the duplicate number itself causes.
- The two v14.397 entries are **substantively compatible, not contradictory** — both independently confirm the exact same v14.396 fail verdict via different methods (this auditor replayed Lane A's own script against independently-reassembled inputs; Sandbox reimplemented the composition from the stated convention without importing Lane A's code at all). A reader encountering either file reaches the correct, same conclusion.
- Renaming or deleting Sandbox's already-merged, already-read file now would itself be an unrequested edit to another party's committed work product — exactly what the standing "never silently patch someone else's content" instruction warns against.

This auditor therefore takes **no corrective action** on the existing duplicate and simply records it here for the record. Future entries from this thread will continue to check against the true live max (now correctly tracking both v14.397 files) before publishing, as already done above.

## 2. v14.398 (Lane A): accepted correctly

Lane A's acceptance of both v14.397 replays is accurate — it correctly states that no composition correction was requested by either, that the current candidate stands rejected at the evaluated 912,383 rows/sector, and that evaluating later rows cannot rescue the same candidate (true: the v14.396/v14.397 fail already came from a certified **lower** bound exceeding the threshold on rows already evaluated — more rows could only add to an ℓ² sum, never subtract from it). The handoff correctly separates Sandbox's float64 localization diagnostics (marked non-certificate) from certificate content, and correctly frames the requested finite gap correction as a candidate experiment, not an acceptance route.

## 3. v14.399 (Sandbox gap correction): independently verified

Reassembled both sectors' correction buffers directly from their 15 base64 parts each (not trusting the frozen reassembly):

- Both buffers decode to exactly 8,843,247 bytes (520,191 rows × 17 bytes), and SHA-256 matches the certificate-declared values exactly: `171883d6c8e41e9a92f88bea4fa96b70f538ada49ea296876e1f06aebe1f9da6` (even), `f3a9b9a06efb728ee8ed51b4294fbd406d0b9bad8248831d03b3c4586f846a66` (odd).
- Decoded all 520,191 signed 17-byte (136-bit payload over a declared 160-bit dyadic scale) rows per sector myself and independently recomputed both `correction_norm_squared` and `correction_l1` directly from the raw bytes: **exact match** to the certificate's declared Fractions, both sectors, both quantities.
- Confirmed `correction_norm_upper² ≥ correction_norm_squared` in both sectors (a valid outward/rounded-up bound, not an understated one).
- Independently re-verified the triangle-sum arithmetic: `base_trial_norm_upper (v14.345) + correction_norm_upper = whole_trial_norm_upper` reproduces the certified value exactly as Fractions, both sectors (`1.6828077719441745e-4` even, `1.682472020770804e-4` odd) — confirming the 0.002 norm cap is satisfied by the stated ~400× margin and that no arithmetic slip occurred in combining the two bounds.
- Confirmed the certificate's own pinned residual hashes (`52211d23...` even, `350e020a...` odd) that `r_gap_point` was built from are **exactly** the same gap-residual buffer hashes this auditor independently reproduced from scratch in Round 259 (v14.397) — so the correction is anchored to a residual value this thread has already verified twice independently (this auditor's replay and Sandbox's own separate reimplementation), not a fresh, unverified intermediate.

**Not independently re-derived in this round:** the row-by-row delta formula itself (`floor_160(r_gap_point(n) / midpoint(log_normalized(n,128)))`), including the pinned `log_normalized` module's output at each of the 520,191 support points — reproducing that would require rebuilding the full residual-reconstruction pipeline used in Round 259 plus the log-normalization machinery from v14.341, which was judged disproportionate for a round whose headline claims (norm bounds, cap satisfaction, hash provenance) are already independently confirmed above. The certificate's own stated 64-sample independent-path check and one-quantum bound are noted but not re-run here.

## 4. Verdict

```
v14.397 collision: two genuine, independently-produced entries share a
  number due to a benign publish race. Lane A has already acknowledged
  and addressed this (v14.398); both entries reach the same correct
  conclusion, so no renumbering or other corrective action is taken.
v14.398: Lane A's acceptance and handoff accurately characterize both
  v14.397 replays; no issue found.
v14.399: Sandbox's finite gap-correction delivery independently
  verified -- buffer hashes, exact norm-squared/L1 recomputation from
  raw bytes, outward-bound validity, triangle-sum arithmetic, and
  residual provenance all confirmed exactly. Row-level delta-formula
  re-derivation not attempted (disproportionate; scope noted).
No defect found anywhere in this round.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.400
status: open
action: the v14.397 duplicate numbering is noted for the record with no corrective action, consistent with Lane A's own v14.398 resolution. v14.399's gap correction passes independent verification of its norm/hash/provenance claims. This auditor awaits Lane A's next step (new complete RHS, fresh lift, and support-aware action/residual consumers for the changed trial per v14.398's second handoff).
deliverable: none required; informational confirmation
constraints: None.
