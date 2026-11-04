# Cone Derivation Ledger v15.374 — External Audit Round 469: transported q=3,7 coefficient certificate independently verified — fourth pair confirmed

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A's fourth coefficient-sensitive pair result (v15.373, q=3,7) independently cross-checked by a freshly written floating-point program and confirmed against the frozen witness.
**Parents:** v15.371 (Round 468), v15.372, v15.373.

---

## Fresh pre-write check

Live `origin/master` was `d6c83b9` (v15.373) both at the start of this round and immediately before this write; no further commits landed in between. `v15.374` is the next free ledger number; no collisions (one liveness note from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.372 (my own prior liveness note) and v15.373 (Lane A's transported q=3,7 coefficient certificate) in full.

**Independent numerical cross-check, written from scratch for this pair.** Implemented the same `s`, `D`, `G` functions in a fresh floating-point script with `A=\log(3)\approx1.098612`, `B=\log(7)\approx1.945910`, and densely sampled the row sum at 300,000 points over `[0,2)`: the maximum found was `4.216359403778747`, matching the claimed exact `12-4B` to `0.0` difference at double precision. Recomputed `\alpha_3\alpha_7=\log(3)\log(7)/(4\sqrt{21})` and confirmed `B_{37}=\alpha_3\alpha_7\cdot(12-4B)` equals the claimed closed form `\log(3)\log(7)(3-\log7)/\sqrt{21}\approx0.4917396414482828` exactly, matching bit-for-bit and lying inside the claimed `(0.491,0.492)` enclosure.

Noted that this pair's row-maximum closed form `12-4B` is structurally identical to v15.364's q=3,5 result (`12-4\log5`), just with `B=\log7` instead of `B=\log5` — plausible since both pairs share `A=\log3` as the smaller frequency and the branch/case structure of the sawtooth reduction depends on which of `A,B` is larger and by how much, which is the same qualitative configuration (`1<A<B<2`) in both cases.

Verified the witness file's SHA-256 (`f162322a...`) and git blob (`ac2b8743...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `q37_cross_block_lower`/`upper = 0.4917396414482828` and the certified line, matching exactly, with the internal polynomial `{(0,1):-4, (0,0):12}` decoding to `12-4B` as claimed.

## Scope check

The entry is correctly and narrowly scoped: `B_{37}\approx0.492` is a fourth, independent coefficient-sensitive pair bound for the q=3,7 self-adjoint cross block only. It explicitly repeats that no scalar sum of the four pair bounds (`B_{23}, B_{25}, B_{35}, B_{37}`) is asserted, since the cross-pair combination rule is still missing, and it is not a full five-frequency, complete-tail, stationary, or infinite-capacity certificate. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

Confirmed without correction. Four of the ten possible frequency pairs among `{2,3,4,5,7}` now have independently verified coefficient-sensitive cross-block bounds (q=3,5: ≈0.635; q=2,3: ≈0.622; q=2,5: ≈0.610; q=3,7: ≈0.492), each via the same transported-coefficient technique and each matching independent floating-point cross-checks exactly. The combination problem remains the central open gap, and the five-frequency frontier is unchanged at 3.273 against the 2.535946 target. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-469
parent: v15.374
status: closed
action: none — v15.373's row-sum maximum and final `B_37` enclosure independently confirmed via a freshly written floating-point program and witness re-execution. No correction needed.
deliverable: independent confirmation of the fourth transported-coefficient pair result and its correctly narrow scope.
