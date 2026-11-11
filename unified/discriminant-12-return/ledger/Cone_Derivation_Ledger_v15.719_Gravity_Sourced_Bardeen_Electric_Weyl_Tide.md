# Cone Derivation Ledger v15.719 — Gravity: sourced K4 Bardeen potentials, scalar Weyl tide, and a physical 2/3 STF norm

**Date:** 2026-11-11 US Eastern. **Parents:** v14.935 original Einstein–Hilbert plus elastic-solid quadratic scalar action; v15.709 local gauge-invariant Riemann electric-tidal detector controls; v15.712 exact source-before-constraint mixed scalar Lagrangian; v15.713–714 scalar source consistency and retarded mode response; v15.716 coasting-FLRW covariantly conserved tilted anisotropic Fourier stress and dimensional STF 2/3; v15.717 exact Ward/source matching and particular solution. **Independent audit:** Round 545/v15.718 independently verified v15.708–715 and the crucial v15.713 archive issue, with a correction: the original state-space script does NOT visibly crash at 0/0; floating-point noise produces a finite, meaningless alpha that happens not to contaminate its printed dispersion at tested points. The mathematical psi elimination is still ill-defined, whereas the independently reconstructed P equation and scalar dispersion survive. This ledger preserves the audit's exact nuance.

**Immediately prewrite live HEAD:** 5956a47547acfb5bd2a938bd500f9bf5c8797535; target v15.719 ledger path absent, v15.718 occupied by audit. Additive-only; no Suzuki/far-tail or historical v14.935 modifications.

**Result status:** [D] explicit gauge-independent metric potentials for one covariantly conserved Fourier source and one sourced particular scalar-mode solution; [D] first nonzero scalar electric-Weyl response from the source-first chain; [D] same universal STF 2/3 norm for source and scalar tidal eigen-tensor; [C] chosen source realization, physical initial/boundary conditions and complete detector calibration; [N] new parameter-free Cone gravity constant or universal tidal coupling not yet found.

## Gate 326 — reconstruct lapse and shift from original constraints, preserving time dependence

Use the exact v14.935 EH+solid scalar quadratic action regenerated in the additive v15.712 reproducer, with spatial scalar E=0 gauge. The constrained variables are **Phi** (lapse perturbation) and **B** (longitudinal shift potential, metric g_0z=-a partial_z B). Their unsourced auxiliary Hessian H and mixed vector d(psi,P,psi_dot,P_dot) are not postulated: they are extracted from the original action as in v15.711–712.

Insert the exact coasting background **a=tau/sqrt(3), Hubble=1/tau, kappa=C=1** at fixed nonzero comoving wavenumber k. Use the v15.717 conserved tilted tracefree stress with amplitudes sigma and rho0 and corresponding formal ADM source coefficients

**J_Phi=sqrt(3)(k² sigma tau+4 rho0)/36**,

**J_B=-k² sigma tau/36**,

which satisfy the sourced energy Ward identity. Choose the exact v15.717 **particular**, not arbitrary retarded, displacement solution

**P_part = sigma/(4 k² beta)**,

**beta=1+(8 eta-3)(1+k²)/3>1** in the stable eta>3/8 range.

Keeping the residual scalar-gauge function psi(tau) arbitrary, solve the full original sourced nondynamical constraint exactly:

**(Phi,B)^T = -H^(-1)[d(psi,P_part,psi_dot,0)+(J_Phi,J_B)^T]**.

The result contains psi and its derivative as expected for a gauge-dependent shift/lapse. It will be combined into invariant observables in the next gate.

## Gate 327 — explicit gauge-invariant Newtonian potentials

For the scalar perturbation in the original +--- ADM sign convention, with E=0 and longitudinal shift g_0z=-a partial_z B, the usual time-slicing invariant Newtonian/Bardeen combinations are

**Phi_N = Phi + d(a B)/d tau**,

**Psi_N = psi - Hubble a B**.

They are invariant under a residual first-order time-coordinate change in the specified conventions. Substitution of the full sourced constraints and the particular P_part gives the exact cancellations of psi and psi_dot:

**Phi_N = sigma/24 + rho0/[6 tau(1+k²)]**,

**Psi_N = sigma/24 + rho0/[6 tau(1+k²)] - sigma(8 eta-3)/[12 D]**,

where

**D=8 eta(1+k²)-3k² = 3+(8 eta-3)(1+k²) =3 beta**.

The gravitational slip is therefore

**Phi_N-Psi_N = sigma(8 eta-3)/(12D)**.

These are source-dependent gauge-invariant scalar metric potentials for one particular solution of the linearized K4 equations, rather than arbitrary potential ratios inserted after deriving a dispersion. Both vanish for the zero source sigma=rho0=0 (up to separate homogeneous solutions). Their overall normalization depends on the physical source amplitudes; the external stress was constructed as a conserved Fourier template rather than derived from a specific positive-energy localized matter action.

## Gate 328 — scalar electric Weyl gives a gauge-invariant tidal measurement and another exact 2/3

The FLRW background is conformally flat, so **Weyl(background)=0** and its first-order perturbation is gauge invariant. Independently derive the four-dimensional linearized Weyl tensor from the local scalar Newtonian metric perturbation (signature +---) **h_00=2 Phi_N**, **h_ij=2 Psi_N delta_ij**, with Fourier spatial wavevector along z. The electric Weyl matrix in a local orthonormal FLRW frame is, with a consistent Riemann sign convention,

**E^Weyl_(ij)= [k²(Phi_N+Psi_N)/(2 a²)] (z_i z_j-delta_ij/3)**.

The scalar tide therefore has physical orthonormal eigenvalues **(-W/3,-W/3,2W/3)** with

**W = k²(Phi_N+Psi_N)/(2 a²)**.

Its norm is

**E^Weyl_(ij)E^Weyl_(ij)=(2/3)W²**.

This 2/3 is EXACTLY the same three-dimensional STF dyad norm independently derived for the conserved anisotropic source in v15.716, now appearing in a bona fide gauge-invariant curvature tensor. The scalar curvature *tensor shape* is a standard consequence of the rotational representation and of the trace-free Weyl decomposition; it does not make W a universal gravitational coupling. In particular, the tidal eigenvalue pattern and 2/3 norm follow from conventional scalar metric perturbation theory, not uniquely from the Cone quarter Casimir.

## Gate 329 — the sourced tidal amplitude retains material parameters and background limitations

Define the source-normalized scalar potential sum with the additional homogeneous density amplitude set rho0=0:

**12(Phi_N+Psi_N)/sigma =
 [3+(8 eta-3)k²]/[3+(8 eta-3)(1+k²)]**.

This is dimensionless and independent of the overall sigma, but **still depends on the free K4 elastic parameter eta and comoving k**, and cannot be interpreted as a new universal Cone parameter-free number. More generally rho0 contributes the additional time-dependent term **rho0/[3 tau(1+k²)]** to the potential sum and can change or cancel the Weyl amplitude. A full detector transfer also needs physical source preparation, real wave-packet superposition, the proper local orthonormal tetrad, and matching to a realistic cosmological/observational background. The coasting K4 cosmology remains observationally disfavored by the prior full-covariance supernova comparison.

The assumed P_part is an exact steady/particular solution, **not** the unique zero-initial-data retarded response: homogeneous modes may be added. The derived Weyl field is correspondingly a source-conditioned particular tide, not a universal response valid for all boundary conditions.

**Positive milestone:** The entire scalar source-first chain now reaches a **nonzero gauge-invariant tidal curvature**, not merely a formal solid displacement. This is an actual conditional field-theory result for the prescribed conserved source. **Novelty verdict:** the universal 2/3 is an ordinary STF norm, and the response amplitude depends on the K4 material and source; no new G-free parameter-free distinguishable gravitational observable is certified.

**Reproducibility:** additive research-notes/k4_sourced_scalar_bardeen_weyl_v15_719.py, commit 5956a47547acfb5bd2a938bd500f9bf5c8797535. This regenerates the original archived v14.935 scalar EH+solid quadratic action through the additive v15.712 script, recomputes sourced constraint fields, verifies cancellation of the arbitrary psi gauge variable, checks Phi_N/Psi_N and material slip exactly, independently derives the full four-dimensional linearized Weyl tensor, and verifies the electric Weyl STF norm 2/3. The independent local algebra was checked with SymPy before commit; external execution/audit of the committed script remains requested.

**HANDOFF — external audit high priority:** independently regenerate and execute the new reproducer, verify all original ADM g_0z and Fourier signs, the Bardeen potential transformation laws and cancellation, conformal Weyl-to-orthonormal 1/a² scaling, and the distinction between a particular solution and a retarded wave-packet response. Check this new result against the precise Round 545 correction to v15.713's original state-space reproducibility wording. No historical silent edits.

**NEXT:** build the true retarded scalar metric/Weyl Green-function transfer by including v15.714's homogeneous addition and source-history dependence, then derive vector and tensor Weyl transfer for the *same* conserved stress. Test whether a source-independent dimensionless response can be isolated once these physically measurable transfer functions, source orientations and conventional elasticity controls are included. If not, close this candidate as a conditional elasticity-wave response, not a new universal Cone gravity constant.
