# Covariant action test for the four-factor Hessian Cone FLRW source

Date: 2026-10-24. Parents v14.818–821. Gravity-only note, separate from Suzuki/far-tail.

## Constructive covariant source action [D]

Adopt metric signature (+---), cosmological constant Λ=0. Introduce three scalar material coordinates φ^I, I=1,2,3, define
\[
B^{IJ}=-g^{\mu\nu}\partial_\mu\phi^I\partial_\nu\phi^J,\quad b=\sqrt{\det B},
\]
on configurations where the spatial-gradient Gram matrix B is positive definite. Consider
\[
S=\frac1{2\kappa}\int d^4x\sqrt{-g}\,R
-\int d^4x\sqrt{-g}\,C\,b^{2/3},\quad C>0.
\]
This is a diffeomorphism-invariant perfect-fluid (comoving scalar) action, with internal volume-preserving relabeling symmetry. Here κ is inserted independently; it is not obtained from AM–GM combinatorics.

On spatially-flat FLRW \(ds²=d\tau²-a(\tau)^2\delta_{ij}dz^idz^j\), use \(\phi^I=z^I\). Then \(B^{IJ}=a^{-2}\delta^{IJ}\), \(b=a^{-3}\). The energy density is \(\rho=C b^{2/3}=C/a²\) and pressure \(p=bF'(b)-F(b)=-\rho/3\), where F(b)=Cb^{2/3}. The matter-field equations hold for this homogeneous comoving configuration (spatial divergences vanish). The Einstein equation \(3H²=\kappa\rho\) gives \(\dot a²=\kappa C/3\), hence an expanding branch
\[
a(\tau)=\sqrt{\kappa C/3}\,(\tau-\tau_0).
\]
Choosing \(\tau_0=0,\ \kappa C=1\) gives precisely \(a(\tau)=\tau/\sqrt3\), the Hessian-derived metric of v14.821 in its fixed z-coordinate normalization. The acceleration equation is consistent: \(\rho+3p=0\), hence \(\ddot a=0\).

## What this does and does not derive [D/O]

This action gives a fully covariant on-shell realization of the *already selected* FLRW Hessian geometry, including the effective w=-1/3 fluid and its scalar-label equations. It does NOT derive the product Hessian ansatz \(g_{\mu\nu}=\partial_\mu\partial_\nu(\prod_i x_i)\) as a compulsory field solution. The three material scalar fields are chosen to realize an isotropic comoving medium; the fractional-power exponent 2/3 was chosen to give the target equation of state rather than deduced from the divisor lattice. Requiring κC=1 is parameter matching, not an emergent G derivation. Other fluid exponents produce different w and different cosmologies.

An actual selection theorem needs a separately motivated action for factor fields \(x_i\), a covariant map into physical spacetime fields with dynamical constraints selecting the Hessian, and an independent coupling prediction rather than fitting C against κ.

No assertion the scalar material fluid represents our universe; no Suzuki/Weil carrier identification.
