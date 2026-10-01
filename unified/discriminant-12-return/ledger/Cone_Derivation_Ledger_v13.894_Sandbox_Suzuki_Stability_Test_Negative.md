# Cone Derivation Ledger v13.894 — Sandbox: Suzuki Stability Test (Decisive Negative)

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [N] numerical; [D] formula reconstruction; [I]/[O] interpretation
**Authorization:** Jeremy, 2026-10-01 ("yes ledger it")
**Predecessors:** v13.892 (quantization map); Road 2 / Suzuki (background main line)
**Note:** v13.893 is audit-thread; this takes the next free version.

---

## Question

v13.892's front-runner: does the spring↔Suzuki bridge go through
positivity? I.e., does Suzuki's screw kernel stay PSD under indicator
(compression) weights? **Answer: no — decisively.**

## Step 1 — Full g(t) [D]

Reconstructed Suzuki (1.3) from 2606.09096v2:
g(t) = −4(e^{|t|/2}+e^{−|t|/2}−2) + Σ_{n≤e^{|t|}} Λ(n)/√n·(|t|−log n)
       − (|t|/2)(ψ(1/4)−log π) − (1/4)(F(0)−F(t)).

- **Lerch bracketing ambiguity RESOLVED [D]:** §2.2 rewrites as
  −(1/4)(F(0)−F(t)), F(t)=e^{−|t|/2}Φ(e^{−2|t|},2,1/4); Lerch-direct vs
  power-series cross-checked to 10 dp at five points. Bracketing (a)
  confirmed.
- F(t) convergence: power series (|t|<1) + direct Lerch (|t|≥1).
- Validated [N]: g(0)=0 exact; matches (2.2) asymptotic ½|t|log|t|+A|t|.

## Step 2 — Calibration [N] ✓

Anchored kernel G(s,t)=g(s−t)−g(s)−g(−t)+g(0), symmetrized, eigvalsh:

| interval | grid | λ_min | negatives |
|----------|------|------:|----------:|
| (−6,6) | 400 | +0.002269 | 0 |
| (−3,3) | 400 | +0.002223 | 0 |
| (−6,6) | 800 | +0.001741 | 0 |

PSD holds everywhere — Suzuki's theorem (screw ⟺ RH) confirmed
numerically. Implementation correct.

## Step 3 — Indicator weights [N] ✗ FAILS decisively

Λ → 1_{prime} (full archimedean kept): **λ_min = −34,659, 36
negatives** (vs +0.00227, 0 for Λ). The archimedean term does **not**
rescue indicator-positivity.

**Isolation — prime powers are load-bearing [N]:** Λ on primes only
(dropping p^k, k≥2) → λ_min = −586.7, 95 negatives. Suzuki's positivity
needs the *full* von Mangoldt; the prime-power "higher harmonics" are
essential.

## Step 4 — θ-interpolation [N]

w_θ(p)=(log p)^θ on primes, w_θ(p^k)=(log p)^θ·θ for k≥2:
θ=1.0: +0.0023 (0 neg) → 0.999: −73.7 (4) → 0.99: −794.9 (6) →
0.9: −7331.9 (18) → 0.5: −22k (31) → 0.0: −34,659 (36).

**Stability boundary is exactly at θ=1** — monotonic breakdown, no
stable PSD neighborhood in the compression direction.

## Interpretation [I]/[O]

1. **The spring↔Suzuki bridge does not go through positivity.**
   Compression weights destroy screw-PSD; the failure is in the weights,
   not the missing archimedean.
2. **Two mechanisms, not one:** the spring gives zeros as *frequencies*
   [D, Guinand–Weil / v13.891]; Suzuki gives them via *positivity* [D,
   his theorem]. The spring's operator (if it exists) will not be a
   Suzuki perturbation.
3. **Positivity route for the spring: CLOSED.** Remaining live
   quantization directions: twisted trace as holonomy, Mayer validation.

Honest caveat preserved: even a positive result would have needed a new
theorem for RH-equivalence; the negative moots it. **No RH claims.**

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/suzuki_stability_report.md`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/suzuki_stability_theta.png`
- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/suzuki_stability_*.npz`

---

**Creed check:** The cone selects frequencies (derived) — but not through
Suzuki-positivity. The negative is decisive and reported plainly: two
mechanisms, not one. The spring's quantization, if it exists, lies
elsewhere.
