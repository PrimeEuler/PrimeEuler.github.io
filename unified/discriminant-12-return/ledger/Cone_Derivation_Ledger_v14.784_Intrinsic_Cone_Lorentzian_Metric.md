# Cone Derivation Ledger v14.784 — Intrinsic Cone metric and boundary-operator signature gate

Date: 2026-10-23. Gravity lane. Parents v13.748, v14.768, v14.773, v14.780–783. Research note: research-notes/Gravity_Cone_Intrinsic_Metric_and_Boundary_Operator.md, commit de0fcd200b40e2d61c559e3c7bfef3f9e2de06fb. Prewrite HEAD de0fcd200b40e2d61c559e3c7bfef3f9e2de06fb. Additive only; Suzuki far-tail and certified payloads untouched.

## Intrinsic factor Cone signature [D]

For x,y>0, write Y=sqrt(xy), β=(1/2)log(x/y), r=log(xy), and T=(x+y)/2, X=(x-y)/2. Then T=Y coshβ, X=Y sinhβ and T²-X²=Y². The pullback of the natural quadratic form is
\[
\boxed{dx\,dy=dT²-dX²=dY²-Y²dβ²=e^r(dr²/4-dβ²)}.
\]
This metric is Lorentzian. It does not by itself give the positive-definite elliptic Dirichlet-to-Neumann operator used in v14.781–783. Those hyperbolic-plane scalar calculations are internally exact but require an independently chosen physical metric, action, or justified continuation before application to the original Cone.

## Optional positive metric is a separate dynamical choice [D]

The Euclidean factor-quadrant form dx²+dy² pulls back to
\[
e^r[(\cosh(2β)/2)dr²+2\sinh(2β)\,dr\,dβ+2\cosh(2β)dβ²].
\]
Alternatively choosing the Riemannian polar form g_+=dY²+Y²dβ² (not inherited from dxdy) gives, on u=log Y=r/2, the conformal strip metric du²+dβ². For fixed boundaries u_i,u_o, and **additionally assumed** periodic β with period B, a massless scalar bulk with coefficient K has zero-mode boundary stiffness
\[
\boxed{k_+=KB/(u_o-u_i)=2KB/(r_o-r_i)}.
\]
Thus a uniform half-grid dilation sends r→r-log4 while leaving the radial width invariant if both walls scale together, and the conditional strip stiffness remains unchanged. A boundary fixed independently changes the response only through a specified relative wall.

## Selection and causal guardrail [O]

The intrinsic Cone's Lorentzian metric calls for a well-posed causal field problem, including physical source and boundary conditions, not automatic elliptic continuation. Its metric alone does not select K, a unique causal Green function, EM/G sector embedding, or Newton's G. The unit-circle and quarter-vertex correspondences remain arithmetic/kinematic until a field action fixes these choices. v13.770 arithmetic-carrier mismatch respected.

Flags: Cone_metric_signature=LORENTZIAN_EXACT; hyperbolic_plane_metric_not_intrinsic=TRUE; optional_positive_strip_stiffness=EXACT_CONDITIONAL; half_grid_common_dilation_no_stiffness_ratio=EXACT_CONDITIONAL; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-metric-and-boundary-operator-check
parent: v14.784
status: open
action: Independently verify the metric pullbacks, positivity/signature distinction, conformal-strip stiffness and the inability to infer a physical elliptic operator from the Lorentzian Cone. Preserve Suzuki/far-tail.
deliverable: scoped verification.
