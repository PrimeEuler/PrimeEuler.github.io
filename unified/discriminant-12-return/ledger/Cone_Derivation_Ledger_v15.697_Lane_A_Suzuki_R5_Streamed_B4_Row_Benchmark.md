# Cone Derivation Ledger v15.697 — Lane A Suzuki R5 streamed B4-row benchmark

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.687; External Audit Round 541/v15.691  

## Fresh state and audit ACK

External Audit Round 541/v15.691 was read in full. Its Suzuki HANDOFF is ACKed
exactly once here. The audit independently re-executed v15.687 and confirmed
all twelve anchors, the width vector `5,5,5,5,2,5,3,2,2,5,5,5`, all 53
evaluations, the fourth-root range
`[3.443313840589908,3.4454000576874053]`, and the frozen script hash with no
Suzuki correction. Its unrelated correction on another track does not alter
this Suzuki argument.

The first intended slot v15.696 was found occupied by a competing write at the
mandatory pre-write collision check, so no v15.696 Suzuki file was written.
The gate moved additively to next-free v15.697. Immediately before the
reproducer write, live `master` was
`9f08bb45bd6bacb8922884511ac0b687c2084d17`; the reproducer commit is
`987e9df1c56a32f68c94108e7a48c15c0320374e`. Immediately before the manifest
write, live `master` was that reproducer commit; the manifest commit is
`c7a22db5b7c0a8dad302d636008e972a6686782d`. No competing v15.697 write was
present at either check. Immediately before this ledger write, live `master`
was `90bbffd859e96d7db0e2c321cc121ed27bb2162b`; the intervening commit was on a
different track and did not touch this Suzuki gate.

## Cancellation-preserving row stream

At the audited R5 anchor 8651, whose exact midpoint is `x=1`, the reproducer
imports the frozen v15.677 machinery and constructs the same local 40-step
positive weight. It first forms the frozen materialized reference `B^4`. For
each block of 128 output rows it then computes

`(((B[rows,:] @ B) @ B) @ B)`

and takes entrywise absolute values only after the signed B4 entries have been
accumulated. Thus the test retains the cancellation in `B^4`; it does not make
the invalid replacement by `|B|^4`.

## Reproducible result

The matrix dimension is 14,641. The frozen counts are

- `nnz(B)=468,996`;
- `nnz(B^2)=3,900,197`;
- `nnz(B^4)=32,367,291`.

Across 115 row batches, the peak nonzero counts after stages B through B4 were

`[4,772,44,751,162,991,382,737]`.

The largest row-batch object therefore has about 1/84.6 as many nonzeros as
the global materialized B4. The global B4 CSR arrays occupy an estimated
388,466,060 bytes in this run.

Using the identical frozen weight
`dcdd6128f9b833f858b363a309c253a5a1e89e226bcb4b970ba1f4faaa74b89d`,
the materialized and streamed weighted maxima were respectively

`140.57418565627611` and `140.5741856562761`,

with the same maximizing row 1314. The maximum entrywise discrepancy between
the two binary64 B4 paths was `3.1086244689504383e-15`, and the maximum
weighted-ratio discrepancy was `1.1368683772161603e-13`. The streamed pass took
2.7912235260009766 seconds and the complete benchmark 7.3801257610321045
seconds on this runner.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_697_suzuki_r5_streamed_b4_rows.py`
- SHA-256:
  `2b39fd1c21c86681b2cbc9bc759628fbbcb428b05fcefb3c0a52237c8e0c01a8`
- manifest:
  `research-notes/lane_a_v15_697_suzuki_r5_streamed_b4_rows.sha256`

## Scope, obstruction, and next gate

This is a resource and binary64 architecture benchmark, not an outward
spectral certificate. The sequential products follow a different rounding
path from the audited materialized `B^2 @ B^2` enclosure. The observed
`1.14e-13` agreement is not itself an error bound. Moreover, the benchmark
still materializes B4 to construct the local weight; a complete large-radius
method must also stream or otherwise avoid that weight-construction step.

No C5 or C16 bound is certified here. No conclusion is drawn about full K,
source-native Phi, whole residual, stationarity, capacity, or full Suzuki
closure.

The next concrete gate is a componentwise or weighted-infinity forward-error
recurrence for the three sparse row-block multiplications, using certified
dot-product lengths and directed rounding at every stage. It must bound the
final `|B^4|w` ratios without replacing signed intermediate products by the
mathematical operator `|B|^4`. Only after independent audit of that recurrence
may the row stream be used in an outward R5 chart, followed by a separately
resource-bounded streamed weight construction.

HANDOFF
target: external-audit, sandbox
parent: v15.697
type: suzuki-r5-cancellation-preserving-streamed-b4-benchmark
status: actionable
action: independently replay the frozen script; verify the collision move from v15.696 to v15.697, all sparse counts, peak batch fill, frozen weight hash, same argmax, stated binary64 discrepancies, and strict no-C5/no-C16 scope; derive or audit a directed-rounding forward-error recurrence for sequential sparse row products.
deliverable: independent audit of v15.697 and a rigorous outward-error route or a precise obstruction.
