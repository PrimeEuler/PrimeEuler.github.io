# Cone Derivation Ledger v15.865 — Gravity: physically conserved coupled matter/force-agent pair with identical Cone leverage but rotated K4 tensor optical output

**Date:** 2026-11-13. **Parents:** Muse/Sandbox force HJ/null/parabola-leverage v15.857–860 (Round 565/v15.861 independently audited; v15.857 NumPy portability defect separately owned by Sandbox); Gravity v15.862/863 exact lever-vs-null-stress/TT angular obstruction; certified K4 relativistic EH+solid tensor equation and photon/mirror/clock detector v15.750–818, full solid gauge Ward v15.833. **Immediately prewrite live HEAD:** fa13309d1e9676a4d81080b4612aa750748880cb. Unique target path checked absent; additive only, no Suzuki, Sandbox, or certified historical objects altered.

**Status:** [D] an exactly on-shell, two-real-scalar, interacting classical matter-plus-force-agent system with equal and opposite local stress exchange; [D] an exact tensor-source polarization rotation at fixed particle-mode energy and rapidity; [N] first sourced **coasting K4 tensor-channel** wave and conventional tensor optical response with fixed Cone leverage but different plus/cross outputs; [N] the leverage ratio alone selects neither polarization nor gravitational coupling; [O] full five-helicity K4 scalar/vector constraints for the interaction source, physically localized emitter, remote detector and a new parameter-free Cone-specific interaction.

## Gate 489 — specify a local force agent and enforce total stress conservation

Replace the earlier unforced rank-one stress *snapshot* by two interacting real canonical scalars `chi` (matter) and `phi` (momentum-exchange agent) with a specified covariant action, metric signature (−+++):

**ℒ=−(∇chi)²/2−m²chi²/2−(∇phi)²/2−m²phi²/2−g chi phi**, with m²>0 and g>0 supplied (not predicted by Cone).

The coupled exact equations are **□chi−m²chi−g phi=0** and **□phi−m²phi−g chi=0**. Separately define the standard kinetic-plus-own-mass stress T_chi and agent stress T_phi+interaction, assigning **−g chi phi g_mu nu** to the agent. Their covariant divergences satisfy

**∇_mu T_chi^{mu}{}_nu=+g phi ∂_nu chi**, 
**∇_mu T_agent^{mu}{}_nu=−g phi ∂_nu chi**,

hence **∇_mu (T_chi+T_agent)^{mu}{}_nu=0** identically on shell. The first exchange current is nonzero at generic spacetime points; this is a truly interacting, mutually compensated system rather than an imposed force on a nonconserved test source. The arbitrary coupling g is a conventional supplied input; the two-field system is a comparator, not a derivation of gravity.

## Gate 490 — two exact interacting wave configurations of the same leverage and different TT stress

Choose the symmetric coupled-field eigenmode **chi=phi**, with arbitrary common real amplitude A, and two equal-frequency plane waves

**chi=phi=A[cos(omega t−p·x)+cos(omega t−q·x)]**,

**omega²=k²+m²+g**,

**p=(k sinθ cosα,k sinθ sinα,k cosθ)**,

**q=(−k sinθ cosα,−k sinθ sinα,k cosθ)**.

All α share **|p|=|q|=k**, the same omega and physical group-speed label **β=k/omega**, hence the exact same Muse cone energy leverage **L=(1+β)/(1−β)**. The shared source Fourier wavevector **K=p+q=(0,0,2k cosθ)** does not change with α. This plane-wave analytic witness is not spatially compact and has formally infinite total energy; local canonical energy density is nonnegative for the positive-eigenvalue branch m²+g>0. There is no independently calibrated force magnitude or source amplitude.

Fourier project the *total* pair stress at the summed wavevector K, with the standard spatial TT projector transverse to K. From the actual canonical gradients of both fields, including the cosine Fourier coefficients and the equal/effective interaction eigenmode, the **positive-K TT stress** is exactly

**Π^TT(K,t)=Q exp(−2i omega t) [ [cos2α,sin2α,0],[sin2α,−cos2α,0],[0,0,0] ]**,

**Q=A² k² sin²θ/2**.

The interaction potential is isotropic and contributes no TT gradient/shear source. For α=0 the stress is entirely tensor-plus; for α=π/4 it is entirely tensor-cross; α=π/8 splits equally. Their tensor norms are identical **Π^TT:Π^TT=2Q²** although the individual detector projections differ.

This is an exact, fully conserved *local field-theory source*, not a dust test particle forced along a prescribed worldline. The relevant β is the common eigenmode group speed, not the instantaneous velocity of every point in an oscillatory real scalar standing/superposed field. Do not interpret β as a measured local fluid speed or an on-shell accelerating massive particle's trajectory.

## Gate 491 — independently reproduce its genuine coasting-FLRW tensor optical readout

For a stronger model check, put the very same interacting symmetric eigenmode on the frozen coasting **a(τ)=τ/√3** FLRW background. Its exact coupled on-shell time-dependent amplitude V(τ) obeys

**V¨+3V˙/τ+[3k²/τ²+(m²+g)]V=0**,

with V(1)=1, V˙(1)=−1. In each Fourier summed-K component the *total* canonical stress energy continuity equation is verified exactly: **ρ_K˙+3(ρ_K+p_K)/τ+iK·T^{i0}_K=0** (the mass/coupling potential is included), not merely the external-force or dust approximation. With k²=2 and the 3D rotated pair p=(cosα,sinα,1), q=(−cosα,−sinα,1), the comoving K=(0,0,2), and the initial wave group velocity label is **β=√[2/(2+1.25)]≈0.78446454**, with **lever≈8.27921561** independent of α.

Use the exact archived K4 EH+solid tensor Euler equation at solid eta_s=3/4, **γ¨+3γ˙/τ+14γ/τ²=−2Π^TT**, with the total physical canonical tensor TT stress coefficient **Π_+=V²/(2a²)cos2α**, **Π_×=V²/(2a²)sin2α**, and zero propagating tensor initial position/velocity at τ=1. This is a linear-order sourced tensor sector on the original coasting background; its full on-shell scalar/vector Einstein/solid perturbations are not reconstructed in this gate. There is no free extra force or numerical fitting after setting m²+g=1.25, eta_s=3/4 and field amplitude 1.

Finally insert both tensor histories into the existing standard FLRW photon outward/return metric transfer with transverse equal comoving arms **d=0.10**, conformal emission **eta_e=0.08** and return eta_e+2d=0.28, within the solved cosmic-time window through τ=1.6. The zero scalar/vector perturbation TT-gauge comparator has no first-order mirror acceleration or emitter lapse; the tensor differential **x−y** and rotated ±45-degree readouts are

**D_+=(a_r)∫_(eta_e)^(eta_e+2d) γ_+(eta)d eta**, 
**D_×=(a_r)∫_(eta_e)^(eta_e+2d) γ_×(eta)d eta**.

The numerical integration of the actual coasting KG and sourced K4 tensor ODE, with an independent outbound-versus-inbound photon quadrature check, gives:

| source orientation α | Cone lever | normalized D_plus | normalized D_cross |
| --- | ---: | ---: | ---: |
| 0 | ~8.279216 | **−0.00199200794** | ~0 |
| π/8 | ~8.279216 | **−0.00140856** | **−0.00140856** |
| π/4 | ~8.279216 | ~0 | **−0.00199200794** |

These are coasting model-normalized Fourier-mode optical proper-time coefficients, not experimentally calibrated strains or independent far-field waveforms. Numerical ODE and optical quadrature controls pass at the stated tolerances. They show a nonzero polarization-specific difference at **identical Cone leverage and identical supplied coupling/energy mode**.

The same file additionally checks an independently forced **Minkowski** tensor oscillator benchmark with equal leverage L=5 (different normalization and background), showing a plus↔cross optical rotation. The Minkowski and coasting outputs must not be mixed as though they share one source-preparation background.

## Gate 492 — decisive novelty verdict and limitations

**Positive:** the force-agent conservation loophole from v15.862/863 is now closed for this controlled classical field example: both sectors exchange momentum locally with opposite divergences and the complete interacting matter-plus-agent tensor is conserved, while the same rapidity leverage gives different TT optical polarizations. This is a source-to-*sourced-K4-tensor*-to-standard-optical-detector comparison rather than merely a kinematic dyad projection.

**Negative:** the result demonstrates **non-universality of lever-only gravitational response**, not a new Cone force. The same conventional interacting relativistic fields and EH+ordinary elastic-solid action produce identical outputs in an ordinary GR+solid comparator. Their polarization rotation is the standard spin-2 angular projection. The chosen interaction g and field amplitude A were supplied by hand and therefore select nothing about fundamental forces, G, the 1/4 gravity mesh, or Door III.

**Open:** the source is an unbounded plane-wave configuration and the coupled interacting scalar fields are exact on-shell only on the specified background, without gravitational backreaction to the coasting geometry. The tensor-mode optical outputs are partial **sector** contributions to a fully constrained detector; the scalar/vector gravity perturbations sourced by the same total stress are not included. A complete five-helicity optical response, especially at a separated receiver from spatially compact matter-plus-agent data, remains uncomputed.

## Reproduction and audit/collision notice

The first script was committed under **research-notes/k4_conserved_force_agent_tensor_optical_v15_864.py**, SHA **4b4118ca57d68e83a6acc5fd2bf6811755164605**, while Sandbox separately deposited its **v15.864 tangency-chain** ledger and payload. The paths and contents are independent and no existing file was overwritten, but **v15.864 was also used as a semantic version label by Sandbox**. This is a disclosed version-label collision.

The original gravity script also has one **SymPy structural-equivalence assertion bug**: `assert S_TT.subs(az,0)==Q*s.diag(1,-1,0)` can fail because algebraically opposite forms `c²−1` versus `−(1−c²)` are not structurally equal. It is **not** executable PASS as first committed, even though its mathematics checks out.

The additive original-preserving **research-notes/k4_conserved_force_agent_tensor_optical_v15_865_repair.py**, commit **fa13309d1e9676a4d81080b4612aa750748880cb**, repairs exactly that assertion in memory and replays all original calculations without changing the archived script or Sandbox files. An equivalent expanded local standalone calculation **was independently run to PASS** for both coupled equations, stress conservation, source TT projection, angle rotation, coasting Fourier stress Ward, sourced tensor K4 ODE and flat/coasting optical responses. The exact newly committed repair wrapper is **pending external post-commit audit**.

**HANDOFF — external audit and Muse/Sandbox:** independently reexecute the repaired v15.865 wrapper and derive the two-field source/current/TT coefficients; check coasting stress Ward (including the mass/interacting potential), source term factor-of-two, solid beta_T=14, photon time conversion, initial eigenmode rapidity labels, and the negative novelty verdict. Explicitly preserve Sandbox's authoritative v15.864 tangency chain and both historical gravity scripts without rewrite.

**NEXT:** extend the same interacting conserved two-field source to all scalar/vector Einstein–solid constraints and all five optical polarization channels; then localize its complete Cauchy data and compute a remote receiver response. Require an independently justified Cone operator/scale before claiming any new force or gravity.
