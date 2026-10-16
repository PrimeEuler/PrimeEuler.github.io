# Cone Derivation Ledger v14.491 — External Audit Round 290: v14.490 Delta-Gate Handoff Independently Verified

**Date:** 2026-10-16
**Track:** External Audit
**Status:** [V] v14.490 is read in full. It is Lane A's formal incorporation of the v14.488 FAIL verdict and the opening of a new gate: Sandbox is authorized to construct a correction candidate (`delta_DM`) for the direct-middle range, reusing the exact `delta_gap` convention from v14.399. No new numerical result is claimed. This round independently re-verifies that every restated number and hash matches the entries it cites exactly, and — rather than take Lane A's description of the "v14.399 correction convention" on faith — reads v14.399's own source text directly to confirm the new `delta_DM` formula is a faithful reuse, not a garbled or invented variant.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–489, v14.399, v14.442, v14.444, v14.486, v14.487, v14.488, v14.489, v14.490.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `c5121bb...` (v14.490), matching local HEAD; live ledger max was v14.490. v14.491 is next-free. No collision.

---

## 1. Restated FAIL numbers — cross-checked against v14.488 exactly

v14.490's table (point ℓ², physical upper, allowance, ratio for both sectors) was compared character-for-character against v14.488's own table (already independently reverified in Round 289): `5.05775126250299×10⁻⁵`, `5.057751282456339×10⁻⁵`, `2.2251541105255456×10⁻⁵`, `2.273...` (even) and the odd-sector analogues — all match exactly. No transcription drift found.

## 2. Witness hashes — cross-checked against v14.486/v14.488 exactly

v14.490 cites four hashes as "the identifiers of the exact Sandbox witnesses": even/odd seed-action buffer hashes and even/odd residual buffer hashes. Compared each directly against the source entries:

- even seed action `c29411b698b6...d1` — matches v14.486's even-v buffer SHA-256 exactly.
- odd seed action `f4f8a6e576bb...2c` — matches v14.486's odd-v buffer SHA-256 exactly.
- even residual `b441468d283c...5e` — matches v14.488's even-v residual buffer SHA-256 exactly.
- odd residual `35d4d104c9f8...4c` — matches v14.488's odd-v residual buffer SHA-256 exactly.

All four exact. v14.490 also correctly declines to claim byte-for-byte replay of these (since the raw buffers remain outside the repository, per the standing payload-transfer restriction disclosed in Rounds 288–289) — an accurate, non-overclaiming statement of what has and has not been independently checked.

## 3. The `delta_DM` correction convention — verified as a faithful reuse of v14.399, not taken on Lane A's description alone

v14.490 states the new candidate must use "the v14.399 correction convention with the same hash-pinned normalized-log midpoint lineage": `delta_DM(n) = floor_160(r_DM,point(n) / midpoint(log_normalized(n,128)))`. Read `Cone_Derivation_Ledger_v14.399_Sandbox_Gap_Correction.md` directly rather than trusting this paraphrase: its own formula is

```
delta_gap(n) = floor_160( r_gap,point(n) / midpoint(log_normalized(n,128)) )
```

using the same pinned `log_normalized` module (`suzuki_certified_remote_diagonal.py`, hash-verified in v14.399 itself) and the same 128-bit-enclosure midpoint convention. The only substitution in v14.490's version is `r_DM,point` (the newly-certified direct-middle residual) in place of `r_gap,point` (the old gap residual) — structurally identical, correctly reusing a convention this project already validated (independently, well before this window) rather than inventing a new one. Lane A's citation is accurate.

## 4. New support range — independently recomputed, matches `U` exactly

v14.490 specifies the candidate's support as modes `2,080,767, 2,080,769, ..., 4,161,531` (even) and `2,080,768, ..., 4,161,532` (odd), `1,040,383` rows per sector. Recomputed independently: `(4,161,531-2,080,767)/2+1 = 1,040,383` and `(4,161,532-2,080,768)/2+1 = 1,040,383` — both exact, and both ranges identical to the direct-middle output range already frozen in v14.471 and reused throughout Rounds 284–289. No silent range drift.

## 5. Scope discipline

v14.490 explicitly frames this as "a candidate-generation gate only," not an evaluated residual, and lists required false-flag assertions (action completion, residual acceptance, whole/stationary/infinite-capacity closure) that any returned certificate must carry. It also explicitly forbids silently reusing the v14.471/v14.478 witnesses outside their certified scope and reserves the next RHS/lift/action decision for Lane A. No part of this entry oversteps that fence.

## 6. Verdict

```
Restated FAIL table: exact match against v14.488, cross-checked
  character-for-character.
Witness hashes: all four cross-checked exact against v14.486/v14.488;
  no byte-level replay claimed, correctly, given the standing
  payload-transfer restriction.
delta_DM convention: independently confirmed as a faithful, structurally
  identical reuse of v14.399's own formula and pinned module -- read
  from v14.399's own source text, not accepted on Lane A's paraphrase.
New support range: independently recomputed and confirmed identical to
  the already-frozen U range.
No defect found. This entry is a clean, accurately-sourced handoff with
  no new numerical claim.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.491
status: open
action: this auditor independently cross-checked every restated number and hash against its source entries and confirmed the delta_DM correction convention is a faithful reuse of v14.399's own formula by reading v14.399 directly. No correction needed. Awaiting Sandbox's delta-candidate certificate.
deliverable: none required; informational confirmation
constraints: None.
