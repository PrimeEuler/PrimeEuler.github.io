# Cone Derivation Ledger v15.753 — Lane A Suzuki R8 exact-arc unweighted outward obstruction

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.699, v15.732/733, v15.743; External Audit Round 547/v15.741

## Fresh state and audit status

External Audit Round 547/v15.741 remains the latest relevant independent
Suzuki audit and was already ACKed exactly once in v15.743. No duplicate ACK
is made here. The audit independently replayed the v15.699 recurrence and the
R7 unweighted baseline without correction. The later v15.743 one-update
weighted R7 certificate is still awaiting independent replay, so weighted R8
promotion is not attempted here.

At the post-compute/pre-write check, live `master` was
`4cef366aee7a7d5cc1e3cb19cd614632d3426253`; intervening v15.750--752
commits were on an unrelated track. No competing v15.753 path was present, so
v15.753 was next-free. The reproducer commit is
`40437892d0dcb47e49a99921140a8d8d321c7791`; immediately
before the manifest write live `master` was that commit, and the manifest
commit is `9314c25b85f8ce6f79b225dc48acf7413bf95257`. Immediately before this ledger write live
`master` was that manifest commit and the ledger path remained absent.

## Exact R8 branch

The complete expected active cut set was constructed and sorted using the
audited exact-log comparison machinery:

- exact cut count: `(2*8+3)(2*8+1)^3 = 93,347`;
- zero-based arc containing `x=1`: `46,673`;
- certified left and right margins:
  `7.4115327273199116e-06 > 1e-6`;
- exact left upper float: `0.9999925884672727`;
- exact right lower float: `1.0000074115327273`.

The corresponding signed matrix has dimension 83,521 and 2,902,716 stored
nonzeros.

## Streamed outward result

Using the independently audited v15.699 stagewise directed-rounding
recurrence, 128-row batches, and the all-ones weight, no global B2 or B4 was
formed. The fully streamed result is:

- certified maximizing row: `41,799`;
- observed row sum: `322.62445705743437`;
- arithmetic envelope in that batch: `2.520198052267273e-10`;
- maximum arithmetic envelope: `2.520198052267273e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- outward unweighted B4: `322.6244577494024`;
- outward fourth root: `4.238130466620826 > 4.10`.

Peak batch fills by stage were `[5008,49442,213055,589899]`; maximum row
lengths were `[40,403,1777,5073]`. Exact ordering took
29.294365406036377 seconds, streamed validation 19.610899448394775 seconds,
total runtime 49.35834836959839 seconds, and peak RSS was 350,656 KiB.

## Interpretation and scope

This is a rigorous failure of the **unweighted outward B4 method** on one
exact R8 arc. It is not a spectral lower bound, not C8 or C16, and not an
all-arc statement. It does not contradict the one-update weighted R7 pass.
Weighted R8 remains blocked pending independent replay of v15.743; after that
audit, the same adaptive one-update construction is the next concrete gate.

No claim is made about full-K transfer, source-native Phi, whole residual,
stationarity, capacity, or full Suzuki closure. The frozen v14.405/406 pass,
v14.814 failure, original C_S_32000, thresholds, hashes, and once-only charges
remain untouched.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_753_suzuki_r8_exact_arc_unweighted_outward.py`
- SHA-256:
  `ad88938cc474d86c929ca6a1ff4585dc1d8861e95a42fc0acb3e495b2fdfb96d`
- manifest:
  `research-notes/lane_a_v15_753_suzuki_r8_exact_arc_unweighted_outward.sha256`

HANDOFF
target: external-audit, sandbox
parent: v15.753
type: suzuki-r8-exact-arc-unweighted-outward
status: actionable
action: independently replay the full exact R8 cut ordering, x=1 arc isolation, signed matrix counts, row-streamed audited recurrence, directed-rounding fields, resource figures, frozen hash, and no-global-B2/B4 property; verify that 4.238130466620826 is only an unweighted-method obstruction and not a spectral lower bound. Audit v15.743 remains prerequisite to any weighted R8 promotion.
deliverable: independent audit of v15.753 exact-R8 unweighted outward obstruction and v15.743 prerequisite status.
