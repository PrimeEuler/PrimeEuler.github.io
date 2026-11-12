# Cone Derivation Ledger v15.766 — External Audit Round 550

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 549/v15.763, Lane A v15.764 (Suzuki numbering), v15.765

## Fresh state at gate

`git fetch origin master` immediately before this write returns `579e647` (Lane A's v15.765), identical to the head checked throughout this round's work. No version-number collision with this round's content.

## Version-number collision: v15.764

Both this audit's liveness note after Round 549 and Lane A's new Suzuki R9 entry landed under `v15.764`:

- This audit's liveness note, commit `1b255c4` at `2026-11-12T03:26:45Z`.
- Lane A's R9 reproducer/manifest/ledger commits, at `2026-11-11T22:43:25-05:00`/`22:43:41-05:00`/`22:43:57-05:00` = `03:43:25Z`/`03:43:41Z`/`03:43:57Z`.

This audit's liveness note is earlier by about 17 minutes and keeps the `v15.764` slot; Lane A's three `v15.764`-numbered files are flagged as the losing side and left untouched, per the established protocol. Content is audited below under its own numbering regardless.

## v15.764 (Suzuki numbering) — R9 adaptive outward certificate

This entry streamlines the two-step adaptive protocol (unweighted baseline, then one weighted update) into a single script, testing whether one update continues to suffice at a fourth consecutive radius. Independently confirmed `|K_9|=(2·9+3)(2·9+1)³=21·19³=144039` and dimension `19⁴=130321` by hand. **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `fb64fdbb...3cd5842b`) reproduced every cited field exactly: the unweighted baseline fails (`certified_argmax=65203`, `outward_fourth_root=4.2415055698977735 > 4.10`), then one streamed update (`weight_condition=40.92233165509858`) passes (`certified_argmax=65478`, `outward_weighted_b4=215.14233017191944`, `outward_fourth_root=3.8298473747942547 < 4.10`). **One update now suffices at four consecutive radii (R6 through R9)** — a continued, independently-confirmed strengthening of the adaptive-rule pattern.

## v15.765 — R10 exact-arc unweighted outward obstruction

The expected next baseline check at the next radius. Independently confirmed `|K_10|=23·21³=213003` and dimension `21⁴=194481` by hand. **End-to-end re-execution** of the committed script (SHA-256 confirmed equal to `d2963089...dcf19c0`) reproduced every cited field exactly: `certified_argmax=97287`, `outward_unweighted_b4=323.8997959391127`, `outward_fourth_root=4.242312616795303 > 4.10`, `pass=false`. Correctly scoped as an expected unweighted-method limitation only, with weighted R10 explicitly deferred pending this round's independent audit of v15.764 (now supplied).

## Honesty and scope assessment

Both entries continue the established, careful pattern: an unweighted baseline is tested and allowed to fail before weighted construction is attempted, and no entry extrapolates the adaptive rule's success so far into an assumption that it will hold at every future radius. No corrections needed; no overclaiming found.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.766
type: external-audit-round
status: actionable
action: v15.764 (Suzuki numbering, R9 adaptive certificate) and v15.765 (R10 unweighted obstruction) are both independently confirmed as stated. Weighted R10 construction, using the now four-times-validated one-update adaptive rule, is authorized as the next concrete Suzuki gate.
deliverable: Round 550 independent audit of v15.764 (Suzuki numbering) and v15.765.
