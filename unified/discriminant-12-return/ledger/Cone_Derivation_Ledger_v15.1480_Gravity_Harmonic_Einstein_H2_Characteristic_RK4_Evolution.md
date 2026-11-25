# Cone Derivation Ledger v15.1480 — Fourth-order numerical time evolution of the exact nonlinear harmonic Einstein–H² gravitational-wave sector

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Status:** [NUMERICAL PASS] numerical RK4 time integration of a dynamically changing curved H² sigma null profile and an independent vacuum Weyl tidal-wave profile inside an **exact nonlinear 4D harmonic Einstein–H² pp-wave ansatz**, with fourth-order temporal convergence verified against the exact 4D metric and sigma solution at t=4. [NEGATIVE CONTROL] the same solution always has B=0 due to its rank-one sigma target motion, so no Weyl–F–B or EM conversion; and the numerical evolution is a **restricted null-wave characteristic subsystem**, not the full unconstrained nonlinear 3D generalized-harmonic Einstein PDE. [OPEN] unrestricted fully coupled spatially inhomogeneous 3+1 GH metric+sigma evolution, full ADM+GH constraint monitoring, long-time gauge and EFT stability, physical quarter-grid coupling. **Audit Round 649** independently verified v15.1463–1473, new committed v15.1477–1480 await replay; no collisions with Lane A v15.1476.

## Gate 1405 — nontrivial curved spacetime evolved from two propagating profiles

Transform the exact nonlinear Brinkmann spacetime v15.1477 to Cartesian 3+1 timelike coordinates t,z,x,y with null w=t−z and Kerr–Schild metric

\`ds²=−dt²+dz²+dx²+dy²+H(w,x,y)(dt−dz)²\`,
\`H(w,x,y)=−κ/2 f'(w)²(x²+y²)+e(w)(x²−y²)\`.

For **arbitrary smooth** two right-moving functions f(w) and e(w), with curved-H² sigma target field \`φ=(sinh(f),0)\`, the full nonlinear Einstein and target sigma equations are satisfied exactly because \`R_ww=−(∂x²+∂y²)H/2=κ f'(w)²\` and the independent traceless e(w) term has zero Ricci but nonzero Weyl curvature. The four harmonic coordinate constraints vanish for any f/e depending only on w. The full metric is **nonlinear in the sigma gradient** f'(w)², not just a linear radiation formula. But its profile functions have been restricted to a **specific exact invariant null-wave solution family**; it does not allow arbitrary perturbations off that ansatz, so its numerics must not be presented as a freely evolving 3D Einstein solver.

Numerically integrate the two independent hyperbolic transport equations on a spatial periodic z grid:

\`∂t f+∂z f=0\`, \`∂t e+∂z e=0\`.

At initial t=0 choose \`f(0,z)=.12 sin(z)\`, \`e(0,z)=.02 cos(z)\`; exact right-moving solutions are **f(t,z)=.12 sin(z−t)=−.12 sin(t−z)** and **e(t,z)=.02 cos(z−t)=.02 cos(t−z)**. Use N=32 Fourier spectral derivative \`∂z\` and fourth-order explicit Runge–Kutta to t=4, then reconstruct metric H(t,z,x,y) at physical (x=.4,y=−.3) and physical H² target coordinate \`u=sinh f\`. Independent exact test compares each profile and nonlinear metric H, and computes harmonic gauge obstruction \`∂tH+∂zH\` using the evolution RHS. Ricci Einstein source cancellation follows exactly from the quadratic transverse ansatz and does not require numerical curvature reconstruction.

## Gate 1406 — measured RK4 temporal order and prior sign-test correction

**Actually executed local code:** \`/mnt/data/cone_next/k4_gh_null_wave_evolution_v15_1480.py\`. The **first** test run compared the correctly right-moving numeric \`f=.12sin(z−t)\` to an incorrectly sign-reversed reference \`+.12sin(t−z)\` and **FAILED** its fourth-order convergence assertion (profile mismatch ≈.239 at all timesteps). Diagnosed that the exact reference had the wrong sign for the odd sine, corrected **only the reference** to \`−.12sin(t−z)\`, with numerical transport RHS unchanged, then reran. The corrected test PASSED with the expected fourth-order timestep reduction. This is a numerical test-code sign error, not an intrinsic failure of Einstein/sigma equations, but is recorded openly.

| N³ spatial z modes | Δt | end time | max two-profile deviation | max metric H deviation | max sigma target u deviation | max gauge error |
|---|---:|---:|---:|---:|---:|---:|
| N_z=32 | .16 | 4 | 2.616001654e−6 | 3.053719076e−8 | 2.616101845e−6 | 0 |
| N_z=32 | .08 | 4 | 1.638262964e−7 | 1.912382299e−9 | 1.638325725e−7 | 0 |
| N_z=32 | .04 | 4 | 1.023177886e−8 | 1.194379252e−10 | 1.023217084e−8 | 0 |

The respective profile error-reduction factors upon halving Δt are **15.96814255 and 16.01151653**, in agreement with the fourth-order RK4 expectation 2⁴=16. The gauge residual \`∂tH+∂zH\` is exactly zero in the implemented restricted ansatz by construction using the same derivative on each side; it is therefore not an independent numerical test of GH constraint propagation for freely evolved metric components. Similarly, the Ricci source identity \`R_ww=κ f'(w)²\` is an *analytical property of this restricted ansatz*, not a separately evaluated finite-grid nonlinear Einstein constraint. The nonlinear metric/time-dependent scalar solution is nonetheless nontrivial and the comparison against the exact profile/time evolution is a genuine independent RK4 convergence test.

**Additive standalone committed script:** \`research-notes/k4_gh_characteristic_ppwave_rk4_v15_1480.py\`, SHA **47bf577491c555c24973ce7e7f030decf583664e**, independently authored equivalent of the locally tested algorithm. Exact committed-byte external Audit replay pending.

## Link to v15.1479, audit and next milestone

Gate v15.1479 independently verified the **entire nonlinear 3+1 GH time-acceleration RHS** for both metric and curved sigma fields against this exact 4D curved spacetime, but only pointwise with analytically supplied spatial jets. This gate verifies an **actual time-stepper and fourth-order temporal convergence** in the exact invariant characteristic sector, but not the general 3+1 field system. These two prerequisites are complementary but **not the final nonlinear GH Einstein–H² evolution milestone**. The v15.1473 periodic inhomogeneous nonlinear Einstein initial slice continues to satisfy both ADM and initial GH constraints and remains the intended full PDE initial dataset.

**AUDIT:** rerun exact v15.1480 script, verify sign f(t,z)=sin(z−t), both numerical error ratios, physically real reconstructed g with Lorentz signature on tested compact patch, and subtle fact that exact harmonic/Einstein residuals are imposed by ansatz. Confirm the separate nonzero Ricci sourced by H² gradient and nonzero independently adjustable Weyl, zero B and no EM conversion. Do not interpret it as full unrestricted 3D GH evolution or as first-principles derivation of κ.

**NEXT:** develop unrestricted spatial-FFT/finite-difference generalized-harmonic RHS from v15.1479 on grids with **evolved** g_μν, g_μν,t, φ^A, φ^A_t, and compute all spatial derivatives numerically rather than from the exact plane wave. Use the v15.1473 constrained initial data and v15.1463 nonlinear curvature oversampling for short time and longer T=.04 convergence; monitor independently recomputed all 4 GH and 4 ADM constraints at every time. The beyond-GR Weyl–F–H² interaction needs a separate full metric variation and EFT order reduction; the internal q2=1/16 variance does not select κ or EM coupling.