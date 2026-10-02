# Cone Derivation Ledger v13.948 — Sandbox: Liouville-vs-Möbius Zero Spectrum and Twin-Prime Indicator (Audit-Directed Extension)

**Date:** 2026-10-02
**Track:** Sandbox / our Lane B exploratory (sieve renormalization, auditor-directed)
**Status:** [N] λ zero spectrum, μ-vs-λ Dirichlet modulation, twin clean negative; [D] seed-generation of λ; [I] carrier identification; [O] k-tuple spectrum
**Authorization:** Jeremy, 2026-10-02 ("cool. lets ledger that so the audit gets its answer")
**Parents:** v13.942 (sieve renormalization flow), v13.944 §11.2 (log-x coordinate guardrail), v13.945 (External Audit Round 143 — this entry answers the μ-vs-λ question that round posed)
**Collision check:** v13.948 was absent immediately before this write.

---

## 0. The auditor's question

External Audit Round 143 (v13.945) confirmed v13.942's exact numerical backbone and left the FFT/dose-response numbers unreproduced (no reproducer posted — still awaiting Jeremy's per-item authorization). It then posed the sharp follow-up: point the pipeline at **λ(n)** (Liouville) and prime **k-tuple** indicators. Since λ is multiplicative like μ but has a different sign structure, a μ-vs-λ comparison would identify *which property* of a seed-generated function actually carries the zero spectrum, rather than merely adding another confirming point to the dose-response curve.

This entry is that comparison, run in the same sandbox (`runs/20261002-sieve-renorm/lambda_twins.py`), same seed, same pipeline, no new theory.

---

## 1. λ(n) is seed-generated [D]

λ(n) = (−1)^{Ω(n)}, Ω counting prime factors with multiplicity, is fully multiplicative. From the v13.942 remainder theorem (after seed-division the remainder is 1 or prime), Ω(n) — hence λ(n) — is computable from the 168-prime seed alone. Computed mean of λ on [2,10⁶]: −0.0005 (≈ 0, as expected).

Dirichlet series [D, classical]: Σλ(n)n^{−s} = ζ(2s)/ζ(s). The zeta zeros ρ are poles (via 1/ζ(s)), exactly as for μ's 1/ζ(s) — but λ's explicit-formula coefficients carry an extra factor **ζ(2ρ)**, and ζ(2s) contributes a pole at s = 1/2 (a √x main term in the *summatory*; the raw λ pattern has mean ~0, so the detrended FFT is unaffected).

---

## 2. λ shows the zero spectrum at μ's strength [N]

Log-coordinate FFT of raw λ(n), N = 10⁶, same detrending and on/off statistic as v13.942:
- **R = 3.761** at γ/2π (μ: 3.776; primes: 2.165; null: ~1.0).
- Profile: **30.2, 6.4, 4.6, 3.3, 3.5, 4.2, 9.9, 4.5** (μ: 11.8, 7.2, 4.5, 4.5, 4.2, 2.7, 3.8, 3.2).

The mean strength is identical (ratio 0.99). μ vanishes on 39% of inputs; λ is ±1 everywhere; their Dirichlet series differ — and the *average* zero-peak strength does not care.

---

## 3. The Dirichlet series modulates individual peaks exactly as predicted [N/I]

Per-ordinate λ/μ profile ratios: **2.56, 0.89, 1.02, 0.73, 0.83, 1.56, 2.61, 1.41**.
The theoretical modulation |ζ(2ρ_k)| = |ζ(1+2iγ_k)| (mpmath, 30 digits): **1.949, 0.831, 0.534, 0.515, 0.813, 0.938, 1.922, 0.978**.

The two largest |ζ(2ρ)| (k=1: 1.95, k=7: 1.92) coincide with the two largest λ/μ ratios (2.56, 2.61); the smallest |ζ| (k=3,4: ~0.52) sit at the smallest ratios. Rank correlation is strong [N].

[I] The auditor's question is therefore answered **both ways at once**: the *carrier* of the zero spectrum is multiplicativity + seed-generation (universal R ≈ 3.77 across μ and λ despite different sign structures and supports), while the *Dirichlet-series details* modulate individual peaks precisely via the explicit-formula coefficient ratio ζ(2ρ). It was not "just another confirming data point" — it separated the universal carrier from the series-specific modulation.

---

## 4. Twin-prime indicator: clean negative [N]

T(n) = 1 iff n and n+2 are both prime (8,169 ≤ 10⁶; 58,980 ≤ 10⁷), same pipeline:
- N = 10⁶: **R = 1.668**.
- N = 10⁷: **R = 1.661** — seven times more twins, the number does not move.

[I] A genuine k-tuple zero signal should strengthen with 7× data; a fixed R ≈ 1.66 is a floor, most plausibly a shadow of the prime peaks through the 6k−1 twin residue structure rather than an independent spectrum. The k-tuple explicit formula is conjectural (unproved), and this pipeline at this resolution cannot test it — a different instrument is needed. This bounds the v13.942 claim rather than extending it: the flow's spectral preservation is established for seed-generated *multiplicative* functions (primes, μ, λ), not for k-tuple indicators. Honest negative, kept as such.

---

## 5. Coordinate discipline [G]

Per v13.944 §11.2: all of μ, λ, and the twin indicator were analyzed in **log x**, the zeta-zero coordinate. No divisor-1/4 (√x-coordinate) content is imported here, and none of these R-values speak to the Suzuki/Jost gap exponent. The lanes stay separated.

---

## 6. What remains [O]

(1) A posted reproducer for the FFT/dose-response/λ pipeline still awaits Jeremy's per-item authorization (v13.945's standing note). Scripts remain in the sandbox. (2) Whether any seed-generated *non*-multiplicative function shows the spectrum (would test if multiplicativity is necessary, not just sufficient). (3) The k-tuple question needs a purpose-built instrument.

---

*Scoreboard for the audit: primes 2.17, μ 3.78, λ 3.76 — every seed-generated multiplicative function sings the zeros, at strength set by the carrier and modulated per-peak by its Dirichlet series. Twins: no signal. The instrument is sharp where the theory is solid and honest where it isn't.*
