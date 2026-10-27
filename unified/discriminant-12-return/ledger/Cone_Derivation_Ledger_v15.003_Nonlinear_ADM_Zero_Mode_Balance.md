# Cone Derivation Ledger v15.003 — Full nonlinear ADM momentum zero-mode balance

Date 2026-10-27. Parent v15.002 and corrected ADM v14.996. Research note research-notes/K4_Nonlinear_ADM_Momentum_Global_Constraint_Zero_Mode.md commit feb8a0d8bc00c1c334991b452d449636cb3c4f70. Prewrite live HEAD feb8a0d8bc00c1c334991b452d449636cb3c4f70. Additive gravity-only; protected other lanes untouched, Suzuki physical-quarter weld PARKED.

[D] Exact canonical momentum constraint H_i=−2h_ij D_kΠ^{jk}+p_I∂iφI=0, with Π^{ij}=√h(K^{ij}−h^{ij}K)/(2κ), p_I=(2C/3)√h(φdot^I−N^j∂jφI)/N. Tensor-density algebra yields H_i=−2∂k(h_ijΠ^{jk})+Π^{jk}∂i h_jk+p_I∂iφI. On periodic T³ or vanishing boundary-flux domain, the exact zero-mode condition ∫[Π^{jk}∂i h_jk+p_I∂iφI]d³z=0 follows, valid to all nonlinear orders. For φI=zi on T³ the gradient requires winding/compact target chart or work with boundary terms; not globally periodic real-valued zi scalar.

[D/scoped] At quadratic order about spatially homogeneous background metric and Π0, p0=0, periodic boundary integral reduces schematically to ∫[Π^(1)jk∂i h^(1)_jk+p_I^(1)∂iπI+p_i^(2)]=0, with p_i^(2) containing ADM lapse/shift and metric corrections. Thus v15.002 fixed-metric quadratic T0i is not by itself the total constraint source; admissible initial data obey a global gravitational+matter momentum balance. No unconditional cancellation of matter momentum or uniform near-K=0 estimate follows. On R³ include surface contributions.

Flags: nonlinear_ADM_momentum_constraint=EXACT; global_zero_mode_balance=EXACT_CONDITIONAL_BOUNDARY; isolated_matter_source_zero_mode_must_vanish=FALSE; arbitrary_traveling_wave_admissible=NOT_GUARANTEED; near_zero_K_uniform_inverse_bound=OPEN; future_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: ADM-nonlinear-global-momentum-zero-mode
parent: v15.003
status: open
action: Verify canonical density index identity, integrated momentum balance, winding/background domain caveat, and second-order decomposition including p_i^(2), and identify assumptions needed for uniform low-K inversion.
deliverable: scoped verdict.

NEXT: compute precise quadratic p_i^(2) in ADM variables and study near-zero K convolution cancellation or weighted estimates beyond only the exact K=0 solvability law.
