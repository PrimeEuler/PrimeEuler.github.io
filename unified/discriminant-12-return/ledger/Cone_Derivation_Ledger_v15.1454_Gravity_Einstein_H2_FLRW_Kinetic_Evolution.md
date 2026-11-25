# Cone Derivation Ledger v15.1454 — Homogeneous dynamical Einstein–H² sigma FLRW benchmark with an exact a-cubed invariant

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Classification:** [EXACT D] spatially homogeneous kinetic H² sigma fields in 3+1 flat FLRW generate the standard stiff-fluid Einstein expansion and conserve an internal geodesic kinetic invariant; [N PASS] integrate genuine coupled homogeneous Einstein and curved-target sigma equations numerically, confirming conserved sigma invariant, Friedmann constraint, and exact a³(t) formula at 1e−11–1e−13 relative error; [NEGATIVE] not the inhomogeneous ADM initial data of v15.1453, no spatial gradients or TT sector, no Maxwell/Weyl interaction, and no physically fixed gravitational coupling or quarter-grid sector bridge. Strict additive. Prior v15.1450–1453 inhomogeneous ADM initial-constraint solve preserved, independent Audit of these newer gates pending.

## Gate 1378 — exact Hamiltonian and FLRW benchmark

Use a flat FLRW 3+1 metric `ds²=−dt²+a(t)²δij dx^i dx^j`, with spatially homogeneous real sigma field `phi^A(t)=(u(t),v(t))` in the actual curved positive-sheet H² target `G_AB=δ_AB−phi_A phi_B/(1+phi²)`, with sigma kinetic scale `f²` and `κ=8πG`. Target cotangent momenta per unit comoving spatial volume are `p_A=a³ f² G_AB phi_dot^B`, so the exact inverse metric is `G^AB=δ^AB+phi^Aphi^B`. The conserved canonical sigma kinetic invariant is

`C=δ^AB p_Ap_B+(phi^A p_A)²`.

The true homogeneous sigma Hamiltonian is `H_sigma=C/(2a³f²)`; its canonical equations

`phi_dot^A=[p_A+phi^A(phi·p)]/(a³f²)`,
`p_dot_A=−phi·p p_A/(a³f²)`

preserve C exactly. Its physical energy density and pressure are `rho=p=C/(2a^6f²)`: a standard massless homogeneous sigma stiff fluid, with zero potential and no Weyl–F–area coupling (spatial pullback area B=0 automatically for homogeneous phi). Einstein's Friedmann equation is `3H²=κrho`, with H=a_dot/a. Hence

`a_dot=[sqrt(κ C/(6 f²))]/a²`,
`a³(t)=a³(0)+sqrt(3κ C/(2f²))t`.

The result is a standard exact GR+sigma benchmark, **not a Cone-specific new gravitational law**. The q2 representation radius and its 3:1 null-affine ratio do not select G, f or C.

## Actual numerical evolution and independent analytic comparator

Initial data `a(0)=1, phi(0)=(.15,−.08), p(0)=(.12,.07), f=1`, giving exact `C=0.01945376`. Integrate five real first-order variables with SciPy DOP853, rtol 2e−12, atol 1e−14 to t=120, and compare C at 251 time samples to initial and a³ to the exact linear law. The actual executed local file `/mnt/data/cone_gate/h2_flrw_benchmark_v15_1454.py` produced:

| κ | slope of a³ | a(120) | max relative C drift | max relative a³ difference | max Friedmann residual |
|---:|---:|---:|---:|---:|---:|
| .003 | .00935638391687729 | 1.2851901226207627 | 1.534697e−11 | 1.834711e−13 | 6.77626e−21 |
| .0015 | .006615962515008682 | 1.215068216755339 | 1.586363e−11 | 2.653768e−13 | 3.38813e−21 |

The Poincare-type H² coordinates (u,v) grow very large along this particular target geodesic (at κ=.003, final phi≈(38221.66,15486.02)), while cotangent momenta shrink, yet the target invariant C is preserved; large embedding coordinate values are **not** a physical divergence of energy. H is computed from the Friedmann constraint throughout this run; the tiny displayed Friedmann residual is therefore a partially algebraic consistency check, while the independent a³(t) and C comparisons are the stronger dynamical tests. For an independent *evolution* check of the acceleration equation, the next gate must evolve the metric's second-order Einstein equation and compare its constraint drift, not use Friedmann algebraically to define H.

**Executable:** additive committed `research-notes/k4_h2_flrw_benchmark_v15_1454.py`, source SHA **2cb0396a47b0eaa15b33cc6f456d53046fdfd809**, mathematically equivalent to executed local source and awaiting Audit exact-byte replay.

**AUDIT:** derive H² inverse metric, p_A, C preservation, stiff equation-of-state and exact a³(t) law, independently run source, recognize Friedmann imposed algebraically and target-coordinate growth, and distinguish *spatially homogeneous Einstein dynamics* from fully evolved nonlinear inhomogeneous ADM Einstein–sigma initial data v15.1453.

**NEXT:** integrate independent Einstein a_ddot / Hdot evolution with constraint monitor and move toward gauge-fixed 3+1 inhomogeneous metric evolution of the constraint-consistent ADM initial data. Restore Weyl–F–area only after complete metric variation/EFT order reduction. Do not claim a G-free new physical interaction.
