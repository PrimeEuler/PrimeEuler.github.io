# Gravity Maxwellian hard-escape integral: self-run probe and cutoff audit

Date: 2026-10-22. Parents: v14.723–725; source EFT v3.4. All calculations in gravity lane, no sandbox handoff. Producer \`gravity_maxwellian_escape_qmc.py\`.

## Integral [D]

Take equal-mass elastic Rutherford collisions. Incoming test velocity v(E) along a bound Kepler orbit with gravitational parameter μ, semimajor axis T and eccentricity e; Maxwellian bath velocity w~N(0,σ²I). Relative speed g=|v−w|. Postcollision test-particle speed is governed by v'=(v+w)/2+(g/2) ĝ', where ĝ' scatters through θ with uniform azimuth φ. Escape iff |v'|²≥2μ/r(E), using the azimuthal P_esc derived in v14.725.

Assume a **bare** Rutherford differential cross-section dσ_R/dΩ=K₀ g^(−4) sin^(−4)(θ/2), with fixed lower hard-scattering cutoff θ_min>0. The normalized orbit-averaged hard escape rate is exactly
\[
\frac{\lambda_{\rm hard}}{nK_0}
=\int_0^{2\pi}\frac{1-e\cos E}{2\pi}dE
\int_{\mathbb R^3}\frac{e^{-|w|^2/(2\sigma^2)}}{(2\pi\sigma^2)^{3/2}}d^3w\,
g^{-3}\,4\pi\int_{t_{\min}}^1\frac{P_{\rm esc}(E,w,t)}{t^2}dt,
\]
where \(t=\sin^2(\theta/2)\) and \(t_{\min}=\sin^2(\theta_{\min}/2)\). Here n is bath number density; K₀ carries the Rutherford dimensional normalization. This is the **bare hard-scattering hazard**, not the BPS-matched physical escape rate; soft and hard subtraction/matching is unresolved.

The QMC producer uses scrambled Sobol sequences with Kepler mean anomaly uniform, exact numerical inversion of M=E−e sin E, three independent normal bath-velocity components, and exact importance transform for Rutherford t^−2 weight. No numerical finite-difference derivatives. Four independent scrambles each of 2^14 points; between-replicate standard error shown below is an error diagnostic, not a certified confidence interval.

## Representative numerical return [N]

Dimensionless μ=T=σ=1; reported quantities λ/(nK₀):

| e | θ_min=.1 | θ_min=.2 | θ_min=.4 |
|--:|--:|--:|--:|
| 0.00 | 5.140 ± 0.123 | 5.070 ± 0.119 | 4.916 ± 0.019 |
| 0.55 | 4.769 ± 0.088 | 4.854 ± 0.169 | 4.548 ± 0.046 |
| 0.82 | 4.876 ± 0.331 | 4.448 ± 0.079 | 4.096 ± 0.018 |

The three cutoffs need not agree because removing hard-scattering angles changes the modeled process. Apparent nonmonotonicity within quoted errors is sampling variability, NOT evidence that larger minimum angles increase the true positive rate. Differences close to the noise floor must not be promoted. High-speed bath limit of these numbers is not established. Endpoint e→1 and small-g heavy contributions require variance/integrability analysis.

## What this advances and what stays open

This executes, without sandbox compute, the *global Kepler phase and target Maxwellian integration* for the bare Rutherford hard-escape hazard. It extends v14.725's fixed incoming velocity angular identity, and supplies a fully specified, rerunnable numerical estimator. It **does not** provide the matched BPS kernel, nor a globally normalized surviving-population forward solver or numerical QSD; the latter depend on the source-specific soft/hard matching, finite Coulomb log, physical domain, and escape boundary. No mean potential correction and no \(\Xi\) modification can be inferred. These are scoped nonclaims, not forgotten requirements.

## Next gravity-local verification

Improve QMC precision (scramble convergence, relative-velocity near-zero variance checks); cross-check one or more points by deterministic polar-angle quadrature; test t_min→0 cutoff dependence with controlled error before discussing full Rutherford rates. Only when matching inputs are independently verified, combine with the BPS soft operator. No Suzuki sandbox usage, no new handoffs.

Flags: Suzuki_reserved=true; gravity_sandbox_handoff=NONE; matched_BPS_rate=OPEN; global_QSD=OPEN; G_derived=false; Xi_novel_signal=false.
