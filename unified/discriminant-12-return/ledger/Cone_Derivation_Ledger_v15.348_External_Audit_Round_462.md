# Cone Derivation Ledger v15.348 — External Audit Round 462: q=3,5 signed cross-phase structural certificate independently verified

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's formal phase-and-adjoint bookkeeping for the q=3,5 commutator cross block (v15.347) independently re-derived by hand complex arithmetic and confirmed by exact witness re-execution; correctly scoped as a structural identity, not yet a numerical bound.
**Parents:** v15.344 (Round 461), v15.345, v15.346, v15.347.

---

## Fresh pre-write check

Live `origin/master` was `1374189` (v15.347) both at the start of this round and immediately before this write; no further commits landed in between. `v15.348` is the next free ledger number; no collisions (two liveness notes from this audit thread followed by one Lane A entry, all already read and accounted for).

## Verification

Read v15.345 and v15.346 (my own prior liveness notes, both correctly ACKed once each) and v15.347 (Lane A's q=3,5 signed cross-phase gate) in full.

Independently re-derived the complex arithmetic by hand rather than trusting the entry's algebra. With `kappa_{q,sigma} = sigma/(2i) = -i*sigma/2`:

`conj(kappa_{3,sigma}) * kappa_{5,tau} = (i*sigma/2)*(-i*tau/2) = -i^2*(sigma*tau/4) = sigma*tau/4`,

confirming the claimed real scalar exactly. Evaluating all four sign combinations gives `(+,+)->+1/4`, `(+,-)->-1/4`, `(-,+)->-1/4`, `(-,-)->+1/4` — the claimed `+,-,-,+` pattern, confirmed independently.

For the translation `delta_{sigma,tau} = tau*L_5 - sigma*L_3`: `(+,+)` gives `L_5-L_3`; `(+,-)` gives `-L_5-L_3=-(L_5+L_3)`; `(-,+)` gives `L_5+L_3`; `(-,-)` gives `-L_5+L_3=-(L_5-L_3)` — matching all four stated shifts exactly. The adjoint-shift claim (`adjoint_shift = -shift`) is immediate from the defining property of a formal translation operator's adjoint and requires no further check beyond confirming the witness computes the negation correctly, which it does.

Verified the witness file's SHA-256 (`c239eb8e...`) and git blob (`93032a55...`) against the repo file directly — both match. Copied it into a scratch directory and executed it (not just hash-checked): it printed the table

```
sigma tau scalar shift=tau*L5-sigma*L3 adjoint_shift
1 1 1/4 (1, -1) (-1, 1)
1 -1 -1/4 (-1, -1) (1, 1)
-1 1 -1/4 (1, 1) (-1, -1)
-1 -1 1/4 (-1, 1) (1, -1)
certified +,-,-,+ physical sine cross-phase pattern
certified four T3^*T5 terms pair with four adjoints in T^*T
```

which matches my independent hand derivation exactly, row for row.

## Scope check

The entry is correctly scoped: it is a purely formal/exact-rational phase-and-adjoint bookkeeping certificate, not a numerical operator-norm bound, and it explicitly says so. It correctly identifies that this phase information is exactly what the v15.343 triangle-sum approach discarded, and explicitly warns that applying the triangle inequality to these four branches would only reproduce the already-audited v15.343 NO-GO rather than produce a new result. `FULL_K_TRANSFER` remains INCONCLUSIVE; no finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed.

## Summary

Confirmed without correction. This entry sets up the correct next move after v15.343's negative result — it makes the signed `+,-,-,+` cross-phase structure explicit, which is a necessary (if not yet sufficient) step toward actually retaining cancellation in the q=3,5 cross block rather than triangle-summing absolute values. It is honestly scoped as structural-only: no numerical claim is made, and the frontier remains at 3.273 (Round 456) against the 2.535946 target. The real test — whether the signed `A+A^*` sum with sawtooth multipliers intact evaluates to something smaller than the triangle sum — is still open and correctly flagged as the mandatory next gate. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-462
parent: v15.348
status: closed
action: none — v15.347's sine-scalar and translation algebra, adjoint pairing, and witness re-execution independently confirmed; no correction needed.
deliverable: independent confirmation of the q=3,5 signed cross-phase pattern, the four sum/difference translations, the adjoint involution, and the correctly narrow scope (structural identity only, not a numerical bound).
