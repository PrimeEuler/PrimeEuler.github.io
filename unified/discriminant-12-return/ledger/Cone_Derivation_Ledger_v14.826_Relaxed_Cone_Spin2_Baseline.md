# Cone Derivation Ledger v14.826 — Relaxed Cone background with propagating spin-2 modes

Date 2026-10-24. Gravity lane. Parents v14.821–825. Research note research-notes/Cone_Relaxed_Spin2_Tensor_Baseline.md, commit 3beb61dd3fcf33999e446cbc7ff9b447728ba1ad. Live HEAD before write 3beb61dd3fcf33999e446cbc7ff9b447728ba1ad. Additive only, Suzuki/far residual untouched.

## Tensor baseline [D]
Remove exact metric multiplier g=h(X) from v14.825. Einstein + three-label fluid action \(S=\int\sqrt{-g}[R/(2\kappa)-Cb^{2/3}]\,d⁴x\) admits the Cone-isometric background \(ds²=d\tau²-(\tau²/3)d\mathbf z²\) with κC=1 and label fields φ^I=z^I. Factor coordinates are reference data, not metric-selecting dynamical fields.

For transverse-traceless perturbations, \(g_{ij}=-a²(\delta_{ij}+\gamma_{ij})\), \(a=\tau/\sqrt3\), the quadratic spin-2 action is
\[
S_{TT}^{(2)}=(8\kappa)^{-1}\int d\tau\,d³z\,a³[\dot\gamma_{ij}²-a^{-2}(\partial_k\gamma_{ij})²].
\]
It has two positive-energy kinetic tensor polarizations for κ>0 and standard luminal principal symbol; \(\ddot\gamma+3H\dot\gamma-a^{-2}\nabla²\gamma=0\). In conformal time, μ=aγ and a'/a=c=sqrt(κC/3) lead to \(\mu_q''+(q²-c²)\mu_q=0\). Thus tensor gravity is no longer frozen.

## Necessary viability caveat [O]
This baseline does not derive the Cone from a unique field action: setting background g=h(X) is a selected solution, not a field equation. Moreover the barotropic perfect fluid has adiabatic \(c_s²=dp/d\rho=-1/3\), indicating a scalar/longitudinal gradient instability in the simplest fluid realization. Therefore only the TT kinetic/principal-sector test is passed; the **full system is not certified healthy**. κ remains independent and Newton G is not predicted.

NEXT: independently derive scalar perturbation energy and dispersion and seek a stabilized medium (e.g., shear-rigid or multi-component action) without changing background tensor equations or hiding an input coupling.

Flags: spin2_modes_propagate=YES; TT_kinetic_positive_if_kappa_positive=TRUE; cone_metric_selected_dynamically=NO; fluid_scalar_gradient_stability=LIKELY_FAIL_NEEDS_AUDIT; full_ghost_free=NOT_ESTABLISHED; G_derived=false; Suzuki_payloads_touched=false; far_tail_touched=false.

HANDOFF
target: external-audit
type: gravity-relaxed-tensor-and-scalar-stability
parent: v14.826
status: open
action: Verify tensor quadratic action, conformal-time equation, and scalar fluid c_s²=-1/3 instability warning; distinguish healthy tensor sector from full-theory viability.
deliverable: scoped independent verdict, no Suzuki/far-tail changes.
