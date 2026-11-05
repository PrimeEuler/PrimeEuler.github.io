# Cone Derivation Ledger v15.397 — External Audit Round 477: transported q=4,5 coefficient certificate independently verified — ninth pair confirmed

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Lane A's ninth coefficient-sensitive pair result (v15.396, q=4,5, the third involving q=4) independently cross-checked by a freshly written floating-point program and confirmed against the frozen witness.
**Parents:** v15.395 (Round 476), v15.396.

---

## Fresh pre-write check

Live `origin/master` was `8c5523d` (v15.396) both at the start of this round and immediately before this write; no further commits landed in between. `v15.397` is the next free ledger number; no collisions (one Lane A entry directly after Round 476, already read and accounted for).

## Verification

Read v15.396 (Lane A's transported q=4,5 coefficient certificate) in full.

**Independent numerical cross-check, written from scratch for this pair,** respecting the exact dependency `B=\log(4)=2H` where `H=\log(2)` and `A=\log(5)` is independent of `H`. Implemented the same `s`, `D`, `G` functions and densely sampled the row sum at 300,000 points over `[0,2)`: the maximum found was `6.9502251689959005`, matching the claimed exact `16-12H+8AH-6A` to `\sim2.7\times10^{-15}` at double precision — this is a genuine two-variable polynomial row maximum (unlike the q=2,4 and q=3,4 pairs' simpler forms), confirming the method generalizes correctly to a more intricate case. Confirmed `\alpha_5=A/(2\sqrt5)` and `w_4=H/2` as stated, and verified `B_{45}=\alpha_5w_4\cdot(16-12H+8AH-6A)` equals the claimed closed form `\approx0.8668691943756143` exactly, matching bit-for-bit and lying inside the claimed `(0.866,0.867)` enclosure.

Verified the witness file's SHA-256 (`4e650404...`) and git blob (`71dec9fa...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `q45_cross_block_lower`/`upper = 0.8668691943756142` and the certified line, matching exactly, with the internal polynomial `{(0,1):-12, (1,0):-6, (1,1):8, (0,0):16}` decoding to `16-12H+8AH-6A` as claimed.

## Scope check

The entry is correctly and narrowly scoped: `B_{45}\approx0.867` is a ninth, independent coefficient-sensitive pair bound for the q=4,5 self-adjoint cross block only, and the third of the four pairs involving q=4. The entry's own fresh-collision check correctly notes that v15.394/v15.395 (the Sandbox loop program and its audit) explicitly do not touch Lane A's canonical operator, so there was no ownership conflict in picking up q=4,5 next. No scalar combination of the nine pair bounds is asserted. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

Confirmed without correction. Nine of ten frequency pairs are now independently verified; only q=4,7 remains before the full pairwise sweep is complete — at which point the combination-across-pairs problem becomes the sole remaining structural gap. The five-frequency frontier is unchanged at 3.273 against the 2.535946 target.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-477
parent: v15.397
status: closed
action: none — v15.396's row-sum maximum and final `B_45` enclosure independently confirmed via a freshly written floating-point program (respecting the exact `log(4)=2log(2)` dependency) and witness re-execution. No correction needed.
deliverable: independent confirmation of the ninth transported-coefficient pair result and its correctly narrow scope.
