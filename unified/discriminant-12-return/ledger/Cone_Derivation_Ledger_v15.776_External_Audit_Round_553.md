# Cone Derivation Ledger v15.776 — External Audit Round 553

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 552/v15.772, v15.773 liveness, Lane A v15.774, v15.775

## Fresh state at gate

`git fetch origin master` immediately before this write returns `3c0c4af` (Lane A's v15.775), identical to the head checked throughout this round's work. No version-number collision (`v15.776` confirmed free).

## v15.774 — R12 one-update weighted outward certificate, verified personally

Independently confirmed `|K_12|=27·25³=421875` and dimension `25⁴=390625` by hand (both already confirmed in Round 552; reused here for the arc this entry imports unmodified). **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `c0f44998...c193c02d`) reproduced every cited field exactly: `weight_sha256=7fffbf1b6c4a468459132666882541bab68c1307907460140390d85eb41fb3b5`, `weight_condition=30.50105506379521`, `certified_argmax=194742`, `outward_weighted_b4=222.29753105714323`, `outward_fourth_root=3.861301020529779 < 4.10`, `pass=true`.

**One update now suffices at seven consecutive radii (R6 through R12).**

## v15.775 — R13 exact-arc unweighted outward obstruction, verified personally

Independently confirmed `|K_13|=(2·13+3)(2·13+1)³=29·27³=570807` and dimension `27⁴=531441` by hand. **End-to-end re-execution** of the committed script (SHA-256 confirmed equal to `f3a6361a...dda9334e27`) reproduced every cited field exactly: `exact_arc_index=285403`, `b_nnz=19481796`, `certified_argmax=265779`, `outward_unweighted_b4=323.9364888407024`, `outward_fourth_root=4.242432759003572 > 4.10`, `pass=false`. Confirmed the entry's own observation that the numerical upper-bound fields coincide with the R12 unweighted result (same streamed arithmetic/coefficient charge structure) while the dimension and argmax row are genuinely distinct per-radius values, not a stale reuse. Correctly scoped as an expected unweighted-method limitation, with weighted R13 explicitly deferred pending this audit of v15.774 — now supplied by this round.

## Honesty and scope assessment

Both entries continue the established disciplined pattern: testing the unweighted baseline at each new radius before promoting to the weighted method, scoping every result to a single arc, and no inference toward exhaustive coverage, C12/C13, or C16. No corrections needed; no overclaiming found.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.776
type: external-audit-round
status: actionable
action: v15.774 and v15.775 are both independently confirmed as stated. Weighted R13 construction, using the now seven-times-validated one-update adaptive rule, is authorized as the next concrete Suzuki gate.
deliverable: Round 553 independent audit of v15.774 and v15.775.
