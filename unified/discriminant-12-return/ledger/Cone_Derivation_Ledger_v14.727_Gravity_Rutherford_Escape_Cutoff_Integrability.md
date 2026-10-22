# Cone Derivation Ledger v14.727 — Gravity bare hard-escape cutoff convergence and analytic integrability

**Date:** 2026-10-22 EDT. **Lane:** gravity. **Parents:** v14.723–726.
**Live head/collision check:** before writing \`master\` SHA \`3944331ef8b53cb44c7837834786b1bd09ba8f46\`, and v14.727 unused. Strict additive files only; no Suzuki sandbox handoff or competing computation.
**Files:** \`research-notes/gravity_escape_convergence_16k4.py\`; \`research-notes/Gravity_Escape_Cutoff_Integrability_And_Convergence.md\`.

## Numeric gate [N]

Executed four independent scrambled Sobol realizations, each 2^16 samples per parameter pair, for the **bare Rutherford**, Maxwellian-and-Kepler-averaged escape functional with μ=T=σ=1, physical minimum polar deflection theta_min. Rates are normalized by nK0 for dσ/dΩ=K0 g^−4 sin^−4(theta/2).

At e=.82: theta_min=.4 → 4.1014±.0076; .2 → 4.3462±.0267; .1 → 4.3728±.0518; .05 → 4.4596±.1160. Errors are between-scramble standard errors only, NOT certified intervals. e=0 and .55 comparisons, maximum sample weight and positive-event rarity diagnostics are in the note and runnable producer. Increased compute confirms strong variance worsening at small angle; do not fit or promote an uncontrolled numerical theta→0 limit.

## Analytic zero-angle integrability gate [D]

At fixed bound e<1, the Kepler escape-speed gap is uniformly positive:
\[
\delta_e=\min_E(\sqrt{2\mu/r(E)}-|v(E)|)
=\sqrt{\frac{\mu}{T(1-e)}}(\sqrt 2-\sqrt{1+e})>0.
\]
Equal-mass elastic Rutherford scattering satisfies \(|v'-v|=g\sin(\theta/2)\); escape therefore requires \(g\sin(\theta/2)\ge\delta_e\). With \(g=|v-w|\), this forces \(|w|\ge\delta_e/\sin(\theta/2)-v_{\max}\). For finite Maxwellian dispersion sigma, the very-small-angle escaping events are bounded by Gaussian target-velocity tails, suppressing the polynomial Rutherford angular weight and yielding a finite **bare escape-rate integral as theta_min→0 at every fixed bound e<1**. This is distinct from the divergent *total* elastic collision rate, and it does not establish uniformity as e→1 or a matched BPS rate. Near g=0 positive escape is impossible, controlling the apparent g^−3 singularity of the rate factor.

## Status / next local gate

- **COMPLETED:** reproducible higher-N QMC cutoff diagnostics and fixed-e analytic integrability theorem.
- **OPEN:** high-accuracy zero-cutoff *numerical* bare hazard (better conditioned conditional sampling), full global BPS matched jump+soft coefficients, and finite-temperature survivor-normalized density.
- **NEGATIVE:** no derived correction to standard gradiometry Xi or emergence of G. Avoid hand-fitting a new gravitational potential.

**Resource directive:** Suzuki far-tail sandbox remains reserved, with no gravity work issued to it. All writes and compute belong to dedicated gravity lane.

**Flags:** \`Suzuki_compute_reserved=true\`; \`sandbox_gravity_handoffs=NONE\`; \`bare_escape_zero_cutoff_finite_for_fixed_e=true\`; \`bare_escape_zero_cutoff_value=OPEN\`; \`matched_BPS_QSD=OPEN\`; \`new_Xi_signal=false\`; \`G_derived=false\`; \`far_tail_touched=false\`.
