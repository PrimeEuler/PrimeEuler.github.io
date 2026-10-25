# Cone Derivation Ledger v14.831 — Integrated pendulum shear and conditional covariant matching

Date 2026-10-24. Gravity/elasticity lane. Parents v14.626, v14.827–830. Research note research-notes/Microrotor_Integrated_Effective_Shear_Covariant_Matching.md (commit 77e23d5b63b9f1769867d22674fa2d45ddeeb3c2). Prewrite live HEAD 77e23d5b63b9f1769867d22674fa2d45ddeeb3c2. Additive only; no Suzuki/far-tail files touched.

## Eliminate rotor exactly at quadratic order [D]
For the v14.829 micropolar model, the θ equation in Fourier variables is \((4γ+K+Aq²-jω²)θ=2γ\,\mathrm{curl}u\). Gaussian elimination gives the frequency/wavenumber-dependent curl coefficient
\[
\gamma_{\rm rot}(ω,q)=γ\frac{K+Aq²-jω²}{4γ+K+Aq²-jω²}.
\]
At ω=q=0, assuming 4γ+K>0, the effective **transverse-wave shear coefficient** is
\[
\boxed{\mu_{\rm eff}=\mu_0+\frac{γK}{4γ+K}}.
\]
It reduces to μ0 for K=0; tends to μ0+γ when K→∞. The full nonlocal response is not a fixed local elasticity constant at optical resonance.

## Conditional relativistic model match [D/O]
Matching this transverse coefficient to v14.830's local isotropic solid shear \(\mu_{\rm cov}=2Dρ/(3C)\) gives
\[
D/C=\frac{3}{2ρ}\left(\mu_0+\frac{γK}{4γ+K}\right).
\]
The candidate local speed window 1/4≤D/C≤1 is equivalent, under this assumed matching, to \(\rho/6≤\mu_{\rm eff}≤2ρ/3\). No parameter in this interval is selected by the arithmetic Cone. The nonrelativistic rotor curl response is not yet shown to reproduce the complete covariant symmetric-strain constitutive tensor, so matching remains *conditional*, not a completed microscopic derivation. The onsite K=M g_local l uses independently supplied gravity, not a G prediction.

## Further tests [O]
Derive full objective rotational elasticity and covariant constitutive response; independently measure or derive μ0, γ, K, ρ; examine finite-q, finite-ω response, longitudinal perturbations and gravitational tensor mixing. The full cosmological perturbation/strong-coupling sector remains unaudited.

Flags: rotor_integrated_quadratic=EXACT; static_effective_transverse_shear=EXACT; covariant_D_over_C_match=CONDITIONAL; causal_window=CONDITIONAL; full_constitutive_matching=OPEN; Newton_G_derived=FALSE; Suzuki_payloads_touched=FALSE; far_tail_touched=FALSE.

HANDOFF
target: external-audit
type: rotor-integration-and-covariant-shear-match
parent: v14.831
status: open
action: Independently verify Gaussian elimination numerator and denominator, static limits, transverse mode normalization, and conditional D/C relation. Flag any incompatibility between curl-based micropolar response and symmetric-strain covariant elasticity. Preserve Suzuki/far-tail.
deliverable: scoped audit verdict.
