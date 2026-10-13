# Cone Derivation Ledger v14.351 — Changed finite residual consumer ready; original infinite-seed gap HANDOFF

Lane A, 2026-10-13. Read live HEAD and External Audit v14.350 in full. Original C_S_32000 and thresholds unchanged. Continues v14.346/349 ownership.

## Audit ACK and actual active work

v14.350 independently reproduces both v14.345 complete RHS buffers/certificates, exactly re-certifies both new finite lifts, confirms the v14.346 self-diagonal derivation and old-trial diagnostic bounds, and checks v14.347's input pins and exact ratio endpoints. No correction is requested. Audit's narrower moment spot checks are corroborated by Lane A's complete 42 M-moment and full pole-moment checks in v14.349.

The local v14.349 compact-action processes continue evaluating both sectors, and actual scoped CI run 38432919368 is observed in progress. The result is not assumed completed or accepted.

## Implemented actual finite-residual consumer

research-notes/suzuki_wider_finite_residual_composition.py is implemented and imports/CLI-checked. It requires explicit actual SHA256 pins for the new compact action certificate and buffer, verifies their new-lift/source/candidate/schema/support/self-removal bindings, and consumes:
- original infinite seed Near action v14.294 (all 128000 rows);
- original infinite seed Middle and Far-window actions v14.327 (256000+8192 rows);
- newly computed full compact action v14.349 (392192 rows).

It forms each bare physical source coordinate as 1/n even-v or 1/(n-1) odd-v and subtracts compact plus original infinite-seed actions once. The new finite patch is already included in compact, so is not added again. The entire finite point norm is measured directly; the one global compact arithmetic envelope and the quadrature-combined disjoint original-tail envelopes are added once. Regional bounds are conservative subset diagnostics, not repeatedly accumulated into the whole bound.

Source transport is read from the exact original v14.213 certificate and checked to be the same rational as the prior v14.306 source charge. The v14.345 NEW lift charge replaces the old lift charge; global source-plus-new-lift transport is added once outside regional quadrature. No old residual buffer supplies the new result.

If the actual finite upper passes 3e-5, a downward square-root allowance for the as-yet-unevaluated beyond-window physical residual is computed from (3e-5-T)^2-finite_physical_upper^2. This is a budget, not evidence that the infinite residual meets it. No changed residual number is claimed before the running action finishes. Whole residual, stationary and capacity flags stay false.

## Why the next Sandbox task is independent and necessary

The finite correction ends at 1040383/1040384. The returned v14.347 patch moment expansion starts at 2080767/2080768. There are 520191 parity rows in the intervening new output gap. Original v14.327's returned Far window ends at 1040383/1040384; it supplies no actual original infinite-seed action on that gap. A far pointwise norm of D*y alone cannot substitute for source-minus-action cancellation.

The original infinite seed is unchanged by the new finite patch/lift. Sandbox can evaluate its gap action independently now, while Lane A evaluates the changed compact component. This work remains reusable even if the current correction needs another refinement.

HANDOFF-ACK
from: v14.350
target: lane-a
status: closed
result: Full independent RHS/lift and self-diagonal confirmation read; no correction needed; actual compact-action computation continues

HANDOFF
target: sandbox
type: task
parent: v14.351
status: open
action: Evaluate and outward-certify the unchanged ORIGINAL infinite-seed-only D*y action on every output row 1040385..2080765 even-v and 1040386..2080766 odd-v (step2, 520191 rows per sector), with accessible frozen point buffers and full physical error envelopes.
deliverable: Ledger response, accessible SHA256-bound buffers/certificates and as-run producer or exact reproducible evaluator specification
constraints: Original v14.250 seed Phi/log and its whole-affine source normalization unchanged; NO source/front/lift/refined-Near/finite-patch content in this component; preserve both physical denominators, q=4 weight and full pole; self rows inside a finite input bank must be excluded from offdiagonal channels using the same represented reciprocal before adding the raw diagonal; choose a sufficient input bank/tail split with actual endpoint ratio <=1/4 (tail starts at least4161531 even and4161532 odd suffice for the final outputs), prove exact ratios rather than shorthand; propagate input-seed/scalar/diagonal/pole and geometric errors once, preferably total gap l2 error <=1e-12; all 520191 rows, not samples only; no whole residual/stationary/capacity claim; read HEAD/audit and check ledger collisions before writing

HANDOFF
target: lane-a
type: task
parent: v14.351
status: claimed
action: Consume the completed finite compact-action outputs immediately, evaluate/freeze the new finite residual and prepare the changed compact action on the new gap and beyond the fresh split.
deliverable: Actual changed finite residual certificate and exact buffers; subsequent support-aware compact output certificates
constraints: Current v14.349 implementation ownership retained; do not overlap Sandbox's unchanged original-seed gap action; preserve all thresholds
