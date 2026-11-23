# Cone Derivation Ledger v15.1345 — Full 3D Fourier physical TT propagation with both helicities and a common dealiased Maxwell source

**Date:** 2026-11-23 Eastern. **Gravity/Cone lane.** **Prewrite live HEAD:** 29295e1c4a244ea24f68ac3fe4abfe4b17395e6e. **Status:** [N] independently locally executed full 3D nonzero-mode TT physical Einstein source/propagation across 16³,24³,32³, plus 24³ temporal refinement; [PASS] symmetric/transverse/tracefree Fourier source and evolved physical metric, corrected TT Einstein equation, real-field conjugacy; [NEGATIVE] original archived negative-forced gamma interpreted as physical spatial strain has a finite Einstein residual; [OPEN] complete five-helicity nonzero scalar/vector/tensor metric assembled in one test with homogeneous k0 and independent all-component Einstein checks, spatial accuracy, optical observer readout and physical quarter-grid selector. Strictly additive; do not change past source/certification objects.

## Version precedence and Audit return

External Audit Round 626 landed DURING this gate (canonical **v15.1344**, commit **c5d6a13345fe212889253d818ae551550af055f3**, UTC 2026-11-23T17:29:48Z). It **PASSed** exact committed-byte independent replay of the preceding Gravity v15.1343 physical TT sign repair, including the full 31-slice three-grid evolution; it also noted Gravity's previously used v15.1343 collided with an earlier Audit liveness file by ~4 minutes. While the Audit commit arrived, this gate's independent reproducer was committed under the filename `research-notes/k4_fullgrid_tt_physical_metric_v15_1344.py` at SHA **29295e1c4a244ea24f68ac3fe4abfe4b17395e6e**, UTC 17:31:40Z. **This v15.1344 filename is NONCANONICAL by precedence:** Audit already owned the numbered ledger slot. No historical file is overwritten or renamed. The actual canonical Gravity ledger is therefore **v15.1345**, target absent before creation. Refer to the reproducer by exact GitHub path/SHA and disclose its older conflicting filename, not by claiming canonical v15.1344 priority.

## Gate 1258 — one true Maxwell stress feeds the full TT projector in every Fourier direction

Initialize the original compact E0 of v15.1078 on L=4π, with v15.1267's transverse Fourier Gauss projection and common Nyquist-plane zeroing. Evolve the true source-free Maxwell conformal fields analytically: `Ehat=h cos(|q| sqrt3 log tau)`, `Bhat=−i(q×h) sin(|q| sqrt3 log tau)/|q|`. Reconstruct on 2N³ via zero-padded FFT with inverse normalization factor 8, form physical positive Maxwell conformal quadratic stress `Tij=rho δij−EiEj−BiBj`, transform the quadratic product on the 2N³ grid, and project its Fourier coefficients to original **strictly interior nonzero non-Nyquist** modes.

For any nonzero q, let `n=q/|q|` and `Qij=δij−ni nj`. Construct the full two-helicity TT source directly as

`Tij_TT=Qia Qjb Tab−(1/2)Qij Qab Tab`.

This is independent of choosing a transverse polarization frame, includes both real symmetric TT polarization degrees of freedom, and is Hermitian (real-space IFFT imaginary leakage ~1e-17); at t=1.08, max Fourier trace, divergence, and antisymmetry are ~1e-20–1e-19. All excluded N-Nyquist modes and k0 are set identically zero (controlled truncation, not a claim about the true homogeneous tensor).

## Gate 1259 — entire finite-time TT field and Einstein equation

Evolve the **physical metric tensor strain** `hij(q,tau)`, `gij=a²(δij+hij)` for each retained nonzero q, all nine tensor matrix components (with TT projector ensuring two independent helicities), with zero propagating data at tau=1:

`hij''+3hij'/tau+(3|q|²+2)hij/tau²=+18 Tij_TT/tau⁴`.

This uses the independently verified physical-sign repair v15.1343, **not** the archived incompatible negative-source gamma interpreted directly as metric strain. Source is independently formed from the Maxwell field on 13 common time samples t=1 to 1.08; cubic-spline interpolate and integrate all tensor modes with fourth-order RK4. At final time, independently check the linearized Einstein TT spatial equation

`Cij_TT=(hij''+3hij'/tau+3|q|²hij/tau²)/2−9Tij_TT/tau⁴+hij/tau²`.

As this evaluation uses the same discrete sourced Euler RHS to recover h'', the small residual checks sign/bookkeeping/projection, **not** an independent test of an unsolved gravitational equation. The TT tracefree/real/symmetry/divergence checks supply separate structure diagnostics. The no-conversion negative control uses `h_wrong=−hphysical` in the same physical spatial-metric Einstein expression, yielding a nonzero residual.

### Actually executed local NumPy/SciPy five-run results (tau=1.08)

| N³ | time samples | retained nonzero modes | max |T_TT| | max |hphys| | max |C_TT| | max |C_TT(h_wrong)| |
|---|---:|---:|---:|---:|---:|---:|
| 16³ | 13 | 3374 | 0.00014936994835160636 | 0.000009241716825163678 | 2.320870275476783e−19 | 0.001976244680683711 |
| 24³ | 13 | 12166 | 0.00036788263821730543 | 0.000028390157108489254 | 1.018133602599669e−18 | 0.004867284985474264 |
| 32³ | 13 | 29790 | 0.0003373908845802668 | 0.000026409862423248603 | 8.368685518872487e−19 | 0.004463862700102176 |
| 24³ | 9 | 12166 | 0.00036788263821730543 | 0.000028390164924709087 | 8.656676720938949e−19 | 0.004867284985474264 |
| 24³ | 25 | 12166 | 0.00036788263821730543 | 0.000028390157600336533 | 1.0503208545953324e−18 | 0.004867284985474264 |

At N=32: source max Fourier trace and divergence ~2.7e−19, symmetry 2.7e−20; evolved h max trace ~1.19e−20 and transversality ~1.67e−20; Fourier real-space imaginary leakage ~3.41e−17. The small nt=9/13/25 variations at N24 do not establish spatial convergence: the N16/24/32 amplitude varies significantly because the original sampled compact packet is only modestly resolved and has high-mode effects. No full 3D 5-helicity metric or causal optical detector can be certified from this test.

## Provenance, audit, next gate

**Locally executed file:** `/mnt/data/cone_gate/k4_fullgrid_tt_physical_metric_v15_1344.py`; the separate full test above actually executed under local Python (NumPy/SciPy) across all five runs. **Additive GitHub reproducer:** `research-notes/k4_fullgrid_tt_physical_metric_v15_1344.py`, commit SHA **29295e1c4a244ea24f68ac3fe4abfe4b17395e6e**, includes the corresponding FFT Maxwell/TT/RK4 reproduction, structural assertions, and old-sign negative control. Exact committed-byte post-upload Audit replay remains pending. The v15.1344 filename **is noncanonical** because earlier Audit v15.1344 owns the ledger number, as stated above.

**AUDIT:** replay the exact committed source and check consistency with local results, especially TT double-projector normalization and Hermitian Nyquist cut, signed Fourier mode indexing, plus source factor 18, tensor strain sign, Euler test's source-constructed nature, the real-space conjugacy, RK4 time refinement and version precedence. Independently review that a comparison between `h_physical` and `−h_physical` is convention-dependent rather than a new physics observable.

**NEXT:** integrate the same dealiased Maxwell stress into the already-verified scalar and vector sectors at all q, combine with the homogeneous Bianchi-I u/beta, reconstruct the full g00/g0i/gij field on a common time grid, check all mixed Einstein tensor components against separately varied Maxwell+solid stress and reality, then only after stringent field and spatial/time convergence proceed to causal photon/free-mirror/emitter clock transfer. Identical-action GR+same K4 comparator still has zero physical difference. The arithmetic 1/4-Casimir geometry has supplied no independent interaction or Newton-G-free testable prediction.
