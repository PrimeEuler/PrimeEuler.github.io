# Cone Derivation Ledger v15.721 — Gravity: common conserved source, vector and tensor Weyl channels, and electric-only three-mode obstruction

**Date:** 2026-11-11 US Eastern. **Parents:** v14.928 EH+K4 TT tensor action; v14.935 original vector reduced-action construction; v15.710 source-first vector shift; v15.716–717 exactly covariantly conserved tilted trace-free Fourier stress; v15.719–720 scalar gauge-invariant Bardeen and Weyl transfer. **Status:** [D] exact vector source-to-constraint response on coasting K4, and local conformal-frame vector electric and magnetic Weyl; [C] standard TT action-to-source coefficient and source-conditioned particular solutions; [N] a single electric tidal channel does not automatically display all three modes; [O] full retarded vector/tensor history, physically localized source/action and proper detector transfer. **Immediately prewrite HEAD:** 4c92e26e18fe1212bdf380a12066cbaa61482ca0; target file absent. Additive only; no Suzuki/far-tail protected objects touched.

## Gate 334 — source the original vector constraint using the same conserved FLRW stress

Take the source of v15.716, Fourier phase exp(+ikz), normalized axis n=(sqrt(1/2),sqrt(1/3),sqrt(1/6)), and its fixed trace-free tensor coefficient Q0_ij=sigma(n_i n_j-delta_ij/3). For any transverse component Q=Q0_zy, the prescribed covariantly conserved stress satisfies

**T^(0y)=-i k Q/(2 tau a²)**, **a=tau/sqrt(3)**.

In the archived vector gauge F_y=0, g_0y=-a B_v and the metric source term gives the *formal* vector shift coefficient

**J_v=-a⁴ T^(0y)=i k tau Q/6**,

with a consistent conjugate Fourier-mode pairing. The vector shift was already derived from the original EH+K4 action at v15.710. Its unreduced quadratic coefficients on coasting K4, k>0 and kappa=C=1, are

**A_v=tau(4+3k²)/(6sqrt(3))**,

**b_v=4tau/[sqrt(3)(4+3k²)]**,

**K_v=2tau³ k²/[3sqrt(3)(4+3k²)]**,

**G_v=4tau eta k²/(9sqrt(3))**,

where **B_v=b_v f_dot-J_v/A_v**. The sourced vector Euler equation is exactly

**K_v f_ddot+K_v' f_dot+G_v f=-(b_v J_v)'**.

Hence, dividing by K_v,

**f_ddot+(3/tau)f_dot + [2eta(4+3k²)/(3tau²)]f = -2i Q/(k tau²)**.

The homogeneous mode coefficient reproduces the archived vector dispersion **omega_V²=[(8eta/3)+2eta k²]/tau²**; the source is not an added arbitrary oscillator forcing. For this *particular source history*, an exact steady particular solution is

**f_part=-3i Q/[eta k(4+3k²)]**,

**B_v,part=-i sqrt(3)k Q/(4+3k²)**.

The source normalization relies on standard metric-stress variation and prescribed conservation; a localized physical matter action or real, finite-width wave packet has not been supplied. A real perturbation is obtained by combining complex-conjugate Fourier modes.

## Gate 335 — gauge-invariant vector Weyl distinguishes electric from magnetic response

Use the conformal time chi, with **dchi=d tau/a**, and the vector conformal metric perturbation **h_(chi y)=-B_v** in the original spatial-vector gauge. Four-dimensional Weyl curvature is conformally invariant with the appropriate index placements; orthonormal electric/magnetic components acquire a factor 1/a². Independently derive linearized four-dimensional Weyl from the conformal perturbation h_(chi y)=V exp[i(kz-omega chi)] in flat conformal coordinates:

**C_(0y0z) = k omega V/4**, **C_(0z yz)=k² V/4**,

in the stated Riemann/sign convention. Restoring V=-B_v and an arbitrary time history gives

**E^(Weyl,V)_(yz) = -i k (dB_v/dchi)/(4a²) = -i k B_v_dot/(4a)**,

**C_(0z yz)^(orth) = -k² B_v/(4a²)**.

These are curvature observables, unlike B_v alone. In the explicit particular solution **B_v,part is constant in conformal time**, so its **vector electric Weyl vanishes** while the displayed magnetic-type Weyl component is **nonzero** for kQ nonzero.

This does NOT mean the general vector mode has zero electric curvature: transient/retarded vector motion has B_v_dot not generally zero. It also does not mean that every detector can sense the nonzero magnetic Weyl component; a physical detector coupling must be specified. It is a source-history-dependent selection, not a universal prohibition on gravitational vector tides.

## Gate 336 — independent tensor action source and TT Weyl response

The audited v14.928 TT quadratic action is

**S_T²=(1/(8kappa)) integral a³[gamma_dot_ij²-(k²/a²+m_T²)gamma_ij²]**,

**m_T²=(8eta/3)H²**.

Source it by the standard stress variation **delta S_m=(1/2) integral sqrt(-g) T^(ij)delta g_ij**, with **delta g_ij=-a² gamma_ij** in the original +--- notation. For the same v15.716 tracefree source, the transverse tracefree component is **Pi_T=Q0_T/tau²**, so, with the stated sign convention,

**gamma_T,ddot+3H gamma_T,dot + [k²/a²+m_T²]gamma_T= -2kappa Q0_T/tau²**.

On coasting a=tau/sqrt(3), a constant particular TT tensor solution is

**gamma_T,part=-2kappa Q0_T/[3k²+8eta/3]**.

The conventional exact linearized Weyl computation for a local TT conformal perturbation h_xx=-gamma_+, h_yy=+gamma_+, h_xy=-gamma_cross yields

**C_(0x0x)=-(k²+omega²)gamma_+/4**, **C_(0y0y)=+(k²+omega²)gamma_+/4**, and analogous cross components, before dividing by a² for orthonormal FLRW curvature. The static conformal particular tensor therefore has a **nonzero electric Weyl tide** for generic TT source, unlike the static-vector particular solution in Gate 335.

The linearized Weyl formula and source-to-particular TT amplitude are conventional field-theory/elastic-solid responses. Their overall sign depends on the adopted stress/Riemann conventions, not on a Cone-specific numerical 1/4 interaction.

## Gate 337 — three-mode detector claim is strictly conditional

The common covariantly conserved Fourier stress has generic nonzero **source projectors** into tensor, vector and scalar sectors. The source-first calculations now show: (i) the scalar *particular* sourced metric has nonzero scalar electric Weyl (v15.719), (ii) the tensor *particular* sourced metric has nonzero electric Weyl (this gate), and (iii) the vector *particular* source has **zero electric but nonzero magnetic** Weyl here. Thus three nonzero source projectors are not equivalent to three nonzero readout amplitudes in one detector. The v15.706 exact squared-frequency-pole ratio 3 remains an identity of the homogeneous coasting isotropic-elastic model, not a guaranteed three-peak electric-tidal measurement.

The universal **2/3** in scalar STF Weyl norm remains standard three-space trace-free geometry. The vector magnetic curvature and tensor TT shape are different irreducible polarization structures: do not transfer the scalar 2/3 amplitude normalization to them by analogy. A physical finite-size source, full covariant matter action, retarded initial conditions, actual Fermi detector coupling, and coherent T/V/S readouts remain open. K4 coasting cosmology remains empirically disfavored by the earlier supernova comparison.

**Reproducer:** research-notes/k4_vector_tensor_weyl_v15_721.py, additive commit 4c92e26e18fe1212bdf380a12066cbaa61482ca0, independently tested locally to PASS: original vector coefficients/pole, source-first particular, full four-dimensional linearized Weyl electric and magnetic components, TT source Euler coefficient and TT electric Weyl. No image generator. Original certified scripts and Suzuki/far-tail unchanged.

**HANDOFF — external audit:** independently verify the vector metric source coefficient J_v under original v14.935 Fourier/sign/normalization conventions, Euler source derivative and coasting particular solution; check conformal Weyl components and a^-2 orthonormal conversion; verify the tensor stress variation and normalization against v14.928; distinguish local Fourier complex source from realizable matter. Audit v15.719–720 and the earlier v15.716–717 source/ward mapping concurrently before any physical detector claim.

**NEXT:** derive source-history-dependent vector and tensor retarded curvature transfer, then evaluate response to a finite-duration conserved physical stress pulse. Specifically determine whether the vanishing vector *particular electric* tide persists under retarded initial conditions (expected no), and whether a joint electric/magnetic detector can robustly reconstruct all three pole locations. No physically unique Cone coupling is yet certified.
