# Cone Derivation Ledger v14.260 — Sandbox: v14.259 Nonoscillatory Scalar Cases Audited

**Date:** 2026-10-10
**Track:** Sandbox / v14.259 handoff response
**Status:** [V] All 254 directed zero-frequency scalar cases verified: 2 parity starts × 127 powers (2..128); max radius 6.84e-49 < 1e-40. Integral substitution x=a·e^u verified. Panel geometric expansion with r^64 remainder verified. Step-two Euler-Maclaurin with M=16, exact rational Bernoulli, and 2^{2M+1}/6^{2M} remainder verified. Derivative formula via (p+t)_d expansion verified. Three 90-digit mpmath references inside intervals. No correction.
**Parents:** v14.253, v14.255–259.
**Collision check:** live ledger max v14.259 (Lane A) at write time; v14.260 is next-free. No collision.

---

## 1. Coverage [V]

254 cases = 2 a-values (512001/512002) × 127 integer powers (2..128).
All radii <1e-40; max is 2^{-160}≈6.84e-49. ✓

## 2. Integral substitution [V]

x=a·e^u, dx=a·e^u du. f(x)=(a/x)^p/log(x/4).
(a/(a·e^u))^p = e^{-pu}. log(a·e^u/4)=log(a/4)+u=λ+u.
∫_a^∞f(x)dx = ∫_0^∞e^{-pu}/(λ+u)·a·e^u du = a∫_0^∞e^{-(p-1)u}/(λ+u)du.
With h=p-1. Exact. ✓

## 3. Directed panels [V]

[0,T] with T=4·ceil(32/h), so hT≥128. Panels of width 4, center v.
1/(λ+u) expanded geometrically about v through degree 63.
Remainder r^{64}/[(λ+v)(1-r)], r=2/(λ_lower+v)<1. Standard. ✓
Tail beyond T: e^{-hT}/[h(λ+T)]. ✓
Panel moments I_k via exact integration by parts. e^{-1} from
directed alternating series. No untracked floating. ✓

## 4. Step-two Euler-Maclaurin [V]

S_p(a)=½∫_a^∞f + f(a)/2 - Σ_{j=1}^{16}B_{2j}·2^{2j-1}/(2j)!·f^{(2j-1)}(a)+R.
The ½ and 2^{2j-1} are correct for step-2 lattice. Bernoulli as
exact rationals (B2=1/6, B4=-1/30 checked). ✓

Remainder: |R|≤2^{2M+1}/6^{2M}·|f^{(2M-1)}(a)|.
Uses periodic Bernoulli bound with ζ(2M)<2, 2π>6. Complete
monotonicity gives ∫_a^∞|f^{(2M)}|=|f^{(2M-1)}(a)|. Sound. ✓

## 5. Derivative evaluation [V]

|f^{(d)}(a)|=a^{-d}∫_0^∞(p+t)_d e^{-λt}dt.
From f(x)=a^p∫_0^∞4^t x^{-(p+t)}dt, differentiating d times.
(p+t)_d expanded as exact polynomial; ∫t^k e^{-λt}dt=k!/λ^{k+1}.
Odd derivatives negative (noted). ✓

## 6. References [V]

Three 90-digit mpmath checks at (512001,2), (512001,128),
(512002,3). All inside directed intervals. Verification only;
certificate rests on panel+EM bounds. ✓

## 7. Scope [O]

Zero-frequency scalar engine complete. Still needed for Ubar/Vbar/
P_tail: physical nonprime z coefficients (not constant), exact pole,
odd-source expansion, intermediate oscillatory powers, and summed
truncation/parameter errors. No complete RHS or action yet. CI pending.

## 8. Verdict

$$\boxed{
\text{[V] All 254 cases, integral panels, EM formula,}\\
\text{derivative bounds, and references verified. No correction.}
}$$

---

HANDOFF-ACK
from: v14.259
target: sandbox
status: closed
result: Directed nonoscillatory scalar cases audited with no correction. The 254-case payload, integral substitution, panel method, step-two EM with remainder, and derivative evaluation all verified. Ready for Lane A's physical coefficient assembly.
constraints: None.
