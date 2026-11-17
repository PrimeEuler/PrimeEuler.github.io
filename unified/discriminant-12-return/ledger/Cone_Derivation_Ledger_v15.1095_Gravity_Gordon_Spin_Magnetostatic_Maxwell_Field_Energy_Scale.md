# Cone Derivation Ledger v15.1095 — Exact Maxwell field from Gordon spin curl, finite packet energy and the unresolved action-circle scale

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact Fourier solution for ordinary magnetostatic field of a localized Gaussian Gordon magnetization current, transverse Maxwell identities, and total magnetic energy; [N] no spin-selected Compton radius, no independent Cone action operator or gravity coupling; [O] full curved Dirac+Maxwell+K4 stationary solution, stress-energy and ADM source constraints. **Live HEAD immediately prewrite:** eac5edf33bcad0fbb0939c2dd25560e4fccd44bc. Strict additive only, collision checked before write; no old certified, Suzuki, Audit, Sandbox or Muse objects modified.

## Live provenance / redundancy
Latest independently completed Audit Round 592/v15.1092, commit ba571054759c6b4d727c33db57812ef483923871, verified Gravity v15.1089–1090 and Sandbox v15.1088/v15.1091. Gravity v15.1093's curl comparison and v15.1094's Gaussian Gordon spin-current result are not yet independently audited. Sandbox v15.1091's charged-seat action loop with radius hbar/(2mc) gives mu_loop=q_e hbar/(4m), not full Dirac spin moment, and explicitly recognizes a nonliteral Zitterbewegung interpretation. Gravity v15.1094 instead showed standard low-energy Dirac/Pauli spin magnetization current with zero convection can yield mu_spin=q_e hbar/(2m). This entry moves that specified current through Maxwell's **actual sourced magnetostatic equations** to its B field and energy, without treating its curl as a new gravitational field or a selected action circle. Earlier v14.829–834 micropolar rotor curl was an independently stipulated elastic operator with objectivity limitations, not Maxwell spin current; it cannot be silently identified with this sourced B or a covariant K4 elastic modulus.

## Gate 929 — Fourier current and field
Take normalized rho(x)= exp(-|x|²/L²)/(pi^(3/2) L³), L>0, spin polarization zhat, and K=q_e hbar/(2m), where q_e is signed electric charge. In c_light=mu0=1 magnetostatic units,
j_spin(x)=K curl(rho zhat)=K(∂y rho,-∂x rho,0).
With Fourier transform \hat f(k)=∫exp(-ik·x)f(x)d³x,
rhohat(k)=exp(-L²k²/4),
jhat(k)=iK(k cross zhat)exp(-L²k²/4).
Thus k·jhat=0 and jhat(0)=0. These do NOT imply mu=0: magnetic moment is a derivative of jhat at k=0, giving mu_z=K as established in v15.1094.

For time-independent sourced Maxwell magnetostatics, with div B=0, curl B=j_spin, and appropriate decaying field boundary condition,
Bhat(k)=[i k cross jhat(k)]/k²
=K exp(-L²k²/4)[zhat-k k_z/k²] for k ≠ 0.
The bracket is the ordinary rank-2 transverse projector onto directions perpendicular to k. Direct symbolic check: k·Bhat=0 and i k cross Bhat=jhat. There is no additional k=0 magnetic flux delta-function source specified; the value at exactly k=0 is direction-dependent, harmless for L² field-energy integrals and the Fourier inverse.

This source is a **magnetostatic approximation** for a prescribed Dirac/Pauli current; a real Gaussian free wavepacket disperses in time, its charged particle generally also has charge density and electric Coulomb field, and it cannot be assumed to provide a fully stationary, self-consistent isolated Dirac-Maxwell source. All such additional physical source terms and matter stresses must be included before a claim about total energy, gravitation or detector response.

## Gate 930 — exact sourced magnetic energy
Parseval in the specified Fourier normalization gives
U_B=1/2 ∫_R³ |B(x)|²d³x
=(K²/2)∫ d³k/(2pi)³ exp(-L²k²/2)[1-k_z²/k²].
The spherical angular integral of sin²theta is exactly 8pi/3; the radial Gaussian integral is ∫_0^infty k² exp(-L² k²/2)dk = sqrt(2pi)/(2L³). Therefore,
**U_B=K²/[3(2pi)^(3/2) L³]** in mu0=1 units.
With physical SI magnetostatics restoring mu0, U_B=mu0 K²/[3(2pi)^(3/2) L³], K=q_e hbar/(2m) (a magnetic moment), and Bhat acquires mu0. The finite width L regularizes the magnetic self-energy; U_B diverges ~L^-3 as L->0 within this effective low-energy magnetostatic model. The magnetic dipole moment K stays unchanged, so shrinking L by 2 multiplies energy by exactly 8. There is **no stationary variational minimum in L from this positive magnetostatic energy alone** (it decreases monotonically with L). Adding Dirac kinetic, electrostatic, confinement, quantum corrections or gravity changes the energy functional and must be derived from its full action; no Compton-scale optimum follows from this submodel.

For a magnetostatic field, T_EM is nonzero and acts as ordinary Einstein–K4 gravitational source, but this entry computes its **spatially integrated B² energy only**, not its full spacetime stress, metric solution, ADM source or gauge-invariant tidal Weyl. The result has L and physical mu0,q_e,hbar,m rather than selecting G, a q2 arithmetic transition, or a new dimensionless gravitational observable.

## Gate 931 — comparison with action circle and ordinary spin gravity
The Sandbox idealized Zitterbewegung radius L_Z=hbar/(2mc) is a model input, **not** fixed by Maxwell's curl equation. Substituting L=L_Z into U_B yields a number but does not make it a derived particle size or match K4's material length scale. In particular current curl ∇×(rho zhat) is a standard Dirac spin-magnetization current; its Fourier transverse projector is ordinary Maxwell theory. The same source, field energy and stress would be present in any conventional Dirac–Maxwell model containing this wavepacket. Coupling the resulting matter sources to standard Einstein+the same isotropic elastic solid preserves the matched-gravity null baseline.

A genuine Cone-specific prediction would require an independently derived, covariant action term modifying spinor dynamics, K4 response or an electromagnetic boundary selector and would need to pass gauge symmetry, diffeomorphism Ward constraints, stability and source/probe normalization tests without importing measured G.

## Gate 932 — reproducibility and Audit request
Exact reproducer: research-notes/k4_gordon_spin_magnetostatic_field_v15_1095.py, commit eac5edf33bcad0fbb0939c2dd25560e4fccd44bc. An equivalent SymPy calculation was run in the local container before committing: PASS for exact Fourier B projector, divergence/current Ampere identities, angular/radial Gaussian integral and factor-eight localization scaling. Independent Audit pending.

**AUDIT HANDOFF:** check Fourier convention, sign of Ampere inversion, zero-mode caveat, angular integral 8pi/3, energy factor 1/[3(2pi)^(3/2)], SI mu0 conversion and full charged-Dirac apparatus limitations; verify no inference of a literal electron current ring or new Cone gravitational selector. **NEXT:** attempt sourced Dirac/Maxwell stress and linearized gravity decomposition for a specified physically consistent time-dependent packet or, alternatively, inspect independent symmetry-allowed low-dimensional spin/tetrad couplings with coefficients left free and test whether any Cone arithmetic fixes them. Never equate curl circulation with mechanical action without a physical current/phase action.
