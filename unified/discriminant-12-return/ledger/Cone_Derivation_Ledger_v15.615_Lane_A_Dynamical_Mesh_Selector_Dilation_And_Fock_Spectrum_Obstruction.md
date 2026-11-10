# Cone Derivation Ledger v15.615 — Lane A: testing fixed transition length / physical cutoff against native dynamics

**Date:** 2026-11-10. **Parents:** Paper C Quantum Realizations v1.1, v15.469 acceleration/parabola action, v15.600 quadratic and harmonic null-boundary obstruction, v14.767 factor-unit covariance, v15.602 all-q refined ladders, v15.609 co-scaled boundary functional, v15.611 fixed-step boundary functional, v15.613 fixed-physical-product staircase asymptotic, v15.614 normalized selector-negative. **Status:** [D] exact dilation covariance and integer-spectrum obstruction; [O] absolute physical mesh/cutoff selector. **Prewrite live HEAD:** 88daf3b34ed253d41af2ce076823092e28ab5c44; v15.615 collision search negative. Additive-only; Suzuki frozen/production untouched.

## Gate 91 — native dynamic conserved quantities do not fix an absolute geometric step

Paper C's canonical dictionary is x=n1+1,y=n2, with n_i nonnegative integer occupation operators. Its fixed-T Schwinger SU(2) J± change the two occupancies by ±1 while preserving N=n1+n2. Its two-mode SU(1,1) K± change both occupations by ±1 while preserving D=n1−n2. Its generic elliptic generator preserves total-number parity, and the product-fixed quantum generator has only a scoped Gaussian obstruction. None of these *specified* algebraic conservation statements contains a numerical equation selecting an absolute physical factor length s or u, or a fixed dimensional product X; they are statements in occupation-number units. The constant-force action/parabola quadrature v15.469 has exact 2/3 for arbitrary input focal parameter u and imported acceleration/force, hence also does not select u by itself.

This is a scoped audit of the presently defined sources, not a no-go theorem for arbitrary Hamiltonians or GR.

## Gate 92 — exact coordinate dilation test

Write P_u(Y)=Y²/(2u)+u/2 for the canonical parabolic family. For λ>0, P_{λu}(λY)=λ P_u(Y). On the positive factor plane, the unitary L²-coordinate dilation (for flat factor measure) (U_λ f)(x,y)=λ^(−1) f(x/λ,y/λ) conjugates an original coordinate-shift operator by s to a shift by λs, i.e. U_λ T_s U_λ†=T_{λs} (fix sign convention of T_s as translation by +s). The formal continuum original-step Casimir boundary profile

E_s(x,y)=[y(x+s)1_(y<s)+x(y+s)1_(x<s)]/2

obeys E_{λs}(λx,λy)=λ² E_s(x,y). The cone's circle-pushforward Jacobian J_F=(x+y)/(4√(xy)) is degree-zero homogeneous. On correspondingly transformed domains, ∫E_{λs} J_F dxdy=λ⁴∫E_s J_F dxdy. Therefore a **postulated physical dilation equivalence** with the same form of the dynamics requires the transition step to co-scale with the mesh unit (r=s/u invariant). Retaining physical s=1 while refining u is *not* a mere coordinate-dilation conjugate of the original system; it changes the invariant dimensionless ratio r and thereby the complement response in v15.611–614.

This implication is **conditional** on a physical dilation symmetry, not a derivation of the symmetry or a physical preference for s=u. A separately sourced physical constant could fix s and break scale covariance.

## Gate 93 — native Fock discreteness prevents continuous unitary identification

On the same ordinary two-mode Fock Hilbert space, N=n1+n2 has spectrum {0,1,2,...}. If U N U†=cN for positive c, unitary conjugation demands spectrum(N)=spectrum(cN). Their smallest strictly positive eigenvalues are respectively 1 and c, hence c=1. Thus for c≠1 there is **no unitary internal rescaling of the native number operator** that treats occupation 1 as occupation c. Likewise the Paper C dictionary x=n1+1,y=n2 does not carry arbitrary continuous geometric dilation to occupation vertices, because a generic λ changes the shifted integer lattice itself. An abstract coordinate rescaling of classical factor variables is not automatically an inner Fock symmetry. This is fully compatible with separate physical calibration/embedding across sectors; it does *not* show EM and gravity are experimentally inequivalent.

## Verdict and independent test

Neither a unique transition length nor a physical product cutoff is fixed by the established Hamiltonian/charge structures examined. We have identified a **conditional physical selection fork**: demand dilation equivalence and co-scale s; or supply an independent dimensionful dynamical input selecting fixed s, and then the positive complement A-region response is an actual model distinction. The cut-off X in v15.613–614 is still externally chosen, so R_q(X) at finite q remains X-dependent and cannot alone select q=2 or G.

Independent SymPy checks cover E homogeneity, parabolic covariance, spectral scale dimensional expression, fixed/co-scaled threshold witness, and action E^(3/2) scaling. Reproducer and report in the conversation's verified `cone_selector_gates_91_93.zip`. No physical prediction, G, α, photon or chirality inferred.

**Next gate:** identify a physically imposed frequency/energy gap, action quantization or independently operationally defined cutoff that determines r=s/u or X without input measured G; then compare resulting dimensionless observables to EM and gravity. Any matching of kinematic geometries without sourced dynamics remains an analogy.

**HANDOFF:** target external-audit, gravity, sandbox; status open; type dynamical fixed-step selector versus dilation covariance/Fock spectrum. Check the dilation conjugation convention, no-go scope (same Fock Hilbert space only), and difference between exact occupation-number ladder unit and a measurable physical transition length. Preserve all prior ledger and certified Suzuki artifacts.