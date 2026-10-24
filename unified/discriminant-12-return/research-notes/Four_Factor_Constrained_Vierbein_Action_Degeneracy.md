# Constrained vierbein realization of the four-factor Hessian Cone: explicit construction and no-dynamics obstruction

Date 2026-10-24. Gravity lane; parents v14.818–824. Standalone conditional toy action. Protected Suzuki/far-tail untouched.

## Covariant factor coframe

Take four positive spacetime scalar fields X^A(x)>0 with nondegenerate Jacobian and P(X)=∏_{A=1}^4 X^A. Let r(X)=Σ_A log X^A and s_A(X)=log X^A-r/4. Choose an arbitrary constant orthonormal basis E^i_A of the three-plane Σs_A=0, i=1,2,3, so z^i=Σ_A E^i_A s_A. Define the one-form coframe
\[
e^0=\frac{\sqrt3}{2}e^{r/2}\,dr,\qquad e^i=e^{r/2}\,dz^i,
\]
with differential taken on spacetime after substituting scalar fields X(x). It is a diffeomorphism-covariant coframe and locally invertible if det(∂_μX^A)≠0. Define \(h_{\mu\nu}(X)=\eta_{ab}e^a_\mu e^b_\nu\), η=diag(1,-1,-1,-1). Then \(h_{\mu\nu}=H_{AB}(X)\partial_\mu X^A\partial_\nu X^B\), where H_AB=∂_A∂_B P. The metric h has exactly the previously derived curvature \(\mathcal R=-2/P\), provided the factor map is a local diffeomorphism.

## Lagrange-multiplier action and field equations

Take independent spacetime metric g and a symmetric tensor multiplier Λ^{μν}. Add three independent matter-label scalars φ^I and B^{IJ}=-g^{μν}∂_μφ^I∂_νφ^J, b=√det B. On the admissible domain P>0, b>0, det(∂X)≠0, set
\[
S[g,X,\Lambda,\phi]=\int d^4x\sqrt{-g}\left[\frac{R(g)}{2\kappa}-C b^{2/3}+\frac12\Lambda^{\mu\nu}(g_{\mu\nu}-h_{\mu\nu}(X))\right].
\]
Varying Λ imposes \(g=h(X)\) exactly. On the branch Λ=0, metric variation reduces to Einstein equations for the independent fluid; X variation of the metric-constraint term vanishes, since X appears nowhere else. In coordinates (τ,z^i) induced by X, τ=√3e^{r/2}, the induced metric is g=dτ²-(τ²/3)d\mathbf z². Choose φ^I=z^I; this solves the fluid-label equations. For κC=1 the Einstein-fluid equations hold and hence the full constrained action has this explicit on-shell branch (g=h, Λ=0, φ=z, κC=1). Parameter κC=1 is fitted, not predicted.

## Degree-of-freedom and ghost assessment

This construction DOES force the Hessian metric, but solely because a Lagrange multiplier imposes it. It does not dynamically select the form from unconstrained factor-field Euler–Lagrange equations. There is no independent sigma-model kinetic term \(H_{AB}g^{\mu\nu}\partial_\mu X^A\partial_\nu X^B\), so the immediate indefinite sigma-model kinetic Hessian/ghost of v14.823 has not been introduced. However, since rank(∂X)=4, locally the X scalars can be used as coordinates, and g=h(X) is then a fixed FLRW metric, leaving **no independent local gravitational metric perturbations**. Consequently the model has no demonstrated healthy propagating gravitons or empirical GR limit. Constraint multiplier fluctuations and full Hamiltonian stability have not been analyzed; do not assert universal ghost freedom.

The coframe is not automatically torsion-free as a Cartan connection: Levi-Civita spin connection can be solved from e; do not confuse de^a≠0 with torsion of that connection. The internal orthonormal shape basis choice is an O(3) rotation only and does not affect h.

## Decisive result and next gate

The constrained construction is mathematically coherent at the on-shell level, and exposes a tradeoff: enforce the Hessian geometry exactly -> gravitational dynamics are eliminated locally; leave g independent -> ordinary product fields do not select it, and a naive Hessian scalar target has ghosts. The needed advance is a weaker, justified constraint or action selecting a *family* of causal geometries with propagating healthy spin-2 degrees, not a rigid pullback metric.

No physical G, EM/G ratio, or Suzuki divisor-carrier identity is established.
