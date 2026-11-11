# Cone Derivation Ledger v15.725 — Gravity: exact Mellin pulse notch removes a selected K4 post-pulse Weyl channel

**Date:** 2026-11-11, US Eastern. **Parents:** v14.935 K4 coupled homogeneous SVT, v15.706 conventional-elasticity squared-frequency gap ratio 3; v15.713–714 scalar sourced Euler/retarded Green; v15.719–722 electric/magnetic Weyl transfers; v15.724 finite-duration conserved tracefree common pulse with all three nonzero electric Weyl afterglows. **Audit:** Round 546/v15.723 independently confirmed v15.716–717 and v15.719–721; v15.722 and v15.724 awaiting audit. **Classification:** [D] exact compact-envelope differential-operator spectral notch theorem; [D] nonzero T/V Weyl with absent postpulse scalar for an explicit witness; [N] a universal three-mode detector peak claim, source-independent amplitude ratio, novel Cone gravity constant; [O] positive-energy localized stress/matter realization. **Immediately prewrite live HEAD:** 3b0d60a23dd40a212b9728384f2ffd93ffbb1389. Target ledger path absent, no version collision. Additive-only; all frozen Suzuki/far-tail and historical audit objects untouched.

## Gate 347 — postpulse mode amplitude is a logarithmic Mellin coefficient

The exact coasting K4 common compact-source construction from v15.724 gives, separately for X∈{scalar,vector,tensor},

**X''+3X'/τ+[1+ν_X²]X/τ² = c_X b''(τ)/τ²**,

where b∈C_c^∞((τ0,τ1)), the c_X are source-orientation/coupling factors defined in v15.724, and ν_X>0 in the stable nondegenerate parameter range. For τ>τ1 the exact retarded solution is

**X(τ)=c_X/(ν_X τ) Im[exp(iν_X log τ) I_b(ν_X)]**,

**I_b(ν)=∫_(τ0)^(τ1) b''(s) s^(-iν) ds**.

Therefore the *full postpulse solution* for mode X, including all time derivatives and corresponding free metric electric-Weyl curvature, vanishes if I_b(ν_X)=0. Nonzero spatial source projector c_X alone cannot guarantee nonzero postpulse mode excitation. By two integrations by parts, with all compact-support boundary terms zero,

**I_b(ν)=(-iν)(-iν-1) ∫ b(s) s^(-2-iν) ds**.

This is a Mellin/Fourier transform in logarithmic cosmological time, not evidence of an extra universal oscillator frequency.

## Gate 348 — exact real compact pulse shaping cancels a chosen eigenfrequency

Let **D=s d/ds** and let b0(s) be *any real, nonzero smooth compactly supported* base pulse. For a selected real target frequency ν_* define

**b_*(s)=[D²-2D+(1+ν_*²)]b0(s)**.

This remains real and compactly supported, with the same support as b0 (up to possible interior zeros). Integration by parts gives, for M_b(ν)=∫b(s)s^(-2-iν)ds,

**M_(Db)(ν)=(1+iν)M_b(ν)**,

so

**M_(b_*)(ν)=[(1+iν)²-2(1+iν)+1+ν_*²]M_b0(ν)
           =(ν_*²-ν²) M_b0(ν)**.

Consequently **I_(b_*)(±ν_*)=0 exactly** and the postpulse response of a targeted K4 mode with ν_X=ν_* is identically zero, although the common source remains covariantly conserved and generally has nonzero source projections into all three SO(2) sectors.

The temporal notch uses a *tuned signed stress history*. It is mathematically permitted by the prescribed conserved-source template, but no claim is made that a particular ordinary positive-energy localized material emitter can realize it. The source is Fourier-periodic in space and has no specified independent matter action.

## Gate 349 — explicit one-sector-dark, two-sectors-bright witness

Use **η=3/4, k=2, κ=1**, the same generic tilted STF spatial dyad n=(√(1/2),√(1/3),√(1/6)) from v15.716, and retain the real source as conjugate Fourier modes. Then

**ν_S=√5, ν_V=√7, ν_T=√13**.

Take the illustrative finite-regularity base bump **b0(s)=10000(s-1)^8(2-s)^8** for 1<s<2, zero outside (globally C⁷); define **b_*=(D²-2D+6)b0** (globally C⁵). Its exact polynomial on the interior is

**b_*(s)=20000(s-2)^6(s-1)^6(115s⁴-342s³+255s²-12s+12)**.

The algebra above guarantees **I_b(√5)=0 exactly**, not merely numerically. Quadrature of the committed witness independently gives a scalar Mellin amplitude ~3.6×10^-12 (floating residual), while the vector and tensor Mellin amplitudes are approximately **0.3029724** and **2.1450987**.

At τ=3 (after all source components have vanished), the source-conditioned electric Weyl components are

**W_S(3)≈ -1.2×10^-15** (numerical zero),

**E^(Weyl,V)_yz(3)≈ +7.8736412×10^-4**,

**E^(Weyl,T)_xx(3)≈ +1.2371151×10^-2**,

in the same K4 source/metric conventions as v15.724. These contrast with the unshaped generic finite pulse in v15.724, which gave three nonzero electric components. The difference is *only* the source time profile: the same geometry, same k, same η and same source direction are retained.

## Gate 350 — new exact observation-selection obstruction, not a new gravity constant

The response can be suppressed in one chosen channel by the common source's temporal Mellin zero, while other channels retain nonzero curvature. This is an exact **source-spectral selection effect** separate from the known orientation projection zeros: source direction Q and pulse history b are *two independent factors* in physical excitation. Therefore the exact homogeneous three-sector frequency-gap ratio 3 of v15.706 cannot be asserted to produce three observed spectral lines for arbitrary conserved source preparations.

This is **not a no-go theorem for detecting K4 modes**: a sufficiently broadband and properly controlled physical source, and an appropriate combination of electric/magnetic detectors, might excite and reveal all three. Conversely, a missing spectral peak is not by itself evidence that a mode does not exist. The relation 3 is already an isotropic relativistic elasticity identity and is not uniquely Cone.

The earlier recurring **2/3** remains the spatial STF dyad norm **tr(Q²)=2/3** for a unit dyad, independent of pulse history; it does not protect any mode from being spectrally dark or fix the source-to-detector amplitude.

**Reproducibility:** research-notes/k4_compact_pulse_mellin_notch_v15_725.py, additive commit 3b0d60a23dd40a212b9728384f2ffd93ffbb1389. Locally tested PASS: exact Mellin-adjoint/operator factorization, finite C⁵ polynomial notch identity, spectral integrals at all three frequencies and distinct postpulse electric-Weyl outputs. The symbolic zero is exact even though the numerical quadrature retains roundoff. No images, no protected-object edits.

**HANDOFF — external audit:** independently check the Mellin integration-by-parts factor and the sign of the D adjoint, pulse regularity, spectral double-sided ±ν null, conservation inheritance from v15.724, all three physical ν values and the local scalar/vector/tensor Weyl readout. Explicitly distinguish a **tunable prescribed signed compact stress** from a physically selected localized matter action. Check whether the scalar notch remains exactly zero in a fully realistic source theory with material positivity and detector couplings (not established here).

**NEXT:** a credible physical-source gate must begin with a *specified positive-energy localized matter Lagrangian or microscopic medium* and derive an allowed, smooth covariantly conserved stress pulse on K4, rather than freely tuning Q and b. Without that extra selection the three-sector K4 system has genuine calculable response, but it cannot deliver a unique, source-independent dimensionless new gravitational observable.
