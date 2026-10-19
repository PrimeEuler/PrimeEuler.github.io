# Overlay P in the distribution class — closure note

*Sandbox (little Euler), 2026-10-18. [I]/[O] exploratory; nothing here
touches the ledger's certified Suzuki objects (v13.258 exact, v13.753
[D]) — v13.258's closed form is used read-only. Continues the sandbox
reports `20260928-005525-spherical-archimedean/` (PRODUCT_FORM_BRIEF)
and `20260928-010240-spherical-archimedean-2/` (archimedean_report_2
§§3–4, STATUS). Producer: `overlay_P.py` (deposited alongside).
Workspace run: `lane_b/sandbox/runs/20261018-overlay-P/`.*

## Brief step 2 — discharged in the distribution class

The product-form brief asked: exhibit P, a helix overlay, with
E·P = A₁₂ verified and E ≥ 0. Report 2 §3 proved P cannot be a finite
sum, an ℓ¹ spectrum, or a finite signed measure
(T̃(x) ~ −s·log(L/x) at the centre, s = 0.24060639745313878…), and
§4/STATUS prescribed the construction: P as the measured 1/n tempered
distribution, its conditional convergence studied directly. This note
carries that out, with one strengthening: the 1/n part is resummed in
closed form.

With the D_exp dictionary (L = 12/11, x = Le^{−t}) and
T̃(x) = a₀/2 + Σ_{n≥1} aₙ cos(πnx/L),
aₙ = 2∫₀¹ T(−log u) cos(πnu) du, the analytic split
aₙ = −s/n + rₙ gives

**P(x) = a₀/2 + s·log(2 sin(πx/(2L))) + Σ_{n≥1} rₙ cos(πnx/L)**,

since Σ_{n≥1} (−s/n)cos(πnx/L) = s·log(2 sin(πx/(2L))) exactly. The
log kernel is the distribution-class heart (it *is* the centre dive);
the remainder is an honest helix overlay provided
rₙ = O(n^{−3/2} log n) is summable — verified below.

## Numbers

- **Coefficients.** a₀/2 = 0.035905161267. aₙ for n ≤ 512 by
  Clenshaw–Curtis on the log-subtracted integrand
  h(u) = T(−log u) − s·log u over 8192 Chebyshev–Lobatto points
  (dps 30). Independent mpmath quadrature anchors (dps 40) at
  n ∈ {1,2,3,5,8,13,21} agree with the grid values to
  **≤ 8×10⁻¹³**. The coefficients are not the error source anywhere
  below.
- **Tail law.** Fit on n ∈ [48,512]:
  rₙ ≈ A·n^{−3/2} + B·(−1)ⁿ(log n)n^{−3/2} + C·n^{−5/2} with
  **A = 0.150064** (predicted 0.15 = 2 × report 2's 0.075 transient
  in cₙ units), B = −0.014744 (predicted ≈ −2K ≈ −0.015 from report
  2's cusp fit), C = −0.0008; Σ_{n≤512}|rₙ| = 0.3920. rₙ is
  absolutely summable, as required.
- **Centre constant.** a₀/2 + s·log π + R(0) = 0.7163830844 vs the
  exact ζ(2,1/4)/24 = 0.7165553814: agreement to **1.7×10⁻⁴**,
  limited by the fitted tail beyond n = 512 (see error budget).
- **Product.** On 78 t-points in [0.02, 30]:
  max |Ã(t)·P(x(t)) − A₁₂(t)| = **1.03×10⁻³** (at t = 30, where
  |A₁₂| ≈ 41); rms 2.2×10⁻⁴; max relative error where |A₁₂| > 1:
  **3.5×10⁻⁵**.
- **Sign change.** The reconstructed P vanishes at
  t = 1.912049582569 vs the exact t₀ = 1.912049280865:
  **3.0×10⁻⁷**. With E = Ã ≥ 0 this is sign(P) = sign(A₁₂) made
  quantitative — positivity-neutrality verified, not assumed.
- **Error budget (complete).** Everywhere, the product error equals
  Ã × (P error), and the P error is the rₙ tail-model error beyond
  n = 512 (~1.7×10⁻⁴, uniform in x — the kernel is exact and the
  coefficients are 1e-12-accurate). Tightening means computing more
  coefficients, nothing else.

## Conditional convergence, as prescribed

Raw partial sums P_N (no kernel split) at the centre obey
P_N(0) + s·log N → a₀/2 + R(0) − sγ = 0.30207197 with the values
0.26294 (N=64), 0.28303 (256), 0.29275 (1024), 0.29753 (4096) —
approach like 0.3/√N, exactly the rate the rₙ tail
(Σ_{n>N} rₙ ~ 2A/√N) predicts. Crossover: the 512-mode raw sum
tracks T̃(x) with errors 0.111 / 0.0168 / 0.0050 / 0.0012 at
x = c·L/512 for c = 0.5 / 1 / 2 / 4 — resolution down to a few
times L/N, degrading inside, as §3's analysis requires.

## Honest scope

- The verification is numerical, at the stated tolerances, on
  t ∈ [0.02, 30]. It is not a proof; report 2's §3a remains the
  proof of the class statement.
- P is the quotient's own spectral distribution, exhibited with
  measured coefficients and a fitted tail — the construction the
  2026-09-28 report prescribed. It is not an independent derivation
  of the phase from helix geometry first principles; the "infinity
  of helices" is realised as (closed-form log kernel) + (ℓ¹ helix
  series), which is the strongest form the obstruction permits.
- Sanity anchors reproduced on the way in: s to 20 digits;
  t₀ = 1.91204928086509854 (STATUS digits); bump max 0.4410119 on a
  coarse scan (STATUS refined value 0.4410124); T(30) = tail
  formula to all printed digits.
- First computational attempt crashed at grid point ~7000 on the
  unguarded endpoint u = 1 (T = 0/0); fixed (analytic endpoint,
  t = 0 guard, checkpointed grid) and rerun clean.
