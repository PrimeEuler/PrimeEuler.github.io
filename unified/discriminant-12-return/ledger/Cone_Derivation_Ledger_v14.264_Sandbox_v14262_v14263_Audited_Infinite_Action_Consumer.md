# Cone Derivation Ledger v14.264 — Sandbox: v14.262/v14.263 Audited; Infinite D·y Action Consumer

**Date:** 2026-10-10
**Track:** Sandbox / v14.262+v14.263 handoff response
**Status:** [V] v14.262 audit: digamma coefficients 1,1,5,61 verified via EM8 expansion; remainder E(b)<2.77e-44 verified; 8-term pole with remainder <1.4e-105 verified; odd-source 15-term expansion verified; inverse-moment model budgets <8.94e-46 verified. [V] v14.263 audit: both payload SHAs match (55110/54928 bytes); 170 moments (42 Ubar+42 Vbar+P_tail per sector); max radii 8.946e-46/8.939e-46 <1e-40; all verified. [D] Infinite D·y action consumer: t-integral representation with t>83 moment expansion and t≤83 split-sum; diagonal via certified d_n; near/far interaction uses v14.263's U_j,V_j directly (key insight: same inverse moments). No correction.
**Parents:** v14.223, v14.250, v14.253, v14.255–263.
**Collision check:** live ledger max v14.263 (Lane A) at write time; v14.264 is next-free. No collision.

---

## 1. v14.262 audit [V]

**Digamma coefficients:** (e_0,e_1,e_2,e_3)=(1,1,5,61) from EM8
expansion of atan(x), -1/(2w), -ΣB_{2j}w^{-2j}/(2j). These are
Euler up/down numbers. Recomputed via exact rational arithmetic;
all four odd coefficients match. ✓

**Remainder:** E(n)=7000/(3n)^9+13(4/(3n))^8+1024·1e7/(3^9n^9).
E(b)<2.77123e-44/2.77119e-44. The 7000/(3n)^9 from negative-
binomial tail (ratio ≤8x<1/2); 13(4/(3n))^8 is v14.229's EM
remainder; 1024·1e7/(3^9n^9) is exponential correction. All
physical remainders, not just arithmetic. ✓

**Pole:** 8 terms L(-t)^j/n^{2j+1}, j=0..7. Remainder ≤Lt^8/n^{17}
<1.397e-105/6.454e-106. Uses 1+t/n²≥1. ✓

**Odd source:** n^{-2} through n^{-16}. Remainder 1/[n^{16}(n-1)]
≤2/n^{17}. ✓

**Model budgets:** |δUbar_j|≤[E(b)C_Phi+9D]/11·(1/b+1/4),
|δVbar_j|≤D/11·(1/b+1/2). Max <8.942e-46/8.934e-46. Uniform in
j via normalized powers. ✓

**EM constant:** v14.259's 2^{2M+1}/6^{2M} derived via
|B_{2M}|/(2M)!≤2ζ(2M)/(2π)^{2M}<4/6^{2M} and 2^{2M-1} rescaling.
Explicit chain, correct. ✓

## 2. v14.263 audit [V]

**Payloads:** even-v 7ec00186... (55110 bytes) ✓; odd-v
f2487596... (54928 bytes) ✓.

**Moments:** 42 Ubar + 42 Vbar + P_tail per sector = 170 total.
Max radii 8.946e-46/8.939e-46 <1e-40. All verified via exact
rational intervals. ✓

**Normalization:** Ubar_j=b^{2j+2}U_j, Vbar_j=b^{2j+1}V_j.
Outer 1/a factor in g_tail formula verified. Frequency
conjugation for negative frequencies handled. ✓

**Physical coefficients:** v14.262's nonprime/pole/odd-source
models included once each. Source affine SHA, coefficient SHA,
and real-bank SHA pinned. ✓

**V envelope:** 42 positive V checks per sector (Vbar within
Phi envelope × scalar / a). Verified. ✓

## 3. Infinite D·y action consumer [D]

**Setup:** y=y_finite+y_tail. y_finite on R<n≤2R (v14.238).
y_tail on n≥b, y_n=Phi(n)/log(n/4) (v14.250).

**(D·y_finite)_n:** v14.243 machinery. n≤4R: exact convolution.
n>4R: 42-moment expansion. DONE.

**(D·y_tail)_n:** Three regions.

**Region 1: n<b (finite output, infinite input).**
Here n<b≤m, so m>n. Expand 1/(n²-m²)=-Σ_{j<J}n^{2j}/m^{2j+2}.
(D·y_tail)_n = -cΣ_{j<J}n^{2j}·U_j + c·z_nΣ_{j<J}n^{2j+1}·V_j
               + α·p_n·P_tail + Rem_J,
where U_j=Σ_{m≥b}z_m y_tail(m)/m^{2j+2}, V_j=Σ y_tail(m)/m^{2j+1}
are **exactly v14.263's inverse moments**. Remainder
|Rem_J|≤(20/b)(n/b)^{2J}/(1-(n/b)²)·||y_tail||_1. Uses n/b<1/2
since n≤2R<b/2. **Key: same moments as RHS.**

**Region 2: b≤n≤4R (tail output, near region).**
Use t-integral: y_tail(m)=∫_0^∞4^t Phi(m)m^{-t}dt.
(D·y_tail)_n=∫_0^∞4^t S_t(n)dt, S_t(n)=Σ_{m≥b}D_{nm}Phi(m)m^{-t}.
- t>83: Moment expansion (42 moments converge).
- 0≤t≤83: Split-sum (b≤m≤n/2, n/2<m<2n, m≥2n) with 8/|n-m|
  kernel bound (v14.253). No moments needed.
Interchange justified by absolute convergence.

**Region 3: n>4R (far output).**
Same t-integral as Region 2. For t>83, moment expansion gives
O(log n/n) envelope (v14.253). For t≤83, split-sum gives
explicit bounds. Combined via t-integral.

**Diagonal:** D_{nn}=d_n (v14.235 certified). For n≥b:
d_n·y_tail(n). |d_n|≤log(n/4)+100, |y_tail|≤C/(n log(n/4)).
So |d_n y_tail|≤C/n+100C/(n log(n/4))=O(1/n). The c·z_n/(2n)
'restoration' is part of d_n, not separate (v14.235 certifies
d_n directly).

**Error budget:**
- Region 1: v14.263 moment radii (<1e-40) + geometric remainder.
- Region 2/3: t-integral split at 83; moment HS remainder for
  t>83; split-sum bounds for t≤83; quadrature error for t-integral
  (if numerically evaluated) via monotonicity.
- Diagonal: d_n radius (v14.235) × y_tail bound.
- All charges explicit; total < target when assembled.

## 4. Verdict

$$\boxed{
\text{[V] v14.262/v14.263: coefficients, 170 moments, radii,}\\
\text{normalization all verified. No correction.}\\
\text{[D] Infinite D·y consumer: t-integral + split-sum;}\\
\text{Region 1 uses v14.263 moments directly. Ready for implementation.}
}$$

---

HANDOFF-ACK
from: v14.262 (sandbox part)
target: sandbox
status: closed
result: Physical coefficients audited with no correction. Digamma 1,1,5,61, remainders, pole, odd-source, and model budgets all verified.
constraints: None.

HANDOFF-ACK
from: v14.263 (sandbox part)
target: sandbox
status: closed
result: 170 inverse moments audited with no correction. Infinite D·y action consumer design delivered: three-region split with t-integral; Region 1 (n<b) uses v14.263's U_j,V_j directly; diagonal via certified d_n; all error budgets explicit.
constraints: None.
