# Cone Derivation Ledger v15.724 — Gravity: compact-duration covariantly conserved pulse drives all three electric-Weyl channels

**Date:** 2026-11-11, US Eastern. **Parents:** v14.928 EH+K4 tensor action, v14.935 constrained K4 SVT action, v15.713–714 sourced scalar retarded Euler equation, v15.716–717 coasting FLRW conserved stress and scalar Ward, v15.720 source-history scalar Weyl, v15.721–722 source-conditioned vector/tensor Weyl and retarded transients. **Audit:** Round 546/v15.723 independently confirmed v15.716–717 and v15.719–721; v15.722 pending. **Status:** [D] compact-in-time conserved FLRW stress template and exact common three-sector time-envelope, [D] finite-support numerical pulse leaves nonzero T/V/S electric-Weyl tails, [N] no universal residue ratio, [O] localized positive-energy matter source and calibrated readout. **Immediately prewrite HEAD:** 33ea6985cba5bc7c533a89c0cb5fdcc58e11d4e7; target v15.724 ledger path absent. Additive-only; Suzuki/far-tail untouched.

## Gate 342 — whole stress-energy, not just anisotropic stress, must end with the pulse

On **ds²=-dτ²+a(τ)² δ_ij dx^idx^j**, **a=τ/√3**, Fourier phase e^(ikz), take any *constant spatial traceless symmetric tensor* Q_ij and a smooth compactly supported scalar b(τ)∈C_c^∞((τ0,τ1)). Define a prescribed perturbative contravariant source

**T^(ij)= Q_ij b''(τ)/(a² τ²)**,

**T^(0i)=T^(i0)= -ik Q_zi [τ b'(τ)-b(τ)]/(a² τ³)**,

**T^(00)= -3k² Q_zz b(τ)/τ⁴**.

Because the source uses only b, b', b'', **every component vanishes identically both before τ0 and after τ1**. By explicit background-Christoffel calculation,

**∇_μ T^(μν)=0, ν=0,1,2,3**,

provided **tr(Q)=0**. An initial independent symbolic test with unconstrained Q exposed a residual energy divergence tr(Q) b''/τ³, which disappears exactly when the intended tracefree condition is imposed. This is a legitimate constraint, not evidence of a new physical 2/3 coupling.

The source is smooth and compact in *time*, but it remains a plane Fourier mode throughout space, not a spatially localized positive-energy matter system. A real source uses e^(ikz) and e^(-ikz) conjugate modes. The stress is prescribed as a conserved perturbation; a standalone microscopic material action has not been derived.

## Gate 343 — the three physical K4 dynamical sectors see exactly the same pulse envelope

Introduce **J_Φ=a³T^(00)** and **J_B=ik a⁴T^(0z)** in the archived scalar ADM Fourier conventions. The exact source Ward identity from v15.713–717,

**τ J_Φ' +√3 J_B=0**,

follows from the above four-dimensional conservation. Substitution into the directly derived physical scalar P equation gives

**P''+3P'/τ+β_S P/τ² = c_S b''(τ)/τ²**,

**β_S=[8η(1+k²)-3k²]/3**, **c_S=-3Q_zz/(2k²)**.

Using the *original sourced vector shift constraint* and solid transverse displacement (v15.710 and 721) gives

**f''+3f'/τ+β_V f/τ² = c_V b''(τ)/τ²**,

**β_V=2η(4+3k²)/3**, **c_V=-2i Q_zy/k**.

The EH+solid tensor equation gives for a fixed TT plus/cross polarization

**γ''+3γ'/τ+β_T γ/τ² = c_T b''(τ)/τ²**,

**β_T=3k²+8η/3**, **c_T=-2κ Q_T**.

The same physical Fourier source now enters all three reduced wave equations, with **exactly the same temporal profile b''/τ²** and sector-dependent *known* angular/source factors and propagator coefficients. The common-pulse identity is stronger than matching arbitrary unrelated source strengths. It does not make the measured amplitudes equal: Q_zz, Q_zy and Q_T depend on orientation and may vanish independently.

## Gate 344 — exact post-pulse response is a frequency-filtered logarithmic convolution

For any one of the three modes X∈{S,V,T}, on η>3/8 and k>0, write

**ν_X²=β_X-1>0**,

and for zero dynamical initial data use the exact retarded Green kernel already certified in scalar form at v15.714 and extended to V/T at v15.722:

**G_X(τ,s)= [s²/(ν_X τ)] sin[ν_X ln(τ/s)]**, τ>s.

Then, for τ>τ1 after every source component has vanished,

**X(τ)= c_X/(ν_X τ) ∫_(τ0)^(τ1) b''(s) sin[ν_X ln(τ/s)] ds**.

This is a strictly causal *free afterglow*: the external stress is zero, while the sourced fields can remain nonzero. Curvature must be reconstructed separately: scalar electric Weyl from the v15.720 Bardeen transfer, vector electric Weyl from the time derivative of the constrained shift, tensor electric Weyl from the TT wave's temporal/spatial derivatives. This is linear field theory on the prescribed coasting FLRW background, not an observable forecast in our universe.

## Gate 345 — one finite-support example excites all three electric Weyl components after the pulse ends

For the generic tilted unit direction used at v15.716, take Q_ij=n_i n_j-δ_ij/3 with n=(√(1/2),√(1/3),√(1/6)); then **Q_zz=-1/6**, **Q_zy=√(1/18)**, **Q_T,plus=(Q_xx-Q_yy)/2=1/12**. Choose an illustrative compactly supported, piecewise-polynomial **C⁵** pulse

**b(τ)=(τ-1)^6(2-τ)^6** for 1<τ<2 and b=0 outside,

with **η=3/4, k=2, κ=1**, and read out at **τ=3**. The pulse is finitely differentiable; the exact construction above admits arbitrarily smooth C_c^∞ envelopes as well.

Independent numerical quadrature of the exact retarded kernels and the source-free metric-to-Weyl transfer yields the three **electric** curvature amplitudes in the stated coordinate/normalization conventions:

**W_S(3)≈+1.4626834392×10^-7** (scalar STF amplitude),

**E^(Weyl,V)_yz(3)≈-7.1024748076×10^-7** (vector shear electric component),

**E^(Weyl,T)_xx(3)≈-2.7353968368×10^-6** (tensor plus electric component).

All three are nonzero at τ=3, where **T^(μν)=0 identically**. This supersedes the earlier idealized step-source *for the purpose of demonstrating the existence of simultaneous electric afterglows*, but it still does not select a physical localized emitter or detector. Their ratios are not expected to be invariant under changes in source orientation, pulse shape, eta, k, or readout time.

## Gate 346 — conclusions and next falsification criterion

**Positive:** one smooth-ended, exactly covariantly conserved coasting FLRW Fourier stress is sufficient to generate nonzero scalar/vector/tensor *electric Weyl* signals after it has ended. The formerly static vector electric null is not an obstacle to general transient excitation. The source Ward identity is satisfied automatically; no spurious surface impulse is required for the polynomial witness.

**Negative:** the response strengths and pulse-selected spectral weights vary. There is no parameter-free triple electric-amplitude ratio, and the v15.706 pole-gap relation 3 remains conventional coasting relativistic elasticity. The tracefree Q source norm tr(Q²)=2/3 for unit dyad is an angular geometric identity, not the dynamic response coefficient.

**Reproducibility:** research-notes/k4_compact_conserved_three_sector_pulse_v15_724.py, additive commit 33ea6985cba5bc7c533a89c0cb5fdcc58e11d4e7. Checks FLRW Christoffel covariant divergences (all four), source Ward identity, exact S/V forced coefficients, and numerical post-pulse T/V/S electric Weyl response from common retarded kernels. The independent local algebra/numeric reproductions passed. No imagegen, no certified object edits.

**HANDOFF:** external audit/gravity/sandbox: verify the four conserved-source components with tr(Q)=0, absence of post-pulse density/momentum tails, all S/V/T force coefficients against archived K4 action, the retarded Weyl transfer and finite-regularity/numeric witness; note that a plane Fourier mode is **not a spatially localized material source**.

**NEXT:** probe a potentially sharp obstruction to the three-pole observable: pulse-shape spectral zeros. Determine whether a nontrivial, covariantly conserved, common-stress compact pulse can cancel one sector's *post-pulse* mode while leaving the others, even when all Q projectors are nonzero. If yes, three dispersion poles do not guarantee three observed peaks for arbitrary source histories.
