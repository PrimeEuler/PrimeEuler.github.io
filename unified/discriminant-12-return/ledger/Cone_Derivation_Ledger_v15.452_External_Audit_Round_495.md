# Cone Derivation Ledger v15.452 — External Audit Round 495: v15.451's finite-width Hankel scale barrier independently verified, including a direct numerical check of the Schur row-sum mechanism

**Date:** 2026-11-06
**Track:** External Audit
**Status:** [B] Lane A's v15.451 — proving that a finite-width numerical section of the constant-Hankel component, taken at a fixed width `M` much smaller than the tail origin `N`, has operator norm bounded by `M/(2N)` (hence well under `1/2`, far short of the true infinite-tail value `π/2` established in Rounds 491-492) — independently re-derived and confirmed, including a from-scratch numerical sanity check of the Schur-test mechanism on small matrices. A correctly-scoped methodological/explanatory result, not a new bound on the physical operator.
**Parents:** v15.448 (Round 494), v15.449, v15.450, v15.451.

---

## Fresh pre-write check

`git fetch origin master` returns `f9ae8f2` (v15.451), identical to the head just read. `v15.452` is next free; no collisions.

## What this entry explains

Rounds 491-492 established that the constant-Hankel term's *infinite*-tail operator norm is exactly `π/2≈1.5708`. This entry explains why a *finite-width numerical section* of the same matrix, taken at any width `M` much smaller than the tail origin `N=256001`, would see a far smaller number — not because the infinite result is wrong, but because a narrow finite window simply cannot resolve a scale that only becomes visible once the window is comparable to the tail origin itself. This matters because it draws a bright line against treating any past or future finite-width numerical probe (widths 128–1024, as the entry notes) as evidence about the true infinite-tail norm.

## Independent re-derivation of the bound

**Setup.** For a step-two parity tail with modes `n_j=N+2j`, the constant-Hankel matrix is `C_M(j,k)=1/(n_j+n_k)=1/(2N+2j+2k)` for `0<=j,k<M`.

**Schur row-sum bound.** For a symmetric matrix with nonnegative entries, the operator norm is bounded by the maximum absolute row sum — a standard, elementary fact (Schur's test with trivial weight `p=1`: `|<x,Ax>|<=sum_{j,k}|x_j||x_k|A(j,k)<=sum_j|x_j|^2·(max row sum)` by Cauchy–Schwarz/AM-GM on the symmetric kernel). I re-derived this from the definition rather than citing it, and verified it numerically by directly diagonalizing small finite Hankel matrices of this exact form (`N=50`, `M=10,30,50,80`): in every case the true operator norm (largest `|eigenvalue|`, since the matrix is symmetric) was comfortably below both the max row sum and the cruder `M/(2N)` bound — e.g. at `M=80`, true norm `0.348085` vs. row-sum bound `0.480847` vs. `M/(2N)=0.8` — confirming the chain of inequalities is not just formally valid but has real slack in practice.

**Row-sum monotonicity and the crude bound.** Since every entry of row `j` strictly decreases as `j` increases (larger `j` means larger denominators), the maximum row sum is attained at `j=0`: `sum_{k=0}^{M-1}1/(2N+2k)=(1/2)sum_{k=0}^{M-1}1/(N+k)<=(1/2)·M/N=M/(2N)` (bounding each of the `M` terms by the largest, `1/N`). Both steps checked directly.

## Independent re-derivation of the exact rational values

Rebuilt all four `(N=256001, width)` row sums from scratch with Python's `Fraction` (not importing the witness): `width=128: 0.000249937032788928...`; `256: 0.000499749190956123...`; `512: 0.000998999382112517...`; `1024: 0.001996006744086531...` — matching the ledger and witness exactly, digit for digit, and each confirmed `<=` the corresponding crude `M/(2N)` bound. Also independently confirmed the three boundary assertions: `M/(2N)` at `M=1024` is `<1/500`; at `M=N-1=256000` is `<1/2`; at `M=N=256001` equals exactly `1/2` — all exact, trivial fraction comparisons, verified directly.

## Hash and execution verification

Witness `lane_a_v15_451_finite_width_hankel_scale_barrier_certificate.py` (commit `dff3f5a`, blob `16a7ab7`, SHA-256 `a6f3497b...`) and manifest `lane_a_v15_451_finite_width_hankel_scale_barrier_certificate.sha256` (commit `c7038a5`, blob `0d2ed69`, SHA-256 `ee93aa59...`) verified directly — exact match. Executed the witness directly (`python3 -I`, unmodified): ran clean, output matches the ledger text exactly, including `full_joint_norm_gate=UNEVALUATED`.

## Scope and honesty assessment

This entry is precisely calibrated: it neither claims this bounds the physical operator nor disputes any prior numerical probe's prime-norm findings — it states plainly "it does not validate or invalidate their observed prime norms, and it does not give a bound on the infinite full joint sum." The practical consequence — that resolving the true `π/2` constant-Hankel scale numerically would need a width comparable to `N=256001` itself, computationally prohibitive by direct dense diagonalization — is stated accurately and used correctly to redirect the next gate toward analytic (Mellin/multiscale) or structured joint methods rather than brute-force finite sections.

## Summary

Confirmed. The Schur row-sum argument, its exact rational evaluation at the physical scale, and the qualitative "finite narrow sections cannot see the π/2 scale" conclusion are all independently re-derived and verified, including a direct numerical demonstration of the underlying mechanism on small test matrices. This is a useful, honestly-scoped methodological result explaining a blind spot in finite-section numerics, not a claim about the actual joint operator.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-495
parent: v15.452
status: closed
action: none — v15.451's Schur row-sum bound, exact arithmetic, and scope are correct and independently re-derived, including a numerical sanity check of the underlying mechanism. No correction needed.
deliverable: independent confirmation that fixed small-width finite sections of the constant-Hankel component cannot resolve its true pi/2 infinite-tail scale, and that this says nothing about the full joint operator norm.
