# Cone Derivation Ledger v15.1473 — Full nonlinear Einstein–H² ADM initial slice now simultaneously satisfies four spacetime harmonic gauge constraints

**Date:** 2026-11-25 Eastern. **Track:** Gravity/Cone, primary nonlinear generalized-harmonic evolution path. **Classification:** [ACTUAL NUMERICAL PASS] reconstruct the full 4D contracted Christoffel harmonic-gauge constraints on the **identical nonlinear 3+1 spatially inhomogeneous Einstein–H² sigma initial slice** obtained from v15.1453, with correct lapse and shift time derivatives, and verify all four vanish to roundoff concurrently with the ADM Hamiltonian and momentum constraints; [CONTROL NEGATIVE] setting both initial lapse and shift time derivatives to zero produces an O(1.6×10^-2) nonzero harmonic-gauge violation even though the ADM constraints are satisfied; [STRICT OPEN] nonlinear generalized-harmonic *time evolution*, preservation of gauge and Einstein constraints after evolution, well-posed gauge damping/filtering, full Weyl–Maxwell EFT metric stress, and independently selected G remain unproved. **Audit** previous v15.1466–1470 pending; all earlier certified Lane A/Sandbox/Audit objects preserved.

## Gate 1397 — initialize harmonic time derivatives on actual nonlinear constrained fields

Use the **fully nonlinear** periodic ADM conformal solution with coordinates x,y,z and the exact curved-H² sigma target from v15.1453, not an illustrative hand-picked conformal metric. The actual nonlinear initial data are:

`gamma_ij=e^(2psi) delta_ij`, `K_ij=e^(2psi)[(LW)_ij−H delta_ij]`, where psi,W,H are solved together from the full Hamiltonian and momentum constraints with κ=.003 chosen, and the two sigma fields and their normal velocities use the fixed v15.1453 profiles. The mean positive sigma energy forces H≈.005259956.

Choose **initial** lapse α=1 and shift βi=0. In 4D harmonic gauge with source functions Hμ=0, the contracted spacetime Christoffels `Gamma^mu=g^alpha beta Gamma^mu_alpha beta` must vanish. The exact corresponding 4-metric time derivatives at the initial slice are:

`partial_t g_00=−2 dot alpha`, `partial_t g_0i=gamma_ij dot beta^j`, `partial_t g_ij=−2 K_ij`.

Harmonic gauge fixes the otherwise missing time derivatives

`dot alpha=−K`,
`dot beta^i=gamma^jk (3)Gamma^i_jk=−e^(−2psi) partial^i psi`.

No gauge condition is imposed by hand on the numerical divergence after this prescription: it is recomputed from **all** 4D metric derivatives and the **complete 4×4 inverse metric** through its defining Christoffel expression and contracted independently. The ADM constraints are separately recomputed by the original nonlinear v15.1453 elliptic solver. Thus one and the same matter+geometry slice satisfies both sets of initial conditions. This is an important step from the previous v15.1468 *illustrative* slice to the actual v15.1453 constrained slice.

## Numerical checks

**Actually executed self-contained local Python** `/mnt/data/cone_gate/k4_h2_constrained_gh_initial_v15_1472.py`: starts with the literal v15.1453 solver, returns its physical `psi,A,q`, constructs complete 4D g derivative array and Γμ, and compares with a deliberately incorrect zero-`dot alpha`/zero-`dot beta` control. This local name reflects when the scratch file was built. The additively committed complete reproducer is **v15.1473**, `research-notes/k4_h2_constrained_gh_fullcheck_v15_1473.py`, commit **d5bd33d0a9e4c9db0cb44c51e5c9dd44ff64d301**, constructed from canonical v15.1453 source and same analytic independently tested gauge calculation. An earlier v15.1472 **helper-only** file `research-notes/k4_h2_constrained_gh_initial_v15_1472.py`, commit **0ce757caa996c43afeedab1a4b36e0584779309e**, is only a reusable copy of the initial-data solver returning fields; it does **NOT** contain or certify the harmonic-gauge check and must not be used as the reproducer of this gate. The helper is preserved additively rather than rewritten.

| N³ | initial nonlinear ADM Hamiltonian max | ADM momentum max | four GH conditions maximum | deliberately wrong initial derivatives GH maximum |
|---:|---:|---:|---:|---:|
| 24³ | 6.64073830647e−19 | 9.72070165383e−12 | 3.46944695195e−18 | .01577986800387445 |
| 32³ | 1.00288700955e−18 | 2.89831703017e−14 | 6.07153216592e−18 | .015779868003730036 |

Correct mean lapse derivative `mean(dot alpha)=.01577986800387`, about +3 times the required background expansion H, and maximum initial `|dot beta^i|≈6.39e−6`. **Crucial distinction:** harmonic gauge condition `Gamma^mu(t0)=0` is algebraic/initial, not a certificate that its *time derivative* or its nonlinear subsidiary wave equation is preserved. Initial `K_ij` and `gamma_ij` also do not alone specify the metric's future harmonic 4D evolution. The v15.1466 principal-wave test establishes only **linear** hyperbolicity; v15.1470 demonstrates **homogeneous** nonlinear gauge evolution; this new gate closes their missing *inhomogeneous nonlinear initial-data connection* but does NOT claim the requested full GH evolution has been achieved.

**Independent Audit handoff:** execute exact v15.1473 committed bytes and independently reconstruct at least Γ0 and Γi from 4D spacetime Christoffels; verify v15.1453 full Einstein Hamiltonian/momentum constraints and correct extrinsic-curvature sign, compare N24/32; verify the deliberately incorrect lapse/shift velocity control. Inspect 1472 helper vs 1473 actual reproducer explicitly to prevent an accidental certification of the helper as the complete test. Investigate whether higher time derivatives/evolved gauge source and Cdot can be initialized consistently from the reduced Einstein–H² equations and prove a constrained subsidiary system.

**NEXT MAIN:** implement **nonlinear 3+1 generalized-harmonic Einstein–H²** metric and sigma wave evolution with `Gamma^mu=0` constraint and the initial data from this gate, true covariant stress source and wave-gauge constraint propagation, explicit constraint monitoring/oversampling, and a controlled T=.04 run. Only then restore full Weyl–F–H² higher-derivative operator through EFT order reduction. The 1/16 variance-susceptibility idea remains Sandbox/independent; neither it nor our conformal initial data derives κ=8πG or the Maxwell coupling.
