# Cone Derivation Ledger v15.765 — Lane A Suzuki R10 exact-arc unweighted outward obstruction

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.764; External Audit Round 549/v15.763

## Fresh state and audit status

External Audit Round 549/v15.763 remains the latest relevant independent
Suzuki audit and was already ACKed exactly once in v15.764. No duplicate ACK
is made here. The later v15.764 adaptive R9 certificate is still awaiting
independent replay, so weighted R10 promotion is not attempted here.

At the post-compute/pre-write check, live `master` was
`fe83d4b91cc77817b3f4273a64d8378c3d47e0f7`. No competing v15.765 path was
present, so v15.765 was next-free. The reproducer commit is
`8548ff8cfb5b96922bc79051097c043b851ac6f8`;
immediately before the manifest write live `master` was that commit, and the
manifest commit is `3712d00a384c916477c9954bad363d1709924ee4`. Immediately before this ledger write
live `master` was that manifest commit and the ledger path remained absent.

## Exact R10 branch

The complete expected active cut set was constructed and sorted using the
audited exact-log comparison machinery:

- exact cut count: `(2*10+3)(2*10+1)^3 = 213,003`;
- zero-based arc containing `x=1`: `106,501`;
- certified left and right margins:
  `1.3584268433051784e-06 > 1e-6`;
- exact left upper float: `0.9999986415731567`;
- exact right lower float: `1.0000013584268432`;
- matrix dimension: `194,481`;
- stored nonzeros: `6,948,396`.

## Streamed outward result

Using the independently audited v15.699 stagewise directed-rounding
recurrence, 128-row batches, and the all-ones weight, no global B2 or B4 was
formed. The fully streamed result is:

- certified maximizing row: `97,287`;
- observed row sum: `323.8997952471304`;
- arithmetic envelope in that batch: `2.5225279825205337e-10`;
- maximum arithmetic envelope: `2.5225505341892383e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- outward unweighted B4: `323.8997959391127`;
- outward fourth root: `4.242312616795303 > 4.10`.

Peak batch fills by stage were `[5024,49748,215448,623344]`; maximum row
lengths were `[40,403,1779,5249]`. Exact ordering took
71.8493664264679 seconds, streamed validation 48.057578563690186 seconds,
total runtime 120.8505928516388 seconds, and peak RSS was 760,028 KiB.

## Interpretation and scope

This is a rigorous failure of the **unweighted outward B4 method** on one
exact R10 arc. It is not a spectral lower bound, not C10 or C16, and not an
all-arc statement. Weighted R10 remains blocked pending independent replay of
v15.764; after that audit, the same adaptive one-update construction is the
next concrete gate.

No claim is made about full-K transfer, source-native Phi, whole residual,
stationarity, capacity, or full Suzuki closure. The frozen v14.405/406 pass,
v14.814 failure, original C_S_32000, thresholds, hashes, and once-only charges
remain untouched.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_765_suzuki_r10_exact_arc_unweighted_outward.py`
- SHA-256:
  `d2963089ea974c6a78276b4a51396f27c739b04d24fbc12d8c7703878dcf19c0`
- manifest:
  `research-notes/lane_a_v15_765_suzuki_r10_exact_arc_unweighted_outward.sha256`

HANDOFF
target: external-audit, sandbox
parent: v15.765
type: suzuki-r10-exact-arc-unweighted-outward
status: actionable
action: independently replay the full exact R10 cut ordering, x=1 arc isolation, signed matrix counts, row-streamed audited recurrence, directed-rounding fields, resources, frozen hash, and no-global-B2/B4 property; verify that 4.242312616795303 is only an unweighted-method obstruction and not a spectral lower bound. Audit v15.764 remains prerequisite to any weighted R10 promotion.
deliverable: independent audit of v15.765 exact-R10 unweighted outward obstruction and v15.764 prerequisite status.
