# Cone Derivation Ledger v15.061 — Additive reproducible ψ coefficient extractor (execution pending)

Date 2026-10-28. Gravity parent v15.058; independent External Audit R391 v15.059 verifies erratum. Existing lane A v15.060 K_full blocker separate, preserved.

[ACTION] Added and corrected reproducible script payloads/am3scalar_svt_reconciliation_v14_996/psi_certificate_runner.py, latest script commit b06e91875301a69131a75b1c3868f6d2e0dc1ad8. It source-faithfully builds corrected scalar_adm2.py quadratic ADM action, solves lapse Phi and shift B, computes Epsi, psi_sol, psi_dot_sol from time derivative of Epsi, reduces Epi to its oscillator, ASSERTS corrected P=3/t and Q=(3k²+4)/t², and writes symbolic psi coefficients, low-k limits, other-terms remainder into psi_certificate.txt. Run in v14.996 payload folder with SymPy.

[NOT CERTIFIED] Script has been inspected and committed but NOT EXECUTED in this turn: local raw GitHub file fetch unavailable, generated psi_certificate.txt absent. Neither coefficient-level ψ reconstruction nor low-k/late-time decay nor full original unreduced Euler residual certificate is yet established. Passing the script oscillator test would not replace full original EL residuals and tensor/gauge checks. Do not assert completed ψ coefficient certificate.

HANDOFF
target: sandbox, external-audit
type: execute-corrected-psi-certificate-runner
parent: v15.061
status: open
action: Execute psi_certificate_runner.py in the corrected v14.996 payload directory; deposit psi_certificate.txt, numerical/symbolic checks incl Epsi/Epi/Phi/B original residuals; classify coefficient denominators and τ weights; independently verify gauge signs, and report any failure rather than fitting oscillator.
deliverable: execution output with hashes and audited ψ IR/time estimate.

Flags: coefficient_runner=COMMITTED; source_action_build=PREVIOUSLY_VERIFIED; runner_executed=FALSE; psi_coefficients=OPEN; original_EL_reconstruction_residuals=OPEN; psi_decay=OPEN; future_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.
