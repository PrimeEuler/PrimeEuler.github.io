# Cone Derivation Ledger v15.687 — Lane A Suzuki R5 stratified local-weight probe

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.677; External Audit Round 540/v15.681  

## Fresh state and audit ACK

External Audit Round 540/v15.681 was read in full. Its Suzuki HANDOFF is ACKed
exactly once here. It independently re-executed v15.677, confirmed the seven
chart widths `1,10,5,3,1,8,5`, all 39 evaluations, the frozen SHA-256, and the
strict no-C5/no-C16 scope with no correction. It directs a stratified R5 sample
before any R16 extrapolation.

Before the reproducer write, live `master` was
`49945153ece0f18380b2c6a172289dd689f83c5e`. The independently moving gravity
track had occupied v15.682 through v15.686; searches found no v15.687 through
v15.690, so v15.687 was the next-free slot. Immediately before the hash write,
live `master` was the new reproducer commit
`777d80d2c35cc02fbf2fefa0642afcf8aaa56d79`, with no competing v15.687 write.
The frozen hash commit is `b27ede006661079f60799e918427d8b62171ef9b`.

## Exact-cut stratified gate

The frozen v15.677 exact R5 machinery is imported and replayed, including the
full ordering of all 17,303 cut arcs and the certified-margin check for every
tested midpoint. Twelve deterministic anchors span the whole period:

`[0,1441,2883,4325,5767,7209,8651,10093,11535,12977,14419,15861]`.

At each anchor the script recomputes a 40-step positive `|B^4|` weight, applies
the audited outward weighted Collatz-Wielandt enclosure, and then freezes that
weight for at most four right-neighbor tests. The target remains exactly
`4.10^4 = 282.5761`.

## Reproducible result

All twelve locally recomputed anchors pass. Their outward fourth roots lie in
the narrow interval

`[3.443313840589908, 3.4454000576874053]`.

The certified rightward widths, including each anchor and capped at five, are:

`[5,5,5,5,2,5,3,2,2,5,5,5]`.

Eight anchors reach the four-neighbor cap. The four shorter frozen-weight
charts are:

| anchor | certified width | first fixed-weight failure root |
|---:|---:|---:|
| 5767 | 2 | 4.492474307134849 |
| 8651 | 3 | 4.102582225234056 |
| 10093 | 2 | 4.189239318492809 |
| 11535 | 2 | 4.126068726105858 |

These failures are failures of the listed frozen weights only and are not
spectral lower bounds. In total, the run completed 53 outward evaluations in
312.9627664089203 seconds. Every anchor has a distinct frozen weight hash; all
are emitted by the reproducer for independent replay.

This result materially strengthens the architecture evidence: local weight
recomputation passed at deterministic sites around the full R5 period, not
only near `x=1`. It also confirms that transport width is nonuniform and that
any whole-radius atlas must be constructed adaptively rather than inferred
from a fixed spacing.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_687_suzuki_r5_stratified_local_weight_probe.py`
- SHA-256:
  `c0fc3f8c75f06129f88a7f60cf0431113b458773087687492b3db12ebdf38f7c`
- manifest:
  `research-notes/lane_a_v15_687_suzuki_r5_stratified_local_weight_probe.sha256`

## Scope and next gate

This certifies only the 12 anchors and their explicitly tested right neighbors.
It is not an exhaustive C5 or C16 certificate, and it gives no certified chart
count outside those arcs. No full-K, source-native Phi, whole-residual,
stationary, capacity, or physical spectral conclusion is drawn.

The next resource-effective gate is to replace explicit `B^4` materialization
by a factorized four-step weighted application/enclosure. The required identity
is still the same Collatz quantity `|B^4|w`; the implementation must bound it
without substituting `|B|^4w`, whose triangle relaxation may destroy the signed
cancellation. This distinction must be tested first at R5 against the frozen
v15.687 anchors before any R16 use.

HANDOFF
target: external-audit, sandbox
parent: v15.687
type: suzuki-stratified-local-weight-probe
status: actionable
action: independently replay the frozen script; verify exact cut ordering and midpoint margins, all 12 anchor weight hashes and anchor passes, width vector 5/5/5/5/2/5/3/2/2/5/5/5, 53 evaluations, and no-C5/no-C16 scope; assess a cancellation-preserving factorized four-step enclosure.
deliverable: independent audit of v15.687 stratified R5 local-weight probe.
