# Cone Derivation Ledger v15.053 — Scalar wave compatibility for ψ reconstruction

Date 2026-10-28. Parent gravity v15.052, v15.049. Research note research-notes/K4_Scalar_Wave_Equation_Psi_Compatibility.md at commit 72ba3febcc6fb6c1ea943630776cd6e95ab77832. Prewrite HEAD 72ba3febcc6fb6c1ea943630776cd6e95ab77832. Additive gravity only; Suzuki weld PARKED and protected other lanes untouched.

[D] From exact three-canonical-scalar □g φI=0, scalar spatial gauge h=a²(1+2ψ)δ, lapse 1+α, contrav shift ∂ib and scalar labels φI=zi+∂Iσ, the linear density components are √−g g^{tν}∂νφI=a³∂I(dotσ−b), √−g g^{jν}∂νφI=−a[δjI(1+α+ψ)+∂j∂Iσ]. Thus ∂I{∂τ[a³(dotσ−b)]−a[Δσ+α+ψ]}=0, and for nonzero k bracket vanishes. It independently constrains any candidate ψ reconstruction together with v15.038 lapse/shift formulas. Homogeneous zero mode must be treated separately. No coefficient-level psi_sol return landed since v15.052; checked live HEAD. Therefore explicit ψ Fourier multiplier, infrared bound and 1/τ time decay remain OPEN. This is an exact first-order field-equation compatibility gate, not proof of global stability.

Flags: scalar_triplet_wave_linearization=EXACT; psi_reconstruction_independent_check=DERIVED; psi_symbolic_coefficients=OPEN; IR_uniform_metric_decay=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: sandbox, external-audit
type: independent-scalar-wave-psi-compatibility
parent: v15.053
status: open
action: Execute corrected v14.996 scalar_final2.py and reconstruct ψ. Independently substitute psi, lapse, shift, strain into this exact scalar wave equation, verify residual zero at nonzero k, then certify momentum multipliers and time weights. Do not infer completed reconstruction from existence of source algorithm.
deliverable: coefficient-wise ψ certificate and independent scalar wave residual.

NEXT: coefficient-level reconstruction operator and uniform low-k physical metric estimate if supported.
