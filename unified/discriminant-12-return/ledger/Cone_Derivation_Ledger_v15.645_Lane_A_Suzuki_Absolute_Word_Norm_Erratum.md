# Cone Derivation Ledger v15.645 — Lane A Suzuki v15.643 absolute-value witness correction

**Date:** 2026-11-10 (America/New_York). **Track:** original Suzuki five-frequency commutator, additive correction of v15.643; companion to numerical-only v15.644. **Status:** [D] outward rational absolute-value correction executed; independent audit pending. 

## Exact correction

The original v15.643 Python witness enumerated all signed piecewise-constant values of each transported `G^{qr}_{sigma,tau}` at all certified breakpoint intervals, but incorrectly formed its reported supremum enclosure by applying `max` to the **signed** values rather than first applying the absolute value required by `||G||_infinity`. That omission is a genuine logical defect in the old replay, even if the resulting values happen to match; v15.643 should be read together with this correction.

The corrected, additive witness `research-notes/lane_a_v15_645_corrected_absolute_word_norm_witness.py` explicitly applies outward rational `absi` to **each** cell enclosure before taking the maximum, then uses these maxima in the audited v15.499 tent penalty. It retains exact atanh logarithm remainder enclosures, integer-sqrt brackets, and certified breakpoint/wrap ordering. Replayed successfully with 40 words, each over its finite cell partition, and exact rational pass assertions for:

- `E_8^word < 485/1000 = 0.485`;
- `E_16^word < 142/1000 = 0.142`;
- `E_32^word < 39/1000 = 0.039`.

The corrected absolute-value implementation reproduced the old printed orientation numbers (respectively `0.4849756547931857`, `0.14117490094584004`, `0.038116518204005106`). Thus the v15.643 **numerical penalty values and strict caps survive**, but the corrected witness—not the originally omitted-absolute replay—is the appropriate producer for any downstream strict claim. The coincidence comes from each word's maximum positive cell being at least the magnitude of every negative cell, a property now checked through taking all cell absolute values rather than assumed.

## Frozen correction and audit

Witness path `unified/discriminant-12-return/research-notes/lane_a_v15_645_corrected_absolute_word_norm_witness.py`, commit `a3627120daee7bd74092da232a7e770afb2b3d14`. This is a new file; the original frozen v15.643 script remains immutable for traceability.

External Audit requested: independently replay the strict rational caps, verify four-breakpoint completeness for every q,r,s,t, confirm negative-cell magnitudes are not missed, and verify `E_16^word<0.142`. Pending audit, call the result **internally replayed, not independently certified**.

## Upstream and downstream

The separate v15.644 sparse-matrix computation is **binary64 reconnaissance only**: at one x=0.12345, radius-16 CSR has 1,185,921 sites and 44,182,908 nonzeros, sampled largest eigenvalue ~3.79708, not a uniform spectral-norm upper enclosure. Its attempted radius-16 negative extreme timed out; no two-sided bound is claimed. The missing gate stays `C_16=ess sup_x ||B_16(x)||<4.10` certified outward on both signs and all x. If that eventually passes, the corrected `E_16^word<0.142` will produce `||X||<4.242`, below required 4.249030150943723.

All source/frozen Suzuki artifacts and original C_S_32000, 3e-5/.002 thresholds, v14.405/v14.406 finite-plus-gap PASS, v14.814 later far FAIL, and once-only charges unchanged. Full-K transfer remains INCONCLUSIVE, and no source-native Suzuki synthesis is asserted. No physical/gravity/quarter-grid or whole-residual result follows.
