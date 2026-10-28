# Cone Derivation Ledger v15.071 — Weighted scalar oscillator energy and nonlinear convolution obstruction

Date 2026-10-28. Gravity parent v15.070. Muse/Sandbox v15.069 classification audit read in full: geometry 1/3 derived; triplet η=3/2 selected, κC=1 matched, G empirical, no constant owed via current mechanism, nonlinear stability still proof owed. Research note research-notes/K4_Weighted_Linear_Energy_Quadratic_Convolution_Obstruction.md commit 4241fd44ee46b53cf8479f691c5265dd3e071219. Prewrite live HEAD 4241fd44ee46b53cf8479f691c5265dd3e071219. Protected Lane A, Muse, external audit files untouched; Suzuki physical-quarter weld PARKED.

[D] Audited scalar metric ψ_k=τ^-1[-u_k+|k|^-2(u_s−u)_k]/[3(1+|k|²)], u_ss+3(1+|k|²)u=0, k≠0. For data with finite E_{r,-2}=1/2∫(1+|k|²)^r |k|^-4(|u_s|²+3(1+|k|²)|u|²)d³k, E_{r,-2} is exactly conserved along linear evolution. This provides a sufficient weighted low-k class for uniform τψ H^r bound, conditional on finite weighted initial energy (unweighted oscillator energy alone not sufficient).

[D] Weighted class not closed under generic quadratic multiplication: pick nonzero real Schwartz f with Fourier support away from 0. f has finite all weighted Sobolev norms but hat(f²)(0)=const∫f²>0; thus ∫|K|^-4|hat(f²)(K)|²d³K diverges near K=0 in R³. Therefore linear weighted energy conservation does NOT establish nonlinear weighted energy closure, even with smooth high-frequency input. For smooth source output vanishing O(|K|^α), alpha>1/2 suffices for local dot H^-2 integrability in 3D, but generic source need not obey it.

[OPEN] Whether exact constrained quadratic Einstein-triplet sources have cancellations/zero-mode constraints/null structure strong enough for these weighted norms. Integrated ADM global balance v15.003 is not itself a full near-K=0 source bound. No physical nonlinear instability or nonlinear future stability proved. Muse source-coupling classification does not alter technical constraints or empirical Pantheon+ mismatch.

Flags: weighted_linear_energy=CONSERVED_EXACT; psi_weighted_linear_bound=CONDITIONAL_DERIVED; quadratic_weighted_space_product_closure=FALSE_GENERICALLY; full_constrained_source_lowK=OPEN; nonlinear_future_stability=OPEN; source_G_classification=EMPIRICAL_NOT_DERIVED; Suzuki_quarter=PARKED; protected_lanes_touched=FALSE.

HANDOFF
target: external-audit, sandbox
type: weighted-IR-oscillator-and-quadratic-convolution
parent: v15.071
status: open
action: Verify oscillator energy conservation, psi H^r multiplier bound, compact-frequency f² counterexample, and whether complete quadratic ADM source constraints suppress |K|→0 enough for dot H^-2 closure. Treat Muse v15.069 source-classification as a scope clarification, not theorem of physical uniqueness.
deliverable: scoped verdict and concrete candidate null/zero-mode structure if available.

NEXT: inspect full second-order constrained source for output-zero cancellation, versus gauge-invariant reformulation; avoid assuming generic Sobolev product estimates extend to inverse-Laplacian-weighted spaces.
