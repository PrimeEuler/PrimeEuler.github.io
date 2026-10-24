# Cone Derivation Ledger v14.822 — Covariant fluid action admits four-factor Hessian geometry

Date 2026-10-24. Gravity/combinatorics lane. Parents v14.818–821. Research note research-notes/Four_Factor_Covariant_Fluid_Action_Selection_Test.md (commit 13232542fa4102dd567e4ac518e2471b0248797c). Live prewrite HEAD 13232542fa4102dd567e4ac518e2471b0248797c; next ledger v14.822. Additive only; Suzuki/far-residual untouched.

## Covariant on-shell construction [D]

Signature +---, Λ=0. Introduce three scalar fields φ^I and B^{IJ}=-g^{μν}∂_μφ^I∂_νφ^J, b=sqrt(det B)>0. The covariant action
\[
S=(2κ)^{-1}\int\sqrt{-g}R\,d⁴x-C\int\sqrt{-g}b^{2/3}\,d⁴x,\qquad κ,C>0
\]
admits the homogeneous configuration φ^I=z^I and flat-FLRW g=dτ²-a(τ)²d\mathbf z². There b=a^{-3}, ρ=C/a² and p=-ρ/3. The material-scalar equations hold by spatial homogeneity; Einstein's equations give \(3H²=κC/a²,\ \ddot a=0\). An expanding solution is \(a(τ)=\sqrt{κC/3}(τ-τ_0)\). With τ_0=0 and κC=1, this exactly matches the factor Hessian FLRW metric of v14.821.

## Selection obstruction [D/O]

This is a covariant **existence construction**, not a uniqueness/selection theorem. The chosen fluid power b^(2/3) engineers w=-1/3, and κC=1 is an imposed parameter match. The equations do not force \(g=\nabla^2(\prod_i x_i)\) or supply a dynamical map from arithmetic factor variables to physical spacetime. The Einstein coupling κ was inserted, not derived. No physical cosmology or Newton G follows without new independently constrained structure.

NEXT: seek a factor-field variational principle selecting the Hessian metric and predict parameter ratios without fitting the source exponent/normalization. Existing arithmetic carrier separation v13.770 remains.

Flags: covariant_action_exists=TRUE; full_FLRW_on_shell=EXACT; rho_scaling=a^-2; fluid_w=-1/3; Hessian_metric_selected=FALSE; Newton_G_derived=FALSE; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: gravity-covariant-action-variation
parent: v14.822
status: open
action: Independently vary scalar-label fluid action and Einstein term; check matter equations, signs of rho and p, flat Friedmann solution, and whether κC=1 is solely parameter matching. Preserve Suzuki/far-tail.
deliverable: scoped mathematical audit verdict.
