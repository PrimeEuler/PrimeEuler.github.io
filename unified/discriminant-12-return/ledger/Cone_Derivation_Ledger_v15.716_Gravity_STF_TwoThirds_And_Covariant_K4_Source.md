# Cone Derivation Ledger v15.716 — Gravity: why 2/3 reappears, and a tilted covariantly conserved source on coasting FLRW

**Date:** 2026-11-11, US Eastern. **Parents:** v14.592 parabolic-segment 2/3 and distinct integrals; v14.935 K4 background/constraint-reduced SVT; v15.708 unit-dyad source projector sum 2/3; v15.713 sourced scalar compatibility; v15.714 retarded scalar kernel. **Status:** [D] dimension-dependent STF dyad norm and explicit FLRW-conserved tilted Fourier perturbation; [C] physical source/strain normalization and compatibility with a fully sourced Einstein–solid detector calculation; [N] neither a fixed Newton G nor new 2/3 coupling coefficient. **Immediately prewrite live HEAD:** d8c8139e0685f571f91775835a64c0e84f086a9a; v15.716 ledger path absent. Suzuki v15.715 already occupied; all files additive-only; frozen Suzuki/far-tail untouched.

## Gate 318 — exact dimensional origin of 2/3 for a rank-two direction dyad

In d-dimensional Euclidean space, for a unit vector n, take the symmetric tracefree (STF) rank-two dyad

**Q_ij=n_i n_j-delta_ij/d**.

Then, without specifying an orientation,

**Q_ij Q_ij = (n_i n_i)^2 - 2(n_i n_i)/d + d/d² = 1-1/d = (d-1)/d**.

For physical three-dimensional source directions **d=3**, this is exactly **2/3**. It comes from projecting a rank-one dyad away from the one-dimensional trace component, not from a gravitational coupling or two-independent-sector energy ratio. It equals 1/2 in d=2 and 3/4 in d=4: the 2/3 is specifically a three-spatial-dimensional geometry invariant.

The v15.708 tensor/vector/scalar *stress projector* decomposition is orthogonal, so its norm sum is precisely this same invariant:

**norm(Q_T)^2 + norm(Q_V)^2 + norm(Q_S)^2 = norm(Q)^2 =2/3**.

The individual projected norms still depend on source orientation. A separate angular mean **(1/2) integral_(-1)^1 (1-u²) du = 2/3** is another elementary three-dimensional transverse-projection consequence. The Archimedes parabolic-segment area ratio 2/3 and earlier nonorthogonality/drift 2/3 values must NOT be equated with this rank-two STF object without an explicit map between their measures/operators. Reappearance of the rational number is evidence for a useful common *algebraic motif* in some instances, not evidence of universal dynamical equivalence.

## Gate 319 — physically covariant local Fourier stress, not just flat-space conservation

On the exact coasting FLRW background

**ds²=-d tau² + a(tau)² (dx²+dy²+dz²), a=tau/sqrt(3), H=1/tau**,

take a linear externally prescribed Fourier stress perturbation proportional to exp(i k z) with k nonzero. Let n be an arbitrary fixed unit spatial direction and let **Q0_ij=sigma(n_i n_j-delta_ij/3)**. Define the contravariant spatial-stress components

**T^(ij)=Q0_ij/[a² tau²]**.

Define the momentum components and energy density by

**U_i=-i k Q0_zi/(2 tau), T^(0i)=U_i/a²**,

**T^(00)=rho=-3 k² Q0_zz/(2 tau²) + rho0/tau³**.

Here sigma and rho0 are freely prescribed source coefficients. They are **not** derived by varying a new material source action and no positive-energy/physical-localization claim is made.

Directly calculating the Christoffel symbols of the coasting FLRW metric and the Fourier covariant divergence gives

**nabla_mu T^(mu nu)=0 for all nu=0,1,2,3**,

exactly, for any fixed unit n. The nontrivial equations are equivalent to

**U_i' +3H U_i + i k Q0_zi/tau²=0**,

**rho' +3H rho + i k U_z/a²=0**,

where Q0/tau² is the comoving orthonormal spatial stress. A subtle scale-factor placement matters in the rho equation; an initial trial omitted 1/a² in the spatial momentum divergence and failed a direct covariant check. The corrected full Christoffel calculation passes, including the energy equation. This error was caught and fixed before any ledger claim.

## Gate 320 — a single tilted source has all three stress helicity projections, yet a free amplitude

Choose a concrete nonaxisymmetric normalized direction

**n=(sqrt(1/2),sqrt(1/3),sqrt(1/6))**.

Then all three SO(2)-about-z traceless spatial stress projections are nonzero: a transverse-traceless tensor part, transverse vector shear, and scalar anisotropic part. In this example **Q0_zz=-sigma/6**, **rho=k² sigma/(4 tau²)+rho0/tau³**, and **T^(0z)=i k sigma/(4 tau³)**.

The source norm is still exactly

**tr(Q(tau)²)=2 sigma²/(3 tau⁴)**,

independent of orientation, and all four covariant stress-conservation equations hold. Thus a single **covariantly conserved perturbative Fourier stress** can provide nonzero geometric overlaps in T,V,S simultaneously. But sigma remains undetermined, and solving the K4 *inhomogeneous coupled metric and solid field equations* is still required to identify the mode residues. Covariant conservation is a necessary source condition, not proof of source realizability by positive-energy, localized matter or the full K4 background constraints.

## Gate 321 — relationship to the original experimental objective

**Positive exact results:** (a) 2/3 is a kinematic universal STF norm for three-space; (b) the same number in v15.708 is now explained algebraically; (c) the previously purely flat-source completion has an explicit **coasting-FLRW covariantly conserved** extension with nonzero generic T/V/S stress projections.

**Still open:** an independently motivated matter action that realizes the conserved perturbation, its correct ADM stress-source coefficients for the v14.935 cos-Fourier convention, and a gauge-invariant detector tidal response. None of these follows from the 2/3 norm, and it is not a gravitational 2/3 coupling prediction. The other 2/3 appearances—including Archimedes' parabolic quadrature—remain separate mathematical facts until a derivable intertwiner connects them.

**Reproducers:** research-notes/cone_stf_two_thirds_v15_716.py, commit 8e4c305ce0742f20d2200715edab01f278698ec6; research-notes/k4_covariant_stf_flrw_source_v15_716.py, commit d8c8139e0685f571f91775835a64c0e84f086a9a. Both executed locally to PASS; source checked by constructing all metric Christoffel components and all four independent divergences. No image generation.

**HANDOFF:** external audit/gravity/sandbox: independently verify the full FLRW covariant source divergence with the factors of a, the orientation-independent dyad norm, the choice of Fourier complex source coefficient, and the distinction between a conserved source template versus a matter action. Validate that none of the 2/3 correspondences is promoted to an unexplained physics constant.

**NEXT:** check whether the v15.713 scalar auxiliary compatibility condition tau J_Phi' + sqrt(3) J_B=0 can be obtained from the **same** covariant FLRW energy Ward identity for a correctly specified source map. Check relative Fourier phase and ADM shift conventions explicitly. A matching Ward identity would be a real bridge between the source-free and source-first sectors, but must not be confused with a physically fixed detector coupling.
