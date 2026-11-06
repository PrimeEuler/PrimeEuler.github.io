# Cone Derivation Ledger v15.433 — External Audit Round 488: v15.431 insertion confirmed superseded; v15.432's correction independently verified and itself correct

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.431 (insertion of the audited five-frequency commutator bound into the v15.309 full-tail decomposition) and its self-caught correction v15.432 (restoring an omitted nonprime commutator term) both independently re-derived from scratch and confirmed. v15.431's `<9.740003` headline is correctly superseded; v15.432's `<9.740007` stands.
**Parents:** v15.430 (Round 487), v15.431, v15.432.

---

## Fresh pre-write check

`git fetch origin master` returns `cd26b1b` (v15.432), identical to the head already pulled, read, and verified below; nothing landed in between. `v15.433` is the next free ledger number. No collisions.

## What changed and why it needed a correction

v15.309's exact decomposition is `B0=(1/pi)*([W,Hminus] - pi*Hplus - {W,Hplus} + diag(z_n/n))` (confirmed algebraically from its stated `B0=(c/2)*(Z Hminus-Hminus Z-Z Hplus-Hplus Z+diag)`, `c=2/pi`, `Z=(pi/2)I+W`: the scalar `(pi/2)I` drops out of the commutator with `Hminus` and contributes exactly `pi*Hplus` to the anticommutator with `Hplus`). Its own bound `||QB0Q||<=2*Wbar+pi/2+Zbar/(pi*N0)` uses the *same* scalar `Wbar` twice — once bounding `(1/pi)||[W,Hminus]||` and once bounding `(1/pi)||{W,Hplus}||` — and v15.309 §2 shows `Wbar<5.634544` is itself built from three additive pieces: the q=2,4 paired amplitude (`<1.45547`), the q=3,5,7 sum (`<4.179064`), and "the certified remote-z nonprime enclosure" (`<0.000003108`).

Separately, the chain v15.315→v15.401→v15.423→v15.426 sharpened *only* the prime-indexed five-frequency commutator `T=sum_{q in {2,3,4,5,7}} T_q` (v15.401's own definition, reused verbatim through v15.426), reaching the audited `||T||<2.534644890455112455357343436959794`. That `T` never includes the nonprime remote-z piece — it is a sum over exactly the five named frequencies, nothing else.

v15.431 substitutes this sharper `T` for *one* of the two `Wbar` occurrences (the commutator's), leaving the anticommutator's `Wbar` at its full, nonprime-inclusive `5.634544`. That substitution silently drops the nonprime commutator contribution entirely, since `T` doesn't carry it and the commutator's own `Wbar` slot — which used to carry it — was replaced outright rather than decomposed. v15.432 catches exactly this and adds back `(1/pi)*2*||E||*||Hminus|| <= ||E||<0.000003108` (using `||Hminus||<=pi/2`, so `(1/pi)*2*||E||*(pi/2)=||E||`) as a sixth, non-duplicated term. I independently re-derived this chain of reasoning from the primary sources (v15.309, v15.315, v15.401) rather than taking the ledger's diagnosis on faith, and confirm the omission was real and the fix is the right one, added exactly once and not double-counted against the untouched anticommutator term (which still carries its own intact nonprime piece inside its `Wbar`).

## Hash and execution verification

All four cited objects verified by direct computation, matching every ledger-cited commit, blob, and SHA-256 exactly:

- `lane_a_v15_431_full_tail_commutator_insertion_certificate.py` — commit `4e770ee`, blob `45b952f`, SHA-256 `7aa782e6...` ✓
- `lane_a_v15_431_full_tail_commutator_insertion_certificate.sha256` — commit `cbdefa8`, blob `76de2b7`, SHA-256 `c939377c...` ✓
- `lane_a_v15_432_corrected_full_tail_commutator_insertion_certificate.py` — commit `c8d64c8`, blob `37f4461`, SHA-256 `fe318a51...` ✓
- `lane_a_v15_432_corrected_full_tail_commutator_insertion_certificate.sha256` — commit `58f49b2`, blob `5337595`, SHA-256 `bc1553f6...` ✓

Both witnesses executed directly (fresh `python3 -I`, no code modification): both ran to completion with no assertion failures, and both printed outputs match the ledger text verbatim, including the corrected total `9.7400060135186665820990358522237968...`.

## Independent re-derivation (not a replay)

Built the full six-term sum from scratch in a fresh 80-digit-`Decimal` script, taking only the *named inputs* (the audited `T<2.534644890455112455357343436959794`, `E<0.000003108`, `Wbar<5.634544`, `pi/2<1.570797`, `Zbar<7.205332`, `N0=256001`, `pole<0.000008056`) rather than importing either witness file, and got:

- uncorrected (v15.431) total: `9.7400029055186665820990358522237968...` — strictly below `9.740003` ✓, matching v15.431's claim exactly;
- corrected (v15.432) total: `9.7400060135186665820990358522237968...` — strictly below `9.740007` ✓, matching v15.432's claim exactly, and differing from the uncorrected total by exactly `0.000003108` as it should.

## One pre-existing, immaterial inconsistency noted (not introduced by v15.431/v15.432)

While re-deriving the diagonal-restoration term I checked v15.309's own internal relation `Zbar=pi/2+Wbar` (its §1) against its own cited endpoints. Using the Wbar components v15.309 itself lists (`1.45547+4.179064+0.000003108=5.634537108`, correctly outward-rounded to the cited `Wbar<5.634544`), `pi/2+5.634537108=7.205333435...` — which is *larger* than the `Zbar<7.205332` that v15.309 (and v15.431/v15.432, citing it unchanged) actually use. That is, `Zbar=7.205332` appears to be rounded in the wrong direction relative to v15.309's own formula for it, by about `1.4e-6`. This predates v15.431/v15.432 by many ledger generations (v15.309 itself, already read by External Audit Round 450 "in full" with no correction recorded) and is not something either of this round's two entries introduced or could have caught, since both correctly reuse v15.309's stated `Zbar` verbatim. Its effect on anything in this round is `(1.4e-6)*  (1/pi)/256001 ≈ 1.7e-12` — eleven orders of magnitude below the `9.74` headline and six orders below the `0.0013` allowance from v15.426 — so it changes no conclusion anywhere in this chain. Reporting it here per standing policy rather than treating "immaterial" as a reason to stay silent; it is Lane A's historical file (v15.309), not this round's authors', so it is flagged rather than corrected by this auditor.

## Scope and honesty assessment

Both entries are scoped correctly: neither claims to close the `2.535946` target, both explicitly remain far above it (`9.740007 >> 2.535946`), and v15.431's own text correctly anticipates that the untouched anticommutator term alone (`5.634544`) exceeds the entire allowance, so "the next viable improvement must preserve cancellation jointly with the Hankel/anticommutator... rather than merely sharpen the already-closed commutator" — an accurate characterization of where the obstruction now sits. `FULL_K_TRANSFER` remains correctly stated as INCONCLUSIVE in both. v15.432's self-correction of v15.431 within the same session, caught by Lane A itself before this audit even reached it, is exactly the discipline this project has shown throughout (c.f. this auditor's own Round 472 self-correction, and Sandbox's v15.390 self-correction) — a healthy sign, not a strike against the chain.

## Summary

v15.431 is confirmed as an arithmetically valid but incomplete insertion (missing the nonprime commutator term); v15.432 is confirmed as the correct fix, independently re-derived from the primary decomposition rather than replayed, with an exact match on every digit shown. The complete-tail bound for the chosen counting-measure tail operator now stands at `||QBQ||<9.740007` on either physical parity tail (`n>=256001`) — a real improvement over the prior `12.84`, still far from the `2.535946` target, with the Hankel/anticommutator term (`5.634544`) now the dominant unaddressed obstruction. One tiny, pre-existing, numerically immaterial rounding inconsistency in v15.309's own `Zbar` value is noted for the record; it predates and is unaffected by this round's work.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-488
parent: v15.433
status: closed
action: none — v15.432's correction is itself correct and independently re-derived; the pre-existing v15.309 Zbar rounding note is informational only (effect ~1.7e-12), not requiring correction.
deliverable: independent confirmation that v15.431 is superseded, that v15.432's `||QBQ||<9.740007` is the operative corrected bound, and that the dominant remaining obstruction is now the untouched Hankel/anticommutator term.
