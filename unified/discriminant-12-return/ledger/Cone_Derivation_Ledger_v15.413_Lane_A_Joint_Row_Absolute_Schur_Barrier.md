# Cone Derivation Ledger v15.413 — Lane A: exact common-row five-frequency absolute-Schur barrier

**Date:** 2026-11-05. **Track:** Lane A / Suzuki, frozen five-frequency commutator; not complete tail. **Parents:** v15.357 (signed sawtooth), v15.364–v15.400 (ten audited transported pair coefficients), v15.401 (all-pair Gram triangle), v15.405–v15.406 (strict budget), v15.408–v15.409 and v15.412 (individual-information barriers). **Status:** [D] exact rational interval witness at one shared coordinate; [O] cancellation-preserving operator-level joint estimate.

**Live pre-write:** current HEAD `db92f0eb904f8f24c6f2bb045ce75f2e3c0b178e`, containing only the new independent witness, after prior `v15.412` HEAD. No prior v15.413 ledger found. No existing sources modified.

## Gate: shared-coordinate row sum is insufficient

Use the *same* signed sawtooth `s(x)=1-(x mod 2)`, shift differences `D_sigma(x;L)=s(x-sigma L)-s(x)`, and transported products from audited v15.364 for every unordered pair `q<r` of `Q={2,3,4,5,7}`:

`G_{sigma,tau}^{qr}(x)=D_sigma(x+sigma L_q;L_q) D_tau(x+sigma L_q;L_r) + D_{-tau}(x-tau L_r;L_r) D_{-sigma}(x-tau L_r;L_q)`,

where `L_q=log(q)` and `alpha_q=log(q)/(2 sqrt(q))` (in particular `alpha_4=log(2)/2`). The absolute Schur row estimate on the **common** variable x is

`J_row = sup_{x in R/(2Z)} sum_{q<r} alpha_q alpha_r sum_{sigma,tau in {±1}} |G_{sigma,tau}^{qr}(x)|.`

This differs crucially from the separate-max sum `P=sum B_{qr}=6.18177121609...` from v15.401/412, since the maximum is taken **after** assembling all ten functions on one common x.

### Rigorous pointwise test

Set the **fixed rational coordinate** `x=3/1250` (no data-dependent contour or state choice). Evaluate all ten pair rows by exact rational interval arithmetic using:

- For q>1, `log q = 2 sum_{k=0}^{N-1} t^{2k+1}/(2k+1) + R_N`, `t=(q-1)/(q+1)`, `0<R_N<2 t^{2N+1}/((2N+1)(1-t²))`, `N=140`.
- `sqrt(q)` enclosed between `floor(sqrt(q)*10^35)/10^35` and the next grid point, with integer `isqrt`.
- All sawtooth wrap floors certified to agree throughout each input interval; products, sums, absolute values and reciprocal calculations done on rationals, no floating decision enters an assertion.

The frozen witness produces

`5.5 < sum_{q<r} alpha_q alpha_r sum_{sigma,tau}|G_{sigma,tau}^{qr}(3/1250)| < 5.6`.

For orientation only, the floating midpoint prints `5.570316360001187`; this is not used as the certificate. Consequently

`J_row > 5.5 > 4.249030150943723...`

while the v15.405 necessary cross budget to attain `||T||<2.535946` by the audited Gram decomposition is **strictly below** `4.249030150943723...`.

**Conclusion:** even after preserving a *shared* row coordinate, an argument that proves the joint cross-block norm only by the common-row **absolute Schur sum** cannot reach the required target. This is a no-go for that specific upper-bound method: its computed candidate upper bound is too large. It is **not** a lower bound on the true joint operator norm, nor does it exclude beneficial interference invisible to the absolute-value sum. This fact is stronger and more physically grounded than v15.412's abstract separate-max information barrier.

The row computation is a certified lower bound on the **maximum of an explicitly defined bound function**, not a spectral lower bound. Whether some translations coincide and can be combined before absolute values must be checked before interpreting J_row as the sharpest available Schur route; the witness treats individual pair translation groups exactly as in the ten audited pair certificates.

## Frozen exact witness

`research-notes/lane_a_v15_413_joint_row_witness.py`
- commit `db92f0eb904f8f24c6f2bb045ce75f2e3c0b178e`
- Git blob `9936a12f62c9a83b09ad6161d3bb649cee98513f`
- run `python3 unified/discriminant-12-return/research-notes/lane_a_v15_413_joint_row_witness.py`.
- The reproducible strict assertions require the joint row at x=3/1250 to exceed 11/2, exceed 17/4, and be below 28/5. No numerical rounding is admitted to the pass conditions.

## Next gate

Determine exact collisions among the full signed translation labels `±log q ±log r` across pairs (including the relation log4=2log2); combine any coincident shifts with their *signed* coefficients and phase before absolute values. If labels remain distinct, abandon common-row absolute-Schur optimization and develop a genuinely operator-level joint Cotlar/Gram or weighted-shift crossed-product certificate that retains interference across distinct translations. The objective remains a justified joint-cross bound below the v15.405 budget, not an artificial reduction of separately proved estimates.

No source-canonical Suzuki synthesis, full-K transfer, complete residual, stationarity, capacity or new seed asserted. v14.405/406 finite-plus-gap PASS and v14.814 finite-far FAIL remain; protected C_S_32000, 3e-5, .002 and exactly-once accounting unchanged. Independently auditable; no Sandbox computation requested.
