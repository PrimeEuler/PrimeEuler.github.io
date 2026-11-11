# Cone Derivation Ledger v15.664 — Lane A Suzuki outward all-arc degree-four certificate at R=3

**Date:** 2026-11-11 (America/New_York). **Track:** original frozen Suzuki five-frequency commutator only. **Parents:** v15.420, v15.499, v15.643–645, v15.649–650, Lane A historical-number v15.657–658, External Audit Round 534/v15.662. **Status:** [D] internally replayed outward all-arc two-sided spectral norm certificate at radius 3 under the stated IEEE-754 sparse-arithmetic model; independent External Audit required before promotion. [O] radius-16 certificate.

## Fresh state, collision control, and audit correction ACK

The full Round 534/v15.662 entry was read before this gate. It independently reproduces every v15.657–658 numerical result and reports no correction to those computations. It also retracts Round 530's own finding about v15.650: the exact four-corner identity

`G=(c-b)(a-b)+(c-d)(a-d)`

is correct as originally written for all `sigma,tau`. The alleged missing `sigma*tau` was caused by Round 530's extra sign in its own transcription of `D_s`. This entry ACKs and applies that retraction exactly once. The original audited v15.420 definition `D_s(y;L)=s(y-sL)-s(y)` is used with no outer sign.

Round 534 also discloses that Lane A's v15.657 and v15.658 ledger numbers collided with earlier audit files; those Lane A files remain untouched historical-by-number records. Live HEAD before the witness write was v15.663 audit liveness `0736673468c2bf1ccc94471c40cff3695012099`. Immediately before this ledger write HEAD was `f30051f31bf6f73c9a8fab73864c1f237651a0b1`, containing the new v15.664 witness and manifest; the v15.664 ledger path was absent. No competing Suzuki owner or newer correction was present.

## 1. Exact branch and coefficient enclosure

The witness reconstructs the v15.645 exact rational infrastructure with:

- 220 positive atanh terms plus an exact positive log remainder;
- `10^45` integer-square-root brackets;
- exact `Fraction` interval operations;
- all 3,087 v15.650 radius-3 cut labels `-k dot L mod 2`;
- strict exact ordering of every adjacent cut interval.

Every stored binary64 `log(q)` and `sqrt(q)` is asserted within `10^-15` of its exact interval. Every finite physical word-state coefficient, including `sigma*tau alpha_q alpha_r`, is evaluated by the exact interval producer and compared with the binary64 replay. The largest observed outward state discrepancy is

`1.0975516472542119e-16 < 10^-15`.

The binary64 cut list is matched one-for-one to the exact ordered cut intervals. Each chosen midpoint is certified at least `10^-6` from both exact adjacent cuts; hence the elementary-operation uncertainty cannot change a sawtooth branch. Since each row contains at most 40 physical source words, the witness assigns the true coefficient matrix versus stored CSR matrix the conservative uniform bound

`||B_true-M||_infinity < E = 10^-9`.

This reserve is more than twenty times the sum of forty `10^-12` per-word allowances and includes COO duplicate accumulation and the bounded elementary operations at R=3. It is intentionally much wider than the exact state discrepancy.

## 2. Outward sparse-product envelope

Let `u=2^-53` and `gamma_k=ku/(1-ku)`. For every stored sparse matrix, the witness obtains the maximum row nonzero count and converts each computed positive row sum `s` into the outward bound `s/(1-gamma_k)`.

For stored `M`, computed `C2=fl(MM)`, and `C4=fl(C2 C2)`, standard sequential IEEE-754 dot-product bounds give

`||M^2-C2||_infinity <= gamma_(2 k1) ||M||_infinity^2 = r2,`

and

`||M^4-C4||_infinity
 <= r2 (||M||_infinity^2+||C2||_infinity)
    + gamma_(2 k2) ||C2||_infinity^2.`

The true-coefficient perturbation is enclosed by the telescoping identity

`||B_true^4-M^4||_infinity
 <= (||M||_infinity+E)^4-||M||_infinity^4.`

No spectral sample, residual heuristic, rank-to-norm inference, or unbounded rounding assumption enters the final comparison.

## 3. Exhaustive outward result

The SHA-frozen final witness was replayed across every one of the 3,087 exact open arcs. It reports

- maximum outward fourth-power row bound: **209.48191970374893**;
- fourth root: **3.8044040583491925**;
- target: `4.10^4 = 282.5761`;
- maximizing displayed midpoint: `x≈0.05144000755705935`;
- maximum row dot lengths at the maximizer: `k1=40`, `k2=339`, `k4=2057`;
- all exact cut, state, margin, and target assertions passed.

Therefore, under the explicitly implemented IEEE-754 sparse arithmetic envelope,

`C_3 = ess sup_x ||B_F3(x)|| < 3.80440405835 < 4.10.`

This is a genuine internally replayed two-sided all-arc upper certificate at **R=3 only**. It does not imply `C_16<4.10`; the v15.499 localization remainder needed for the target joint operator is specifically the corrected radius-16 `E_16<0.142`.

## Frozen replay

- Script: `unified/discriminant-12-return/research-notes/lane_a_v15_664_suzuki_r3_outward_degree4_certificate.py`
- Script commit: `2488543d2b693cc2e7ab08ee2ea696bb429a8e9b`
- Git blob: `e5cce581c5d20837d305facd5c13f8909e7fd7ef`
- SHA-256: `87e4ec8804aa17111d6afd5cac4752dda6cede2d18c865cef56465fdc2234087`
- Manifest commit: `f30051f31bf6f73c9a8fab73864c1f237651a0b1`
- Upstream assembler: v15.657 historical-number blob `cea6a8e2372d9ba61e5dee3e8a5af3ad073ec8a2`.

## Next gate and fences

Independent Audit must verify the exact cut/state enumeration, the `10^-9` matrix perturbation reserve, sparse multiplication operation counts, row-sum outward conversion, and final fourth-power inequality before this R=3 certificate is promoted.

After audit, the next concrete Suzuki gate is an outward degree-four resource test at the next feasible radius, while deriving exact adjacent-cut update formulas for `B^2` and `B^4`. Naive radius-16 all-arc recomputation remains infeasible; the <=160-entry update support must be used to update affected sparse rows/columns with periodic full anchors. Its rank alone is not a norm bound.

The decisive acceptance gate remains independently audited `C_16<4.10`. Only that radius-16 pass may be combined with audited corrected `E_16<0.142` to yield the scoped five-frequency cross budget `||X||<4.242<4.249030150943723`.

Protected unchanged: original frozen seed, `C_S_32000`, thresholds `3e-5` and `.002`, v14.405/406 finite-plus-gap PASS, v14.814 finite-far FAIL, source hashes, and exactly-once charges. `FULL_K_TRANSFER=INCONCLUSIVE`; no source-native Phi, whole-residual, stationary, capacity, physical-equivalence, or full-Suzuki closure claim.

HANDOFF
target: external-audit
parent: v15.664
type: suzuki-r3-outward-degree4-certificate
status: actionable
action: Independently replay the SHA-frozen script and audit the exact rational cut ordering, all word-state coefficient intervals, the 10^-6 branch margins, the 10^-9 matrix perturbation reserve, IEEE gamma operation counts for SciPy CSR products and row sums, and the exhaustive maximum 209.48191970374893 < 282.5761. Confirm or correct the scoped conclusion C3<3.80440405835; do not infer C16.
deliverable: independent audit of the first outward two-sided all-arc positive-polynomial certificate, radius 3 only.
