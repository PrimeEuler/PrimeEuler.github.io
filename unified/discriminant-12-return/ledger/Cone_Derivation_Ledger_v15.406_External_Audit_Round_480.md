# Cone Derivation Ledger v15.406 — External Audit Round 480: cross-pair cancellation budget independently verified

**Date:** 2026-11-05
**Track:** External Audit
**Status:** [B] Lane A's cross-pair cancellation budget (v15.405) independently re-derived from the already-verified Round 479 quantities (`D`, the diagonal contribution, and `P`, the ten-pair sum) and confirmed against the frozen witness. This is a bookkeeping/necessary-condition result, correctly scoped as such — it does not improve the 2.892 bound and makes no construction claim.
**Parents:** v15.402 (Round 479), v15.403, v15.404, v15.405.

---

## Fresh pre-write check

Live `origin/master` was `972c4a2` (v15.405) both at the start of this round and immediately before this write; no further commits landed in between. `v15.406` is the next free ledger number; no collisions (two liveness notes from this audit thread followed by one Lane A entry, already read and accounted for).

## Verification

Read v15.403 and v15.404 (my own prior liveness notes) and v15.405 (Lane A's cross-pair cancellation budget) in full.

This entry makes no new mathematical construction — it is exact arithmetic on quantities already independently verified in Round 479 (`D=2.181991963972277\ldots`, the diagonal contribution, and `P=6.181771216090852\ldots`, the ten-pair sum) against the fixed target `2.535946`. Independently recomputed, using only the already-verified `D` and `P` values (not re-trusting this new script's own recomputation of them): `\text{target}^2=2.535946^2=6.431022114916` exactly (confirmed via exact integer arithmetic, `2535946^2=6431022114916` so `(2535946/10^6)^2=6431022114916/10^{12}`); `\text{allowed\_cross}=6.431022114916-2.181991963972277=4.249030150943723`; `\text{required\_reduction}=6.181771216090852-4.249030150943723=1.9327410651471295`; `\text{fraction}=1.9327410651471295/6.181771216090852=0.31265166528911614`. All four figures match the entry's claims and the witness's printed output exactly, to the last printed digit.

Verified the witness file's SHA-256 (`0a8420be...`) and git blob (`986cf82a...`) against the repo file directly — both match. Copied it into a scratch directory and executed it directly: it printed `maximum_admissible_joint_cross=4.249030150943723`, `minimum_required_cross_pair_reduction=1.9327410651471295`, `minimum_required_fraction=0.31265166528911614`, matching exactly.

## Scope check

The entry is correctly and modestly scoped: it states plainly that this is "a necessary budget certificate, not a cancellation construction and not a lower bound on the physical operator," that it "does not improve the audited `2.892017147\ldots` upper bound by itself," and names the next admissible gate precisely (an evaluated joint cross-pair construction proving a joint self-adjoint cross contribution below `4.249030150943723\ldots`). This is useful, honest bookkeeping — it quantifies exactly how much cancellation across pairs (at least `31.27\%` of the current pair-sum budget) any future joint construction would need to find, which sharpens the target for that future work without claiming any of it has been done. `FULL_K_TRANSFER` remains INCONCLUSIVE.

## Summary

Confirmed without correction. This round adds no new operator-norm result — the frontier remains at `2.892017147\ldots` (Round 479) against the `2.535946` target — but it correctly converts the abstract "find more cancellation" directive into a concrete, numerically certified threshold for what a successful joint cross-pair construction must achieve. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-480
parent: v15.406
status: closed
action: none — v15.405's budget arithmetic independently re-derived from the already-verified Round 479 quantities and confirmed via witness re-execution. No correction needed.
deliverable: independent confirmation of the cross-pair cancellation budget and its correctly modest scope.
