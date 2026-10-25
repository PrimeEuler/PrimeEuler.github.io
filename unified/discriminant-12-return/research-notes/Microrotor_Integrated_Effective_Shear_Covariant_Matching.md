# Integrating out pendulum microrotations: effective shear and covariant matching

Date 2026-10-24. Gravity subgate, parents v14.626, v14.827–830. Protected Suzuki/far-tail untouched.

## Exact Gaussian elimination [D]
From v14.829 the micropolar quadratic action contains \(\gamma|\nabla\times u-2\theta|^2/2+K|\theta|^2/2+A|\nabla\theta|^2/2\), plus shear \(\mu_0|\mathrm{dev}\,e|^2\), inertia j, and bulk term. In a spatial Fourier mode q and frequency ω, the Euler–Lagrange equation for θ is
\[
[4\gamma+K+Aq^2-j\omega^2]\theta=2\gamma(\nabla\times u).
\]
Away from resonant denominators, substituting back gives the frequency/wavenumber dependent rotational contribution
\[
\boxed{\gamma_{\rm rot}(\omega,q)=\gamma\,{K+Aq^2-j\omega^2\over 4\gamma+K+Aq^2-j\omega^2}}.
\]
The effective curl term is \(\gamma_{\rm rot}|\nabla\times u|^2/2\); it is nonlocal in spacetime once rotations propagate. In the static/adiabatic limit ω→0 and q→0 with 4γ+K>0,
\[
\boxed{\mu_{\rm eff}=\mu_0+{\gamma K\over4\gamma+K}}
\]
for transverse shear waves, according to the v14.829 normalization. At K=0 rotational relaxation removes the added q=0 shear contribution, while K→∞ freezes orientation and adds γ. γrot(ω,q) must NOT be interpreted as a stable instantaneous modulus near an optical mode pole.

## Matching to v14.830 (conditional, not a physical derivation) [D/O]
That covariant model's shear modulus is \(\mu_{\rm cov}=2D\rho/(3C)\); thus equating local, quasistatic isotropic shear stiffnesses implies
\[
{% raw %}\boxed{{D\over C}={3\over2\rho}\left(\mu_0+{\gamma K\over4\gamma+K}\right)}{% endraw %}.
\]
For its previously stated local stable causal window 1/4≤D/C≤1, the necessary conditional matching requirement is
\[
\boxed{\rho/6\le\mu_0+{\gamma K\over4\gamma+K}\le2\rho/3}.
\]
Example in consistent units: choose μ0=ρ/4, γ=ρ/2, K=2ρ (so γK/(4γ+K)=ρ/4). Then μeff=ρ/2, D/C=3/4; the covariant local speeds would be cT²=3/4, cL²=2/3. These are chosen coefficients, not predicted.

## Critical constitutive distinction [O]
A standard micropolar solid's quadratic curl energy is not automatically the same as the isotropic *symmetric-strain* shear invariant q of the relativistic solid. Even if a single transverse plane-wave dispersion maps μeff, the complete tensor constitutive operator, longitudinal response and covariant stress-tensor matching can differ, including terms involving solid-body rotations. A true isotropic matching requires deriving/engineering the full strain response and background energy density from the rotor microphysics. K=M g_local l itself depends on an external gravitational field, cannot determine Newton G, and can violate independent universality tests. For perturbations with wavelengths near microstructure or frequencies near rotational resonance, derivative expansion fails and one must retain θ dynamically.

## Outcome
The rotor calculation supplies an algebraically explicit tunable effective shear stiffness; there is no intrinsic stiffness ratio selection from the factor Cone. Need independent microphysical values and a symmetry/continuum map to GR. No Suzuki/Weil arithmetic carrier claim.
