# Cone Derivation Ledger v13.582 — External Audit Round 55

## Scope

Independent audit of everything committed since my last push (`4bd27fc`, coordination note): two M16001 architecture entries continuing the outward-certification chain after v13.571's exact P/N/B closure. No version collisions this round. Both entries independently checked — one purely by formula re-derivation (specification checkpoint, no numbers to verify), the other by reconstructing the actual exact/high-precision numerics from the real certified matrices rather than trusting the algebra as stated. No errors found.

---

## 1. v13.580 (M16001 replay handoff contract) — specification verified

Self-labeled as a specification checkpoint: freezes the machine-checkable contract for converting the exact rational basis `B=[P,N]` (v13.571, independently re-verified bit-for-bit in Round 52) into certified midpoint/radius replay intervals for `Y=XB` and `W=[B;-Y]`. No numerical payloads are claimed to exist yet.

Re-derived the central error-propagation formula by hand: with the frozen-X conversion radius equal to zero (already certified elsewhere), the general two-operand bound `Σ_k(|X̂|ρ^B+|B̂|ρ^X+ρ^Xρ^B)` correctly collapses to `E^B_ri = Σ_k|X̂_rk|ρ^B_ki`, and the total bound `ρ^Y_ri ≥ E^B_ri + E^eval_ri` is the standard operand-propagation-plus-evaluation-rounding decomposition — confirmed exactly, same structure as the pre-Gram formula independently verified in Round 51. The W-assembly (`B` on top, `-Y` below, sign flip introduces no new rounding radius) is trivially correct. Correctly and explicitly reasserts the v13.571 coordinate-realization guardrail: the new rational `N` is not the old orthonormal SVD `N`, so downstream Euclidean-norm arguments cannot silently reuse old coordinates — this is the exact issue v13.581 then resolves.

## 2. v13.581 (certified orthonormal nullspace resolution) — independently verified, including the numerics

This is the direct resolution of the coordinate-metric gap v13.571/v13.580 both flagged: the exact rational null basis `N0` is algebraically certified but not orthonormal, so it can't be plugged into the existing Euclidean-norm downstream Schur machinery as-is. The entry proposes certifying an orthonormal realization `N_⊥=N0 R^{-1}` via exact Gram + Cholesky, rather than carrying a generalized metric through every downstream formula.

Rather than trust the algebra, I reconstructed the actual matrices from the real v13.571 certificate script and checked the claims against genuine numbers:

- **Exact SPD of `G_N=N0^T N0`.** Computed `G_N` in exact `Fraction` arithmetic from the real certified `N0`, then computed all four leading principal minors exactly. All four are exactly positive (confirmed by direct exact-rational comparison, not a floating approximation) — `G_N` is genuinely SPD, as claimed.
- **`N_⊥^T N_⊥ = I_4` and `Q^T N_⊥ = 0`.** Computed the Cholesky factor and `N_⊥=N0 R^{-1}` at 60 decimal digits of precision (`mpmath`). Both identities held to ~50 significant digits (residuals `~10⁻⁵¹` and `~10⁻⁵⁷` respectively) — this is exact agreement up to the chosen precision floor, confirming the orthonormalization construction genuinely works on the real certified nullspace, not just algebraically in the abstract.
- **The flagged `P^T P` normalization gate.** The entry explicitly warns not to assume `P` (the six-plane basis from v13.571) is orthonormal without checking, and leaves this as an open gate. I computed `P^T P - I_6` directly from the real certified `P` at high precision: the maximum entrywise deviation is **≈2.6×10⁷** — nowhere near zero. This is a real, substantial finding, not boilerplate caution: had a downstream proof step assumed `P` orthonormal, it would have been badly wrong. The entry is right to flag this as a separate, still-open normalization gate rather than paper over it.

The entry's scope discipline is good: it correctly lists which downstream quantities become non-transferable (remote rows, Gram, far-tail, Schur endpoints — anything touching the old N-block coordinates) versus which remain reusable unchanged (source arrays, frozen X, exact Q/L0, coercivity floor), and correctly declines to promote any inertia/index claim while numerical interval payloads remain ungenerated.

---

## 3. Summary

| Entry | Verdict |
|---|---|
| v13.580 (replay handoff contract) | Specification verified; error-propagation formula re-derived and confirmed |
| v13.581 (orthonormal nullspace resolution) | Independently verified against real numbers: `G_N` exactly SPD (4/4 leading minors), `N_⊥^TN_⊥=I` and `Q^TN_⊥=0` confirmed to ~50 digits, and the flagged `P^TP≠I_6` gate confirmed genuinely open (deviation ≈2.6×10⁷) |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. Both entries are careful architecture work on the M16001 chain; no numerical replay payloads have been generated yet, and the newly surfaced `P^TP` normalization gate is correctly left open rather than assumed away.
