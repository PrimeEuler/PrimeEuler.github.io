# Fixed-product divisor shell Lorentzian test and causal-cone distinction

Date 2026-10-24. Gravity/combinatorics lane; parents v13.770, v14.784, v14.807. [D] exact combinatorics and quadratic geometry; [O] physical identification.

## Canonical shell homogenization and obstruction [D]

For integer N>=1 let
\[
F_N(X,Y,Z)=\sum_{ab=N,\ a,b\ge1}X^aY^bZ^{N+1-a-b}.
\]
Every exponent is nonnegative since (a-1)(b-1)>=0 implies a+b<=ab+1=N+1. Thus F_N is homogeneous of degree N+1 with positive coefficients and has precisely d(N) monomials, one per ordered factor pair. This is one explicitly declared canonical homogenization, not uniquely selected by arithmetic.

For any N>=3, support contains u=(1,N,0), v=(N,1,0). The M-convex exchange axiom applied to i=Y (where u_Y>v_Y) and j=X (where u_X<v_X) would require u-e_Y+e_X=(2,N-1,0) in support. This would demand 2(N-1)=N, possible only N=2. For N>=3 it is absent. Hence support(F_N) is not M-convex and F_N is not Lorentzian in the standard homogeneous nonnegative-coefficient Lorentzian-polynomial class.

At N=3, F_3=XY³+X³Y; its nonzero second derivative in Y is 6XY, but support exchange already fails. The key obstruction is support gaps, not simply one Hessian eigenvalue of f=xy.

At N=2, F_2=XY²+X²Y has adjacent supports and satisfies the degree-three Hessian tests: ∂_X F=Y²+2XY, ∂_Y F=X²+2XY, whose Hessian matrices each have one positive and one negative eigenvalue; its support is M-convex. N=1 gives F_1=XYZ^0=XY. Therefore the direct fixed-shell construction passes N=1,2 and fails all N>=3.

This result does not rule out OTHER encodings of factor pairs or weighted/augmented shell polynomials possessing a Lorentzian structure.

## Hyperbolicity versus physical causality [D/O]

The quadratic polynomial Q(T,X)=T²-X² is hyperbolic in the time direction e=(1,0): for any v, t↦Q(v+te) has real roots t=-v_T±|v_X|. The associated future hyperbolicity cone is \(\{T>|X|\}\). On the x,y>0 quadrant, T=(x+y)/2, X=(x-y)/2, so T>|X| holds exactly.

For any Lorentzian metric g at a spacetime point, its tangent-space causal cone has the corresponding one-time-direction quadratic form after choosing a local orthonormal frame. This establishes local algebraic analogy for 1+1 quadratic cones. It does NOT provide a metric field on a physical spacetime, a coordinate-independent global mapping from combinatorial exponents to tangent vectors, Einstein curvature, a gravitational source equation, or Newton's G. The Hessian in polynomial coefficient/exponent variables and the spacetime metric tensor are different data.

## Next tests [O]

Find a product-shell encoding with naturally M-convex support (if one exists without discarding divisor contacts), and independently identify a dynamical metric/connection whose tangent cones are transported covariantly from Cone variables. Preserve v13.770 arithmetic-carrier distinction; no Suzuki production changes.
