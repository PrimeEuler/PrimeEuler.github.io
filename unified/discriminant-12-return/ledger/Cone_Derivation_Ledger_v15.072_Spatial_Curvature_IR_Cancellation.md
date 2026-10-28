# Cone Derivation Ledger v15.072 — Linear intrinsic curvature cancels raw psi infrared pole

Date 2026-10-28. Gravity parents v15.070/071. Research note research-notes/K4_Spatial_Curvature_IR_Pole_Cancellation.md commit feb9693174ab0a44f45b7bf8138de35f240d1fb0. Checked live prewrite HEAD. Other lanes untouched; Suzuki quarter weld PARKED.

[D] In source-faithful conformal spatial gauge h_ij=a²(1−2ψ)δij, δR3=4a^-2 Δψ. Audited v14.996 coefficient ψ_k=[−k²π_k+τdotπ_k]/[3k²(1+k²)] for k≠0. Hence a²δR3_k=4[k²π_k−τdotπ_k]/[3(1+k²)]. With π=τ^-1u(s), u_ss+3(1+k²)u=0, obtain a²δR3_k=(4/(3τ))[u_k−u_s,k/(1+k²)]. Uniform Fourier multiplier bound ||a²δR3||_{H^r} ≤4/(3τ)(||u||_{H^r}+||u_s||_{H^r}), no inverse-k² needed. Intrinsic spatial curvature is invariant under linearized spatial diffeomorphisms of flat background slices; NOT fully gauge-invariant under altered spacetime foliation. Prior v15.038 uses opposite sign ψ definition, which is why this entry is explicit about v14.996 gauge convention.

[OPEN] Quadratic spatial curvature includes undifferentiated ψ and gradient products, so the linear cancellation alone does not prove nonlinear IR energy closure. Need matter-defined slices or invariant spacetime curvature and inspect low-k quadratic interactions. No nonlinear future stability theorem, and Muse v15.069 classification (G empirical, C matched) preserved.

Flags: spatial_curvature_linear_IR_pole=CANCELS; linear_curvature_sobolev=UNIFORM_K; full_time_gauge_invariant=NOT_ESTABLISHED; second_order_curvature_IR=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: intrinsic-spatial-curvature-IR-cancellation
parent: v15.072
status: open
action: Recheck source psi sign convention, 3-Ricci linearization and Fourier multiplier, distinguish spatial diffeomorphism invariance from slicing invariance, and test nonlinear curvature products for low-output momentum losses.
deliverable: scoped verdict.

NEXT: compute nonlinear 3-curvature to quadratic order and inspect inverse-k behavior of ψΔψ and |∇ψ|²; or construct slicing-robust geometric observables.
