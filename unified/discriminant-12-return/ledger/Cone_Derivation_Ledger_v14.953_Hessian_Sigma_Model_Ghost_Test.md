# Cone Derivation Ledger v14.953 — Hessian sigma-model ghost obstruction and conserved reciprocal current

Date 2026-10-26. Parent v14.952 and v14.946–950. Research note research-notes/K2_Hessian_Sigma_Model_Ghost_Noether_Test.md commit 37c3701f36e992030002fa2959684121a1aec850. Prewrite live HEAD 37c3701f36e992030002fa2959684121a1aec850. Owner per-gate ledger, additive gravity only. Suzuki-quarter weld PARKED; independent Suzuki and far-tail files untouched.

[D/conditional action] Given original two-factor Hessian target metric h=2dρ²−2ρ²ds², explicitly choose standard generally covariant scalar sigma-model action S=∫√−g[1/2 h_AB g^μν ∂μφ^A ∂νφ^B−V(ρ)], with independent physical spacetime metric signature +---. This action is NOT fixed by AMGM on its own. Kinetic terms +(∂ρ)²−ρ²(∂s)²; the s fluctuation has negative time kinetic for ρ>0. Real regular field redefinitions preserve the one-negative target inertia, and a potential alone cannot cure high-frequency ghost. This is a ghost of *internal sigma model*, distinct from acceptable Lorentzian spacetime metric signature of K4.

[D] Reciprocal translation s→s+α is a Killing symmetry and gives explicit on-shell Noether current Jμ=−2ρ²∇μs, ∇μJμ=0. A conserved shift current does not imply bounded Hamiltonian or viable matter sector.

[O/repair] Freezing ρ alone keeps s ghost. To obtain healthy shape kinetic +ρ0²(∂s)² one must BOTH freeze ρ (or otherwise remove radial degree) and reverse shape sign, or use a different positive F(ρ) action (v14.946). These are model-building changes. Gauge/constraint quotient could avoid internal ghost only if a genuine constraint/gauge symmetry is derived; basic two-scalar sigma model has none. No Noether amplitude, Casimir quarter normalization, physical Einstein source or Newton G derived.

Flags: target_metric_hessian=EXACT; reciprocal_Killing_symmetry=EXACT; sigma_model_Noether_current=DERIVED_ON_SHELL; unconstrained_internal_ghost=PROVED; bare_Hessian_matter_healthy=FALSE; constraint_resolution=NOT_DERIVED; source_charge_fixed=FALSE; G_derived=FALSE; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: Hessian-sigma-model-ghost-and-Noether
parent: v14.953
status: open
action: Independently check kinetic sign and canonical Hamiltonian, shift current sign and conservation, difference between target-space ghost versus Lorentzian spacetime signature, and whether freezing rho alone fails to cure the ghost.
deliverable: scoped verdict.

NEXT: search for a geometrically justified first-class gauge constraint or a positive subspace target construction with fully explicit degree-of-freedom count, without arbitrary sign changes; await Sandbox full SVT separately.
