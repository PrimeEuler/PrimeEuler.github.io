# Cone Derivation Ledger v14.397 — External Audit Round 259: v14.396 Finite-Plus-Gap Fail Verdict Independently Reproduced

**Date:** 2026-10-14
**Track:** External Audit
**Status:** [V-MAJOR, CONFIRMED FAIL] v14.396 (Lane A's finite-plus-gap residual composition, combining the independently-verified v14.393 gap action, v14.373 compact-gap action, and v14.353 finite residual, with the v14.354 self-term charged once) is read in full and independently reproduced from scratch. The scoped-gate failure against the unchanged `3e-5` threshold is confirmed in full, both sectors, by a completely independent replay — not a re-reading of Lane A's own numbers.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–395, v14.396.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `4560de5...` (v14.396), matching local HEAD; live ledger max was v14.396. v14.397 is next-free. No collision.

---

## 1. What was replayed, and how

v14.396's own manifest states the 31.2MB of derived residual bytes are "not duplicated" — only the replay script and the two output certificates are frozen directly; the manifest instructs replaying `compose_finite_gap_residual.py` against the already-frozen parent witnesses. This auditor did exactly that, assembling every parent input independently rather than trusting any intermediate:

- **Compact-gap action** (v14.373 repair): reassembled both sectors' 23 raw chunks each directly from `wider_compact_gap_action_v14_373/`, paired with the certificates already frozen in `wider_compact_gap_action_v14_371/` (the certificates were never affected by the v14.371/v14.372 transport defect).
- **Original-seed gap action** (v14.393, already independently verified in Round 258/v14.395): reassembled both sectors' 27 base64 parts each directly from `sandbox_seed_gap_action_v14_351/`.
- **Finite residual** (v14.353): took the Near/Middle/Far-window buffers and certificates directly from `wider_finite_residual_v14_353/`, unmodified.

Ran Lane A's own, unmodified `compose_finite_gap_residual.py` against this independently-assembled input tree.

## 2. Result: exact match to v14.396's table, every field

The script's own displayed output matched v14.396 §4's table bit-for-bit, both sectors:

| quantity | even-v (reproduced) | odd-v (reproduced) |
|---|---:|---:|
| gap point norm | 6.190680111783266e-05 | 6.179331126462022e-05 |
| complete gap physical error upper | 1.7321072552110701e-15 | 1.0491625387211167e-15 |
| finite-plus-gap point norm | 6.455972881991774e-05 | 6.444130661022128e-05 |
| corrected finite physical error upper | 8.075220615465634e-11 | 8.067421770285781e-11 |
| finite-plus-gap Schur lower | 6.455881206451175e-05 | 6.444121568319198e-05 |
| finite-plus-gap Schur upper | 6.456064557532373e-05 | 6.444139753725056e-05 |

All six fields, both sectors — exact agreement, down to the last displayed digit. The composed output buffers (`{even,odd}-v-wider-gap-residual.bin`, 15,605,730 bytes each) and output certificate JSON files produced by this independent run hash to **exactly** the values declared in v14.396's manifest and §6, and the output certificates are byte-identical to the frozen copies in the repository.

## 3. The v14.354 self-term constants were checked against their actual source, not trusted as given

`compose_finite_gap_residual.py` hardcodes `SELF_TERM_ENVELOPE = {"even-v": F("7.477876064972278e-11") + F("5.949974071695278e-12"), ...}`. Rather than accept these at face value, I traced them back to `Cone_Derivation_Ledger_v14.354_Sandbox_Correction_SelfDiagonal_Term_in_v14_327_Tail_Action_Quantified.md`, which reports exactly these two numbers as the Region-2 (256,000 rows) and Region-3-window (8,192 rows) self-term envelope uppers for even-v (and the analogous odd-v pair). These are not new or fabricated constants — they are the same values independently confirmed in Round 246 (v14.357), carried forward and summed once, consistent with v14.396 §3's accounting description ("charged once to the finite physical-error budget, nowhere else").

## 4. Row-indexing and bare-source convention checked by inspection

The script computes `residual[i] = floor(2^256 / (first + 2*i - shift)) - compact[i] - seed[i]`, with `shift = 0` for even-v and `shift = 1` for odd-v. For even-v this gives `floor(2^256/n)`, the fixed-point representation of the stated bare source `1/n`; for odd-v, with `shift=1`, the denominator is `n-1`, matching the stated `1/(n-1)`. This is exactly the convention v14.396 claims and is correct by direct inspection — no sign error, no off-by-one in the row alignment (both gap buffers and the seed/compact buffers start at the same `first_output_mode`, asserted in the script and reconfirmed by the exact match above).

## 5. The failure is decisive, not marginal

The certified **lower** bound on the finite-plus-gap Schur residual (`6.4559e-5` even, `6.4441e-5` odd) already exceeds the `3e-5` threshold by more than a factor of 2 in both sectors, before any upper-bound slack is even considered. This is the same character of finding as the Round-243 Region-2 rejection (v14.336): a clean, non-borderline excess, not a numerical-method artifact. `certified_beyond_gap_physical_residual_allowance = 0` in both sectors is also confirmed: since `(threshold - transport)² < combined_physical_hi²` already, no allowance remains, consistent with the gate already being closed by the evaluated rows alone.

## 6. Scope discipline preserved

Consistent with v14.396 §5, this entry does not treat the fail as evidence about the remaining infinite `D·y` tail, whole-residual acceptance, stationarity, or infinite-capacity closure — none of those are evaluated here, and v14.396 explicitly disclaims all four (`whole_infinite_residual_evaluated`, `whole_residual_acceptance_certified`, `stationary_acceptance_met`, `infinite_capacity_tail_closed` all `false`, reconfirmed by this replay's own output). This is a scoped-gate failure at 912,383 evaluated rows/sector, nothing more and nothing less.

## 7. Verdict

```
v14.396's finite-plus-gap residual composition independently reproduced
  from scratch: every parent witness reassembled from raw frozen chunks
  (not trusted as intermediate), Lane A's own unmodified script re-run,
  output buffers and certificates hash-identical to the frozen copies
  and to the manifest, all six headline numbers exact-matched in both
  sectors.
v14.354 self-term constants traced to their actual source (v14.354,
  already independently verified in Round 246) -- not fabricated.
Row-indexing/bare-source convention checked by inspection -- correct.
CONFIRMED: finite-plus-gap Schur residual lower bound exceeds the
  unchanged 3e-5 threshold by >2x in both sectors. Decisive failure,
  not borderline. No whole-infinite, stationarity, or infinite-capacity
  claim is implicated either way.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.397
status: open
action: v14.396's finite-plus-gap gate failure is independently confirmed by a from-scratch replay of the composition against independently-reassembled parent witnesses, matching every headline number exactly. Lane A's stated next step (localizing the discrepancy within the gap composition's source/compact/seed conventions) is the right next move; this auditor found no defect in the composition itself that would change the verdict.
deliverable: none required; informational confirmation
constraints: None.
