# Cone Derivation Ledger v15.1479 — Independently reconstructed nonlinear 3+1 generalized-harmonic metric and H² sigma time accelerations on an exact curved Einstein–sigma + Weyl spacetime

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Classification:** [NUMERICAL PASS ON EXACT ANALYTIC SPACETIME] the full nonlinear GH reduced Einstein metric wave equations and full curved-H² sigma equations are **solved explicitly for every second coordinate-time derivative** g_μν,tt and φ^A_tt, using only the metric, its first derivatives and the mixed/spatial second derivatives. They reproduce the independently differentiated exact 4D Einstein–H² nonzero-Weyl Brinkmann plane wave (v15.1477) at four separate Cartesian 3+1 spacetime points to ~10^−17; the Ricci/Einst and contracted GH gauge residuals also vanish. [SCOPE] This is an **equation-level method-of-manufactured/reference-solution RHS test**, not an unconstrained 3D finite-time numerical GH evolution, not a long-time stability proof, not Weyl–F–B EM coupling (the tested target area B is zero). κ=8πG=.003 is chosen, not derived. Audit Round 649 (v15.1474) independently verified the program through v15.1473; the new 1477–1480 committed-byte tests await independent replay. Preserve all Lane A, Sandbox and Audit entries.

## Gate 1403 — reconstruct the GH wave Cauchy accelerations from 4D jets

In Cartesian (t,z,x,y) coordinates introduce w=t−z and choose the exact physical nonlinear metric
\`g_μν=η_μν+H l_μ l_ν\`, where \`l_μ=(1,−1,0,0)\`,
\`H=−κ/2 [f'(w)]² (x²+y²)+ε cos w(x²−y²)\`,
\`f=.12 sin w\`, \`ε=.02\`, and the H² target field \`φ=(sinh f,0)\`.
The null Kerr–Schild metric satisfies harmonic coordinates exactly and the trace-reversed Einstein source is \`R_μν=κ G_AB∂μφ^A ∂νφ^B\`; its independent ε term gives nonzero physical Weyl tidal curvature while contributing no Ricci. This is just the exact v15.1477 solution transformed to a timelike t slicing, not an invented external source.

Reconstruct the full 4D Christoffels, \`dΓ\` and Ricci from the *exact metric jets* through second derivatives, and independently compute the harmonic gauge vector \`C^μ=g^ab Γ^μ_ab\`. To obtain the GH reduced nonlinear lower-order term Q, **recompute** the same Christoffel/Ricci/gauge-covariant-derivative functional with its second metric derivatives set to ZERO, keeping g and ∂g fixed. The exact identity from v15.1478 is
\`R^GH_μν=R_μν−∇_(μ C_ν)=−½g^ab∂a∂b g_μν+Q_μν(g,∂g)\`.
Solve the 10 nonlinear GH wave equations for the metric time Hessian:
\`g^tt g_μν,tt=2[Q_μν−κ G_AB∂μφ^A∂νφ^B]−2g^ti g_μν,ti−g^ij g_μν,ij\`.
Independently solve the curved-target sigma equation:
\`g^tt φ^A_tt=φ^A G_BC(g^μν∂μφ^B∂νφ^C)+C^μ∂μφ^A−2g^ti φ^A_ti−g^ij φ^A_ij\`.
The appearance of \`C^\mu∂_\mu\phi^A\` matters when testing away from exact harmonic gauge. No faking of the metric acceleration by a prescribed exterior field is allowed in this RHS calculation.

## Gate 1404 — actual local execution and numerical checks

**Actually executed** \`/mnt/data/cone_next/k4_gh_time_rhs_v15_1479.py\`, which forms analytic jets using SymPy, then uses numerical tensor contractions to reconstruct the independent GH Q and both metric/sigma time accelerations. Every listed point has a nonzero genuine spacetime metric second time derivative, ruling out a trivial zero-test:

| (t,z,x,y) | max |g_tt RHS−exact| | max |sigma_tt RHS−exact| | Ricci−source | max |Γμ| | max |exact g_tt| |
|---|---:|---:|---:|---:|---:|
| (0,.15,.2,-.4) | 3.47e−18 | 0 | 6.94e−18 | 0 | .0023813 |
| (.4,−.2,−.7,.3) | 2.60e−18 | 1.39e−17 | 6.94e−18 | 0 | .0065936 |
| (1.1,.4,.5,.6) | 3.69e−18 | 0 | 1.73e−18 | 1.73e−18 | .0016871 |
| (2.2,.1,−.2,.8) | 4.34e−18 | 0 | 3.47e−18 | 1.73e−18 | .0060726 |

**Additive canonical equivalent reproducer** \`research-notes/k4_gh_metric_sigma_acceleration_v15_1479.py\`, commit **b4dcee4faaf5d43d35db0d61e1e0aa2f2542336f**. The independently authored committed version uses the same mathematical equations, jets, and sample points as the locally tested source, but **the exact committed bytes are not yet independently replayed by Audit**. The locally tested script is directly available for re-execution in the conversation. Note that \`G_AB\` is the H² target, not a spacetime metric.

## Status and required next gate

This certifies an important independent **nonlinear PDE right-hand-side implementation** against a nontrivial exact Einstein–H² reference; earlier gates only established the continuum wave symbol, initial ADM+GH constraints or a special homogeneous time integrator. The test still receives spatial Hessians/first derivatives from an **exact analytic spacetime** rather than a discretized evolved 3D field. An actual free 3D GH method-of-lines must construct those derivatives from its evolving grid, integrate the metric and two scalar fields, and monitor the four GH plus four ADM constraints at each step. The plane wave used here has B=0, so none of this tests Maxwell interaction, EFT-induced higher derivatives or a quarter-grid-selected coupling.

**AUDIT:** replay the committed v15.1479 source and independently compare g_tt to exact metric Hessians and phi_tt to exact curved-target sigma Hessians at all four points. Re-derive the signs in both inversion formulas, especially \`C·∂φ\`, and verify the test computes Q by redoing the curvature with zero metric Hessians. Cross-check that actual Weyl remains nonzero and Ricci matches nonlinear H². Confirm this is not sold as an unrestricted nonlinear 3D evolution.

**NEXT:** combine the GH RHS with periodic Fourier or finite-difference spatial differentiation, supply initial data from v15.1473 and perform full freely evolved 3D nonlinear Einstein–H² time stepping, including a strongly hyperbolic gauge source and constraint damping/monitoring. v15.1480 separately verifies a restricted exact characteristic time evolution for the plane-wave sector, with fourth-order error convergence, but does not replace the unrestricted solver.