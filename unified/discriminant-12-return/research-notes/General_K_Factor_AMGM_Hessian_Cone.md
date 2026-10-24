# General k-factor AM–GM Hessian Cone: radial/shape splitting

Date 2026-10-24. Gravity/combinatorics lane. Parents v13.748, v14.767, v14.784, v14.807–811, v14.814–817. Mathematical extension only; Suzuki/far residual untouched.

## Product, variables and AM–GM [D]
For k>=2 and x_i>0 define P_k(x)=∏_{i=1}^k x_i. AM–GM gives (Σx_i)/k >= (P_k)^(1/k), equality iff all x_i equal. Set u_i=log x_i, r=Σu_i, s_i=u_i-r/k, so Σs_i=0 and x_i=exp(r/k+s_i). Thus r is logarithmic product and s lies in a (k-1)-dimensional shape subspace.

## Exact Hessian metric [D]
Let D=diag(x_i) and J the all-ones k×k matrix. The Hessian has off-diagonals P_k/(x_i x_j), zero diagonals, so
\[
H=\nabla_x^2 P_k=P_k D^{-1}(J-I)D^{-1}.
\]
By Sylvester's law of inertia, H has one positive and k-1 negative eigenvalues for all positive x. At x_i=1 these are k-1 and -1 (multiplicity k-1); away from the diagonal the eigenvalues vary but inertia does not.

For any tangent increment dx, write du_i=dx_i/x_i, dr=Σdu_i, ds_i=du_i-dr/k. The *pullback bilinear form*
\[
g_H(dx,dx)=dx^T H dx=P_k[(Σdu_i)^2-Σdu_i^2]
=P_k\left[\frac{k-1}{k}dr^2-\sum_i ds_i^2\right].
\]
The shape sum has one linear constraint, and hence signature (1,k-1). In particular k=4 has algebraic Lorentzian inertia (1,3).

This is NOT the Hessian of the composite P_k(e^u)=e^r in u coordinates: that Hessian is e^r J, positive semidefinite rank one. Hessians are not tensors under nonlinear coordinate substitution; one must clearly distinguish the x-Hessian metric pullback from the u-Hessian.

## Factor tuples and arithmetic [D]
For positive integer a_i with ∏a_i=N, the ordered k-fold factor count is d_k(N), and
\[
\sum_{N>=1}d_k(N)N^{-s}=\zeta(s)^k,\quad\Re s>1.
\]
For uniform grid step h, x_i=ha_i implies r_h(N)=log(h^kN). A common half-step h=1/2 translates r by -k log2, yielding -log4 at k=2 and -log16 at k=4. This is a factor count/coordinate scaling, not a derived physical force or coupling.

## Geometry/physics boundary [O]
The Hessian form defines a Lorentzian pseudo-Riemannian metric on positive factor space, but no physical map to a 3+1 GR spacetime, no Einstein dynamics, no Newton G, and no identification of divisor tuples with Suzuki/Weil carrier follows from the common signature. The radial coordinate and Hessian metric must be treated as different objects from measured proper time/space without an independently established operational map.

Next: compute curvature of g_H, its null cone relative to AM–GM equality/shape subspace, and test whether it supplies genuinely new information beyond a coordinate/dilation analogy. Keep v13.770 and protected Suzuki lane constraints.
