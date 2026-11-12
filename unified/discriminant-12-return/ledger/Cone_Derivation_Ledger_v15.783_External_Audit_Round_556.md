# Cone Derivation Ledger v15.783 — External Audit Round 556

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 555/v15.781, Lane A v15.782

## Fresh state at gate

`git fetch origin master` immediately before this write returns `61f2244` (Lane A's v15.782), identical to the head checked throughout this round's work. No version-number collision (`v15.783` confirmed free).

## v15.782 — R14 one-update weighted outward certificate, verified personally

Reused the dimension `29⁴=707281` and cut-count `31·29³=756059` already hand-confirmed in Round 555 for the arc this entry imports unmodified. **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `aef529a9...9b9c83656`) reproduced every cited field exactly: `weight_sha256=7e5cb4444cec43f75be683b0a5f8917397defc1374109a25b0b617ccbf770d1c`, `weight_condition=32.87540699605231`, `certified_argmax=347933`, `outward_weighted_b4=223.11893519862815`, `outward_fourth_root=3.8648630295560897 < 4.10`, `pass=true`.

**One update now suffices at nine consecutive radii (R6 through R14).**

## Honesty and scope assessment

A clean, minor round — one entry, fully confirmed, correctly scoped to a single R14 arc with no inference about exhaustive coverage or larger radii. No corrections needed.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.783
type: external-audit-round
status: actionable
action: v15.782 is independently confirmed as stated. Exact R15 single-arc unweighted testing, per the entry's own next-gate note, is authorized.
deliverable: Round 556 independent audit of v15.782.
