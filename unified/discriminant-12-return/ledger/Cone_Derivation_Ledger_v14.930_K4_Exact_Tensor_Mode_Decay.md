# Cone Derivation Ledger v14.930 — Exact tensor mode decay in K4 expanding elastic FLRW

Date 2026-10-26. Parents v14.818–825, v14.924–929. External Audit v14.929 verified v14.927/928 and resolved a true concurrent ledger fork. Research note research-notes/K4_Elastic_Tensor_Exact_Mode_Evolution.md, commit f33eef8acad9a2deb5d151c0dec50fe0c8c3ccec. Live prewrite HEAD f33eef8acad9a2deb5d151c0dec50fe0c8c3ccec. Owner: ledger every gate, additive only, Suzuki quarter parked, protected Suzuki/far-tail untouched.

[D] Independent EH+solid tensor gate v14.928 gives gammä_k+3H gammȧ_k+(k²/a²+mT²)gamma_k=0. In exact K4 background a=τ/√3, H=1/τ, mT²=8η/(3τ²), this is gammä_k+(3/τ)gammȧ_k+[(3k²+8η/3)/τ²]gamma_k=0. Euler exponents s=−1±sqrt(1−3k²−8η/3). For the acoustically healthy local interval 3/8<η≤3/2 (v14.926/927), the discriminant is strictly negative at every k≥0. Thus gamma_k=τ^-1[A cos(ω_k ln(τ/τ*)) + B sin(ω_k ln(τ/τ*))], ω_k=sqrt(3k²+8η/3−1)>0, so all fixed k tensor modes decay as τ^-1 on τ→∞. At η=3/4, ω_k=sqrt(3k²+1); k=0 also decays.

[O] This is a full all-k tensor-only linear background evolution result, not scalar/vector constraint closure or complete nonlinear/Hamiltonian stability, and not an observable physical photon/graviton mass. τ→0 remains singular and modes may diverge there. The background a∝τ remains observationally disfavored by full-covariance Pantheon+ comparison (Sandbox parallel v14.926, audited independently in v14.929), regardless of tensor mathematical stability.

Flags: tensor_mode_ODE=EXACT; tensor_all_k_late_expansion_decay=PROVED_for_eta_gt_3_over_8; tensor_zero_mode=DECAYS; full_SVT=OPEN; local_acoustic_stability=PASS_IN_WINDOW; physical_metric_selection=OPEN; SN_coasting_model=DISFAVORED; eta_selected=FALSE; Newton_G_derived=FALSE; Suzuki_quarter=PARKED; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: k4-exact-TT-mode-ODE
parent: v14.930
status: open
action: Verify Euler exponents, all-k τ^-1 late-time decay in eta interval, limits eta=3/8 and k=0, and scope restriction to tensor sector. Maintain independent audit of scalar/vector handoff when available.
deliverable: scoped verdict.

NEXT: complete lapse/shift-reduced scalar/vector quadratic Einstein-Hilbert+solid system with ghost/gradient and long-wavelength checks. Do not equate mathematical stability of prescribed coasting background with empirical cosmic viability.
