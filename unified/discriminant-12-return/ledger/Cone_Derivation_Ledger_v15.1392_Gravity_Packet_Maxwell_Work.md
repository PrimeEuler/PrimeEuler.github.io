# Cone Derivation Ledger v15.1392 — Maxwell mode energy/work driven by finite-periodic-energy H² and TT free-wave packets

**Date:** 2026-11-24 Eastern. **Gravity/Cone.** **Parent:** v15.1391 periodic finite-energy real free internal+TT wave packets and direct Weyl–area source. **Status:** [N PASS] actual time history of one transverse Maxwell Fourier mode, sourced by finite periodic H²/TT free packets, yields a nonzero Maxwell response; the increase in its quadratic energy matches the work supplied by the **externally prescribed** Weyl–H² current within about 4×10−9 relative error; [NEGATIVE] this is *not* total Einstein–Maxwell–sigma–Weyl interacting energy conservation, no incoming sigma or GW energy debit has been computed, and current/curvature remains a perturbative prescribed background; [OPEN] full interacting variational stress, principal-symbol/EFT cutoff, backreaction, finite radiation readout, quarter-grid-specific coupling selection. Strictly additive; Audit Round 633 independently certified the earlier v15.1384–1390 source family but has **not** yet independently certified v15.1391/1392. **Before ledger HEAD:** 84251afa30d4ff619c6a65ef2fa8acec8a71bfe7.

## Gate 1310 — source is a dynamic packet product, not a prescribed Gaussian current

Use the v15.1391 **real free-wave** packet solver, whose two internal H² coordinate fields and TT gravitational field are distinct localized Gaussian initial-value data evolved exactly by the Fourier propagator on a finite periodic cell, with leading curvature area source `J^nu(t,x)=−partial_mu[C^{mu nu rho sigma}(t,x)B_rho sigma(t,x)]`. At every sampled time, calculate K independently from full space-time packet derivatives, differentiate it in time with centered steps dt=.0008, and take the Fourier transverse projection at q=(.5,.5,−1/sqrt2), |q|=1. The source is **not** assumed to be Gaussian in time. Sample a finite observation window t∈[−.8,.8] with 17 source times. Cubic-spline interpolate the computed 3-vector transverse J(t) and solve the **driven Maxwell transverse mode**

`A''+|q|² A=−g J_T(t)`, `A(t_initial)=A'(t_initial)=0`,

with an arbitrary illustrative g=.05 and an independent solve_ivp high-accuracy DOP853 integrator. This is a source-driven linear Maxwell solution in a fixed finite periodic box; the incoming sigma and GW packet propagation is **not** adjusted by the photon field's acquired energy.

## Gate 1311 — verify source work matches photon mode energy

For one complex Fourier mode define normalized transverse oscillator energy `E_A(t)=[|A'|²+|q|²|A|²]/2`. From its own Maxwell equation derive the independent work identity

`dE_A/dt=−Re[A'^*(t)·g J_T(t)]`.

Integrate the RHS directly from the ODE dense solution with 1,281-point Simpson quadrature and compare with the **separately computed final oscillator energy**. The source satisfies the Fourier Ward identity to ~1e−22; at the selected q, it is exactly transverse to ~1e−14 numerical. The comparison for N12 and N16 and g=.05, and amplitude scaling g/2 at N16, was **actually run** in `/mnt/data/cone_gate/k4_quarter_h2_packet_maxwell_work_v15_1392.py`:

| N³ | g | final transverse photon-mode E_A | independently integrated source work | relative work residual |
| --- | ---: | ---: | ---: | ---: |
| 12³ | .05 | 2.2331216491689654e−16 | 2.2331216495901410e−16 | 1.8860405373913655e−10 |
| 16³ | .05 | 2.2369024584693060e−16 | 2.2369024638538520e−16 | 2.4071439068738360e−9 |
| 16³ | .025 | 5.5922561893518880e−17 | 5.5922561668889420e−17 | 4.0167949041072520e−9 |

Thus the output is nonzero and its magnitude scales as the square of the arbitrarily chosen g, with energy ratio ≈4 between g=.05 and .025. The integrated source work matches within ≈4×10−9 relative. An initial numerical attempt used ODE absolute tolerance 1e−14 while the mode's field energy was ~2e−16, causing 2.6e−6 and 8.4e−6 *relative* work discrepancies; this was a **numerical precision floor, not physical energy violation**. Tightening ODE atol to 1e−19 and increasing Simpson quadrature to 1,281 points reduced the discrepancy to ~1e−9. The trial is thereby independently falsifiable with numerical tolerances, rather than a perfect source=geometry algebraic substitution.

**Crucial limitation:** This identity is the energy budget for the driven Maxwell *mode*, not the **total** coupled EFT energy. It validates that the EM energy gain is supplied by *work done by the externally held packet-induced source*. The source packet's own sigma/GW energies are held constant by separate free evolution, so the combined fields' energies are **not** conserved under this one-way approximation. Full conservation is open until Maxwell sigma/Einstein stress variations yield a compensating loss and metric backreaction; no perpetual energy generation is inferred.

**Other caveats:** An observation-window final field is not necessarily a post-interaction freely propagating photon; the packets remain overlapping and continue to drive after t=.8. This is a finite periodic box, not asymptotic radiation at spatial infinity. The on-shell carrier kinematics remain true, but broad packet spectra can also produce off-shell forcing.

## Gate 1312 — provenance, independent Audit, next test

The new additive GitHub reproducer `research-notes/k4_quarter_h2_packet_maxwell_work_v15_1392.py` (source SHA **16b92232bc8bc4538aad776a290f3342518d1813**) imports the v15.1391 packet source and repeats the same spline-sampled packet-current-driven Maxwell ODE and work quadrature with the exact tested tolerance choices. The locally executed code is under `/mnt/data/cone_gate/k4_quarter_h2_packet_maxwell_work_v15_1392.py`. **The exact committed bytes of these new v15.1391/v15.1392 source artifacts are pending independent Audit replay**. Both existing original scripts and all Suzuki, Sandbox, Muse and Audit files remain untouched.

**AUDIT:** replay v15.1391 then v15.1392 exact GitHub files, check complete Riemann/Weyl contraction, physically real and transverse incoming fields, source current conservation, spline interpolation and time derivative errors, and work balance independently. Inspect nonlinear-product aliasing and cell boundaries (3N zero padding for a cubic source). Compare strict N16/24/32 consistency without overstating it as a continuum limit. Audit the factor of 2 for real ±q Maxwell mode energies and clarify which Fourier normalization is meant; this ledger's single complex-mode energy/work is self-consistent, but physical real-field total energy requires both conjugate modes.

**NEXT:** derive the explicit first-order sigma field response to the Maxwell field including its force and conserved stress, then the Weyl interaction's metric-variation contribution and full Noether/Bianchi accounting in a perturbative coupled run. Test the actual local optical readout only after that. A unique physical quarter-grid interaction still requires an independent parameter selector surviving v15.1387's radius degeneracy and comparison to the identical enlarged effective theory; **no such selector has been derived**.
