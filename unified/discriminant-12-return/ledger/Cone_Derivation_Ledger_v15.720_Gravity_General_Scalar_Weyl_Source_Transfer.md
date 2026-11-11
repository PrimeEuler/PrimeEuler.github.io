# Cone Derivation Ledger v15.720 — Gravity: exact general-history scalar source-to-Weyl transfer on coasting K4

**Date:** 2026-11-11 US Eastern. **Parents:** v14.935 source-free K4 Einstein–Hilbert+solid quadratic action; v15.712 reconstructed scalar mixed constraints; v15.713 sourced scalar equation and source Ward; v15.714 scalar retarded Green function; v15.716–717 covariantly conserved tilted traceless FLRW source, and v15.719 particular-source gauge-invariant Newtonian potentials/electric Weyl field. **Audit:** Round 545/v15.718 independently confirmed the v15.713 original scalar_statespace.py has an ill-defined exact 0/0 psi-slaving step *masked*, rather than crashed, by floating-point noise; archived numerical dispersion remains correct at tested points. Historical files preserved. **Status:** [D] exact general-history formal ADM source to Bardeen scalar potential to gauge-invariant electric-Weyl tensor map; [D] verification against the specific v15.719 particular source; [N] no parameter-free Cone tidal coupling; [O] physical localized matter realization, vector/tensor detector transfers and independent experimental readout. **Immediately prewrite HEAD:** af7865359607b9c97ee75d5b6e30a9fc92f953e3; target ledger path absent. Additive-only, Suzuki/far-tail untouched.

## Gate 330 — retain arbitrary scalar history and covariantly compatible source

Start from the actual K4 source-before-constraint scalar Lagrangian of v15.712. On the coasting FLRW background **a=tau/sqrt(3)**, for k>0, include an arbitrary scalar displacement history **P(tau)** and two formal lapse/shift coefficients **J_Phi(tau), J_B(tau)** satisfying the exact compatibility identity, whose physical tracefree-source realization was established at v15.717:

**tau J_Phi_dot+sqrt(3) J_B=0**.

Solve the original full scalar algebraic lapse and shift constraints with P, P_dot, arbitrary psi(tau) and both source coefficients present, then define the Bardeen potentials in the archived scalar gauge:

**Phi_N=Phi+d(a B)/d tau**,

**Psi_N=psi-(a_dot/a) a B**.

Exact symbolic reduction eliminates the arbitrary psi(tau) and psi_dot(tau), and with the source Ward relation gives

**Phi_N = [tau² P_ddot+2 tau P_dot]/[3(1+k²)] +sqrt(3) J_Phi/[2tau(1+k²)] -3 J_B_dot/[2 k²(1+k²)]**,

**Psi_N = [k² P-tau P_dot]/[3(1+k²)] +sqrt(3) J_Phi/[2tau(1+k²)] +3 J_B/[2k² tau(1+k²)]**.

These formulas are exact in the archived **formal source/cos-Fourier normalization**. The sourced scalar equation from v15.713 supplies P_ddot (or equivalently P via v15.714's retarded Green kernel). No source-free frequency fitting or arbitrary gravitational slip has been inserted.

## Gate 331 — the real tidal transfer depends on history, not just the algebraic pole

For a Fourier scalar perturbation with comoving wavevector k zhat, the electric Weyl tensor in a local orthonormal frame is

**E^Weyl_ij = W(tau) [zhat_i zhat_j-delta_ij/3]**,

**W(tau)= [k²/(2 a(tau)²)] [Phi_N(tau)+Psi_N(tau)]**.

Combining the source-first formulas,

**Phi_N+Psi_N = [tau² P_ddot+tau P_dot+k² P]/[3(1+k²)] +sqrt(3)J_Phi/[tau(1+k²)] -3J_B_dot/[2k²(1+k²)] +3J_B/[2k² tau(1+k²)]**.

This is an explicit scalar mode/source-to-gauge-invariant-curvature transfer operator, not merely the location of a dispersion pole. For physically retarded initial conditions, P(tau) is the homogeneous-initial-data term plus the v15.714 retarded convolution with the source; substituting it yields a formal causal scalar-tidal transfer, though the external matter/source and actual instrument remain unselected.

The Weyl norm continues to satisfy

**E^Weyl_ij E^Weyl_ij=(2/3)W(tau)²**,

independent of source amplitude, material eta, k, time and orientation of the scalar Fourier wavevector. This 2/3 is the same **three-space rank-two STF projector norm** rigorously identified at v15.716. It represents a *shape*, not a source-independent Weyl amplitude or a new universal gravitational coupling.

## Gate 332 — exact steady-source reduction and distinction between particular/retarded solutions

Substitute the v15.717 tilted tracefree covariantly conserved source

**J_Phi=sqrt(3)[k² sigma tau+4 rho0]/36**,

**J_B=-k² sigma tau/36**,

and **P_part=sigma/[4 k² beta]**, **beta=1+(8eta-3)(1+k²)/3**. The general formulas reduce exactly to the independent v15.719 results

**Phi_N=sigma/24+rho0/[6tau(1+k²)]**,

**Psi_N=Phi_N-sigma(8eta-3)/[12(3beta)]**.

This is an exact cross-check across the sourced ADM constraints, time-dependent scalar dynamics and Weyl tensor. A retarded, zero-initial-data response need **not** be this steady particular solution: one must add the correct homogeneous terms, which alter the time-dependent measured Weyl amplitude without changing its STF eigenvalue *shape*.

## Gate 333 — novelty and experimental boundary

A genuinely physical, sourced K4 scalar tidal response is now represented by explicit formulas conditional on the formal conserved stress and selected coasting background. The amplitude still depends on **J_Phi, J_B, their derivatives, P initial conditions and eta**. The universal tracefree-shape 2/3 follows from conventional three-dimensional geometry and cannot fix these amplitudes. No unique Cone quarter-shell coupling or experimentally distinguished G-free ratio has been derived.

**Reproducibility:** additive research-notes/k4_scalar_history_weyl_transfer_v15_720.py, commit af7865359607b9c97ee75d5b6e30a9fc92f953e3. Rebuilds the archived scalar quadratic action via additive v15.712, computes arbitrary-history sourced lapse/shift and invariant potentials, verifies residual-gauge cancellation, tracefree Weyl normalization, and reduces exactly to the steady v15.719 source. Independent local symbolic reconstruction also checked the general-history transfer formulas and the reduction. External audit of the newly committed file is requested.

**HANDOFF — external audit/gravity:** independently run the new v15.719 and v15.720 scripts, verify source/cos-Fourier signs and Bardeen gauge invariance, Weyl definition and orthonormal a^-2 scaling; audit the general-history transfer using the original v14.935 EH+solid actions rather than assuming the newer scripts are self-consistent. Preserve the Round 545 distinction: historical scalar_statespace.py **runs** because floating noise masks symbolically invalid 0/0; it is not a literal runtime crash. Audit also v15.716–717 source conservation and Ward mapping not covered by Round 545.

**NEXT:** derive vector and tensor gauge-invariant Weyl/curvature transfer from the same covariantly conserved stress, including source poles/residues and source mode-overlap zeros; compare with conventional isotropic relativistic elasticity. Only after closing this source-to-three-channel response could one claim an independently measurable three-sector ratio or a novel Cone gravity coupling.
