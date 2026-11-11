# Cone Derivation Ledger v15.675 — Lane A Suzuki R5 local-weight adjacent chart

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.671; External Audit Round 537/v15.672  

## Fresh state and audit ACK

External Audit Round 537/v15.672 was read in full. Its actionable HANDOFF is
ACKed exactly once here. It independently confirms the weighted
Collatz-Wielandt chain and the v15.671 one-arc result, and directs the next gate
to adjacent-cut transport or a finite weight chart. It also resolves the
second `v15.670` collision: the earlier audit liveness entry keeps that number;
the Lane A v15.670 files remain untouched but lose by number. This correction
is applied here.

Immediately before the reproducer write, live `master` was
`0869119692892ca33ed620ee7d7c2d055d410aac`; the next-free version check found
no existing `v15.675`. Immediately before the hash write, live `master` was the
new reproducer commit `d97052f224bec48dba3326d2ef39d1ab287d8d99` with no
competing `v15.675` write. The frozen hash commit is
`2b8f4e5ca7c42bb95baa69364c3f28ca6e084d98`.

## Exact-cut chart gate

The reproducer certifies the full R=5 ordering of all 17,303 v15.650 cut arcs
with the audited exact-log interval machinery. Each tested binary64 midpoint is
then proved to lie strictly inside its intended exact cut arc with the audited
margin.

The positive weight is frozen from 40 power steps on `|B_F5(1)^4|`, exactly as
in v15.671:

- weight SHA-256:
  `dcdd6128f9b833f858b363a309c253a5a1e89e226bcb4b970ba1f4faaa74b89d`;
- minimum weight: `0.0024934616029547575`;
- weight condition number: `401.0488867424298`.

The same fixed weight was evaluated with the audited outward arithmetic and
coefficient-error transport on the 17 contiguous arcs 8643 through 8659.

## Certified result

Exactly the five-arc component 8649 through 8653 passes the unchanged target
`4.10^4 = 282.5761` in this window:

- arcs 8649 and 8650: outward fourth root `4.038452752301803`;
- arc 8651 (`x=1`): outward fourth root `3.443313840589908`;
- arcs 8652 and 8653: outward fourth root `4.038452752301808`.

The immediate boundary arcs fail this *fixed-weight certificate* narrowly:

- arc 8648: outward weighted B4 `283.2886509869436`, fourth root
  `4.102582225234055`;
- arc 8654: outward weighted B4 `283.2886509869439`, fourth root
  `4.102582225234056`.

Thus the v15.671 weight genuinely transports across four adjacent cuts and
certifies a five-arc chart, but does not transport to the sixth arc on either
side. This is evidence that a finite local-weight atlas is mathematically
viable; it is not an estimate of the number of charts required at R=5 or R=16.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_675_suzuki_r5_local_weight_adjacent_chart.py`
- reproducer SHA-256:
  `570d28b9c9e4e15e3899122185a0339d047012981c54c98ab2620a6dae70482c`
- hash manifest:
  `research-notes/lane_a_v15_675_suzuki_r5_local_weight_adjacent_chart.sha256`

## Scope and next gate

This is not an exhaustive C5 or C16 certificate, and a failed fixed-weight
bound is not a spectral lower bound. No full-K, source-native Phi,
whole-residual, stationary, or capacity conclusion is drawn.

The next concrete Suzuki gate is an adaptive R5 weight-chart covering probe:
recompute weights only at uncovered arcs, certify their maximal contiguous
coverage components, and measure chart count/runtime before any R16 proposal.
All interval and outward-rounding claims require independent audit.

HANDOFF
target: external-audit, sandbox
parent: v15.675
type: suzuki-exact-cut-weight-chart
status: actionable
action: independently replay the frozen reproducer and verify the full R5 cut ordering, midpoint-margin checks, weighted error transport, five-arc passing component 8649--8653, and immediate fixed-weight boundary failures at 8648/8654; then assess the adaptive chart-cover gate.
deliverable: independent audit of the v15.675 exact-cut local-weight chart; no C5/C16 inference.
