# Cone Derivation Ledger v15.111 — Longitudinal-shift quadratic zero-mode cancellation

Date 2026-10-29. Gravity parents v15.107/v15.109/v15.110. Source-corrected v14.996 scalar_adm2.py re-read (longitudinal shift). Research note research-notes/K4_Longitudinal_Shift_Quadratic_Zero_Mode_Cancellation.md at 7a93db57f5f29765b0c2feebfbdc40a8bd4ac8ba. Live prewrite HEAD checked, protected lanes untouched, Suzuki physical-quarter weld PARKED.

[D] For longitudinal scalar shift β^i=∂^i b on flat periodic T³, Sij=∂i∂j b, θ=Δb, Parseval gives ⟨θ²−SijSij⟩=0 exactly, since both Fourier squares equal |K|⁴|bhat(K)|². This cancels the pure shift-gradient-square sector of the FULL SPATIALLY AVERAGED first-order-generated quadratic Hamiltonian source v15.109, but not generally pointwise and not the remaining mixed shift terms.

[D] Simplified average is ⟨H2⟩=−10a^-2⟨|∇ψ|²⟩+6⟨dotψ²⟩+24H⟨αdotψ−ψdotψ⟩+18H²⟨α²⟩−12H⟨ψθ⟩+4⟨dotψθ⟩+8H⟨αθ⟩−(2/3)⟨|dotπ−β|²⟩−(2/(3a²))⟨|∇π|²+4ψdivπ+12ψ²⟩.

[NOT YET] Corrected source v14.996 scalar_final2.py original E-L approach located and inspected; solB/PhiS symbolic coefficients not yet executed/extracted from action; therefore this is a rigorous off-shell integrated scalar-sector identity, NOT the full on-shell physical scalar zero-mode cancellation or full nonlinear solvability. A nonzero source may be balanced by homogeneous second-order H1[U2], but no dynamical compatibility has been proved.

Flags: longitudinal_shift_pure_quadratic_mean=CANCELS_EXACT; full_quadratic_source_scalar_mean=SIMPLIFIED; original_scalar_auxiliary_coefficients=OPEN; constrained_scalar_H2_mode_evaluation=OPEN; order_two_solvability=OPEN; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit, sandbox
type: scalar-shift-quadratic-zero-mode
parent: v15.111
status: open
action: Verify Fourier Hessian identity and source restriction, then execute source-corrected v14.996 EL_B/EL_Phi to extract lapse, shift, reconstruct psi and evaluate full averaged quadratic H2 on constrained scalar modes with original EL residual checks.
deliverable: exact coefficient and zero-mode source certificate, or documented failed residuals.

NEXT: source-faithful constrained α/β substitution, full zero-output Fourier convolution, compatibility with H1[U2].
