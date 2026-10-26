# Circular-Larmor helical symmetry: diagonal scalar seat response, corrected Floquet interpretation

Date 2026-10-25. Parents v14.872–874 and v14.877. Additive note, correcting interpretations, Suzuki/far-tail untouched.

## Exact symmetry [D]
Given neutral equal-shape Gaussian charge blobs at rσ(t;ξ)=R_x(Ω t)[(σRξ),R sqrt(1−ξ²),0] (where R_x rotates only yz), with qσ=σq and a scalar seat history ξ(t)=δ(t)/u, define density rho and vector current J via moving blobs. For arbitrary ξ(t), under joint time shift τ and spatial rotation R_x(Ωτ),
rho_{ξ(·+τ)}(r,t)=rho_{ξ}(R_x(Ωτ)r,t+τ), with time argument choices adjusted consistently; equivalently the trajectory functional has covariance rσ[ξ(·+τ)](t)=R_x(-Ωτ)rσ[ξ](t+τ). The exact essential relation is rσ(t+τ; ξ_const)=R_x(Ωτ)rσ(t; ξ_const), and for arbitrary δ path the sources transform covariantly under δ'(t)=δ(t+τ).
The electromagnetic vacuum action and Gaussian profile f_a(|r|), plus Coulomb-gauge transverse projector P_T(k)=I-khat khat, are invariant under simultaneous spatial rotations. The reduced action S_eff[δ] after Maxwell integration is time-translation invariant (provided there is no external laboratory anisotropy, boundaries, additional static field, non-rotating support, and Ω is prescribed constant). Thus its Hessian K(t,t') around δ=0 depends only t−t'. In scalar Fourier space K(ω,ω')∝δ(ω−ω'), i.e., no *off-diagonal Floquet* mixing among scalar δ frequency channels.

This is a correction/refinement to v14.872–873: individual k-resolved sources e^-ik·c(t) possess sidebands ω+nΩ, but after integration over all isotropic k and sum over vector components, angular momentum conservation makes them contribute to the same total scalar seat frequency diagonal. There can be frequency shifts, sideband thresholds and radiation channels at ω+nΩ in the scalar kernel's spectral integral; this does NOT require K_nm off-diagonal.

An anisotropic environment, lab-fixed magnetic drive axis transverse to the symmetry rotation, noncircular motion, or independently dynamical drive phases can break joint symmetry and restore genuine Floquet mixing. Caveat: prescribed rotation is held externally; its energy supply and support dynamics remain outside the reduced Maxwell calculation. The finite Ω diagonal kernel has not been numerically integrated to identify the pole shift or prove absence of upper-half-plane poles. This result only establishes an exact selection/diagonalization rule. Need independent audit of the helical symmetry under external rotating-drive coupling.

## Additional check [D]
Static Coulomb seat curvature in this isotropic Gaussian model is invariant under common spatial translation and rotation; it remains kE=g²/(24π^(3/2)ε0 a³), independent of Ω for every instantaneous configuration at δ=0. Quasistatic transverse magnetic energy adds order (ΩR/c)² under v perpendicular x (v14.877), but this equal-time field energy must not be directly identified with the retarded dynamical force.

Decision: exact scalar time-stationarity given helical symmetry, but physical finite-Ω resonance UNCALCULATED. No G/Higgs inference.
