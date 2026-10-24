# Curvature and null cones of the k-factor product Hessian metric

2026-10-24. Gravity/combinatorics lane. Parents v14.818–819. No Suzuki or Lane A modifications.

## Metric and conformal form [D]

For k>=2, P=∏x_i=e^r, r=Σ log x_i, s_i=log x_i-r/k (Σs_i=0), the Cartesian Hessian tensor g=Hess_x P, pulled into these coordinates, is
\[
g=e^r\left(A\,dr^2-\sum_i ds_i^2\right),\qquad A=(k-1)/k.
\]
Choose any orthonormal Euclidean basis of the shape hyperplane Σs_i=0 and call its coordinates z_1,...,z_{k-1}. With t=sqrt(A)r,
\[
g=e^{t/\sqrt A}\left(dt^2-\sum_{\alpha=1}^{k-1}dz_\alpha^2\right)=e^{2\sigma}\eta,\quad \sigma=t/(2\sqrt A).
\]
This is an exact conformally flat Lorentzian metric, dimension k. The conformal factor is nonconstant.

## Ricci and scalar curvature [D]

In η-Minkowski coordinates, σ is linear and has constant timelike gradient with \(|\nabla\sigma|_\eta^2=1/(4A)\), \(\Box_\eta\sigma=0\). The standard conformal change identity gives
\[
\operatorname{Ric}_{ab}=(k-2)(\sigma_a\sigma_b-\eta_{ab}|\nabla\sigma|_\eta^2).
\]
Thus Ric_tt=0, Ric_{z_\alpha z_\beta}=(k-2)/(4A) δ_{\alpha\beta}, and
\[
\boxed{\mathcal R_k=-\frac{k(k-2)}4e^{-r}=-\frac{k(k-2)}{4P}}.
\]
At k=2, curvature vanishes (2D Riemann tensor entirely determined by scalar). For every k>2 scalar curvature is negative and nonzero. At k=4, R=-2/P, while Ricci has nonzero spatial components and vanishing tt component in these conformal coordinates. Therefore g is NOT Einstein with cosmological constant for k>2 (Ric not proportional to g), though it is conformally flat (Weyl=0 when k>=4). No claim of solution to Einstein's equations with a specified physical stress-energy tensor.

## Null cones and AM–GM equality [D]

A tangent increment is null iff
\[
\boxed{A(dr)^2=\sum_i(ds_i)^2}.
\]
For k=4, \(\sum_i(ds_i)^2=\tfrac34(dr)^2\), a 1+3 light cone in orthonormal shape coordinates. The conformal factor does not alter null directions. The locus of AM–GM equality is s_i=0 for all i, a timelike radial line, NOT the null cone or its boundary. For a common positive dilation x_i→h x_i, r→r+k log h while s_i fixed; curvature rescales as h^{-k}. This changes curvature numerically at corresponding points of a mathematically fixed metric, but does not determine the physical meaning of h or a coupling.

## Causal interpretation boundary [O]

This metric is a mathematically defined pseudo-Riemannian metric on positive factor space; it has curvature and local null cones but is not yet a GR spacetime model. A physical interpretation needs mapping factor coordinates to events, physical proper time, calibrated length, dynamics and stress tensor. In particular no Newton G is derived. The divisor-k product generating function and Suzuki/Weil carriers remain distinct.
