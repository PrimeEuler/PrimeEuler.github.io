# Cone Derivation Ledger v15.750 — Gravity: one evolved spatially compact positive-energy scalar sources all three K4 electric Weyl channels

**Date:** 2026-11-11 US Eastern. **Parents:** original K4 action v14.928/935, sourced scalar Ward/pressure and traceful Weyl v15.727–730, compact initial canonical stress and Weyl v15.731/v15.740, conventional source-first vector/tensor Weyl v15.721–722, conserved source-pulse selection v15.724–725. **Audit:** Round 547/v15.741 independently confirmed the v15.724–731 and v15.740 chain, including the v15.732/733 collision disclosure. Suzuki v15.743 on live HEAD; v15.750 chosen as a separate gravity number. **Classification:** [D] exact coasting Klein–Gordon Fourier-mode time evolution and source-conservation identities; [N] finite-resolution initial-value numerical example with all three *gauge-invariant* electric Weyl curvature components nonzero; [C] interpretation as a calibrated observable or unique Cone gravitational coupling not established; [O] full physical source evolution on a realistic cosmological/astrophysical background, backreaction, instrument response and conventional elasticity comparator.

**Immediately prewrite live HEAD:** 09f10439595d197ddfadf7a75415335d46340f0f. Ledger target confirmed absent. All changes additive; historical scripts and protected Suzuki/far-tail files untouched.

## Gate 375 — evolve physically specified compact canonical matter, not prescribed Fourier stress

Use the v15.727 conventional minimally coupled real *massless* scalar with canonical positive local energy density on the coasting FLRW background **a(tau)=tau/sqrt(3)**, and at tau0=1 set

**chi0(x,y,z)=w_R(x,y,z)[cos(2x)+cos(z)]**, **chi_dot0=-chi0**,

where **w_R=product h(u/R)**, **h(s)=(1-s²)^8** for |s|<1 and zero outside. This is spatially compact C7 scalar initial data, the same class independently audited at v15.731/740. For this gate **R=7**, periodic *computational* box side **L=8π**; the packet and its domain of dependence stay strictly away from periodic boundaries to tau=1.35 because the comoving light-travel radius from tau=1 is **sqrt(3) log(1.35)≈0.52**, compared with the box half-size 4π≈12.57 and packet support radius 7 along each Cartesian coordinate. No periodic wrap-around occurs in the physical domain of support over this time range.

The exact coasting KG solution is obtained Fourier mode by Fourier mode, with **q** spatial wavevector and **omega_q²=3|q|²-1**:

**chi_q(tau)=chi0_q cos(omega_q log tau)/tau**.

The initial derivative choice chi_dot0=-chi0 sets the independent logarithmic sine coefficient to zero. Modes with omega_q²<0 are continued analytically as cosh with imaginary omega_q. The first and second time derivatives and all three spatial gradients are calculated analytically from this representation, not by numerically differencing the field, so the scalar wave equation is satisfied mode by mode. Every time slice retains nonnegative local scalar energy.

For the normalized source Fourier component **K=(2,0,1)**, K²=5, use a box side L=8π and therefore correctly locate the FFT coefficient at bin **(8,0,4)**, *not (2,0,1)*. The normalization **sum(w_R²)** removes the extensive packet scale to compare resolutions and is not an experimentally calibrated source strength. A wrong-bin trial was detected and discarded during local reproduction before committing; only the corrected code and numbers are claimed.

## Gate 376 — exact matter time-dependent stress feeds all three constrained modes

At each time, compute the canonical matter stress density and pressure trace from the *same* evolving chi:

**rho=(chi_dot²+|grad chi|²/a²)/2**, **P_trace=(3chi_dot²-|grad chi|²/a²)/2**.

In the original K4 scalar ADM conventions, Fourier source coefficients are

**J_Phi=a³ rho_K**, **J_psi=a³ P_trace,K**,

**J_B=-i a² [chi_dot (K.grad chi)]_K**, including its analytic time derivative **J_B_dot**. The source Ward identity from v15.728 is checked directly from analytic scalar time derivatives, **tau J_Phi_dot+sqrt(3)J_B+J_psi≈0**, with the residual converging under spatial FFT resolution. This includes the physical pressure term absent in the earlier signed tracefree source.

For vector polarization choose unit transverse basis **e1=(1,0,-2)/sqrt5** and **e2=(0,1,0)**, perpendicular to K. Then from the same matter stress,

**J_V=a²[chi_dot (e1.grad chi)]_K**,

**J_V_dot=a²[(2/tau)chi_dot(e1.grad chi)+chi_ddot(e1.grad chi)+chi_dot(e1.grad chi_dot)]_K**,

**Pi_T=[((e1.grad chi)²-(e2.grad chi)²)/(2a²)]_K**.

Here brackets mean the normalized K Fourier coefficient; all formulas are standard metric-stress couplings and no independently fitted sector amplitudes are inserted.

For **eta=3/4, kappa=C=1, K²=5**, the original sourced K4 homogeneous dynamical coefficients (coasting Euler frequencies) are

**beta_S=[8eta(1+K²)-3K²]/3=7**,

**beta_V=2eta(4+3K²)/3=19/2**,

**beta_T=3K²+8eta/3=17**,

giving the *exact conventional elastic* difference ratio

**(beta_T-beta_V)/(beta_V-beta_S)=3**.

The source-first scalar equation (v15.728) is

**P_ddot+3P_dot/tau+beta_S P/tau²
=3sqrt(3)J_psi/(2K² tau³)-9(tau J_B_dot+J_B)/(2K⁴ tau³)**.

The source-first vector shift constraint and vector mode equation from v15.710/721 are

**B_V=b_V f_dot-J_V/A_V**,

**f_ddot+3f_dot/tau+beta_V f/tau² = -(b_V J_V)'/K_V**,

with **b_V=4tau/[sqrt3(4+3K²)]**, **K_V=2tau³ K²/[3sqrt3(4+3K²)]**, **A_V=tau(4+3K²)/(6sqrt3)**.

The tensor equation is

**gamma_ddot+3gamma_dot/tau+beta_T gamma/tau² =-2kappa Pi_T**.

Every J and Pi comes from a *single evolving physical matter field*.

## Gate 377 — source-to-gauge-invariant tidal transfer, consistent initial data

At tau=1 impose zero K4 *propagating* scalar/solid/vector/tensor dynamical initial data **P=P_dot=f=f_dot=gamma=gamma_dot=0**. The *nondynamical* ADM lapse/shift are sourced and solved from their constraints, **not artificially set to zero**. This is a constrained initial-value problem with matter already present at tau=1. It is NOT a solution with source and curvature zero for all past time, and therefore not a full retarded emission/detection setup.

Integrate all three forced Euler systems using the same computed matter histories. Reconstruct scalar gauge-invariant Newtonian potentials using the full pressure-corrected v15.729 formulas:

**Phi_N=[tau²P_ddot+2tau P_dot]/[3(1+K²)] +sqrt3(J_Phi+J_psi)/[2tau(1+K²)] -3J_B_dot/[2K²(1+K²)]**,

**Psi_N=[K²P-tau P_dot]/[3(1+K²)] +sqrt3 J_Phi/[2tau(1+K²)] +3J_B/[2K²tau(1+K²)]**.

The scalar electric Weyl STF amplitude is **W_S=K²(Phi_N+Psi_N)/(2a²)**. The sourced vector electric Weyl component in the orthonormal (Khat,e1) basis is **W_V=-i|K| B_V_dot/(4a)**. The plus tensor electric Weyl component in the orthonormal transverse (e1,e2) basis is **W_T=[tau²gamma_ddot+tau gamma_dot-3K² gamma]/(12a²)**. These are individual curvature components, not quantities with universal relative normalization.

## Gate 378 — numerical grid/refinement test and explicit finite-time three-sector result

The spectral propagation uses exact linear KG Fourier mode functions, periodic computational grid and spectral spatial differentiation, with cubic interpolation of the *matter-derived* source coefficient histories into high-accuracy forced ODE integration. The packet support stays away from the computational boundary. Two independent spatial/time refinements reproduce the following dimensionless, Fourier-normalized curvature amplitudes at **tau=1.35**:

| Grid / source-time samples | W_S | W_V | W_T |
| --- | ---: | ---: | ---: |
| 48³ / 21 | +0.2258728529 | +0.0326043136 | +0.1238078600 |
| 64³ / 31 | +0.2258728585 | +0.0326043176 | +0.1238078821 |

At the initial slice tau=1, the 64³ run gives **(W_S,W_V,W_T)≈(0.8824934282,-0.47033198,-0.31118537)**, a reminder that the sourced constraint/contact fields need not vanish even if the six propagating initial dynamical amplitudes do. At tau=1.35 the scalar solid displacement is **P≈0.0096046982**, initially zero.

The direct analytically differentiated Fourier energy Ward residual has maximum approximately **3.70×10^-8** for 48³ and **1.34×10^-11** for 64³, consistent with resolution-dependent alias/truncation in quadratic source products. The source spline derivative is less accurate (~10^-6 at these settings) and is **not** substituted for the direct analytic derivative when asserting conservation. At 64³, both the angular matter source and the Weyl outputs are real to numerical roundoff after conjugate Fourier pairing.

The actual fields and stress are dimensioned by the small spectator amplitude squared, plus the artificial Fourier-volume normalization used to compare resolution. The numerical values above are not gravitational strain amplitudes in SI units or a measurement of G. Source spatial localization and positive canonical energy are physical properties of the chosen matter action; K4 coasting FLRW is a deliberately chosen, observationally disfavored model background.

## Gate 379 — scientific verdict and next falsification checks

**[D]** For the first time in this chain, one *spatially compact, canonical positive-energy scalar matter field* has been evolved in time and has produced three explicit scalar/vector/tensor **electric-Weyl curvature** signals through independently sourced K4 constraints, not just nonzero stress projectors or a prescribed signed Fourier pulse. The numerical convergence is strong within the stated finite-time window. The standard trace-free shape factor **2/3** remains a representation-theoretic identity for scalar Weyl; the amplitudes **0.2259, 0.0326, 0.1238** are not fixed by that identity.

**[N]** The exact mode-frequency gap ratio **3** is conventional coasting isotropic relativistic elasticity and is not itself a new Cone prediction. The three curvature signals have significantly different evolving amplitudes; the source and detector helicity choices matter. K4 is not a physical explanation for a new Newton G here, and nothing selects the Cone quarter grid as the source strength or measurement scale.

**[O]** Extend to spatially localized **instrument geometry** and a retarded radiation-zone waveform from an actual external source, with full metric and matter backreaction on a realistic background. Compare against ordinary GR+solid under the same source and detector setup. The physically preferred background/eta/length-scale selector remains unsolved.

**Reproducer:** research-notes/k4_compact_canonical_retarded_three_weyl_v15_750.py, additive commit **09f10439595d197ddfadf7a75415335d46340f0f**. Local implementation executed on 48³/21 and 64³/31 to PASS with the detailed amplitudes and Ward residuals above. The committed reproducer encodes the same mode propagation, pressure-Ward check, source-first K4 ODEs and Weyl transfer with an explicit two-resolution assertion. No image generation; no protected/certified source rewrites.

**HANDOFF — independent external audit:** verify the precise FFT bin for the box side L=8π, all KG time derivatives and finite causal support, first- and second-order canonical matter coefficients, sign normalization of J_B and J_V under +--- versus -+++ conventions, the vector shift contact/derivative in E_V, TT source normalization, scalar pressure-corrected Ward, and the 48³/64³ convergence. Critically distinguish **constrained initial-value sourced curvature** from a fully retarded no-past-source signal. Preserve the v15.732/733 collision history as disclosed and avoid new immediate-version collisions with Suzuki.
