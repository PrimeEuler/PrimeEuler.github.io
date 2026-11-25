# Cone Derivation Ledger v15.1478 — Full nonlinear 4D generalized-harmonic Ricci wave-principal cancellation from independent metric jets

**Date:** 2026-11-25. **Lane:** Gravity/Cone. **Status:** [EXACT FORMULA / NUMERICAL PASS] full 4D reduced Ricci wave-principal structure verified without using a linearized metric or assuming zero Christoffels: construct arbitrary Lorentzian metric and its independently varied first/second derivative jets; calculate all connections, their derivatives, full Ricci, harmonic constraint covariant derivatives, and verify cancellation of *every* non-wave second-derivative metric term to ~3.4×10^-17. [STRICT SCOPE] this is the correct continuum *nonlinear generalized-harmonic PDE principal identity*, not yet a discretized evolving nonlinear 3+1 Einstein–H² numerical system or proof of finite-time stability. [OPEN] subsidiary constraint propagation, gauge damping, complete Weyl–F–B EFT higher derivatives and quarter-grid physical coupling. Parent v15.1477 exact curved-H² + nonzero Weyl harmonic pp-wave. Audit Round 649 confirmed v15.1463–1473.

## Gate 1400 — nonlinear GH reduced Ricci principal operator

Use a local symmetric Lorentzian metric gμν, its inverse, all first derivatives \`dg[a,m,n]=∂a g_mn\`, and symmetric second derivatives \`ddg[a,b,m,n]=∂a∂b g_mn\`. The full Levi-Civita connection is

\`Γ^r_mn=½ g^rl(∂m g_ln+∂n g_lm−∂l g_mn)\`.

Define harmonic constraint \`C^r=g^mn Γ^r_mn\`, \`C_n=g_nr C^r\`, and **reduced Ricci**:

\`R^GH_mn=R_mn−∇_(m C_n)\`,

where parentheses denote the symmetric half-sum. By full nonlinear cancellation,

\`R^GH_mn=−½ g^ab∂a∂b g_mn+Q_mn(g,∂g)\`,

with Q depending only on metric and its FIRST derivatives. This is the geometrical reason the gauge-reduced Einstein equations can have a wave-like principal part, unlike raw fixed-lapse ADM's longitudinal Jordan block v15.1464. The exact form of Q is not presumed: the test **evaluates it independently** as \`R^GH+½g^ab ddg_ab\` and checks it is invariant under arbitrary changes of metric Hessians with the same metric and first derivatives.

## Gate 1401 — actual independent nonlinear metric-jet test

For each random seed 1,7,55 choose a symmetric matrix perturbation of \`diag(-1,+1,+1,+1)\` (amplitude .04), all symmetric first metric jets (amplitude .025), and FOUR distinct symmetric second-derivative metric jets (amplitude .015). Compute inverse and its first derivative analytically \`∂a g^ij=−g^ip(∂a g_pq)g^qj\`; compute all 64 Christoffels, all derivatives, all Ricci components, C^μ, C_μ, \`∇_μ C_ν\`, and the reduced Ricci. For each group hold g and ∂g fixed while changing all second derivatives. The computed residual difference \`Q(ddg_1)−Q(ddg_2)\` is:

| metric first-jet seed | max nonlinear Hessian-cancellation discrepancy | max full Ricci Hessian response |
|---:|---:|---:|
| 1 | 2.6020852139652106e−17 | 0.042918675771757425 |
| 7 | 2.7755575615628914e−17 | 0.04345674307219999 |
| 55 | 3.382710778154774e−17 | 0.043535348457632295 |

Both are decisive in scope: the ordinary nonlinear Ricci tensor responds substantially to a changed metric Hessian, while \`R^GH+½g^ab ddg\` does not, to roundoff. This independently verifies the full nonlinear connection/covariant derivative indexing and wave-principal cancellation for nonzero random offdiagonal metric and derivatives. It is not merely a reference to a standard formula or a check of flat TT amplitudes. It still does not prove strong hyperbolicity of every possible full nonlinear generalized-harmonic discretization (which also requires a timelike slicing, gauge-source choices, correct constraint subsystem, boundary treatment and consistent matter equations).

**Actually executed local Python reproducer:** \`/mnt/data/cone_gate/k4_gh_reduced_ricci_principal_v15_1478.py\`, prints table and PASS; **additively committed independently authored equivalent source** \`research-notes/k4_gh_full_ricci_hessian_v15_1478.py\`, commit **bc3076825021433af609f62e4872d4711d899856**. Exact committed-byte external Audit replay pending. The local script's original version printed Q-norms without actually comparing distinct Hessians; this was identified and corrected before the final test and ledger write, preserving an honest distinction between calculating Q and demonstrating Hessian independence.

## Gate 1402 — relation to the physical Einstein–H² system

The massless curved-target H² sigma trace-reversed Einstein source for the **two-derivative** sector is \`R_mn=κ G_AB(φ)∂mφ^A∂nφ^B\`. The proposed GH hyperbolic reduction is \`R^GH_mn=κ G_AB∂mφ^A∂nφ^B\` with harmonic constraints C=0, alongside the hyperbolic curved-target sigma equations \`□_gφ^A−φ^A G_BC(φ)∂φ^B·∂φ^C=0\`. Because the source contains at most first scalar derivatives, it does not disturb the wave principal part of the metric PDE in this standard two-derivative action. The contracted Bianchi identity and *on-shell* sigma Noether conservation (v15.1451) are what propagate the GH gauge constraint if both it and its compatible normal derivative are initially zero; independent monitoring of this subsidiary system is still required in numerical time evolution.

**AUDIT:** rederive full R_mn from connection, check the sign and normalization of \`∇_(m C_n)\` and the negative-half wave Hessian, reproduce three random metric seeds with four independent second jets, show a nonzero Ricci response to changed second jets, and check the causal principal wave sign for signature (−+++). Distinguish this exact continuum nonlinear principal-operator verification from a completed nonlinearly evolved 3D GH spacetime. Test the standalone pp-wave benchmark v15.1477 separately; there B=0 and no EM excitation.

**NEXT:** build a time-stepped *nonlinear* generalized-harmonic Einstein–H² solver with full gauge constraint and energy monitors, starting from the actual v15.1473 constrained periodic initial data and separately validating the exact nonperiodic pp-wave of v15.1477. Require spatial/time convergence, evolved Einstein Hamiltonian and momentum constraints, and no drift of four GH constraints at T=.04 and beyond, without trusting the raw ADM finite-time solver. Only then turn on the full Weyl–F–H² operator with complete metric variation, EFT order-reduction and a matched unconstrained comparator; no q2-to-G derivation exists.
