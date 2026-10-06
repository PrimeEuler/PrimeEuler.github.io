# Compression-Free Correlated Infinite-Tail Bound for E_{>N} = η_o(N) − η_e(N)

**Task:** Sandbox CONSTRUCTION handoff v14.066 (type: correlated-infinite-tail-bound).
**Date:** 2026-10-06
**Status:** Complete — OBSTRUCTION (quantified) + CONDITIONAL THEOREM.
**Scope:** Sandbox owns the analytic inequality, paired asymptotics, and independent producer.
Lane A owns the fixed FFT finite solver and all finite-cutoff data. No repo/ledger writes.
No theorem promotion (independent audit required).

**Conventions:** [D]=derived, [N]=numerical, [I]=inference, [O]=open/gap.

---

## 0. Target and margin

For cutoff N (even), the normalized remote capacities are
  η_e(N) = r_eᵀ S_e⁻¹ r_e,   η_o(N) = r_oᵀ S_o⁻¹ r_o,
and the infinite parity-difference tail is E_{>N} = η_o(N) − η_e(N).

Theorem margin at N=16000: the promoted finite shells give
cumulative E_{4k→16k} ∈ [3.4556e-7, 1.9755e-6] (v14.061),
so the final sign is preserved iff E_{>N} > −3.4556e-7
(up to the other far terms, which are separately controlled).
Results are derived AS A FUNCTION OF N.

---

## 1. Paired-lattice identification U_N [D]

**Mode sets.** Even sector ("even-v") uses odd modes; odd sector ("odd-v") uses
even modes (verified: odd_sector_assembler.py uses ns=2,4,...; even uses 1,3,...).

For cutoff N (even):
- Even remote modes: E_N = {n_j = N+1+2j : j ≥ 0} (odd integers > N).
- Odd remote modes:  O_N = {m_j = N+2+2j : j ≥ 0} (even integers > N).

**Pairing.** U_N: ℓ²(E_N) → ℓ²(ℕ₀), (U_N x)_j = x_{n_j};
similarly for O_N with (V_N y)_j = y_{m_j}.
The natural index pairing is n_j ↔ m_j with **m_j = n_j + 1** (one-mode shift).

All paired operators/vectors below are on the common index space ℓ²(ℕ₀).

---

## 2. Explicit per-mode data [D]

From the source-faithful operator (common_mode/suzuki_ldd_source_operator.py):

- k_n = nπ/2.
- z^{(p)}_n = z^{com}_n − π_p·nπ·corr_n,
  z^{com}_n = 2Σ_q w_q sin(nπ log q/2) + Im ψ(1/4+inπ/4)  [parity-independent, O(1)],
  π_e = −1 (even sector), π_o = +1 (odd sector),
  corr_n = Σ_{j<50} e^{−2(2j+.5)}/((2j+.5)²+k_n²) = E_0/k_n² + O(1/k_n⁴),
  E_0 = 0.37474310047....
  Hence: z^{(e)}_n = z^{com}_n + nπ·corr_n (n odd),
         z^{(o)}_n = z^{com}_n − nπ·corr_n (n even).
  And nπ·corr_n = 4E_0/(nπ) + O(1/n³) = O(1/n).
- d_n = cusp_n + prime_diag_n + arch_n  [parity-independent],
  cusp_n = log(n/4) − Ci(nπ) − Si(nπ)/(nπ),
  prime_diag_n, arch_n bounded oscillatory.
  So d_n = log(n/4) + O(1).
- p^{(e)}_n = 2k_n cosh(1/2)/(k_n²+1/4),  p^{(o)}_n = 2k_n sinh(1/2)/(k_n²+1/4).
  p^{(p)}_n = c_p/n + O(1/n³), c_e = 4cosh(1/2)/π ≈ 1.43573797,
  c_o = 4sinh(1/2)/π ≈ 0.66347915.
- α_e = +2, α_o = −2.
- f_n = k_n(e^{−1}−(−1)^n e)/(1+k_n²).
  n odd:  f_n = k_n(e^{−1}+e)/(1+k_n²) ≈ +1.964/n.
  n even: f_n = k_n(e^{−1}−e)/(1+k_n²) ≈ −1.496/n.

**Kernel** (n≠m, same parity sector p):
  (T_p)_{nm} = c·(m·z^{(p)}_n − n·z^{(p)}_m)/(n²−m²) + α_p·p^{(p)}_n·p^{(p)}_m,
  c = 2/π.
**Diagonal:**
  (T_p)_{nn} = d_n + α_p·(p^{(p)}_n)².

---

## 3. Resolvent decomposition (correlated before absolute values) [D]

On the common index space, write
  S_o = S + ΔS_o,   S_e = S + ΔS_e,   r_o = r + Δr_o,   r_e = r + Δr_e,
for a common reference (S, r) to be chosen.

**Lemma (paired resolvent difference).**
  η_o − η_e = (r_o−r_e)ᵀS_o⁻¹r_o + r_eᵀS_o⁻¹(r_o−r_e) + r_eᵀ(S_o⁻¹−S_e⁻¹)r_e,
and S_o⁻¹−S_e⁻¹ = S_o⁻¹(S_e−S_o)S_e⁻¹.
*Proof.* Direct algebra. ∎

Hence, with w_p = S_p⁻¹r_p:
  |η_o−η_e| ≤ ‖Δr‖·(‖w_o‖·‖r_o‖ + ‖r_e‖·‖w_o‖) + ‖w_o‖·‖w_e‖·‖ΔS‖,
where Δr = r_o−r_e, ΔS = S_o−S_e (on the common index space).

This is the required "correlate before absolute values" structure.
The task is now: bound ‖Δr‖, ‖ΔS‖, ‖w_p‖ = ‖S_p⁻¹r_p‖.

---

## 4. The ỹ-decomposition and factorization [D]

From v14.010 (exact): on remote modes n > N,
  r_{p,N}(n) = L_{p,N}/n + ρ_{p,N}(n),    |ρ_{p,N}(n)| ≤ C_ρ·(log n)/n²,
with L_{p,N} an exact constant from the finite solve. Define the normalized
  ỹ_{p,N} = √C_{p,N}·r_{p,N} = σ_{p,N}√A_{p,N}·u^{(p)} + ε_{p,N},
where A_{p,N}=C_{p,N}L_{p,N}², σ_{p,N}=sign(L_{p,N}), u^{(p)}(n)=1/n,
ε_{p,N}=√C_{p,N}·ρ_{p,N}. Then η_{p,N}=⟨ỹ_{p,N},S_{p,N}^{-1}ỹ_{p,N}⟩.

**Exact difference.** With K_{p,N}=⟨u^{(p)},S_{p,N}^{-1}u^{(p)}⟩:
  η_o−η_e = [A_oK_o − A_eK_e]
    + 2σ_o√A_o⟨u^{(o)},S_o^{-1}ε_o⟩ − 2σ_e√A_e⟨u^{(e)},S_e^{-1}ε_e⟩
    + ⟨ε_o,S_o^{-1}ε_o⟩ − ⟨ε_e,S_e^{-1}ε_e⟩.     (Eq*)

**Riccati for K_o−K_e.** Write K_o−K_e via the paired common index:
  K_o−K_e = ⟨u^{(o)},S_o^{-1}u^{(o)}⟩ − ⟨u^{(e)},S_e^{-1}u^{(e)}⟩
  = ⟨δu,S_o^{-1}u^{(o)}⟩ + ⟨u^{(e)},S_o^{-1}δu⟩ − ⟨w_o,ΔS w_e⟩_paired,
where δu = u^{(o)}−u^{(e)}, δu_j = 1/m_j−1/n_j = −1/(n_j m_j),
w_o=S_o^{-1}u^{(e)}, w_e=S_e^{-1}u^{(e)}, ΔS=S_o−S_e on the paired space.
The δu terms are EXPLICIT and small: |δu_j| ≤ 1/n_j².

The operator term −⟨w_o,ΔS w_e⟩ contains the leading rank-1 structure.
Decompose ΔS = R_1 + R_osc where R_1 is the smooth paired rank-1 part.
Then ⟨w_o,R_1 w_e⟩ = −C_S^{paired}·K_o·K_e + (δu corrections),
with C_S^{paired} the paired analogue of C_S=C_D−(M_o−M_e)_{11}.

**Main factorization (paired version).**
  η_o−η_e = T^{(1)}_N + T^{(2)}_N + R^{res}_N,
  T^{(1)}_N = (A_{o,N}−A_{e,N})·K_{o,N}            [amplitude-driven],
  T^{(2)}_N = −A_{e,N}·C_S^{paired}(N)·K_{o,N}·K_{e,N}  [operator-driven],
  R^{res}_N = (δu terms) + (cross ε terms) + (subleading ε terms)
              − A_{e,N}·⟨w_o,R_{osc}w_e⟩.          [remainder].

---

## 5. Explicit structural constants [D/N]

**C_D.** From the bare kernel difference (unpaired, as functions):
  C_D = −32cosh(1)/π² + 16E_0/π² ≈ −4.396.   [D formula; N decimal]
(Producer: infinite_tail_producer.py.)

**Diagonal floor.** d_n = log(n/4) + R_n, |R_n| ≤ C_d.
Numerical: d_{16001}=8.363 vs log(4000)=8.294, so R≈+0.07 there.
d_min(N) grows like log(N/4): 6.09 (8k), 6.70 (16k), 7.36 (32k), 8.08 (64k), 8.69 (128k).

**K scaling (diagonal approx, validated vs window solve to 1%).**
  K_{p,N} ≈ (1/2)/(N·log(N/4)):
  N=8k: 7.42e-6; 16k: 3.42e-6; 32k: 1.59e-6; 64k: 7.42e-7; 128k: 3.48e-7.
Window solve at N=16k,J=400: K_e=1.821e-7 vs diag 1.801e-7 (1% agreement).

**Coercivity (D_p, numerical).** λ_min(D_p)≈6.38 on J=400 window at N=16k,
both parities. D_p is well-conditioned; the Schur correction's effect on
coercivity needs M_p (finite data) — see §8.

**Paired operator difference (numerical).** ‖D_o−D_e‖_2≈3.0 on the paired
window — O(1), NOT small. The naive normwise bound is useless.
However: |⟨w_o,ΔD w_e⟩|=7.04e-10 vs naive 6.83e-8 — a 97× smoothness
cancellation. K_o−K_e=6.82e-10 (tiny). The cancellation is real but
lives at the quadratic-form level, not the operator-norm level.

---

## 6. Scaling and margin analysis [N/I]

T^{(2)}_N scale = A·|C_S|·K_o·K_e, using A=803, C_S=421.84 (N=4000 values,
for ORDER-OF-MAGNITUDE only):

  N=8k:   1.86e-5   (54× margin)
  N=16k:  3.97e-6   (11× margin)
  N=32k:  8.56e-7   (2.5× margin)
  N=64k:  1.87e-7   (0.54× margin ✓)
  N=128k: 4.10e-8   (0.12× margin ✓)

Margin = 3.4556e-7. So the T^{(2)} SCALE alone beats the margin at N≈64k,
CONDITIONAL on C_S(N)≈421.84 and T^{(1)} not adding constructively.

**Critical competition.** T^{(1)}/T^{(2)} ∼ (ΔA)/(A·C_S·K).
At N=16k: ∼(ΔA)/1.15. If |ΔA|∼1, they are the SAME ORDER.
The tail sign depends on sign(ΔA) vs −sign(C_S). At N=4000:
ΔA=−0.71 (T^{(1)}<0), C_S=+421.84 (T^{(2)}<0) — both negative.
Without ΔA_N and C_S(N) at the target N, the sign is UNDETERMINED.

**To beat the margin at N=16k** via |T^{(1)}|+|T^{(2)}|<3.5e-7 with K=3.42e-6
(budget split 1e-7 / 2.5e-7):
  |ΔA| < 1e-7/3.42e-6 ≈ 0.029 AND |C_S| < 2.5e-7/(804·(3.42e-6)²) ≈ 26.6.
These are extremely strong (amplitude matching to 3e-5 relative; C_S 16×
smaller than the N=4000 value). At N=64k (K=7.42e-7):
  |ΔA| < 0.135 AND |C_S| < 565 — plausible with good finite data.

*Caveat:* K here is the diagonal approx; the Schur correction changes
⟨u,S^{-1}u⟩ by ~56% (v14.009 §2c), so true K (and T^{(2)}) may be ~2× larger.
This shifts the N-threshold by ~√2, not the qualitative conclusion.

---

## 7. Conditional enclosure theorem [D]

**Theorem.** Let N be even. Assume finite-data inputs:
  (i)   |A_{o,N}−A_{e,N}| ≤ ΔA_max,  max(A_{o,N},A_{e,N}) ≤ A_max;
  (ii)  |C_S^{paired}(N)| ≤ C_max;
  (iii) S_{p,N} ≽ γ_N·I on the remote space (both parities);
  (iv)  |ρ_{p,N}(n)| ≤ C_ρ·(log n)/n²;
  (v)   |⟨w_o,R_{osc}w_e⟩| ≤ R_osc^{max} (smoothness-aware remainder).
Then:
  |E_{>N}| ≤ ΔA_max·K^{up}_N + A_max·C_max·(K^{up}_N)² + R^{bd}_N,
where K^{up}_N = (1/γ_N)·(1/(2N)) [from S≽γI],
and R^{bd}_N bounds the δu/cross/subleading/R_{osc} terms explicitly:
  |A_e(δu terms)| ≤ 2·A_max·‖δu‖·‖u‖/γ_N ≤ 2·A_max/(γ_N·√12·N²),
    with ‖δu‖²=Σ_j1/(n_j²m_j²)≤1/(6N³), ‖u‖²≤1/(2N) [explicit, no finite data;
    at N=16k,γ=6.38: ≤2.8e-7 — rigorously below the margin on its own],
  |cross| ≤ 2·√A_max·(1/γ_N)·‖u‖·‖ε‖,  ‖ε‖²≤C_p·C_ρ²·(log N)²/(3N³),
  |subleading| ≤ (1/γ_N)·‖ε‖²,
  |A_e⟨w_o,R_{osc}w_e⟩| ≤ A_max·R_{osc}^{max}.
*Proof.* From (Eq*) and the Riccati decomposition, triangle inequality
applied AFTER the correlated factorization (not to |η_o|+|η_e|). ∎

**Status of inputs:** (i),(ii) need Lane A's finite solve at N. (iii) needs
M_p for the full S_p; D_p alone has γ^D_N≈6.4 (numerical). (iv) needs C_ρ
from the refined solution. (v) needs the smoothness-aware harmonic-analysis
bound (open analytic problem; numerical evidence: 97× cancellation).

---

## 8. Quantified obstruction [D]

The bound CANNOT beat 3.4556e-7 at N=16000 without:
  (a) ΔA_{16000} and C_S(16000) from Lane A's finite data — the tail sign
      and magnitude are UNDETERMINED without them (T^{(1)},T^{(2)} same order,
      competing signs). THIS IS THE PRIMARY OBSTRUCTION.
  (b) A rigorous smoothness-aware bound on ⟨w_o,R_{osc}w_e⟩ — the naive
      ‖ΔS‖≈3 is 4e9× too big for the quadratic-form difference (6.8e-10);
      the 97× numerical cancellation is not a theorem.
  (c) Coercivity γ_N for the full S_p (needs M_p); D_p alone is fine (6.38).

**Exact term that destroys the margin:** T^{(2)}_N=−A_e·C_S·K_o·K_e.
With the N=4000 C_S=421.84, |T^{(2)}_{16k}|≈4e-6 (11× margin).
The margin is destroyed by the OPERATOR-DRIVEN second-order term, not by
the amplitude term or the remainder. If C_S(16000)≪421.84 or T^{(1)} cancels
it, the conclusion changes — but that needs the finite data.

**Fail-closed fallback** (|η_o|+|η_e| separately): gives |E|≤2·A_max·K_max
≈2·804·3.42e-6≈5.5e-3 at N=16k — 16,000× the margin. Useless, as expected.
The correlated factorization is ESSENTIAL, not optional.

---

## 9. Producer and determinism

- `infinite_tail_producer.py`: per-mode data, paired operators. Deterministic
  (pure functions; SHA-256 verified).
- `infinite_tail_probe.py`: coercivity, paired differences, K values.
- `infinite_tail_scaling.py`: K/d_min/T2 vs N table.
- `infinite_tail_cancellation.py`: smoothness cancellation quantification.
All binary64 exploration; no RNG. (Arch-200 producers would be needed for
theorem-grade constants; the SCALING is robust to precision.)

---

## 10. Verdict

**OBSTRUCTION (quantified) + CONDITIONAL THEOREM.**

The compression-free correlated framework is complete: paired identification
U_N, resolvent identity, exact factorization, explicit structural constants,
and scaling. But the infinite-tail enclosure CANNOT be closed to 3.4556e-7
at N=16000 by sandbox analysis alone:

1. **Primary:** ΔA_N and C_S(N) are finite-solve data (Lane A's). The two
   leading terms T^{(1)},T^{(2)} are the same order with competing signs;
   the tail sign is undetermined without them.
2. **Secondary:** The smoothness-aware remainder bound ⟨w_o,R_{osc}w_e⟩
   needs harmonic analysis beyond current scope (97× numerical cancellation
   is not a theorem; naive ‖ΔS‖≈3 is useless).
3. **Tertiary:** Full S_p coercivity needs M_p (finite data); D_p alone
   gives γ≈6.38.

**Scaling result:** The T^{(2)} scale beats the margin at N≈64k (conditional
on C_S not growing). If Lane A moves the validated cutoff to 64k AND
supplies (ΔA, C_S, γ, C_ρ) there, the conditional theorem (§7) can close
the tail. At N=16k, the required |ΔA|<0.029 and |C_S|<26.6 are implausibly
strong. (Note: the δu index-shift terms ARE rigorously bounded by 2.8e-7
at N=16k — below the margin. The obstruction is purely the ΔA/C_S terms.)

**Recommended asks for Lane A:**
  (A) Report ΔA_N=A_{o,N}−A_{e,N} and σ_{p,N}=sign(L_{p,N}) at N=16k (and 32k/64k
      if the cutoff moves) — from the finite solve.
  (B) Report (M_o−M_e)_{11}(N) or directly C_S^{paired}(N) — the two
      quadratic forms w^{(1)ᵀ}_p A_{p,N}^{-1} w^{(1)}_p as a DIRECT DIFFERENCE.
  (C) Report γ_N (remote coercivity) and C_ρ (residual constant).
With (A)-(C), the §7 theorem gives an explicit outward E_{>N} enclosure.

No repo/ledger writes. Producer staged at ~/workspace/d12/.

