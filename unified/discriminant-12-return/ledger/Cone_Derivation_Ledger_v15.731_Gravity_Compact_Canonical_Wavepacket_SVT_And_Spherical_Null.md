# Cone Derivation Ledger v15.731 — Gravity: spatially compact canonical scalar initial source excites all three stress helicities; exact spherical null

**Date:** 2026-11-11 US Eastern. **Parents:** physical canonical minimally coupled scalar source v15.727, pressure-corrected Ward and scalar-to-Weyl transfer v15.728–729, exact two-wave but nonlocalized scalar matter Weyl benchmark v15.730, preceding signed Fourier stress/cosmological K4 SVT v15.716–725. **Status:** [D] smooth spatially compact matter initial data with positive local canonical energy density, explicit nonzero *initial Fourier source* in S,V,T; [D] spherical-symmetry TT/V Fourier projector no-go; [O] actual retarded K4 metric/tidal response of the compact source and full T/V mode amplitudes. **Immediately prewrite HEAD:** f0a7a13b50dbd0e43b2b5c8738c1322b488e4ac3; target ledger path absent; additive only, Suzuki protected.

## Gate 368 — spherical compact scalar pulses are TT/V-dark even though their local 2/3 stress norm is nonzero

For canonical real scalar matter with smooth radially symmetric compact initial chi and chi_dot, background coasting FLRW and KG evolution preserve spatial SO(3) symmetry. Its stress Fourier tensor at any K !=0 must be of the form

**T_ij(K)=A(|K|)delta_ij+B(|K|) Khat_i Khat_j**.

The transverse TT projector and vector shear projector about K annihilate this tensor exactly:

**TT[K](T)=0**, **V[K](T)=0**.

This includes any spherical compact positive-energy scalar wavepacket, despite its locally nonzero anisotropic dyad and universal **Pi_ij Pi_ij=(2/3)|grad chi|⁴**. The global Fourier source polarization—not a pointwise STF norm—determines which SVT waves may be excited. This is a conventional rotational-symmetry selection rule, not an exotic Cone no-go.

## Gate 369 — construct asymmetric compact canonical matter initial data

At a Cauchy slice tau0=1 take the explicit real compact initial data

**chi_0(x,y,z)=w_R(x,y,z)[cos(2x)+cos(z)]**,

**chi_dot_0=-chi_0**,

where the product cutoff is

**w_R(x,y,z)=h(x/R)h(y/R)h(z/R)**,

**h(u)=(1-u²)^8** for |u|<1 and zero outside. This is globally **C^7**, supported on [-R,R]^3, and has finite nonnegative canonical scalar energy. The well-posed massless KG Cauchy equation on coasting FLRW evolves these data and propagates support at finite speed (v15.727); this gate needs only the exactly specified initial stress.

Its coordinate spatial anisotropic stress is proportional to **grad chi_0 grad chi_0^T**, whose Fourier transform at K=(2,0,1) is computed by finite three-dimensional Gauss–Legendre quadrature. Take R=16 and 96 quadrature nodes per coordinate, and normalize by **I0=∫w_R² d³x**. Tracefree K-projector decomposition gives nonzero squared Frobenius norms

**norm(TT)^2 ≈ 0.0800000017144**,

**norm(V)^2 ≈ 0.1799999944213**,

**norm(S)^2 ≈ 0.2399999998302**.

The values agree to quadrature accuracy with the limiting two-wave cross-stress values **32/(25·16)=0.08, 72/(25·16)=0.18, 96/(25·16)=0.24** computed at v15.727/730. The compact cutoff's derivatives are included in the *actual* integrand, not discarded. The source is continuous and finite-energy, not a global plane wave.

## Gate 370 — why the large-support limit is controlled

At each fixed coordinate inside the large support, w_R approaches a constant at the local wave scale, so the dominant *resonant* Fourier stress at K=p+q is the two-wave cross dyad **-(p q^T+q p^T)/4**. The cutoff-gradient contributions are suppressed by 1/R and nonresonant oscillatory integrals by Fourier decay of the compact bump. Normalization by I0 removes the extensive volume factor. This supports the nonzero finite-R numerical witness, but a general physical matter wavepacket spectrum must be evolved before making claims about detector frequencies.

**Positive:** an explicit **spatially compact, positive-local-energy matter initial configuration** can have nonzero T/V/S stress Fourier projections simultaneously. **Negative:** pointwise rank-two 2/3 does not protect TT/V against spherical symmetry; the three source projector norms still do not establish any *gravitational detector* Weyl response. The source's spatial compactness is separate from the earlier globally finite-duration signed Fourier pulse assumption (v15.724/725).

**Reproducer:** research-notes/k4_compact_scalar_svt_v15_731.py, additive commit f0a7a13b50dbd0e43b2b5c8738c1322b488e4ac3. Locally checked at R=16/96 nodes, including exact spherical null and nonzero finite compact initial-stress Fourier S/V/T projections. No image generation or historical edits.

**HANDOFF:** audit/gauge constraints: independently check the compact cutoff's finite regularity and derivatives, Fourier normalizations, tensor/vector/scalar projection conventions for arbitrary K, and the spherical SO(3) null. Recognize that the plotted or numerical source is *initial data* and the K4 full retarded curvature from this compact matter is still open.

**NEXT:** use these actual compact Cauchy data at tau=1 to compute Fourier coefficients of rho, P_trace, T^(0parallel), and its time derivative using the canonical KG equation. Insert those coefficients into the pressure-corrected K4 source-first scalar constraint and metric transfer to obtain a **spatially compact, physical-matter-generated nonzero electric Weyl** at the initial slice; compare its normalized amplitude against the exact v15.730 plane-wave value 83/120. Then propagate the resulting source spectrum and K4 constraints retarded in cosmic time.
