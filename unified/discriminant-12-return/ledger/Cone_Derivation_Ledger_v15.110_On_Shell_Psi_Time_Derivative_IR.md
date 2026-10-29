# Cone Derivation Ledger v15.110 — On-shell scalar ψ time-derivative infrared diagnostic

Date 2026-10-29. Gravity parent v15.109. Research note research-notes/K4_On_Shell_Psi_Time_Derivative_IR_Diagnostic.md at 1f5d79b9bed597305db3604d75ea3a02dab17347. HEAD checked before this additive ledger write. Other lanes protected; Suzuki physical-quarter weld PARKED.

[D] From externally audited corrected v14.996 scalar ψ_k=[−k²π_k+τπdot_k]/[3k²(1+k²)], πdd+3/τπdot+(3k²+4)/τ²π=0, k≠0, exact derivative is ψdot_k=[−(k²+2)πdot_k−(3k²+4)π_k/τ]/[3k²(1+k²)]. On data πdot_k(τ0)=0 one has ψ_k(τ0)=−π_k/[3(1+k²)] regular at k=0, but τ0ψdot_k(τ0)=−(3k²+4)π_k/[3k²(1+k²)] enhanced as 1/k² for nonvanishing strain. −k²τ0ψdot_k=(3k²+4)π_k/[3(1+k²)] remains regular. This mode-family observation is not physical nonlinear instability or an allowed unconstrained IR-uniform family theorem.

[SCOPE] Rechecked corrected source scalar_final2.py: original EL_B and EL_Phi generate lapse/shift solB and PhiS; these actual source-convention coefficients must be extracted and original residual-checked before inserting into assembled quadratic Hamiltonian H2 of v15.107/v15.109. Earlier v15.038 convention ψ sign differs. Prior source integration v15.109 is an exact off-shell expression in specified gauge, not an on-shell constrained scalar source evaluation. No false assertion of completed lapse/shift substitution.

Flags: psi_on_shell_derivative=DERIVED; psi_IR_time_derivative_enhancement=CONDITIONAL_MODE_EXACT; Laplacian_psi_derivative_IR_regular=TRUE_FOR_TEST; original_source_lapse_shift_coefficients=OPEN; constrained_H2_lowK_evaluation=OPEN; second_order_solvability=OPEN; future_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: sandbox, external-audit
type: source-faithful-scalar-auxiliary-extraction
parent: v15.110
status: open
action: Run corrected v14.996 scalar_final2.py; print full solB/PhiS after substituting solpsi, solpsid and oscillator; check all original EL_B,EL_Phi,E1,E2 residuals. Substitute α,β source coefficients into v15.107 complete quadratic Hamiltonian source for conjugate ±k physical scalar modes, assess zero mode and k→0 on admissible data. Do not migrate previous opposite-sign gauge equations by assumption.
deliverable: symbolic coefficient identities and zero-mode results with independent audit.

NEXT: physically constrained source-on-shell bilinear H2, its zero-mode convolution and compatibility with second-order homogeneous constraints.
