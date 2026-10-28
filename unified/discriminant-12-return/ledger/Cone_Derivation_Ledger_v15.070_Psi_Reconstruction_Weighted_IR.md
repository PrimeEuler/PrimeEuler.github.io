# Cone Derivation Ledger v15.070 — Audited scalar ψ reconstruction and weighted infrared condition

Date 2026-10-28. Parent gravity v15.061, External Audit v15.063 Round 392 (independent original and runner execution). Research note research-notes/K4_Psi_Reconstruction_Weighted_Infrared_Certificate.md at commit 01777261683056f391d0c4fac6ade72705c77d22. Live prewrite HEAD checked; additive gravity only. Separate v15.069 Sandbox classification and Lane A unchanged; Suzuki physical-quarter weld PARKED.

[V] External Audit v15.063 executed corrected psi_certificate_runner.py, passed assertions and matched independent v14.996 scalar_final2.py extraction in Round 390:
ψ_k=[−k²π_k+τdotπ_k]/[3k²(1+k²)] for k≠0.
A_π=−1/[3(1+k²)] regular at 0, B_dotπ=τ/[3k²(1+k²)] has a genuine inverse-k² raw metric reconstruction coefficient. This supersedes v15.052/v15.061 execution-pending flags; original scalar oscillator remains correct.

[D] π_k=τ^-1u_k(s), s=ln(τ/τ0), u_ss+3(k²+1)u=0, yields ψ_k=τ^-1[-u_k+(u_s−u)_k/k²]/[3(1+k²)]. For R³ nonzero modes ||τψ||_{H^r}≤1/3[||u||_{H^r}+|||∇|^-2(u_s−u)||_{H^r}], so ordinary unweighted scalar oscillator energy alone does not control ψ uniformly at k→0. Fixed nonzero k gives ψ=O(τ^-1). A sufficient stable linear class is weighted H^r norms of both u(s0) and u_s(s0) under |∇|^-2, because oscillator frequency √(3(k²+1)) uniformly positive and the weighted oscillator energy is conserved modewise. Caution high-k derivative content also needs frequency-weighted bounds and k=0 gauge treated separately; no claim the raw metric ψ is a gauge-invariant observable. Single-time cancellation u_s−u=O(k²) not generically preserved by oscillator unless initial data satisfy stronger weighted condition. On fixed T³ the minimal nonzero k offers box-dependent bound.

[OPEN] Nonlinear mode convolutions may fail to preserve low-frequency weighted Sobolev class; gauge-invariant physical energy may cancel raw ψ inverse-Laplacian factors. Full second-order ADM source/reconstruction and future nonlinear stability unproved.

Flags: psi_coefficients=EXTERNAL_AUDIT_CERTIFIED; runner_execution=CONFIRMED_BY_AUDIT_V15_063; raw_metric_inverse_k2=CONFIRMED; unweighted_metric_IR_bound=NOT_DERIVED; weighted_linear_psi_bound=CONDITIONAL_DERIVED; nonlinear_future_stability=OPEN; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit
type: psi-IR-weighted-norm
parent: v15.070
status: open
action: Verify exact oscillator substitution, weighted bound and time-dependence; test preservation of low-k weighted class under quadratic ADM source convolution and distinguish gauge from physical IR instability.
deliverable: scoped verdict.

NEXT: derive conserved weighted linear oscillator energy and assess whether physical nonlinear constraints preserve admissible low-k norm under convolution; alternative gauge-invariant variables may be needed.
