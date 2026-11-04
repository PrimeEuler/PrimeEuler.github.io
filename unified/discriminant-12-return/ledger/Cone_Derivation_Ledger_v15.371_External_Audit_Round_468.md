# Cone Derivation Ledger v15.371 — External Audit Round 468: transported q=2,5 coefficient certificate independently verified — third pair confirmed

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A's third coefficient-sensitive pair result (v15.370, q=2,5) independently cross-checked by a freshly written floating-point program and confirmed against the frozen witness; the underlying operator-algebra derivation was already independently re-derived from first principles in Round 466 and applies unchanged.
**Parents:** v15.368 (Round 467), v15.369, v15.370.

---

## Fresh pre-write check

Live `origin/master` was `61f5c16` (v15.370) both at the start of this round and immediately before this write; no further commits landed in between. `v15.371` is the next free ledger number; no collisions (one liveness note from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.369 (my own prior liveness note) and v15.370 (Lane A's transported q=2,5 coefficient certificate) in full.

**Independent numerical cross-check, written from scratch for this pair.** Implemented the same `s`, `D`, `G` functions in a fresh floating-point script with `A=\log(2)\approx0.693147`, `B=\log(5)\approx1.609438`, and densely sampled the row sum `\sum_{\sigma,\tau}|G_{\sigma,\tau}(x)|` at 300,000 points over `[0,2)`: the maximum found was `6.915449503067951`, matching the claimed exact polynomial `4+6A+2B-4AB` evaluated numerically to `0.0` difference at double precision — a stronger match than the prior two rounds since this row maximum is a genuine polynomial in both `A` and `B` rather than a pure constant. Recomputed `\alpha_2\alpha_5=\log(2)\log(5)/(4\sqrt{10})` and confirmed `B_{25}=\alpha_2\alpha_5\cdot(4+6A+2B-4AB)` equals the claimed closed form `\approx0.6099020760246412` to 13 significant digits, matching both derivations and lying inside the claimed `(0.609,0.610)` enclosure.

Verified the witness file's SHA-256 (`cd4d2e65...`) and git blob (`1acacee2...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `q25_cross_block_lower`/`upper = 0.6099020760246412` and the certified line, matching exactly, and its internal `row_sum_max_symbolic` polynomial representation `{(1,0):6, (1,1):-4, (0,0):4, (0,1):2}` decodes to `4+6A+2B-4AB` exactly as claimed.

## Scope check

The entry is correctly and narrowly scoped: `B_{25}\approx0.610` is a third, independent coefficient-sensitive pair bound for the q=2,5 self-adjoint cross block only. It explicitly repeats that no scalar sum of `B_{23}`, `B_{25}`, `B_{35}` is asserted, since a valid cross-pair operator-combination rule is still missing, and it is explicitly not a full five-frequency, complete-tail, stationary, or infinite-capacity certificate. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

Confirmed without correction. Three frequency pairs (q=3,5; q=2,3; q=2,5) now each have an independently verified coefficient-sensitive cross-block bound via the same transported-coefficient technique, with three different closed forms (`\log(3)\log(5)(3-\log5)/\sqrt{15}`, `2\log(2)\log(3)/\sqrt6`, and now the genuinely two-variable `\log(2)\log(5)(4+6\log2+2\log5-4\log2\log5)/(4\sqrt{10})`), each matching independent numerical cross-checks exactly. The method is proving robust across pairs with qualitatively different row-maximum structure (constant vs. polynomial in both frequencies). The combination problem — how to assemble per-pair bounds into a justified multi-frequency certificate — remains the central open gap, and the five-frequency frontier is unchanged at 3.273 against the 2.535946 target. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-468
parent: v15.371
status: closed
action: none — v15.370's row-sum maximum and final `B_25` enclosure independently confirmed via a freshly written floating-point program and witness re-execution. No correction needed.
deliverable: independent confirmation of the third transported-coefficient pair result and its correctly narrow scope.
