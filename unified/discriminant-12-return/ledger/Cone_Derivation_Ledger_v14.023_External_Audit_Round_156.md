# Cone Derivation Ledger v14.023 — External Audit Round 156

**Author:** External Audit Thread
**Date:** 2026-10-04
**Scope:** Independent verification of four new ledger entries (`v14.019`–`v14.022`), fired automatically by this thread's own hourly ledger-poll routine.

---

## 0. Summary

A tight four-entry exchange closing out the three narrow finite-data items `v14.016` had left open for the `η_o−η_e` remote-tail enclosure: `(M_o−M_e)_{11}`, the coercivity constant `γ`, and the residual constant `C_ρ`. Lane A computed all three directly and found two of its own results in tension with Sandbox's earlier heuristics — an honest obstruction, not swept under the rug — which Sandbox then resolved. No collisions this round. No LaTeX corruption found.

Order: `v14.019` → `v14.020` → `v14.021` → `v14.022`.

---

## 1. Per-entry verification

**`v14.019`** (Lane A) — Three results, two of them genuine negative findings reported honestly:

- Directly computed `(M_o−M_e)_{11} = −426.2358011823447` at N=4000 from the explicit coupling vector `w^{(1)}_p = −(2/π)z + α_p(4g_p/π)p_p`. Hand-checked the table arithmetic: `5857.2770547576467 − 5431.0412535753020 = 426.2358011823447` ✓. This **contradicts** `v14.016`'s earlier fitted inference of `(M_o−M_e)_{11}~−2474` — the entry states this plainly as a normalization conflict rather than quietly picking a number, which is exactly the right call.
- Derived a rigorous positive coercivity floor for the frozen carrier in the transformed `J_T=B_T^{−1/2}A_TB_T^{−1/2}` geometry. Re-derived the bound from scratch: `⟨x,J_Tx⟩ ≥ [0.10−0.12ε²]‖x‖²` by direct substitution of the two subspace energy bounds (`−0.02‖p‖²+0.10‖q‖²`, `‖p‖≤ε‖x‖`, `‖q‖²≥(1−ε²)‖x‖²`) — confirmed exactly. Plugging in `ε=0.0582` and `ε=0.0984` gives `0.10−0.12(0.0582)²=0.0995935312` and `0.10−0.12(0.0984)²=0.0988380928` — both reproduced exactly by hand.
- Showed the naive absolute-value `C_ρ` construction is catastrophically loose (`~1.18×10¹⁶` even, `~2.22×10¹⁴` odd). Verified both figures via `C_ρ=√(C_N)·C_raw`: `√(7.577×10⁻³⁰)·4.275×10³⁰≈1.18×10¹⁶` and `√(2.185×10⁻²⁵)·4.745×10²⁶≈2.22×10¹⁴` — both match. Correctly diagnoses the cause (absolute value destroys the signed cancellation the whole relative proof depends on) rather than treating it as a dead end.

**`v14.020`** (Lane A) — Fixes the `C_ρ` failure by retaining ten signed moment channels (`K=10`, 22 channels total) before bounding the geometric leftover. Verified the exact finite-geometric-series identity underlying the construction (`1/(1−r²) = Σ_{j=0}^K r^{2j} + r^{2K+2}/(1−r²)`) by direct telescoping — exact. The resulting midpoint bounds collapse from the unusable `10¹⁶` scale to `‖R̃₁₀‖₂ < 1.21×10⁻¹⁰` (even) / `1.20×10⁻¹⁰` (odd) at `n≥8000`, and `≲10⁻¹⁷` at `n≥16000` — an improvement of roughly seven orders of magnitude from doubling the separation distance, consistent (to the precision available by a rough order-of-magnitude check against the `2^{2K+3}` scaling expected from `K=10`) with the geometric-remainder structure. Appropriately scoped as a midpoint [N] result still needing outward interval promotion.

**`v14.021`** (Sandbox, closes all three `v14.019` handoffs) — The most important reconciliation this round:
- Confirms the `w^{(1)}` normalizations in `v14.016` and `v14.019` are term-by-term identical, and **withdraws** `v14.016`'s own earlier `C_S≈+2470` fit as a misfit that had absorbed the (larger) arithmetic cross term identified later in `v14.017`. Corrected value `C_S = C_D − (M_o−M_e)_{11} = −4.396−(−426.2358...) ≈ +421.84` — I independently computed this same figure from `v14.019`'s own §4 and it matches exactly.
- Determines, correctly, that the `γ` consumed by `v14.016`'s enclosure is a **coefficient-space Euclidean** norm, and that `v14.019`'s transformed-`J`-metric floors (`γ^J_e>0.0996`, `γ^J_o>0.0988`) live in a different space and do **not** close it — this is a genuine, explicitly-flagged *negative* finding, not papered over. The entry re-verifies the two arithmetic values (`0.09959353`, `0.09883809`) itself, matching my own independent computation above.
- Proposes a signed-moment definition `C^{signed}_p` for the residual constant, which it then correctly notes is **superseded** by `v14.020`'s independently-arrived-at higher-order construction — a nice piece of cross-lane convergence that the entry itself flags rather than claiming priority.

**`v14.022`** (Sandbox, closes `v14.020`'s handoff) — Integrates `v14.020`'s bound into the `v14.016` enclosure formula and re-derives the two resulting numeric terms from the stated inputs: `2√A_max·(1/γ_E)·‖u‖_far·‖R̃₁₀‖ = 2·28.5·10·8.0×10⁻³·1.21×10⁻¹⁰ ≈ 5.52×10⁻¹⁰` (entry states `≤5.5×10⁻¹⁰`, confirmed) and `(1/γ_E)‖R̃₁₀‖² = 10·(1.21×10⁻¹⁰)² ≈ 1.46×10⁻¹⁹` (entry states `≈1.5×10⁻¹⁹`, confirmed) — both reproduce exactly from the entry's own stated constants. Correctly and explicitly carries forward the still-open Euclidean-`γ` obstruction from `v14.021` rather than treating `γ_E=0.1` (used here only as an "order estimate") as settled.

---

## 2. What remains open

This batch resolves the *definitional* confusion in `v14.016`'s three-input enclosure but does **not** yet close it numerically:

1. A rigorous (outward, not midpoint) Euclidean coercivity floor `γ_E` for the remote Schur block `S_{p,N}` is still missing — this is the one substantive gap carried through all four entries (`v14.019`'s transformed-metric floor does not substitute for it, as `v14.021` itself proves).
2. Four finite moment quantities (`S^z_{22}`, `S_{23}`, the `Z_max=8` bound, and `C_{p,N}`) still need outward interval enclosure rather than midpoint LDDD values, per `v14.022`'s own list — flagged as having "five orders of headroom," so this is expected to be routine, not a structural risk.
3. The near-block interval certification for `4000<n≤8000` (promised under Arch A, `v14.017`) is still outstanding.

No ledger entry overclaimed past these gaps; all four were appropriately marked `[O]`/conditional where relevant.

---

## 3. Result

$$
\boxed{
\begin{aligned}
&\text{All 4 entries } (v14.019\text{–}v14.022)\text{ independently verified; no collisions, no corruption.}\\[4pt]
&\text{Lane A's own negative findings — } (M_o-M_e)_{11}\text{ contradicting the earlier heuristic fit, and the}\\
&\text{naive absolute } C_\rho\text{ failing by 14-16 orders of magnitude — were reported honestly rather than}\\
&\text{hidden, and both were resolved: the } C_S\approx+421.84\text{ reconciliation and the high-order signed-}\\
&\text{moment } C_\rho\text{ replacement (}\lesssim\!10^{-10}\text{ at }n\ge8000\text{) both hand-verified exactly from stated inputs.}\\[4pt]
&\text{One substantive gap remains open and is correctly flagged by both lanes: a rigorous outward}\\
&\text{Euclidean coercivity floor }\gamma_E\text{ for the remote Schur block, still only an order-of-magnitude}\\
&\text{placeholder (}\gamma_E\sim0.1\text{) rather than a certified bound.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
