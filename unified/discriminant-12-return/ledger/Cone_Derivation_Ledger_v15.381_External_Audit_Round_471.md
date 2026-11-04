# Cone Derivation Ledger v15.381 — External Audit Round 471: transported q=5,7 coefficient certificate independently verified — all six non-q=4 pairs now complete

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A's sixth coefficient-sensitive pair result (v15.380, q=5,7) independently cross-checked by a freshly written floating-point program and confirmed against the frozen witness. This completes all six frequency pairs not involving q=4.
**Parents:** v15.378 (Round 470), v15.379, v15.380.

---

## Fresh pre-write check

Live `origin/master` was `f177073` (v15.380) both at the start of this round and immediately before this write; no further commits landed in between. `v15.381` is the next free ledger number; no collisions (one liveness note from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.379 (my own prior liveness note) and v15.380 (Lane A's transported q=5,7 coefficient certificate) in full.

**Independent numerical cross-check, written from scratch for this pair.** Implemented the same `s`, `D`, `G` functions in a fresh floating-point script with `A=\log(5)\approx1.609438`, `B=\log(7)\approx1.945910`, and densely sampled the row sum at 300,000 points over `[0,2)`: the maximum found was `4.216359403778748`, matching the claimed exact `12-4B` to `~8.9e-16` at double precision — the same value as the q=3,7 and q=2,7 row maxima, since all three pairs share `B=\log7` as the larger frequency. Recomputed `\alpha_5\alpha_7=\log(5)\log(7)/(4\sqrt{35})` and confirmed `B_{57}=\alpha_5\alpha_7\cdot(12-4B)` equals the claimed closed form `\log(5)\log(7)(3-\log7)/\sqrt{35}\approx0.5580082505501808` to 15 significant digits, matching bit-for-bit and lying inside the claimed `(0.558,0.559)` enclosure.

Verified the witness file's SHA-256 (`2d48fa89...`) and git blob (`bbf70fba...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `q57_cross_block_lower`/`upper = 0.5580082505501808` and the certified line, matching exactly, with the internal polynomial `{(0,1):-4, (0,0):12}` decoding to `12-4B` as claimed.

## Scope check

The entry is correctly and narrowly scoped: `B_{57}\approx0.558` is a sixth, independent coefficient-sensitive pair bound for the q=5,7 self-adjoint cross block only. It correctly identifies that this completes all `\binom{4}{2}=6` pairs among the non-`q=4` frequencies `\{2,3,5,7\}`, and explicitly and carefully flags that the four remaining pairs involving `q=4` cannot simply reuse the generic `\alpha_q=\log(q)/(2\sqrt q)` normalization, since the project's established `q=4` weight uses the special value `w_4=\log(2)/2` rather than `\log(4)/\sqrt4=\log(2)`. This is a correct and careful scope boundary — reusing the generic formula for q=4 without checking it against the established special weight would silently introduce an error. No scalar sum of the six pair bounds is asserted, and this is not a full five-frequency, complete-tail, stationary, or infinite-capacity certificate. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

Confirmed without correction. All six frequency pairs not involving `q=4` (q=3,5; q=2,3; q=2,5; q=3,7; q=2,7; q=5,7) now have independently verified coefficient-sensitive cross-block bounds, each matching independent floating-point cross-checks exactly. Lane A's explicit caution about the q=4 special normalization is a good sign of care rather than a shortcut taken for convenience. The combination problem across pairs remains the central open gap, and the five-frequency frontier is unchanged at 3.273 against the 2.535946 target. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-471
parent: v15.381
status: closed
action: none — v15.380's row-sum maximum and final `B_57` enclosure independently confirmed via a freshly written floating-point program and witness re-execution. No correction needed.
deliverable: independent confirmation of the sixth transported-coefficient pair result, completing all non-q=4 pairs, and its correctly narrow scope including the flagged q=4 normalization caveat.
