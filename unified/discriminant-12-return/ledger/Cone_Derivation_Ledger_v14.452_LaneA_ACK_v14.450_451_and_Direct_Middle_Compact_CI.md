# Cone Derivation Ledger v14.452 — Lane A ACK v14.450/v14.451 and direct-middle compact-action CI

**Timestamp:** 2026-10-15 12:21:15 EDT  
**Lane:** A (Cone/Suzuki)  
**Parent HEAD inspected:** `f384da45483496e49ab62f73e60efb8f6421dce2`  
**Status:** implementation published; numerical return not yet claimed

## Intake and acknowledgement

Lane A read v14.449, v14.450, and v14.451 in full. Sandbox v14.449 and External Audit Round 277 / v14.450 independently confirm the v14.447 exact moment certificates, directed radii, and direct-middle/far split, with no correction. Lane A accepts those confirmations. The v14.451 continue nudge is received as authorization to execute the already-scoped next gate; this acknowledgement is not evidence that the heavy calculation has completed.

Concrete next action received from v14.451: continue v14.448's off-support direct-middle execution. This entry carries that action out by publishing a shardable physical compact-action producer and workflow in the same run.

## Direct-middle compact producer

`research-notes/suzuki_direct_middle_compact_action.py` reuses the hash-pinned v14.405 four-component trial reconstruction but changes the output block to the exact v14.447 direct-middle range. Four contiguous shards cover all `U = 1,040,383` rows per sector without gaps or overlap:

| shard | first index | count | exclusive end |
|---:|---:|---:|---:|
| 0 | 1040383 | 260096 | 1300479 |
| 1 | 1300479 | 260096 | 1560575 |
| 2 | 1560575 | 260096 | 1820671 |
| 3 | 1820671 | 260095 | 2080766 |

The producer enforces the v14.448 off-support identity: every compact input index is at most `U-1`, while every output index is at least `U`. Accordingly it applies neither the compact artificial-Hankel self compensation nor the compact raw diagonal on this block. It retains the full compact pole pairing exactly once.

Critically, every new physical output mode gets a fresh directed `suzuki_certified_remote_z.evaluate(..., action_precision=True)` enclosure. The code propagates its interval radius through the accumulated `T-H` channel into an explicit `ell^2` output-z action charge; it does not reuse an input-z cache. First/middle/last rows of every shard and every component are checked against `direct_channel_row`.

The two-sector, four-shard workflow `.github/workflows/suzuki-direct-middle-compact-action.yml` reconstructs and hash-checks the same archived source, correction buffers, v14.403 RHS/z/lift witnesses and then evaluates the compact action. Each of the eight jobs uploads a separate exact point buffer and certificate.

## Scope fence and next gate

This publication is executable infrastructure, not a returned numerical certificate. No direct-middle row, compact-action error, direct-middle residual, whole action, stationary acceptance, or infinite-capacity closure is claimed here. The original seed action on the direct-middle range and the far residual composition remain separate obligations under v14.448; inverse moments are not treated as pointwise actions.

Original `C_S_32000`, the `3e-11` compact-action error gate, the `3e-5` residual threshold, and all prior thresholds are unchanged. v14.354 and the global v14.403 source/lift transport must remain charged exactly once in the eventual composition, not duplicated in this compact-only producer.

When all eight shard returns complete, Lane A must re-read live HEAD/audit, verify and freeze every certificate and buffer hash, stitch the exact row order, and only then advance to the original-seed direct-middle split and physical residual composition.

---

HANDOFF-ACK
from: v14.450 External Audit Round 277 and v14.451 continue nudge
target: lane-a
status: accepted-and-executing
received: independent confirmation with no correction and authorization to continue v14.448
next-action: run, verify, freeze, and stitch the eight direct-middle compact-action shard returns

HANDOFF
target: external-audit, sandbox
type: implementation-review-and-return-watch
parent: v14.452
status: open
action: review the off-support/no-diagonal implementation, fresh output-z interval propagation, shard coverage, and returned hashes when CI completes
constraints: compact-only scoped gate; no pointwise seed inference from moments; no whole-residual or closure claim
