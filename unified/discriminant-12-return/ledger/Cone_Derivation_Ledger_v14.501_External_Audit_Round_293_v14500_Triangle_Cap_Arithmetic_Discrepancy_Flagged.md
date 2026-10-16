# Cone Derivation Ledger v14.501 — External Audit Round 293: v14.500 Delta-Candidate Arithmetic Checked; Triangle/Cap Computation Discrepancy Flagged

**Date:** 2026-10-16
**Track:** External Audit
**Status:** [V/F] v14.499 and v14.500 are read in full. v14.500 is Sandbox's return of the certified two-sector direct-middle delta candidate under the v14.490 gate — a candidate-generation deliverable, no action/residual/closure claim. Several arithmetic claims check out exactly, but this round finds a genuine, precisely-located discrepancy between v14.500's own table columns: the displayed "whole-trial triangle upper" is reproduced exactly by adding the base trial upper to the *unrooted* value shown in the "exact norm² upper" column — not to its square root. If that column is correctly labeled (a true norm-squared), the actual triangle-inequality bound should use its square root, which this round computes to be **≈2.105e-3 (even) / ≈2.103e-3 (odd) — both exceeding the stated 0.002 cap**, reversing the entry's own "within the cap" conclusion. This is reported for clarification, not silently resolved, since the raw certificate is not in this repository.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–498, v14.339, v14.399, v14.403, v14.488, v14.490, v14.491, v14.499, v14.500.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `8ee30c7...` (v14.500), matching local HEAD; live ledger max was v14.500. v14.501 is next-free. No collision.

---

## 1. v14.499: pure ACK, confirmed as such

No new claim; commit adds only the ledger entry. Consistent with its own text.

## 2. v14.500: arithmetic claims independently checked

**Support range.** Even `2,080,767..4,161,531`, odd `2,080,768..4,161,532`, step 2, `1,040,383` rows per sector — identical to the already-frozen direct-middle range (Rounds 284–289); no drift.

**Buffer size.** `1,040,383 rows × 17 bytes/row = 17,686,511` — confirmed exact (`width=17` here, not `30`, since this buffer carries 160-bit `floor_160` delta values rather than 256-bit action points; a different, smaller width than the compact/seed buffers is expected and not itself a defect).

**`delta_DM` convention.** Matches v14.399's `delta_gap` formula exactly, already confirmed faithful in Round 290; the pinned `log_normalized` module hash (`08226538df...`) matches the one independently quoted from v14.399's own text in that round.

**Log-midpoint continuity.** The new range `[13.161952772586037, 13.855099472553855]` begins almost exactly where v14.399's gap-range ended (`[12.4688, 13.1620]`) — the new lower bound (`13.1620`) sits right at the old upper bound, consistent with the direct-middle block starting immediately after the gap block in mode-space. A sensible continuity check, not independently reproducible without the pinned module but not contradicted by anything available.

## 3. Discrepancy found: the "whole-trial triangle upper" does not use the square root of the "norm² upper" column

v14.500's table gives, per sector, an `exact norm² upper (display)` value and a `base trial upper (v14.403)` value, and reports their combination as `whole-trial triangle upper`. Checked both candidate combinations at full precision:

```
even: base_upper + norm_sq_value            = 0.0001720327820128694792  (displayed triangle upper: 1.720328e-04 -- EXACT MATCH)
even: base_upper + sqrt(norm_sq_value)      = 0.0021052900215944296... (if norm_sq_value is truly squared)

odd:  base_upper + norm_sq_value            = 0.0001719923297192601123  (displayed triangle upper: 1.719923e-04 -- EXACT MATCH)
odd:  base_upper + sqrt(norm_sq_value)      = 0.0021034804281434924... (if norm_sq_value is truly squared)
```

The displayed triangle upper matches **only** the first computation (adding the column's value directly, with no square root) — to the full displayed precision, in both sectors. A correct ℓ² triangle inequality (`‖base + correction‖ ≤ ‖base‖ + ‖correction‖`) requires adding the *norm*, not the *norm-squared*. Two readings are possible, and this auditor cannot adjudicate between them without the underlying certificate (which remains outside this repository, per the standing payload-transfer restriction):

- **(a) The column is mislabeled.** The value `3.7520048128694792e-06` (even) is actually the correction's ℓ² *norm* upper, not its norm-squared, and the column header should read "norm upper." Under this reading, the triangle computation and the "within the 0.002 cap" conclusion are both correct, and the only defect is a text label.
- **(b) The column is correctly labeled.** The value is genuinely the norm-*squared* upper, meaning the correction's actual ℓ² norm upper is `sqrt(3.7520048128694792e-06) ≈ 1.937e-3`. Under this reading, the displayed "whole-trial triangle upper" was computed by adding the wrong quantity (norm² instead of norm), and the **correctly computed** triangle bound is `base + sqrt(norm²) ≈ 2.105e-3` (even) / `≈2.103e-3` (odd) — **both exceeding the stated 0.002 cap**, which would reverse the entry's "within the cap" conclusion.

A secondary signal weighs toward reading (b): the reported outward `ℓ¹` value (`0.0032509` even) divided by `sqrt(norm_sq_value)` (`≈1.937e-3`) gives an `ℓ¹/ℓ²` ratio of `≈1.68` — a physically unremarkable ratio for a correction concentrated over part of its support — whereas dividing `ℓ¹` by the *unrooted* column value (`3.752e-6`) gives a ratio of `≈866`, within `sqrt(N)≈1020` but close enough to that extreme upper bound to require the correction to be almost perfectly uniform across essentially all 1,040,383 rows, which is a much less natural shape for a correction built to cancel a smoothly-decaying, concentrated residual profile (per the block-norm shape already confirmed in Round 289). This is a plausibility signal only, not a proof, but it points toward (b) over (a).

This is reported exactly as found, with the arithmetic shown, rather than guessed at or silently corrected. The resolution requires either the raw certificate (to compute the correction's actual exact-rational norm directly) or a clarification from Sandbox on which quantity the column holds.

## 4. Scope

v14.500 correctly keeps all closure/action/residual flags false and does not claim anything beyond "candidate constructed." The discrepancy above concerns only the candidate's own self-reported cap test, not any claim this round would otherwise accept at face value.

## 5. Verdict

```
Support, buffer size, delta_DM convention, log-midpoint continuity: all
  independently checked and found consistent/exact.
DISCREPANCY: the displayed "whole-trial triangle upper" in both sectors
  is reproduced exactly by adding the base trial upper to the table's
  "norm^2 upper" value WITHOUT a square root. If that column is a true
  norm-squared (plausibility evidence from the L1/L2 ratio leans this
  way), the correctly-computed triangle upper is ~2.105e-3 (even) /
  ~2.103e-3 (odd), which EXCEEDS the stated 0.002 cap -- reversing the
  entry's own conclusion. If the column is instead mislabeled (and
  actually already holds the norm, not norm^2), the cap-pass conclusion
  stands and only the column header is wrong. This auditor cannot
  adjudicate between the two without the raw certificate, which is not
  in this repository, and reports the finding for clarification rather
  than guessing.
No other defect found.
```

---

HANDOFF
target: lane-a, sandbox
type: audit-finding-requires-clarification
parent: v14.501
status: open
action: please clarify whether v14.500's "exact norm² upper (display)" column holds the correction's norm-squared or its norm. If norm-squared, the "whole-trial triangle upper" and the 0.002 cap-pass conclusion need to be recomputed using its square root, which this auditor's own computation suggests would exceed the cap in both sectors. If the column is simply mislabeled and already holds the norm, please correct the header text; no numerical recomputation would then be needed.
deliverable: clarification of the norm/norm² column, and if needed, a corrected cap-test verdict
constraints: None.
