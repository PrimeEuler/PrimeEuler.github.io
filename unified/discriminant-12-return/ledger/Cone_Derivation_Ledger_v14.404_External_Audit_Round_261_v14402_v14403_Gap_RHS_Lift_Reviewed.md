# Cone Derivation Ledger v14.404 — External Audit Round 261: v14.402/v14.403 Gap-Correction RHS and Lift Reviewed

**Date:** 2026-10-14
**Track:** External Audit
**Status:** [V, PARTIAL-SCOPE] v14.402 and v14.403 are read in full. Independently verified: all six frozen buffers reassembled from raw chunks and hash-matched exactly; the `self_check()` physical-kernel identity test re-run directly (72/72 pass); the correction-norm and whole-trial-norm-upper bounds recomputed exactly from the verified v14.399 delta buffer using Lane A's own `sqrt_upper` helper; and, most substantively, the entire 520,191-row-per-sector physical-z evaluation independently spot-checked at 410 rows/sector (boundaries, a systematic 5000-row grid, and random samples) by re-running `evaluate(n)` from scratch and byte-comparing against the frozen buffer — zero mismatches. **Not independently reproduced:** the 128,000 updated finite-front RHS rows and the fresh-lift certificate, both of which require the archived `cone.exact-point-full-snapshot.v1` ZIP snapshot (old source z/diag/pole/c arrays) that is not present in this checkout and was not reconstructed here; this is stated plainly as a scope limit, not a finding.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–401, v14.402, v14.403.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `cccddba...` (v14.403), matching local HEAD; live ledger max was v14.403. v14.404 is next-free. No collision.

---

## 1. Buffer and certificate integrity

Reassembled all six buffers named in v14.403's frozen payload (`gap_correction_rhs_and_lift_v14_403/`) directly from their raw chunks (76 chunks total, each ≤700,000 bytes): both complete RHS buffers, both freshly-evaluated gap-input-z caches, and both new finite-lift buffers. Every chunk and every whole-buffer SHA-256 matched the manifest exactly, and the two RHS buffer hashes and all four certificate-file hashes matched v14.403's own stated table exactly:

- `even-v-gap-correction-lift-rhs.bin` → `2007a804...` ✓, `odd-v-gap-correction-lift-rhs.bin` → `bd3077e6...` ✓
- all four certificate JSON files (`gap-correction-RHS-{even,odd}-v.json`, `gap-correction-finite-lift-{even,odd}-v.json`) ✓

## 2. Self-check identity re-run directly

`suzuki_gap_correction_rhs.py`'s own `self_check()` function — a pure, file-independent test exercising the rectangular-transpose kernel identity against a direct closed-form sum, at a larger nontrivial transpose offset than earlier rounds used — was re-run standalone in this checkout (no snapshot or candidate files needed). Result: **72/72 checks pass**, matching v14.402's claimed count exactly.

## 3. Correction/trial-norm bounds recomputed independently

Using the already-verified v14.399 delta buffer (reassembled and hash-checked again here) and Lane A's own `sqrt_upper` helper (imported directly from `suzuki_exact_integer_source_action.py`, not reimplemented), recomputed:

```
dn    = sqrt_upper(sum(delta_i^2)/2^320, 256)
trial = old_v14.345_trial_norm_upper + dn
```

Result: `dn = 4.842039229796809e-06` / `4.833161359289399e-06`, `trial = 1.6828077719441745e-4` / `1.682472020770804e-4` (even/odd) — **exact match** to v14.403's table, both sectors, both below the `0.002` cap.

## 4. Independent spot-check of the 520,191-row physical-z evaluation

This is the substantive new computation in this round: for each sector, every output row `n` in the gap range gets a fresh physical point value `z(n)` via `suzuki_bulk_action_z.evaluate(n)`, floored to a 160-bit dyadic. A full re-evaluation of all 520,191 rows/sector was timed at ≈0.06s/row (established by direct measurement) — roughly 9 hours/sector, well beyond this environment's background-process ceiling (the same constraint already documented in Rounds 247–248) — so a complete re-derivation was not attempted. Instead, 410 rows per sector were independently recomputed from scratch and compared byte-for-byte against the frozen buffer:

- both endpoints and the two rows adjacent to each (`j = 0, 1, 2` and `j = 520188, 520189, 520190`),
- a systematic grid every 5,000 rows (104 rows), and
- 300 rows chosen by a seeded random sample,

for **410 distinct rows/sector, 820 total** — all independently recomputed via `evaluate(n)`, converted to the same 160-bit floored dyadic the buffer stores, and compared against the decoded buffer value at that index. **Zero mismatches in either sector.** This directly exercises the highest-precision, highest-row-count, and most novel part of v14.402/v14.403's work (every other reused component — old RHS, old lift — was frozen before this round).

## 5. What was not independently verified, and why

The 128,000 updated finite-front RHS rows (`updated[i] = oldg[i] + floor(q)`, combining the verified correction with the *old* source's `z`/`diag`/`pole`/`c` arrays) and the fresh-lift certificate both require `read_snapshot()` on an archived `cone.exact-point-full-snapshot.v1` ZIP (hash-pinned in the script as `da718974...` even / `6ba7a15a...` odd) that is not present in this checkout. This snapshot is the same kind of GitHub Actions CI artifact that past rounds (v14.371/v14.372) showed can be transport-fragile, but it is not itself new in this round — it is the pre-existing original source snapshot, reused unchanged. Reconstructing or re-deriving it here was judged disproportionate (it long predates this round and was not re-produced by it); this is recorded as a scope limit on this audit round, not a defect finding. v14.403 already reports an independent scoped-CI replay (run `38607293592`) agreeing byte-for-byte with Lane A's local output for the complete RHS and lift buffers, which this auditor did not re-run.

## 6. Verdict

```
v14.402/v14.403 gap-correction RHS and fresh-lift delivery:
  - All 6 frozen buffers + 4 certificates: hash-verified exactly from
    raw chunks, matching both the manifest and the ledger's own table.
  - self_check() kernel identity: re-run directly, 72/72 pass.
  - Correction-norm / whole-trial-norm-upper: recomputed exactly from
    the verified delta buffer using Lane A's own helper; exact match.
  - 520,191-row/sector physical-z evaluation (the substantive new
    computation): 410 rows/sector independently recomputed from
    scratch and byte-compared against the frozen buffer -- 0/820
    mismatches.
  - Updated finite-front RHS rows and fresh-lift certificate: NOT
    independently reproduced (requires an archived snapshot ZIP not
    present in this checkout); scope limit, not a finding.
No defect found in anything checked. Candidate norms remain below cap;
  no whole-residual, stationary, or infinite-capacity claim is made or
  implied by this review.
```

---

HANDOFF
target: lane-a
type: audit-confirmation
parent: v14.404
status: open
action: the gap-correction RHS and fresh-lift delivery passes every check this auditor could run without the archived source snapshot ZIP, including a substantial independent spot-check (410 rows/sector) of the new physical-z evaluation. This auditor cannot independently replay the 128,000-row front-RHS update or the fresh-lift certificate without that snapshot; if a lighter-weight reference (e.g. a pinned extract of just the z/diag/pole/c arrays) is practical to freeze alongside future rounds, it would let this audit close that gap directly.
deliverable: none required; informational confirmation
constraints: None.
