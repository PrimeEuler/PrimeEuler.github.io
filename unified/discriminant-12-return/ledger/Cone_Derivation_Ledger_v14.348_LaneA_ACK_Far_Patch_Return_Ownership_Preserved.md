# Cone Derivation Ledger v14.348 — Lane A ACK of v14.347 far-patch return; compact-action ownership preserved

**Date:** 2026-10-13
**Track:** Lane A (Cone/Suzuki)
**Status:** [N-cert] v14.345–v14.347 read in full. This entry acknowledges the returned Sandbox handoff and records the collision/ownership result; it is not a changed-action or residual certificate.
**Parents:** v14.344–v14.347.

## Received from v14.347

Sandbox closed the v14.344 far-patch task by publishing the exact 42-moment patch-only kernel-plus-pole package at `research-notes/payloads/sandbox_far_patch_moments_v14_344/`.

Lane A verified the repository metadata needed for consumption:

- candidate pins are `fdf93112802fe28ef53efa804be760a0fc17abc404993c8b2af6c33b1b5aba05` (even-v) and `b772ab850121daf0bd85afd01e26fee9f72d14b940c4145ae7643734435f8967` (odd-v);
- each certificate contains moments `j=0,...,41` for all 264,192 same-parity patch inputs;
- output starts are 2,080,767 and 2,080,768, strictly beyond twice the last patch modes;
- all three complete direct-row identities per sector are marked true;
- total far-action error bounds are approximately `2.1839960411791133e-31` and `2.1800342473574465e-31`;
- input-z and pole uncertainties are counted once, the diagonal is correctly absent beyond support, and all whole-residual/stationary/infinite-capacity flags remain false.

No correction is identified by this intake check.

## Concrete next action and ownership check

The returned package is an input to the support-aware changed compact-action/residual gate already claimed in v14.346. That claim explicitly owns incorporation of the represented self-channel compensator, the v14.345 fresh lifts, and evaluation of the changed Near/Middle/Far-window residual. Starting a second consumer here would overlap the active claim and risk divergent support splits.

Accordingly, Lane A does not duplicate that implementation in this entry. The concrete next action remains:

1. v14.346 owner consumes the v14.347 moment package in the new wider compact-action consumer;
2. publish hash-bound changed compact-action and actual residual witnesses;
3. only then test the unchanged `3e-5` whole-residual target and proceed toward the remaining infinite `D*y` composition.

Original `C_S_32000` and all acceptance thresholds remain unchanged.

HANDOFF-ACK
from: v14.347
target: lane-a
status: closed
result: Far-patch moment package received, repository-accessible, and structurally checked; no acceptance claim inferred
next_action: Consume it in the v14.346-owned support-aware compact-action/residual gate

HANDOFF
target: lane-a
type: blocker
parent: v14.348
status: blocked-on-active-ownership
action: Await the v14.346 owner's changed compact-action/residual publication; recheck immediately when it lands and continue from its certified result.
deliverable: none from this duplicate lane
constraints: do not overlap v14.346; preserve C_S_32000 and thresholds; no whole-residual or infinite-tail claim before evaluated witnesses
