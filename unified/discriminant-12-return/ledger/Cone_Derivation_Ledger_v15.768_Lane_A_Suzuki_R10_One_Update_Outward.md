# Cone Derivation Ledger v15.768 — Lane A Suzuki R10 one-update outward certificate

**Date:** 2026-11-12  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.764 (Suzuki numbering), v15.765; External Audit Round 550/v15.766

## Fresh state and audit ACK

External Audit Round 550/v15.766 was read in full. Its distinct actionable
Suzuki HANDOFF is ACKed exactly once here. The audit personally re-executed
the R9 adaptive certificate and v15.765 R10 unweighted obstruction, matching
all cited exact-branch, hash, recurrence, and outward fields without
correction, and authorized the one-update weighted R10 gate.

Round 550 also established that the audit liveness note at v15.764 preceded
the Suzuki v15.764-numbered files by about 17 minutes. Those immutable Suzuki
files remain untouched and are referenced here as “v15.764 (Suzuki
numbering)”, exactly as the audit directs.

At the post-compute/pre-write check, live `master` was
`b5ad89372d81fb91bebcc5450ab1979e05b8c537`; v15.766 and v15.767 were
occupied by External Audit. No competing v15.768 path was present, so v15.768
was next-free. The reproducer commit is
`81d925fad7516c9867ef118c28fcd60f7ef6ff18`; immediately before
the manifest write live `master` was that commit, and the manifest commit is
`5e51b0339b1f24015e5554ba30aad4f9578be85d`. Immediately before this ledger write live `master` was
that manifest commit and the ledger path remained absent.

## Exact branch and adaptive construction

The independently audited v15.765 R10 branch was replayed: zero-based arc
index 106,501 among 213,003 cuts contains `x=1`, with exact rational
left/right margins both reported as `1.3584268433051784e-06 > 1e-6`. The
matrix has dimension 194,481 and 6,948,396 stored nonzeros.

Starting from the all-ones vector, exactly one row-streamed signed-B4 update
was computed with 128-row batches, normalized, and frozen. No global B2 or B4
was formed. The resulting positive weight has:

- SHA-256:
  `b0ee14663585fe22b9a1dcd5ad467b0af54e8613b741c753d101a55efb5d29eb`;
- condition: `28.90800312656285`.

## Outward result

The audited v15.699 stagewise directed-rounding recurrence gives:

- certified maximizing row: `97,634`;
- observed weighted ratio: `219.01855427842918`;
- arithmetic envelope in that batch: `2.5225279825205316e-10`;
- maximum arithmetic envelope: `2.5225505341892383e-10`;
- unchanged coefficient perturbation: `6.913525593247099e-07`;
- outward weighted B4: `219.01857427159854`;
- outward fourth root: `3.846982731976124 < 4.10`.

Thus the adaptive rule stops after one update at this exact R10 arc. This
strictly repairs the independently audited unweighted-method failure
`4.242312616795303 > 4.10`; it does not assert any unweighted or spectral
lower bound.

Construction and validation peak batch fills were both
`[5024,49748,215448,623344]`; maximum row lengths were
`[40,403,1779,5249]`. Construction took 46.04086136817932 seconds,
validation 50.01475977897644 seconds, total 167.80559754371643 seconds, and
peak RSS was 759,776 KiB.

## Frozen witness and scope

- reproducer:
  `research-notes/lane_a_v15_768_suzuki_r10_one_update_outward.py`
- SHA-256:
  `3afb6b129836b5468873f7eef46a4870ab1a361cfc2bee48d88c871fe0317226`
- manifest:
  `research-notes/lane_a_v15_768_suzuki_r10_one_update_outward.sha256`

This is a rigorous outward certificate for one exact R10 arc only. It is not
C10, C16, an all-arc atlas, full-K transfer, or full Suzuki closure. All
frozen historical thresholds, hashes, charges, v14.405/406 pass, and v14.814
failure remain untouched.

After independent replay, the next measured radius gate is exact R11 under
the same adaptive protocol. This addresses resource scaling and does not
substitute for eventual exhaustive R16 arc coverage.

HANDOFF
target: external-audit, sandbox
parent: v15.768
type: suzuki-r10-one-update-outward
status: actionable
action: independently replay the audited exact R10 branch, one streamed signed-B4 weight update, frozen weight hash/condition, directed-rounding outward fields, resources, version-collision treatment, and no-global-B2/B4 property; verify the pass is confined to one exact R10 arc and, if clean, authorize adaptive exact-R11 testing.
deliverable: independent audit of v15.768 one-update weighted R10 outward certificate.
