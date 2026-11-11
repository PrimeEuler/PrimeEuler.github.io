# Cone Derivation Ledger v15.727 — Gravity: positive-local-energy canonical scalar source with localized Cauchy data, and a new traceful-stress obstruction

**Date:** 2026-11-11 US Eastern. **Parents:** v14.928/935 frozen K4 EH+three-solid action, v15.716–717 conserved *prescribed tracefree* Fourier stress, v15.719–722 conditional Weyl transfer, v15.724–725 compact-duration signed common source and spectral notches. **Version collision:** Suzuki v15.726 was present at live HEAD; therefore the next gravity version is v15.727. **Result types:** [D] independently specified conventional canonical matter Lagrangian, background conservation, local positive energy density, finite propagation of compact Cauchy data, STF 2/3 gradient stress, explicit nonparallel-wave S/V/T projector witness; [N] old tracefree-only Ward mapping does not apply directly; [O] complete pressure-corrected sourced K4 ADM constraints, localized matter-to-detector Weyl transfer, nonlinear backreaction.

## Gate 351 — matter source from an actual action rather than a freely prescribed stress

Append a *spectator*, minimally coupled real massless scalar field with conventional action, in (-+++) metric convention:

**S_chi=-(1/2)∫d⁴x sqrt(-g) g^(mu nu) partial_mu chi partial_nu chi**.

On the exact coasting FLRW background **a(tau)=tau/sqrt(3)**, zero background chi and a small perturbation chi=epsilon chi_1, its order-epsilon² stress is

**T^(mu nu)=partial^mu chi partial^nu chi - (1/2)g^(mu nu)partial_alpha chi partial^alpha chi**,

and its covariant conservation is the exact off-shell identity

**nabla_mu T^(mu nu)=(nabla^nu chi) Box chi**.

The wave equation **Box chi=0** is

**chi_ddot+3H chi_dot -a^-2 Delta chi=0**, H=1/tau.

The local comoving-frame matter energy density satisfies

**rho_chi=(1/2)[chi_dot²+|grad chi|²/a²]>=0**.

This is a legitimate positive local energy density for a canonical massless scalar, unlike the freely signed stress history of v15.724–725. However the stress is **quadratic** in the scalar field, so its leading source to the K4 metric/solid equations is order epsilon², not a first-order stress perturbation in chi. At this order the fixed coasting background and free scalar evolution are consistent as a perturbative source; a fully sourced Einstein–solid solution is not claimed.

## Gate 352 — spatial compactness and why global compact-time matter pulses were an idealization

Choose smooth compactly supported initial data chi(tau0,x) and chi_dot(tau0,x). The scalar wave equation is hyperbolic with finite physical propagation; its radial comoving causal radius obeys **Delta r <= ∫_(tau0)^tau ds/a(s)=sqrt(3) log(tau/tau0)**. Therefore the scalar and its stress remain supported inside a finite, growing comoving spatial region at every finite time.

For example, a smooth radially compact initial bump may use **chi(tau0,r)=epsilon exp[-1/(1-r²/R²)] for r<R, and zero for r>=R**, with chi_dot(tau0,r)=0. A nonradial superposition or spatially displaced bumps can break spherical symmetry when necessary to excite vector/tensor source overlaps.

Unlike a *prescribed signed source*, the nontrivial source cannot be zero everywhere after some finite later time and still solve the same free source equation: if T00=0 at the whole final Cauchy slice, the positivity identity implies chi_dot=0 and grad chi=0 there. Compact support then implies chi=0 on that slice; uniqueness of the linear scalar Cauchy problem forces the original solution to have been trivial. This does **not** prohibit a finite local stress pulse at an individual detector as the wave passes; it prohibits the earlier modeling assumption that a nontrivial freely propagating positive-energy field vanishes *globally* after a finite time.

## Gate 353 — the rank-two 2/3 appears in actual scalar-field anisotropic stress

On any spatial slice, remove the spatial trace of the canonical scalar stress. Its anisotropic part in an orthonormal spatial frame is

**Pi_ij=grad_i chi grad_j chi - (1/3)delta_ij |grad chi|²**.

Thus **Pi_ij Pi_ij=(2/3)|grad chi|⁴**. This is the exact same three-dimensional STF dyad invariant identified at v15.716, now sourced by a standard physical matter Lagrangian, with NO newly chosen 2/3 coefficient. The scalar gradient's size and direction remain field-dependent; the 2/3 does not fix a gravitational coupling or any tidal response amplitude.

Crucially the scalar's full spatial stress has a generally **nonzero isotropic trace**:

**a² delta_ij T^(ij)=(3 chi_dot²-|grad chi|²/a²)/2**.

The tracefree stress template used in v15.716–725 had spatial trace zero by construction. That simplification removed a direct scalar-spatial-metric source term and yielded the special Ward relation tau J_Phi_dot+sqrt(3) J_B=0 in v15.713/717. For this canonical matter action, a pressure/trace source is generally present and cannot be discarded. The old tracefree-source Ward, P forcing, or three-channel transfer must **not** simply be reused with the canonical scalar substituted. The correct sourced scalar ADM variation needs its direct spatial trace coupling and the full energy-momentum conservation identity.

## Gate 354 — can one canonical scalar actually project into all three SVT sectors?

At a fixed point, a single gradient is a dyad with a 2/3 STF norm, but this does not guarantee nonzero global Fourier projections of all three sectors. Spherical symmetry would force the vector and tensor source Fourier projections to vanish despite nonzero local anisotropic stress.

There is nonetheless an explicit conventional-scalar *kinematic possibility*: consider two nonparallel scalar Fourier components with spatial wavevectors **p=(2,0,0)** and **q=(0,0,1)**. Their quadratic gradient cross-stress contains a mode at **K=p+q=(2,0,1)** proportional to the symmetric dyad **S=p q^T+q p^T** (plus an isotropic trace term). Exact transverse/longitudinal STF decomposition about K gives the nonzero squared Frobenius norms

**norm(S_T)²=32/25; norm(S_V)²=72/25; norm(S_S)²=96/25**,

with their sum equal to norm(S_STF)²=8. Thus a canonical scalar source can kinematically have nonzero T, V and S stress overlaps at a common wavevector when its spatial structure is sufficiently asymmetric. The two monochromatic Fourier waves are an algebraic projector control; physically compact initial data instead use wavepackets that can contain such components. A fully normalized sourced detector response has not been computed.

## Gate 355 — honest current scope and next gate

**Positive:** action-level ordinary matter, explicit positive local energy, an exact source conservation identity, finite propagation from smooth spatially compact data, pointwise STF 2/3, and a nonzero all-sector Fourier cross-stress control. **Negative / important new obstruction:** a nontrivial positive-energy free scalar cannot give the globally compact-in-time signed source used for the exact notch gate, and its pressure violates that gate's tracefree-only assumption. Therefore v15.724/725 remain valid mathematical source-template controls but cannot yet be claimed as physically prepared canonical-scalar pulses.

**Reproducer:** research-notes/k4_canonical_scalar_localized_source_v15_727.py, additive commit a285a1fa414090843369e52efb995d10715acf0c. Locally independently checked sympy covariant divergence with the exact FLRW Christoffels, positivity formula, tracefree norm, complete cross-wave SVT projections, log-time scalar wave reduction. Existing frozen Suzuki/certified assets left untouched.

**HANDOFF:** audit the source action/stress convention (-+++) versus archived K4 (+---), the 4-divergence and the quadratic source order, the spatially localized hyperbolic finite propagation argument and zero-everywhere-afterwards uniqueness no-go, and the traceful-pressure obstruction to v15.717. Do not promote local Pi norm 2/3 to a new gravity constant.

**NEXT:** derive the **pressure-corrected scalar Ward identity** and include the direct scalar-spatial-metric source term in the original v14.935 unreduced ADM EH+solid action. Only thereafter insert explicit scalar wavepacket stress into a genuine K4 gauge-invariant curvature calculation, comparing with standard relativistic elasticity.
