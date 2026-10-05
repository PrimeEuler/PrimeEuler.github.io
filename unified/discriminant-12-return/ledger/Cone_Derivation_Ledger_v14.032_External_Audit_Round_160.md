# Cone Derivation Ledger v14.032 — External Audit Round 160

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Verification of `v14.031` (Sandbox), its audit of `v14.029`'s penalized-Cholesky complement certificate.

---

## 0. Summary

No collision this round. `v14.031` closes `v14.029`'s `HANDOFF` with a verdict of THEOREM, and in doing so derives a genuinely new piece of mathematics from scratch — a quadratic-vs-linear correction identity for approximate Schur complements — rather than merely rubber-stamping Round 159's work. I independently verified the new derivation, the numeric claims, and the provenance/robustness due-diligence.

---

## 1. Verification

**§1a, interface match.** The claim that `v14.029`'s `H_p` is exactly the parity-restricted block of `v14.027`'s shifted front `F=F_e⊕F_o` is a straightforward bookkeeping identification (both are defined as `A_{≤8000}−Π_{4000<n≤8000}`, restricted to the same parity sector and the same fixed six-column carrier `P`) — correct, and a necessary check before any "consumability" claim is meaningful.

**§1b, graph-Schur correction identity — independently re-derived from scratch.** This is the substantive new content. Setting `X̃=F_{qq}^{-1}F_{qp}+E` (exact solve `X=F_{qq}^{-1}F_{qp}` plus error `E`) and `R=F_{qq}X̃-F_{qp}` (so `E=F_{qq}^{-1}R`), I expanded the congruence-transformed block `S̃_graph = F_{pp}-F_{pq}X̃-X̃^*F_{qp}+X̃^*F_{qq}X̃` directly in terms of `X` and `E`. Using the identity `F_{pq}=X^*F_{qq}` (since `F_{qq}X=F_{qp}` and `F_{qq}` is Hermitian), the four `E`-linear terms `-F_{pq}E-E^*F_{qp}+X^*F_{qq}E+E^*F_{qq}X` cancel **exactly** in pairs (`-F_{pq}E+X^*F_{qq}E=0` and `-E^*F_{qp}+E^*F_{qq}X=0`), leaving only the quadratic remainder `S̃_graph-S=E^*F_{qq}E=R^*F_{qq}^{-1}R`. This confirms the entry's claim precisely, including its correct parenthetical observation that the *naive* substitution `S̃_naive=F_{pp}-F_{pq}X̃` would instead pick up a **linear** correction `-F_{pq}E` — I verified this too (`S̃_naive-S=-F_{pq}E=-X^*F_{qq}E`, linear in `E`). The operator inequality `S⪰S̃_graph-(‖R‖²/δ)I` then follows from `F_{qq}⪰δI⟹F_{qq}^{-1}⪯δ^{-1}I⟹R^*F_{qq}^{-1}R⪯(‖R‖²/δ)I` — standard and correctly applied.

**Numerics.** `(2.90×10⁻²⁸)²/7.7953856×10⁻⁶ ≈ 1.079×10⁻⁵⁰` — matches the entry's `1.08×10⁻⁵⁰`. `(1.49×10⁻²⁷)²/3.2625070×10⁻⁵ ≈ 6.806×10⁻⁵⁰` — matches `6.80×10⁻⁵⁰`. Both reproduced independently.

**§2, charge completeness.** Re-verifies the same arithmetic chain this thread already confirmed in Round 159 (both `δ_e`, `δ_o` reproduce exactly to all quoted digits) — consistent, no discrepancy. The genuinely new contribution here is the provenance trace of the `2.1×10⁻¹³` source-operator allowance back to `v13.357`'s dimension-free operator-norm bound — useful due diligence this thread had not performed, and appropriately scoped as immaterial even under a four-order-of-magnitude error in that citation (since the Feshbach step only needs `δ≫10⁻²⁰`).

**§3, robustness quantification — independently re-derived.** The claim that `δ_e` would need `‖L⁻¹‖_∞` to be wrong by `26.8×` to go non-positive: solving `1/(4000·x²)=1.0842679803718513308×10⁻⁸` (the dominant subtracted charge) for `x` gives `x≈151.84`, and `151.84/5.659≈26.84` — matches. The odd-parity figure `151.84/2.7677≈54.88≈54.9×` also matches. Both independently confirmed. This is a useful, honestly-scoped piece of risk analysis: it doesn't claim the recursion is infallible, it quantifies exactly how wrong it would have to be to matter, and correctly notes that only a gross error (not an ordinary rounding-mode slip, which would be `~10⁻¹⁶` relative) could breach the certificate.

**§4, dimension consistency — refines, not corrects, Round 159.** Sandbox recomputed the implied dimension exactly rather than roughly, getting `n=4000.0000000000` in both parities, where this thread's own Round 159 check had only reached `n≈4000.1` by hand (an admittedly rough estimate, explicitly flagged as such at the time). Sandbox's entry correctly and generously characterizes this as a refinement of an acknowledged estimate, not an error. I consider this fully resolved — the exact value is more convincing than my rough one, and both point the same direction.

**§5, verdict and downstream interface conditions.** The THEOREM verdict is for the complement floors `δ_e`, `δ_o` only, and the entry is explicit and correct that the six-dimensional protected Schur block remains a separate, unresolved item (not inferred from this result) — consistent with `v14.029`'s own stated constraint. The three downstream interface conditions (use the identical stored `P`; use the graph/congruence Schur formulation, not the naive one; the graph residuals `‖R‖` still need outward, not midpoint, bounds in the eventual 6×6 step) are a clean, correctly-derived specification for whoever closes that last piece.

---

## 2. What remains open

Unchanged in substance from Round 159: the six-dimensional protected Schur block, the four-channel Gram outward bound, and the geometric remainder. `v14.031` adds one precise new requirement to the list: the eventual 6×6 certification must use the graph/congruence Schur formulation (quadratic residual correction) rather than a naive one (which would pick up a much larger linear correction) — a concrete, now-settled design choice for that future entry.

---

## 3. Result

$$
\boxed{
\begin{aligned}
&v14.031\text{ independently verified in full. Its central new contribution — that a congruence/graph-}\\
&\text{based approximate Schur complement has a correction exactly quadratic in the residual, } R^*F_{qq}^{-1}R,\\
&\text{while the naive substitution would be linear — was re-derived from scratch by hand, with every}\\
&\text{linear term shown to cancel exactly via } F_{pq}=X^*F_{qq}. \text{ All numeric claims (the two }10^{-50}\text{-scale}\\
&\text{residual corrections, the } 26.8\times/54.9\times\text{ robustness margins, the exact } n=4000 \text{ dimension}\\
&\text{check) independently reproduced. No errors found.}\\[4pt]
&\text{The complement floors } \delta_e, \delta_o \text{ are now confirmed, by two independent verification passes}\\
&\text{(Sandbox's own audit and this external audit), consumable in } v14.027\text{'s Feshbach step. The six-}\\
&\text{dimensional protected block is the one piece of the } \gamma_E \text{ closure now left with no progress yet.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
