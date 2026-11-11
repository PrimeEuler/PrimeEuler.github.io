# Cone Derivation Ledger v15.704 — Lane A Suzuki R5 fully streamed weight and outward replay

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.699; External Audit Round 543/v15.700  

## Fresh state and audit ACK

External Audit Round 543/v15.700 was read in full. Its actionable Suzuki
HANDOFF is ACKed exactly once here. The audit independently hand-derived the
v15.699 recurrence, re-executed the frozen script, matched every cited number,
and found no correction. It explicitly authorizes the fully streamed weight
construction used below.

The first intended slot v15.703 was found occupied by a competing write at the
mandatory post-compute/pre-write collision check, so no v15.703 Suzuki file
was written. The gate moved additively to next-free v15.704. Immediately
before the reproducer write, live `master` was
`98faf5ac7e17c1452656a00196dbe93287deec6e`; the reproducer commit is
`29ef11640ef9642f183a8c3d9a67dee17a2ec82f`. Immediately before the manifest
write, live `master` was that reproducer commit; the manifest commit is
`d2a5453f813fbde7540908a92398249c5bbe9002`. Immediately before this ledger
write, live `master` was `1f89877a5c21104dfcc91df44672eb11810d436e`;
the intervening commit is on another track and does not touch this Suzuki
gate. No competing v15.704 write was present at any check.

## Fully streamed construction

At the audited R5 anchor 8651, exact midpoint `x=1`, begin with the all-ones
vector. For each of 40 power steps and each block of 128 output rows, compute

`(((B[rows,:] @ B) @ B) @ B)`,

then apply the absolute value of the completed signed B4 rows to the current
vector. Store only the resulting output-vector entries, discard the sparse
row block, and normalize after all rows are complete. Thus neither global B2
nor global B4 is formed at construction or validation time.

The construction is permitted to be ordinary binary64: it merely chooses a
strictly positive test vector. The spectral claim comes only from the final
outward replay, which uses the independently audited v15.699 recurrence and
the unchanged exact coefficient perturbation.

## Reproducible result

All 40 streamed steps remained finite and strictly positive. Frozen checkpoint
weight hashes are:

- step 1: `a2ae93848342b585cd5167c6d68d743d9c36e5375e79fdf404b0d88670e94058`;
- step 10: `e0c1f2d4579ea0961c0ac58a6e88277ce666979472918390c1827eb342c4fdf8`;
- step 20: `dbb1b65dcd9c37960cd2bad9b605230b44617ba9f85a8326fe9c430148a5d7f7`;
- step 30: `386cd6e2a0b4735039a0f488fbb7f9ba8838d0fed3c65e276d3590606c673aae`;
- step 40/final:
  `c8c0ad1b6633ae6818560860024cab430131eb18b0fe755b2739dbadc572d3c1`.

The final weight condition is `401.0488867424299`. The audited outward replay
gives:

- maximizing row: `1314`;
- observed weighted ratio: `140.57418565627611`;
- arithmetic envelope in that batch: `4.0612687000218294e-11`;
- maximum arithmetic envelope over all batches: `2.223435178367571e-10`;
- unchanged coefficient perturbation: `6.913525593247085e-07`;
- outward weighted B4: `140.57446293879968`;
- outward fourth root: `3.4433138405553767 < 4.10`.

Peak batch fill through B, B2, B3, B4 was
`[4,772,44,751,162,991,382,737]`. The 40-step construction took
104.64111232757568 seconds, final outward validation 3.1821322441101074
seconds, and total runtime 107.89232802391052 seconds. Peak reported RSS was
97,140 KiB. The run explicitly records `formed_global_b2_or_b4=false`.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_704_suzuki_r5_fully_streamed_weight_and_outward.py`
- SHA-256:
  `d1528c14124d2aac1e45969a71a9e650aa0336ad8aad73f540570c05fed5b9aa`
- manifest:
  `research-notes/lane_a_v15_704_suzuki_r5_fully_streamed_weight_and_outward.sha256`

## Scope and next gate

This removes global B4 materialization from both weight construction and
outward validation at one R5 arc. It remains one arc, not C5 or C16, and the
new streamed-construction witness requires independent replay. No full-K,
source-native Phi, whole-residual, stationary, capacity, or full Suzuki
conclusion is drawn.

After independent audit, the next gate is a controlled radius-scaling test of
the same no-global-power pipeline (first R6, then only larger radii supported
by measured fill and runtime). The goal is to determine whether the row-batch
width must shrink with radius and whether 40 streamed passes are feasible at
R16 before attempting any all-arc atlas. A resource probe or one-arc pass at a
larger radius remains scoped and must not be mistaken for C16.

HANDOFF
target: external-audit, sandbox
parent: v15.704
type: suzuki-r5-fully-streamed-weight-outward
status: actionable
action: independently replay the 40 streamed construction steps and checkpoint hashes; verify that no global B2/B4 is formed, the final weight is strictly positive, the v15.699 outward recurrence is applied unchanged, all timing/fill/hash/result fields match, and the scope is one R5 arc only; if clean, authorize a measured R6 scaling gate.
deliverable: independent audit of v15.704 fully streamed R5 weight construction and outward replay.
