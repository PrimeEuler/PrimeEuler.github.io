# Cone Derivation Ledger v15.058 — ERRATUM closes v15.057 scalar compatibility blocker

Date 2026-10-28. Parent v15.057 contradiction claim, v15.038 scalar constraints, v15.053 scalar wave, v14.996 corrected scalar oscillator. Note research-notes/K4_Scalar_Wave_Constraint_Blocker_Resolved_Erratum.md commit 16ea15a539f20f2b77fc850c45e4cc602c6f282a. Prewrite live HEAD 16ea15a539f20f2b77fc850c45e4cc602c6f282a. Additive erratum; protected other lanes untouched; Suzuki quarter physical weld PARKED.

[CORRECTION] v15.057's inferred unstable oscillator from gauge-fixed constraints plus wave was an ALGEBRAIC ERROR. Exact independent symbolic recomputation, setting p=Δσ and k≠0, yields
 b=[−t pdot+k²p−3k²(1+k²)ψ]/[k²t(1+k²)],
 S=dotσ−b=[−t pdot−p+3(1+k²)ψ]/[t(1+k²)],
 α=t ψdot+(t/3)S.
Wave residual W=∂t(t³S)−3t(p+α+ψ) simplifies identically to
 W=−t/(1+k²)[t² pddot+3t pdot+(3k²+4)p].
Therefore W=0 reproduces EXACTLY corrected v14.996 physical scalar strain oscillator pddot+3/t pdot+(3k²+4)/t² p=0. The conflicting sign and (3k²+2) term in v15.057 are RETRACTED. No evidence for source-sign failure from this test. All ψ and ψdot cancel, hence the system does not itself yield the missing coefficient-level ψ reconstruction.

Flags: v15_057_scalar_wave_blocker=RESOLVED_ALGEBRAIC_ERRATUM; v15_057_bad_oscillator=RETRACTED; corrected_linear_wave_compatibility=EXACT; independent_source_ADM_psi_reconstruction=OPEN; psi_low_k_time_weight=OPEN; full_future_nonlinear_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: erratum-v15-057-compatibility
parent: v15.058
status: open
action: Independently substitute b,S,α into wave and verify exact W factorization, identify previous algebraic error, confirm k≠0 and sign conventions; do not confuse resolved compatibility with ψ coefficient certificate.
deliverable: scoped confirmation.

NEXT: extract ψ from corrected v14.996 independent Euler equation E1 in machine-built action, report Fourier coefficients, IR limits, τ weight and original unreduced residuals.
