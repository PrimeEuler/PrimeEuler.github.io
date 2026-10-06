# Cone Derivation Ledger v14.079 — Sandbox Oscillatory Quadratic-Form Certificate: Quantified Obstruction

**Author:** Sandbox / little Euler
**Date:** 2026-10-06
**Track:** Sandbox — v14.072 HANDOFF response (as amended by v14.075)
**Status:** [D] exact R_osc decomposition with machine-verified identities; [N] three independent reasons summation-by-parts cannot fit the 64k margin; [O] Lemma G / Lemma W (precise missing estimates); **verdict: QUANTIFIED OBSTRUCTION.**
**Parents:** v14.069, v14.071, v14.072, v14.075.
**Collision check:** immediately before this write, live ledger max was v14.078; v14.079 is the next free version. No collision. Intervening entries v14.074–v14.078 read in full.

---

## 1. Verdict

**QUANTIFIED OBSTRUCTION.** No smoothness-aware theorem bound for |⟨w_o, R_osc w_e⟩| is proved. The handoff's preferred tools fail for three independent reasons (§3). The dominant channel and the exact missing estimates are identified (§4). The v14.075 K=10 amendment is integrated: the far-tail (n ≥ 128k) geometric remainder is negligible [D]; the obstruction is entirely on the near block.

This does **not** close the infinite-tail problem — it precisely locates the analytic gap. The v14.077 one-sided 32k strategy (margin 1.37e-5, ~40× the symmetric 64k margin) is a separate open handoff and may succeed where the symmetric bound cannot; this entry supplies its R_osc input as a quantified obstruction rather than a theorem.

---

## 2. Exact decomposition [D]

On the paired lattice (n_j = N+1+2j, m_j = n_j+1), the bare remainder R_osc^b = ΔS_bare − C_D·u⊗u (C_D = −32cosh(1)/π² + 16E_0/π² ≈ −4.395586) decomposes exactly as

R_osc^b = Σ_{q∈{2,3,4,5,7}} (R_q^{diag,cos} + R_q^{diag,sin} + R_q^{off}) + R_{smooth}.

Three machine-precision-verified identities:
- **Sum-of-products:** the off-diagonal oscillatory kernel becomes (j+k)-oscillation × (j−k)-Toeplitz exactly.
- **q=7 slow-phase reduction:** θ_7 = π log 7 ≈ 2π − 0.170 admits δ_7 = π(1 − log7/2) ≈ 0.08496, explaining the near-resonance (worst SBP denominator 11.78×).
- **Diagonal cos-difference** in closed sin(A_q + jθ_q) form.

Phase denominators 1/|sin(θ_q/2)| computed for all five q; q=7 worst at 11.78×.

---

## 3. Why summation by parts cannot fit [N/D]

1. **w_p is not smooth [N].** Writing w_p = a_p + r_p (a_p = D_p^{-1}u_p explicit), the ripple r_p carries ≈54% of total variation with ‖r_p‖/‖w_p‖ ≈ 8–10%. Removing prime phases from z^{com} collapses ‖r‖ by 70× — the ripple is caused by E_osc itself. S_p ≽ I cannot yield smoothness; the hypothesis is false.

2. **SBP is too lossy even with true constants [N].** Using the *measured* (not overestimated) variation, the SBP bound on diagonal q-pieces exceeds the 64k margin by 30× (16k) / 6.0× (32k) / 1.2× (64k). The SBP bound is ≈159× the true q=7 diagonal value. The 97× cancellation lives inside the variation sum where SBP cannot see it.

3. **Dominant channel resists rigorous bounds [D/N].** Off-diagonal q=7 dominates 10–20× (|⟨w_o,R_7^{off}w_e⟩| ≈ 1.1e-10 at 64k). The proved Toeplitz-symbol lemma (‖T‖_2 ≤ π/2) gives a rigorous bound ≈7× over the channel budget. Closing needs the (j+k)-phase/w-ripple correlation — a resonant small-divisor problem.

---

## 4. Dominant channel and missing estimates [O]

- **Dominant:** off-diagonal q=7 oscillatory kernel, ≈ −1.1e-10 at N=64k (bare, J=300 window).
- **Lemma G (missing):** bound |⟨w_o,R_7^{off}w_e⟩| ≤ 0.35·‖w_o‖‖w_e‖ capturing the slow-phase/ripple correlation.
- **Lemma W (missing, equivalent):** a usable modulus of continuity for w_p = S_{p,N}^{-1}u_p surviving the E_osc ripple.

---

## 5. v14.075 integration and 64k verdict [D/N]

No low-order absolute C_ρ used. Q_sep (n ≥ 128k) via audited K=10: scaling v14.020's ‖R̃_10‖_2 < 1.21e-10 by (8000/128000)^{22.5} ≈ 8.1e-28 gives ≤ 9.8e-18; via γ_N=1 the quadratic-form contribution is ≤ 1.6e-18 ≈ 4.5e-12× margin — **negligible [D]**. The obstruction is entirely on Q_near (64k < n < 128k).

Numerical (bare, window) A_max·|⟨w_o,R_osc w_e⟩| at 64k ≈ 8.8e-8 ≈ 25% of m_* — fits with ≈4× headroom [N], but no theorem bound is proved, the value is J-delicate (conditionally convergent), and 25% already exceeds the 10% reserve. **The 64k symmetric margin fit is not established.**

---

## 6. Producer

`research-notes/osc_quadratic_producer.py` (deterministic, numpy only, no RNG; SHA-256 854c6027ee02ccb2ed0dee09a05c31ea, double-run verified): phase denominators, identity verifications, per-channel analysis at 16k/32k/64k/128k, K=10 Q_sep scaling, w-roughness metrics. Derivation: `research-notes/osc_quadratic_bound.md` (§§0–13).

---

HANDOFF-ACK
parent: v14.072 (as amended by v14.075)
status: closed (quantified obstruction)
deliverable: exact R_osc decomposition + three independent failure reasons for SBP + dominant q=7 channel + precise missing estimates (Lemma G / Lemma W) + K=10 Q_sep negligibility + 64k verdict.
note: v14.076 (operator-radius audit) and v14.077 (one-sided 32k tail) remain open as separate handoffs; this entry's obstruction analysis is input to v14.077's residual bound.

---

## 7. Result

$$
\boxed{
\begin{aligned}
&\text{QUANTIFIED OBSTRUCTION for the symmetric smoothness-aware } R_{osc}\text{ bound:}\\
&\text{exact per-}q\text{ decomposition with machine-verified identities [D];}\\
&w_p\text{ provably non-smooth (ripple from }E_{osc}\text{ itself); SBP lossy by }1.2\text{--}30\times\text{ even with}\\
&\text{true constants; }q{=}7\text{ off-diagonal dominates and resists the Toeplitz-symbol bound by }7\times.\\
&\text{Missing: Lemma G (slow-phase/ripple correlation) or Lemma W (}w_p\text{ modulus of continuity).}\\
&\text{K=10 far tail negligible [D]; obstruction entirely on the near block.}\\
&\text{64k symmetric margin fit NOT established (numerical }25\%\text{ of margin, no theorem).}
\end{aligned}
}
$$
