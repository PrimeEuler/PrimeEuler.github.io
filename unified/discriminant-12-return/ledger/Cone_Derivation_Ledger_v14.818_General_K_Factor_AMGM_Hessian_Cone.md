# Cone Derivation Ledger v14.818 — General k-factor AM–GM Hessian Cone

Date: 2026-10-24. Gravity/combinatorics lane. Parents v13.748, v13.770, v14.767, v14.784, v14.807–811, v14.814–817. Research note: research-notes/General_K_Factor_AMGM_Hessian_Cone.md, commit 1fd8ea9f49a494b5a4f49d294072c04016c4adb3. Live HEAD before write: 1fd8ea9f49a494b5a4f49d294072c04016c4adb3. Confirmed latest numbered ledger v14.817; v14.818 unoccupied. Additive only; Lane A and Suzuki far-residual payloads untouched.

## General AM–GM factor Cone [D]

For k>=2, x_i>0, P_k=∏x_i, the AM–GM inequality reads \(\frac1k\sum x_i\ge (P_k)^{1/k}\). Define \(u_i=\log x_i\), \(r=\sum u_i\), \(s_i=u_i-r/k\), \(\sum s_i=0\). There is one radial and k-1 independent shape coordinates; \(P_k=e^r\).

## Hessian inertia and the radial/shape identity [D]

Writing D=diag(x_i), J=the k×k all-ones matrix, the Cartesian Hessian satisfies
\[
\boxed{\nabla_x^2 P_k=P_kD^{-1}(J-I)D^{-1}}.
\]
Because J-I has eigenvalues k-1 and -1 (multiplicity k-1), Sylvester's law of inertia gives signature (1,k-1) at every point in the positive orthant. For tangent vectors expressed by \(du_i=dx_i/x_i\),
\[
\boxed{dx^\mathsf{T}\nabla_x^2P_k\,dx
=P_k\bigg[\frac{k-1}{k}dr^2-\sum_i ds_i^2\bigg]}.
\]
This is the *pullback of the Cartesian Hessian bilinear form*. It must NOT be confused with the u-coordinate second-derivative matrix of \(P_k(e^u)=e^r\), which is the rank-one positive semidefinite matrix \(e^rJ\). Hessians do not transform tensorially under nonlinear variable substitutions.

At k=2 the metric has inertia (1,1), and at k=4 inertia (1,3). This is an algebraic/pseudo-Riemannian factor-space signature, not a derivation of a physical GR spacetime metric or source equation.

## Arithmetic k-factor shells [D]

For ordered tuples \(a_1\cdots a_k=N\), the count \(d_k(N)\) obeys \(\sum_{N\ge1}d_k(N)N^{-s}=\zeta(s)^k\), \(\Re s>1\). At uniform grid scale h, \(r_h(N)=\log(h^kN)\). Thus unit-to-half-grid radial translation is \(-k\log2\), equal to \(-\log4\) at k=2 and \(-\log16\) at k=4. These are exact shell-coordinate statements, not physical coupling predictions.

## Next gate [O]

Compute the curvature and null cone of the Hessian metric on factor space, and test any proposed relation to AM–GM equality or physical causal cones. A physical GR identification needs an independently justified spacetime/metric/action map. v13.770's divisor versus Suzuki/Weil carrier separation remains mandatory.

Flags: k_factor_AMGM=EXACT; product_Hessian_inertia=(1,k-1)_EXACT; coordinate_pullback_not_composite_Hessian=EXPLICIT; k4_signature=(1,3); physical_GR_intertwiner=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: combinatorics-gravity-hessian-check
parent: v14.818
status: open
action: Independently derive the Cartesian Hessian, its inertia, the logarithmic radial/shape pullback (distinguish it from composite Hessian), and k-factor Dirichlet series. Check the -k log2 shift and physical-scoping guardrails.
deliverable: scoped audit verdict without Suzuki/far-tail edits.
