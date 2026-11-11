# Cone Derivation Ledger v15.708 — Gravity: one conserved Fourier stress excites generic SVT projectors, without fixed mode-amplitude ratio

**Date:** 2026-11-11, US Eastern. **Parents:** v14.928 Einstein–Hilbert+K4 elastic-solid tensor; v14.935 full reduced, source-free SVT stability dispersions; v15.703 rank-two GR tide; v15.705 tensor-only shape; v15.706 eta-independent same-k squared-frequency-gap ratio 3 and conventional relativistic-elasticity comparator. **Audit:** Round 544/v15.707 independently confirmed v15.701–706 without new defects. **Prewrite HEAD:** 9ba3096ce9a0fba1848795cd2f3f6b01e01ed809; v15.708 ledger target absent, version free; additive only, frozen Suzuki/far-tail work untouched. **Classification:** [D] exact algebraic common conserved Fourier stress, orthogonal tensor/vector/scalar stress projectors and local gauge-invariant linear source coupling; [C] physical realizability and coupling to dynamical K4 modes; [N] source projection does not determine scalar/vector metric transfer or a detector observable.

## Gate 289 — construct a single conserved common source

Use local inertial Fourier coordinates (t,x,y,z), metric perturbations of frequency omega and wave number k along z with convention exp(-i omega t+i k z), omega nonzero. Let the symmetric spatial stress amplitude be **S_ij=n_i n_j**, with **n=(x,y,z)** a normalized Euclidean direction (x²+y²+z²=1). Overall dimensional stress amplitude may be restored as a free factor A and does not enter the normalized source projectors.

Define the four-dimensional symmetric Fourier source T^(mu nu) by retaining spatial T^(ij)=S_ij and imposing

**T^(0j)=(k/omega)S_(zj), T^(00)=(k/omega)² S_zz**.

Then exactly **q_mu T^(mu nu)=0**, with **q_mu=(-omega,0,0,k)**. This is a single symmetric conserved Fourier stress amplitude, not three independently prescribed sources. It is a **local algebraic conserved-source construction**. Conservation alone does not show a positive-energy, localized or microscopically realizable medium, nor the correct covariant background conservation on exact K4 FLRW. These requirements remain open and are not smuggled into the result.

## Gate 290 — exact orthogonal SO(2)-about-k stress projectors

Remove the spatial trace, **Q_ij=S_ij-delta_ij/3**, then split into transverse traceless tensor, vector shear and scalar longitudinal anisotropic components. In the z propagation frame,

**Q_T = [[(x²-y²)/2,xy,0],[xy,-(x²-y²)/2,0],[0,0,0]]**;

**Q_V = [[0,0,xz],[0,0,yz],[xz,yz,0]]**;

**Q_S = diag((1-3z²)/6,(1-3z²)/6,(3z²-1)/3)**.

They are mutually orthogonal in the matrix Frobenius trace inner product, and **Q=Q_T+Q_V+Q_S**. Their squared norms, for |n|=1, are

**N_T=(1-z²)²/2**, **N_V=2z²(1-z²)**, **N_S=(1-3z²)²/6**,

with exact **N_T+N_V+N_S=2/3**.

Generically all three are nonzero in this *stress projector* decomposition. But they have orientation-dependent strengths: for z=0 the vector stress projection vanishes; for z=±1 both tensor and vector projections vanish; at z²=1/3 the tracefree scalar anisotropic stress projection vanishes. The last statement **does not** imply that the physical K4 scalar mode is unexcited, because the density, momentum and trace sources and scalar constraint mixings have not been eliminated. Do not conflate a scalar-anisotropy projection zero with the complete scalar-mode Green-function overlap.

## Gate 291 — local gauge invariance and physical incompleteness of the common-source ansatz

The usual linear metric source term **S_int=(1/2) integral h_(mu nu) T^(mu nu)** is gauge invariant modulo boundary conditions under a linearized diffeomorphism **delta h_(mu nu)=partial_mu xi_nu+partial_nu xi_mu** when **partial_mu T^(mu nu)=0**. With Fourier q=(-omega,0,0,k), direct symbolic contraction proves **(q_mu xi_nu+q_nu xi_mu)T^(mu nu)=0**. The universal metric source coefficient is standard GR; the special Cone quarter grid does not add a new sourced coupling.

This verification does **not** derive the real K4 source-to-mode functional. A physical common source on the coasting solid background must solve covariant background conservation and the coupled scalar/vector gravitational and solid perturbation constraints. The archived v14.935 eigenfrequencies were derived for the homogeneous linear system, not this externally sourced perturbation; hence we cannot assign physical oscillator amplitudes to scalar/vector/tensor modes merely from their dispersion relations.

## Gate 292 — the eta-free pole relation is distinct from unequal source residues

The v15.706 identity

**(omega_T²-omega_V²)/(omega_V²-omega_S²)=3**

for same nonzero physical k and 3/8<eta<3/2 concerns the *homogeneous squared-frequency pole locations*. A common source may overlap all three eigenvectors but source projections differ by the angle of n. Even if all three pole locations were identifiable in a real readout, one cannot infer a universal amplitude ratio or a guaranteed three-pole observed signal. At source orientations with vanishing relevant overlap, individual poles could be invisible; at finite damping, frequency peak positions also differ from undamped mode frequencies. Any proposed experimental ratio must use the actual on-shell and detector response and distinguish these effects.

**Verdict:** Positive conventional kinematic common-source construction and exact tensor/vector/scalar stress decomposition; negative against automatic universal response amplitudes and against identifying the ratio 3 with a three-channel gravitational observable. It provides a concrete input that can be passed into a *new* K4 inhomogeneous SVT constraint calculation, rather than inventing three separate source amplitudes.

**Reproducibility:** research-notes/k4_common_conserved_source_svt_v15_708.py, additive commit 43828acc87b4639105d05d9635d13c31dfbbbb52, and research-notes/k4_linear_source_gauge_check_v15_708.py, additive commit 9ba3096ce9a0fba1848795cd2f3f6b01e01ed809. Both locally executed PASS. Exact symbolic projector identities, conservation, gauge variation, orientation zeros; no figures generated.

**HANDOFF:** external audit and K4/SVT sandbox: independently reproduce Frobenius projector norms and the Fourier 4-stress conservation, especially the scalar-anisotropy-versus-full-scalar-source distinction. The next physical calculation would add this source to the **original frozen v14.935 action**, eliminate sourced lapse/shift, and compute gauge-invariant scalar/vector/tensor Riemann-electric detector response with explicit source stress and any required background perturbations. Confirm that the external stress is covariantly conserved on the chosen FLRW background; do not assume local Minkowski conservation is enough.

**NEXT:** first derive source-independent local *gauge-invariant tidal response tensors* for scalar and vector metric perturbations, and show what undetermined gravitational potentials enter; then assess if the v14.935 source-free return fixes the sourced potential ratios. Do not fabricate a unique sourced signal if it does not.
