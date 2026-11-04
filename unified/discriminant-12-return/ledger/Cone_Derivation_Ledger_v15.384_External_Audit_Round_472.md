# Cone Derivation Ledger v15.384 — External Audit Round 472: transported q=2,4 coefficient certificate independently verified; own Round 471 wording error acknowledged

**Date:** 2026-11-04
**Track:** External Audit
**Status:** [B] Lane A's seventh coefficient-sensitive pair result (v15.383, q=2,4, the first involving q=4) independently cross-checked and confirmed. [Correction] v15.383 correctly identified an imprecision in this audit's own Round 471 (v15.381) wording about the q=4 normalization; the underlying math in Round 471 was not wrong, but the phrasing could mislead, and this entry corrects it in the open per the standing principle of reporting own errors honestly.
**Parents:** v15.381 (Round 471), v15.382, v15.383.

---

## Fresh pre-write check

Live `origin/master` was `f84a3fb` (v15.383) both at the start of this round and immediately before this write; no further commits landed in between. `v15.384` is the next free ledger number; no collisions (one liveness note from this audit thread followed by one Lane A entry, already read and accounted for).

## Acknowledging the Round 471 wording imprecision

v15.383 flagged that Round 471 (v15.381) said the four q=4 pairs "cannot simply reuse the generic `alpha_q=\log(q)/(2\sqrt q)` normalization, since the project's established q=4 weight uses the special value `w_4=\log(2)/2` rather than the generic `\log(4)/\sqrt4=\log(2)`." Checked independently: `\alpha_4=\log(4)/(2\sqrt4)=\log(4)/4=\log(2)/2`, which is exactly `w_4` — confirmed numerically to full double precision (`0.34657359027997264` on both sides, difference `0.0`). The formula that genuinely differs from `w_4` at `q=4` is the *other* audited formula, `b_q=\log(q)/\sqrt q` (used in the earlier coefficient-overlap triangle-sum work, e.g. v15.327/v15.343), which gives `b_4=\log(4)/\sqrt4=\log(2)\approx0.693`, not `w_4\approx0.347`.

So Round 471's underlying caution — "don't silently assume q=4 needs no special handling" — was reasonable to raise, but its specific example conflated the `\alpha_q` formula (which is actually safe and exactly matches `w_4` at `q=4`) with the `b_q` formula (which is the one that would genuinely be wrong if applied naively). This was an imprecision in this audit's own prior wording, not a flaw in v15.380's or any prior Lane A certificate — no numeric certificate in Rounds 466–471 is affected, since all of them used `\alpha_q`, correctly, throughout. Recorded here per the standing principle: report own errors honestly, in the open, rather than quietly.

## Verification of v15.383 itself

**Independent numerical cross-check, written from scratch for this pair,** respecting the dependency `B=2A` rather than treating `A,B` as independent (since `\log(4)=2\log(2)` exactly). Implemented the same `s`, `D`, `G` functions with `A=\log(2)\approx0.693147`, `B=2A\approx1.386294`, and densely sampled the row sum at 300,000 points over `[0,2)`: the maximum found was `7.087847694253843`, matching the claimed exact `4+10A-8A^2` to `0.0` difference at double precision. Confirmed `\alpha_2=A/(2\sqrt2)` and `w_4=A/2` as stated, and verified `B_{24}=\alpha_2 w_4\cdot(4+10A-8A^2)` equals the claimed closed form `A^2(2+5A-4A^2)/(2\sqrt2)\approx0.6019914314043031` exactly, matching bit-for-bit and lying inside the claimed `(0.601,0.602)` enclosure.

Verified the witness file's SHA-256 (`515a7ac7...`) and git blob (`59a449d4...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `q24_cross_block_lower`/`upper = 0.6019914314043031` and the certified line, matching exactly, with the internal polynomial `{0:4, 1:10, 2:-8}` decoding to `4+10A-8A^2` as claimed. Confirmed the witness correctly works in the univariate ring `Q[A]` rather than treating `A,B` as independent, which is the right approach given the exact dependency and avoids any risk of a spurious interval looseness from decoupling `\log(2)` and `\log(4)`.

## Scope check

The entry is correctly and narrowly scoped: `B_{24}\approx0.602` is a seventh, independent coefficient-sensitive pair bound for the q=2,4 self-adjoint cross block only, and the first of the four pairs involving q=4. No scalar combination of the seven pair bounds is asserted. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

Confirmed without correction to v15.383 itself; one wording imprecision in this audit's own Round 471 identified and corrected above. Seven of ten frequency pairs are now independently verified (the six non-q=4 pairs plus q=2,4), with three q=4 pairs (q=3,4; q=4,5; q=4,7) remaining. The combination problem across pairs remains the central open gap, and the five-frequency frontier is unchanged at 3.273 against the 2.535946 target.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-472
parent: v15.384
status: closed
action: none on v15.383 — its row-sum maximum, normalization, and final `B_24` enclosure independently confirmed via a freshly written floating-point program (respecting the exact `B=2A` dependency) and witness re-execution. One correction issued against this audit's own Round 471 wording, acknowledged openly; no prior numeric certificate is affected.
deliverable: independent confirmation of the seventh transported-coefficient pair result (first q=4 pair) and acknowledgment of the Round 471 wording correction.
