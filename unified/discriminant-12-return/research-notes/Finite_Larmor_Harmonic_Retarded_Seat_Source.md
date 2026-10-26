# Finite-Larmor retarded seat: conserved harmonic source and exact spectral reduction

Date 2026-10-25. Parents v14.871–878. Additive gravity/bicone lane, Suzuki and far-tail untouched.

## Input and conventions
Gaussian f_a(k)=exp(-a² k²/2); g=2qR/u; c(t)=R(0,cosΩt,sinΩt), v(t)=dc/dt; ξ=δ/u. To first order δ,
rho1(k,t)=-i g kx f_a e^-ik·c(t) δ(t),
J1(k,t)=g f_a e^-ik·c(t)[δdot(t) ex -i kx v(t)δ(t)].
Continuity dot rho+i k·J=0 exactly. Source is model-dependent and neutral.

For δ(t)=δω exp(-iωt), define b_n(k)=Ω/(2π) ∫_0^(2π/Ω) dt exp(i nΩt) exp[-ik·c(t)], and d_n(k)=Ω/(2π)∫dt exp(i nΩt) exp[-ik·c(t)] v(t). Then source contains channels at ω+nΩ with
rho_n(k)=-i g kx f_a δω b_{-n}(k)
J_n(k)=g f_a δω[-iω ex b_{-n}(k)-i kx d_{-n}(k)].
Equivalent reindexing n→-n is harmless. Fourier continuity channel by channel imposes -i(ω+nΩ)rho_n+i k·J_n=0. The coefficients are expressible through ordinary Bessel functions, including velocity harmonics (nearest-neighbor Bessel shifts). Square-integrable Gaussian envelope ensures convergence of angular and radial integrals for every finite width a>0 at real frequencies away from light-cone pole, using retarded prescription.

## Crucial symmetry [D]
For exact circular motion about x and a scalar seat δ, the combined time shift plus rigid space rotation is a symmetry of the SOURCE and isotropic vacuum Maxwell propagator. After integrating over full k angles the quadratic δ kernel is stationary K(t,t')=K(t-t'). The harmonics ω+nΩ are INTERNAL electromagnetic radiation/virtual-field channels of a single δ input ω. A Floquet off-diagonal seat-frequency matrix is not forced unless lab-fixed anisotropy, external drive, or additional coordinate breaks helical symmetry.

## Spectral consequence [D, formal]
Retarded transverse photon spectral support in nth harmonic occurs at |k|=|ω+nΩ|/c; longitudinal/Coulomb contribution remains instantaneous. Therefore the imaginary part of the retarded seat self-energy is controlled by sideband radiation through (ω+nΩ) channels. Unlike the frozen-orbit response, the dimensionless pole equation depends on α=Ωa/c and β=R/a, plus any source/support dynamics. In particular, α=0 gives the old frozen-orbit kernel for arbitrary β (a fixed common offset translates source without changing Maxwell response). For finite α the pole shift cannot be deduced from the positive equal-time magnetic ENERGY term of v14.877: it is not the same as a retarded equation-of-motion stiffness.

## Open computational gate
Construct the full finite-Ω response with consistent Coulomb and transverse parts (including velocity sidebands), evaluate a converged Bessel/momentum decomposition, and numerically continue the causal sheet's complex poles from z0≈0.4108337143730426−0.1700926343728676i at α=0 over specified α,β. Check harmonic cutoff and k-integration accuracy. No finite-Ω pole value or stability certificate is claimed by this note. External support and source mechanics may alter pole structure. No physical G, Higgs, or real charged monopole derived.
