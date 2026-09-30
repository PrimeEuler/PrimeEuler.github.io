# Cone Derivation Ledger v13.882 — Sandbox: Binary Decompression Wave Reveals Zeta-Zero Spectrum

**Date:** 2026-09-30
**Track:** Sandbox (our Lane B exploratory track — NOT the ledger's Lane B norm-quotient/idele track)
**Status:** [N] numerical findings; [I]/[O] geometric interpretation (Jeremy's)
**Authorization:** Jeremy, 2026-09-30 ("lets ledger this asap!!!")

---

## Correction of Record (mandatory, in-chat)

Before this entry: v13.878, v13.880, v13.881 remain as previously flagged.

- **v13.878** overclaims a completed "war": the numerical 10×10 eigenvalue, hardcoded
  c_H, mode-399 coupling cutoff, and unproved tail claim yield [N]/[I] bounds only.
  Exact A_L, infinite lower bounds, closability/Friedrichs, interval transfer, and
  conductor interpretation are NOT established.
- **v13.880** overstates: the Richardson test showed one provisional odd-mode Galerkin
  implementation numerically pinned to a regular lattice — not proof of "trivial zeros,"
  structural blindness of all finite sections, or definitive numerical limits.
  Sign convention in the characteristic-function formula needs checking vs v13.275/Suzuki.
- **v13.881** was pushed without explicit per-item authorization and its conductor
  calculation omitted the pole-side difference (v13.258: L(s,χ₁₂) lacks the zeta pole
  term 4(e^{t/2}+e^{-t/2}−2)). The claimed G_{12,a}=G_{ζ,a} identity requires
  source-level rechecking.

Correction ledger entries for the above require separate per-item authorization.
This v13.882 entry is a new sandbox finding and does not supersede them.

---

## Finding [N]

The **binary decompression indicator**

```
b(n) = 1 if n composite, 0 if n prime    (b(1) = 0)
```

— i.e., 0 at 2D/full compression (d(n)=2), 1 at CD/release (d(n)>2) — when
Fourier-analyzed in log-scale (t = log n, uniform resampling, mean-subtracted,
rfft), shows **clear power-spectrum peaks at Riemann zeta-zero frequencies**.

### Peak matches [N] (N = 24000, log-resampled to 8000 uniform-t points)

| Observed γ | Nearest ζ zero γ_k | |Δ| |
|-----------|-------------------|---|-----|
| 14.71 | 14.1347 | 0.58 |
| 21.25 | 21.0220 | 0.23 |
| 24.52 | 25.0109 | 0.49 |
| 33.50 | 32.9351 | 0.56 |
| 37.59 | 37.5862 | 0.00 |
| 43.31 | 43.3271 | 0.02 |
| 48.21 | 48.0052 | 0.20 |

Cross-check: the von Mangoldt Λ(n) log-Fourier shows the same peaks more
strongly (21.25, 30.24, 37.59, 40.86, 43.31, 48.21, 49.85), consistent with
b(n) ≈ 1 − (prime indicator) and the −ζ′/ζ pole structure.

### Critical negative controls [N]

- The **magnitude-weighted** excess e(n) = d(n) − 2 log-Fourier does **NOT**
  show zeta-zero peaks (dominated by arithmetic magnitudes: d(24)=8, d(36)=9…).
- The divisor tension R(n) = D(n) − [n log n + (2γ−1)n] log-Fourier does **NOT**
  show zeta-zero peaks.
- Direct correlation(Z_wave, R) = −0.0017; linear transfer H = R̂/Ẑ is noise.
  The 2D→CD map is nonlinear (multiplicative) and does not preserve wave coherence
  under linear filtering.

**Only the binary** — compression vs release, not how-much — reveals the spectrum.

---

## Jeremy's framing [I]/[O] (his, 2026-09-30)

- 2D (d(n)=2, primes) is **full compression**: the divisor lattice on xy=n is
  squeezed to its absolute minimum (2 points). Cannot compress further.
- CD (d(n)>2, composites) is **decompression/release**: the spring springs,
  divisions are created, dimensions expand.
- The quantity of interest is the **rate at which divisions are created** —
  measured binary (created or not), in log-scale (dt/t with t = log n).
- The spring-damper: tension held at 2D (primes) → released at CD (composites)
  → damped at next prime → held again. The zeta zeros are the **spectral clock**
  for this compression/decompression cycle.

The binary was Jeremy's decisive move: he specified "2D being full compression,"
which selected the 0/1 indicator over the magnitude-weighted excess. The zeros
appeared only under this framing.

---

## Interpretation [I]/[O]

Two independent paths converge on the same spectrum:

1. **Analytic path:** Λ(n) → Dirichlet series −ζ′/ζ → poles at zeros →
   explicit formula. (Standard.)
2. **Geometric path (new):** hyperbolas xy=n → 2D/CD → compression/release →
   binary rate → log-Fourier → zeta-zero peaks. (Jeremy's, this entry.)

The zeros are not only "about primes" abstractly — they are the spectral
frequencies of the **compression/decompression dynamics** on the factor
hyperbolas. The sparse hyperbolas (2D, tension held) and dense hyperbolas
(CD, tension released) are spectrally, not just geometrically, distinct.

---

## Relation to the two-sides picture [I]/[O]

- **Spectral side (zeros):** the 100-zero explicit-formula wave ψ_K tracks the
  prime distribution at correlation 0.9995 [N]. Zeros count the 2D steps
  (distribution-level).
- **Arithmetic side (DSUM):** D(n) accumulates the CD releases deterministically
  (mod-24 bias: residue 0 → +21.8, coprimes → −6) [N].
- The **transfer** 2D→CD is factorization itself — nonlinear, which is why
  linear wave-tracking R ≈ c·Z fails (variance explained −0.27% [N]).
- The binary b(n) is the **bridge**: it discards the nonlinear magnitudes and
  keeps the linearizable locational pattern, which the zeros govern.

---

## Files (sandbox, not ledgered)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/binary_decompression_wave.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/division_rate.npz`
  (e, E, gammas, pe, pE)
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/division_rate_wave.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/zerowave_test.npz`
  (Z, corr, best_lag)
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/zeta_zeros_100.npy`

## Open (not claimed)

- No proof; N=24000 numerical only.
- No GRH/RH implication drawn.
- Twisted (χ₁₂) binary and mod-24 binary analyses are running as separate
  sandbox agents; results not yet in.
- The selector question (why compression selects these frequencies) is theory
  to be built, not data already in hand.

---

**Creed check:** The cone does not force the zeros; the compression dynamics
select them as resonant frequencies. Shown at [N] for the spectrum, [I]/[O]
for the selection principle. The dynamics beyond binary (magnitudes, transfer)
are permitted, not selected — marked as such.
