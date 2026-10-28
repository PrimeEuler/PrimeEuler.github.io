# Cone Derivation Ledger v15.038 — Gauge-fixed scalar and vector ADM auxiliary infrared gaps

Date 2026-10-28. Gravity parents v15.007, v15.011, v15.013. Parallel Lane A v15.037 K_full blocker read and left untouched. Research note research-notes/K4_Scalar_Gauge_ADM_Constraint_Block_IR_Gap.md committed 9daadead115e18e61d0719810dac9b7dbae9dd4b. Live HEAD prewrite 9daadead115e18e61d0719810dac9b7dbae9dd4b. Suzuki physical-quarter weld PARKED.

[D] Correct ADM metric momentum v15.007 yields first-order local vector momentum equation κH_i^(1)/a³=−(1/2)∂k(dotε_ik−δik dottrε)−2H∂iα+(1/2)(Δβ_i−∂i divβ)+(2/3)(dotπ_i−β_i)=0. With spatial conformal scalar gauge εij=2ψδij, β_i=∂ib, π_i=∂iσ, for k≠0 longitudinal constraint 2dotψ−2Hα+(2/3)(dotσ−b)=0. Combine exact first-order Hamiltonian from v15.011: −4/a²Δψ+12Hdotψ−4HΔb−12H²α−4H²Δσ+12H²ψ=0. Eliminating α gives (1−Δ)b=dotσ+HΔσ−3Hψ+Δψ/(a²H), or b_k=[dotσ_k−Hk²σ_k−3Hψ_k−k²ψ_k/(a²H)]/(1+k²); α=dotψ/H+(dotσ−b)/(3H). Therefore scalar auxiliary inverse has positive denominator 1+k² for nonzero Fourier k; no isolated finite-k singularity in b reconstruction. For transverse gauge ε_T=0, β_T=shift and π_T matter, momentum implies (−Δ+4/3)β_T=(4/3)dotπ_T, bounded multiplier β_T,k=4dotπ_T,k/(3k²+4). This normalization is different from Muse v14.996 vector V but same IR gap structure.

[O] This is a correct *linearized constraint operator in a fixed spatial gauge*, not second-order full ADM source estimate. Scalar longitudinal parametrization π=gradσ can itself have special zero-mode and 1/k effects. Lapse coefficient H^-1 grows at late time, so no uniform time bootstrap follows; need second-order gauge-fixed source and resonance estimates. No global nonlinear stability / unique source or Newton G derived.

Flags: scalar_constraint_b_denominator=1_plus_k_squared; transverse_constraint_gap=3k_squared_plus_4; linear_lapse_shift_reconstruction=DERIVED; full_second_order_joint_inversion=OPEN; time_uniform_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: scalar-gauge-adm-auxiliary-infrared-gaps
parent: v15.038
status: open
action: Independently check local momentum linearization from Π1 and Hamiltonian, coefficient signs and Fourier inverses in scalar conformal gauge and transverse spatial gauge, verify comparison with corrected v14.996 under variable changes; distinguish k=0 and late-time limitations.
deliverable: scoped verdict.

NEXT: calculate second-order sources of gauge-fixed Hamiltonian+momentum operator and establish weighted Sobolev estimates for source convolution and time growth, with explicit zero-mode compatibility.
