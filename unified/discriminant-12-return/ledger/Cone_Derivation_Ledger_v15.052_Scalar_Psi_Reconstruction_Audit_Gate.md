# Cone Derivation Ledger v15.052 — Corrected scalar ψ reconstruction: source-audited gate, IR coefficients still needed

Date 2026-10-28. Parent gravity v15.049; external audit v15.051 confirmed v15.049. Research note research-notes/K4_Scalar_Psi_Reconstruction_Source_Audit.md committed 8f2458113716d989ee67091212cd4d757b47522e. Prewrite live HEAD 8f2458113716d989ee67091212cd4d757b47522e. Protected Lane A and Sandbox untouched; Suzuki quarter weld PARKED.

[SOURCE VERIFIED] Exact corrected v14.996 payload scalar_adm2.py uses metric variable ψ and strain variable π, φ3=z+π(t)sin(kz)/k. scalar_final2.py machine-builds the unreduced quadratic action, eliminates Phi and B, defines E1=EL(Lred,ψ), E2=EL(Lred,π), then solves ψ=solve(E1,ψ)[0] and reconstructs dotψ from time derivative E1 before obtaining the audited π oscillator. The reconstruction operator is defined in source and necessary for linking conditional v15.049 metric decay to π. No deposited psi_sol expression was retrieved (script writes runtime scalar_final.txt, absent at inspected path). Hence exact coefficient multipliers, denominators, k→0 limits, τ weights and Sobolev bounds are NOT certified by this gate. Do not promote inferred ψ~τ^-1 and nonlinear future stability.

Flags: corrected_psi_reconstruction_pathway=SOURCE_VERIFIED; explicit_psi_coefficients=NOT_EXTRACTED; psi_low_k_multiplier=OPEN; psi_time_decay=OPEN; normal_velocity_IR_cancellation_v15_049=PRESERVED_CONDITIONAL; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: sandbox, external-audit
type: corrected-scalar-psi-reconstruction-certificate
parent: v15.052
status: open
action: Execute corrected v14.996 scalar_final2.py plus scalar_adm2.py; return exact psi_sol, psid_sol from generated scalar_final.txt, all denominators, k→0 limits, τ scaling after π=τ^-1u, and residuals against original unreduced Euler equations. Independently audit action correctness incl inverse metric and shift derivatives. Assess ψ H^r multiplier bounds and whether π implies ψ decay without low-k losses.
deliverable: reproducible coefficient-level ψ reconstruction certificate.

NEXT: only after exact coefficient return, attempt constrained energy decay theorem for physical scalar in time-weighted Sobolev norms. Do not infer a theorem from source algorithm alone.
