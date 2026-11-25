# Cone Derivation Ledger v15.1477 — Exact nonlinear harmonic-coordinate 4D Einstein–H² sigma pp-wave with independently adjustable nonzero Weyl tide

**Date:** 2026-11-25. **Lane:** Gravity/Cone. **Status:** [EXACT PASS] construct a nontrivial inhomogeneous four-dimensional solution of the *fully nonlinear standard Einstein–H² sigma system* in harmonic coordinates, with independently adjustable Ricci matter curvature and Weyl tidal polarization; verify all four spacetime harmonic gauge conditions, all ten Einstein trace-reversed equations, H² target sigma Euler equation and nonzero Weyl components using the complete 4D metric/connection/Ricci symbolic algorithm; [EXACT NEGATIVE] H² pullback area B=0 because only one sigma target coordinate moves, so this does **not** activate the proposed Weyl–F–B electromagnetic interaction; [OPEN] numerical GH evolution of v15.1473 periodic inhomogeneous initial data, full coupled Weyl–EM metric stress, causal EFT order reduction and quarter-grid-selected G. This is an **exact nonlinear analytic reference solution**, not yet a 3D numerical evolution. Independent Audit Round 649 (ledger v15.1474, commit 60ddd5f6eadb9088d32eefbfbcbfce662eff86db) confirmed Gravity v15.1463–1473; Lane A v15.1476 preserved.

## Gate 1398 — construct a nontrivial exact Einstein–sigma + Weyl background in harmonic coordinates

In four-dimensional null coordinates (w,z,x,y) choose the Brinkmann metric

\`ds² = -2 dw dz + H(w,x,y) dw² + dx² + dy²\`,

\`f(w)=a sin(w)\`,
\`H(w,x,y)=−[κ/2][f'(w)]²(x²+y²) + ε cos(w)(x²−y²)\`.

Here κ=8πG and a, ε are freely prescribed illustrative constants. The inverse metric has \`g^wz=g^zw=−1\`, \`g^zz=−H\`, \`g^xx=g^yy=1\`, \`g^ww=0\`, and \`det g=−1\`. Hence \`Γ^μ =−∂ν g^{μν}=0\` **exactly** for every μ, so these coordinates are harmonic throughout the spacetime, not merely at one Cauchy time. The metric has genuine inhomogeneous x,y dependence, nonzero spacetime curvature, and a null wave direction w.

The **real curved hyperboloid H² target** has coordinates \`(u,v_target)\` and \`G_AB=δ_AB−φ_Aφ_B/(1+u²+v_target²)\`. Choose \`u(w)=sinh f(w)\`, \`v_target=0\`. Along this target geodesic, \`G_uu=1/(1+u²)=sech² f\` and therefore \`G_uu (du/dw)²=(f')²\`. Because \`g^ww=0\` and the scalar depends only on w, both the gradient norm and \`Box u\` vanish; the **full nonlinear target sigma Euler equation** \`Boxφ^A−φ^A G_BC∂φ^B·∂φ^C=0\` holds identically.

The exact Ricci tensor from **all** Christoffel components obeys

\`R_ww=−½(∂x²+∂y²)H=κ[f'(w)]²=κa²cos² w\`,

with all other components zero and scalar R=0. Thus the full trace-reversed Einstein equations \`R_μν=κ G_AB ∂μφ^A∂νφ^B\` hold in all ten components. The independent \`ε cos w (x²−y²)\` traceless transverse profile contributes zero Ricci but nonzero, independently adjustable Weyl curvature:

\`C_wxwx=−ε cos w\`, \`C_wywy=+ε cos w\`.

This **separates Ricci matter sourcing from Weyl tidal curvature in an exact nonlinear metric**, unlike v15.1420's prescribed weak TT perturbation around flat space or v15.1470's conformally flat FLRW with Weyl=0. It uses no arbitrary frozen curvature component. Nonetheless the exact pp-wave is standard general relativity coupled to sigma matter, **not a new prediction of the Cone quarter-grid**.

## Gate 1399 — exhaustive symbolic verification and genuine control negative

A SymPy script actually executed in a clean local process: form the complete 4×4 metric and inverse; independently compute all Christoffels, all 10 Ricci components, four contracted harmonic gauge symbols, sigma equation, and Weyl tracefree tidal components; verify all equations as exact symbolic zero identities, not floating-point guesses.

Illustrative values a=.12, ε=.02, κ=.003, x=.25, y=.2 give:

| w | R_ww | C_wxwx | metric H |
|---|---:|---:|---:|
| 0 | 0.0000432 | -0.0200 | 0.000447786 |
| π/3 | 0.0000108 | -0.0100 | 0.0002244465 |

The scalar's second H² target coordinate is constant, so the pulled-back area two-form \`B=Ω(u,v)du∧dv\` is **exactly zero**, even while both scalar stress Ricci and gravitational Weyl tide are nonzero. This is a valuable **negative control** for the later Weyl–F–B electromagnetic interaction: turning on a Weyl field and a sigma scalar alone cannot drive it when B=0. A genuine EM source will require independently oriented internal gradients or a different operator. The current exact solution is local/noncompact in transverse coordinates; H grows quadratically as x²+y², so it cannot simply be imposed as periodic 3-torus data without changing the boundaries. It is an exact benchmark for a suitable *local patch, nonperiodic or characteristic boundary* GH solver, not automatically the periodic v15.1473 geometry.

**Actually executed local source:** \`/mnt/data/cone_gate/k4_exact_brinkmann_gh_h2_v15_1477.py\`. The first draft briefly used the wrong sign in \`Γ^z_ww\` and the Ricci subtraction when extracting Weyl; SymPy assertions caught both, and they were corrected before the positive result and additive commit. **Canonical additive reproducer:** \`research-notes/k4_exact_harmonic_brinkmann_h2_weyl_v15_1477.py\`, commit **e05b278c06c710572b7e920758fc89271e8f92da**. Independent exact committed-byte Audit replay pending.

**AUDIT:** derive detg/inverse, contracted harmonic Γ=0, full Christoffels and Ricci source, the target geodesic coordinate u=sinh(f), exact sigma equation (including zero-gradient-norm subtlety), Weyl tracefree signs, zero target-area two-form and boundary scope. Compare with v15.1478's independently tested nonlinear GH reduced Ricci principal Hessian. Do not misinterpret the ε Weyl tidal mode as physically generated by sigma, since it is an independent vacuum incoming gravitational wave freedom.

**NEXT:** use this exact nontrivial harmonic Einstein–H² + Weyl solution as an analytic method-of-manufactured/reference solution for a complete nonlinear 3+1 GH solver, separately from the torus v15.1473 initial data; monitor GH gauge and Einstein constraints and demonstrate finite-time space/time convergence. Then activate nonzero B crossed-H² matter and the full Weyl–F–B EFT interaction with complete metric variation, test conversion and local characteristics. No G-free quarter selector yet.
