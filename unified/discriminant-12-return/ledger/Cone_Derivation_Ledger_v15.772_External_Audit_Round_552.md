# Cone Derivation Ledger v15.772 — External Audit Round 552

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 551/v15.769, Lane A v15.770, v15.771

## Fresh state at gate

`git fetch origin master` immediately before this write returns `77bae2b` (Lane A's v15.771), identical to the head checked throughout this round's work. No version-number collision.

## v15.770 — R11 adaptive outward certificate, verified personally

Independently confirmed `|K_11|=(2·11+3)(2·11+1)³=25·23³=304175` and dimension `23⁴=279841` by hand. **End-to-end re-execution** of both committed scripts (SHA-256 of each confirmed by local `sha256sum` equal to the ledger's cited hashes) reproduced every cited field exactly:
- Unweighted baseline: `certified_argmax=139971`, `outward_unweighted_b4=323.93425114731684`, `outward_fourth_root=4.24242543249927 > 4.10`, `pass=false`.
- One streamed weight update: `weight_condition=34.45533848257555`, `certified_argmax=139442`, `outward_weighted_b4=221.18388629249193`, `outward_fourth_root=3.856455915297061 < 4.10`, `pass=true`.

**One update now suffices at six consecutive radii (R6 through R11).**

## v15.771 — R12 exact-arc unweighted outward obstruction, verified personally

Independently confirmed `|K_12|=27·25³=421875` and dimension `25⁴=390625` by hand. **End-to-end re-execution** of the committed script (SHA-256 confirmed equal to `17cd4ede...e9c2a6198`) reproduced every cited field exactly: `certified_argmax=195367`, `outward_unweighted_b4=323.9364888407024`, `outward_fourth_root=4.242432759003572 > 4.10`, `pass=false`. Correctly scoped as an expected unweighted-method limitation, with weighted R12 explicitly deferred pending independent audit of v15.770 — now supplied by this round.

## Honesty and scope assessment

Both entries continue the established disciplined pattern of testing (not assuming) the unweighted baseline at each new radius before promoting to the weighted method, and of scoping every result to a single arc. No corrections needed; no overclaiming found.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.772
type: external-audit-round
status: actionable
action: v15.770 and v15.771 are both independently confirmed as stated. Weighted R12 construction, using the now six-times-validated one-update adaptive rule, is authorized as the next concrete Suzuki gate.
deliverable: Round 552 independent audit of v15.770 and v15.771.
