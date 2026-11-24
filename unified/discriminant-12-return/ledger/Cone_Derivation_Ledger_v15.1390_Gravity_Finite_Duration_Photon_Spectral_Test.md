# Cone Derivation Ledger v15.1390 — Finite-duration source spectral test of phase-matched EM output

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Preledger inspected live HEAD:** d048d7c88b2b6936e5ac3a5d1953f84041d710ae. **Parents:** v15.1388 detuned/off-shell steady response negative, v15.1389 exact null outgoing Fourier vector and nonzero transverse Weyl–H² current. **Status:** [N PASS] a finite-duration prescribed electromagnetic source pulse excites genuine free vacuum Maxwell modes *after the pulse* and favors the phase-matched channel; [NEGATIVE] the pulse envelope is externally prescribed rather than derived from a localized finite-energy coupled H²/TT initial-value solution, therefore no unique emitted radiation flux or quarter-grid physics is established; [OPEN] self-consistent localized packets, full energy exchange and metric variation, EFT cutoff and independent physical target selector. All files additive, no changes to certified prior material.

## Gate 1306 — finite-time forcing removes the infinite monochromatic switching ambiguity

For either already-derived v15.1388/1389 transverse-current geometry, take an **equal-normalized** positive spatial Fourier current amplitude J0=.02 i and a prescribed time envelope `e^(−t²/(2σ²))e^(−iωt)`, with ω=1. Solve the linear Maxwell transverse oscillator `A''+k²A=−J0 exp(−i ωt−t²/(2σ²))`, with zero initial A and derivative at t=−8σ and observe at t=+8σ, after the source amplitude is exponentially negligible.

For a free photon k=|q|, the retarded Green function gives two outgoing free-wave coefficients. In the asymptotic full Gaussian limit, the exact answer is

`A(t) = J0/(2 i k) [ e^(−ikt) I_minus − e^(+ikt) I_plus ]`,
`I_±=sqrt(2π) σ exp[−σ²(k∓ω)²/2]`.

The resulting post-pulse **free oscillator** mode energy `E=(|A'|²+k²|A|²)/2` is `|J0|²(I_minus²+I_plus²)/4`. This is a free Maxwell *Fourier mode* after the source is removed. It does not establish a globally localized field or quantized photon count because the spatial harmonic retains infinite/periodic extent. To compare pure spectral phase matching rather than different tensor amplitudes, the transverse current amplitudes are **normalized equal**; the actual Weyl–H² tensor sources have different geometric prefactors, which must be restored in a future common finite-packet experiment.

Compare the **phase-matched k=1, ω=1 branch** of v15.1389 against **detuned k=√3, ω=1** of v15.1388/1385. The Gaussian spectral transform suppresses the detuned branch by `exp[−σ²(√3−1)²/2]` in its positive-frequency amplitude; phase-matched branch is not so suppressed.

## Gate 1307 — independent ODE and analytic pulse verification

The actual executed Python/NumPy/SciPy test `/mnt/data/cone_gate/k4_quarter_weyl_finite_duration_em_v15_1390.py` solved the forced oscillator using DOP853 with strong tolerances and compared final A and A' against independent analytic Gaussian Fourier integrals:

| σ | phase-matched postpulse free energy | detuned postpulse free energy | phase-matched/detuned |
|---:|---:|---:|---:|
| .5 | .00021486600016902094 | .0001616898795155062 | 1.3288772359337129 |
| 1 | .0006398265860335082 | .00036801663743736893 | 1.738580599205647 |
| 2 | .00251327440570217 | .00029463817380672407 | 8.530036597874181 |
| 3 | .0056548667764564665 | .000045476075113457185 | 124.34817126034454 |

Largest complex A/A' deviation between analytic Gaussian and independent numerical ODE across all eight tests = **2.24e−13**. All tests PASS. A *short* pulse has large bandwidth and can excite both branches; a *longer* pulse is spectrally narrower and increasingly favors the phase-matched branch. This is standard coherent driven-wave kinematics of the specified extra EFT, not automatic gravitational conversion or an intrinsic 1/4-grid parameter.

**Reproducer** (additive): `research-notes/k4_quarter_weyl_finite_duration_em_v15_1390.py` at **d048d7c88b2b6936e5ac3a5d1953f84041d710ae**, separately authored equivalent to the locally executed version. Exact committed-byte external Audit replay still pending.

## Audit, remaining physical gate and novelty verdict

**AUDIT:** first exact-replay v15.1388/1389/1390 committed scripts; independently verify the 4-vector nulls, TT Ricci, current Ward identity, transverse polarizations, forced Maxwell Green functions, adiabatic tanh switch and Gaussian Fourier limits. Probe one or two wavelengths and orientations away from perfect phase matching to ensure source selection is geometric, not a hardcoded projection. Analyze whether the Weyl–F–H²-area operator survives *general* on-shell EFT field redefinitions, and whether its higher-derivative metric equations are well posed below cutoff.

**NEXT:** replace the prescribed Gaussian **current** with localized positive-energy H² initial data and a genuine finite, sourced gravitational tidal packet; evolve the coupled Maxwell and internal sigma equations, track energy transfer with the full metric coupling's stress tensor and Einstein/Bianchi equations, and construct a finite-arm event-anchored clock/optical output. Even when finite-pulse free EM radiation is achieved, it is reproduced by the **same enlarged conventional EFT** and its amplitude contains free ζ/Λ² and f. The radius r=1/4 does not select those coefficients (v15.1387). A distinct Cone-specific gravitational prediction remains unestablished.
