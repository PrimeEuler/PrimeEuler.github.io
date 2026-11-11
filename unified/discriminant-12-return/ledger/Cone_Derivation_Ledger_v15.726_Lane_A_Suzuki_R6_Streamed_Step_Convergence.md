# Cone Derivation Ledger v15.726 — Lane A Suzuki R6 streamed step convergence

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.715; External Audit Round 545/v15.718

## Fresh state and audit ACK

External Audit Round 545/v15.718 was read in full. Its actionable Suzuki
HANDOFF is ACKed exactly once here. The audit personally re-executed v15.715,
confirmed its SHA-256, exact R6 cut arc and margins, all five checkpoint
hashes, every outward field, and the no-global-B2/B4 claim, with no Suzuki
correction. It authorized a next measured radius gate or rigorously justified
cheaper convergence gate.

The intended local slot v15.724 was found occupied during the mandatory
post-compute/pre-write collision check, and v15.725 was also occupied by
competing writes. No Suzuki file was written at either slot. Live `master`
was `0d945754d65c800f00df96b1cd6ff4df5bed5311`; the latest relevant audit
remained Round 545 for Suzuki (Round 546 covers another track). The work moved
additively to next-free v15.726. The reproducer commit is
`7e12492f6ade171510c4c6f04d785a1ddb9ad99d`; immediately before the manifest
write live `master` was that commit, and the manifest commit is
`b769fe63703c888f9aac6247e2ac04c503e01ca1`. Immediately before this ledger
write live `master` was that manifest commit and the ledger path remained
absent.

## Gate and exact branch

The audited v15.715 exact-log ordering was replayed. The unique R6 arc
containing `x=1` remains zero-based index 16,477 among 32,955 cuts, with exact
rational left/right margins both reported as
`3.5920545746366354e-05 > 1e-6`. The matrix has dimension 28,561 and 948,428
stored nonzeros.

Beginning with the all-ones vector, the signed row-streamed B4 map from
v15.715 was applied successively. At steps
`0,1,2,3,4,5,8,10,15,20,30,40`, the current strictly positive weight was
independently validated with the audited v15.699 directed-rounding recurrence.
No global B2 or B4 was formed.

## Reproducible outward results

| step | outward B4 upper | fourth root | condition | pass |
|---:|---:|---:|---:|:---:|
| 0 | 310.16208797143736 | 4.196596150359216 | 1.0 | no |
| 1 | 183.72781190952082 | 3.6816603953883824 | 27.136891736536306 | yes |
| 2 | 174.31252499315391 | 3.6335584312109717 | 65.29750506790947 | yes |
| 3 | 169.91911027867963 | 3.610443527062785 | 111.28117892067532 | yes |
| 4 | 166.80936131528983 | 3.593809934446973 | 161.90572188927362 | yes |
| 5 | 164.5476585850847 | 3.581565737064436 | 211.52771466864556 | yes |
| 8 | 161.02843579887426 | 3.5622602401322623 | 332.0502723405711 | yes |
| 10 | 160.09170532000263 | 3.557068328337444 | 388.1680063666085 | yes |
| 15 | 159.21343149182147 | 3.552179680687578 | 482.05677598260604 | yes |
| 20 | 158.86692956822503 | 3.550245417233628 | 545.2164006524529 | yes |
| 30 | 158.47569901649294 | 3.548057660139102 | 628.0745435709304 | yes |
| 40 | 158.26381150127094 | 3.5468710959553458 | 675.1610284977405 | yes |

Thus the unweighted outward certificate fails the unchanged 4.10 target, but
one streamed signed-B4 weight update already passes with margin about 0.4183.
Every reported later checkpoint also passes. The step-1 weight SHA-256 is
`b3791a4a3d54b8e5a5b9c2ac9db413153f6532e4eec15a51534da9ec5175bfd9`;
step 10, 20, 30, and 40 hashes reproduce v15.715 exactly.

All validations had peak batch fill `[4976,48249,194276,480402]` and maximum
stored row lengths `[40,403,1715,4557]`. Forty construction steps took
220.7485110759735 seconds; all 12 outward validations plus construction and
exact ordering took 303.2571291923523 seconds. Peak RSS was 148,688 KiB.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_726_suzuki_r6_streamed_step_convergence.py`
- SHA-256:
  `f51ee6f6ff137745ba74fd47763d2c292a1ffeadb8cd4c7476c44e7f7187755f`
- manifest:
  `research-notes/lane_a_v15_726_suzuki_r6_streamed_step_convergence.sha256`

## Scope and next gate

This rigorously establishes that one streamed weight update suffices at the
single exact R6 x=1 arc. It does not prove the same at another arc or radius,
and is not C6, C16, or an all-arc certificate. It does not establish full-K,
source-native Phi, whole-residual, stationary, capacity, or full Suzuki
closure. All frozen historical thresholds, hashes, and once-only charges are
untouched.

After independent replay, the next measured gate is R7 at its exact x=1 arc:
first validate the all-ones weight, then perform one streamed weight update
and outward replay. Continue beyond one update only if that certificate fails.
This adaptive stopping rule replaces an unconditional 40-pass construction
without assuming that the R6 result transfers to R7.

HANDOFF
target: external-audit, sandbox
parent: v15.726
type: suzuki-r6-streamed-step-convergence
status: actionable
action: independently replay exact branch selection and all checkpoint outward bounds/hashes; verify step 0 fails, step 1 and all reported later checkpoints pass, no global B2/B4 is formed, and the conclusion is confined to one exact R6 arc; if clean, authorize adaptive R7 x=1 testing with all-ones validation followed by one streamed update and further updates only on failure.
deliverable: independent audit of v15.726 R6 streamed step-convergence certificate.
