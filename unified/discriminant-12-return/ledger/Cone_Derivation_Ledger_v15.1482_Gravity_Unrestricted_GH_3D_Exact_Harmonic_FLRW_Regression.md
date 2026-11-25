# Cone Derivation Ledger v15.1482 — Exact nonlinear Einstein–H² FLRW benchmark passed by the same unrestricted 3D generalized-harmonic solver

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone, parent v15.1481 and exact harmonic-time FLRW reference v15.1470. **Status:** [ACTUAL NUMERICAL PASS] full unrestricted 3D GH Einstein–H² code (all 10 metric components + two curved-target scalars) evolves the *exact* homogeneous nonlinear harmonic-time Einstein–sigma solution using the same grid-based 3D Fourier and full nonlinear GH right-hand-side as on general inhomogeneous Cauchy data. RK4 time-step halving yields characteristic fourth-order ratios 15.96485 and 16.00000 against an independent closed-form 4D metric-and-scalar solution, with fully recomputed 4D GH and 3+1 Einstein Hamiltonian/momentum constraints near roundoff. [SCOPE LIMIT] homogeneous data are a proper invariant *subsector* of the unrestricted code; this certifies its time integration and curved Einstein–sigma source more strongly than an analytical RHS jet or restricted characteristic solver, but does NOT establish longer-time inhomogeneous convergence or a physical Maxwell/Weyl coupling. No quarter-sector G derivation. Independent Audit of committed-byte v15.1481–1482 pending.

## Gate 1409 — an exact nonlinear homogeneous Einstein–sigma solution in harmonic time, without altering the unrestricted solver

Use 3+1 flat spatial sections in harmonic coordinate time s,
\`ds²=−α(s)²ds²+a(s)²(dx²+dy²+dz²)\`, α=a³(s).
Choose the real H² sigma target along a genuine geodesic \`φ(s)=(sinh F(s),0)\`, with \`F(s)=F0+v s\`, F0=.2, v=.12. Then the exact conserved target kinetic invariant is v² and massless sigma stress gives

\`B=sqrt(3κv²/2)=.008049844718999243\`, with κ=.003,
\`a³(s)=exp(Bs)\`, \`α(s)=exp(Bs)\`,
\`g_ss(s)=−exp(2Bs)\`, \`g_ii(s)=exp(2Bs/3)\`,
\`φ^1(s)=sinh(.2+.12s)\`, \`φ^2(s)=0\`.

Initialize the FULL 4D metric and its time derivatives from these exact expressions at s=0 (all other gμν zero), plus the real target fields and their coordinate-time derivatives. Then evolve with **exactly the same unrestricted 3D nonlinear GH solver** as v15.1481, on N=6³ Fourier grid. The nonlinear metric Einstein source κGAB φ_,μ φ_,ν, nontrivial spatial metric/lapse and curved target connection all remain active; there are simply no spatial gradients in this exact sub-sector. The solver does not know the analytical a³ law and does not impose harmonic gauge/Friedmann during time integration. It computes the complete 4D GH vector and independent physical 3D Ricci/Kij Einstein constraints after RK4. The 4D metric remains Lorentzian.

## Gate 1410 — measured fourth-order time convergence and independent constraints

**Actually executed local reproducible:** \`/mnt/data/cone_gh/flrw_test.py\`, importing the actual unrestricted nonlinear GH implementation \`/mnt/data/cone_gh/gh3d.py\`. Both are stored as downloadable artifacts in this conversation; local SHA-256: gh3d.py **087310cf64d4aea64bcc3443a71af2b0d3c2092c0136cb42ac9c91d581efbb60**, flrw_test.py **d607d7e57728a31f4ea6205db570f90f43e944300c1b3e5c1dbfcfa4d13eebf8**. **Equivalent standalone reproducible committed:** \`research-notes/k4_gh_3d_exact_flrw_regression_v15_1482.py\` SHA commit **449715313eeeaee3b1011951512d0e638059bc18**; imports committed same-directory v15.1481 full solver at commit **134a3faf7f267cdcbce017c39718f7f112edb1bd**. Independent committed-byte exact replay pending.

| dt | final harmonic time | max absolute error over g_ss,g_xx,phi¹ | max GH vector | max ADM Hamiltonian | max ADM momentum |
|---:|---:|---:|---:|---:|---:|
| 0.1 | .4 | 1.0336953515e−11 | 9.75348274e−15 | 2.83234265e−16 | 0 |
| 0.05 | .4 | 6.4748206796e−13 | 6.11490025e−16 | 1.83636743e−17 | 0 |
| 0.025 | .4 | 4.0467629248e−14 | 3.55618313e−17 | 1.21295118e−18 | 0 |

Observed numerical fourth-order ratios are **15.964849108367627 and 16.0**, as predicted by RK4. The tight agreement between all three independently monitored evolved field components and the closed-form solution is nontrivial: the lapse g_ss evolves exponentially rather than remaining geodesic-unit-lapse, the sigma target is curved, and the Einstein source dynamically balances a nonzero scalar energy density. The ADM momentum constraint is zero because the solution is homogeneous, not because the code lacks a momentum residual evaluator; the inhomogeneous v15.1481 case independently evaluates a nonzero residual.

**Interpretation and restrictions:** This is a substantial real numerical check that the new unrestricted 3D generalized-harmonic Einstein–H² implementation has correct nonlinear time stepping, source normalization and harmonic lapse **at least in a homogeneous limit**. The spatially varying v15.1481 test is still short-time and limited by spectral aliasing; this homogeneous test does not prove its long-time stability, gauge-constraint damping or spectral convergence. Explicitly do not call the homogeneous exact reference an independent new gravitational law. The H² geodesic F(s)=F0+vs is standard kinetic sigma dynamics; κ is arbitrary.

**AUDIT:** independently replay the two committed scripts on a clean checkout, confirm SymPy or hand derivation of exact harmonic metric and curved-H² geodesic, check nonlinear Einstein source and target scalar Hessian signs, observe dt ratios with **unrestricted** grid-based PDE solver, compare 4D GH and physical 3D H/M constraints against reported values. Verify numerical N=6 complex Fourier handling, axis ordering, symmetric metric, positivity of spatial metric and Lorentzian g^tt, and no hidden resetting of constraints.

**NEXT MAIN:** increase spatial resolution / apply full 2× oversampling and FFT mode projection on nonlinear GH source evaluation, then run t=.04 and longer freely spatially inhomogeneous v15.1473 torus data and independently monitor both constraint subsystems. Use exact nontrivial inhomogeneous Weyl plane wave v15.1477/79 as a second, nonperiodic reference on a local Cartesian patch (appropriate boundaries required). Only once stable Einstein–H² propagation is verified should Weyl–F–B electromagnetic EFT with complete metric variation/order reduction be added. V=1/16 variance remains a separate Sandbox response hypothesis and must not be inserted as arbitrary κ or ζ.