# Cone Derivation Ledger v13.885 — Sandbox: Twisted Explicit Formula Closes the Loop

**Date:** 2026-09-30
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerical; [I]/assumption flagged; [I]/[O] interpretation
**Authorization:** Jeremy, 2026-09-30 ("yes ledger")
**Predecessors:** v13.882 (binary ζ wave), v13.883 (mod-24), v13.884 (twisted binary)

---

## Finding [N]

The truncated **twisted explicit formula**, built from the 67 computed
L(s,χ₁₂) zeros (v13.884), tracks the true χ₁₂-weighted prime distribution
the way the ζ zero-sum tracked ψ — closing the loop for the D12 character.

### Formula [N]

For ψ_χ(x) = Σ_{n≤x} χ₁₂(n)·Λ(n), with ρ_j = 1/2 + iγ_j the 67 L-zeros (t<100):

```
ψ_χ,T(x) = −2·Re[ Σ_{j=1}^{67} x^ρ_j/ρ_j ] + (1/2)·log(1 − x^{−2})
```

- **No main term x**: exact — χ₁₂ is non-principal, s=1 is not a pole.
- **No −log(2π)**: exact — that constant is ζ-specific.
- **Trivial zeros included**: (1/2)log(1−x^{−2}) from s=−2,−4,…;
  max |·|=0.144 at x=2, ≤5e−5 by x=100 — negligible, kept for exactness.
- **RH for L(s,χ₁₂) assumed** ([I]/assumption, not proved): all 67 zeros
  placed on Re(s)=1/2 per findroot refinement.
- Truncation leaves a DC offset (mean ψ_T ≈ 9.1 vs true ≈ 0.7) — finite-T
  artifact, does not affect correlation.

### Tracking results [N] (x = 2..24000, true ψ_χ via sieve × χ₁₂)

| scale | corr(ψ_χ,true, ψ_χ,T) |
|-------|----------------------|
| pointwise | 0.9303 |
| block 100 | 0.9532 |
| block 500 | **0.9840** |
| block 1000 | **0.9973** |

Residual std shrinks with zero count (33 zeros → 19.40; 67 zeros → 16.47;
true ψ_χ std 44.89) — systematic convergence, more zeros = better tracking,
as the explicit formula predicts.

### The quantitative parallel [N]

- ζ zeros → ψ(x) → 2D steps: **0.9995** at block-500 (100 zeros, T≈236).
- L(s,χ₁₂) zeros → ψ_χ(x) → twisted 2D steps: **0.9840** at block-500
  (67 zeros, T≈99).

Fewer zeros, slightly lower correlation — exactly as expected. The parallel
is quantitative, not just qualitative.

---

## Interpretation [I]/[O]

The compression framework (Jeremy's) now covers both worlds end to end:

```
ζ world:    binary → spectrum → ζ-zeros → explicit formula → 2D steps ✓
χ₁₂ world:  twisted binary → spectrum → L-zeros → twisted explicit → twisted 2D ✓
```

The D12 character's zeros **count the twisted 2D steps** via the explicit
formula, just as ζ's zeros count the 2D steps. The cone's selection principle
— compression dynamics selecting spectral frequencies — operates identically
in both worlds, with the character selecting which spectrum appears.

---

## Explicitly NOT claimed

- **No GRH.** RH for L(s,χ₁₂) was an *input assumption* [I] in placing the
  67 zeros on the critical line. This validates that *if* the zeros are on
  the line, the explicit formula tracks — it says nothing about *whether*
  they are.
- Numerical only (N=24000, 67 zeros).

---

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_explicit_overlay.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_explicit_wave.npz`

---

**Creed check:** The cone selects the L-zero spectrum via χ₁₂-weighted
compression, just as it selects the ζ spectrum via unweighted compression.
Shown [N] for tracking; the selection *principle* (why) remains [I]/[O].
