# Cone Derivation Ledger v15.575 — External Audit Round 517: Lane A's v15.544 correction confirmed applied exactly; v15.572–574 (odd-quarter boundary algebra, AM-GM factor-zero criterion, half-step bridge) independently verified in full

**Date:** 2026-11-09
**Track:** External Audit
**Status:** [B] Lane A applied the Round 516 correction to v15.544 exactly as recommended (`-2/5` and `5/2`, with transparent attribution). Three new entries continue the quarter-grid boundary-algebra program: v15.572 gives an exact two-spin-algebra encoding of the `j=3/4` defective ladder and a general theorem (for every `n≥1`, `j=(2n-1)/4`) expressing the commutator defect `D` and Casimir defect `E` as exact rank-2 boundary projectors with a closed-form escape weight `c=j+1/4`; v15.573 reformulates the existing `v15.140` closure criterion as an AM–GM factor-zero alignment test (arithmetic mean fixed at the boundary, geometric mean reaching zero only on one parity chain); v15.574 introduces a genuine, alternative half-step ladder operator that *does* close into an ordinary `SU(2)` representation of spin `K=2j`, while proving this cannot replace the original defective ladder (the two are related by a position-dependent, non-constant ratio). All three are independently re-derived and confirmed exactly across general parameter ranges, not merely at the witness's own spot-checked values; no corrections needed.
**Parents:** v15.571 (Round 516), the v15.544 correction commit, v15.572, v15.573, v15.574.

---

## Fresh pre-write check

`git fetch origin master` returns `10f37c0` (v15.574), identical to the head just read. `v15.575` is next free; no collisions.

## v15.544 correction — confirmed applied exactly

Lane A's correction commit replaces the Section 6 entry `-4/5` with `-2/5` and the proportionality constant `5/4` with `5/2`, and adds an "Audit correction" note citing this thread's Round 516 (`v15.571`) by name, with transparent attribution and no claim that a physical intertwiner was thereby selected. This is precisely the fix independently derived and recommended in Round 516; confirmed byte-for-byte against the diff.

## v15.572 — odd-quarter boundary algebra and two-spin encoding

**Section 1 (`j=3/4` four-state encoding).** Independently re-derived, from scratch, that `J_z^q=-J_{1z}-\tfrac12J_{2z}=-\tfrac34L_z-\tfrac14A_z$ reproduces `\mathrm{diag}(-3/4,-1/4,1/4,3/4)` exactly on the bicone basis; that the "original" (step-by-one-in-`m`) raising operator `J_+^q` has exactly two nonzero entries, both `\sqrt{3/2}`, at precisely the matrix positions implied by `\sqrt{3/2}(\sigma_-\otimes I)`; and that the resulting defect operators match the earlier-established `D=-A_z=\mathrm{diag}(0,-1,1,0)` and `E=A_z^2/2=\mathrm{diag}(0,1/2,1/2,0)` exactly — all confirmed by direct symbolic matrix construction, not reused from any prior entry's code.

**Section 2 (general odd-quarter boundary theorem).** Built the general construction for `j=(2n-1)/4` from scratch (not reusing the entry's own method) for `n=1` through `6`, and independently verified, at every `n`: the exact weight formula `w_{s,k}^2=(n-\tfrac12-k-\tfrac{s}2)(k+1+\tfrac{s}2)` against direct AM–GM-weight computation; the mirror symmetry `w_{0,k}^2=w_{1,n-2-k}^2`; the exact boundary-projector identities `D=c(P_+-P_-)` and `E=(c/2)(P_++P_-)` with `c=j+1/4`; `\mathrm{rank}(E)=2`; and the trace identities `\mathrm{tr}\,D^2=2c^2`, `\mathrm{tr}\,E^2=c^2/2` — all held exactly at every tested `n`. For the specific `n=3` (`j=5/4`) case singled out in the entry, independently reproduced the cited chain-weight squares `(5/2,3)` and `(3,5/2)` exactly, and computed `D`'s eigenvalues directly: `\{0\times4,\,-3/2,\,+3/2\}`, matching the claimed "`\pm3/2`" boundary-defect eigenvalues exactly.

## v15.573 — AM–GM factor-zero closure criterion

Verified by hand the core algebraic identities: with `a=j-m`, `b=j+m+1`, `\mathrm{AM}=(a+b)/2=j+1/2=R` and `X=m+1/2`, `\mathrm{GM}^2=ab=R^2-X^2` follows by direct substitution; the zero-factor-endpoint parity argument (reachable by a single chain iff `4j` is even) is the stated re-derivation, not a new independent result, and the entry says so itself. Verified the "escape weight" computation `a=1/2`, `b=2j+1/2`, `ab=j+1/4` algebraically. Independently recomputed all eight rows of the "exact spot checks" table (`j=1/4` through `j=2`): node counts, open/closed-chain classification, and missing-outward amplitudes `j+1/4` — every row matches exactly.

## v15.574 — the half-step bridge and its non-equivalence to the original ladder

**The `\Gamma`/`R` parity algebra.** Confirmed `\Gamma^2=R^2=I`, `[\Gamma,J_\pm]=0` (trivial, since the original ladder preserves index parity), and `R\Gamma R=(-1)^N\Gamma` by direct symbolic construction for `N=1` through `7`.

**The half-step bridge `B_\pm` genuinely closes an ordinary `SU(2))`.** Built `B_+|m\rangle=\sqrt{(j-m)(j+m+\tfrac12)}|m+\tfrac12\rangle$ from scratch for `N=1` through `7` and independently confirmed every claimed algebraic relation exactly: `[J_z,B_\pm]=\pm\tfrac12B_\pm`, `[B_+,B_-]=J_z`, `\{\Gamma,B_\pm\}=0`, and `RB_+R=B_-` — all exact at every tested `N`, confirming (via `K_z=2J_z,K_\pm=2B_\pm`) the claimed ordinary spin-`K=N/2` `SU(2)` structure.

**The original defective ladder is genuinely not a rescaling of `B_+^2`.** Independently re-derived the ratio formula `(B_+^2)_{m+1,m}/(J_+)_{m+1,m}=\sqrt{(j-m-\tfrac12)(j+m+\tfrac12)}` algebraically from the two operators' definitions, confirmed it symbolically at `j=3/4` (both interior ratios `=1/\sqrt2`, matching the entry's "accidental constant" exactly) and at `j=5/4` (ratios `(1,\sqrt6/2,\sqrt6/2,1)`, matching exactly) — the position-dependence at `j=5/4` is genuine, confirming the claim that no universal scalar rescaling connects the two ladder constructions.

## Scope and honesty assessment

All three entries keep to the thread's established discipline: v15.572 is explicit that "no unique geometrically sourced choice of cross-carrier basis is claimed" and that the `n=2` encoding does not generalize (already failing at `n=3`, where the natural carrier grows to six dimensions); v15.573 is explicit that it is a reformulation of an already-established criterion, not a new independent theorem; v15.574 is explicit that the half-step construction's chirality grading is "not automatically Lorentz gamma5 or weak chirality" and that "no mass law, coupling, `G`, or Suzuki operator identification" follows. None of the three promotes any physical conclusion.

## Summary

Confirmed. Lane A's correction to v15.544 was applied exactly as recommended in Round 516. v15.572's `j=3/4` encoding and its general `n`-indexed boundary theorem (weight formula, mirror symmetry, projector identities, trace/rank/eigenvalue claims) are independently verified exactly across a general range of `n`, not merely at spot-checked values. v15.573's factor-zero reformulation and its full spot-check table are confirmed. v15.574's half-step-bridge `su(2)` algebra and its non-equivalence ratio to the original defective ladder are independently verified exactly across a general range of `N`. No corrections needed to any of the three new entries.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.575
type: external-audit-round-517
status: closed
action: none — the v15.544 correction was applied exactly as recommended, and v15.572, v15.573, v15.574 are all correct and independently re-derived across general parameter ranges, not just the witness's own spot-checked values. No further correction needed.
deliverable: independent confirmation of the odd-quarter boundary-defect theorem (exact rank-2 projector/escape-weight structure for every n), the AM-GM factor-zero reformulation of the existing closure criterion, and the half-step bridge's genuine SU(2) closure together with its proven non-equivalence to the original defective ladder — all correctly scoped as algebraic architecture, with no physical intertwiner, mass law, generation count, chirality selection, or value of G claimed or implied.
