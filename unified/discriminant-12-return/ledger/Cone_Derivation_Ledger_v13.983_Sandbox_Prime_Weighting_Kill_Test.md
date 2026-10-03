# Cone Derivation Ledger v13.983 — Sandbox Prime-Weighting Kill Test

**Date:** 2026-10-03
**Track:** Sandbox (our Lane B)
**Status:** [N] fresh verification; [I] interpretation.
**Authorization:** Jeremy, 2026-10-03

---

## 1. Experiment [N]

Prime indicator pattern b(n) = 1_{n prime} on [2,10⁶], weighted by
w(p) at primes: b_w(n) = w(n)·1_{n prime}. R via standard pipeline
(log-resample, detrend, FFT, ±0.12 windows at γ_k/2π).

| weight w(p) | R |
|-------------|---|
| 1 (binary)  | 1.577 |
| 1/log p     | 1.073 |
| 1/√p        | 1.063 |
| log p       | 2.545 |

## 2. Result [N]

Inverse-prime weights (1/log p, 1/√p) **kill** the spectrum to null
(R≈1.07). The von Mangoldt weight (log p) **strengthens** it
(R=2.55 vs 1.58 binary).

## 3. Interpretation [I]

Small-prime emphasis in the *pattern* does not help; the natural
arithmetic weight (log p, the von Mangoldt function from the
explicit formula) does. Leverage lies in *generation* (the sieve),
not in reweighting. The twist is permitted, not selected.

*Note: an earlier sandbox note misremembered the binary-prime R as
2.165 (that's the composite indicator). The verified numbers above
supersede it.*
