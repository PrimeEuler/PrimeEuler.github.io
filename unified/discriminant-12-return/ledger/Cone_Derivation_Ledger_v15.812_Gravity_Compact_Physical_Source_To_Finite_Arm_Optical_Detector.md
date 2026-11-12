# Cone Derivation Ledger v15.812 — Gravity: one evolved compact positive-energy matter source drives a coasting-FLRW finite-arm photon/mirror/clock detector

**Date:** 2026-11-12 US Eastern. **Parents:** independently audited v15.750 canonical scalar physical matter evolution and scalar/vector/tensor source-first K4 modes; v15.760–761 and v15.787–788 independently audited Weyl versus full-Riemann Fermi detection; v15.794 independently audited conventional TT roundtrip light timing; v15.810 verified local photon/mirror/clock pure-gauge null; v15.811 coasting FLRW photon/mirror/proper-clock causal transfer. **Classification:** [D] an internally reproducible finite-baseline, two-way light-time response driven by the *same physically specified canonical matter stress* and all three K4 sectors with a coasting observer and freely falling mirrors; [N] any nonzero Cone-minus-conventional-GR+solid residual or a unique parameter-free prediction; [O] fully gauge-covariant cosmological detector boundary conditions, independent reexecution of committed v15.812 script, source-to-detector far-field wavepacket geometry, instrumental calibration. **Immediately prewrite live HEAD:** 3ebafee5e37d6414aa74849b29099763d37f82af, target path absent, no collision; existing Suzuki/certified files unchanged.

## Gate 420 — feed actual source-driven K4 metric histories into the causal FLRW light transfer

Preserve the v15.750 source and equations: on the coasting background **a(τ)=τ/sqrt3**, a compact positive-local-energy canonical spectator scalar has initial C7 data **χ0=w_R[cos(2x)+cos(z)]**, **χdot0=−χ0**, with R=7, box L=8π, source Fourier **K=(2,0,1)** and eta(solid)=3/4, κ=1. The canonical scalar is evolved by its exact KG Fourier functions from τ=1 to τ=1.35. Its derived energy density, pressure trace, momentum, tensor shear and analytic derivatives drive the constrained scalar P, vector f and tensor γ K4 modes, with the original v15.728 corrected pressure Ward.

At each source-time slice reconstruct, from those **same constrained mode solutions**:

**Φ_N(τ), Ψ_N(τ)** from the full traceful scalar ADM constraints (v15.729–750),

**B_V(τ)=b(τ) f_dot−J_V/A_V** and its conformal derivative **∂η B_V=a ∂τ B_V**,

**γ_T(τ)** from the sourced tensor mode.

These are *actual time histories*, not independently chosen harmonic response amplitudes. The new reproducer creates an additive standalone copy of the v15.750 code, retaining all source and mode calculations and appending only these auxiliary metric histories and the v15.811 photon/mirror/clock detector functional. The old v15.750 file remains unchanged.

## Gate 421 — define five actual freely falling arms and three independent differences

Introduce the spatially orthonormal directions

**n=(2,0,1)/sqrt5**, **e=(1,0,−2)/sqrt5**, **b=(0,1,0)**,

so **K=sqrt5 n**, and the two diagonal directions **u±=(n±e)/sqrt2**.

Choose comoving arm length **d=0.075** and conformal emission time **η_e=0.08** relative to τ0=1, with **η=sqrt3 logτ** and **ℋ=1/sqrt3**. The return event is at **η_e+2d=0.23**, strictly inside the source-history coverage of about 0.52. A return proper-time delay for each arm is computed from

**O_u=∫_0^d ds [−Φ_N−Ψ_N−V_u+H_uu/2]_(η_e+s) exp[i(K·u)s]**,

**I_u=∫_0^d ds [−Φ_N−Ψ_N+V_u+H_uu/2]_(η_e+d+s) exp[i(K·u)(d−s)]**,

**M_u=2exp[i(K·u)d]X_u(η_e+d)−X_u(η_e)−X_u(η_e+2d)**,

where the free mirror's displacement is obtained from the complete history of the **physical K4 metric**

**X_u(t)=∫_0^t ds [1−exp(−ℋ(t−s))]/ℋ [−i(K·u)Φ_N +∂η V_u+ℋ V_u](s)**.

The emitting observer proper clock adds **C_u=∫_(η_e)^(η_e+2d) a(s) Φ_N(s) ds**, and the received proper travel-time perturbation is

**δτ_u=a(η_e+2d)(O_u+I_u+M_u)+C_u**.

This formula contains a fixed source Fourier coefficient, freely falling mirrors initially at rest in the chosen conformal Newtonian gauge at η=0, and one coasting beam-splitter proper clock. It is a first-order finite-baseline optical transfer on an **FLRW background**, but it is not a realistic laser interferometer with full optics, moving spacecraft, or transverse spatial wavepacket transport. Fourier conjugate ±K must be combined for a real spacetime signal.

Construct differential equal-arm outputs **D1=δτ_n−δτ_e**, **D2=δτ_e−δτ_b**, **D3=δτ_(u+)−δτ_(u−)**. The common beam-splitter proper-clock correction cancels exactly between equal-length arms in these differences, as it should.

## Gate 422 — numerical physical-source polarization selection and refinement

Evaluate both independently refined versions of the v15.750 matter evolution: **48³ with 21 source-time samples** and **64³ with 31 samples**, Fourier bin (8,0,4) for box L=8π. The direct matter Fourier energy Ward residual is about **3.70×10^-8** and **1.34×10^-11** respectively. Use cubic source-time interpolation in conformal time and *independently numerically integrate* the causal photon, mirror and clock terms, without approximating the source as a stationary harmonic mode.

The final 64³ differential normalized complex positive-K Fourier coefficients for the three output arms are approximately:

| Differential arm signal | scalar S | vector V | tensor T | all sectors |
| --- | ---: | ---: | ---: | ---: |
| D1=n−e | +0.000693644−0.0000300045 i | ≈+2.05×10^-11 i | +0.000224430 | +0.000918074−0.0000300045 i |
| D2=e−b | exactly 0 by symmetry | ≈−2.05×10^-11 i | −0.000448861 | −0.000448861 |
| D3=u+−u− | exactly 0 by symmetry | +0.000685992+0.0000396612 i | exactly 0 by symmetry | +0.000685992+0.0000396612 i |

The 48³ and 64³ responses agree with a **maximum absolute difference about 2.63×10^-10** across their 3×4 complex matrices, for these specific smooth initial data and time/arm setup. The source's two unobserved helicities are absent by construction: one vector transverse polarization e and one plus tensor mode (e⊗e−b⊗b). This is a **restricted three-sector polarization demonstration**, not a general five-polarization detector inversion.

The strong geometric result is that this particular symmetric arm geometry gives **D2 scalar=0** and **D3 scalar=tensor=0** identically in the adopted linear/source basis, so the rotated difference D3 genuinely isolates the vector contribution of this sourced K4 model. D1 has nonzero scalar and tensor contributions and D2 is tensor-dominated for this initial-value history. The tiny D1/D2 vector coefficient is a source-history/geometry cancellation, not an exact universal vector null. The individual complex amplitudes are **model/Fourier normalized time-delay perturbations**; a real time delay requires ±K pairing, source strength and actual physical arm scale, so no SI strain or gravitational coupling is inferred.

## Gate 423 — physical meaning and the stringent novelty null

This is the first **same-source complete optical transfer** in the gravity ledger: the physically defined canonical matter Cauchy data lead to conserved stress, then to sourced K4 scalar/vector/tensor dynamics, then to constrained metric potentials, and finally to null photons, free mirrors and proper clock on the matching coasting FLRW background. It goes beyond either the earlier local Fermi tidal metric (v15.788) or arbitrary-metric harmonic photon transfer (v15.811).

However the photon and mirror calculations are standard perturbative GR geometry, and the K4 Einstein–Hilbert+ordinary relativistic-solid action remains exactly identical to the matched comparator certified at v15.760. A conventional GR+same-isotropic-solid calculation with the **same action, cosmological background, source, initial data and photon/mirror detector** necessarily yields the same three displayed complex time-delay amplitudes. Therefore the **Cone-minus-matched-GR+solid residual is exactly zero** at this action level. This is an important negative originality result, not a measured exclusion of *all potential future Cone physics*.

**Reproducibility:** research-notes/k4_compact_canonical_two_way_coasting_detector_v15_812.py, additive commit **3ebafee5e37d6414aa74849b29099763d37f82af**. The local independent numerical derivation (including the same v15.750 physical-source spectral evolution and independent causal quadratures) produced the table and passed the two-resolution checks. The committed source is an additive extension generated from the frozen v15.750 script; its exact committed-byte independent execution remains an external audit item and is not yet certified. No image generation; no historical objects edited.

**HANDOFF — external audit high priority:** independently run the new committed v15.812 script; inspect retained exact v15.750 physical-source evolution, auxiliary B and B_η extraction, correct 0.23 conformal-time reception within window, correct a(η)=exp(η/√3)/√3 reception scaling and proper clock factor, both mirror worldline Green functions, ±K reality pairing, scalar/tensor/vector isolated output symmetry and numeric convergence. Audit v15.810/811 source-independent photon transfer and its pure-gauge test concurrently. Preserve the existing K4 matched-comparator null, not a false positive physical prediction.

**NEXT:** construct full cosmological gauge-invariance controls for the *same* photon/mirror/clock initial-value setup, include the other two helicities and a source with localized **three-dimensional spatial propagation to a remote receiver**, and derive a physically independently selected Cone-only operator or physical scale. Without that, no new dimensionless gravitational observable is claimed despite the successful complete source-to-optical-transfer chain.
