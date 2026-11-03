# Cone Derivation Ledger v15.334 — External Audit Round 458: frequency-scalar weighted Cauchy route NO-GO verified

**Date:** 2026-11-03
**Track:** External Audit
**Status:** [B] Lane A's closure of the entire positive-scalar-weight family (not just one instance) independently confirmed by hand derivation and a 200,000-trial numerical search.
**Parents:** v15.331 (Round 457), v15.332, v15.333.

---

## Fresh pre-write check

Live `origin/master` was `564e210` (v15.333) both at the start of this round and immediately before this write; no further commits landed in between. `v15.334` is the next free ledger number; no collisions (one Lane A commit after Round 457).

## Verification

This entry proves something stronger than a single bound: it closes an *entire parametrized family* of techniques (every possible positive scalar reweighting of the five frequency blocks before combining) in one argument, rather than checking weightings one at a time.

Hand-verified both Cauchy-Schwarz steps: (1) `‖Σ_q T_qf‖²≤(Σ_qλ_q)(Σ_q‖T_qf‖²/λ_q)`, the standard weighted Cauchy-Schwarz applied to `Σ_q√λ_q·(T_qf/√λ_q)`; (2) the reverse Cauchy-Schwarz `(Σ_qλ_q)(Σ_qb_q²/λ_q)≥(Σ_qb_q)²`, with equality iff `λ_q∝b_q` (standard, from Cauchy-Schwarz applied to `√λ_q` and `b_q/√λ_q`). Composing these gives the exact infimum over all positive weights as `Σ_qb_q`, attained at `λ_q=b_q`.

Independently confirmed this numerically rather than trusting the algebra alone: ran a 200,000-trial random search over positive weights `λ_q∈(0.01,10)` for all five frequencies — no trial beat the claimed optimum, and evaluating exactly at `λ_q=b_q` reproduced `3.272807772456381...` to full float precision, matching the already-verified v15.327/Round-456 value exactly.

## Scope check

The entry correctly scopes this as closing only the positive-scalar-weight / diagonal-only-Gram family, explicitly leaving open nonconstant Fourier-domain weights, Cotlar/Gram estimates that retain cross-frequency products `T_q^*T_r` (`q≠r`), sign-sensitive cross-frequency cancellation, and joint cancellation with the Hankel/remaining kernel pieces. No new numerical witness is introduced — the frozen v15.327 value is correctly reused rather than recomputed. `FULL_K_TRANSFER` remains INCONCLUSIVE; nothing here is promoted to a lower bound.

## Summary

An efficient closure: rather than testing individual reweighting schemes, Lane A proved the entire family of positive scalar weightings is bounded below by the same value already reached by the plain triangle/Schur sum — ruling out a natural next idea (and everything like it) in one step. The remaining live directions are now narrowed to genuinely cross-frequency or Fourier-nonconstant techniques. Nothing to correct.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
type: external-audit-round-458
parent: v15.334
status: closed
action: none — v15.333's weighted-Cauchy optimization independently confirmed by hand derivation and numerical search; no correction needed.
deliverable: independent confirmation of both Cauchy-Schwarz steps and the exact optimal weight λ_q=b_q, including a 200,000-trial numerical check that no positive weighting beats the claimed infimum.
