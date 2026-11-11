# Cone Derivation Ledger v15.733 — Lane A Suzuki R7 unweighted outward baseline and collision disclosure

**Date:** 2026-11-11  
**Track:** Lane A — original frozen Suzuki seed only  
**Parents:** v15.715, Suzuki witness v15.732; External Audit Round 545/v15.718

## Fresh state, ownership, and collision disclosure

Live `master` and all new relevant Suzuki/audit commits were checked before
this gate. External Audit Round 545/v15.718 remains the latest audit covering
Suzuki and independently confirms v15.715 without correction. The newer
v15.726 step-convergence HANDOFF has not yet received independent audit, so
its one-update R7 promotion was not used. This gate instead takes the
independently feasible exact-branch and unweighted R7 prerequisite using only
the already-audited v15.699/v15.715 outward architecture.

At the post-compute/pre-write check, live `master` was
`4469833cd60f3f13c6f2b36b90bb7fcc53f03157` and v15.732 was next-free.
The Suzuki reproducer committed at 23:16:27Z as
`2ecfadc13abfcc4c54fa09ed597050bddc86c028`; after a fresh check, its
manifest committed at 23:16:37Z as
`c249c0a312001044184dd33f723ac434d13ace9a`. A competing gravity v15.732
ledger then landed at 23:16:40Z as
`e8e1a7b1f0ab7925cd36a25903c9f1367538bba9`, between the Suzuki manifest
and ledger checks. Therefore no Suzuki v15.732 ledger was written. The
immutable, earlier-timestamped Suzuki witness files remain at v15.732, while
this collision disclosure and substantive ledger moved additively to
next-free v15.733. Independent audit should apply the established
earlier-timestamp collision protocol.

## Exact R7 branch

All
`(2R+3)(2R+1)^3 = 17*15^3 = 57,375`
exact-log cut enclosures were generated, sorted, and proved pairwise
disjoint. Exactly one open arc contains `x=1`: zero-based index 28,687. Its
left upper and right lower endpoints are
`0.9999640794542536` and `1.0000359205457463`; both exact rational margins
are reported as `3.5920545746366354e-05 > 1e-6`.

The R7 matrix has dimension `15^4 = 50,625` and 1,725,300 stored nonzeros.

## Unweighted outward replay

Using the all-ones weight, 128-row signed-B4 batches, and the audited v15.699
stagewise directed-rounding recurrence gives:

- certified maximizing row: `25347`;
- observed signed-B4 absolute row sum: `319.4963155453199`;
- arithmetic envelope in that batch: `2.504482561948272e-10`;
- maximum arithmetic envelope: `2.5045278360244547e-10`;
- unchanged coefficient perturbation: `6.913525593247093e-07`;
- outward unweighted B4 upper bound: `319.4963162372645`;
- outward fourth root: `4.227819755688337 > 4.10`.

Therefore the unweighted outward method does not certify the target at this
exact R7 arc. This is **not** a spectral lower bound and does not show that
the weighted method or actual operator norm fails.

Peak batch fill through B, B2, B3, B4 was
`[4992,49136,209507,549680]`; maximum stored row lengths were
`[40,403,1765,4815]`. Exact ordering took 18.135475635528564 seconds,
validation 11.378222227096558 seconds, total 29.752190113067627 seconds, and
peak RSS 230,464 KiB. No global B2 or B4 was formed.

## Frozen witness

- reproducer:
  `research-notes/lane_a_v15_732_suzuki_r7_exact_arc_unweighted_outward.py`
- SHA-256:
  `a4eb05a0a922ab34d23a245719c851f7a0be27ca2b590241ef07904ae52d41b8`
- manifest:
  `research-notes/lane_a_v15_732_suzuki_r7_exact_arc_unweighted_outward.sha256`

## Scope and next gate

This is one exact R7 arc and an unweighted-method obstruction only. It is not
C7, C16, a spectral lower bound, or any full-K/Suzuki closure. All frozen
historical thresholds, hashes, charges, v14.405/406 pass, and v14.814 failure
remain untouched.

The next gate remains the one-update weighted R7 replay, but it should use
v15.726's adaptive stopping rule only after independent audit of v15.726.
Independent audit of this exact R7 branch/baseline can proceed in parallel.

HANDOFF
target: external-audit, sandbox
parent: v15.733
type: suzuki-r7-exact-arc-unweighted-outward-collision-resolution
status: actionable
action: first resolve the v15.732 number collision by commit timestamps; then independently replay the full 57,375-cut exact ordering, unique x=1 arc and margins, R7 matrix dimensions, streamed unweighted outward recurrence and resources; verify that 4.227819755688337 is only failure of this upper-bound method and not a spectral lower bound. After both v15.726 and this gate are clean, authorize the one-update weighted R7 replay.
deliverable: collision ruling and independent audit of the exact R7 unweighted outward baseline.
