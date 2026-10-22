# Joint (T, ε) bath generator — sandbox return to v14.713/v14.714 (2026-10-22)

**Priority/relation note (added after live-HEAD check during drafting):**
gravity v14.714 Gate 2 derived the same hot cross-covariance cancellation
independently in (T, q) coordinates (d[T,q]_t/dt = (4D₀T²q/μ)(1−Tv²/μ),
averaged zero; the two formulas are identical under d[T,ε] = −2q·d[T,q],
verified algebraically), and Audit R334 (v14.715) answered the escape
question via the exponential functional of drifted Brownian motion
(a.s. finite physical escape time). My producer was run before I read
v14.714; the ledger return credits v14.714 with the deposited priority
for the hot cancellation and R334 for the escape answer, and positions
this work as: the (T, ε)-coordinate form, the finite-temperature
cross-covariance (not in v14.714), an independent BESQ escape route, and
the survival-conditioned physical-time ε marginal that v14.714's
sandbox handoff explicitly requests (its `survivor_shape=OPEN`).

Producer: `joint_generator.py` (runs clean, ~15 s). Conventions: EFT v3.4
half-covariance (dv_i dv_j = 2 D_ij dt, L f = b·∇f + D:Hess f); hot limit
D = D₀I, friction neglected; finite-Θ Maxwellian Rosenbluth coefficients
per v3.4 (A(v), D_∥(v) = 𝒦G(χ)/v, D_⊥,eig = 𝒦[erf χ − G(χ)]/(2v),
Θ = μ/(2Tσ²)). ε = e², u = |r×v|² = μT(1−ε), T = −μ/(2h).

## 1. Cross covariance [D, with N checks]

Instantaneous (any isotropic D with eigenvalues D_∥, D_⊥; v is an
eigenvector of D):

  d[T,ε]_t/dt = (4 T_h u D_∥(v) / μ²) (v² + 2h),   T_h = 2T²/μ.

Friction contributes nothing (drift only). Derivation: ∇_v T = T_h v,
∇_v ε = (2u/μ²)v + (2h/μ²)∇_v u, v·∇_v u = 2u, Dv = D_∥v.

- Hot limit, orbit-averaged: **exactly 0**. u, T_h are orbit constants and
  ⟨v² + 2h⟩ = ⟨v²⟩ − μ/T = 0 (Kepler virial). Quadrature: |⟨C_Tε⟩| ≤ 6e-17
  at e = 0, 0.3, √(2/3), 0.95 (μ=T=D₀=1); diagonals reproduce the known
  closed forms exactly (⟨C_TT⟩ = 8, ⟨C_εε⟩ = 2Cε(1−ε), C = 10).
- Pointwise Monte Carlo (frozen r, 4×10⁵ velocity kicks, 3 random bound
  states, hot and finite-Θ): all three covariance rates match the analytic
  formulas within MC noise (worst ~3%, on C_TT state 2 hot).

## 2. Joint averaged generator, hot limit [D]

  L̄ = L̄_T + C(T)·J_ε,   no mixed derivative,
  L̄_T f = (14 D₀T²/μ) f′ + (4 D₀T³/μ) f″,
  J_ε g = (1−2ε) g′ + ε(1−ε) g″,   C(T) = 10 D₀T/μ.

The coupling is **one-way**: T drives the ε clock, ε does not drive T.
v14.713's obstruction stands (T is not slow: ⟨ℒT⟩/T = 7C/5), but the
shared-noise cross term it asked for vanishes identically after orbit
averaging — the Jacobi shape operator survives as a time-changed
diffusion, not as a frozen-T approximation.

## 3. Finite temperature [D formula + N table]

The cancellation breaks because D_∥(v) depends on v:

  ⟨d[T,ε]/dt⟩ = (8T³(1−ε)/μ²) · ⟨D_∥(v)(v²+2h)⟩,
  ⟨D_∥(v)(v²+2h)⟩ = (2eμ/T) · ⨍_E D_∥(v(E)) cos E dE   (exact E-identity,
  verified to 6 digits at three (e, Θ) points).

D_∥ decreases with v, so the pericentre-weighted mean is **negative** for
0 < e < 1. Correlation coefficient ρ_Tε = ⟨C_Tε⟩/√(⟨C_TT⟩⟨C_εε⟩)
(𝒦 cancels), μ=T=1:

| e \ Θ | 0.01 | 0.1 | 0.32464 | 1.0 | 3.0 | 10.0 |
|---|---|---|---|---|---|---|
| 0.2000 | −0.0015 | −0.0151 | −0.0469 | −0.1259 | −0.2394 | −0.2222 |
| 0.5000 | −0.0041 | −0.0393 | −0.1178 | −0.2837 | −0.4608 | −0.4657 |
| 0.8165 | −0.0078 | −0.0693 | −0.1747 | −0.3191 | −0.4498 | −0.5236 |
| 0.9500 | −0.0104 | −0.0692 | −0.1305 | −0.2036 | −0.2839 | −0.3695 |

ρ_Tε → 0 as Θ → 0, and vanishes at e = 0 and ε = 1. This is a
generator-level statement at fixed (T, ε); the global finite-Θ
Fokker–Planck problem (friction drift included) is not solved here.

## 4. Stationarity / quasi-stationarity [D averaged model + N simulation]

D₀ dependence (v14.714 handoff asks): in the hot model every generator
coefficient is ∝ D₀, so D₀ is a pure time rescale — survival fractions
and conditioned laws at fixed D₀·t are D₀-independent; the simulation's
D₀ = 1 is without loss of generality. (Finite-Θ coefficients are not
∝ a single constant; the §3 table is the finite-Θ content.)

Scale sector: the orbit-averaged energy process is
dy = −3D₀ dt + √(4D₀y) dW (y = −h), i.e. **BESQ(δ = −3)** in D₀-scaled
time. Escape (y = 0, h = 0) is a.s. in finite time; E[t_esc] = y₀/(3D₀).
This is an independent route to R334's escape answer (exponential
functional of the ln T Brownian motion): finite mean escape time here,
a.s.-finite there — consistent.
Simulation (μ=D₀=1, y₀=0.5, 30,000 paths): 99.8% escaped by t = 1.6,
mean escape 0.1608 vs 0.1667 predicted. **No joint stationary law.**

Shape sector: ε is a Jacobi diffusion on the clock τ(t) = ∫C(T_s)ds
with Brownian motion independent of the scale process (§1). Doob
h-transform (verified symbolically, Part 4b): BESQ(−3) conditioned to
survive forever is BESQ(4−δ) = BESQ(7); hence survivor y grows
unboundedly (median T falls 1.61 → 0.17 over t = 0.1 → 1.6; y quartiles
at t = 1.6 are [1.29, 2.97, 5.07] from 0.5), τ ~ (5/7) ln t → ∞, and the
survivor ε law relaxes to the **uniform Jacobi law**:

| t | surv% | E[ε\|surv] | sd[ε\|surv] | E[W\|surv] |
|---|---|---|---|---|
| 0.05 | 92.4 | 0.5495 | 0.2819 | 0.5364 |
| 0.10 | 58.3 | 0.5222 | 0.2870 | 0.5244 |
| 0.20 | 22.4 | 0.5119 | 0.2887 | 0.5198 |
| 0.40 | 6.1 | 0.4883 | 0.2872 | 0.5097 |
| 0.80 | 1.25 | 0.4835 | 0.2920 | 0.5044 |

(targets: E[ε] = 1/2, sd = 1/√12 = 0.2887, E_π[W] = (8 ln2 − 4)/3 =
0.5151; ε₀ = 2/3 start.)

Verdict: **a quasi-stationary eccentricity law exists only as a
survival-conditioned marginal — the uniform Jacobi law — and there is no
joint QSD** (the conditioned scale marginal is not tight: y → ∞,
T → 0). This is exactly the v3.4 BPS channel split, carried
independently here:
- **Bound-preserving (conditioned):** survivor moments → Jacobi values
  above.
- **Killed (cemetery):** unconditional E[ε·1_surv] decays with survival
  (0.508 → 0.0010 over the same window); killed moments are not survivor
  moments. The draft's bound-vs-kill fold endpoints differ at O(1/L_C)
  [draft-reported numerics, not recomputed].

## 5. Ξ link [negative, concurs]

No instrument rule connecting this process to Ξ = (1 − RΦ″/Φ′)/3 is
produced; the cross-covariance is a property of the stochastic (T, ε)
process, Ξ a static field-response ratio. Concurs with the v14.708 and
v14.710 (sandbox) negatives. G_derived = false throughout.
