# Cone Derivation Ledger v15.817 — Gravity: all five canonical scalar source helicities persist under smooth spatial localization

**Date:** 2026-11-12 US Eastern. **Parents:** v15.727 ordinary canonical positive-local-energy action, v15.731–740 spatially compact source and source Fourier stress method, v15.750/812 physical three-sector evolution-to-optical-detector, v15.815 five-helicity local and finite-arm tomography, v15.816 all-five exact four-wave nonlocalized source witness. **Live HEAD immediately prewrite:** 29229e6a1513d3ce3d745c8f72623909d10ff9ae. New ledger target absent. Additive-only and no Suzuki/frozen certified assets changed.

**Status:** [D] explicit smooth compact Cauchy datum with all five nonzero canonically derived stress Fourier helicities, [N] finite spatial window changes source amplitudes relative to exact unbounded waves, [O] time evolution and all-five sourced K4 optical detector, complete cosmological gauge control and new Cone-only operator.

## Gate 431 — apply the finite spatial window to the physically specified source

At τ0=1, on the coasting a=τ/sqrt3 canonical real massless scalar background, take the four-wave initial configuration of v15.816:

**chi0=w_R(x,y,z){cos(2x)+cos(z)+sqrt2[cos(x+y)+cos(x−y+z)]}**,

**chi_dot0=−chi0**.

The cutoff is **w_R=product h(coord/R)**, **h(u)=(1−u²)^8** for |u|<1 and zero outside; each spatial direction has compact support of width 2R and the cutoff is globally C7. This defines smooth-enough finite-energy Cauchy data with local nonnegative canonical energy density **rho=(chi_dot0²+|grad chi0|²/a²)/2≥0**. The standard well-posed hyperbolic KG Cauchy problem evolves these data, although this gate evaluates only their stress on the initial slice.

For the Fourier stress at **K=(2,0,1)**, use a periodic numerical box **L=8pi** with cutoff radius **R=10<4pi**, and retain all cutoff derivatives when evaluating actual coordinate gradient products. The 3D FFT bin is (8,0,4); normalize the Fourier coefficient by **sum(w_R²)** so different spatial numerical refinements represent comparable source strengths. The source's physical total energy and Fourier amplitude still depend on the packet size and canonical field amplitude, and this quotient is not a gravitational coupling calibration.

## Gate 432 — five independent, nonzero finite-energy source projections

In the detector-aligned basis

**n=(2,0,1)/sqrt5**, **e=(1,0,−2)/sqrt5**, **b=(0,1,0)**,

calculate the *actual* spatial orthonormal canonical stress's positive-K Fourier coefficient **T_(ij)(K)=3 Fourier_K[partial_i chi0 partial_j chi0]**, with the isotropic spatial term removed by the tracefree contractions. Define its five coefficients

**S=n T n−tr(T)/3**, **Ve=n T e**, **Vb=n T b**, **T+=(e T e−b T b)/2**, **T×=e T b**.

For this compact finite R=10 packet, directly evaluated normalized Fourier coefficients at the initial τ=1 slice are approximately

**(S,Ve,Vb,T+,T×)=(-5.07273329,+0.64246997,-0.65234397,-0.57650916,+1.42509902)**.

All five are nonzero and real to numerical roundoff. The three-grid 48³,64³,80³ refinement gives maximum absolute differences **3.87×10^-12** between 48³ and 80³, and **2.33×10^-15** between 64³ and 80³. Thus this is not a spurious alias or FFT-bin error at the stated resolution.

For comparison, the unbounded exact four-wave source of v15.816 gives

**(-24/5,+3/5,-3sqrt5/10,-3/5,+3sqrt5/5)** ≈ **(-4.8,+0.6,-0.67082,-0.6,+1.34164)**.

The finite packet differs due to its cutoff gradients and Fourier windowing. Unlike a numerical-resolution discrepancy, these differences persist under N→∞ at fixed R; they encode a different *physical source preparation*. The packet is spatially compact at the initial slice and can be evolved without boundary contact over a short causal interval.

## Gate 433 — separate source existence from field evolution and detection

The positive result removes one more source-selection worry: the two extra helicities necessary for the v15.815 five-mode detector can arise from **finite-energy compact canonical scalar initial data**, not just an unbounded four-plane-wave algebraic construction. But it remains a **source-stress projection** test, not a full K4 five-mode curvature response, let alone a detector measurement. The scalar's stress is quadratic in the field and at τ0 has nonzero isotropic pressure, energy and momentum; those must be included in a correct full sourced constrained evolution (as in v15.728–729 and v15.750).

**Reproducer:** research-notes/k4_compact_five_helicity_canonical_stress_v15_817.py, additive commit **29229e6a1513d3ce3d745c8f72623909d10ff9ae**. Independent local NumPy FFT tests compared 48³/64³/80³ and reproduced all five nonzero projections. The new committed script awaits external independent audit and will not be called certified until then. No image generation, source-code overwrite or measured G insertion.

**HANDOFF — external audit:** verify the four spatial wavenumbers' common Fourier K, all finite C7 window derivatives, correct Fourier bin and normalized local stress, the five independent projected components and three-resolution agreement. Compare with v15.816 unbounded source and v15.815 five-mode detector but do **not** promote their conjunction to a computed physical five-helicity detector observation.

**NEXT:** evolve this **same compact four-wave canonical scalar source** under the KG equation, derive pressure-corrected scalar and both vector/two tensor K4 driving stresses and constrained metric histories, then apply the existing FLRW photon/mirror/clock detector to all five modes. In parallel, test full gauge covariance of the source+mirror Cauchy data+emitter clock in the cosmological background. Finally subtract exactly matched standard EH+solid GR; no Cone-specific residual exists until a new independently justified operator/scale is derived.
