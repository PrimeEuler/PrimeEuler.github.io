# Cone Derivation Ledger v15.761 — Gravity: an explicit on-shell matter Ricci correction survives differential tidal-arm subtraction

**Date:** 2026-11-11 US Eastern. **Parents:** standard canonical scalar action and positive local energy v15.727; on-shell two-nonparallel-wave stress and exact gauge-invariant scalar Weyl v15.730; spatially compact source and evolved all-three Weyl channels v15.731/740/750; finite-Fermi-detector Weyl tomography and Ricci decomposition v15.760. **Audit:** Round 548/v15.754 independently verified the v15.750–752 gravity calculations; new detector gates v15.760–761 await independent audit. **Immediately prewrite live HEAD:** c75b32f9164d25f537caaef076ca4a2b2789ab43; target v15.761 ledger absent. All files additive and no certified Suzuki assets modified.

**Status:** [D] exact leading-order Einstein Ricci anisotropic-shear correction due specifically to the canonical spectator matter's two-wave cross Fourier mode, [N] a trace-free local detector reading only electric Weyl without Ricci correction, [O] total elastic-solid Ricci stress, complete full-Riemann physical detector and novel Cone-minus-conventional-model residual.

## Gate 394 — use the actual on-shell matter cross-stress, not a free Ricci ansatz

Recall the exact on-shell canonical scalar solution of v15.730 on a=tau/sqrt3:

**chi=A(tau)cos(2x)+B(tau)cos(z)**,

**A=cos(sqrt11 log tau)/tau**, **B=cos(sqrt2 log tau)/tau**.

For its spatial wavevectors **p=(2,0,0)**, **q=(0,0,1)**, and **K=p+q=(2,0,1)**, the positive sum-frequency cross-mode of the real scalar's spatial anisotropic physical stress in an orthonormal FLRW frame is

**[T^(orth)_(ij)]_K,anisotropic=−A(tau)B(tau)[p_i q_j+q_i p_j]/[4a(tau)²]**.

Each real cosine contributes positive-frequency Fourier amplitude 1/2; taking two spatial derivatives yields the explicit minus sign. The isotropic spatial stress trace, which is generally nonzero for this positive-energy matter field, does not contribute to trace-free detector arms D. A real stress includes the conjugate minus-K coefficient as well; a single complex Fourier coefficient may have either sign and is not individually a positive energy density.

At tau=1, **A=B=1**, **a²=1/3** and the anisotropic cross-stress coefficient becomes **−3/4(p q^T+q p^T)**.

## Gate 395 — exact nonzero spectator-field Ricci contamination of all three arm combinations

Use the orthonormal basis and three differential arm tensors from v15.760,

**n=(2,0,1)/sqrt5**, **e=(1,0,-2)/sqrt5**, **b=(0,1,0)**,

**D1=nn^T−ee^T**, **D2=ee^T−bb^T**,

**D3=uu^T−vv^T**, with **u=(n+e)/sqrt2**, **v=(n−e)/sqrt2**.

Direct exact index contraction at tau=1 gives

**(D1:T_spectator,D2:T_spectator,D3:T_spectator)=(−12/5,+6/5,+9/5)**

for the positive complex K coefficient at the stated unit scalar amplitude.

Assuming the Einstein field equation with coupling κ and the standard orthonormal (−+++) decomposition,

**D:R_0i0j = D:C_0i0j−(1/2)D:R_ij**,

**D:R_ij = κ D:T_ij,total** for D trace-free.

Therefore the **spectator-only** contribution to the full-Riemann minus Weyl projected tidal curvature is the nonzero vector

**Delta_A_spectator=[6κ/5,−3κ/5,−9κ/10]**.

This does not mean these are the physical *complete* corrections, because **T_total = T_spectator + delta T_K4 solid** (including the solid's own anisotropic and background/metric perturbations). The solid contribution has not yet been reconstructed or independently audited as a full Ricci/Einstein constraint transfer. Nor is the monochromatic benchmark spatially localized; compact physical source fields were constructed later in v15.731/740/750, but the neat rational coefficients in this gate belong **only** to v15.730's exact on-shell two-wave example.

The outcome is nevertheless decisive as a control: **real positive-energy canonical matter does not generically permit electric Weyl curvature to be equated with the full differential tidal acceleration**. The missing Ricci correction is not merely a formal symbolic possibility.

## Gate 396 — experimental and originality implications

A physically measurable local geodesic-deviation differential acceleration at short baseline ℓ is **−ℓ D:R_0i0j** at leading Fermi order, not **−ℓ D:C_0i0j** unless the Ricci contraction is independently zero, removed, or measured. The exact D matrix inversion in v15.760 reconstructs the *Weyl-only* modes from hypothetical Weyl-selective readouts; it does **not** reconstruct the full detector response without accounting for the elastic solid's total stress.

More fundamentally, the current K4 action is the same Einstein–Hilbert plus ordinary relativistic isotropic-solid action used in the matched conventional comparator. The exact action-level transfer residual established in v15.760 is zero if background, material coefficients, source and detector map are matched. The nonzero Ricci shear does not introduce a new Cone interaction: it follows from standard Einstein equations with conventional matter and must be present in both matched models.

**Reproducer:** research-notes/k4_two_wave_spectator_ricci_shear_v15_761.py, additive commit **c75b32f9164d25f537caaef076ca4a2b2789ab43**. Locally executed to PASS using exact SymPy rational projectors and on-shell cosine amplitudes, no image generation, no frozen file changes.

**HANDOFF — independent audit:** check the sign and Fourier factor 1/4 for the on-shell two-wave gradient cross stress, orthonormal a^-2 conversion, the three arm shear contractions and signature-dependent Einstein/Weyl conventions. Crucially distinguish spectator-only Ricci from total K4 elastic-solid Ricci, and demand exact full-Riemann sourced detector calculation before predicting actual detector accelerations or invoking a physical new interaction.

**NEXT:** reconstruct the complete gauge-invariant **electric Riemann** tidal field from sourced scalar/vector/tensor metric perturbations including the coasting solid's linearized stress response, then embed in finite-separation, retarded Fermi detector geometry. Compare that full detector response against a standard GR+relativistic-solid model *using exactly the same action and matter source*. A nonzero physical residual requires deriving some independently selected Cone-specific field-theoretic term rather than relabeling the existing action.
