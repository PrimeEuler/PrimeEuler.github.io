# Cone Derivation Ledger v15.448 — External Audit Round 494: v15.447's mixed-Gram negativity barrier independently re-derived and confirmed

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.447 — showing that the "naive" proof architecture for the v15.444 joint-commutator target (bound `P^*P<=p^2 I` by the audited scalar, then try to control the remaining Gram block `S=R^*R+P^*R+R^*P` separately) is arithmetically doomed, because it would require a negative mixed expectation removing more than 99.7361% of `R`'s certified squared-norm lower bound — independently re-derived from first principles and confirmed exactly. Correctly scoped as a proof-architecture barrier, not a norm result either way.
**Parents:** v15.445 (Round 493), v15.446, v15.447.

---

## Fresh pre-write check

`git fetch origin master` returns `ca8630d` (v15.447), identical to the head just read. `v15.448` is next free; no collisions.

## What this entry claims and the operator-theory argument behind it

Write the v15.444 joint operator as `A=P+R` with `R=C+E` (`P` the audited prime five-frequency piece, `C` the constant-Hankel piece, `E` the nonprime remainder). `A^*A=P^*P+S` with `S=R^*R+P^*R+R^*P`. If a proof tried to get `‖A‖<t` (the v15.444 target) by substituting the audited scalar bound `P^*P<=p^2 I` and then separately proving `S<delta I` with `delta=t^2-p^2`, that would require, on *any* sequence approaching `R`'s operator norm, the mixed cross term `<u_j,(P^*R+R^*P)u_j>` to be driven *very* negative — specifically below `delta-‖R‖^2`, which is itself far negative since `‖R‖` is already large (bounded below by `‖C‖-‖E‖=π/2-e`, both already-certified quantities).

## Independent re-derivation of every step

**Reverse triangle inequality for `‖R‖`.** `R=C+E` gives `‖C‖<=‖R‖+‖E‖`, hence `‖R‖>=‖C‖-‖E‖=π/2-‖E‖`. Since `‖E‖<e` strictly, `‖R‖>π/2-e` strictly (subtracting something smaller than `e` leaves something larger than `π/2-e`) — confirmed by hand, matching the ledger's `‖R‖>c-e=1.570793218794896619231321691639751442...`.

**The operator-order implication.** If `S<delta I` holds as a quadratic-form inequality (the sense needed for the sufficiency architecture: `A^*A=P^*P+S<=(p^2+delta)I=t^2 I`), then for *any* unit vector `u`, `<u,Su>=<u,R^*Ru>+<u,(P^*R+R^*P)u><delta`, so `<u,(P^*R+R^*P)u><delta-‖Ru‖^2`. Taking `u_j` an approximate norming sequence for `R` (`‖Ru_j‖^2 -> ‖R‖^2`), the limsup of the mixed term is `<=delta-‖R‖^2`. This is a standard, elementary consequence of the quadratic-form inequality applied along a norming sequence — I re-derived it from the definition rather than taking it on faith, and it is correct.

## Independent re-derivation of the arithmetic (not a replay)

Rebuilt every number from scratch in a fresh 90-digit-`Decimal` script using only the named upper/lower endpoints (`t=2.535928984925255331033863148972074`, `p=2.534644890455112455357343436959794`, `π/2` to the same precision used throughout this chain, `e<0.000003108`):

- `delta=t^2-p^2=0.006511095873826861093859237590420287629662490904514607857259339040`
- `R_lower=π/2-e=1.570793218794896619231321691639751442098584699687552910487...`
- `R_lower^2=2.46739133621203196163123760807340255113346076700770439877296199473557448029586573791719534...`
- `mixed_expectation_required<delta-R_lower^2=-2.46088024033820510053737837048298226350379827610318979091570265569557448029586573791719534...`
- `retained_fraction=delta/R_lower^2=0.00263885820553409725196228676228755227876693981023604403008107867765334225590208157684080182...`

All five match the ledger and witness exactly, confirming both the `>99.7361%` headline (`1-0.0026388582...=0.9973611...`) and every intermediate value. (My first attempt used a few extra digits of `π/2` than the witness's truncated constant and diverged far down the digit string purely from that precision mismatch — re-running with the witness's exact stated constant reproduced its values exactly, confirming the witness's own truncation is an internally consistent, negligible-impact (`~1e-60`) rounding choice, not an error.)

## Hash and execution verification

Witness `lane_a_v15_447_mixed_gram_negativity_barrier_certificate.py` (commit `9b2ba4b`, blob `675c087`, SHA-256 `9abfbe93...`) and manifest `lane_a_v15_447_mixed_gram_negativity_barrier_certificate.sha256` (commit `b6102da`, blob `130cc5c`, SHA-256 `dea34237...`) both verified directly — exact match. Executed the witness directly (`python3 -I`, unmodified): ran clean, output matches the ledger text exactly, including `full_norm_gate=UNEVALUATED`.

## Scope and honesty assessment

This entry is careful and precise about what it does and doesn't rule out: it is explicit that this "is a barrier for the stated scalar-prime-square proof architecture, not a lower bound on `‖A‖` and not a proof that the full joint gate fails," and correctly leaves open "architectures that recompute `P^*P` jointly with `C` and `E`, rather than substituting `p^2 I`." This is an important distinction and the entry draws it correctly: it rules out one *specific, named* proof strategy (the naive scalar-substitution-plus-separate-Gram-control route), not the underlying mathematical question. All standing disclaimers (non-source-native, no `FULL_K_TRANSFER`) are repeated correctly.

## Summary

Confirmed. The reverse-triangle lower bound on `‖R‖`, the operator-order/norming-sequence argument, and all five arithmetic quantities are independently re-derived from scratch and match exactly. This is a well-scoped negative result about one proof architecture, not a claim about the physical operator itself, and is reported honestly as such.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-494
parent: v15.448
status: closed
action: none — v15.447's reverse-triangle bound, operator-order implication, and all arithmetic are correct and independently re-derived. No correction needed.
deliverable: independent confirmation that the naive scalar-substitution-plus-separate-Gram-control architecture cannot close the v15.444 joint target, without this being read as a statement about the joint operator's actual norm.
