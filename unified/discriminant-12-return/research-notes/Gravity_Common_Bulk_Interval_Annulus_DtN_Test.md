# Gravity common-bulk integration: interval versus annulus

Date 2026-10-23. Gravity lane. Parents v14.773–779. Scope: exact quadratic effective models, NOT identified with actual EM and gravitational propagating actions. No Suzuki/far-tail computation.

## Gate A. Integrate one common bulk field on an interval [D]

A real scalar phase lift θ(s) (near zero phase; compact target S¹) on [0,L] has
\[
E[\theta]=\frac{K}{2}\int_0^L(\partial_s\theta)^2\,ds,\quad K>0,\quad \theta(0)=0,\quad\theta(L)=\Theta.
\]
The unique energy-minimizing lift of zero winding is \(\theta_{\rm cl}(s)=\Theta s/L\). With \(\theta=\theta_{\rm cl}+\eta\), \(\eta(0)=\eta(L)=0\), the cross term vanishes and
\[
E[\theta]=\frac{K}{2L}\Theta^2+\frac K2\int_0^L(\eta')^2ds.
\]
Consequently integrating fluctuations contributes a Θ-independent Gaussian determinant (assuming common measure/regularization), while the effective boundary stiffness is
\[
\boxed{k_{\rm bdy}=K/L}.
\]
Adding source \(-j\sin\Theta\) gives local susceptibility \(\chi=L/K\).

For two channels with a common bulk coefficient K, if they traverse physical lengths \(L_E,L_G\),
\[
\boxed{\chi_G/\chi_E=L_G/L_E}.
\]
An assumed half *length* \(L_G=L_E/2\) gives 1/2, not 4. An assumed common physical length yields equality. The factor is not selected by action topology.

## Gate B. Integrate the same field on an annulus [D]

For a radially symmetric phase θ(r) on Euclidean annulus \(a<r<b\) (r is proper radius in a flat plane), define
\[
E[\theta]=\frac K2\int_a^b\int_0^{2\pi}|\nabla\theta|^2 r\,d\phi\,dr,\quad \theta(a)=0,\ \theta(b)=\Theta.
\]
Its unique radial harmonic solution is
\[
\theta_{\rm cl}(r)=\Theta\,\frac{\log(r/a)}{\log(b/a)}.
\]
The bulk on-shell energy and resulting boundary stiffness are
\[
\boxed{E_{\rm on-shell}(\Theta)=\frac{\pi K}{\log(b/a)}\Theta^2,\quad
k_{\rm ann}=\frac{2\pi K}{\log(b/a)}}.
\]
For two channels with common K and radius ratios \(\rho_E=b_E/a_E\) and \(\rho_G=b_G/a_G\),
\[
\boxed{\chi_G/\chi_E=\log\rho_G/\log\rho_E}.
\]
A *simultaneous* rescaling of BOTH radii in a sector by 1/2 keeps \(\rho\) and stiffness unchanged: conformal scale invariance defeats any assertion that half-grid radius alone forces a different response.

If only the inner radius is halved while the outer radius is fixed, the ratio becomes \(\log(2\rho_E)/\log\rho_E\), which depends on the free annulus aspect ratio and is not universally 2 or 4. This distinction matters: which boundary is fixed is physical input.

## Gate C. Topological consistency and limits [D/O]

For compact θ, specify the lift/winding sector. Near Θ=0, the zero-winding sector above determines the local Hessian. On the annulus, nonzero angular windings θ(φ)=mφ can add an independent energy proportional to \(\pi K m^2\log(b/a)\); this does not eliminate K and requires appropriate topology/branch treatment. A one-loop functional determinant may depend on geometry and regularization but, for the Gaussian fixed-boundary theory, does not introduce a Θ-dependent correction to the classical Hessian.

A common coefficient K truly removes independent *bulk* coefficient freedom, but boundary embedding lengths, aspect ratios, source normalization, geometry and possible nonminimal boundary terms still need derivation. In particular there is no forced \(\kappa_G/\kappa_E\) = 1/4, nor a derivation of Newton G.

## Next falsifiable selector [O]

Derive from Cone geometry plus an independently specified physical action (i) the two actual bulk domains or operator domains, (ii) source normalization for one common boundary probe, and (iii) the pair-grid-to-domain mapping. Compute the Dirichlet-to-Neumann map and see if it selects a sector-invariant ratio. Demonstrate robustness under common rescaling and boundary condition changes. The current scalar-field models are exact examples, not physical EM/GR equivalences.
