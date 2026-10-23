# Gravity hyperbolic Cone bulk — radial and Fourier Dirichlet-to-Neumann gates

Date 2026-10-23. Gravity-only mathematical model. Parents v14.773–780. Geometry is a chosen constant-negative-curvature hyperbolic disk; not yet a derivation that physical EM or gravity occupies it.

## A. Hyperbolic annulus radial stiffness [D]
Consider the hyperbolic plane of curvature -1/ell² with metric
\[
ds^2=d\rho^2+\ell^2\sinh^2(\rho/\ell)d\phi^2,\quad0<\rho_i<\rho_o,\quad\phi\in[0,2\pi).
\]
For the common compact scalar zero-winding lift, use \(E=K/2\int|\nabla\theta|^2dA\), boundary \(\theta(\rho_i)=0,\theta(\rho_o)=\Theta\). Define
\[
t(\rho)=\log\tanh(\rho/(2\ell)),\quad
\Delta=t(\rho_o)-t(\rho_i)>0.
\]
Since \(dt/d\rho=[\ell\sinh(\rho/\ell)]^{-1}\), the radial harmonic minimizer is \(\theta=\Theta[t(\rho)-t(\rho_i)]/\Delta\) and
\[
E_{\rm eff}(\Theta)=\pi K\Theta^2/\Delta,\qquad
\boxed{k_0=2\pi K/\Delta}.
\]
A common scaling (\rho_i,\rho_o,\ell)\mapsto(\lambda\rho_i,\lambda\rho_o,\lambda\ell) leaves Δ and k_0 unchanged. Holding ell fixed and changing only radii can alter Δ: that is a physical change of domain, not a forced coupling relation.

## B. Full Fourier boundary operator [D]
In (t,phi) coordinates the hyperbolic annular metric is conformal to \(dt^2+d\phi^2\). Two-dimensional scalar Dirichlet energy is conformally invariant:
\[
E={K\over2}\int_{t_i}^{t_o}\int_0^{2\pi}[(\partial_t\theta)^2+(\partial_\phi\theta)^2]\,d\phi\,dt.
\]
For inner Dirichlet zero and arbitrary outer real lift \(f(\phi)=\sum_{m\in\mathbb Z}f_m e^{im\phi}\), the harmonic extension of m≠0 is
\[
\theta_m(t)=f_m{\sinh(|m|(t-t_i))\over\sinh(|m|\Delta)},
\]
while \(\theta_0(t)=f_0(t-t_i)/\Delta\). The on-shell energy is
\[
\boxed{E_{\rm eff}[f]=\pi K\sum_{m\in\mathbb Z}\lambda_m|f_m|^2},\quad
\lambda_0=1/\Delta,\quad\lambda_m=|m|\coth(|m|\Delta).
\]
This is the full angular Fourier Dirichlet-to-Neumann quadratic form in conformal-coordinate flux normalization. The *physical* normal derivative on outer wall is related by the positive conformal factor \(1/[\ell\sinh(\rho_o/\ell)]\). The zero-mode k_0 agrees with Gate A. For narrow Δ, λ_m~1/Δ+|m|²Δ/3; for broad Δ, nonzero λ_m→|m|, while λ_0→0.

## C. Why geometric shape does not uniquely select physics [D/O]
Even after fixing the hyperbolic metric and bulk K, optional local boundary terms are compatible with phase compactness; e.g. \(-u\cos f(\phi)\) produces a positive quadratic boundary Hessian u near f=0 if u>0. Different legitimate boundary actions/conditions therefore shift response without changing the bulk conformal annulus or topology. The cone needs independent physical boundary terms and a geometry-to-sector identification. No established map forces h_G=1/2 to a specific Δ_G or DN eigenvalue ratio.

In particular an assumed half-grid radial *coordinate* shift \(\rho\mapsto\rho-\ell\log2\) is not an isometry of the full metric and does not implement \(\rho\mapsto\rho/2\) in a universal way. Do not identify Cone product log r with hyperbolic proper radius without a derived metric map.

## Next
Find the actual Cone radial metric and sector boundary data from a physical action, and test whether normalized bulk coefficient and boundary terms are fixed by the unit-circle representation. Gauge symmetry alone constrains allowed terms; it does not fix their magnitudes. No G, α, force law, Suzuki/Weil trace equivalence claimed. Suzuki far-tail files untouched.
