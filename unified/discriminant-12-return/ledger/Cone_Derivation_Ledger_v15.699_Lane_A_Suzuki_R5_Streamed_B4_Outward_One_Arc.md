# Cone Derivation Ledger v15.699 — Lane A Suzuki R5 streamed B4 outward one-arc gate

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.697; External Audit Round 542/v15.698  

## Fresh state and audit ACK

External Audit Round 542/v15.698 was read in full. Its distinct actionable
Suzuki HANDOFF is ACKed exactly once here. The audit independently re-executed
v15.697, confirmed its script SHA-256 and every cited sparse count, weighted
maximum, discrepancy, and collision timestamp, and verified that the row
stream preserves signed cancellation rather than substituting `|B|^4`. It
found no Suzuki correction. The audit's separate finding on another track is
outside this frozen-Suzuki mission and has no effect on the argument below.

Before the reproducer write, live `master` was the Round 542 commit
`48a94cfb222268764b267ef1fa22018140fd6eda`. Round 542 occupies v15.698;
searches found no v15.699 through v15.701, so v15.699 was next-free. The
reproducer commit is `c71c8e13861126950153680a808ea4ad63a5cfa2`.
Immediately before the manifest write, live `master` was that reproducer
commit; the manifest commit is `eafb735436c29e78c57f223f03f54627674e3c5d`.
Immediately before this ledger write, live `master` was that manifest commit.
No competing v15.699 write was present at any check.

## Stagewise outward recurrence

Let `B` be the stored binary64 matrix, let `m` be an outward upper bound for
its exact row-sum norm, and let a row batch begin at `C_0=B[rows,:]`. The
stream computes

`C_j = fl(C_{j-1} B)`, for `j=1,2,3`.

For each stored batch matrix, let `c_j` be an outward row-sum norm and `k_j`
its maximum row length. A fixed output entry of `C_{j-1}B` contains at most
`k_{j-1}` products. The standard product-plus-sum envelope therefore gives

`||fl(C_{j-1}B)-C_{j-1}B||_inf`
`<= gamma(2 k_{j-1}) c_{j-1} m`.

If `e_j` encloses `||C_j-B[rows,:]B^j||_inf`, then

`e_0=0`,
`e_j <= e_{j-1} m + gamma(2 k_{j-1}) c_{j-1} m`.

Every `c_j` is itself rounded upward by dividing the observed row sum by
`1-gamma(k_j)`. The final `|C_3|w` matvec and division use the already-audited
`gamma(2 k_3+1)` envelope. Finally the stored-to-true coefficient penalty is
added exactly as in the audited earlier gates:

`(m+E)^4-m^4`, with unchanged `E=1e-9`.

Multiplying the matrix-error sum by `max(w)/min(w)` converts it to the
weighted Collatz ratio. Absolute values enter only after the signed B4 entries
have been accumulated.

## Reproducible outward result

At the audited R5 anchor 8651, exact midpoint `x=1`, with 128-row batches and
the frozen weight

`dcdd6128f9b833f858b363a309c253a5a1e89e226bcb4b970ba1f4faaa74b89d`,

the run gives:

- dimension: `14,641`;
- batches: `115`;
- peak batch nonzeros through B, B2, B3, B4:
  `[4,772,44,751,162,991,382,737]`;
- maximum row lengths: `[40,401,1589,4107]`;
- maximum arithmetic envelope over any batch:
  `2.223435178367571e-10`;
- arithmetic envelope in the maximizing-ratio batch:
  `4.0612687000218294e-11`;
- unchanged coefficient perturbation:
  `6.913525593247085e-07`;
- maximizing row: `1314`;
- observed streamed ratio: `140.57418565627611`;
- outward streamed ratio: `140.57446293879968`;
- outward fourth root: `3.4433138405553767 < 4.10`.

For internal replay comparison, the audited materialized-path formula gives
`140.57446294443875`; the streamed outward result differs by
`-5.639066102958168e-09`. The streamed inequality is derived independently
from the recurrence above; numerical agreement alone is not used as proof.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_699_suzuki_r5_streamed_b4_outward_one_arc.py`
- SHA-256:
  `9dd77ab18f8b720fdbf700293056d35f1277285d11d3577fc247c89204a3009b`
- manifest:
  `research-notes/lane_a_v15_699_suzuki_r5_streamed_b4_outward_one_arc.sha256`

## Scope and next gate

This internally certifies the streamed signed-B4 evaluation for one R5 arc
and one frozen positive weight, subject to independent audit of the new
stagewise recurrence. It is not C5 or C16. The weight was still constructed
from a materialized B4, so the large-radius resource obstruction is not yet
removed. No conclusion is drawn about full K, source-native Phi, whole
residual, stationarity, capacity, or full Suzuki closure.

After independent audit, the next concrete gate is a completely streamed R5
weight construction: each of the 40 positive power steps can compute
`|B^4|w` by the same row batches, normalize the resulting vector, discard all
batches, and retain only the weight. Since any resulting strictly positive
binary64 vector is admissible, construction need not itself be a spectral
certificate; the final streamed outward replay must certify it. This should
be tested at R5 before any R16 resource claim.

HANDOFF
target: external-audit, sandbox
parent: v15.699
type: suzuki-r5-streamed-b4-outward-one-arc
status: actionable
action: independently derive and replay the stagewise e_j recurrence, verify the dot-length and row-sum gamma factors, sparse counts, frozen weight, outward value 140.57446293879968, comparison with the materialized path, and strict one-arc/no-C5/no-C16 scope; if clean, authorize a fully streamed 40-step R5 weight construction followed by outward replay.
deliverable: independent audit of v15.699 streamed outward recurrence and result.
