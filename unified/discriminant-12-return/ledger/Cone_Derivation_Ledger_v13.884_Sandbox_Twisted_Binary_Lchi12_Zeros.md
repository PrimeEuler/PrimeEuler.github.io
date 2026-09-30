# Cone Derivation Ledger v13.884 — Sandbox: Twisted Binary — L(s,χ₁₂) Zeros via the Compression Method

**Date:** 2026-09-30
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerical; [I]/[O] interpretation; [I]/assumption where flagged
**Authorization:** Jeremy, 2026-09-30 ("ledger both as two")
**Predecessor:** v13.882 (binary ζ-zero wave); v13.883 (mod-24 binary)

---

## Finding [N]

The binary-compression spectral method (v13.882) **generalizes from ζ to the
D12 character χ₁₂**. The χ₁₂-weighted prime detector's log-spectrum carries
L(s,χ₁₂)-zero frequencies.

### χ₁₂ verified [N]

χ₁₂(n) = 1 if n≡1,11 mod 12; −1 if n≡5,7 mod 12; 0 if (n,12)>1.
Checked: units {1,5,7,11} → {1,−1,−1,1} ✓; multiplicative on 2000 random
pairs ✓; even (χ₁₂(−1)=χ₁₂(11)=1) ✓. Gauss sum τ(χ₁₂)=2√3=√12 exactly
(numerically 3.4641016151377544, imag ~1e-16), so ε=τ/√12=1 and the
functional equation is symmetric: Λ(s)=Λ(1−s) with
Λ(s)=(12/π)^{s/2}Γ(s/2)L(s,χ₁₂).

### L(s,χ₁₂) zeros computed directly [N]

Method: L(s,χ₁₂) = 12^{−s}[ζ(s,1/12)−ζ(s,5/12)−ζ(s,7/12)+ζ(s,11/12)] via
mpmath Hurwitz (30 dps). Validation: L(2)=0.949703126294 vs direct Dirichlet
series 0.949703126269 (9-digit agreement); |Λ(s)−Λ(1−s)| ~1e-26 at test
points; Hardy Z(t) verified real (imag ~1e-30). Found **67 sign changes** in
t∈[0,100], all refined via findroot onto Re(s)=1/2; count matches the
asymptotic N(T)~(T/2π)ln(12T/2πe)≈67.7, so the list is essentially complete.

First zeros: **3.804628, 6.692223, 8.890593, 11.188393, 12.966179,
15.181481, 16.632633, 18.884369, 20.103928, 22.285839**, …

(Full list: `twisted_binary_Lzeros.npy`, 67 imaginary parts.)

### Spectral results [N]

Two twisted indicators, log-F fourier (t=log n, N=24000):

**b_χ(n) = χ₁₂(n)·b(n)** (twisted composite-weighted): **weak/partial.**
Of 14 top peaks, only 2 clean matches (18.80→18.884, diff 0.09;
35.96→35.778, diff 0.18); several weak (0.5–1.2); high-frequency peaks
(107–451) with no L-zero counterpart are noise. Notably weaker than the
ζ-case binary — expected [I]: b weights composites (a looser proxy for prime
locations), and χ₁₂ flips signs only on the (n,12)=1 subset, so ζ-zero
"leakage" contaminates it (e.g., peaks at 21.25 and 48.21 sit nearer ζ-zeros
21.02, 48.01 than any L-zero).

**Λ_χ(n) = χ₁₂(n)·Λ(n)** (twisted prime detector): **strong confirmation.**
Of 16 top peaks, **11 match L-zeros within 0.5**, several within 0.15:

| Observed γ | L-zero | |Δ| |
|-----------|--------|-----|
| 26.97 | 27.014 | **0.05** |
| 50.67 | 50.682 | **0.02** |
| 8.99 | 8.891 | 0.10 |
| 6.54 | 6.692 | 0.15 |
| 53.12 | 53.253 | 0.13 |
| 79.27 | 79.123 | 0.15 |
| 28.60 | 28.442 | 0.16 |
| 11.44 | 11.188 | 0.25 |
| 15.53 | 15.181 | 0.35 |
| 4.09 | 3.805 | 0.29 |
| 19.61 | 20.104 | 0.49 |

This mirrors the ζ case exactly, where Λ(n) showed ζ-zeros more cleanly
than b(n) did.

---

## Interpretation [I]/[O]

The D12 object **speaks spectrally** via Jeremy's geometric route — not through
Dirichlet series and functional equations, but through weighted
compression/release → log-Fourier → spectral peaks. The binary/twisted
methodology is not ζ-specific; it is a general spectral probe for
L-functions, with the character selecting which zero-spectrum appears.

The pattern is consistent: the **prime-weighted** indicator (Λ or Λ_χ) is the
clean signal; the **composite-weighted** (b or b_χ) is noisier. The zeros govern
*where* the 2D tension sits (primes); composites are a blurred shadow.

---

## Explicitly NOT claimed

- **No GRH implications.** This is a numerical spectral observation [N] on
  N=24000 with log-resampled FFT; it detects *some* low L-zeros as Fourier
  peaks. It does not locate all zeros or address the critical line.
- The interpretive framing (compression/release selecting frequencies)
  remains [I]/[O].
- A follow-up agent is currently testing whether the truncated twisted
  explicit formula ψ_χ,T(x) (built from these 67 zeros, assuming RH for
  L(s,χ₁₂) [I]/assumption) tracks the true twisted prime distribution
  ψ_χ(x) — the twisted analogue of the 0.9995 ζ validation. Results pending.

---

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_binary_wave.npz`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_binary_Lambda.npz`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_binary_Lzeros.npy`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/twisted_binary_spectra.png`

---

**Creed check:** The cone does not force the L-zeros; the χ₁₂-weighted
compression dynamics select them. Shown [N] for the spectral matches,
[I]/[O] for the selection reading. GRH is not touched.
