# Cone Derivation Ledger v14.073 — γ_N=1 Enclosure Update and 32k/64k Admissible Budgets

**Author:** Sandbox / little Euler
**Date:** 2026-10-06
**Track:** Sandbox — v14.071 theorem-input-update HANDOFF response
**Status:** [D] conditional enclosure constants recomputed with the theorem input γ_N=1 (v14.071); [N] feasibility budgets at 32k/64k from the diagonal K; [O] Lane A's 32k/64k ΔA_N, C_S(N), C_ρ still pending.
**Parents:** v14.069, v14.070, v14.071, v14.072.
**Collision check:** immediately before this write, live ledger max was v14.072; v14.073 is the next free version. No collision. Intervening entries v14.070–v14.072 read in full.

---

## 1. What v14.071 changes

v14.071 promotes, by nested exact Schur complementation from v14.044/v14.046,

$$
\boxed{S_{p,N} \succeq I \quad \text{for every } N \ge 4000,\ p \in \{e,o\}}
$$

i.e. the v14.069 conditional theorem (hypothesis (iii)) may now take the **theorem** value

$$
\boxed{\gamma_N = 1}
$$

replacing the exploratory numerical diagonal/window value γ ≈ 6.38. This closes the γ_N ask structurally. All enclosure constants below are recomputed with γ_N = 1; nothing else in the v14.069 framework changes.

Consequence to flag honestly: the rigorous γ = 1 makes every γ-dependent *coarse* remainder bound 6.38× looser than the exploratory-γ version. The δu index-shift remainder, previously "rigorously ≤ 2.8e-7 at 16k, below the margin on its own," is now the binding constraint (§3).

---

## 2. Updated theorem constants (γ_N = 1) [D]

Margin m_* = 3.45557892442104e-7, A_max = 804. Explicit lattice bounds used throughout:
‖u‖² = Σ_j 1/n_j² ≤ 1/(2N); ‖δu‖² = Σ_j 1/(n_j²m_j²) ≤ 1/(N⁴) + 1/(6N³) ≤ 1.0004/(6N³) (N ≥ 16000).

| N | K^{up}_N = 1/(2N) | δu coarse = 2A_max/(√12·N²) | δu / m_* | cross coeff. (×√C_p·C_ρ) | subleading coeff. (×C_p·C_ρ²) |
|---|---|---|---|---|---|
| 16k | 3.125e-5 | 1.813e-6 | 5.25× | 8.76e-7 (2.53×) | 7.63e-12 |
| 32k | 1.563e-5 | 4.533e-7 | 1.31× | 2.35e-7 (0.68×) | 1.10e-12 |
| 64k | 7.813e-6 | 1.133e-7 | 0.328× ✓ | 6.26e-8 (0.18×) | 1.56e-13 |
| 128k | 3.906e-6 | 2.833e-8 | 0.082× ✓ | — | — |

Formulas (v14.069 §7 with γ_N = 1):
- K^{up}_N = (1/γ_N)(1/(2N)) — the coarse theorem bound on K_{p,N} = ⟨u, S_{p,N}^{-1}u⟩.
- |A_e(δu terms)| ≤ 2·A_max·‖δu‖·‖u‖/γ_N ≤ 2·A_max/(γ_N·√12·N²).
- |cross| ≤ 2·√A_max·‖u‖·‖ε‖/γ_N, ‖ε‖ ≤ √C_p·C_ρ·(log N)/√(3N³).
- |subleading| ≤ ‖ε‖²/γ_N.

Producer: `~/workspace/d12/gamma1_budget_update.py` (deterministic, reproduces this table).

---

## 3. Admissible budgets

### N = 64k — fits (feasibility, diagonal K = 7.42e-7)

After reserving the coarse δu remainder (1.133e-7, 32.8% of margin), 2.322e-7 remains for T^{(1)} + T^{(2)} + cross + subleading + R_osc. With a 35%/50%/15% split:

$$
\boxed{|\Delta A_{64k}| < 0.11, \qquad |C_S^{paired}(64k)| < 262}
$$

i.e. |ΔA| < 8.13e-8/7.42e-7 and |C_S| < 1.16e-7/(804·(7.42e-7)²). The 15% reserve (3.5e-8) covers cross (6.3e-8·√C_p·C_ρ — needs C_ρ ≲ 0.5 if C_p ∼ 1) and leaves the R_osc slot for the v14.072 construction. Subleading is negligible (∼1e-13·C_p·C_ρ²).

These relax the v14.069 §6 "implausible" 16k requirements (|ΔA| < 0.029, |C_S| < 26.6) by ∼4× and ∼10× respectively, and sit near the earlier 64k feasibility sketch (|ΔA| < 0.135, |C_S| < 565) — now with the δu reserve made explicit and γ_N = 1 rigorous.

### N = 32k — does NOT fit with coarse bounds

The coarse δu remainder alone is 4.533e-7 = 1.31× the margin. **No admissible (ΔA, C_S) budget exists at 32k within the current coarse enclosure.** The δu index-shift bound is the binding constraint, not the T^{(1)}/T^{(2)} terms.

---

## 4. Headroom note (not a theorem) [N/I]

The coarse δu bound is ∼500× loose against numerics: the window computation gives K_o − K_e = 6.82e-10, while the coarse δu + R_osc machinery budgets ∼4.5e-7 at 32k. The δu_j = −1/(n_j·m_j) terms have explicit fixed sign and the paired quadratic forms exhibit the 97× smoothness cancellation — both are exactly what the v14.072 smoothness-aware construction is designed to capture. If v14.072 produces a theorem R_osc^{max}(N) (and, by the same techniques, a sharpened δu bound), 32k may re-enter. With only the coarse bounds, **64k is the first cutoff where the rigorous-γ enclosure fits inside the margin.**

---

## 5. What remains open (unchanged ownership)

- ΔA_N, C_S^{paired}(N) at 32k/64k — Lane A's fixed-FFT producer (running; do not consume until recorded complete).
- C_ρ — needed to close the cross term (currently parametric; small iff C_ρ ≲ 1).
- R_osc^{max}(N) — the v14.072 sandbox construction (dispatched).

No finite-cutoff stabilization inference is made. No theorem promotion without independent audit.

---

HANDOFF-ACK
parent: v14.071
status: closed
deliverable: conditional enclosure constants updated to γ_N = 1 (table §2, producer gamma1_budget_update.py); admissible budgets |ΔA_{64k}| < 0.11, |C_S(64k)| < 262 reported (§3); 32k quantified as not fitting with coarse bounds (§3–§4).
note: the v14.072 R_osc construction is separately dispatched and will be ledgered on completion.

---

## 6. Result

$$
\boxed{
\begin{aligned}
&\text{Enclosure updated to the theorem input } \gamma_N = 1\ (N \ge 4000).\\
&\text{Coarse remainder bounds are 6.38}\times\text{ looser than the exploratory-}\gamma\text{ version;}\\
&\text{the }\delta u\text{ index-shift term is now the binding constraint:}\\
&\quad 16k:\ 5.25\times\text{ margin (out)},\quad
32k:\ 1.31\times\text{ margin (out)},\quad
64k:\ 0.33\times\text{ margin (fits)}.\\[4pt]
&\text{Admissible 64k budgets (diagonal }K\text{, after }\delta u\text{ reserve): }
|\Delta A| < 0.11,\ |C_S| < 262.\\
&\text{No admissible 32k budget exists with coarse bounds.}\\
&\text{Numerical headroom (}K_o - K_e = 6.82\times10^{-10}\text{) suggests the v14.072}\\
&\text{smoothness construction may recover 32k; with coarse bounds alone, 64k is first.}
\end{aligned}
}
$$
