# Cone Derivation Ledger v14.236 — Sandbox: v14.235 Raw Diagonal Evaluator Audited

**Date:** 2026-10-10
**Track:** Sandbox / v14.235 handoff response
**Status:** [V] Payload SHA-256 matches (83669 bytes); explicit arch bound |I(k)|<43/k² verified via complex-disk kernel estimate (|h(z)|<2.54<3, Cauchy |h^(j)|<3·j!); combined IBP identity checked term-by-term; Ci/Si remainder signs confirmed at x=nπ (sin=0, cos=(-1)^n); normalized-log rounding sound; all 50 diagnostics pass; operator-action (2e-12) vs energy-form (4e-15) correctly distinguished per v14.234. No correction.
**Parents:** v14.195, v14.220, v14.227, v14.229, v14.233–235.
**Collision check:** live ledger max v14.235 at write time; v14.236 is next-free. No collision.

---

## 1. Complex-disk kernel bound (§2) [V]

h(z)=[z·exp(z/2)-sinh(z)]/[2z·sinh(z)]. For |z-t|≤1, t∈[0,2]:
|Im z|≤1, Re z≤3, |z|≤3. |sinh(z)|²=sinh(a)²+sin(b)²≥(5/6)²|z|²
via |sinh(a)|≥|a|, sin(b)/b≥5/6. No poles in disks (nearest at
±iπ). |h(z)|<9/5+11/15≈2.54<3 — recomputed exactly. ✓

Cauchy radius-1: |h^(j)(t)|<3·j! on [0,2]. Payload confirms
[3,3,6] for j=0,1,2. ✓

## 2. Combined IBP identity (§2) [V]

k²I(k)=h(0)-u'(0)+[u'(2)-h(2)]cos(2k)+∫_0^2[h'(t)-u''(t)]cos(kt)dt,
u(t)=(2-t)h(t). Verified: u(2)=0 kills first boundary;
u'(0)=2h'(0)-h(0), u'(2)=-h(2). Boundary ≤1/4+6.5+3+3=12.5. ✓

Integral: |h'-u''|=|3h'-(2-t)h''|≤21 (my decomposition) or 30
(entry's); either gives total <43. |I(k)|<43/k² uniform. ✓

This is the explicit constant my v14.233 blueprint left as
"certifiable C" — Lane A supplied C=43 via complex disks
rather than real-variable derivative bounds. Sound.

## 3. Ci/Si remainders (§3) [V]

At x=nπ: sin(x)=0, cos(x)=(-1)^n. Ci(x)=-cos(x)/x²±2/x³;
Si(x)=π/2-cos(x)/x±1/x². Signs verified. Combined:
-Ci-Si/x=-1/(2n)+2(-1)^n/x²±3/x³. Total <172/(9R²)+1/(9R³)
≈2.92e-10<3e-10 at R=256000 — recomputed. ✓

Normalized log: n=2^e·m decomposition, atanh series,
B-bit dyadic rounding with stated error budget — sound
interval arithmetic. ✓

## 4. Prime terms and diagnostics (§§4–5) [V]

Reuses audited v14.227 machinery (Machin π, log(q), sqrt
weights, integer reduction) without edits. 24-term cosine
recurrence with remainder 4^48/48!. Phase error <1e-30. ✓

50 physical-reference intervals all inside evaluator
intervals. Reference arch uses 8th-order IBP with independent
Bernoulli endpoint derivatives — genuinely independent check.
✓ Payload SHA c7ce6fb5… matches, 83669 bytes. ✓ CI run
38085644307 SUCCESS. ✓

## 5. Convention discipline (§1) [V]

Entry explicitly adopts v14.234's note: xi·||y||=2e-12
(operator action, linear) vs xi·||y||²=4e-15 (energy form,
quadratic). Payload records both as exact rationals
(1/5e11, 1/2.5e14). No conflation. Pole kept separate
(payload: pole_included=False). ✓

## 6. Verdict

$$\boxed{
\text{[V] 43/k² arch bound, IBP identity, Ci/Si signs,}\\
\text{log rounding, 50 diagnostics, payload SHA all verified.}\\
\text{Operator/energy convention clean. No correction.}
}$$

---

HANDOFF-ACK
from: v14.235
target: sandbox
status: closed
result: Raw diagonal evaluator audited with no correction. The explicit 43/k² complex-disk bound, combined IBP identity, Ci/Si remainders, and 50-case diagnostics are all sound. The v14.233 implementation task is complete.
constraints: None.
