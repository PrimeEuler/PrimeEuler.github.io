# Cone Derivation Ledger v14.251 — Sandbox: v14.250 Audited; Infinite-Tail Action/RHS Consumer Derived

**Date:** 2026-10-10
**Track:** Sandbox / v14.250 handoff response
**Status:** [V] v14.250 audit: domain certificate verified (payload SHA, requires_finite_42_positive_power_moments=False, norms 1.45e-4/1.66e-3 match); 4R screen correctly flagged [N] (not a rigorous rejection); infinite seed honestly not claimed to meet 3e-5. [D] Infinite-tail consumers: RHS (B^* y_tail) via convergent moments (all j≥0); action (D y_tail) via split-sum with explicit 1/log n dominant bound; integral representation with t>83 moment / t≤83 direct split and interchange justification. The slow tail's 1/log n action decay is a fundamental limitation — the seed is admissible but needs correction before acceptance.
**Parents:** v14.213, v14.223, v14.238–250.
**Collision check:** live ledger max v14.250 (Lane A) at write time; v14.251 is next-free. No collision.

---

## 1. v14.250 audit [V]

**Domain payload:** infinite-diagonal-seed-domain.json verified.
requires_finite_42_positive_power_moments=False (explicit).
admissible_in_logarithmic_diagonal_domain=True.
Whole norm 1.451e-4/1.450e-4; log-diagonal norm 1.662e-3/1.660e-3.
Match v14.250 §3 displays. ✓

**Honesty:** residual_acceptance_met=False; action_evaluated=False;
trial_tail_numerically_evaluated=False. The entry does NOT claim
the seed works — only that it's admissible (in Domain(S), norm
<0.002). ✓

**4R screen:** Correctly flagged [N] exploratory. The 5e-4–7e-4
screen is a design warning, not a certified rejection. v14.248's
rejection of the Near-only trial remains the only rigorous
rejection. ✓

**Phi vs g:** §2 is explicit: Phi is the transported source
(for S*y=rho candidate), while any residual must use g-Dx with
bare g (v14.248). Correctly distinguished. ✓

## 2. RHS consumer: (B^* y_tail)_m [D]

For m≤R (front), n>2R (tail): n≥2m, so
1/(n±m)=Σ_{j≥0}(∓m)^j/n^{j+1} converges (ratio≤1/2).

(B^* y_tail)_m = Σ_{j<J} c_j·(±m)^j + Rem_J,
c_j = Σ_{n>2R} [kernel coeff]·y_tail(n)/n^{j+1}.

Convergence: |y_tail(n)|≤(C_Phi/11)·1/n, so
|y_tail(n)/n^{j+1}|≤(C_Phi/11)/n^{j+2}; Σ_{n>2R}1/n^{j+2}
converges for all j≥0. ✓

Remainder: |Rem_J|≤(1/2)^J/(1-1/2)·max|c_j|·(1+...). Explicit.

All c_j computable from Phi's rational W_j,A_j and 1/log(n/4)
quadrature (or the t-integral below). No moment divergence.

## 3. Action consumer: (D y_tail)_n [D]

For n>4R, split Σ_{m>2R}=A+B+C+(m=n):

- **m=n term:** d_n·y_tail(n). |d_n|≤log(n/4)+100, |y_tail|≤C/(n log n).
  Contributes O((log n)/(n log n))=O(1/n).

- **A (2R<m≤n/2):** |m/(n²-m²)|≤2/(3n).
  |A|≤(2/(3n))·Σ_{2R<m≤n/2}|y_tail(m)|
     ≤(2/(3n))·log(log(n/2)/log(2R)). Decays as (log log n)/n.

- **B (n/2<m<2n, m≠n):** |m/(n²-m²)|≤4/3 (using |n-m|≥1).
  |B|≤(4/3)·Σ_{n/2<m<2n}|y_tail(m)|≤(4/3)·C_1/log(n/2).
  Decays as 1/log n. **DOMINANT — very slow.**

- **C (m≥2n):** |m/(n²-m²)|≤4/(3m).
  |C|≤Σ_{m≥2n}(4/(3m))·|y_tail(m)|≤C_2/(n log n).

- **Pole:** α·p_n·P_tail, P_tail=Σ_{m>2R}p_m·y_tail(m) converges
  (|p_m y_tail|~1/(m² log m)). Contributes O(1/n).

- **z_m oscillatory:** In B, the factor z_m is retained inside
  the sum (not bounded by 8 separately); the 1/log n bound uses
  |z_m|<8 only for the final magnitude. The oscillatory phase is
  preserved in the exact sum.

**Total:** |(D y_tail)_n| ≤ C_B/log(n/2) + O((log log n)/n).
The 1/log n from region B dominates. This is certified but slow.

## 4. Integral representation [D]

1/log(m/4)=∫_0^∞(4/m)^t dt for m>4.
y_tail(m)=∫_0^∞4^t·Phi(m)·m^{-t}dt.
(D y_tail)_n=∫_0^∞4^t·(D Phi_t)_n dt, Phi_t(m)=Phi(m)m^{-t}.

- **t>83:** All 42 moments Σm^{2j}Phi_t(m) converge (need t>2j+1,
  max 83 for j=41). Use v14.243 moment expansion with HS remainder.
- **t∈[0,83]:** Use §3 split-sum bound (no moments needed).
- **Interchange:** Justified by ∫_0^∞4^t·|(D Phi_t)_n|dt<∞,
  since the split-sum bounds gain m^{-t} decay, integrable.

This gives an alternative certified consumer, but the 1/log n
limitation persists (it comes from the t→0 end).

## 5. Assessment

The infinite seed is **admissible** (v14.250 [V]) but its action
decays only as 1/log n — too slow for the 3e-5 target without
correction. The seed is a valid starting trial, not an accepted
solution. Lane A should:
1. Use the §2 RHS consumer to compute the new g=B^*y (finite+tail).
2. Solve the finite lift for the finite part; treat the tail via
   the §3/§4 action consumer.
3. Apply preconditioned corrections (the diagonal Lambda^{-1}
   is a natural preconditioner since y=Phi/Lambda).
4. Re-evaluate the residual with v14.248's consumer.

The 4R finite extension (v14.250 §1) screens poorly; the infinite
tail is the right direction, but it needs the correction step.

---

HANDOFF-ACK
from: v14.250
target: sandbox
status: closed
result: Domain certificate audited (verified). Infinite-tail RHS consumer via convergent moments; action consumer via split-sum with certified 1/log n bound; integral representation with interchange justification. Seed is admissible but requires correction before acceptance; 1/log n decay is a fundamental limitation of the slow tail.
constraints: None.
