# Cone Derivation Ledger v15.1453 — Simultaneous nonlinear 3+1 Einstein ADM constraints solved for curved H² sigma initial data

**Date:** 2026-11-25 Eastern. **Lane:** Gravity/Cone. **Status:** [N PASS] nonlinear Einstein Hamiltonian AND momentum constraints simultaneously solved, to rapidly converging Fourier spectral residuals, for explicitly chosen positive-energy curved H² sigma Cauchy data on a periodic 3-torus, with uniform homogeneous expansion H and conformal/longitudinal ADM ansatz; [NEGATIVE] coarser N12 grid gives large aliased momentum residual and must be rejected, whereas N24/32/40 converge rapidly; [STRICT SCOPE] this is a solution of the Einstein–sigma **initial constraint equations in a specified spatial conformal ansatz** with a freely chosen κ=8πG, not a solution of full Einstein time evolution, and **does not yet include the Weyl–F–B operator**, EM excitation, metric variation of this operator, or a physical quarter-grid-selected coupling. Additive source SHA **c2b1a207795556144c5a1699137d997e59e50d23**. Previous v15.1450–1452 ledgers and all Lane A/Audit certified objects preserved.

## Gate 1375 — nonlinear constraints with homogeneous solvability

Use the H² target metric `G_AB=δ_AB−phi_Aphi_B/(1+phi²)`, f*r=1 and 3D periodic initial sigma data inherited from v15.1450:

`u=.16 sin x;v=.13 sin(2y+.3);u_t=.10 sin(2x);v_t=.09 sin(4y+.6)`.

The actual sigma normal energy and ADM momentum on a conformal spatial slice `γij=e^(2ψ)δij` with lapse normalized to 1 are

`rho_gamma=½ G_AB(phi)[phi_t^Aphi_t^B+e^(−2ψ)Σi∂i phi^A∂i phi^B]`,
`j_i=−G_AB(phi)phi_t^A∂i phi^B`.

Write `Kij=−H γij+e^(2ψ)Aij`, `Aij=(LW)ij=∂iWj+∂jWi−(2/3)δij∂·W`, so K=−3H and `K²−KijK^ij=6H²−Aij Aij`.

The FULL nonlinear 3D spatial scalar curvature for this ansatz is

`³R=e^(−2ψ)[−4∆ψ−2|∇ψ|²]`.

Hamiltonian and momentum constraints therefore become the explicit coupled elliptic system

`e^(−2ψ)(−4∆ψ−2|∇ψ|²)+6H²−A²=2κ rho_gamma`,

`∂j Aij+3(∂jψ)Aij=κ j_i`.

The latter coefficient 3 is from the exact Levi-Civita divergence of a symmetric tracefree `A^j_i` in a three-dimensional conformal metric, **not** the flat momentum constraint `∂j Aij=κj_i` alone. The homogeneous H is updated simultaneously using the **spatially integrated** Hamiltonian solvability condition, rather than imposing a nonzero average Laplacian on a torus. With `kin=G_AB phi_t^A phi_t^B`, `spatial=G_AB Σi∂i phi^A∂i phi^B`, `q=e^(2ψ)`, solve

`H²=<2|∇ψ|² + q(A²+κ kin)+κ spatial> / [6<q>]`.

Angle brackets mean the coordinate spatial average. This is not an arbitrary cosmological constant: it is the homogeneous extrinsic-curvature degree of freedom required by the mean matter density.

## Gate 1376 — coupled Fourier elliptic solve and nonlinear momentum correction

For the nonzero spatial Fourier modes, invert the flat vector-Laplacian `∂j(LW)ij=∆W_i+(1/3)∂i∂·W` by decomposing the Fourier source into longitudinal/transverse pieces. The full nonlinear momentum equation can be solved iteratively using

`∂j(LW_new)ij=κ j_i−3∂jψ(LW_old)ij`.

The scalar Hamiltonian updates `ψ` by solving a periodic Poisson equation for the **nonlinear** right-hand side, with zero mean and H updated from its integrated solvability condition. The weighted momentum solvability condition `<e^(3ψ)j_i>=0` is satisfied by the chosen symmetric sigma data to roundoff; otherwise a non-comoving homogeneous momentum/background degree of freedom would be needed. Both elliptic equations are iterated together until change in ψ and Fourier W is <2e−16.

**Actually executed independent local code** `/mnt/data/cone_gate/k4_h2_adm_both_constraints_solve.py`, NumPy/SciPy-free spectral FFT implementation. New additive GitHub source `research-notes/k4_h2_adm_both_nonlinear_constraints_v15_1453.py`, commit **c2b1a207795556144c5a1699137d997e59e50d23**, independently authored to reproduce the same exact equations and N24/32/40 convergence; exact committed-byte external Audit replay pending.

| N³ | iterations | H | max |ψ| | max Hamiltonian residual | max momentum residual |
|---:|---:|---:|---:|---:|---:|
| 24³ | 3 | 0.005259956001291482 | 4.08998657e−6 | 6.64e−19 | 9.72e−12 |
| 32³ | 3 | 0.0052599560012433445 | 4.23255570e−6 | 1.00e−18 | 2.90e−14 |
| 40³ | 3 | 0.0052599560012433445 | 4.26208790e−6 | 3.23e−18 | 2.54e−17 |

H is stable to ~5×10−14 absolute between N32 and N40; grid maxima of ψ need not be monotonic. The Hamiltonian residual is near roundoff because the nonlinear Poisson equation is enforced; the momentum residual decreases rapidly with grid resolution as spectral aliasing fades. For N12 the same solver returns a **FALSE/FAILED momentum-constraint residual ≈2.73818×10−5**, despite the nonlinear Hamiltonian residual ≈2.03×10−19 and three-iteration update convergence. N16 has ≈2.08×10−9, N24 ≈9.72×10−12, N32 ≈2.90×10−14, N40 ≈2.54×10−17. **These negative N12/N16 results are recorded explicitly**; algebraic iteration convergence without constraint-residual evaluation is NOT enough. N24 is a useful intermediate verification, N32–N40 resolves the nonlinear momentum constraint to strong numerical precision. Still not a mathematically certified continuum elliptic solution: Fourier interpolation, nonlinear aliasing and finite resolution remain.

## Gate 1377 — what is now closed and what is not

These constructed metric and extrinsic-curvature Cauchy fields satisfy the full nonlinear standard ADM Hamiltonian/momentum **constraints of the chosen Einstein+H² sigma action** on the tested grids (at high resolution). They do **not** specify a completely evolved 3+1 solution: lapse/shift and evolved geometry must satisfy the ADM/BSSN hyperbolic equations and propagate constraints. We have not yet turned on a transverse gravitational TT wave or electromagnetic field in the initial data. The **original extra Weyl–F–H²-area interaction** requires an independent metric variation including higher derivatives; treating its initial constraint modification as identically zero merely because the initial EM field may be set to zero would not be justified without checking derivative data and the full constraints. Thus this is a stronger physical **initial-data prerequisite**, not the conclusion of the full covariant EFT completeness gate.

The matter energy normalization f*r=1 and κ=.003 were both illustrative freely chosen scales. The standard Einstein Hamiltonian constraint determines H *given κ and sigma energy*, not κ from quarter-grid arithmetic. The discrete closed q2 Casimir (Q=1/16), null-affine 3:1 interval and conditional ±π/2 loop holonomy remain representation geometry, not a G-free parameter selector. The 45.310004305 historical rapidity still contains measured G in its defining Dirac ratio.

**AUDIT HANDOFF:** Independently derive conformal ³R and `D_j A^j_i=∂j Aij+3ψ_j Aij` for this precise Kij ansatz; reproduce nonlinear integrated Hamiltonian H² identity and momentum solvability; replay v15.1450–1453 exact committed scripts, including the N12 coarse-grid FAILURE of v15.1453 and N24/32/40 positive results; verify that weighted momentum zero mode vanishes and check solver for aliasing via Fourier zero padding or de-aliasing. Verify target stress positive with φ values, that κ remains free, and that v15.1450–1452 are strictly first-order/progressive gates rather than contradictory models.

**NEXT:** evolve these fully constrained Einstein–sigma initial data with actual metric dynamics and a constraint-preserving gauge (e.g. BSSN/generalized harmonic), monitor constraints and the sigma stress Ward identity. Separately derive full four-dimensional Weyl–F–area metric stress and EFT order reduction, then incorporate Maxwell fields and test causal principal characteristics and total energy in a **single** coupled system. If no independent quarter-grid operator fixes κ and ζ/Λ², the same-enlarged-EFT comparator produces the same dynamics; do not claim a new G force.
