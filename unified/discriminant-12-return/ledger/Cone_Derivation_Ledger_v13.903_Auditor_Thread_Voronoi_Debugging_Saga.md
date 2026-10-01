# Cone Derivation Ledger v13.903 — Auditor-Thread: Why the Zeros Don't Encode d(n) (Structural Proof), and the Divisor Problem's Real Dual Formula (Voronoi, Verified After Two Self-Caught Errors)

Date: 2026-10-01

Author: External audit thread (Claude, independent instance) — **contributed finding, not an audit round.** This entry records a debugging saga in full, including two of my own errors, because the final result only means something in light of what was ruled out to get there. Predecessors: v13.898–900 (my own HC-number/gap-length work), triggered by a direct conversational challenge from the project owner ("the zeros have to be encoding the prime gaps and the gaps encode HC").

Status: **[D]** for the structural Euler-product argument (proved, not just tested); **[N]** for all numerical verification; **[I]/[O]** for interpretation. No RH/GRH claim. Unrelated to the positivity program (v13.894/896/902) — same firewall as v13.898.

## 1. The question that started this: do the zeros encode d(n)/HC structure?

Challenged directly on whether "zeros encode primes, primes determine gaps, gaps contain HC numbers" implies the zeros must encode HC-type divisor structure too. Four prior numerical tests (`|ψ(x)-x|` at HC numbers, at record-gap boundaries, the explicit-formula derivative at HC numbers and at abundant numbers with real sample size) had already come back null. This entry supplies the **proof** of why, not just another null test.

## 2. Structural proof: no Euler-product's logarithmic derivative can ever produce d(n) [D]

For any Dirichlet series with an Euler product `F(s) = Π_p (local factor at p)` — this is `ζ(s)` and essentially every classical L-function — `log F(s) = Σ_p (...)` turns the product into a sum over primes. Differentiating term by term, every contribution stays locked to a single prime (no term can ever mix two different primes). So `-F'(s)/F(s)`, as a Dirichlet series `Σ a(n)n^{-s}`, is **forced** to have `a(n)=0` unless `n` is a prime power — a structural consequence of the product-to-sum conversion, true for *any* choice of `F`, not a property of `ζ(s)` specifically.

`d(n)` is not prime-power-supported (`d(6)=4≠0`, `6` is not a prime power), so it can never arise this way, for any `F`. Concretely for the most natural candidate, `ζ(s)²`: `(ζ²)'/ζ² = 2ζ'/ζ` by the plain chain rule, so `-(ζ²)'(s)/ζ(s)²` is exactly `2Λ(n)` as a series — its coefficient at `n=6` is `0`, not `4`. Squaring zeta doesn't get you closer to the divisor function; it gets you the prime information again, doubled.

**Further sharpened:** even restricted to prime powers alone, `Λ(p^m) = log(p)` for *every* `m≥1` — the von Mangoldt function cannot distinguish exponents. So the explicit-formula machinery can't recover `d(p^m)=m+1` even at the one class of points where it has any support at all. And `d(p^m)=m+1` doesn't need the zeros to explain it in the first place — it's an exact one-line fact from what a divisor is, with no error term, no oscillation, nothing for a zero-based correction to resolve. The zeros exist specifically to explain genuine gaps between a smooth prediction and reality (`ψ(x)-x` has one); `d(p^m)` doesn't have one.

## 3. First wrong turn: Perron's formula for D(x) does NOT pick up a residue at the zeros [D, verified numerically]

Initially claimed (incorrectly, in conversation) that a "Voronoi formula" reconstructs `Δ(x)` as a sum over the zeta zeros `ρ`, analogous to `ψ(x)`'s explicit formula. **This is wrong, and I corrected it the same session.** Re-derived via Perron's formula for `D(x)=Σ_{n≤x}d(n)`:

```
D(x) = (1/2πi)∫ ζ(s)² x^s/s ds
```

At a nontrivial zero `ρ` (simple), `ζ(s)` has a simple zero, so `ζ(s)²` has a **double zero** — confirmed numerically (`ζ(ρ+2ε)/ζ(ρ+ε) → 2.0000` as `ε→0` at `ρ_1=0.5+14.1347...i`, the signature of a simple zero). A zero of the integrand contributes **no residue, no pole, nothing** to the contour integral. The nontrivial zeros of `ζ(s)` literally do not enter `D(x)`'s residue-sum reconstruction. This is why `D(x)`'s only direct zero-based connection is through the much weaker mechanism of §5, not a discrete sum naming each `ρ`.

## 4. Second wrong turn: the critical-line integral exists as an identity but is numerically treacherous [N, debugged live]

Having correctly identified that shifting the Perron contour to `Re(s)=1/2` leaves `Δ(x) = (√x/2π)∫ζ(½+it)² x^{it}/(½+it) dt` (a valid contour-shift identity — the residue-crossing at `s=1` was checked in isolation and matched the known main term `x log x + (2γ-1)x` to `0.2%`), I attempted to evaluate this numerically with a Gaussian-tapered quadrature. **It failed cleanly and instructively**: the result came out nearly constant (`≈0.2500`, suspiciously close to `ζ(0)²=¼`) regardless of `x`, for every taper width tried (`σ_t=15,60,150`), with correlation `+0.03` against the true (smoothed) `Δ(x)`.

Root cause, confirmed directly: `|ζ(0.6+it)|` does **not** decay with `t` (sampled `1.51, 0.34, 2.36, 4.74, 0.55, 1.60` at `t=10...800` — no trend, genuine growth at times), unlike `|ζ(2+it)|` (`1.20, 0.78, 1.19, 1.47, 1.27, 1.08` — bounded, settles near 1, consistent with absolute convergence). The basic Perron pipeline was independently confirmed sound first (reconstructed `D(x)` from a tapered `c=2` contour matched truth to within `~1%`, imaginary part at machine-noise `~1e-9` to `1e-12`, confirming the expected real-valued symmetry). The failure is specific to the critical strip: the integral there is only conditionally convergent, resting on delicate oscillatory cancellation in the `x^{it}` phase that a smooth Gaussian taper destroys rather than respects. **This is a real numerical-analysis obstruction, not a coding bug** — confirmed by first ruling out the coding-bug explanation via the working `c=2` control.

## 5. The correct, convergent dual formula: classical Voronoi summation, verified after finding and fixing a jump-discontinuity bug [N, now matching to a few percent]

Looked up rather than trusted from memory this time (memory had already failed twice on this exact topic): the classical truncated Voronoi formula,

```
Δ(x) = (x^{1/4}/√2π) Σ_{n≤N} d(n) n^{-3/4} cos(4π√(nx) - π/4) + O(x^{1/2+ε}N^{-1/2}),   1≤N≪x
```

confirmed via live source lookup (arXiv:1001.3556, arXiv:1711.09589) to be exactly the formula intended. First implementation still failed, with a discrepancy growing roughly like `x^{1/4}` (`diff≈8` at `x=1000` up to `≈20` at `x=100000`) that did not shrink with more truncation terms and survived a high-precision (`mpmath`, 30 dps) re-implementation — ruling out float64 cosine-of-large-angle precision loss as the cause. The actual bug: comparing against raw `D(x)` at **exact integer** `x`, where `D` has a jump discontinuity from `d(x)` landing exactly there. Perron-formula-derived reconstructions converge to the **symmetrized** midpoint `D(x) - d(x)/2`, the same convention that appears at jump discontinuities of a Fourier series. Confirmed directly: at `x=1000`, raw `Δ=6.56` vs. symmetrized `Δ=-1.44`; the Voronoi sum (`N=1000`) gives `-1.31` — matching the symmetrized value to `0.13`, not the raw value at all.

**Final verification**, symmetrized convention throughout, `x` from `1,000` to `150,000`, `N` up to `~0.8x`:

| x | best-N diff | relative to the formula's own `x^{1/4}` scale |
|---|---|---|
| 1,000 | 0.013 | 0.2% |
| 5,000 | 0.147–0.59 | 2–7% |
| 10,000 | 0.049–0.70 | 0.5–7% |
| 50,000 | 0.03–0.29 | 0.2–2% |
| 100,000 | 0.30–2.93 | 2–16% |
| 150,000 | 0.19–2.29 | 1–12% |

Non-monotonic convergence in `N` (sometimes worse before better) is expected and consistent with the stated `O(x^{1/2+ε}N^{-1/2})` bound, which guarantees control, not monotonicity; every observed discrepancy sits within a few multiples of that scale, nowhere near the order-of-magnitude failure of §4.

## 6. The full, corrected picture

`Λ(n)` (primes) and `d(n)` (divisors) are governed by the same `L`-function family (`ζ(s)` and `ζ(s)²`, sharing a zero set) through **two structurally different mechanisms**: `Λ(n)` via a discrete residue sum over the zeros (a logarithmic-derivative pole at each `ρ`, forced to be prime-power-supported by the Euler-product structure); `d(n)` via a convergent *dual sum over integers themselves* (Voronoi, Bessel-kernel in origin, now numerically verified), with the zeros entering only weakly and indirectly, through moment/magnitude bounds on `ζ(½+it)`, never by name. Both are real, both are now checked — one derived and confirmed exactly (§2), one built, debugged twice, and verified to the expected precision (§5) — and together they fully answer the original challenge: the zeros don't encode HC/divisor structure, for a provable reason, and the actual formula connecting `Δ(x)` to anything is a self-referential sum over `d(n)` itself, not a sum over `ρ`.

## Self-audit note

Two errors of my own, both corrected within the same conversation rather than left standing: (1) initially claiming Voronoi's formula sums over the zeta zeros `ρ` — wrong, corrected in §3 with a direct residue computation showing zeros of `ζ(s)²` contribute nothing; (2) the first Voronoi implementation attempt, which used the correct formula (confirmed via live lookup) but compared against the wrong (non-symmetrized) target, corrected in §5. Recording both because the discipline of catching them is the actual content here, not just the final clean numbers.

## Synchronization

Live ledger head checked immediately before this write: v13.902 (sandbox rigidity/isolated-maximizer result, read in full). No collision on v13.903.
