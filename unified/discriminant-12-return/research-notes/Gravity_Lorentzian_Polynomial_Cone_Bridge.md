# Lorentzian polynomial / Cone metric bridge: exact scope

Date: 2026-10-24. Gravity-combinatorics lane. Parents v13.748, v13.770, v14.766–768, v14.784–785. Independent of the reserved Suzuki production chain.

## Signature of the base factor polynomial [D]

Take \(f(x,y)=xy\), \(x,y>0\). Its Hessian is
\[
\nabla^2 f=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
with eigenvalues \(+1,-1\). With \(T=(x+y)/2,\ X=(x-y)/2\), \(f=T^2-X^2\). The bilinear form \(dx\,dy=dT^2-dX^2\) is the polarization of the same quadratic shape (its Hessian is twice the associated metric matrix). Thus the simplest Cone factor-product polynomial has the one-positive-direction Hessian property of degree-two Lorentzian polynomials, and its positive-factor domain lies in a hyperbolicity cone.

CAUTION: the Euclidean geometry of a polynomial's coefficient space and the Lorentzian metric of a spacetime are *different objects*. The Hessian of f is flat and fixed; neither a dynamical spacetime metric nor an Einstein field equation follows from this identity. The metric dxdy on the factor quadrant is Lorentzian but not a general relativistic gravitational field.

## Product monomial family [D]

For integers a,b≥1 and d=a+b, let \(f_{a,b}=x^ay^b\). The Hessian determinant is
\[
\det\nabla^2 f_{a,b}=ab(1-d)x^{2a-2}y^{2b-2}<0.
\]
Consequently it has one positive and one negative eigenvalue everywhere on the positive quadrant. Every nonzero (d-2)-fold partial derivative is a nonnegative multiple of x², xy, or y²; each has a Hessian with at most one positive eigenvalue. Thus each monomial is Lorentzian in the standard homogeneous nonnegative-coefficient definition (allowing boundary supports). This is a rigorous family of combinatorial Lorentzian polynomial building blocks.

## A divisor frontier is not automatically a Lorentzian polynomial [D/O]

The arithmetic set \(S_N=\{(a,b)\in\mathbb Z_{>0}^2:ab\le N\}\) encodes \(D(N)=|S_N|\), but the naïve bivariate generating polynomial \(P_N(x,y)=\sum_{ab\le N}x^ay^b\) is not homogeneous. Homogenizing to a fixed total degree and preserving coefficient normalization is a nontrivial modeling choice; the Lorentzian polynomial property is *not* stable under arbitrary sums of Lorentzian monomials. Therefore no claim is made that P_N is Lorentzian or that log-concavity of d(n) follows. In fact d(n) is not generally log-concave: d(2)^2=4 < d(1)d(3)=2 is false; instead a genuine counterexample is d(3)^2=4 < d(2)d(4)=2*3=6. 

A direct candidate for further testing is a homogeneous polynomial encoding fixed-product shells, with explicit normalization and a quadratic derivative test on every degree-two derivative. A failure is meaningful and would distinguish the Cone's local Lorentzian signature from global arithmetic Lorentzian polynomial structure.

## Physical separation [O]

To reach GR one needs a specified spacetime metric field, connection, curvature and field equation; a Hessian signature on generating functions does not determine Einstein curvature or G. A possible rigorous bridge would use an explicitly defined action or geometric map transporting a polynomial's hyperbolicity cone into physically calibrated causal cones, proving covariance and source dynamics. No such map is currently derived.

Flags: base_xy_signature=EXACT; positive_monomials_Lorentzian=EXACT; divisor_global_Lorentzian=NOT_ESTABLISHED; GR_field_equations=NOT_DERIVED; G_derived=false; Suzuki/far-tail untouched.
