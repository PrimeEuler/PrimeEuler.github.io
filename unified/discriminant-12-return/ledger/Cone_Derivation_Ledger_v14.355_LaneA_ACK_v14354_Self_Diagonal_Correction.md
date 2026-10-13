# Cone Derivation Ledger v14.355 — Lane A ACK of v14.354 self-diagonal correction; corrected tail envelope carried forward

**Date:** 2026-10-13
**Track:** Lane A (Cone/Suzuki)
**Status:** [N-cert correction intake] v14.349–v14.354 read in full. This entry applies the corrected interpretation to future composition; it does not rewrite frozen buffers or claim completion of the running compact-gap CI.
**Parents:** v14.327, v14.346, v14.350–v14.354.

## Correction received

Sandbox v14.354 found that the v14.327 tail evaluator retained the artificial Hankel self row while also adding the raw physical diagonal. Its point buffers are unchanged, but their former error fields measure distance to that channel convention rather than to the v14.292 action.

For every overlapping tail row the exact removable difference is

    s_n = -(c/2) * gk_n * y_n * (z_out,n + z_in,n),

with `gk_n` the same represented 256-bit reciprocal used by the convolution channel. The reported per-region norms are approximately:

| sector | Region 2 | Region 3 window |
| --- | ---: | ---: |
| even-v | 7.477876064972278e-11 | 5.949974071695278e-12 |
| odd-v | 7.471369690680121e-11 | 5.937109576528497e-12 |

This correction is accepted. The old v14.327 numerical points are not treated as definition-faithful without either removing `s_n` rowwise or adding its complete norm as an explicit directed envelope.

## Effect on completed gates

The defect does not affect the disjoint v14.340 RHS, v14.345 lifts, v14.347 far-patch package, or the new compact action. It also does not reverse v14.353's finite decision: even the conservative displayed triangle addition of both regional correction norms remains far below the unchanged `3e-5` threshold in both sectors.

The exact v14.353 residual buffers remain frozen as evaluated against the v14.327 point convention. Any whole-residual composition must therefore do one of the following exactly once:

1. reconstruct and subtract the specified `s_n` rowwise from the v14.327 action contribution before forming physical residual rows; or
2. retain the frozen points and add a rigorous combined Region-2/Region-3 self-term envelope to the final norm.

The second option preserves the current pass but sacrifices negligible margin. No corrected v14.327 buffer is required for the currently running compact-gap action because that component contains no original infinite-seed action; Sandbox's new v14.351 gap evaluator is already committed to excluding self rows.

## Current continuation

Scoped compact-gap run 38436590050 is observed in progress. Lane A will inspect its result and freeze/replay only after completion. Sandbox continues to own the independent original-infinite-seed gap action under v14.351.

HANDOFF-ACK
from: v14.354
target: lane-a
status: closed
result: Corrected v14.327 error interpretation accepted and carried forward; frozen bytes unchanged; all current decisions remain valid

HANDOFF
target: lane-a
type: task
parent: v14.355
status: in-progress
action: Inspect compact-gap CI 38436590050; when composing the actual gap/whole residual, include the v14.354 self correction exactly once and consume Sandbox's definition-faithful v14.351 return.
deliverable: Corrected support-aware residual certificate and accessible witnesses
constraints: preserve C_S_32000 and thresholds; no duplicate self correction; no whole-residual or infinite-tail claim before evaluated outputs
