# Cone Derivation Ledger v15.1271 — All four Maxwell stress-conservation equations, aliasing and constraint-ready source gate

**Date:** 2026-11-20 Eastern. **Lane:** Gravity/Cone. **Status:** [D/N] independently implemented and locally executed spectral Maxwell stress energy + three momentum continuity on the original compact initial data at five grids; [NEGATIVE] native full-band quadratic stress is aliased and fails conservation; [PASS] doubling stress product grid resolves all components, and a strict two-thirds Maxwell band with source projection resolves all **retained** modes to ~1e-18; [OPEN] the exact committed script independent replay, K4-coupled ADM gravitational constraints, time-dependent four-metric, optical detector, and physical quarter-grid interaction. **Immediately pre-ledger inspected live HEAD:** cb569707ef8a3a6a6f42a56c75f0e059dfd28033. Protect earlier canonical results and Audit/Suzuki/Muse/Sandbox. Strictly additive.

## Gate 1218 — full Maxwell energy-momentum divergence, beyond scalar Ward

In conformal Maxwell evolution `xi=sqrt(3) log(tau)`, with `Ehat=h cos(k xi)` and `Bhat=-i(q cross h) sin(k xi)/k`, use the **analytically differentiated** Fourier histories to evaluate:
`rho=(E²+B²)/2`, `F=E cross B`, `T_ij=rho delta_ij-E_iE_j-B_iB_j`.
Their flat conformal stress conservation reads
`rho_dot+(sqrt(3)/tau)partial_j F_j=0` and
`F_i_dot+(sqrt(3)/tau)partial_j T_ij=0`.
These include the already tested v15.729 scalar source Ward but provide three additional vector conditions necessary for the momentum sector. The real E,B source uses the same discrete transverse projector and common Nyquist removal as v15.1267.

Three numerical product conventions were evaluated independently at tau=1.08 and N=16,24,32,40,48:
- Full finite Maxwell Fourier field, native N³ quadratic product: **expected negative** aliased divergence.
- Exactly the same full finite Maxwell field, zero-padded Fourier reconstruction on (2N)³ before taking quadratic products: **fully resolved** four-divergence; no gravitational source coefficients refitted.
- Additional strict componentwise |m_j|<N/3 Maxwell field truncation, native N³ quadratic product, and subsequent projection of stress divergence onto that same band: **resolved retained-band only**, not full-band conservation and not the same field as either full-field case.

## Gate 1219 — independently executed five-grid numerical evidence

Each entry below is the largest absolute discrete Fourier residual, with no normalization by source amplitude. Both equations use cosmic tau derivatives and include the conformal factor sqrt(3)/tau.

| N³ | Full native energy | Full native momentum | Full 2N energy | Full 2N momentum | 2/3 retained energy | 2/3 retained momentum |
|---|---:|---:|---:|---:|---:|---:|
| 16³ | 1.163454e-3 | 1.451467e-3 | 2.192e-19 | 5.216e-19 | 1.491e-19 | 1.636e-19 |
| 24³ | 4.839668e-3 | 3.871138e-3 | 1.334e-18 | 1.940e-18 | 6.604e-19 | 7.591e-19 |
| 32³ | 4.890558e-3 | 2.035990e-3 | 1.741e-18 | 2.917e-18 | 7.228e-19 | 6.855e-19 |
| 40³ | 1.288854e-3 | 2.984861e-4 | 2.175e-18 | 2.721e-18 | 1.311e-18 | 1.113e-18 |
| 48³ | 9.229746e-4 | 2.251753e-4 | 2.270e-18 | 2.763e-18 | 1.748e-18 | 1.737e-18 |

Representative source-sensitivity check: the conformal Maxwell mean rho at N=32 is 0.0007676608970155842 for the complete Nyquist-clean field, compared with 0.000742165825182177 for the distinct two-thirds-band initial field. At N=48 these means are 0.000778695424536061 versus 0.0007764440607162524. **Never weld the homogeneous Friedmann source from the first prescription to the nonzero metric modes of the second.** Stress-grid refinement does not itself guarantee spatial convergence of local tidal amplitudes.

**Execution classification:** the numerical table came from actual local Python/NumPy execution of a separately authored equivalent script (`/tmp/momentum_gate.py` during this gate); the new byte-level canonical GitHub source has been committed for independent replay and is not yet independently Audited. Reproducer source: `research-notes/k4_maxwell_four_stress_conservation_v15_1271.py` committed SHA cb569707ef8a3a6a6f42a56c75f0e059dfd28033. All old parent Python files remain unchanged.

## Gate 1220 — what this opens and what remains unproven

This establishes the **source consistency input** necessary for gravitational Hamiltonian/momentum propagation in a controlled finite Fourier scheme; it does not demonstrate gravitational constraint closure by itself. The next true gravity test must impose a **single declared discretization** for Maxwell energy/momentum/stress, homogeneous k=0 mean, source-first scalar ADM lapse/shift, sourced vector and tensor histories, and direct independent `G_mu_nu-kappa (T_EM+T_K4)_mu_nu` checks. Specifically, the v15.1262 curvature calculation's original *native-grid* quadratic stress cannot be treated as satisfying exact high-band spectral Maxwell Ward even though it passes an `R_00` trace imposed by its algebraic source reconstruction. If the dealiased source changes Fourier coefficients, rerun both homogeneous and nonzero tidal reconstructions and test the new pointwise trace against the identically projected source—not against a mismatched old source.

External Audit: replay the exact new committed reproducer with NumPy, verify sign of momentum flux/stress, analytic time derivatives, Fourier padding normalization, retained-band projection, Nyquist pairing and no hidden source amplitude rescaling. Confirm these are ordinary Maxwell identities; do not classify them as independent Einstein solutions or as a new Cone observable.

**Scientific boundary:** the framework remains Einstein–Maxwell coupled to the previously specified K4 solid. The quarter-grid Casimir/arithmetic structure has no independently justified coupling in this source, and the matched GR+identical-solid comparator remains a strict physical null.
