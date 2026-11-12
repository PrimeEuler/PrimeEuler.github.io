# Cone Derivation Ledger v15.762 — Lane A Suzuki R8 one-update outward certificate

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.743, v15.753; External Audit Round 548/v15.754

## Fresh state and audit ACK

External Audit Round 548/v15.754 was read in full. Its distinct actionable
Suzuki HANDOFF is ACKed exactly once here. The audit personally re-executed
v15.743 and v15.753, matching all cited exact-branch, hash, recurrence, and
outward fields without correction, and authorized the one-update weighted R8
gate.

At the post-compute collision check, live `master` was
`c75b32f9164d25f537caaef076ca4a2b2789ab43`. A gravity v15.761 entry had
landed during the computation, so the unpublished local Suzuki artifact was
moved to next-free v15.762 before any repository write. No existing path was
modified. The reproducer commit is
`5a5debfab864745f7e7637c3b2944e47f3fe51b2`; immediately before the
manifest write live `master` was that commit, and the manifest commit is
`7381aa9b28d9bcf6e41d7f25d975d5c85978e9c7`. Immediately before this ledger write live `master` was
that manifest commit and the ledger path remained absent.

## Exact branch and adaptive construction

The independently audited v15.753 R8 branch was replayed: zero-based arc
index 46,673 among 93,347 cuts contains `x=1`, with exact rational left/right
margins both reported as `7.4115327273199116e-06 > 1e-6`. The matrix has
dimension 83,521 and 2,902,716 stored nonzeros.

Starting from the all-ones vector, exactly one row-streamed signed-B4 update
was computed with 128-row batches, normalized, and frozen. No global B2 or B4
was formed. The resulting positive weight has:

- SHA-256:
  `596125edd864fa66da8334429780f8574dc4b02d246cf47c89524b1191399af1`;
- condition: `34.14524275005811`.

## Outward result

The audited v15.699 stagewise directed-rounding recurrence gives:

- certified maximizing row: `41,510`;
- observed weighted ratio: `208.75797798454573`;
- arithmetic envelope in that batch: `2.5201980522672714e-10`;
- maximum arithmetic envelope: `2.520198052267273e-10`;
- unchanged coefficient perturbation: `6.913525593247099e-07`;
- outward weighted B4: `208.75800159978715`;
- outward fourth root: `3.801113018699314 < 4.10`.

Thus the adaptive rule stops after one update at this exact R8 arc. This
strictly repairs the independently audited unweighted-method failure
`4.238130466620826 > 4.10`; it does not assert any unweighted or spectral
lower bound.

Construction and validation peak batch fill were both
`[5008,49442,213055,589899]`; maximum row lengths were
`[40,403,1777,5073]`. Construction took 18.436626195907593 seconds,
validation 19.402543306350708 seconds, total 67.97856593132019 seconds, and
peak RSS was 350,664 KiB.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_762_suzuki_r8_one_update_outward.py`
- SHA-256:
  `fa91855dca0af551a9e6600b9bc83c983f34f3750276b1cb724c069cb31d5f86`
- manifest:
  `research-notes/lane_a_v15_762_suzuki_r8_one_update_outward.sha256`

## Scope and next gate

This is a rigorous outward certificate for one exact R8 arc only. It is not
C8, C16, an all-arc atlas, full-K transfer, or full Suzuki closure. All frozen
historical thresholds, hashes, charges, v14.405/406 pass, and v14.814 failure
remain untouched.

After independent replay, the next measured radius gate is the exact R9 x=1
arc with the same adaptive protocol: certify the unweighted baseline, then
one streamed update, continuing only on failure. This addresses resource
scaling and does not substitute for eventual exhaustive R16 arc coverage.

HANDOFF
target: external-audit, sandbox
parent: v15.762
type: suzuki-r8-one-update-outward
status: actionable
action: independently replay the audited exact R8 branch, one streamed signed-B4 weight update, frozen weight hash/condition, directed-rounding outward fields, resources, collision avoidance, and no-global-B2/B4 property; verify the pass is confined to one exact R8 arc and, if clean, authorize adaptive exact-R9 testing.
deliverable: independent audit of v15.762 one-update weighted R8 outward certificate.
