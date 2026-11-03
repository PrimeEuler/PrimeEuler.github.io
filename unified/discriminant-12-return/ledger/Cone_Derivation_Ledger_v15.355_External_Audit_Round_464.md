# Cone Derivation Ledger v15.355 — External Audit Round 464: same-translation phase NO-GO independently verified

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's same-translation phase-collection result for the q=3,5 cross block (v15.354) independently re-derived by hand (all eight branch/adjoint terms regrouped by shift) and confirmed by exact witness re-execution.
**Parents:** v15.352 (Round 463), v15.353, v15.354.

---

## Fresh pre-write check

Live `origin/master` was `75dfe58` (v15.354) both at the start of this round and immediately before this write; no further commits landed in between. `v15.355` is the next free ledger number; no collisions (one liveness note from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.353 (my own prior liveness note) and v15.354 (Lane A's same-translation phase NO-GO) in full.

Independently reconstructed all eight terms (four branches `A_{sigma,tau}` plus their four adjoints) from the v15.347 data, rather than trusting the entry's table. Using `scalar=sigma*tau/4`, `shift=(tau,-sigma)` for `A_{sigma,tau}`, and `shift=-(tau,-sigma)`, same scalar, for its adjoint:

- `A(+,+)`: shift `(1,-1)`, scalar `1/4`. `A*(+,+)`: shift `(-1,1)`, scalar `1/4`.
- `A(+,-)`: shift `(-1,-1)`, scalar `-1/4`. `A*(+,-)`: shift `(1,1)`, scalar `-1/4`.
- `A(-,+)`: shift `(1,1)`, scalar `-1/4`. `A*(-,+)`: shift `(-1,-1)`, scalar `-1/4`.
- `A(-,-)`: shift `(-1,1)`, scalar `1/4`. `A*(-,-)`: shift `(1,-1)`, scalar `1/4`.

Regrouping by shift (not by the entry's own grouping, to check independently):

- shift `(1,-1)` [`+(L5-L3)`]: `A(+,+)` and `A*(-,-)`, both scalar `1/4`, sum `1/2`.
- shift `(-1,1)` [`-(L5-L3)`]: `A*(+,+)` and `A(-,-)`, both scalar `1/4`, sum `1/2`.
- shift `(1,1)` [`+(L5+L3)`]: `A*(+,-)` and `A(-,+)`, both scalar `-1/4`, sum `-1/2`.
- shift `(-1,-1)` [`-(L5+L3)`]: `A(+,-)` and `A*(-,+)`, both scalar `-1/4`, sum `-1/2`.

This matches the entry's claimed four groups and the reinforcing (not canceling) phase sums `+1/2, +1/2, -1/2, -1/2` exactly, confirming independently that the two scalars sharing a translation are always equal rather than opposite.

Verified the witness file's SHA-256 (`a63d5658...`) and git blob (`dfeb286e...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: its printed groups and phase sums matched my hand derivation term-for-term (same eight tuples, same four sums), and the final certified line read `same-translation phase factors reinforce: +1/2,+1/2,-1/2,-1/2`.

## Scope check

The entry is correctly scoped: it proves only that the already-audited scalar sine phases do not cancel within an equal-translation group. It explicitly does not claim the physical operator has no cancellation — the two terms sharing a translation still carry distinct, unevaluated sawtooth coefficient multipliers, and cancellation may still occur inside their coefficient sum or jointly across the four distinct translations. It explicitly flags that replacing those multipliers by norms would just return to the already-closed v15.343/v15.351 routes. `FULL_K_TRANSFER` remains INCONCLUSIVE; no finite Schur inertia, whole-residual, stationary, or infinite-capacity certificate is claimed.

## Summary

Confirmed without correction. This closes another specific shortcut attempt — hoping that grouping terms by identical translation would reveal scalar-phase cancellation — and correctly reports that it does not: the paired phases reinforce. The entry is careful to distinguish this from the still-open question of whether the actual sawtooth coefficient functions (not yet evaluated) cancel when summed within or across these groups. The frontier remains at 3.273 (Round 456) against the 2.535946 target. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-464
parent: v15.355
status: closed
action: none — v15.354's eight-term phase collection, four same-translation groups, and reinforcing phase sums independently confirmed by hand derivation and witness re-execution; no correction needed.
deliverable: independent confirmation of the same-translation phase-collection result and the correctly narrow scope (scalar phases only; sawtooth coefficient cancellation remains open).
