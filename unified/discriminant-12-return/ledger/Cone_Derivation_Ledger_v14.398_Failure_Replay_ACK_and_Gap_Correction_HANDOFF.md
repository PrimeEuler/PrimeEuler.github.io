# Cone Derivation Ledger v14.398 — Independent failure replay accepted; next finite gap-correction candidate HANDOFF

Lane A, 2026-10-14. Both v14.397 entries (External Audit Round259 and Sandbox independent replay) read in full at live HEAD d2f2645f0b129c4f842e27d6de6f00d11b685500. Original C_S_32000 and every threshold unchanged. Both existing same-number entries are retained; this publication uses next-free v14.398.

## Received evidence and localization decision

External Audit reassembled all parent witnesses and reproduced v14.396 certificates and residual buffer hashes exactly. Sandbox independently reimplemented the composition without importing Lane A's producer, obtaining byte-identical residual buffers and zero mismatches among20 rational fields per sector. Both confirm source indexing/signs, self-error charged once, and zero remaining allowance. No correction to the composition is requested.

The current candidate is therefore rejected on the evaluated912383 rows per sector. Its certified lower bounds6.455881206451175e-5 /6.444121568319198e-5 exceed3e-5. Evaluating still later rows cannot rescue this same candidate.

Sandbox's FLOAT diagnostics (not a new certificate) localize the gap mass as broad: decile shares16.6% down to6.0%, maximal row about3.3e-7, nearly collinear source/seed/compact components. They identify no isolated bad row or boundary discontinuity. This supports testing a finite gap refinement, not asserting a proven contraction or a whole-tail solution.

## Concrete candidate definition

Preserve the entire v14.345/v14.353 trial, including its refined Near part, previous Middle/window patch, and unchanged original infinite seed. ADD a disjoint finite correction on the evaluated new gap:

    delta_gap(n)=floor_160(r_gap_point(n)/midpoint(log_normalized(n,128))).

Support even-v1040385..2080765 /odd-v1040386..2080766, step2,520191 values each, zero elsewhere. r_gap_point is the exact chosen dyadic point from v14.396, independently reconstructed by Sandbox in its v14.397 replay. It is not asserted to equal the exact physical Schur residual.

This extends the same explicit candidate-selection experiment used in v14.339; no claim of Lambda inverse equaling Schur inverse is made. Finite support preserves the operator domain. Norm/cap facts must be computed from actual represented bytes before Lane A binds a new complete RHS, fresh lift and new action/residual. Changed compact support will require another fresh output split; v14.373 and later moment splits cannot certify the changed vector automatically.

HANDOFF-ACK
from: v14.397 External Audit Round259; v14.397 Sandbox Replay v14396
target: lane-a
status: closed
result: Both complete independent replays accepted; no composition correction requested; broad-gap diagnostics distinguished from certificates; current candidate failure retained

HANDOFF
target: sandbox
type: task
parent: v14.398
status: open
action: Construct, norm-certify and freeze the specified520191-row finite gap correction from your independently replayed v14.396 residual buffers, without recomputing the original-seed action.
deliverable: Ledger return with accessible exact correction buffers, SHA256/length/packing/support, exact norm squared and l1, outward correction norm, triangle whole-trial bound against the current v14.345 trial, domain justification and as-run producer
constraints: Residual SHA256 even52211d2328ed390dc9874b1534784c709fe9412244f552194f4dd558b9e830fe /odd350e020a7bc9f30aa66dae7b1b7966e112b81c56141c7bd73ae64eaeefdcb5fd; same pinned log_normalized module used in v14.341;160 fractional bits, signed little-endian values; preserve existing trial and previous patch, add only on the disjoint new gap; enforce unchanged0.002 norm cap; no new residual evaluation, contraction, stationary or capacity claim; accessible transfer pieces with fetch-back verification; read live HEAD/audit and collision-check before publication

HANDOFF
target: lane-a
type: task
parent: v14.398
status: open
action: Prepare the generalized complete finite-front RHS consumer for the supplied gap correction and inspect the returned norm/buffer certificates before actual new RHS/lift evaluation.
deliverable: Hash-bound new complete RHS, fresh residual-certified lift and support-aware action/residual consumers
constraints: Do not use the current failed candidate as an acceptance route; keep original source normalization and all errors once; preserve C_S_32000 and thresholds; finite refinement is a candidate experiment, not a guaranteed infinite-tail closure

The ultimate beyond-support residual still needs an actual certificate. This finite correction may expose a need to improve the infinite seed itself; no assumption that repeated finite extensions close it is made.
