# Rotating reflected-Larmor current: exact Fourier sidebands and limits of quasistatic inertia

Date 2026-10-25. Parents v14.870-871. Side-lane gravity/bicone, additive only.

## Exact current and linearization [D, conditional charged-blob model]
Take opposite Gaussian blobs qσ=σq, rσ(t)=c(t,ξ)+σR ξ xhat with c=R sqrt(1-ξ²)(0,cos Ω_L t,sin Ω_L t), ξ=δ/u. Charge density in Fourier convention ρ(k)=∫dr e^-ikr ρ(r):
ρ(k,t)=-2i q exp(-a²k²/2) exp[-ik·c(t,ξ)] sin(kx R ξ).
Current J(k,t)=exp(-a²k²/2)Σσ σq rdotσ e^-ik rσ
=2q exp(-a²k²/2) exp[-ik·c(t,ξ)] [R ξdot cos(kx R ξ) xhat - i cdot(t,ξ) sin(kx R ξ)].
These obey dotρ - i k·J = 0 with convention ∂tρ+∇·J=0 → dotρ+i k·J=0 (thus verify dotρ+i k·J=0). At first order ξ, c=c0+O(ξ²) and J(k,t)=2q R exp(-a²k²/2) exp[-ik·c0(t)] [ξdot xhat - i ξ kx v0(t)] +O(ξ²) (the parity of source makes next order odd, normally O(ξ³), but ξdot scaling assumed first order).
Dipole p=2qRξ xhat exact and has no rotation of its direction. Its far-field electric dipole radiative term is P_E1=(2qR/u)² δddot²/(6π ε0c³); pure Ω sidebands at leading E1 order do NOT occur without δ(t) frequency content. At finite kR, the rotating phase e^-ik⊥R cos(Ωt-φk) expands in Bessel harmonics Σ_n(-i)^n J_n(k⊥R)e^{in(Ωt-φk)} (depending convention for signed azimuth). A seat Fourier mode at ω therefore contributes currents at ω+nΩ_L, with J also carrying Ω harmonics. The radiative/near-field Maxwell Green function has transverse denominator k²-[(ω+nΩ_L+i0)/c]²; the effective δ quadratic response under periodic drive is a Floquet kernel rather than one universal scalar frequency-independent mass. Sideband strength is suppressed by powers of kR for kR≪1 and determined by finite source and frequency.

## Finite-rotation magnetic dipole [D]
At fixed ξ with common circular v0 and source charges ±q, m=(1/2)Σ qσ rσ×rdotσ=qR ξ xhat×v0= -q R² ξ Ω_L (0,cosΩ_L t,sinΩ_L t). Magnitude qR²|ξ|Ω_L, and radiates at magnetic-dipole order for Ω≠0 and ξ≠0, with P_M1=μ0 |mddot|²/(6πc³)=μ0 q²R⁴ξ²Ω_L^6/(6πc³) for constant ξ in magnetic dipole approximation. Electric quadrupole and other multipoles may contribute at comparable expansion order; P_M1 is NOT the complete radiation power. When ξ=0, the charge/current distributions cancel identically even though individual centers rotate.

## Inertia decision [D/O]
Previous v14.871 M_T=μ0(2qR/u)²/[6π^(3/2)a] arises only from frozen orbit/local quasistatic polarization current. Including finite Ω induces velocity-dependent longitudinal/transverse current, sideband mixing, dispersive reactive response and radiation. The positive field energy coefficient in the strict low-frequency frozen-orbit limit remains true there; no proof establishes that full frequency-dependent δ kernel has the same positive kinetic coefficient. A causal retarded Maxwell integration (including Gauss/Coulomb energy and mechanical supports) is still required for renormalized physical mass and stability. No intrinsic resonant mode follows solely from the externally fixed Ω_L and Maxwell vacuum: sidebands are not a binding-mode pole. Charges, regulator a, radius R, φ(t), and map δ/u are postulates; no common gravity seat coupling or Higgs particle derived.

Audit: check sign in Fourier continuity, parity of linearization, Bessel sidebands, magnetic dipole and missing higher-multipole caveat. No Suzuki/far-tail modifications.
