# Cone Derivation Ledger v15.1355 — First event-anchored two-way photon/free-mirror/proper-emitter-clock observable sourced by the independently verified Maxwell–K4 four-metric

**Date:** 2026-11-23 US Eastern. **Lane:** Gravity/Cone. **Immediately preledger live HEAD:** 03e8a6f88f34a0ef0b60e0e39ebfcb0dd9a712af. **Status:** [N] actual finite-arm, first-order optical response combining outbound light, inbound light, freely falling emitter and mirror, and proper emitter clock from the **same original 3D Maxwell-sourced K4 metric** whose ten linearized Einstein components passed External Audit Round 629; [PASS] nonzero response with a proper-clock term, zero-source null, exactly quadratic source-amplitude scaling at N12, preliminary optical sampling refinement; [NEGATIVE] severe N12→N16 spatial resolution dependence, so no converged optical number; [OPEN] full diffeomorphism/event-preparation null for THIS sourced metric, independent full 3D spatial arm, exact geodesic shooting, spatial continuum, realistic scale, and any additional Cone quarter-grid interaction. Additive only; protect all earlier original K4/Suzuki/Audit/Sandbox/Muse artifacts.

## Gate 1279 — audit arrival and physical gauge/observer precedents

External Audit Round 629 (canonical v15.1354, SHA **7a8898910fc2742a350ad9c346c02948d387dc42**) independently replayed the exact committed Gravity v15.1351, v15.1352, v15.1353 programs. Every ten-component Einstein residual class, time-step refinement, and no-solid/no-Maxwell negative control PASSED, apart from negligible floating-point reduction-order noise. This closes independent real-space **first-order** Einstein–Maxwell+K4 internal consistency for the finite-resolution sourced physical four-metric, not nonlinear gravity.

The earlier physical optical formalism v15.811 computed the perturbative coasting FLRW photon/free-mirror/proper-clock transfer for supplied harmonic S/V/T metric coefficients, while v15.821 showed a crucial **pure-gauge endpoint/event-label trap**: a fixed coordinate emission label is not necessarily a fixed physical emission event under general coordinate changes. The new gate uses the actual **common Maxwell-sourced** four-metric rather than separately supplied harmonic coefficients. It fixes a physical preparation in the chosen Newtonian/vector gauge: emitter at spatial x=0, mirror initially at x=d, both freely falling with **zero perturbative position and peculiar velocity at emission conformal eta=0**, and a round-trip emission event fixed at eta=0. This specifies an event-anchored perturbative observation within that gauge. It is **not** itself a proof of an arbitrary 3+1 diffeomorphism-invariant optical observable; the v15.821 gauge control must be adapted to the current sourced initial data before that claim.

## Gate 1280 — null rays, geodesic endpoints and proper emitter clock

Use the complete *already-sourced* weak-field four-metric, with `a(tau)=tau/sqrt3`, `eta=sqrt3 log tau`, and the source field amplitude A=.1 (not inadmissibly large A=1). Along an x-directed arm, obtain from the assembled physical metric, **without replacing it with Weyl or a scalar tidal proxy**,

`Phi(eta,x)=−[g00(eta,x)+1]/2`,
`B_x(eta,x)=−g0x(eta,x)/a`,
`s_xx(eta,x)=gxx(eta,x)/a²−1`.

Thus

`ds²/a²=−(1+2Phi)deta²−2B_x deta dx+(1+s_xx)dx²`.

On the *background* photon paths x_out(eta)=eta for 0<=eta<=d and x_in(eta)=2d−eta for d<=eta<=2d, the **first-order null travel-time variation** is

`I_out=integral_0^d [−Phi−B_x+s_xx/2]_(eta,eta) deta`,
`I_in=integral_d^(2d) [−Phi+B_x+s_xx/2]_(eta,2d−eta) deta`.

Spatial ray deflection is second order in a first-order endpoint-arrival variation for the fixed background arm, so this is a first-order eikonal/endpoint calculation, **not** fully integrated null-geodesic shooting. Independently evolve **both** emitter and mirror from their perturbative initial Cauchy state, using the original v15.811 coasting conformal geodesic equation

`delta x''+Hcon delta x'=−partial_x Phi+partial_eta B_x+Hcon B_x`, `Hcon=1/sqrt3`,

with numerical quadrature of the retarded Green response. Do NOT leave the mirror fixed at a coordinate location or treat the emitter as fixed if the gauge exerts a force. The endpoint correction to the two-way conformal reception event is

`I_boundary=2 delta x_m(d)−delta x_e(2d)−delta x_e(0)`.

The measured emitter clock lapse is

`I_clock=integral_0^(2d) a(eta) Phi(eta,x_e=0) deta`,

and the first-order physical emitter proper-time correction, keeping the emission physical event fixed by its initial preparation, is

`delta tau_roundtrip=a(2d)[I_out+I_in+I_boundary]+I_clock`.

Everything is evaluated from **the same single Maxwell-sourced full metric**. Metric spatial sampling at arbitrary x and y=z=0 is exact Fourier trigonometric interpolation on the retained discrete grid, not nearest-neighbor sampling. The time-dependent metric is assembled separately at each optical source/sample time. The t=1 metric is approximated by t=1+1e−8 due to the parent evolution CubicSpline's strictly increasing t grid, with the same a used for constructing the initial perturbation; an initial implementation incorrectly divided the t=1+eps spatial metric by a(t=1), introducing an artificial nonzero **vacuum** optical signal ~3e−11. This bug was caught and fixed; in final source the A=0 vacuum correction is **exactly zero** at machine precision. Preserve this negative finding as a repeatability warning.

## Gate 1281 — actual source-driven numerical optical result and essential negatives

Use comoving arm length d=.045 in the dimensionless model's L=4pi periodic box, tau_em=1, tau_rec_background=exp(2d/sqrt3)≈1.0533352138471728, initial mirror/emitter comoving and freely falling, and the original finite compact Maxwell packet A=.1. This is deliberately a **short** arm within the finite-time weak-field interval to keep the first variation meaningful.

Actually executed local Python/NumPy/SciPy source `/mnt/data/cone_gate/k4_causal_optical_common_metric_v15_1355.py`; its final program printed the following round-trip first-order values, in model time units, with **all terms present**:

| Grid/time slices | A | photon two-way integral | free endpoint correction | proper clock integral | total delta tau |
|---|---:|---:|---:|---:|---:|
| 12³/9 | .1 | +4.147356049117524e−5 | −1.2485839794383402e−7 | −1.489497419451571e−5 | **+1.0250964811055272e−5** |
| 12³/17 | .1 | +4.147396768999038e−5 | −1.2499335216527555e−7 | −1.489545334381598e−5 | **+1.0250651225499479e−5** |
| 16³/9 | .1 | +1.3660935393665754e−4 | −3.3203723952743804e−7 | −5.612172180433478e−5 | **+2.6754424725784933e−5** |
| 12³/9 | .05 | +1.0368390122793031e−5 | −3.121459948595931e−8 | −3.723743548628924e−6 | **+2.562741202763347e−6** |
| 12³/9 | 0 | 0 | 0 | 0 | **0** |

The ratio A=.1 to A=.05 for the total correction is numerically **4** within the 1e−6 assertion, the expected quadratic source-response test. N12 optical time discretization 9→17 changes total by ~3.14e−10 absolute (~3e−5 relative), but N12→N16 changes total by a factor ~2.61. Therefore **spatial convergence FAILS to be established**; the displayed numbers are demonstration of a nonzero source-conditioned response within a specified resolution/gauge/preparation, NOT a continuum forecast. The symmetry-protected x arm has near-zero x-shift at the emitter (source/reflection symmetry), even though the full metric's transverse vector field is nonzero elsewhere and other arm orientations would see different contributions.

The pure-background round-trip emitter proper-time interval is `tau_rec_background−tau_em≈0.05333521385`. The perturbation is a tiny model-normalized shift at A=.1 relative to that background interval; there is **no** conversion to seconds or a measured G. The matched Einstein–Maxwell+**identical K4 action** comparator uses precisely this same metric/source/observer definition and therefore has **exactly zero theory difference by construction**. The nonzero optical shift relative to the background is an ordinary gravitational response of the chosen Einstein+solid model, not a distinctive Cone 1/4 Casimir effect.

## Gate 1282 — reproducibility and next falsification

Canonical additive source `research-notes/k4_causal_optical_common_metric_v15_1355.py`, committed SHA **03e8a6f88f34a0ef0b60e0e39ebfcb0dd9a712af**, loads the audited v15.1351 metric assembly directly, combines it with event-anchored first-order photon paths, both geodesic endpoints and proper clock, and asserts zero-source null, nonzero A=.1 result, A² scaling, and modest 9/17 optical time-step agreement. The local executed test and separately authored GitHub source are mathematically equivalent; exact committed-byte execution and independent Audit replay remain pending.

**AUDIT HANDOFF:** independently replay exact GitHub source and numerical table, inspect the conformal x metric/shift sign and both photon directions, geodesic emitter *and* mirror equations, background flight-time derivative factor `a(2d)`, clock lapse and physical emission-event matching. Verify that the source-driven perturbation at eta=0 was not spuriously erased, that the t=1+1e−8 workaround does not introduce a gauge/initial-state error, and the N12→N16 resolution dependence is properly flagged. Test arbitrary pure-gauge 3+1 perturbations with transformed worldlines and emission event as in v15.821 **within this same transfer algorithm**; a gauge-only transformation should produce zero change in the complete optical proper time. If that gauge test fails, do not promote this numerical signal as operationally invariant.

**NEXT:** improve N24/32/40 source grid convergence, improve optical sampling and interpolation and choose several independent arm orientations/lengths; add independent ODE null-geodesic shooting and direct proper-time integration to test the first-order eikonal approximation, then the pure-gauge/null event-control. Only afterwards use physically realistic source and a calibrated detector to ask for a novel dimensionless observable. A genuinely new Cone gravity prediction requires an extra action-derived 1/4-grid interaction and a nonzero difference from the **identical-source identical-K4** ordinary Einstein comparator. No such new interaction has been found.
