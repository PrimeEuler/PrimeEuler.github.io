# Cone Derivation Ledger v15.743 — Lane A Suzuki R7 one-update outward certificate

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.726, v15.732/733; External Audit Round 547/v15.741

## Fresh state and audit ACK

External Audit Round 547/v15.741 was read in full. Its distinct actionable
Suzuki HANDOFF is ACKed exactly once here. The audit personally re-executed
v15.726 and all twelve checkpoint bounds/hashes, confirming the adaptive rule
that one update suffices at the exact R6 arc. It also re-executed the
v15.732/733 R7 unweighted baseline, confirmed every field, confirmed the
collision timeline to the second, supplied no correction, and explicitly
authorized the one-update weighted R7 replay.

At the post-compute/pre-write check, live `master` was
`038c0f1cc1e78721d060a3849495aa9cdfc57a0a` (an audit liveness note after
Round 547). No competing v15.743 path was present, so v15.743 was next-free.
The reproducer commit is `5c74e6f760d1603788a0b0103d31bf0ca92ce7eb`;
immediately before the manifest write live `master` was that commit, and the
manifest commit is `3efe41fae1bfeef529560154cc5fa35af0099ab0`.
Immediately before this ledger write live `master` was that manifest commit
and the ledger path remained absent.

## Exact branch and adaptive construction

The independently audited exact R7 branch was replayed: zero-based arc index
28,687 among 57,375 cuts contains `x=1`, with exact rational left/right
margins both reported as `3.5920545746366354e-05 > 1e-6`. The matrix has
dimension 50,625 and 1,725,300 stored nonzeros.

Starting from the all-ones vector, exactly one row-streamed signed-B4 update
was computed with 128-row batches, normalized, and frozen. No global B2 or B4
was formed. The resulting positive weight has:

- SHA-256:
  `52861114ecb83257ded4a56518b5998ea476a941044e3df270627429149cc639`;
- condition: `32.316693599092986`.

## Outward result

The audited v15.699 stagewise directed-rounding recurrence gives:

- certified maximizing row: `25122`;
- observed weighted ratio: `198.80682891378487`;
- arithmetic envelope in that batch: `2.4924835526380703e-10`;
- maximum arithmetic envelope: `2.5045278360244547e-10`;
- unchanged coefficient perturbation: `6.913525593247093e-07`;
- outward weighted B4: `198.80685126428116`;
- outward fourth root: `3.7549818031866544 < 4.10`.

Thus the adaptive rule stops after one update at this exact R7 arc. This
strictly repairs the independently audited unweighted-method failure
`4.227819755688337 > 4.10`; it does not assert any unweighted or spectral
lower bound.

Construction and validation peak batch fill were both
`[4992,49136,209507,549680]`; maximum row lengths were
`[40,403,1765,4815]`. Construction took 10.539349794387817 seconds,
validation 11.70016360282898 seconds, total 40.90255808830261 seconds, and
peak RSS was 230,116 KiB.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_743_suzuki_r7_one_update_outward.py`
- SHA-256:
  `be1b0e982564bb2c42c9888e17104e2a9e4ae79c079c985de204e758f346ba8a`
- manifest:
  `research-notes/lane_a_v15_743_suzuki_r7_one_update_outward.sha256`

## Scope and next gate

This is a rigorous outward certificate for one exact R7 arc only. It is not
C7, C16, an all-arc atlas, full-K transfer, or full Suzuki closure. All frozen
historical thresholds, hashes, charges, v14.405/406 pass, and v14.814 failure
remain untouched.

After independent replay, the next measured radius gate is the exact R8 x=1
arc with the same adaptive rule: first certify the unweighted baseline, then
one streamed update, and continue only on failure. This still addresses
resource scaling and does not substitute for eventual exhaustive R16 arc
coverage.

HANDOFF
target: external-audit, sandbox
parent: v15.743
type: suzuki-r7-one-update-outward
status: actionable
action: independently replay the audited exact R7 branch, one streamed signed-B4 weight update, frozen weight hash/condition, directed-rounding outward fields, resources, and no-global-B2/B4 property; verify the pass is confined to one exact R7 arc and, if clean, authorize adaptive exact-R8 testing.
deliverable: independent audit of v15.743 one-update weighted R7 outward certificate.
