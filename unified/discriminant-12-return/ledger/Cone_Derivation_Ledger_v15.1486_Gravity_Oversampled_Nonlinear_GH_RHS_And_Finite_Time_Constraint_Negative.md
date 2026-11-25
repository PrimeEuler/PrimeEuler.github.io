# Cone Derivation Ledger v15.1486 — 2× nonlinear generalized-harmonic RHS oversampling: strong acceleration improvement, but no automatic Einstein-constraint gain

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Parent:** Audit Round 650 (v15.1484, commit e7c8422122f0) and additive corrected unrestricted 3D GH–H² reproducer v15.1485. **Status:** [NUMERICAL POSITIVE] true two-times periodic Fourier upsampling of the **unchanged** constrained initial metric, coordinate velocities and both H² sigma fields, evaluation of the full nonlinear generalized-harmonic Einstein–H² RHS on the 2× grid, followed by spectral projection of the computed RHS back onto the original grid, gives nonlinear metric and sigma accelerations **much closer** to an independent 3×-oversampled RHS than the native RHS. [NUMERICAL NEGATIVE] this does **NOT** by itself improve evolved 4D GH-gauge and 3+1 Einstein Hamiltonian/momentum constraints over short time; at N16 it slightly worsens GH/M. [RESOURCE LIMIT] N24 padded T=.04 was attempted but exceeded the 120-second execution limit after the native control completed; no padded N24 result is claimed. κ=.003 remains prescribed. Sandbox's newest v15.1485 area-covariance census, landed while this gate was underway, independently closed variance→area as a parameter-free selector; the main GH gravity lane does not use V=1/16 as an assumed coupling.

## Gate 1412 — fair 1× versus 2× versus 3× full nonlinear RHS comparison

Let U denote a full 3D periodic state `U=(gμν,∂tgμν,φA,∂tφA)` from the **same** nonlinear v15.1453/1473 constrained Einstein–H² ADM initial-slice solver with harmonic gauge initialization. Define FFT `I_m` as periodic spectral interpolation to grid size mN on each dimension, `P_N` as Fourier spectral projection/decimation to the nominal N-grid (SciPy `scipy.signal.resample` applied to each of the three axes), and `F_m` as the full nonlinear unrestricted GH–H² RHS evaluated at that grid resolution. Compare `F_N(U)` with `P_N F_{2N}(I_2 U)` and `P_N F_{3N}(I_3 U)`. The 3× RHS is an **independent high-resolution numerical reference**, not an exact Einstein solution or evidence of physical coupling. No source fields are low-pass filtered; the interpolated field represents the **same bandlimited nominal initial data**.

Actual local executed source `/mnt/data/cone_gh/padded_rhs_gate_v15_1486.py` imports the previously executed unrestricted solver `/mnt/data/cone_gh/gh3d.py` and records N12 and N16. At N12 the initial momentum constraint is already unacceptable, H≈3.10e−7, M≈2.74e−5 (as independently known from v15.1453); its RHS comparison is **only a numerical diagnostic**, not an acceptable time-evolution initial condition. N16 has H≈4.22e−6 and M≈2.08e−9, so also only a coarse method test. The canonical GitHub reproducible `research-notes/k4_gh_rhs_padding_and_evolution_v15_1486.py`, committed initially SHA 721e16b48800622e4414a4280b5dfeecc9ac9c9c and refined in additive SHA **a2284cd0ffe6b4a19b228aab9400fcbc95e18459**, imports the **repaired v15.1485** unrestricted solver; the committed script intentionally restricts its self-run to N16 because that solver's own preexisting coarse-grid assertion correctly prevents execution with N12's much larger initial constraint error. Exact committed-byte Audit replay remains pending.

| Resolution | RHS component | Native vs 3× max | 2× padded vs 3× max | Error ratio |
|---:|---|---:|---:|---:|
| 12³ | metric acceleration | 2.38449210e−5 | 2.21724683e−12 | 1.0754e7 |
| 12³ | sigma acceleration | 6.60139183e−4 | 2.03733957e−9 | 3.2402e5 |
| 16³ | metric acceleration | 2.93060276e−7 | 3.21558101e−14 | 9.1138e6 |
| 16³ | sigma acceleration | 2.69411686e−4 | 1.66894276e−13 | 1.6143e9 |

The 2× calculations have substantially better *nonlinear acceleration evaluation* at the original nodes after spectral projection. This does **not** show a comparable improvement in the independent Einstein constraint evolution.

## Gate 1413 — actual freely evolved short-time test and negative

Independently executed `/mnt/data/cone_gh/padded_evolution_v15_1486.py`: evolve actual unrestricted 3D GH metric+H² data with RK4 dt=.004, using native or the above 2× padded **entire** nonlinear RHS, including exact coordinate first-derivative kinematics, with no filtering of the initial physical state; reconstruct full evolved ADM H/M and all four GH constraints at nominal N using the existing independent unpadded constraint monitor (monitor mismatch can itself contribute to the floor).

| grid | T | scheme | max GH | max ADM Hamiltonian | max ADM momentum |
|---:|---:|---|---:|---:|---:|
| 12³ | .008 | native | 4.41999898e−7 | 2.43167096e−6 | 2.78758762e−5 |
| 12³ | .008 | 2× padded | 4.39124191e−7 | 2.43460567e−6 | 2.78776566e−5 |
| 16³ | .008 | native | 8.54880413e−9 | 4.24396484e−6 | 3.51888017e−7 |
| 16³ | .008 | 2× padded | 8.78282248e−9 | 4.24403976e−6 | 3.53470902e−7 |
| 16³ | .040 | native | 6.94075710e−8 | 4.17598843e−6 | 1.72808262e−6 |
| 16³ | .040 | 2× padded | 7.99732816e−8 | 4.17697544e−6 | 1.73554998e−6 |
| 24³ | .040 | native | 4.45045416e−10 | 1.09175316e−8 | 1.10733727e−8 |
| 24³ | .040 | 2× padded | **NOT COMPLETED (timeout)** | — | — |

All finished states retain negative inverse g^tt: at T=.04 N16 ~−.99873822, N24 native ~−.99873823, so timelike coordinate evolution persists for the tested range. The native N24 T=.04 result is substantially better than N16, though Hamiltonian remains at its ≈1e−8 initial spectral aliasing floor. **No claim** that 2× padding by itself improves GH/ADM residuals: it clearly does not on this coarse sample, especially at longer T. This is a real negative result, not failed precision due to syntax: all local runs execute cleanly. The N24 padded case was interrupted by the 120-second external execution time limit and **has not been measured**; a resource ceiling is not evidence of numerical instability or failure. No 32³ T=.04 result yet.

## Why improved RHS accuracy need not improve constraints

The ADM initial-slice solver and the GH constraints are evaluated on the *nominal grid* with their original nonlinear products and unresolved high modes; merely improving the RHS through padding while monitoring the constraints in an aliased discretization need not reduce those monitor errors. The GH subsidiary constraints also depend on consistent spatial derivatives and appropriate time-derivative compatibility, not just local acceleration errors. Unlike the v15.1483 naive cutoff, the new approach preserves initial fields and is a more principled pseudospectral RHS method, but it does not commute with the separate nonlinear constraint operator or guarantee constraint-preserving projection.

**Audit:** independent exact-byte replay of corrected v15.1485 standalone GH solver and canonical v15.1486 padding script; verify N16 RHS gains and N16 T=.008 run, and separately compare N16 T=.04. Verify Fourier interpolator projection consistency, field-index shapes, harmonic/ADM residual definitions, and that initial constrained state remains **unchanged**. Treat N12 as aliased diagnostic only and N24 T=.04 padded as explicitly unmeasured. Compare against independent 3× RHS; test for roundoff ceilings and metric invertibility.

**NEXT MAIN:** derive/implement padded ***constraint*** monitors on the same resolved physical data, pursue an elliptic initial-data solver whose products are correctly dealiased as well, and optimize/prefactor nonlinear GH RHS to make N24–32 2× T=.04 feasible; test true spatial/timestep constraint convergence and constraint-subsidiary energy. Only then return to Maxwell–Weyl–H² higher-derivative metric variation/order reduction and causal response. The 1/16 sector variance is a valid arithmetic rung label but Sandbox v15.1485 has closed the variance→area selector without a new action-selected spacetime pullback operator.