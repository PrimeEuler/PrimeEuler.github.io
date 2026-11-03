# Cone Derivation Ledger v15.341 — External Audit Round 460: generic Cotlar-Stein route correctly closed as worse

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's generic-submultiplicativity Cotlar-Stein attempt independently re-derived, re-executed, and confirmed to be strictly worse than the existing bound — including a general proof the ordering is forced, not numerical coincidence.
**Parents:** v15.338 (Round 459), v15.339, v15.340.

---

## Fresh pre-write check

Live `origin/master` was `61abeae` (v15.340) both at the start of this round and immediately before this write; no further commits landed in between. `v15.341` is the next free ledger number; no collisions (two sequential Lane A commits after Round 459).

## Verification

Hand-derived the Cotlar-Stein construction: with `a_{q,r}=√(b_qb_r)` from generic submultiplicativity (`‖T_q^*T_r‖,‖T_qT_r^*‖≤b_qb_r`), the row sum for frequency `q` is `√b_q·Σ_r√b_r`, and the resulting bound is `√(max_qb_q)·Σ_r√b_r`. Computed `b_q=log(q)/√q` for all five frequencies by hand (`0.4902,0.6343,0.6931,0.7197,0.7356` for `q=2,3,4,5,7`) and confirmed `q=7` gives the maximum, matching the entry's claim.

Independently verified the **general forcing argument**, not just the specific numbers: since `b_r≤b_max` for every `r`, squaring shows `√(b_max·b_r)≥b_r` termwise, so summing gives `√b_max·Σ_r√b_r≥Σ_rb_r` always — proving the generic-Cotlar bound can never beat the plain triangle sum, regardless of the specific values of `b_q`. This is a stronger and more useful result than a one-off numeric comparison.

Verified the witness script's hashes (`5a2d31da...`/`5aa9007a...`) match the repo file exactly, and re-executed it: `triangle_upper=3.272807772456381769643485313281` (reproducing the already-verified v15.327 value) and `generic_cotlar_lower=generic_cotlar_upper=3.460483149063549479507173600723`, with the ordering assertion `B_triangle<B_generic_cotlar` passing — all matching the entry's stated values exactly.

## Scope check

The entry correctly scopes this as closing only the Cotlar-Stein route when the off-diagonal terms are bounded by generic submultiplicativity rather than by evaluating the actual coefficient overlaps in `T_q^*T_r`. It explicitly does not claim this is a lower bound and explicitly names the real next step (evaluate the actual shifted-multiplier overlaps, not substitute generic products). `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

Another quick, correctly-reasoned closure, and a particularly good one: Lane A didn't just check that the Cotlar-Stein route happens to be worse at these specific numbers, but proved it always will be whenever the off-diagonal terms are bounded generically rather than evaluated directly — a structural fact that rules out an entire style of attempt, not one instance of it. The frontier remains at 3.273 (Round 456) versus the 2.536 target, with the search now correctly narrowed to approaches that actually evaluate cross-frequency coefficient overlaps. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-460
parent: v15.341
status: closed
action: none — v15.340's Cotlar bound and the general forcing argument independently confirmed by hand derivation and re-execution; no correction needed.
deliverable: independent confirmation of the Cotlar-Stein row-sum construction, the q=7 maximizer, the exact numeric value, and the general proof that generic-submultiplicativity Cotlar bounds can never beat the plain triangle sum.
