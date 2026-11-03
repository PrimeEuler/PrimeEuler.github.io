# Cone Derivation Ledger v15.331 — External Audit Round 457: unweighted Schur saturation proof verified

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's proof that the v15.327 bound is exactly saturated (hence unimprovable within its own route) independently re-derived and confirmed for all five frequencies.
**Parents:** v15.328 (Round 456), v15.329, v15.330.

---

## Fresh pre-write check

Live `origin/master` was `68c9a85` (v15.330) both at the start of this round and immediately before this write; no further commits landed in between. `v15.331` is the next free ledger number; no collisions (one Lane A commit after Round 456).

## Verification

This entry proves that v15.327's bound `3.272807772...` is not merely a valid upper estimate but the **exact supremum** of the unweighted absolute row/column Schur sum — so no finer interval partition or sharper evaluation within that same route can improve it. Independently confirmed the claim at the heart of this: for each `q∈{2,3,4,5,7}`, computed the actual numeric central (cancellation) interval from Round 456's own closed-form result (`[L,2-L)` for `L<1`, `[2-L,L)` for `L>1`) and checked that `x=0` lies strictly below it in every case:

```
q=2: central interval [0.693147,1.306853) — 0 outside
q=3: central interval [0.901388,1.098612) — 0 outside
q=4: central interval [0.613706,1.386294) — 0 outside
q=5: central interval [0.390562,1.609438) — 0 outside
q=7: central interval [0.054090,1.945910) — 0 outside
```

Since `x=0` falls outside every one of the five frequencies' cancellation intervals simultaneously, each `a_{q,+}(0)+a_{q,-}(0)` attains its maximal (non-reduced) value `L/√q` at that single common point — confirmed directly from the branch conditions (`0<L` and `0<2-L` both hold for every `q` in this set, since `L=log q∈(0,2)` throughout). Summing across the five frequencies therefore gives the row sum its full value `R_abs=Σ log(q)/√q` exactly at `x=0`, which is precisely the bound already certified and re-executed in Round 456 — proving the Schur estimate is saturated, not merely an upper bound with unknown slack.

No new numerical witness is introduced; the entry correctly reuses the already-verified v15.327 witness rather than re-deriving the same number by a new route, and I confirm that reuse is appropriate here since the claim is purely analytic (about *where* the known bound is achieved), not a new computation.

## Scope check

The entry draws exactly the right conclusion: this closes only the "repartition or sharpen the same unweighted absolute Schur sum" sub-route, and explicitly leaves open several genuinely different techniques (nonconstant positive Schur weights, Cotlar/Gram control of cross-frequency products, sign-sensitive cross-frequency cancellation, or joint cancellation with the Hankel/remaining kernel pieces). `FULL_K_TRANSFER` remains INCONCLUSIVE; the saturated value is not promoted to a lower bound on the physical commutator.

## Summary

A valuable piece of negative information delivered efficiently: rather than spending further effort trying to sharpen the 3.273 bound by refining the same Schur-sum method, Lane A proved that method is already tapped out, and correctly named the four specific alternative techniques that remain untried. This keeps the search honestly focused. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-457
parent: v15.331
status: closed
action: none — v15.330's saturation proof independently confirmed for all five frequencies; no correction needed.
deliverable: independent confirmation that x=0 lies outside all five frequencies' cancellation intervals simultaneously, proving the Round 456 bound is exactly attained.
