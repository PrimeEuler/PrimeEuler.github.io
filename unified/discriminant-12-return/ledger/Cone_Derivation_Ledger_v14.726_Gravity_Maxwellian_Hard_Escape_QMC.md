# Cone Derivation Ledger v14.726 — Gravity Maxwellian-averaged bare Rutherford hard-escape rate

**Date:** 2026-10-22 EDT. **Lane:** dedicated gravity, user-directed self execution. **Parents:** v14.723–725 and source EFT v3.4.
**Live HEAD and collision check:** \`f8a43fe786718249b97e37db12fd9b5d0ecbe949\`; v14.726 unoccupied. **No Suzuki sandbox usage or handoff.** Strictly additive.
**Files:** \`research-notes/gravity_maxwellian_escape_qmc.py\`; \`research-notes/Gravity_Maxwellian_Escape_QMC_Stage.md\`.

## Implemented next stage [D/N]

Reconstructed a complete *bare-cutoff* hard-escape hazard integral, averaging (i) the exact mean-anomaly/Kepler time measure, (ii) a 3D Maxwellian target-velocity law, (iii) the equal-mass elastic postcollision criterion \(|v'|^2\ge2\mu/r\), (iv) the Rutherford \(g^{-4}\sin^{-4}(\theta/2)\) differential scattering cross section times relative flux g, and (v) exact outgoing scattering azimuth. The resulting integral is evaluated by a deterministic seeded randomized quasi-Monte Carlo reproducer with four independent Sobol scrambles. Normalize \(\lambda/(nK_0)\) for \(d\sigma/d\Omega=K_0 g^{-4}\sin^{-4}(\theta/2)\).

At dimensionless μ=T=σ=1, minimum hard angle θ_min=.2, the numerical rate factors are 5.070±.119 for e=0, 4.854±.169 for e=.55, and 4.448±.079 for e=.82, where errors are **between-scramble sampling diagnostics**, not certified bounds. Other cutoff choices θ_min=.1,.4 are recorded in the note, including expected finite-cutoff effects and sample noise. This moves beyond the fixed incoming-pair angular calculation of v14.725.

**Important:** BPS soft/hard matching and subtraction are NOT applied. The normalized rate is a conditional bare hard-sector diagnostic, not a physical escape prediction or global killed-population solution. No finite-temperature quasi-stationary distribution is claimed. The current corpus's fold-local BPS numbers cannot uniquely fill the missing global soft and jump kernel. Source-specific next gate: QMC convergence/variance and cutoff sensitivity, then global matched kernel if physics input permits.

**Scope:** no new \(\Xi\) response, no derivation of G, no far-tail or manuscript edits; sandbox reserved entirely for Suzuki.

**Flags:** \`hard_escape_Maxwellian_orbit_averaged=PRELIMINARY_QMC\`; \`matched_BPS_escape_rate=OPEN\`; \`finite_temperature_QSD=OPEN\`; \`Suzuki_compute_reserved=true\`; \`new_sandbox_handoff=false\`; \`G_derived=false\`; \`papers_modified=false\`.
