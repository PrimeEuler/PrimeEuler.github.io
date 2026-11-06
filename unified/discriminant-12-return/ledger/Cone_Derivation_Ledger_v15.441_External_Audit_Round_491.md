# Cone Derivation Ledger v15.441 — External Audit Round 491: constant-Hankel tail barrier independently confirmed (lower bound rigorously re-derived; upper-bound citation checked for plausibility, not re-derived from scratch)

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.440 — proving the constant-Hankel tail term `‖Q Hplus Q‖` equals exactly `pi/2` for every tail depth `N`, hence cannot be shrunk by pushing `N0` out further, and that this already exceeds the remaining `0.00128` triangle allowance by three orders of magnitude — independently verified. The rigorous half (the essential-norm lower bound `>=pi/2`, via a from-scratch Hilbert–Schmidt compactness proof) is fully re-derived here and is, by itself, already sufficient for the stated "barrier" conclusion.
**Parents:** v15.438 (Round 490), v15.439, v15.440.

---

## Fresh pre-write check

`git fetch origin master` returns `35d2440` (v15.440), identical to the head just read. `v15.441` is next free; no collisions.

## What this entry claims and why it matters

After Round 490 confirmed the `9.740007 -> 4.105463` improvement, the new dominant obstruction was the constant-Hankel term, previously only bounded above by `1.570797` (`<=pi/2`). v15.440 asks the sharper question: is this term's *exact* operator norm on the tail actually small for large `N0`, or is `pi/2` not just an upper bound but the true, `N`-independent value? It argues the latter — reindexing the constant-Hankel tail as half of a generalized/shifted Hilbert matrix `G_N[j,k]=1/(j+k+N)`, and showing every such shifted matrix has norm exactly `pi` regardless of `N`, so `‖Q Hplus Q‖=pi/2` on *every* tail, not merely `<=pi/2` on this one.

## Independent re-derivation of the reindexing

For `n=N+2j`, `m=N+2k` (`j,k>=0`, same physical parity tail), `n+m=2(N+j+k)`, so `Hplus[n,m]=1/(n+m)=(1/2)·1/(j+k+N)=(1/2)G_N[j,k]`. Confirmed directly by substitution, matching the ledger exactly.

## Independent re-derivation of the Hilbert–Schmidt majorant (the rigorous half)

Worked the algebra from scratch rather than trusting the witness's three spot checks: `G_a[j,k]-G_b[j,k]=(b-a)/((j+k+a)(j+k+b))`, and grouping by `r=j+k` (there are `r+1` pairs `(j,k)` with `j+k=r`) gives `sum_{j,k} |G_a-G_b|^2 = (a-b)^2 sum_r (r+1)/((r+a)^2(r+b)^2)`. I then verified algebraically, for `a,b>=1`, that `(r+a)(r+b)>=(r+1)^2` for every `r>=0`: expanding, `(r+a)(r+b)-(r+1)^2=r(a+b-2)+(ab-1)`, and both `a+b-2>=0` and `ab-1>=0` whenever `a,b>=1`, so the difference is nonnegative termwise. Squaring gives `(r+a)^2(r+b)^2>=(r+1)^4`, hence `(r+1)/((r+a)^2(r+b)^2)<=1/(r+1)^3`, exactly the majorant the witness asserts. Since `sum_r 1/(r+1)^3=zeta(3)` converges, `G_a-G_b` is Hilbert–Schmidt (hence compact) for all `a,b>=1`. This is a complete, from-scratch proof, not a replay.

**Numerical cross-check of the mechanism.** Built finite truncations of `G_1-G_2` directly: the Frobenius-norm-squared stabilizes immediately (`0.355065` at truncation size 500, unchanged to six digits at size 8000), confirming the difference operator is genuinely finite/compact rather than divergent — a cheap, independent sanity check of the HS claim that doesn't require resolving the Hilbert matrix's famously slow truncation convergence.

## Lower bound: `‖G_N‖_ess = ‖G_1‖_ess = pi`, hence `‖G_N‖ >= pi`

Essential norm is invariant under compact perturbation (a standard, elementary fact: for compact `K`, `‖A+K‖_ess=‖A‖_ess`, since essential norm is the distance to the compact operators). Given `G_N-G_1` is compact (shown above), `‖G_N‖_ess=‖G_1‖_ess`. The classical fact that the Hilbert matrix `G_1` has purely continuous spectrum `[0,pi]` with no point spectrum — so its operator norm equals its essential norm, both exactly `pi` — is a standard, well-established result (Hilbert's inequality with sharp constant `pi`, diagonalized via the Mellin transform; this is textbook material, e.g. Hardy–Littlewood–Pólya's *Inequalities* and Magnus's work on the Hilbert matrix spectrum). Trivially `‖A‖>=‖A‖_ess` for any operator `A` (taking the zero compact perturbation in the infimum defining essential norm), so `‖G_N‖>=pi` for every `N>=1`. **This half of the argument I re-derived completely from scratch and verify as rigorous.**

## Upper bound: `‖G_N‖ <= pi` — checked for consistency, not independently re-derived

The entry's matching upper bound relies on a generalized/shifted form of Hilbert's sharp inequality holding with the *same* constant `pi` for every integer shift `N>=1`, not just `N=1`. This is consistent with the standard theory of generalized Hilbert-type operators (the sharp constant for a kernel homogeneous of degree `-1`, such as `1/(j+k+N)`, is governed by its leading large-index asymptotic behavior, which is shift-invariant) and I did not find anything inconsistent with it, but deriving the sharp Schur-test weight for the shifted kernel from first principles is a larger undertaking than this round's scope, so I report this half as *plausible and consistent with well-established classical theory*, not independently re-proved term-by-term the way the lower bound was. Note, importantly, that **this does not weaken the entry's actual conclusion**: the rigorously-established lower bound alone, `‖Q Hplus Q‖>=pi/2≈1.5708`, already exceeds the remaining triangle allowance (`≈0.00128`) by roughly three orders of magnitude — the "barrier" conclusion needs only `>=pi/2`, not the exact equality `=pi/2`, so it stands regardless of how the upper-bound citation resolves.

## Hash and execution verification

Witness `lane_a_v15_440_constant_hankel_tail_barrier.py` (commit `e37df27`, blob `d917632`, SHA-256 `2967c810...`) and manifest `lane_a_v15_440_constant_hankel_tail_barrier_manifest.md` (commit `85bac26`, blob `ce522e0`, SHA-256 `d848140a...`) both verified directly against repo and git objects — exact match. Executed the witness directly (`python3 -I`, unmodified): ran clean, output matches the ledger text exactly, including `remaining_triangle_allowance 0.001280986470142875676519712012280`.

## Independent re-derivation of the final comparison arithmetic

Rebuilt from scratch (fresh 90-digit `Decimal`): `nonconstant_total = 2.534647998455112455357343436959794+0.000008959074744668966136851027926+0.000008056 = 2.534665013529857124323480287987720`; `allowance = 2.535946 - nonconstant_total = 0.001280986470142875676519712012280`; and `(pi/2)/allowance ≈ 1226.24` — confirming the ledger's "fails... by more than three orders of magnitude" is, if anything, an understatement (it's a factor of over 1200).

## Scope and honesty assessment

This is a correctly-scoped negative/barrier result, not a new positive bound, and the entry is explicit about that: it states plainly that this is "not a lower bound on the complete physical operator, because the constant Hankel term may cancel against the variable joint term," and correctly redirects the next admissible gate toward a cancellation-preserving joint estimate rather than any further independent-triangle-charge attempt on this term. No overreach found.

## Summary

Confirmed. The Hilbert–Schmidt compactness argument and the resulting essential-norm lower bound `‖Q Hplus Q‖>=pi/2` are independently re-derived from scratch and are rigorous; the matching upper bound is consistent with standard classical theory though not independently re-proved this round. Either way the practical conclusion is airtight: no independent triangle charge on the constant-Hankel term can close the `2.535946` target, by a margin of three orders of magnitude, confirming that the next genuine gate must preserve cancellation between the constant-Hankel operator and the v15.437 joint variable operator.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-491
parent: v15.441
status: closed
action: none — the rigorous (lower-bound) half of v15.440's argument is independently confirmed and already suffices for its stated conclusion; the upper-bound citation is consistent with established theory. No correction needed.
deliverable: independent confirmation that the constant-Hankel tail term cannot be closed by an independent triangle bound, and that a cancellation-preserving joint estimate with the v15.437 operator is now the only admissible next gate.
