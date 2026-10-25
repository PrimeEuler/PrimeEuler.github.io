# Retarded Maxwell seat kernel: positive balanced electrostatic curvature, causal inertia, and pole test

Date 2026-10-25. Parents v14.870–872. Additive gravity/bicone note. No Suzuki/far-tail changes.

## Source and assumptions
Take the explicitly posited neutral Gaussian blob source of v14.871–872. To isolate the local response, freeze the common Larmor orbital center, retaining first-order seat coordinate δ. Set g=2qR/u and f_a(k)=exp(-a² k²/2). The exact source to first order is rho(k,t)=-i g kx δ(t) f_a(k), J(k,t)=g δdot(t) f_a(k) xhat. It satisfies dot rho+i k·J=0. Full moving-circle Floquet response is separately described below, and should NOT be replaced with frozen-orbit result at finite Ω_L.

## Static electrostatic curvature [D]
Coulomb energy at coincident neutral source, as a function of infinitesimal δ:
U_C=(1/(2 ε0))∫d³k/(2π)³ |rho(k)|²/k²
= g² δ²/(2 ε0) ∫d³k/(2π)³ (kx²/k²)exp(-a²k²)
= g² δ²/(48π^(3/2) ε0 a³).
Therefore k_C=d²U_C/dδ²=g²/(24π^(3/2) ε0 a³)>0.
This is a **different equilibrium** from v14.870 where the + and - charges are separated at ℓ0>0 and U''=-2C/ℓ0³<0. Here opposite equal Gaussian charge blobs coincide at δ=0, their total rho=J=0 there, and separation creates a costly dipole field. Total electrostatic energy as function of separation is positive and minimum at complete cancellation. The coincidence physically requires two independently interpenetrating regulated distributions; do not extrapolate to elementary particles or rigid impermeable charges.

## Retarded transverse kernel [D]
In Coulomb gauge, integrate Maxwell transverse vector potential using retarded Green function:
M_T(z)=μ0g² ∫d³k/(2π)³ exp(-a² k²) (1-kx²/k²) / [k²-(z/c)²],
with Im z>0 as analytic retarded continuation (real z boundary ω+i0). Angular reduction:
M_T(z)=μ0g²/(3π²)∫_0∞ dk k² exp(-a²k²)/[k²-(z/c)²].
At z=0: M_T(0)=μ0g²/(6π^(3/2)a), agreeing v14.871. For real ω>0, Im M_T(ω+i0)=μ0g² ω exp[-(aω/c)²]/(6π c). This positive spectral part of retarded kernel induces radiation (for the Fourier convention e^-iωt, the dynamical force contribution is +ω² M_T(ω)δ; the inverse-response denominator is k_C-ω² M_T(ω)). In the long-wavelength regime aω/c<<1, the imaginary part yields dipole reaction factor -i [g²/(6π ε0c³)]ω³ in inverse-response denominator, consistent with dissipative power P=g² δddot²/(6π ε0c³) for arbitrary motion. Strictly, source supports and other fields needed for complete conservative+reactive mechanical model.

Closed form for Im z>0 with w=z/c:
M_T(z)=μ0g²/(3π²) [sqrtπ/(2a) + (iπ w/2)exp(-a²w²)erfc(-iaw)].
The entire Gaussian regularized retarded kernel is analytic in upper half-plane; this follows from analytic integral continuation. No acausal advanced prescription used.

## Pole and resonance test [D/O]
Naively combining only calculated k_C and frozen field inertia M_T(0) would predict omega_naive²=k_C/M_T(0)=c²/(4a²). But this lies at omega_naive a/c=1/2, OUTSIDE a parametrically controlled low-frequency (aω/c<<1) expansion. Therefore it is NOT a certified low-energy mode. Exact retarded denominator k_C-ω² M_T(ω) may have complex zeros; to call one a physical resonance requires consistent inclusion of all Coulomb/transverse fields, source mechanics, constraint support and finite Ω Floquet mixing. Vacuum Maxwell retarded continuum and an externally specified rotating trajectory do not by themselves prove a stable intrinsic bicone eigenmode.

## Retain full Larmor phase [D as formal kernel]
At finite Ω_L the O(δ) current Fourier component is, with c(t)=R(0,cosΩ_L t,sinΩ_L t), v=cdot,
rho1(k,t)= -i g kx f_a(k)e^-ik·c(t) δ(t);
J1(k,t)=g f_a(k)e^-ik·c(t)[ δdot(t) xhat - i kx v(t) δ(t)].
Continuity dot rho1+i k·J1=0 exactly because dot e^-ikc = -i(k·v)e^-ikc. Maxwell retarded D_T(k,t-t') coupled to J1_T(k,t), and instantaneous Coulomb rho1/rho1, produce a periodic time-dependent quadratic seat kernel K(t,t') with period 2π/Ω_L in both time arguments. Its Floquet matrix K_nm(ω) mixes ω+nΩ_L channels. There is no unique scalar M(ω) for finite Ω without diagonalizing this matrix; nonzero Ω correction was not integrated numerically here. Distinguish formal exact representation from a completed Floquet pole computation.

## Verdict
Positive k_C and causal positive M_T(0) for *regulated overlapping neutral seat model*; inertia and stiffness source-model dependent, with normalized u-invariant values. A low-energy intrinsic resonance, stable physical inertial mass, electromagnetic charged monopole, gravitational coupling, or Higgs identification is not established. Next gate could use dimensionless numerical retarded pole search for frozen model, then full finite Ω matrix using explicit source profile and support constraints.
