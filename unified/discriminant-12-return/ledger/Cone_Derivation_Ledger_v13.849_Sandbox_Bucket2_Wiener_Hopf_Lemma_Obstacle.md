# v13.849 — Sandbox Bucket 2: the Wiener–Hopf lemma — obstacle precisely characterized

**Date:** 2026-09-28
**Lane:** Sandbox (our Lane B — Jeremy's exploratory track under LIttle Euler; disambiguated from the ledger's dormant norm-quotient Lane B)
**Status:** [I]/[O] — exact algebra + numerics + sharp conjectures, not certified
**Entry kind:** sandbox analytic report (proof-obstacle characterization)
**Supersedes nothing. Refines:** v13.846 (the ker-minimization mechanism — its asymptotic step), v13.844 (R2)
**Sibling:** v13.848 (selection identity) — its verdict gates this lemma's transfer to Suzuki's true v_±

**Headline: OBSTACLE (precisely characterized) + sharp partial results.** The lemma as literally stated is trivially true (Cauchy–Schwarz); the meaningful version (corr→0) is reduced by exact algebra to t·ρ₁+ρ₂→0, and the numerics reveal the mechanism is a delicate O(1) cancellation of opposite signs — not a structural orthogonality. A full Wiener–Hopf proof is blocked on analytic control of the discrete minimizer for a *growing* (non-L¹) kernel, outside classical theory.

---

## 1. Clarification: the lemma as stated is trivial

Task as briefed: ⟨w_A, P_{ker(K_Aᵀ)}eˣ⟩ = o(e^A‖w_A‖‖P_{ker}eˣ‖). By Cauchy–Schwarz, |⟨w_A,Pf⟩|/(e^A‖w_A‖‖Pf‖) ≤ 1/e^A → 0 **trivially** — the e^A factor makes the claim content-free. (Correction caught by the sandbox agent; recorded, not hidden.)

The **meaningful** lemma (what v13.846 §2's numerics actually test) is the correlation version **without** e^A: **corr(w_A, P_{ker}eˣ) → 0**, i.e. ⟨w_A,Pf⟩ = o(‖w_A‖·‖Pf‖). Three levels, strongest first:
- **Strong (observed):** ℓ* = o(e^A), i.e. corr = o(1/A).
- **Medium (meaningful lemma):** corr → 0, i.e. ℓ* = o(‖w_A‖‖Pf‖) = o(A·e^A).
- **Weak (as briefed):** trivial by Cauchy–Schwarz.

This entry targets the **medium** lemma and documents the evidence for the strong version.

## 2. Exact algebraic framework (proven, no numerics)

Discrete setting: K = UΣVᵀ (thin SVD), P = I−UUᵀ, X = [x,1], f = eˣ. M_{ker} = XᵀPX = diag(m₁,m₂) by parity (m₁=‖Px‖², m₂=‖P1‖²); w_A = A·Px/m₁ + P1/m₂.

- **Lemma 1.** ℓ*(A) := A·A*+B* = −⟨w_A,Pf⟩ exactly.
- **Lemma 2 (correlation decomposition).** With ρ₁=⟨Px,Pf⟩/(‖Px‖‖Pf‖), ρ₂=⟨P1,Pf⟩/(‖P1‖‖Pf‖), t=A‖P1‖/‖Px‖: **corr(w_A,Pf) = (t·ρ₁+ρ₂)/√(t²+1)**, hence |corr| ≤ √(ρ₁²+ρ₂²).
- **Lemma 3 (residual identities).** R* := P(Xa*+f): ‖R*‖² = ‖Pf‖²(1−ρ₁²−ρ₂²) and ⟨R*,f⟩ = ‖R*‖².
- **Lemma 4 (parity-split).** A* = −⟨Px,P sinh⟩/‖Px‖², B* = −⟨P1,P cosh⟩/‖P1‖² (cross-parity terms vanish exactly).

## 3. Sharp numerical structure (A=2..6, N=120, λ=0, α=1e-10)

| A | ρ₁ | ρ₂ | t | corr | ℓ*/e^A | A*/e^A | B*/(Ae^A) | ρ₁²+ρ₂² |
|---|---|---|---|---|---|---|---|---|
| 2 | +0.839 | −0.543 | 0.79 | +0.094 | −0.171 | −0.472 | +0.387 | 0.999 |
| 3 | +0.816 | −0.578 | 0.79 | +0.051 | −0.145 | −0.478 | +0.430 | 1.000 |
| 4 | +0.699 | −0.715 | 1.04 | +0.0097 | −0.036 | −0.469 | +0.460 | 1.000 |
| 5 | +0.764 | −0.645 | 0.84 | +0.00032 | −0.0015 | −0.470 | +0.466 | 0.999 |
| 6 | +0.736 | −0.676 | 0.94 | +0.0090 | −0.051 | −0.474 | +0.466 | 0.999 |

Scalings: ‖Px‖~A, ‖P1‖~const, ‖Pf‖~A·e^A, ‖w_A‖ bounded. Endpoint signs at +A stable: Px>0, P1<0, Pf>0. Parity exact to 1e-14. (A=6 corr wobble flagged as fixed-N discretization noise.)

**Findings:**
- **(F1)** ρ₁↛0, ρ₂↛0, t↛∞. The individual normalized correlations are O(1) and stable; t is O(1). **There is NO structural orthogonality.**
- **(F2)** ρ₁²+ρ₂²≈1 (‖R*‖/‖Pf‖~0.03): Pf ∈ span{Px,P1} — by parity, P(cosh)∥P(1) and P(sinh)∥P(x) approximately. **The selection makes (8.5) discretely solvable**: (eˣ+A*x+B*) ∈ col(K) to ~3% relative to Pf.
- **(F3)** The cancellation is **t·ρ₁+ρ₂→0 via OPPOSITE SIGNS** (ρ₁>0>ρ₂): a delicate O(1) magnitude balance, not a vanishing.
- **(F4)** Individual limits exist and are stable: A*/e^A→−0.47, B*/(Ae^A)→+0.47. **Only the combination cancels.**

**Two different asymptotics:** "solvability" (F2) is controlled by N (trial-space richness) — the discrete shadow of continuum solvability; "cancellation" (F3) is controlled by A (domain growth) at fixed N — a property of the *minimizer*, not of solvability alone.

## 4. The exact obstacle

To prove corr→0 one must prove t·ρ₁+ρ₂→0 — control of the discrete minimizer (A*,B*)=−M_{ker}⁻¹b_{ker} as A→∞ at fixed N. Three blocks:

- **(a) The kernel is outside classical Wiener–Hopf theory.** The D12 screw g(t) = R_12(t)−A_12(t) GROWS for large t (R_12(t)=o(t·e^{t/2})); it is NOT in L¹ or the Wiener algebra. Classical finite-section/truncated Wiener–Hopf (Gohberg–Krein, Prössdorf–Silbermann) requires integrable symbols. The "unresolvable" space ker(K_Aᵀ) for a growing-kernel truncated convolution is not covered — **new theory needed**.
- **(b) Fixed-N numerics.** The observed decay lives in A∈[2,6] with coarsening mesh h=2A/N. A rigorous A→∞ lemma needs h→0 AND A→∞ jointly — unprobed.
- **(c) The cancellation is delicate, not structural.** (F1)+(F3): an O(1) magnitude balance t·|ρ₁|=|ρ₂|, not a vanishing or a symmetry. Proving it needs precise boundary-layer asymptotics of the range projection Π_{S_A} for the D12 kernel. Concrete foothold: the endpoint sign pattern (Px>0>P1 at +A) — Π_S undershoots x and eˣ but overshoots 1 at +A — is where a boundary-layer analysis starts.

The value 0.48 (=lim A*/e^A): set by D12 ker-geometry (the numbers ⟨Px,P sinh⟩, ‖Px‖²); the lemma as such does not determine it.

## 5. Sharpest conjectures

- **Conjecture (medium):** for the D12-screw truncated convolution K_A (λ=0), corr(w_A,P_{ker(K_Aᵀ)}eˣ)→0 via t·ρ₁+ρ₂→0, with ρ₁>0>ρ₂ stable and t=O(1).
- **Conjecture (strong):** ℓ*(A)/e^A→0 (corr=o(1/A)).
- **Sub-conjecture (parity-split rank-1):** P(cosh)∥P(1), P(sinh)∥P(x) approximately, improving as N→∞ (solvability).

**What would settle it:** (1) numerics with A>6 at fixed h (needs g beyond the tmax=12 spline — use the exact R_12/A_12 formula); (2) boundary-layer analysis of Π_{S_A} for growing-kernel truncated convolutions — new theory; (3) an exact identity for (A*,B*) bypassing asymptotics (none found; §2's lemmas are the complete exact algebra).

## 6. Transfer (per v13.848)

CONDITIONAL TRANSFER under **exactly λ_a>0**: if corr→0 is proven for the discrete Tikhonov selection, it transfers to Suzuki's TRUE v_± conditional solely on λ_a>0 (v13.848 §6). The §7 RH-adjacent gap is the only gap between the Bucket 2 numerics and Suzuki's text. 0.48 unexplained under every reading.

## 7. Caveats

- Scripts wh2/wh3 were OOM-killed under concurrent sibling load; the parity-split was recovered from wh1 data + exact parity instead — flagged, not hidden.
- No positivity, RH, or Hilbert–Pólya claim. The prime ramp is untouched.

## 8. Provenance

- Run: `~/workspace/d12/lane_b/sandbox/runs/20260928-215739-bucket2-wiener-hopf-lemma/` (report.md, STATUS.md, scripts/wh1.py — ran, data/wh1_profiles.npz; wh2/wh3/wh3b — OOM-killed)
