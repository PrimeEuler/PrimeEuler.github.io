# Factor-field variational selection: explicit countermodel and signature hazard
Date 2026-10-24. Gravity lane; parents v14.818–822. No Suzuki/far-tail modifications.

## Scalar factor action and equations [D]
Let M be a four-dimensional Lorentzian spacetime, four positive scalar fields X^A:M→(0,∞), target tensor K_AB(X) symmetric and nondegenerate, potential V(P), P=∏_A X^A. Consider
\[
S[g,X]=\int_M\sqrt{-g}\left[\frac{R}{2\kappa}-\frac12 K_{AB}(X)g^{\mu\nu}\partial_\mu X^A\partial_\nu X^B-V(P(X))\right]d^4x .
\]
The factor Euler–Lagrange equations are
\[
\nabla_\mu(K_{AB}\partial^\mu X^B)
-\tfrac12(\partial_A K_{BC})\partial_\mu X^B\partial^\mu X^C
-\partial_A V=0
\]
with sign convention of the displayed action (a common overall sign change of the scalar part leaves the field equations unchanged). Thus the scalar wave-map equations depend on K and V, and **do not impose** \(g_{\mu\nu}=\partial_\mu\partial_\nu P\), which in any case has indices on factor target space, not spacetime. A pullback proposal \(g_{\mu\nu}=H_{AB}(X)\partial_\mu X^A\partial_\nu X^B\) would be an additional field constraint, not a consequence of a generic scalar action.

Counterexample: take K_AB=δ_AB and V(P)=λ(P-P_0)^2 with λ>0 and P_0>0. Choose constant positive X^A with product P_0. All factor equations hold; matter stress tensor vanishes, and Minkowski g solves Einstein's equation with Λ=0. Hence even an AM–GM/product-dependent covariant action and dynamical positive factors do not select the curved four-factor Hessian geometry. This establishes nonuniqueness of the broad proposal, not a no-go against every specially designed action.

## Naive target-Hessian kinetics have ghosts [D]
For P=∏X^A, \(H_{AB}=\partial_A\partial_B P\) has inertia (1,3) on X>0. If one sets K_AB=H_AB as the scalar kinetic target, perturbations about constant positive X_0 on Minkowski yield a kinetic quadratic form with one sign opposed to three others. For either overall kinetic-sign choice, at least one scalar kinetic mode has the wrong sign: a ghost in an unconstrained, ordinary second-order scalar theory. This is a signature-level obstruction to using the Lorentzian product Hessian *naively as a healthy material target metric*. Gauge constraints or a genuinely different action might evade it, but must be exhibited explicitly.

## Chain-rule and spacetime metric issue [D/O]
For spacetime-dependent factors, \(\partial_\mu\partial_\nu P(X)\) is not generally diffeomorphism covariant; moreover
\[
\partial_\mu\partial_\nu P(X)
=H_{AB}(X)\partial_\mu X^A\partial_\nu X^B
+(\partial_A P)\partial_\mu\partial_\nu X^A
\]
in a chosen coordinate chart. A target Hessian and a spacetime metric are distinct; an intrinsic pullback tensor uses first derivatives, \(h_{\mu\nu}=H_{AB}\partial_\mu X^A\partial_\nu X^B\), requiring rank-four map for nondegeneracy. If one enforces g=h through a Lagrange multiplier, it is an imposed metric identity and no longer an independent emergent selection; moreover stability/constraint counting must be established.

## Decision [D/O]
Product Hessian and AM–GM alone do not specify target kinetic metric, potential, measure, constraints, or coupling κ. Concrete dynamics show many alternatives; direct target-Hessian scalar kinetics are indefinite. The stronger path is seek a symmetry or constrained vierbein formulation with a well-defined positive-energy physical sector and independently derived source normalization. No G claimed.
