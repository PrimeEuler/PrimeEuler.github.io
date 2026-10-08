# Cone Derivation Ledger v14.160 — Sandbox: v14.159 Exact Trace Witness Audited

**Date:** 2026-10-08
**Track:** Sandbox / v14.159 handoff response
**Status:** [V] Trace witness design verified; no obstruction found. 64k/128k witnesses pending CI.
**Parents:** v14.156, v14.157, v14.159.
**Collision check:** live ledger max v14.159 at write time; v14.160 is next-free. No collision.

---

## 1. Exact conversion design: sound [V]

**Hi/lo full-significand conversion.** The capture routine calls
`as_integer_ratio()` on each longdouble entry directly, converts hi and lo
separately to exact Fractions, then adds exactly. This avoids the binary64
narrowing trap (64-bit longdouble significand vs 53-bit float). The entry's
self-test covers 21 exact cases across exponents ±10000, including a
binary64-narrowing counterexample. The design is correct: the stored values
are interpreted exactly, regardless of the solver rounding that produced them.

**"Represented" vs "exact" distinction: properly scoped.** The entry states
"The source solver's rounding affects which trial vector was obtained; it
does not prevent its stored values from being interpreted exactly." This is
the right framing: $\rho$ bounds the defect of the *represented* $V$
($V_{\rm hi}+V_{\rm lo}$ as stored), which is exactly what v14.156's repair
operates on. No claim is made about the ideal mathematical solution.

## 2. Witness consumer: verified [V]

**Rational Gram inversion.** $G=P^*P$, $H=G^{-1}P^*V$, $D=H-[T,Tv]$,
$Z=T^{-1}D$, all in exact Fraction arithmetic. The 6×6 rational inverse is
exact (not the floating Gram inverse). Structure verified numerically.

**$\rho$ bound.** $\rho=\sum_{i,j}|Z_{ij}|\geq\|T^{-1}D\|_F$ confirmed:
the entrywise $\ell_1$ norm dominates Frobenius ($\sqrt{\sum a_i^2}\leq\sum|a_i|$).
Verified on random matrices. The rational numerators/denominators are
retained; no decimal is used as an outward endpoint.

**Support sufficiency.** Only nonzero-$P$ rows are retained; all other rows
"verified exactly zero by enumerating its complete support." For the frozen
carrier, support is in the first 2000 rows. This is a computational claim
(checkable via the witness's support indices); the design is sound provided
the enumeration is complete, which the consumer's hash checks help enforce.

**Frozen-plane and parent-payload binding.** The witness includes the exact
$P$ byte hash (canonical and compressed SHA-256 separately), fixed $T,v$,
and support indices. Each $P$ value is checked against binary64
reconstruction exactly. In parent-payload mode, $T,v$ equality, dimension
selection, and certificate recomputation are all verified. This prevents
witness/payload mismatch.

## 3. 4k/8k validation: passes with large margin [N-cert]

| Parity | Cutoff | $\rho$ (exact) | Target $10^{-20}$ | Margin |
|---|---|---|---|---|
| even | 4000 | $4.55\times10^{-28}$ | ✓ | $2.2\times10^7$× |
| even | 8000 | $6.73\times10^{-28}$ | ✓ | $1.5\times10^7$× |
| odd | 4000 | $2.86\times10^{-28}$ | ✓ | $3.5\times10^7$× |
| odd | 8000 | $1.20\times10^{-28}$ | ✓ | $8.3\times10^7$× |

All four meet $\rho\leq10^{-20}$ by exact rational comparison, with 7+ orders
of magnitude margin. The entry correctly notes these use frontier 1000 and
"do not stand in for unexecuted 64k/128k witnesses."

## 4. Separation and scope: correct [V]

The entry explicitly states:
- Source operator/projector arithmetic: still missing.
- Graph/mixed/scalar assembly caps: still missing.
- Exact projected residual caps: still missing.
- "This entry neither certifies the finite 64k→128k source increment yet
  nor the infinite tail."

The trace-contract field is "restricted to the represented-vector trace and
explicitly labeled that way." No overclaim. CI run 37720158340 observed
in-progress; 64k/128k witnesses not claimed.

## 5. Verdict

$$\boxed{
\begin{aligned}
&\text{[V] Exact trace witness design verified: conversion,}\\
&\qquad\text{Gram inversion, }\rho\text{ bound, and payload binding all sound.}\\
&\text{[V] 4k/8k validation passes with }10^7\times\text{ margin.}\\
&\text{[O] 64k/128k witnesses pending CI; assembly/residual caps still missing.}\\
&\text{No obstruction found. First of six v14.157 targets has a sound implementation.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.159
target: sandbox
status: closed
result: Exact represented trace witness audited. Full-significand hi/lo conversion, support sufficiency design, rational Gram inversion, frozen-plane/parent binding, and separation from missing caps all verified. 4k/8k meet rho<=1e-20 exactly with large margin. 64k/128k witnesses await CI; no obstruction in the design.
constraints: None.
