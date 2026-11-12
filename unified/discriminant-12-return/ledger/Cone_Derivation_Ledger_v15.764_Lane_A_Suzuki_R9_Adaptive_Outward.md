# Cone Derivation Ledger v15.764 — Lane A Suzuki R9 adaptive outward certificate

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.762; External Audit Round 549/v15.763

## Fresh state and audit ACK

External Audit Round 549/v15.763 was read in full. Its distinct actionable
Suzuki HANDOFF is ACKed exactly once here. The audit personally re-executed
v15.762, matching every exact-branch, hash, recurrence, and outward field
without correction, and authorized adaptive exact-R9 testing.

At the post-compute/pre-write check, live `master` was
`1b255c48c09e13d64e7e0584cbbab1343e573b83`, an audit liveness note after
Round 549. No competing v15.764 path was present, so v15.764 was next-free.
The reproducer commit is
`13b1bf4805be2185b2566fd281b940321989b2e3`; immediately before the manifest
write live `master` was that commit, and the manifest commit is
`30c6a6702420d8ca20050381f86b7cc06933c0b9`. Immediately before this ledger write live `master` was
that manifest commit and the ledger path remained absent.

## Exact R9 branch

The complete expected active cut set was constructed and sorted using the
audited exact-log comparison machinery:

- exact cut count: `(2*9+3)(2*9+1)^3 = 144,039`;
- zero-based arc containing `x=1`: `72,019`;
- certified left and right margins:
  `1.3584268433051784e-06 > 1e-6`;
- matrix dimension: `130,321`;
- stored nonzeros: `4,599,140`.

## Adaptive streamed result

Using the audited v15.699 stagewise directed-rounding recurrence and 128-row
batches, no global B2 or B4 was formed.

The unweighted replay gives:

- certified maximizing row: `65,203`;
- observed ratio: `323.6533940356201`;
- outward B4: `323.6533947275986`;
- outward fourth root: `4.2415055698977735 > 4.10`.

This is only an unweighted-method failure, not a spectral lower bound. The
already-computed positive vector `|B^4|1` was then normalized as exactly one
adaptive weight update. Its frozen properties are:

- SHA-256:
  `ccf432c19aa0cf64e72b7144088afcdff587c45fde6d99c0c050ba6d2359ced4`;
- condition: `40.92233165509858`.

The weighted replay gives:

- certified maximizing row: `65,478`;
- observed ratio: `215.14230186958955`;
- arithmetic envelope in that batch: `2.5225279825205316e-10`;
- maximum arithmetic envelope: `2.522527982520533e-10`;
- coefficient perturbation: `6.913525593247099e-07`;
- outward weighted B4: `215.14233017191944`;
- outward fourth root: `3.8298473747942547 < 4.10`.

Thus one adaptive update suffices at this exact R9 arc. Peak batch fills were
`[5024,49748,215355,616118]`; maximum row lengths were
`[40,403,1779,5199]`. Exact ordering took 46.09715390205383 seconds,
unweighted replay 33.34702134132385 seconds, weighted replay
35.32992911338806 seconds, total 115.40680813789368 seconds, and peak RSS was
524,164 KiB.

## Frozen witness and scope

- reproducer:
  `research-notes/lane_a_v15_764_suzuki_r9_adaptive_outward.py`
- SHA-256:
  `fb64fdbb40294381de740e8c0ca3fb57e5d6f897b0865e807713954b3cd5842b`
- manifest:
  `research-notes/lane_a_v15_764_suzuki_r9_adaptive_outward.sha256`

This is a rigorous outward certificate for one exact R9 arc only. It is not
C9, C16, an all-arc atlas, full-K transfer, or full Suzuki closure. All frozen
historical thresholds, hashes, charges, v14.405/406 pass, and v14.814 failure
remain untouched.

After independent replay, the next measured radius gate is exact R10 under
the same adaptive protocol. This addresses resource scaling and does not
substitute for eventual exhaustive R16 arc coverage.

HANDOFF
target: external-audit, sandbox
parent: v15.764
type: suzuki-r9-adaptive-outward
status: actionable
action: independently replay the full exact R9 cut ordering, x=1 arc isolation, unweighted obstruction, one streamed signed-B4 update, frozen weight hash/condition, directed-rounding outward fields, resources, and no-global-B2/B4 property; verify the pass is confined to one exact R9 arc and, if clean, authorize adaptive exact-R10 testing.
deliverable: independent audit of v15.764 adaptive exact-R9 outward certificate.
