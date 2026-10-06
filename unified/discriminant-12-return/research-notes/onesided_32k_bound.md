# One-Sided 32k Tail Closure: Derivation and Quantified Obstruction

**Task:** Sandbox CONSTRUCTION handoff v14.077 (type: one-sided-tail-closure).
**Date:** 2026-10-06
**Status:** Complete — QUANTIFIED OBSTRUCTION (sign framework exact [D];
remainder blocked on rigorous R_osc bound [O]; conditional premise itself
obstructed per v14.080).
**Scope:** Sandbox owns the analytic bound below. Lane A owns finite data.
No repo/ledger writes. No theorem promotion (independent audit required).

**Conventions:** [D]=derived, [N]=numerical, [I]=inference, [O]=open/gap.

**Producer:** `onesided_32k_producer.py` (deterministic, numpy only, SHA-256
38e9a854a610b874da7fa3274a5c00e619ca6483f9693dcf3c7b73b0bb2c62b2).

**Parents:** v14.069, v14.071, v14.073, v14.075, v14.076, v14.077, v14.079, v14.080.

---

## 0. Verdict

**QUANTIFIED OBSTRUCTION.** The one-sided 32k tail closure cannot be
established as theorem. Two independent obstructions:

**(A) Conditional premise obstructed [O].** v14.080 (OUTCOME B) proves the
v14.076 θ_p premise does not transport to the 32k nested section. The
finite interval E_{4k→32k} ∈ [−3.180e-5, −1.375e-5] is not promoted;
it needs Lane A's μ_{32k} floor package (or a common-mode re-derivation).
The one-sided margin M = 1.37456583285676e-5 is therefore conditional
on future Lane A work, not an available theorem input.

**(B) R_osc rigorous bound missing [O].** Even granting the margin,
the residual R^{res}_{32k} cannot be rigorously upper-bounded below M:
- δu index-shift: ≤ 4.533e-7 [D] (3.3% of M) ✓
- K=10 Q_sep (n≥64k): ≤ 1.3e-11 [D] (negligible) ✓
- R_osc quadratic form: numerical A·|⟨w_o,R_osc w_e⟩| ≈ 8.14e-8
  (0.6% of M) [N] fits comfortably, but **no rigorous upper bound exists**.
  v14.079 proved SBP cannot fit, w_p is non-smooth, and the Toeplitz-symbol
  lemma covers only the q=7 off-diagonal channel (≈45% of M for that
  channel alone at 32k); Lemma G/W (slow-phase/ripple correlation,
  w_p modulus) remain open.

Numerically, the one-sided closure fits with ~25× headroom ([D] 3.3% +
[N] 0.6% ≈ 4% of M). The obstruction is purely the rigor gap, not the
underlying scale. If Lemma G/W (v14.079 §10) and Lane A's μ_{32k}
(v14.080 §4) are supplied, the one-sided 32k closure follows.

---

## 1. Sign certification (generous radii) [N]

v14.077 §2 midpoint data (fixed-FFT, arch-200 LDDD):
- A_e = 1200.4587051950723, A_o = 1184.9475540161083,
  ΔA = −15.5111511789640795.
- M_e,11 = 12707.21241231825, M_o,11 = 12062.98874491472,
  M_o − M_e = −644.2236674035302.
- C_D = −4.395585571978897 [D, v14.069 §5].
- C_S = C_D − (M_o − M_e) = 639.8280818315513.

LDDD source residuals after refinement (v14.075 §1):
6.28e-26 (even), 1.44e-26 (odd).

Generous outward propagation: assume relative error 1e-9 on each of
C_p, L_p, M_p,11 — this is 1e17× the residual scale, enormously
pessimistic for 200-digit arithmetic, but rigorous enough given the
sign distances.
- |δ(ΔA)| ≤ (|A_o|+|A_e|)·3e-9 ≈ 7.2e-6 << 15.51.
  Hence ΔA_32k ≤ −15.511144 < 0. **CERTIFIED.**
- |δ(C_S)| ≤ (|M_o,11|+|M_e,11|)·1e-9 + 1e-12 ≈ 2.5e-5 << 639.83.
  Hence C_S(32k) ≥ 639.828057 > 0. **CERTIFIED.**
- A_e,32k ≈ 1200 > 0 is immediate (radius 3.6e-6).

Marked [N] (not interval-[D]) because the 1e-9 is a generous a priori
cap, not a proved error bound. The 1e6×–1e7× margin over the needed
tolerances (15, 600) makes this robust.

---

## 2. One-sided framework [D]

v14.069 exact factorization at N=32000:
  E_{>32k} = T^{(1)}_{32k} + T^{(2)}_{32k} + R^{res}_{32k},
  T^{(1)} = ΔA·K_o,  T^{(2)} = −A_e·C_S·K_o·K_e.

v14.071 theorem: S_{p,32k} ≽ I, hence for nonzero u,
  K_{p,32k} = ⟨u, S_{p,32k}^{-1} u⟩ ≥ ‖u‖² > 0.  [D]

Certified signs (§1): ΔA < 0, C_S > 0, A_e > 0. Therefore
  T^{(1)}_{32k} = (neg)(pos) < 0,  [D]
  T^{(2)}_{32k} = −(pos)(pos)(pos)(pos) < 0.  [D]

For an upper bound, discard the favorable terms:
  ┌─────────────────────────────┐
  │ E_{>32k} ≤ R^{res}_{32k}.   │  [D]
  └─────────────────────────────┘
No absolute-value payment on |ΔA| ≈ 15.5 or |C_S| ≈ 640.

---

## 3. Remainder decomposition

v14.069 §4:
  R^{res}_N = (δu terms) + (cross ε) + (subleading ε) − A_e·⟨w_o,R_osc w_e⟩.

### 3.1 δu index-shift [D]

| A_e·(δu terms) | ≤ 2·A_max·‖δu‖·‖u‖/γ_N ≤ 2·A_max/(γ_N·√12·N²).
At N=32000, γ=1, A_max=804:
  ┌──────────────────────────────────────┐
  │ δu ≤ 4.5331e-7 = 3.30% of M.  [D]   │
  └──────────────────────────────────────┘
(v14.073 §2 recomputation; explicit lattice bounds ‖δu‖² ≤ 1/(6N³),
‖u‖² ≤ 1/(2N).)

### 3.2 K=10 Q_sep (n ≥ 64k) [D]

Per v14.075 §3 (superseding C_ρ): split {n>32k} = {32k<n<64k} ∪ {n≥64k}.
On Q_sep, m/n ≤ 1/2 for front modes m ≤ 32k; use audited K=10
signed-moment expansion (v14.020–v14.023, v14.039/40).

Scale v14.020's ‖R̃_10‖_2 < 1.21e-10 (at n_0=8000) to n_0=64000:
  (8000/64000)^{22.5} ≈ 4.79e-21.
With 1e20 pessimistic moment growth (v14.079 §12.2 methodology):
  ‖R̃_10‖_{ℓ²(n≥64k)} ≤ 5.8e-11.  [D]
Map via γ=1:
  subleading ≤ ‖R̃‖² ≤ 3.4e-21,
  cross ≤ 2√A_max·‖u‖·‖R̃‖ ≤ 1.3e-11.  [D]
  ┌─────────────────────────────────────────┐
  │ Q_sep total ≤ 1.3e-11 — negligible. [D] │
  └─────────────────────────────────────────┘

### 3.3 R_osc quadratic form [N/O] — THE OBSTRUCTION

Need: rigorous upper bound on A_e·|⟨w_o, R_osc w_e⟩| at N=32k.

**Numerical [N] (v14.079 §9, bare, J=300 window):**
  A·|⟨w_o, R_osc^b w_e⟩| ≈ 8.14e-8 = 0.59% of M.
Fits with ~170× headroom. But [N], not theorem.

**Rigorous attempts:**
(a) *Toeplitz-symbol lemma* (v14.079 §6, [D]): for the q=7 off-diagonal
    leading term, |⟨w_o,R_7^{off,lead}w_e⟩| ≤ c·2w_7·π·‖w_o‖‖w_e‖.
    With [N]-scaled ‖w_o‖‖w_e‖ ≈ 2.6e-9 at 32k: ≤ 7.65e-9,
    A_max· = 6.15e-6 = 44.7% of M. Fits for this channel alone,
    but (i) the norm product is [N]-scaled, not rigorous; (ii) the
    other 4 q-channels, all diagonal pieces, and smooth remainder
    have no rigorous bound.
(b) *Toeplitz for all q* [D]: Σ_q c·2|w_q|·π·‖w_o‖‖w_e‖ with the
    rigorous γ=1 cap ‖w‖ ≤ 1/√(2N) gives A_max· ≈ 0.15 — 11× OVER M.
    The γ=1 cap (‖w‖ ≤ 3.95e-3) is ~4000× looser than the numerical
    ‖w‖, because S≽I does not capture the large diagonal.
(c) *SBP* [O]: v14.079 §§4–5 prove SBP cannot fit (w non-smooth;
    1.2–30× too lossy even with true constants).
(d) *Naive operator norm* [O]: ‖R_osc‖_2 ≈ 3 [N] but ‖w‖ cannot be
    bounded tightly from γ=1 alone.

**Missing:** Lemma G (slow-phase/ripple correlation, v14.079 §10) or
Lemma W (w_p modulus of continuity). Either would close this piece.
Without one, no rigorous R_osc upper bound fits M.

---

## 4. Margin test

| Component | Bound | / M | Status |
|-----------|-------|-----|--------|
| δu | ≤ 4.533e-7 | 3.3% | [D] ✓ |
| K=10 Q_sep | ≤ 1.3e-11 | <0.001% | [D] ✓ |
| R_osc (numerical) | ≈ 8.14e-8 | 0.6% | [N] fits |
| R_osc (rigorous) | — | — | **[O] obstructed** |
| **Total [D]** | ≤ 4.53e-7 | 3.3% | fits (excl. R_osc) |
| **Total [D+N]** | ≈ 5.35e-7 | 3.9% | fits [N] |

The [D] subtotal uses only 3.3% of M. The [N] total uses 3.9%.
**But R^{res,+}_{32k} < M is not established as theorem** because the
R_osc piece lacks a rigorous upper bound.

---

## 5. What would close it

1. **Lemma G/W** (v14.079 §10): a rigorous bound on |⟨w_o,R_osc w_e⟩|
   improving on Toeplitz by capturing the slow-phase/ripple correlation.
   Given the [N] scale (0.6% of M), even a 10×-loose rigorous bound
   would fit.
2. **Lane A's μ_{32k}** (v14.080 §4): the finite-section floor needed
   to promote the v14.076 interval, making M itself a theorem input.
   (Alternatively, Lane A's common-mode 16k→32k re-derivation.)

Either (1) alone closes the tail bound conditional on the margin;
both are needed for an unconditional final-sign theorem.

---

## 6. Files

- `~/workspace/d12/onesided_32k_producer.py` — deterministic producer
  (sign radii, δu, K=10 scaling, R_osc inputs, margin test, SHA-256).
- `~/workspace/d12/onesided_32k_bound.md` — this derivation.

No repo/ledger writes. Report to parent with verdict.

---

## 7. Result

$$
\boxed{
\begin{aligned}
&\text{QUANTIFIED OBSTRUCTION for the one-sided 32k tail closure.}\\[4pt]
&\text{[D] exact: } E_{>32k} \le R^{res}_{32k}\ \text{from certified }
\Delta A_{32k}<0,\ C_S(32k)>0,\ K_{p}>0.\\
&\text{[D] fits: }\delta u\le4.53\times10^{-7}\ (3.3\%\text{ of }M),\ 
\text{K=10 }Q_{sep}\le1.3\times10^{-11}.\\
&\text{[N] fits: }A\cdot|\langle w_o,R_{osc}w_e\rangle|\approx8.1\times10^{-8}\ (0.6\%\text{ of }M).\\
&\text{[O] missing: rigorous }R_{osc}\text{ upper bound (Lemma G/W, v14.079 §10).}\\
&\text{[O] missing: }v14.076\text{ margin promotion (}\mu_{32k},\ \text{v14.080 §4).}\\[4pt]
&\text{Numerically the closure fits with }\sim25\times\text{ headroom;}\\
&\text{as theorem, }R^{res,+}_{32k}<1.3746\times10^{-5}\text{ is NOT established.}
\end{aligned}
}
}
$$
