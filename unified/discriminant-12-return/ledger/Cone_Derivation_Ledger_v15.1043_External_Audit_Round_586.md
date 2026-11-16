# Cone Derivation Ledger v15.1043 — External Audit Round 586

**Date:** 2026-11-16
**Track:** External Audit
**Parents:** Round 585/v15.999, liveness notes v15.1000-1041 (mine), Sandbox v15.1042

## Fresh state at gate

`git fetch origin master` immediately before this write returns `c5e772c` (Sandbox's v15.1042, final payload-manifest commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1043` confirmed free); none found for `v15.1042` either.

## v15.1042 — the signed-pair X-cone extension, verified personally

This is the first Sandbox-track entry audited in this stretch (the project's first new substantive content since Round 585, after an extended quiet period of liveness-only ticks). It answers Jeremy's question of whether a cone perpendicular to the existing T-cone exists in the signed-pair plane, by extending the master identity `T²−X²=uv` to its natural completion: opposite-sign pairs (`uv<0`) satisfy `X²=T²+r²` (an X-cone, perpendicular axis), meeting the original same-sign T-cone only at the null hinge `r=0, T²=X²` — correctly identified as the Rindler-wedge structure, and explicitly scoped as a geometric completion with no new dynamics or force-law selector.

Independently re-derived every claim from scratch (fresh SymPy, not the committed script):

- Confirmed the master identity `T²−X²=uv` exactly, and the X-cone mesh identities `X²−T²=r²` and `r²=n(X−T)` for the swapped-role pair `(n,−q)`.
- Confirmed the same-shell difference-pair product identity `−4m²\sinh²(Δψ/2) = −2m²(\cosh(Δψ)−1)` exactly (an elementary half-angle identity, confirmed symbolically).
- Confirmed the lattice-content claim by direct enumeration at all eight cited sample points (`N=1,2,6,12,36,60,97,120`): the integer-pair counts for `uv=+N` and `uv=−N` both equal `2d(N)` exactly in every case, matching the project's existing divisor-count toolkit.
- Independently verified both SHA-256 hashes in the payload manifest against the actual committed files (`X_Cone_Extension.md`, `x_cone.py`) — both match exactly.

**Re-executed the payload script.** Ran to completion with `PASS` (`ALL CHECKS PASS`), and every printed value (the eight signed-pair sector classifications, the hinge intersection, the X-cone mesh identities, and all eight divisor-count rows) matched my independent computation exactly.

## Honesty and scope assessment

This is a clean, modest geometric completion correctly and explicitly scoped: it adds no new dynamics, selects no force law, and is careful to identify the new structure with the existing Rindler-wedge/mirror-sector interpretation rather than claiming a new physical sector. The "lattice content" section correctly notes that the X-cone's divisor-count structure is "no new arithmetic function," just the same `d(N)` doubled by orientation. No mathematical corrections needed in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.1043
type: external-audit-round
status: actionable
action: v15.1042 independently confirmed correct in all its mathematics and payload hashes. No corrections needed. No open items from this round.
deliverable: Round 586 independent audit of v15.1042 (1 Sandbox entry, 1 script, 2 payload files); confirmed correct.
