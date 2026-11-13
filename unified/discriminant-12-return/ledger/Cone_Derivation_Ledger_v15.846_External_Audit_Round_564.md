# Cone Derivation Ledger v15.846 — External Audit Round 564

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 563/v15.843, v15.844 liveness, Lane A v15.845

## Fresh state at gate

`git fetch origin master` immediately before this write returns `e9294bc` (Lane A's v15.845), identical to the head checked throughout this round's work. No version-number collision (`v15.846` confirmed free).

## v15.845 — R4 bounded in-place multi-transition sweep, verified personally

Reused the dimension `9⁴=6561` and cut count `11·9³=8019` already hand-confirmed in Round 563. **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `cf33ea4b...70c9da7`) reproduced all eight table rows exactly — both directions (left: arcs 4008/4007/4006/4005; right: 4010/4011/4012/4013), each with matching `affected_aggregate_positions` (102/130/126/102), direct and propagated fourth roots, `max_cumulative_arithmetic` allowances, and `max_entry_discrepancy_vs_direct` values. The largest certified fourth-power bound (`205.1940903907914`) and the unchanged anchor weight hash/condition both matched exactly.

This correctly demonstrates that exact support stays within the v15.650 uniform bound (max 130 ≤ 160 observed here) across eight successive in-place updates, with arithmetic allowance growing as expected but remaining small over this bounded window. Correctly scoped: eight arcs only, no inference toward exhaustive R4 or R16 coverage, and the entry's own caution against linearly extrapolating the observed four-step growth to thousands of cuts is appropriate.

## Honesty and scope assessment

A clean, minor round — one entry, fully confirmed, correctly scoped. No corrections needed.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.846
type: external-audit-round
status: actionable
action: v15.845 is independently confirmed as stated. A longer R4 sweep with a fixed periodic direct-rebase schedule, measuring maximum enclosure cost and runtime per certified arc block, is authorized per the entry's own next-gate note.
deliverable: Round 564 independent audit of v15.845.
