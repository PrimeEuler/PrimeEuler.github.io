# Cone Derivation Ledger v13.889 — Sandbox: β-Explicit-Formula Loop Closed (χ₄ Beats χ₁₂)

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerical; [I]/assumption for RH-for-L(s,χ₄); [I]/[O] structural
**Authorization:** Jeremy, 2026-10-01 ("yep")
**Predecessors:** v13.885 (χ₁₂ loop-closer), v13.888 (probe universality)

---

## Headline [N]

Dirichlet β's explicit-formula loop is closed — and **beats χ₁₂ at every
scale with 17 fewer zeros**. Three L-worlds now loop-closed: ζ (0.9995),
β (0.9976), χ₁₂ (0.9840) at block-500.

## Method [N]

- True signal: ψ_β(x) = Σ_{n≤x} χ₄(n)·Λ(n), x=2..24000, sieve × χ₄.
- Explicit formula:
  ψ_β,T(x) = −2·Re[Σ_{j=1}^{50} x^ρ_j/ρ_j] + (1/2)·log((x+1)/(x−1)).
  - No main term x: exact (χ₄ non-principal).
  - No −log(2π): exact (ζ-specific).
  - Trivial zeros for the odd character at s=−1,−3,… summed exactly to
    (1/2)·log((x+1)/(x−1)); max 0.5493 at x=2, ≤4.2e−5 by x=24000.
  - All 50 zeros placed on Re(s)=1/2 — [I]/assumption, not proved.
- Finite-T DC offset small: true mean −6.59 vs ψ_T50 mean −5.66.

## Results [N]

| scale | corr (50 zeros) | corr (25 zeros) |
|-------|----------------:|----------------:|
| pointwise | **0.9428** | 0.9078 |
| block-100 | **0.9665** | 0.9315 |
| block-500 | **0.9976** | 0.9776 |
| block-1000 | **0.9996** | 0.9925 |

Residual std: 13.41 (50 zeros) vs 16.87 (25 zeros); true ψ_β std 40.21 —
systematic convergence, more zeros = better tracking.

## β beats χ₁₂ [N]

| scale | χ₄ (50 zeros) | χ₁₂ (67 zeros, v13.885) |
|-------|--------------:|------------------------:|
| pointwise | 0.9428 | 0.9303 |
| block-100 | 0.9665 | 0.9532 |
| block-500 | **0.9976** | 0.9840 |
| block-1000 | **0.9996** | 0.9973 |

β wins at every scale with fewer zeros — consistent with the probe finding
(15/16 spectral matches for χ₄ vs 11/16 for χ₁₂, v13.888). **The cleaner
the spectral detection, the tighter the explicit-formula tracking.**

## Structural [I]/[O]

The compression→spectrum→explicit-formula chain is now confirmed
independently in three L-worlds. β is the tightest per zero count,
reinforcing v13.888's finding that χ₄ is the cleanest spectral detector
of the five tested. The chain is not a ζ accident — it is the shape of
the explicit formula itself, seen through compression.

## Explicitly NOT claimed

- **No GRH.** RH-for-L(s,χ₄) was an *input assumption* [I]. This validates
  tracking *conditional* on critical-line zeros.

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/beta_explicit_wave.npz`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/beta_explicit_overlay.png`

---

**Creed check:** The cone selects β's zero spectrum via χ₄-twisted
compression, and the explicit formula tracks at 0.9976 — the tightest loop
per zero of the three closed. Shown [N]; the *why* remains [I]/[O].
