# Cone Derivation Ledger v15.094 — Quadratic conformal spatial curvature generates zero mode

Date 2026-10-29. Gravity parent v15.072. Research note research-notes/K4_Second_Order_Conformal_Spatial_Curvature_Zero_Mode.md commit 158fc285835115bb0a69fd68b2307ca45b71a05f. Prewrite HEAD 158fc285835115bb0a69fd68b2307ca45b71a05f. Concurrent v15.093 External Audit and Lane A protected and untouched. Suzuki physical-quarter weld PARKED.

[D] Exact spatial conformal metric h_ij=a²(1−2ψ)δ_ij leads to a²R3=4Δψ/(1−2ψ)²+6|∇ψ|²/(1−2ψ)³, using standard 3D conformal curvature formula. Quadratic expansion a²R3=4Δψ+16ψΔψ+6|∇ψ|²+O(ψ³ in perturbation amplitude). For smooth periodic ψ, quadratic geometric zero-mode mean is ⟨16ψΔψ+6|∇ψ|²⟩=−10⟨|∇ψ|²⟩, strictly negative for nonconstant ψ. Thus linear two-derivative cancellation of raw ψ inverse-k² does not guarantee zero-output suppression of quadratic curvature. Fourier high-high → low interactions persist.

[SCOPE] This is the fixed conformal spatial-metric family, not an independently solved full second-order Einstein Hamiltonian constraint; second-order h2, lapse, shift, K²−Kij² and matter terms may compensate in the full system. Spatial curvature is slice dependent, not fully time-gauge invariant. No claim physical instability, nonlinear future instability, or unique G; matched/empirical Muse v15.069 classification preserved.

Flags: exact_conformal_R3=DERIVED; quadratic_conformal_R3=DERIVED; quadratic_R3_zero_mode=GENERIC_NONZERO; full_second_order_Hamiltonian_balance=OPEN; global_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: quadratic-conformal-curvature-zero-mode
parent: v15.094
status: open
action: Verify conformal formula and 16,6 coefficients, integration-by-parts −10 mean, distinguish geometric sector from full constraint including h2, extrinsic, matter and gauge effects.
deliverable: scoped verdict.

NEXT: derive full second-order Hamiltonian zero-mode with metric, extrinsic and scalar normal-energy terms, study nonlinear compatibility rather than assuming curvature zero-mode cancels.
