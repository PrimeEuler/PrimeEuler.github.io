# Cone Derivation Ledger v14.760 — Gravity selector: minimum variational model and symmetry no-go

**Date:** 2026-10-23 EDT. **Lane:** dedicated gravity. **Parents:** v14.696, v14.731–739, v14.759. **User directive:** focus on finding/modeling the selector, while keeping Suzuki sandbox entirely reserved. **Live HEAD before write:** \`14c9531a7ad1e6a80ed5f0f13d072979ffc62547\`; v14.760 confirmed free. No Suzuki/far-tail or paper writes.
**Research deposit:** \`research-notes/Gravity_Selector_Minimal_Variational_Model.md\`.

## Exact conditional selector [D]

For the nonzero gravitational quantization rung \(q_n=|n|/4\), the constituent positive couplings can be written \(\alpha_{1,2}=q_ne^{\pm\psi}\), a continuous split at fixed pair product. Consider the explicit test effective functional
\[
U(\psi)=q_n^2(ae^{2\psi}+be^{-2\psi}),\qquad a,b>0.
\]
It has unique global minimum
\[
\boxed{\psi_*=\tfrac14\ln(b/a)},\quad U''(\psi_*)=8q_n^2\sqrt{ab}>0.
\]
Thus a physically computed, asymmetric pair of positive action costs **could** select the split. However a=b forces ψ=0. Under more general strictly convex exchange-symmetric energy \(U(\psi)=U(-\psi)\), the unique minimum also lies at ψ=0. To get ψ≈45 in this simplest quadratic-cost model requires b/a≈exp(180)≈1.49×10^78. Inserting that coefficient ratio by hand is restating, not solving, the hierarchy. No coefficient derivation from radial mismatch, monopole lattice, or deposited EFT exists yet. A nonconvex symmetric potential can create ± nonzero minima, but then the scale of displacement remains a new model parameter unless independently determined.

**Critical distinction:** the split of the two gravitational-pair charges is not automatically the ratio between independently defined EM and gravitational elementary couplings. Predicting \(\alpha/\alpha_G(\mu)\) requires an additional cross-sector matching law and independently supplied physical mass/coupling units; v14.731's common angular worldline core alone does not furnish this.

## Decision / next gates

Model viability is algebraically established; **physical selector remains OPEN**. Next gravity-only tests are to derive a and b or a nonlinear U from properly regularized source/boundary actions, test whether the effective cost is finite and diffeomorphism/gauge independent, and find a non-circular prediction. Revisit separatrix logarithm v14.696 only with a *dynamically fixed* initial eccentricity or boundary condition: the log cannot supply its own seat.

**Flags:** \`conditional_variational_selector=EXACT\`; \`physical_coefficients=NOT_DERIVED\`; \`symmetric_convex_hierarchy=NO_GO\`; \`EM_G_coupling_hierarchy=NOT_DERIVED\`; \`G_derived=false\`; \`new_sandbox_handoff=false\`; \`Suzuki_compute_reserved=true\`; \`far_tail_touched=false\`.
