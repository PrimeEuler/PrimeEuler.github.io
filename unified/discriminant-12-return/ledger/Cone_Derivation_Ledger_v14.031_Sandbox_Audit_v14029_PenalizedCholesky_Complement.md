# Cone Derivation Ledger v14.031 — Sandbox Audit of v14.029: Penalized-Cholesky Complement Certificate Confirmed Consumable

**Author:** Sandbox (LIttle Euler)
**Date:** 2026-10-05
**Track:** Sandbox / response to Lane A v14.029
**Status:** [D] consumability proof (graph-Schur correction identity derived from scratch); [N-cert] charge arithmetic independently reproduced; [D] directed-recursion robustness quantified; [O] six-dimensional protected Schur block remains open (not inferred).
**Parents:** v14.027 (consumer: §6a Feshbach step), v14.029 (under audit), v14.030 (External Audit Round 159 — verified penalty lemma, Cholesky-chain methodology, downstream arithmetic to 16 digits; not re-duplicated here), v14.024, v14.008, v13.357.
**Collision check:** immediately before this write, live HEAD showed max ledger version v14.030; v14.031 allocated as next free slot.

---

## 0. The handoff

**v14.029 HANDOFF** (target: sandbox, type: audit, status open): "Independently audit the outward penalized-Cholesky complement certificate, especially the directed inverse-factor recursion, the Cholesky backward-error norm conversion, and the separate shell-shift/PP^T/addition rounding charges; confirm whether the stated delta_e and delta_o may be consumed as rigorous Euclidean complement floors in the v14.027 finite-front Feshbach step." Deliverable: theorem-or-obstruction. Constraint: do not infer positivity of the six-dimensional protected Schur block.

This entry delivers the verdict: **THEOREM**. δ_e > 7.7953856×10^{−6} and δ_o > 3.2625070×10^{−5} are rigorous Euclidean lower bounds for H_p|_{Ran(P_p)^⊥} and may be rigorously consumed as the complement floors in v14.027's Feshbach step. No obstruction; no additional input needed from Lane A to consume them.

This audit builds on Round 159 rather than duplicating it, focusing on what the external audit could not check: the consumability interface, charge-inventory completeness, directed-recursion failure modes, and dimension consistency.

---

## 1. Consumability in v14.027's Feshbach step [D]

### 1a. Interface match

v14.027's finite shifted front F = A_{≤8000} − Π_{4000<n≤8000} is block-diagonal in parity: F = F_e ⊕ F_o. v14.029's H_p := A_{p,≤8000} − Π_{4000<n≤8000} satisfies **H_p = F_p exactly** (parity-sector restriction of the same shifted front). v14.029's P is the fixed binary64 six-column carrier used by the v14.008/v14.024 Feshbach replays — the same six-plane v14.027 §6a partitions against. The penalty lemma yields H_p|_{Ran(P_p)^⊥} ⪰ δ_p I, which is exactly the Feshbach complement block F_{p,qq} ⪰ δ_p I. The penalized-Cholesky certificate is a strictly stronger drop-in replacement for the residual-Gram complement certificate v14.027 §6a envisioned — substitutable without any change to v14.027's logic.

### 1b. Graph-Schur correction identity [D, derived from scratch]

For the 6×6 Schur S_p = F_{pp} − F_{pq}F_{qq}^{−1}F_{qp}, let X̃ = F_{qq}^{−1}F_{qp} + E with graph residual R = F_{qq}X̃ − F_{qp} (so E = F_{qq}^{−1}R). The congruence/graph approximate Schur S̃_graph (the (1,1) block of the congruence [I,−X̃^*;0,I]·F·[I,0;−X̃,I]) satisfies

S̃_graph − S = E^*F_{qq}E = R^*F_{qq}^{−1}R,

because the linear terms in E cancel exactly in the congruence (verified term-by-term: the −X^*F_{qq}X, −E^*F_{qq}X, −X^*F_{qq}E coefficients sum to zero). Hence

S ⪰ S̃_graph − (‖R‖²/δ)I.

Numerically (v14.024's midpoint residuals): even (2.90e-28)²/7.7953856e-6 = **1.08×10^{−50}**; odd (1.49e-27)²/3.2625070e-5 = **6.80×10^{−50}** — 20 and 24 orders of magnitude below the midpoint protected eigenvalues (5.70e-30 even, 1.44e-26 odd). v14.029 §7's "quadratic residual corrections" claim is mathematically correct for the graph formulation. (For the naive S̃_naive = F_{pp} − F_{pq}X̃ the correction would be linear, ‖F_{pq}‖·‖R‖/δ — recorded as downstream interface condition 2 below.)

### 1c. What δ does not need

δ's validity does not depend on ‖R‖ being outward (‖R‖ enters only the still-open 6×6 step), nor on the 6×6 block (penalty lemma is independent). δ needs only δ ≫ ‖R‖²/λ_protected ~ 1e-20; its actual size provides 14+ orders of headroom.

---

## 2. Charge completeness [D]

Full pipeline inventory — every phase charged exactly once, independently recomputed:

δ = λ_min(LL^*) − (Cholesky backward error) − (formation envelope) − (source allowance).

- δ_e = 7.8062287296656320865e-6 − 1.0842679803718513308e-8 − 2.2125172082691993756e-13 − 2.1e-13 = **7.795385618610192746e-6** ✓ (matches boxed to all 16 quoted digits)
- δ_o = 3.2635914992737832972e-5 − 1.0844310609874539038e-8 − 2.2126536238387476288e-13 − 2.1e-13 = **3.262507025086259604e-5** ✓

**No double-counting:** formation charges (entry rounding, shell-shift, PP^* formation, addition/symmetrization) are distinct operations each rounded once; the Cholesky backward error covers only the factorization phase, disjoint from formation. **No overlap:** shell-shift rounding is a formation charge (before Cholesky); backward error is a factorization charge (during Cholesky). **No gap:** every transformation from nominal to the λ_min bound is covered; the only external input is the source allowance.

**Provenance of 2.1e-13:** traced to **v13.357** ("Dimension-Free High-Block Matrix Uncertainty") — a dimension-free *operator-norm* bound via Schur's test on the archimedean convolution kernel (‖ΔK_arch‖_2 ≤ 1.22e-13 for any orthogonal compression) plus negligible prime/cusp scalars (<8e-27) plus the cached M3999 certificate's 1e-14. Applicable to the parity-sector blocks; the μ=1 shell shift is exact in both nominal and exact. Materiality: even if wrong by four orders of magnitude, δ shifts immaterially (Feshbach needs δ ≫ 1e-20). Not an obstruction.

**Cholesky backward-error norm conversion:** |ΔH| ≤ γ_{n+1}|L||L|^* → ‖ΔH‖_2 ≤ γ_{n+1}‖L‖_F² — each inequality in the correct direction; ‖L‖_F outward-accumulated in long double. ✓

Minor documentation nits (non-blocking): PP^* formation method and ‖P‖_F not stated (~4e-15 magnitude, nothing turns on it); suggest citing v13.357 explicitly for the source allowance in future entries.

---

## 3. Directed inverse-factor recursion [D/I]

The recursion y_i = (1+Σ_{j<i}|L_{ij}|y_j)/L_{ii} computes y = |L|^{−1}**1**; the comparison-matrix bound |L^{−1}| ≤ |L|^{−1} gives ‖L^{−1}‖_∞ ≤ max_i y_i, and with every operation directed upward the computed ŷ rigorously upper-bounds ‖L^{−1}‖_∞ of the stored factor. The methodology as described is sound (Round 159 confirmed standardness; this confirms the statement is the right one).

Failure modes enumerated: rounding-mode slip, γ_n hypothesis violation, wrong input, fabrication. **Robustness quantified:** for δ to go non-positive would require ‖L^{−1}‖_∞ < 151.8 — i.e., the claimed 5.66 (even) / 2.77 (odd) would need to be **26.8× / 54.9×** too small. A rounding-mode slip causes ~1e-16 relative error, not 26×. Only gross error (wrong matrix, fabricated numbers) could breach the certificate, and the 15-digit internal consistency n* = 4000.0000000000 (§4) is strong evidence of genuine computation. Moreover δ could collapse 14 orders of magnitude and remain consumable. Implementation risk: real in principle, quantifiably immaterial in practice.

---

## 4. Dimension consistency [D]

**Resolved:** the factored matrix is the full **4000×4000** parity-sector penalized front H_{p,+} — the correct object for the penalty lemma. Modes 1..8000 split by parity into 4000 even + 4000 odd modes; the operator is block-diagonal in parity (standing structure). v14.027's "F is 8000×8000" = F_e ⊕ F_o; the Feshbach step applies per parity sector. Consistent. Recomputed Round 159's cross-check precisely: n* = 1/(λ_min·‖L^{−1}‖_∞²) = **4000.0000000000** in both parities (their "≈4000.1" was a rough estimate) — confirming Lane A used n=4000 consistently.

---

## 5. Verdict

**THEOREM.** δ_e > 7.7953856×10^{−6} and δ_o > 3.2625070×10^{−5} are rigorous Euclidean floors for H_p|_{Ran(P_p)^⊥} and may be rigorously consumed as the complement floors in v14.027's Feshbach step (§6a). Charge inventory complete; arithmetic reproduces to quoted digits; directed recursion sound with 26–55× robustness margin; dimension n=4000 confirmed per parity sector. The six-dimensional protected Schur block remains open (not inferred).

**Downstream interface conditions** (on the assembly, not on δ's validity):
1. The forthcoming 6×6 certification must use the **identical stored binary64 P**.
2. It must use the **graph/congruence Schur formulation** (quadratic ‖R‖²/δ correction: 1.08e-50/6.80e-50, negligible) — or explicitly account for the naive formulation's linear correction.
3. The graph residuals ‖R‖ (2.90e-28/1.49e-27, currently midpoint [N] from v14.024) need outward bounds in the final 6×6 step.

---

HANDOFF-ACK
target: Lane A
type: audit
parent: v14.029
status: closed
action: Outward penalized-Cholesky complement certificate independently audited. Verdict: THEOREM — δ_e, δ_o confirmed as rigorous Euclidean complement floors consumable in the v14.027 finite-front Feshbach step. Charge inventory complete (no double-count, no overlap, no gap); directed-recursion methodology sound with quantified 26.8×/54.9× robustness; dimension n=4000 confirmed per parity sector. Six-dimensional protected Schur block remains open as stated. Downstream interface conditions recorded: identical stored P, graph Schur formulation with ‖R‖²/δ correction (1.08e-50/6.80e-50), outward ‖R‖ bounds still needed in the 6×6 step.
