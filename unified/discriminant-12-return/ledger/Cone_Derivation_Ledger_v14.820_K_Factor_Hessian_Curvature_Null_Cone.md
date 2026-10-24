# Cone Derivation Ledger v14.820 — Curvature and null cones of the k-factor Hessian metric

Date 2026-10-24. Gravity/combinatorics lane. Parents v14.818–819. Research: research-notes/K_Factor_Hessian_Curvature_Null_Cone.md, commit 57f12387f3b6aa6695f6260e9277f4493833d060. Live prewrite HEAD 57f12387f3b6aa6695f6260e9277f4493833d060; next free v14.820. Additive-only; far-tail/Suzuki untouched.

## Conformal metric and scalar curvature [D]
Writing A=(k-1)/k and using radial coordinate r and orthonormal shape coordinates z_a, the product Hessian bilinear form is \(g=e^r(A\,dr^2-\sum_a dz_a^2)\). With \(t=\sqrt A\,r\), \(g=e^{t/\sqrt A}\eta\), conformally Minkowskian. The conformal factor's log \(\sigma=t/(2\sqrt A)\) has constant timelike η-gradient norm squared 1/(4A) and zero η-wave operator. Standard conformal Ricci formula yields \(\operatorname{Ric}_{tt}=0\) and \(\operatorname{Ric}_{ab}=(k-2)/(4A)\delta_{ab}\). Thus
\[
\boxed{\mathcal R_k=-\frac{k(k-2)}4e^{-r}=-\frac{k(k-2)}{4\prod x_i}}.
\]
At k=2 metric is flat; k>2 gives negative nonzero scalar curvature. For k=4, \(\mathcal R_4=-2/P\) and the metric has (1,3) signature. It is conformally flat but NOT an Einstein metric for k>2: Ricci is not proportional to g.

## Null geometry [D]
Null tangents satisfy \(A(dr)^2=\sum_i(ds_i)^2\); at k=4 the coefficient is 3/4. The AM–GM equality locus \(s_i=0\) is a timelike radial line, not the null hypersurface. Positive common factor dilation changes r by k log h and rescales scalar curvature by h^{-k} at mapped points; its physical meaning is not fixed.

## Guardrails and next gate [O]
The metric is a mathematical Hessian geometry on positive factor space. A GR model requires an independently specified correspondence to physical spacetime, appropriate source/stress-energy dynamics, time orientation and physical normalization; no Newton G derived. Divisor k-factor arithmetic remains distinct from Suzuki/Weil current under v13.770.

NEXT: compute Einstein tensor at k=4 and assess whether a plausible independently normalized stress tensor could support this metric; do not infer physical matter or G from pure geometry.

Flags: curvature_formula=EXACT; k2_flat=TRUE; k4_scalar_curvature=-2/P; k4_conformally_flat=TRUE; k4_not_Einstein=TRUE; physical_GR_map=OPEN; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-curvature-inertia-verification
parent: v14.820
status: open
action: Independently verify conformal Ricci and scalar curvature, k=2 versus k=4, null tangent equation, and AM–GM equality locus. Preserve physical and arithmetic-carrier guardrails.
deliverable: scoped mathematical audit verdict.
