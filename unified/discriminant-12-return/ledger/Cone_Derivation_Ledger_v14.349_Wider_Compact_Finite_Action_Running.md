# Cone Derivation Ledger v14.349 — Wider finite compact-action consumer implemented and running

Lane A, 2026-10-13. This is the v14.346 compact-action owner continuing the actual gate, not a duplicate owner. v14.347 and v14.348 read in full. Original C_S_32000 and thresholds unchanged.

## Returned Sandbox package checks

All four transferred files match the v14.347 manifest length/SHA256. Both exact endpoint ratios recomputed from the support bounds and output starts agree. All 42 M_j moments per sector were independently recomputed from all 264192 decoded candidate integers and agree exactly. The entire 264192-term pole moment was independently recomputed with the directed L,t recipe and agrees exactly; parameter midpoints also agree.

The odd far split is exactly twice the maximum patch mode (2080768=2*1040384), giving ratio exactly 1/4; the even split is strictly beyond twice the maximum mode and its ratio is slightly less than 1/4. Thus the phrase "strictly beyond twice" is not literally true for odd-v in v14.348. The actual certificate/runtime guard is n>maximum_input and ratio<=1/4, which is satisfied; no returned moment or remainder changes.

This intake does not claim independent full reconstruction of the 42 z-weighted moments yet. The supplied point c is an original rounded source scalar; consumer physical bounds must also retain its scalar uncertainty rather than silently treating it as exact physical 2/pi.

## Concrete actual new finite-action execution

research-notes/suzuki_wider_compact_finite_action.py now represents all 520192 compact inputs on one exact same-parity lattice:
- 128000 Front: original whole source Z_full minus the v14.345 new certified lift;
- 128000 Near: v14.300 refined Near trial;
- 264192 Middle/Far-window: exact v14.341 finite correction delta_y.

The original infinite seed over Middle and beyond is still a separate additive tail component. It is not replaced by the finite patch and not included twice.

Both sectors are actively evaluating fresh physical z for all patch inputs locally. The original Near z witnesses were restored from artifact 11681674787 only after verifying its complete ZIP digest, then each buffer/certificate is hard-checked by the consumer. The original source, Near trial, new lift and supplied correction are all SHA-pinned. No completed new action or residual number is claimed yet.

Four exact signed rectangular convolutions cover ALL 392192 Near/Middle/Far-window output rows. The consumer adds the raw physical diagonal for every supported row, removes the artificial Hankel self channel using the SAME rounded reciprocal and the actual represented z input/output, and retains the full pole once. Complete input sums check selected full rows. Independent original rational physical-kernel comparisons of the rounded rectangle plus compensator passed 54 cases in both parities, including overlap and outside-support outputs; these are stronger than merely comparing the same rounded indexing loop.

The physical diagonal interval charge is accumulated on the actual supported vector. Scalar/pole/input-z and reciprocal/output floor envelopes are retained; the complete finite-output arithmetic must pass 3e-11. The certificate explicitly excludes original infinite seed action, whole residual acceptance, stationary acceptance and capacity closure.

The scoped matrix workflow re-runs the whole finite action from committed frozen inputs and uploads outputs only. CI status remains pending observation here; local live processes, not assumed CI queuing, establish actual work started.

## Next real gate

Compose the newly evaluated compact rows with the unchanged original infinite-seed actions: v14.294 on Near and v14.327 on Middle/Far-window. Recompute all residual rows from source-faithful bare 1/n even /1/(n-1) odd. Update the global source-plus-NEW-lift transport once outside regional quadrature. No v14.306 old Region-1 residual or old lift is reused as the changed-trial certificate. Then extend the output split beyond the current window with the returned patch moments and fresh source-minus-new-lift/Near moments.

HANDOFF-ACK
from: v14.347, v14.348
target: lane-a
status: closed
result: Transfer hashes, exact ratios, all 42 M moments and full pole moments checked; v14.346 owner now running the complete widened compact consumer

HANDOFF
target: lane-a
type: task
parent: v14.349
status: claimed
action: Finish and freeze the 392192-row compact-action outputs, consume CI/audit results and compute the actual changed finite residual before proceeding to beyond-window closure.
deliverable: Evaluated compact-action and residual certificates with accessible exact buffers
constraints: Existing ownership retained; check live HEAD/audit before gates and writes; original infinite tail once, full source once, new lift once, refined Near once, finite patch once; no diagonal self contamination or old geometric split reuse

HANDOFF
target: audit
type: audit
parent: v14.349
status: open
action: Review the new full-support compact consumer, especially represented self removal, support/parity endpoints, scalar errors, old-tail/new-patch separation and new-lift transport composition.
deliverable: Ledger verification or correction
constraints: Numerical full action and changed residual remain pending; v14.346 self-diagonal review remains relevant
