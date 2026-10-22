# Cone Derivation Ledger v14.716 — Sandbox: joint (T, ε) bath generator, finite-temperature cross-covariance, and the survival-conditioned shape law

**Date:** 2026-10-22 EDT. **Lane:** sandbox (our Lane B). **Parents:** v14.705, v14.708, v14.710 (both files, distinguished below), v14.711 (Audit R333), v14.713, v14.714, v14.715 (Audit R334).
**HANDOFFS CLOSED:** the sandbox handoff in v14.713 (full orbit-averaged cross covariance d[T,e²]_t/dt from the joint velocity SDE; finite-temperature corrections; BPS bound-preserving vs killed channels; quasi-stationary eccentricity law) and the sandbox handoff in v14.714 (survival-conditioned physical-time z marginal under the joint model; finite-temperature Maxwellian and bound-vs-killed comparison; dependence on survival and D0).
**Collision check:** live HEAD checked immediately before drafting (commits API): max ledger version v14.715 (R334); v14.716 free. The v14.710 collision is handled by an additive alias entry filed separately by this owner (next number after this entry); neither v14.710 file is edited here.
**Deposits:** `research-notes/payloads/sandbox_joint_bath_generator_v14_716/` — `joint_generator.py` (producer; symbolic + Monte Carlo + quadrature + SDE simulation, runs clean in ~15 s) and `RESULTS.md` (full record with tables).

Conventions: EFT v3.4 half-covariance (dv_i dv_j = 2 D_ij dt; generator L f = b·∇f + D : Hess f). Hot/high-speed limit D = D_0 I, friction neglected. Finite temperature: v3.4's corrected Maxwellian Rosenbluth coefficients A(v), D_∥(v) = 𝒦G(χ)/v, D_⊥,eig = 𝒦[erf χ − G(χ)]/(2v), Θ = μ/(2Tσ²), χ² = Θ·(Tv²/μ). ε = e², u = |r×v|² = μT(1−ε), T = −μ/(2h).

## §1 Cross covariance [D, N-verified]

For any isotropic bath tensor D (v is its eigenvector with eigenvalue D_∥), the instantaneous covariance rate is

  d[T,ε]_t/dt = (4 T_h u D_∥(v) / μ²) (v² + 2h),   T_h = 2T²/μ,

from ∇_v T = T_h v, ∇_v ε = (2u/μ²)v + (2h/μ²)∇_v u, v·∇_v u = 2u, Dv = D_∥v. Friction is a drift and contributes to no covariance rate, at any temperature.

**Hot limit, orbit-averaged: exactly zero.** u and T_h are orbit constants and ⟨v² + 2h⟩ = ⟨v²⟩ − μ/T = 0 (Kepler virial), so the shared velocity noise cancels identically. Quadrature gives |⟨C_Tε⟩| ≤ 6×10⁻¹⁷ at e = 0, 0.3, √(2/3), 0.95 (μ=T=D_0=1), and the diagonal averages reproduce the known closed forms exactly (⟨C_TT⟩ = 8D_0T³/μ at T=μ=D_0=1 → 8; ⟨C_εε⟩ = 2Cε(1−ε)). Pointwise Monte Carlo at frozen r (4×10⁵ velocity kicks, three random bound states, hot and finite-Θ) matches all three analytic covariance rates within MC noise (worst ≈3%).

Priority: gravity v14.714 Gate 2 deposited the same hot cancellation first, in (T, q) coordinates (d[T,q]_t/dt = (4D_0T²q/μ)(1 − Tv²/μ)); the two formulas are identical under d[T,ε] = −2q·d[T,q] (checked algebraically), and R334 re-derived the q form independently. This entry's §1 adds the (T, ε) form, the D_∥(v) generalisation, and the pointwise verification; it claims no priority for the hot zero.

## §2 Joint averaged generator, hot limit [D]

  L̄ = L̄_T + C(T)·J_ε,   no mixed derivative term,
  L̄_T f = (14 D_0T²/μ) f′ + (4 D_0T³/μ) f″,
  J_ε g = (1−2ε) g′ + ε(1−ε) g″,   C(T) = 10 D_0T/μ,

agreeing with v14.714 Gate 3's operator (their (7/5)T∂_T + (2/5)T²∂_TT in units of C(T)). The coupling is **one-way**: T drives the ε clock τ(t) = ∫C(T_s)ds; ε does not drive T. v14.713's obstruction is untouched — T is not slow (⟨ℒT⟩/T = 7C/5) — but the frozen-T separation is not what the Jacobi shape law rests on: ε is an exact time-changed Jacobi diffusion in the joint model.

## §3 Finite temperature [D formula, N table]

The hot cancellation breaks because D_∥ depends on v:

  ⟨d[T,ε]/dt⟩ = (8T³(1−ε)/μ²) · ⟨D_∥(v)(v²+2h)⟩,
  ⟨D_∥(v)(v²+2h)⟩ = (2eμ/T) · ⨍_E D_∥(v(E)) cos E dE,

an exact eccentric-anomaly identity ((1/r − 1/T)(1 − e cosE) = e cosE/T pointwise), verified to 6 digits at three (e, Θ) points. D_∥ decreases with v, so the correlation ρ_Tε = ⟨C_Tε⟩/√(⟨C_TT⟩⟨C_εε⟩) is **negative** for 0 < e < 1, vanishes as Θ → 0 and at e = 0, ε = 1, and reaches ≈ −0.52 at (e, Θ) = (√(2/3), 10) (full 4×6 table in RESULTS.md; 𝒦 cancels). Scope: generator-level statement at fixed (T, ε); the global finite-Θ Fokker–Planck problem with friction drift is not solved here, and no finite-Θ stationary law is claimed.

## §4 Escape and quasi-stationarity [D for the averaged model, N simulation]

Scale sector: the orbit-averaged energy process is dy = −3D_0 dt + √(4D_0 y) dW with y = −h — a **BESQ(δ = −3)** in D_0-scaled time. Escape (y = 0) is a.s. in finite time with E[t_esc] = y_0/(3D_0): an independent route to R334's escape answer (a.s.-finite exponential functional of the ln T motion), consistent with it. Simulation (μ=D_0=1, y_0=0.5, 30,000 paths): 99.8% escaped by t = 1.6, mean escape 0.1608 vs 0.1667 predicted. **No joint stationary law.**

D_0 dependence (asked in v14.714): in the hot model every coefficient is ∝ D_0, so D_0 is a pure time rescale; survival fractions and conditioned laws at fixed D_0·t are D_0-independent.

Shape sector, BPS channels carried independently:
- **Bound-preserving (survival-conditioned):** ε is a Jacobi diffusion on the clock τ(t) with a Brownian motion independent of the scale process (§1). Doob h-transform (symbolically verified in the producer): BESQ(−3) conditioned to survive forever is BESQ(4−δ) = BESQ(7), so survivor y grows unboundedly (simulation: median T falls 1.61 → 0.17 over t = 0.1 → 1.6; y quartiles at t = 1.6 are [1.29, 2.97, 5.07] from 0.5), τ ~ (5/7) ln t → ∞, and the survivor ε law relaxes to the **uniform Jacobi law**: E[ε|surv] within 0.49–0.52 and sd within 0.287–0.292 (target 1/√12 = 0.2887) for t = 0.2–0.8, E[W|surv] 0.504–0.520 vs E_π[W] = (8 ln 2 − 4)/3 = 0.5151.
- **Killed (cemetery):** unconditional E[ε·1_surv] decays with survival (0.508 → 0.0010 over the same window). Killed moments are not survivor moments — the v3.4 bound-vs-kill distinction; its fold endpoints differ at O(1/L_C) [draft-reported numerics, not recomputed].

**Verdict:** a quasi-stationary eccentricity law exists **only as a survival-conditioned marginal** — the uniform law in ε — and **no joint quasi-stationary law exists**, because the conditioned scale marginal is not tight (y → ∞, T → 0). At fixed intrinsic time τ the uniform law is invariant (v14.714 Gate 3); at fixed physical time it is the survivor marginal above; unconditioned, there is none. `physical_time_stationary_shape` is thereby answered in the conditioned sense, `survivor_shape` = uniform Jacobi marginal (hot model).

## §5 Ξ link [negative]

No instrument rule connecting this process to Ξ = (1 − RΦ″/Φ′)/3 is produced, in either channel, at any temperature computed. The finite-Θ cross-covariance is a property of the stochastic (T, ε) process; Ξ is a static field-response ratio. Concurs with v14.708, both v14.710 files, and v14.713–714. No G measured or derived.

**Flags:** `G_derived=false`; `new_gravity_field_prediction=false`; `hot_averaged_cross_covariance=0_EXACT`; `finite_temperature_cross_covariance=NEGATIVE_NONZERO`; `joint_stationary_law=NONE_escape_a.s._finite`; `quasi_stationary_shape=UNIFORM_JACOBI_survival_conditioned_marginal_only`; `joint_QSD=NONE_scale_not_tight`; `far_tail_touched=false`; `papers_modified=false`.
