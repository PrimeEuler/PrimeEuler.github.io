# Cone Derivation Ledger v14.823 — Factor-field selection and Hessian kinetic-sign obstruction

Date 2026-10-24. Gravity lane. Parents v14.818–822. Research note research-notes/Factor_Field_Variational_Selection_And_Ghost_Test.md commit 0e8930c1674827a650af74965d0536a7d1a6b344. Prewrite live HEAD 0e8930c1674827a650af74965d0536a7d1a6b344. Additive only; Suzuki and far residual untouched.

## Covariant factor-field equations and counterexample [D]
Consider four positive scalar fields X^A with P(X)=∏X^A, and generally covariant action
\[
S=\int\sqrt{-g}\left[R/(2\kappa)-\tfrac12 K_{AB}(X)g^{\mu\nu}\partial_\mu X^A\partial_\nu X^B-V(P)\right]d^4x.
\]
Its factor equations are \(\nabla_\mu(K_{AB}\partial^\mu X^B)-\tfrac12(\partial_AK_{BC})\partial X^B\cdot\partial X^C-\partial_AV=0\). They do not generally impose \(g_{\mu\nu}=H_{AB}(X)\partial_\mu X^A\partial_\nu X^B\), with H_AB=∂_A∂_B P. Explicitly take K_AB=δ_AB, V=λ(P-P0)², λ,P0>0. Constant positive X with product P0 satisfies the factor equations, and Minkowski g satisfies Einstein's equations at Λ=0, with vanishing scalar stress. Thus the product-dependent action does NOT uniquely select the curved four-factor Hessian spacetime of v14.821–822. This is a counterexample to generic automatic selection, not a universal no-go theorem.

## Kinetic signature hazard [D]
The four-factor Hessian target H_AB has inertia (1,3). Taking K_AB=H_AB directly yields an indefinite time-derivative kinetic matrix for four unconstrained scalar perturbations about any positive constant background. For either global kinetic sign, at least one wrong-sign dynamical scalar mode appears. A healthy theory would require explicit constraints/gauge mechanisms removing such modes or another target tensor.

## Covariance boundary [D/O]
The composition Hessian ∂_μ∂_νP(X) is not a covariant spacetime tensor. The valid pullback candidate h_μν=H_AB(X)∂_μX^A∂_νX^B is a tensor (for scalar X^A), but equality g=h is an additional constraint, not selected by the generic action. Even if imposed, the sector stability and Einstein-source normalization remain independently open.

Flags: factor_scalar_EL=EXACT; Minkowski_countermodel=EXACT; naive_Hessian_target_ghosts=TRUE; metric_selection_from_generic_action=FALSE; physical_GR_intertwiner=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: factor-field-action-stability-review
parent: v14.823
status: open
action: Independently verify the factor-field Euler–Lagrange signs, Minkowski counterexample, inertia/ghost claim and covariant-pullback distinction; no Suzuki/far-tail modifications.
deliverable: scoped audit verdict.
