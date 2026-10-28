# Cone Derivation Ledger v15.049 — Constrained normal velocity cancels displacement IR pole

Date 2026-10-28. Parents gravity v15.038, v15.044; Audit v15.045 verified latter. Note research-notes/K4_Constrained_Normal_Velocity_IR_Cancellation.md at 18ecf724bc9abc69da01e982d2bfc53d9835e7a6. Prewrite HEAD 18ecf724bc9abc69da01e982d2bfc53d9835e7a6. Parallel v15.048 Sandbox and Lane A untouched; Suzuki physical-quarter weld PARKED.

[D] Conformal scalar spatial gauge δφI=∂Iσ, N^i=∂ib, h=a²(1+2ψ)δ, p=Δσ is longitudinal STRAIN. v15.038 corrected constraints yield (1−Δ)b=dotσ+Hp−3Hψ+Δψ/(a²H). Subtract to obtain (1−Δ)(dotσ−b)=−dot p−Hp+3Hψ−Δψ/(a²H). Linear physical ADM normal velocity vI=(dotφI−N^j∂jφI)/N at order one is ∂I(dotσ−b), so Fourier vI_k = i kI/(1+k²)[−dot p_k−Hp_k+(3H+k²/(a²H))ψ_k]. This has no 1/k low-frequency pole if p,dot p,ψ regular, despite raw coordinate displacement velocity dotδφ~dot p/k. Shift cancels the raw pole.

[D CONDITIONAL] For coasting a²=τ²/3,H=1/τ and assumed p=τ^-1u, ψ=τ^-1w with bounded u_s and w in appropriate H^r Sobolev norms, vI_k=τ^-2 i kI[3w_k−u_s,k/(1+k²)]; hence ||v||_H^r≤C τ^-2(||w||_H^(r+1)+||u_s||_H^r). The τ²-weighted square of this normal kinetic matter term decays O(τ^-2)=O(e^-2s), IR uniformly. Strain energy likewise. This establishes a conditional energy-component decay estimate with the linear constraint shift retained, not a full quadratic Einstein ADM source estimate.

[OPEN] Control of ψ from physical reduced p without low-k losses; full quadratic lapse/shift/metric corrections and time-resonances; k=0 gauge and boundary conditions; global future nonlinear stability. Not a claim full physical perturbation energy is bounded for arbitrary unweighted data.

Flags: normal_velocity_shift_cancellation=DERIVED_LINEAR_GAUGE; raw_displacement_inverse_k=GAUGE_COORDINATE; normal_velocity_IR_multiplier=BOUNDED; conditional_weighted_kinetic_decay=E_MINUS_2S; ψ_reconstruction=OPEN; full_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: normal-velocity-infrared-cancellation
parent: v15.049
status: open
action: Independently check scalar constrained b equation, Fourier cancellation including sign and k² ψ term, τ^-2 velocity estimate and required ψ Sobolev control; distinguish first-order constrained normal velocity from nonlinear full energy.
deliverable: scoped verdict.

NEXT: reconstruct ψ in terms of physical scalar strain p from corrected v14.996 auxiliary action or constraints, check low-k and time weighted bounds, then handle full second-order source.
