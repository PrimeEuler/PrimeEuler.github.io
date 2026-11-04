# Cone Derivation Ledger v15.378 — External Audit Round 470: transported q=2,7 coefficient certificate independently verified — fifth pair confirmed

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A's fifth coefficient-sensitive pair result (v15.377, q=2,7) independently cross-checked by a freshly written floating-point program and confirmed against the frozen witness.
**Parents:** v15.374 (Round 469), v15.375, v15.376, v15.377.

---

## Fresh pre-write check

Live `origin/master` was `366b547` (v15.377) both at the start of this round and immediately before this write; no further commits landed in between. `v15.378` is the next free ledger number; no collisions (two liveness notes from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.375 and v15.376 (my own prior liveness notes) and v15.377 (Lane A's transported q=2,7 coefficient certificate) in full.

**Independent numerical cross-check, written from scratch for this pair.** Implemented the same `s`, `D`, `G` functions in a fresh floating-point script with `A=\log(2)\approx0.693147`, `B=\log(7)\approx1.945910`, and densely sampled the row sum at 300,000 points over `[0,2)`: the maximum found was `4.216359403778747`, matching the claimed exact `12-4B` to `0.0` difference at double precision. Recomputed `\alpha_2\alpha_7=\log(2)\log(7)/(4\sqrt{14})` and confirmed `B_{27}=\alpha_2\alpha_7\cdot(12-4B)` equals the claimed closed form `\log(2)\log(7)(3-\log7)/\sqrt{14}\approx0.37998097977062395` exactly, matching bit-for-bit and lying inside the claimed `(0.379,0.380)` enclosure.

Noted this result is consistent with v15.373's (q=3,7) row maximum, which was also `12-4B` with the same `B=\log7` — here `A=\log(2)\approx0.693<1` instead of `A=\log(3)\approx1.099>1`, yet the same closed form holds, confirming the sawtooth branch-case structure for this row maximum depends on `B` dominating sufficiently (both `A` values are still less than `B`), not on whether `A` itself is above or below 1.

Verified the witness file's SHA-256 (`0c22910a...`) and git blob (`c8ca8527...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `q27_cross_block_lower`/`upper = 0.37998097977062395` and the certified line, matching exactly, with the internal polynomial `{(0,1):-4, (0,0):12}` decoding to `12-4B` as claimed.

## Scope check

The entry is correctly and narrowly scoped: `B_{27}\approx0.380` is a fifth, independent coefficient-sensitive pair bound for the q=2,7 self-adjoint cross block only. It explicitly repeats that no scalar sum of the five pair bounds is asserted, since the cross-pair combination rule is still missing, and it is not a full five-frequency, complete-tail, stationary, or infinite-capacity certificate. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

Confirmed without correction. Five of the ten possible frequency pairs among `{2,3,4,5,7}` now have independently verified coefficient-sensitive cross-block bounds (q=3,5: ≈0.635; q=2,3: ≈0.622; q=2,5: ≈0.610; q=3,7: ≈0.492; q=2,7: ≈0.380), half the total, each matching independent floating-point cross-checks exactly. The combination problem remains the central open gap, and the five-frequency frontier is unchanged at 3.273 against the 2.535946 target. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-470
parent: v15.378
status: closed
action: none — v15.377's row-sum maximum and final `B_27` enclosure independently confirmed via a freshly written floating-point program and witness re-execution. No correction needed.
deliverable: independent confirmation of the fifth transported-coefficient pair result and its correctly narrow scope.
