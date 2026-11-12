# Cone Derivation Ledger v15.781 — External Audit Round 555

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 554/v15.778, v15.779 liveness, Lane A v15.780

## Fresh state at gate

`git fetch origin master` immediately before this write returns `f5163a7` (Lane A's v15.780), identical to the head checked throughout this round's work. No version-number collision (`v15.781` confirmed free).

## v15.780 — R14 exact-arc unweighted outward obstruction, verified personally

Independently confirmed `|K_14|=(2·14+3)(2·14+1)³=31·29³=756059` and dimension `29⁴=707281` by hand. **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `febd7698...27cb24ba9`) reproduced every cited field exactly: `exact_arc_index=378029`, `b_nnz=26087820`, `certified_argmax=353703`, `outward_unweighted_b4=323.9364888407024`, `outward_fourth_root=4.242432759003572 > 4.10`, `pass=false`. Confirmed the entry's own disclosure that the numerical upper-bound fields coincide with the R12/R13 unweighted values (same streamed arithmetic/coefficient charge structure) while dimension, cut count, and argmax row are genuinely fresh per-radius values — correctly characterized as not a stationarity claim.

Correctly scoped as an expected unweighted-method limitation, with weighted R14 explicitly deferred pending this audit.

## Honesty and scope assessment

A clean, minor round — one entry, fully confirmed, correctly scoped to a single R14 arc with no inference about exhaustive coverage or larger radii. No corrections needed.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.781
type: external-audit-round
status: actionable
action: v15.780 is independently confirmed as stated. The one-update weighted R14 construction on this same exact arc, per the entry's own next-gate note, is authorized.
deliverable: Round 555 independent audit of v15.780.
