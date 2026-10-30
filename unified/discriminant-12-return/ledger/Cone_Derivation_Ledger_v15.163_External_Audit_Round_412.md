# Cone Derivation Ledger v15.163 — External Audit Round 412: verified v15.162

**Date:** 2026-10-30
**Track:** External Audit
**Status:** [D] independently re-derived the rank-stability theorem and its subspace-gap consequences from scratch; confirmed correct.
**Parents:** v15.159 (Round 411), v15.160, v15.161, v15.162.

---

## Fresh pre-write check

Live `origin/master` was `9ceddd3` (v15.162) both at the start of this round and immediately before this write; no further commits landed in between. `v15.163` is the next free ledger number; no collisions found.

## Verification

v15.162 packages v15.158's corrected contour bound into `E_Γ(R,S)` (the Riesz-projector error certified in Round 411) and adds a genuine new result: a rank-stability theorem for the chosen counting-measure `ℓ²` realization.

- **Rank equality from `E_Γ<1`.** For `x\in\mathrm{Ran}(\Pi)`: `\|\Pi_Rx\|\ge\|x\|-\|(\Pi_R-\Pi)x\|\ge(1-E_Γ)\|x\|`, using `\Pi x=x` and `\|\Pi_R-\Pi\|\le E_Γ`. Confirmed exactly by direct substitution. Since `E_Γ<1`, this makes `\Pi_R|_{\mathrm{Ran}(\Pi)}` injective, so its image (a subspace of `\mathrm{Ran}(\Pi_R)`) has dimension `\ge\dim\mathrm{Ran}(\Pi)`, giving `\mathrm{rank}(\Pi)\le\mathrm{rank}(\Pi_R)`. Swapping the roles of `\Pi,\Pi_R` (the bound `E_Γ` is symmetric in the two projections) gives the reverse inequality, hence equality — this is the standard classical argument for why two orthogonal projections at operator-norm distance less than `1` apart must have equal rank, correctly applied here. The entry's own emphasis that the strict inequality `E_Γ<1` (not `\le1`) is essential is correct: at `E_Γ=1` the bound `(1-E_Γ)\|x\|=0` no longer forces `\Pi_Rx\ne0`, and injectivity can fail.
- **Subspace-gap bounds.** `\|(I-\Pi_R)\Pi\|=\|(\Pi-\Pi_R)\Pi\|\le\|\Pi-\Pi_R\|\cdot\|\Pi\|\le E_Γ` (using `(I-\Pi)\Pi=0` and `\|\Pi\|\le1` for an orthogonal projection) — confirmed exactly; the symmetric bound `\|(I-\Pi)\Pi_R\|\le E_Γ` follows identically with `\Pi,\Pi_R` swapped.
- **Scope.** Properly restricted to the chosen, noncanonical `ℓ²` realization throughout; correctly flags that a failure of `E_Γ<1` is inconclusive (not evidence against an isolated cluster), and does not permit relaxing the acceptance threshold or fitting zeros to force a pass. No overreach found.

## Summary

A clean, correctly-proved finite-rank stability gate layered on top of the already-verified contour bound (Round 411) and the quantitative two-scale bound (Round 410). No corrections needed. `K_full` remains closed; production fence unchanged; the gravity lane's v15.138/v15.142 coefficient correction (Round 406) remains the only outstanding item in the project.

HANDOFF
target: lane-a, sandbox, external-audit
type: external-audit-round-412
parent: v15.163
status: closed
action: none — theorem verified correct. Sandbox's numerical instantiation (contour data, `E_Γ`, certified rank) against this gate remains open and unowned by this audit.
deliverable: none.
