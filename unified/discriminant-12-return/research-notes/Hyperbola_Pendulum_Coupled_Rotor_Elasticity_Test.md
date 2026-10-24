# Coupled hyperbola pendulum as a candidate shear medium: derivation and obstruction

2026-10-24. Gravity subgate. Parents v14.626, v14.821–826. All couplings here model parameters, not inferred from divisor geometry. No Suzuki/far-tail changes.

## I. Exact discrete rotor elasticity [D]
A cubic array of identical fiber rotors at sites n∈Z³, spacing ℓ>0, with angular deviations θ_n and inertia I>0 has quadratic energy/Lagrangian
\[
L=\sum_n \frac I2\dot θ_n^2-\frac K2 θ_n^2-\frac J2\sum_{\alpha=1}^3(θ_{n+\hat\alpha}-θ_n)^2,\quad K=M g_{\rm local}l>0,\ J>0.
\]
(The kinematic gravitational small-angle torsion potential K from v14.626 is an input; J is a *new* inter-rotor coupling.) Variation gives
\[
I\ddot θ_n+Kθ_n+J\sum_\alpha(2θ_n-θ_{n+\hat\alpha}-θ_{n-\hat\alpha})=0,
\]
with exact lattice dispersion
\[
\boxed{\omega²(\mathbf q)=K/I+(4J/I)\sum_\alpha \sin²(q_\alpha ℓ/2)}.
\]
Thus the lattice has a nonnegative harmonic energy and real linear frequencies for I,J,K>0, and at long wavelengths ω²=K/I+(Jℓ²/I)|q|²+O(q⁴). The scalar angular continuum action is \(\int d³x[(I/\ell³)\dot θ²/2-(K/\ell³)θ²/2-(J/\ell)|\nabla θ|²/2]\). Its gradient rigidity coefficient J/ℓ is exact to leading continuum order, but **is not automatically the macroscopic shear modulus**. One scalar rotor angle cannot furnish the three-dimensional elastic displacement field with longitudinal and transverse phonons.

## II. Explicit conditional displacement-locking shear [D/I]
Introduce *additional* constitutive kinematics for ONE transverse displacement polarization, θ_n=u_x(n)/ℓ. For a shear gradient along y, bond difference θ_{n+ŷ}-θ_n=(u_x(y+ℓ)-u_x(y))/ℓ ≈ ∂_yu_x=γ. One y-bond per site gives energy density \(W_{\rm shear}=(J/2\ell³)\gamma²\). Hence under this declared locking,
\[
\boxed{\mu_{\rm shear}=J/\ell³},
\qquad
\rho_{\rm inertial}=I/\ell^5,
\qquad
v_T²=\mu_{\rm shear}/\rho_{\rm inertial}=J\ell²/I.
\]
The onsite pendulum term becomes \(K u_x²/(2\ell^5)\): a pinning mass incompatible with a freely translation-invariant solid. It can be neglected in short-wave regimes or canceled by a separate symmetry, but no such protection follows from the pendulum alone. This single-polarization model is NOT an isotropic relativistic elastic solid. Achieving that needs a full 3-component displacement/director-locking model and symmetry-compatible strain energy. Gravitational coupling appearing in K cannot be promoted to a derived Newton coupling: local g_local is externally applied.

## III. Necessary relativistic scalar-stability target [D/O]
For a separately postulated isotropic relativistic elastic medium with background p=-ρ/3 and shear modulus μ, the standard locally isotropic speeds (units c=1) are
\[
c_T²=\mu/(\rho+p)=3\mu/(2\rho),\qquad
c_L²=dp/d\rho+4\mu/[3(\rho+p)]=-1/3+2\mu/\rho .
\]
Thus 0≤c_L²≤1 and 0≤c_T²≤1 require
\[
\boxed{\rho/6\le\mu\le 2\rho/3}
\]
for ρ>0, if the medium obeys the assumed standard constitutive description. The microscopic single-shear value μ=J/ℓ³ could satisfy this interval only if J is independently related to ρ and an isotropic relativistic completion is supplied. Neither the rotor potential nor AM–GM arithmetic fixes J/ρℓ³, so this is an inequality on model choices, not a prediction.

## IV. Outcome and next gate [O]
The older pendulum supplies an authentic local librational spring K and, with a new positive J, a stable coupled angular continuum. It does not inherently supply the shear elasticity needed for v14.826; added displacement locking and isotropic completion are necessary. Next derive rotational/translational coupled model with three component displacement fields and transverse/longitudinal spectra; verify no onsite pinning-induced violation of the intended translation symmetry. No physical GR selector or G derived.
