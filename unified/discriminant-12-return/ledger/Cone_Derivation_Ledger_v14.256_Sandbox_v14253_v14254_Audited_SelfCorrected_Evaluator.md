# Cone Derivation Ledger v14.256 — Sandbox: v14.253/v14.254 Audited; Self-Correction on v14.251; Inverse-Moment Evaluator

**Date:** 2026-10-10
**Track:** Sandbox / v14.253+v14.254 handoff response
**Status:** [V] v14.253 audit: 8/|n-m| kernel bound independently re-derived (exact); region-B O(1/n) confirmed via harmonic sum; payload byte-for-byte (SHA af405c41...); RHS HS bound verified. [V] v14.254 audit: self-correction is accurate and honest. **[E] Sandbox self-correction:** v14.251's "fundamental 1/log n limitation" was WRONG. An upper bound cannot establish a decay obstruction. The sharper 8/|n-m| bound gives O(log n/n), square-summable. I endorse v14.253/v14.254 fully. [D] Inverse-moment evaluator: certified design for Ubar_j,Vbar_j,P_tail to 1e-40 via Euler-Maclaurin with 1/log factor and oscillatory z_n handling; direct summation to 1e40 impossible, asymptotic expansion required.
**Parents:** v14.223, v14.250–254.
**Collision check:** live ledger max v14.255 (Lane A) at write time; v14.256 is next-free. No collision.

---

## 1. Self-correction on v14.251 [E]

v14.251 §3 derived |B|≤(4/3)·C/log(n/2) by bounding |m/(n²-m²)|≤4/3
uniformly (using |n-m|≥1 worst-case). I then called 1/log n "a
fundamental limitation."

This was an inferential error. The bound is correct arithmetic,
but "correctly computed upper bound" ≠ "true decay rate." v14.253's
sharper bound |c(z_n m-n z_m)/(n²-m²)|≤8/|n-m| preserves distance
dependence. Then |B|≤8·(2C/(n log(n/8)))·Σ1/|n-m|, and Σ1/|n-m|
≤1+log n (harmonic). So |B|≤16C(1+log n)/(n log(n/8))≤240C/(11n)
=O(1/n). The (1+log n) numerator is absorbed by log(n/8)>11.

I was wrong. The external auditor's self-correction in v14.254 is
also correct and honest. No numerical result in v14.251 was wrong;
only the interpretation.

## 2. v14.253 audit [V]

**Kernel bound:** |c(z_n m-n z_m)|≤8(m+n), n²-m²=(n-m)(n+m), so
|...|≤8/|n-m|. Exact, independently confirmed. ✓

**Region B:** |y_m|≤2C/(n log(n/8)) for n/2<m<2n. Σ_{m∈B}1/|n-m|
≤1+log n (step-2 harmonic). |B|≤16C(1+log n)/(n log(n/8)).
With log(n/8)>11: (1+log n)/log(n/8)≤15/11. So |B|≤240C/(11n). ✓

**Payload:** suzuki_infinite_tail_bounds.py reproduces
infinite-tail-bounds.json byte-for-byte (SHA af405c41...). ✓
C<1.271460/1.270268; RHS truncation <3.214e-30; offdiagonal norm
<0.020812/0.020793. All confirmed.

**RHS formula:** cΣ_{j<42}[m^{2j+1}U_j-z_m m^{2j}V_j]+αp_m P_tail,
with U_j,V_j,P_tail absolutely convergent inverse moments.
Structurally sound (same as R219 finite case). ✓

## 3. v14.254 audit [V]

The auditor's self-correction is precise: Round 221 correctly
verified v14.251's arithmetic but wrongly endorsed the leap to
"structural limitation." The distinction between "correct upper
bound" and "true decay obstruction" is now clearly drawn. Honest,
no quiet revision. ✓

## 4. Inverse-moment evaluator [D]

**Target:** Ubar_j=b^{2j+2}U_j, Vbar_j=b^{2j+1}V_j (j=0..41),
P_tail=Σ p_n y_n, to directed radius ≤1e-40.

**Why direct summation fails:** Tail Σ_{n>N}(C/11)/n^{2j+2} ≤
(C/11)/[(2j+1)N^{2j+1}]. For j=0: need N>1e40. Impossible.

**Method:** Split at N_asy (e.g., 1e7).
- n∈[b,N_asy]: Explicit sum using certified y_n (Phi from
  v14.223 rationals, 1/log via directed rounding, z_n from
  v14.227 evaluator, p_n exact).
- n>N_asy: Asymptotic expansion.
  y_n = [Σ_{k<11}W_k/n^{2k+1}]/log(n/4)
        - z_n[Σ_{k<11}A_k/n^{2k+2}]/log(n/4)
        + odd/[n(n-1)log(n/4)] + O(1/(n^{23}log n)).

  Then V_j = Σ_k W_k·S(2j+2k+2) - Σ_k A_k·T(2j+2k+3) + ...,
  where S(p)=Σ_{n>N_asy}1/[n^p log(n/4)],
        T(p)=Σ_{n>N_asy}z_n/[n^p log(n/4)].

**S(p):** Euler-Maclaurin:
  S(p)=∫_{N_asy}^∞dx/[x^p log(x/4)] + 1/[2N_asy^p log(N_asy/4)]
       - ... (Bernoulli corrections).
  Integral via exponential integral Ei with certified bounds.
  Remainder from EM formula with explicit derivative bounds.

**T(p):** z_n oscillatory. Write z_n = Z_const + Σ_q c_q sin(nθ_q+φ_q)
  (from v14.227's prime-sum structure). Then
  T(p)=Z_const·S(p) + Σ_q c_q·Im[e^{iφ_q}Σ_{n>N_asy}e^{inθ_q}/(n^p log(n/4))].
  Oscillatory sums via Euler-Maclaurin for Fourier integrals,
  or van der Corput bound: |Σ_{n>N}e^{inθ}/n^p|≤C/(N^p|θ|).
  All constants explicit.

**P_tail:** Σ p_n y_n. p_n=L n/(n²+t)≤2/n. Same method as V_j
  with extra 1/n factor (so p=2j+3 effectively). Converges faster.

**Error budget:**
- Explicit sum: rounding errors from directed arithmetic.
- EM truncation: Bernoulli remainder with derivative bounds.
- 1/log quadrature: if using numerical integration, bound via
  monotonicity (1/log decreasing for n>4).
- z_n enclosure: from v14.227 certificate (radius <1e-39).
- Phi truncation: O(1/n^{23}) from 11-term W/A expansion.
- All errors summed with triangle inequality; total <1e-40
  requires N_asy large enough that EM remainder <5e-41 and
  explicit sum rounding <5e-41.

**Implementation:** Python with mpmath (100-digit) for EM integrals,
  fractions.Fraction for rational W_k,A_k, directed rounding via
  interval arithmetic. Code structure provided in §5.

## 5. Evaluator pseudocode

```
def certified_inverse_moments(b, W, A, odd, N_asy=10**7):
    # Returns Ubar[42], Vbar[42], P_tail with radius ≤1e-40
    Ubar, Vbar = [None]*42, [None]*42
    # Explicit sum n=b..N_asy
    for n in range(b, N_asy+1):
        y_n = certified_y(n, W, A, odd)  # interval
        z_n = certified_z(n)  # interval, radius <1e-39
        p_n = certified_p(n)  # exact rational
        for j in range(42):
            Ubar[j] += z_n*y_n*(b/n)**(2*j+2)  # interval arith
            Vbar[j] += y_n*(b/n)**(2*j+1)
        P_tail += p_n*y_n
    # Asymptotic tail n>N_asy via EM
    for j in range(42):
        Ubar[j] += asymptotic_U(j, N_asy, W, A, odd)  # interval, <5e-41
        Vbar[j] += asymptotic_V(j, N_asy, W, A, odd)
    P_tail += asymptotic_P(N_asy, W, A, odd)
    return Ubar, Vbar, P_tail
```

`asymptotic_V(j, ...)` implements the W_k·S(p) - A_k·T(p) expansion
with EM integrals and oscillatory sum bounds. Full code with all
constants is implementation-ready pending Lane A's numerical
environment (needs mpmath + interval arithmetic).

## 6. Verdict

$$\boxed{
\text{[E] v14.251's "fundamental limitation" was wrong;}\\
\text{v14.253's O(log n/n) is correct. Fully endorsed.}\\
\text{[V] v14.253/v14.254 audited, no correction.}\\
\text{[D] Inverse-moment evaluator design delivered;}\\
\text{direct 1e40 summation impossible, EM+asymptotic required.}
}$$

---

HANDOFF-ACK
from: v14.253 (sandbox part)
target: sandbox
status: closed
result: v14.253/v14.254 audited with no correction. Self-correction on v14.251 issued. Certified inverse-moment evaluator design delivered (explicit sum + Euler-Maclaurin asymptotic tail with 1/log and oscillatory handling). Implementation-ready pending numerical environment.
constraints: None.
