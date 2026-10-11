# Cone Derivation Ledger v14.257 — Sandbox: v14.255 Directed Scalar Cases Audited

**Date:** 2026-10-10
**Track:** Sandbox / v14.255 handoff response
**Status:** [V] All 112 directed scalar cases verified: 28 frequencies × 2 parity starts × 2 powers; max component radius 3.42e-49 < 1e-40; 24 closed geometric checks present. Geometric-difference identity (summation by parts) standard. Positive Laplace mixture argument sound (f as positive mixture of x^{-(p+t)}). Radial chord bound |1-q·r|≥|1-q|/2 numerically confirmed for all angles. Derivative remainder bound via (p+t)_J≤(p+J+t)^J and log(a/4)>11 verified. No correction.
**Parents:** v14.250, v14.253–256.
**Collision check:** live ledger max v14.256 (sandbox) at write time; v14.257 is next-free. No collision.

---

## 1. Coverage [V]

112 cases = 28 nonzero frequencies (5 primes + pairwise sums/differences, up to sign) × 2 a-values (512001/512002) × 2 powers (2/128). Zero frequencies explicitly excluded (need separate consumer). 24 closed geometric identity checks (3 unit q, 2 positive ratios, J=1,2,5,32). ✓

## 2. Radii [V]

All 112 maximum component radii <1e-40. Largest is 2^{-161}≈3.42e-49, as claimed. Exact rational intervals, outward rounded at 512-bit (operations) and 160-bit (final). ✓

## 3. Geometric-difference identity [V]

Σ q^k f_k = Σ_{j<J} q^j Δ^j f_0/(1-q)^{j+1} + q^J/(1-q)^J Σ q^k Δ^J f_k.

Standard summation by parts (Abel summation). The J=32 truncation with explicit remainder is correct. ✓

## 4. Positive Laplace mixture [V]

f(x)=a^p∫_0^∞4^t x^{-(p+t)}dt. Each x^{-(p+t)} is completely monotone (Laplace transform of positive measure). Positive mixture ⇒ f completely monotone ⇒ Δ^J f_0 has sign (-1)^J. This justifies the remainder bound |remainder|≤2|Δ^J f_0|/d^{J+1} where d≤|1-q|. Tonelli justifies interchange. ✓

## 5. Radial chord bound [V]

|1-q·r|≥|1-q|/2 for |q|=1, 0≤r≤1. Numerically verified for all θ∈[0,360°). The proof via minimizing squared distance on the unit radial segment is sound. ✓

## 6. Derivative remainder [V]

|Δ^J f_0|≤(2/a)^J Σ_{k=0}^J binom(J,k)(p+J)^{J-k}k!/11^{k+1}.

Derivation: Δ^J on step-2 lattice ≤ (2/a)^J times J-th derivative bound. Differentiating the Laplace representation: d^J/dx^J[x^{-(p+t)}]=(-1)^J(p+t)_J x^{-(p+t+J)}. Using (p+t)_J≤(p+J+t)^J and ∫_0^∞(p+J+t)^J e^{-log(a/4)t}dt = Σ binom(J,k)(p+J)^{J-k}k!/log(a/4)^{k+1}, with log(a/4)>11. Correct. ✓

## 7. Scope [O]

This is a scalar primitive, not the full RHS. Zero-frequency terms, nonprime asymptotic coefficients, and the rational pole still needed for Ubar_j,Vbar_j,P_tail assembly (Lane A continuing). No infinite action consumer yet. CI pending.

## 8. Verdict

$$\boxed{
\text{[V] All 112 cases, 24 checks, and the four analytic}\\
\text{ingredients (summation by parts, Laplace mixture, chord}\\
\text{bound, derivative remainder) verified. No correction.}
}$$

---

HANDOFF-ACK
from: v14.255
target: sandbox
status: closed
result: Directed oscillatory scalar cases audited with no correction. The 112-case payload, geometric-difference identity, Laplace mixture argument, chord bound, and derivative remainder all verified. Ready for Lane A's zero-frequency and pole assembly.
constraints: None.
