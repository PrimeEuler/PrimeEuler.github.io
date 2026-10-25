# Micropolar full constitutive test, objectivity, and rotor relaxation

2026-10-24. Gravity side lane. Parents v14.826–832 (Round 348 audit verified 829–831). No Suzuki/far-tail writes.

## Gate I. Constitutive comparison by rigid rotation [D]

The model of v14.829 uses \(e=\mathrm{sym}\nabla u\), \(c=\mathrm{curl}u\) and potential
\[
W=\frac B2(\mathrm{div}u)^2+\mu_0|\mathrm{dev}e|^2+\frac\gamma2|c-2\theta|^2+\frac K2|\theta|^2+\frac A2|\nabla\theta|^2.
\]
For a pure infinitesimal rigid rotation \(u=\Omega\times x\), one has \(e=0,\ \mathrm{div}u=0,\ c=2\Omega\). With uniform microrotation \(\theta\), minimize \(W=2\gamma|\Omega-\theta|^2+(K/2)|\theta|^2\). Stationarity gives \(\theta=4\gamma\Omega/(4\gamma+K)\) and
\[
\boxed{W_{\rm rigid,min}=\frac{2\gamma K}{4\gamma+K}|\Omega|^2}.
\]
This is nonzero for \(\gamma K>0\), despite vanishing symmetric strain. Accordingly the rotor-generated curl stiffness is not an objective *classical isotropic shear modulus*. It presupposes an external orientation reference, appropriate to gravity-pinched pendulums, and it cannot be inserted into the covariant solid's q-invariant response as an equality of full constitutive tensors. The test concerns locally Euclidean small strains, not a demand that the initial gravity-pinned system be frame indifferent without including its external field.

## Gate II. Objective free-rotor limit [D]

Set K=0. Under a simultaneous rigid body rotation \(u=\Omega\times x,\ \theta=\Omega\), the first-order strain/curl coupling and the microrotation gradient cost both vanish, as required by superposed-rigid-rotation covariance of a free micropolar material.

For a Fourier mode (ω,q), eliminate theta, obtaining
\[
\gamma_{\rm rot}(\omega,q)=\gamma\frac{Aq^2-j\omega^2}{4\gamma+Aq^2-j\omega^2}.
\]
At ω=0, q→0, gamma_rot≈Aq²/4 (if γ>0); thus its elastic energy is O(q⁴|u_T|²), a higher-gradient correction. It contributes NO nonzero zero-frequency q² transverse shear at leading order. The material's leading shear modulus is μ0. If A=0 also, the static rotor responds exactly to curl u, removing all extra curl stiffness in the static limit.

## Gate III. Relativistic matching verdict [D/O]

If one wants the classical symmetric-strain relativistic-solid shear μ_cov=2Dρ/(3C), the objective long-wave limit of this specific local model permits only \(μ_{\mathrm{cov}}=μ_0\), and then \(D/C=3μ_0/(2ρ)\), provided an independent covariant coarse-graining still exists. The candidate local causal interval becomes \(ρ/6≤μ_0≤2ρ/3\). Gravity-pinning K>0 can modify transverse-wave stiffness in a preferred frame, but changes the constitutive class (adds orientation response); it does NOT supply a general shear stabilization mechanism of the exact isotropic q-solid claimed in v14.830.

Longitudinal displacement still has \(\omega_L²=(B+4μ_0/3)q²/ρ_m\), independent of gamma,K,A, so rotor coupling alone cannot repair negative longitudinal modulus. To obtain nontrivial objective long-wave shear from rotors, add a separately justified strain–rotation coupling with physically correct transformation properties or derive μ0 microscopically. Those are new assumptions and require audit.

This is an obstruction to full constitutive identification for the *specified micropolar action*, not a universal no-go theorem for rotational media. No Newton G derived.
