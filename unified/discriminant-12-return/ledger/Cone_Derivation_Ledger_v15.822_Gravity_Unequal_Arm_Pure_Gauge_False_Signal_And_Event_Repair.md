# Cone Derivation Ledger v15.822 — Gravity: unequal-arm pure-gauge false timing differential and physical emission-event repair

**Date:** 2026-11-12 US Eastern. **Parents:** v15.811 conformal photon/free-mirror/proper-clock optical transfer, v15.815 nine-arm five-helicity equal-arm differential geometry, v15.818 fully source-driven five-helicity numerical detector, v15.821 coasting pure-diffeomorphism metric/clock/emission-event null. **Immediately prewrite live HEAD:** b3dce6cc7bc71393d65162f69935786a705c0d1c; target absent. Strict additive-only, source and Suzuki certified objects preserved.

**Classification:** [D] a finite-dimensional and exact algebraic gauge artifact for unequal arms in the fixed-coordinate-emission-time optical formula; [D] cancellation by comparing the same *physical* emission event; [N] this is not an observable gravitational signal or new Cone interaction; [O] realistic unequal-arm spacecraft paths, full 3D gauge transformations and clock synchronization.

## Gate 444 — equal-arm common-mode null does not automatically cover unequal arms

From v15.821, for an arbitrary pure-coordinate perturbation with time-gauge generator **T(η,x)** on FLRW **a(η)=a0 exp(ℋη)**, an arm of comoving length d with coordinate emission η_e has a *spurious* fixed-coordinate-emission-label round-trip proper-time coefficient

**δτ_fixed(d)=−[a(η_e+2d)−a(η_e)] T(η_e,0)**.

The matched physical emission event has changed its coordinate label by **T_e=T(η_e,0)**. Correcting that event identification adds

**δτ_event(d)=+[a(η_e+2d)−a(η_e)]T_e**,

giving **δτ_physical(d)=0** for every arm in the pure gauge.

For two equal arms, their uncorrected fixed-label coefficients are identical and subtract to zero in a differential output. But for two **unequal lengths d1,d2**, their uncorrected difference is

**δτ_fixed(d1)−δτ_fixed(d2)=−[a(η_e+2d1)−a(η_e+2d2)]T_e**,

which is generically NONZERO even though the physical gravitational curvature is unperturbed FLRW. Thus the exact common-mode cancellation seen in the v15.815 equal-arm detector cannot be extrapolated to all future unequal-arm configurations or arbitrary synchronization choices.

## Gate 445 — concrete independent false signal and its exact removal

Take the coasting conformal rate ℋ=1/sqrt3 and explicit pure gauge

**T(η,x)=0.17 η³ exp(−1.1 iη+0.8 ix)**,

**U(η,x)=0.12 η³ exp(−1.1 iη+0.8 ix)**,

with coordinate emission η_e=0.08 and unequal comoving arm lengths **d1=0.075**, **d2=0.11**. Numerically integrating the complete first-order photon paths, free-mirror Green displacements and proper clock using the **original v15.821 pure-diffeomorphism** source, the difference of fixed-coordinate-arm coefficients is

**Δ_fixed≈+4.083647033896725×10^-6 −3.602914518152948×10^-7 i**,

despite the perturbation being a pure diffeomorphism. The exact endpoint formula above reproduces the same value at numerical accuracy. Including the appropriate physical emission-event correction for **each arm** removes the false differential:

**Δ_physical≈−1.54×10^-19+1.00×10^-18 i≈0**.

This example is a *complex Fourier control*, not a measured clock time or a new physical ripple. It proves a modeling failure if one interprets a fixed coordinate event as an invariant physical emission event for unequal arms. The result is independent of source and elasticity dynamics; it is a conventional geometric-optics gauge test.

## Gate 446 — operational lessons and source-detector originality

**Positive:** explicit physical-event anchoring restores the pure-gauge zero even for unequal arms. Any extension to gravitational detector geometries with unmatched baselines, moving spacecraft or clock synchronization must track emission and reception as *physical events*, not reuse coordinate labels untransformed.

**Negative:** optical geometry itself cannot produce a new Cone field interaction. The currently calculated K4 action is still literally matched ordinary Einstein–Hilbert plus isotropic relativistic solid. A conventional GR+same-solid detector with the exact source, boundary data and proper event definitions necessarily produces the **same** observables. There is no Cone-specific residual to claim here.

**Reproducer:** research-notes/k4_flrw_unequal_arm_gauge_bias_v15_822.py, additive commit **2710513ba0f60e56b42999a995164c9f043980fb**, imports the immutable earlier additive v15.821 pure-gauge reproducer and independently checks numerical unequal-arm difference against the closed-form endpoint artifact; locally executed to PASS. Historical source and certified assets unchanged; external audit pending.

**HANDOFF — external audit:** reexecute the v15.821 source script and v15.822 unequal-arm addendum end to end. Verify the physical-event correction sign, the nonzero unequal-length false differential and the exact invariant null, distinguish the special pure-gauge test from a full cosmological 3D gauge proof and review physical event anchoring of the initial-value K4 v15.812/818 optical definitions.

**NEXT:** generalize the benchmark to *arbitrary vector and scalar 3+1 gauge transformations* with explicit observer/receiver tetrads and freely falling mirror event identification; then formulate a physically realistic remote source-to-detector transfer. A new Cone coupling requires an additional independently derived and parameter-free physical operator/selector beyond the existing matched EH+solid action.
