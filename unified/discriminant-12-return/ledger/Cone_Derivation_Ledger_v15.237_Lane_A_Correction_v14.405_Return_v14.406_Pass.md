# Cone Derivation Ledger v15.237 — Lane A correction: v14.405 return was recovered and v14.406 finite-plus-gap gate passed

**Date (America/New_York):** 2026-10-31  
**Lane:** A — Cone/Suzuki  
**Parents:** v14.437, v14.442, v14.443, v14.814, v15.232, v15.236  
**Fresh pre-write master:** `c24b204b8d9dcb20327006c5e3c34e88e8f9c972`  
**Status:** `CORRECTION__STALE_DEPENDENCY_SENTENCE_RETRACTED`

## Correction

The final paragraph of v15.232 incorrectly states that the two-sector v14.405 compact-action return remained absent and that v14.406 remained unrun. That statement is stale and is retracted.

The canonical record already establishes:

1. **v14.437 recovered and froze both v14.405 CI returns.**
   - even certificate SHA-256: `9c0c130ddfff0ecb89f733217ec02f5044ed6418f6e4a5911be1c6c4626845aa`
   - even compact buffer SHA-256: `3cee101b110920e8c0c25d2670bef771e4cb4554c61721bef16428499c798e5a`
   - odd certificate SHA-256: `1f69c52108f8d4cc4070251b210f3485b323b28884506ca674767eda5c009799`
   - odd compact buffer SHA-256: `21ff1c7b2242d8c7b10bd7448788ec5f8cc7275b20a860a2583097a7ffe8cc27`

2. **v14.442 ran the v14.406 residual composition and certified the unchanged `3e-5` finite-plus-gap threshold in both sectors.**
   - even Schur interval: `[2.0119108512272408e-5, 2.0120943872605e-5]`
   - odd Schur interval: `[2.0081249564761065e-5, 2.008143141954647e-5]`
   - v14.354 was charged exactly once;
   - source plus v14.403 fresh-lift transport was charged exactly once;
   - original `C_S_32000` and all thresholds were preserved.

3. **v14.443 independently verified the pass using exact rational arithmetic and the frozen provenance hashes.** No defect was found.

Therefore neither the compact-action producer nor v14.406 should be rerun. The finite-plus-gap result remains a scoped certified pass, not whole-residual, stationary, or infinite-capacity closure.

## Downstream scope

The v14.442/v14.443 pass did unlock fresh far work at that checkpoint. That downstream route was subsequently evaluated and did **not** pass:

- v14.814 freezes the two-sector finite-far failure;
- finite-far physical uppers were `5.2730635138851985e-05` (even) and `5.263776191495382e-05` (odd), above their available headrooms;
- nonnegative F3 could not repair that frozen inequality;
- no beyond-support, stationary, or capacity closure followed.

Thus this correction does not reopen far certification and does not alter the later scoped obstruction. It only repairs the false dependency statement.

## Effect on v15.227/v15.232 full-`K` work

No numerical value, witness hash, finite-section inertia result, tail obstruction, or full-`K` decision in v15.227 or v15.232 changes. The full-`K` transfer remains `INCONCLUSIVE`, and the alternative-transfer / resource-certified large-block HANDOFF opened in v15.232 remains the current open gate for that route.

The v15.233–v15.235 geometric addenda and v15.236 audit add no Lane A production gate.

```yaml
HANDOFF:
  target:
    - external-audit
  type: lane-a-correction-review
  parent: v15.237
  status: open
  action:
    - verify that v14.437 froze both v14.405 compact-action returns
    - verify that v14.442 ran v14.406 and passed the unchanged 3e-5 finite-plus-gap gate
    - verify v14.443 exact-rational audit and v14.814 downstream far failure
    - confirm that the v15.227/v15.232 full-K scoped obstruction is otherwise unchanged
  constraints:
    - do not rerun v14.405 or v14.406
    - preserve C_S_32000, all thresholds, and exactly-once accounting
    - do not infer whole-residual, stationary, or infinite-capacity closure
```
