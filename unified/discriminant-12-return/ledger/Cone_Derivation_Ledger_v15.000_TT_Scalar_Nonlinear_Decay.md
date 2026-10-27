# Cone Derivation Ledger v15.000 — TT–scalar nonlinear bilinear and conditional log-time decay

Date 2026-10-27. Parents v14.996–998; external audit v14.999 verified previous gates. Research note research-notes/K4_TT_Scalar_Bilinear_Logtime_Decay_Gate.md committed cb3828d1c7b0e1613801237ab9f740408b5cb2ff. Live prewrite HEAD cb3828d1c7b0e1613801237ab9f740408b5cb2ff. Additive gravity-only, protected lanes untouched and Suzuki-quarter weld PARKED.

[D] In synchronous prescribed-TT metric g_ij=−a²(δij+γij), trγ=∂iγij=0 and a=τ/√3, triplet φI=zI+πI, expanding □gφI yields displayed bilinear π̈I+3Hπ̇I−a^-2ΔπI+a^-2γij ∂i∂jπI+...=0. The TT source from the background φI=zI at linear order vanishes by ∂iγij=0. In log time s=ln(τ/τ0), multiplied τ² equation reads πss+2πs−3Δπ+3γij∂i∂jπ+...=0. No *explicit* decaying coefficient at fixed γ, but corrected TT solutions satisfy γ=O(τ^-1)=O(e^-s) modewise. Thus controlled tensor Sobolev decay makes this specific bilinear interaction integrable in log time, conditional on Sobolev control.

[SCOPE] This is one nontrivial quadratic interaction under prescribed TT metric, NOT the complete second-order constrained Einstein–triplet source. Scalar πI is not yet fully ADM-reduced physical q; lapse/shift and scalar/vector interactions, infrared modes, nonlinear resonance and derivative loss remain open. A linear mode-decay substitution is not a nonlinear bootstrap closure. No global nonlinear stability claim.

Flags: TT_scalar_bilinear=DERIVED; TT_background_linear_source=ZERO; log_time_interaction_explicit_decay=NONE; conditional_tensordecay=e_minus_s; full_constrained_quadratic_system=OPEN; nonlinear_future_stability=NOT_DERIVED; Newton_G=NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: TT-scalar-bilinear-logtime-source
parent: v15.000
status: open
action: Independently check √−g g^ij TT perturbation, scalar wave bilinear coefficient and log-time factor, then distinguish conditional decay from full constrained nonlinear future stability. Confirm mode-variable mismatch caveat.
deliverable: scoped verdict.

NEXT: derive second-order ADM scalar/vector lapse-shift terms and energy norm bounds in physical reduced variables; inspect inverse-k degeneracy and potential resonances before claiming global result.
