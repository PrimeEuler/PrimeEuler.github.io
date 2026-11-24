# Cone Derivation Ledger v15.1377 — Source-driven optical pure-gauge null with photon/free endpoints/proper clock

**Date:** 2026-11-24 Eastern. **Gravity/Cone lane.** **Pre-ledger live HEAD:** 9fb8fc67e434837b5086d3bfb334d0ff99c9e0f3. **Status:** [N PASS, scoped] actual v15.1355 photon–free-emitter–free-mirror–proper-clock transfer subjected to a nontrivial coasting-FLRW pure-coordinate perturbation, both without and with same independently Audited Maxwell–K4 metric; [PASS] optical gauge artifact decreases about 4x under 9→17 sampling and is source-independent; [OPEN] general 3+1 diffeomorphism, physically nonzero emission-event displacement, spatial convergence, null-geodesic shooting and independent quarter-grid interaction. All commits additive and all prior Suzuki/Sandbox/Audit/Gravity artifacts unchanged. Historical external Audit Round 630, canonical v15.1356, independently replayed the full v15.1355 source-driven optical result, including N12/N16 spatial nonconvergence and A² source-scaling, and verified all reported bytes and values. Hourly external Audit liveness numbering already occupies through v15.1376; fresh v15.1377 target explicitly checked absent.

## Gate 1283 — apply a genuine diffeomorphism to the existing optical instrument

Following earlier v15.821's optical event-pinning trap, choose a *passive* infinitesimal coordinate transformation in coasting FLRW conformal coordinates, with the explicit generators

`eta_new=eta+T(eta,x), x_new=x+U(eta,x)`,
`T=A_g eta³ cos x, U=B_g eta³ sin x`,

and `A_g=.001, B_g=−.0007, H=1/sqrt3`. Both T and U and their first derivatives vanish on the emission/preparation hypersurface eta=0. Thus in this specifically prepared test, the physical emission event is unshifted at first order; unlike v15.821's nonzero-emission-label examples, no extra event shift is required here. These are nontrivial time/spatial gauge generators, not zero deformation or a constant coordinate offset.

At first order the **full arm-projected physical metric** changes under the diffeomorphism by

`delta Phi=−(T_eta+H T)=−(3A_g eta²+H A_g eta³) cos x`,
`delta B_x=U_eta−T_x=(3B_g eta²+A_g eta³) sin x`,
`delta s_xx=−2(H T+U_x)=−2(H A_g+B_g)eta³ cos x`.

The `s_xx` contains the longitudinal gauge shear and must **not** be replaced by isotropic Newtonian-gauge Psi. Apply the terms directly to **exactly the same** numerical four-metric field supplied by the preexisting v15.1355 source history, without recomputing/altering its Maxwell source, K4 perturbation or Einstein equations. Reuse the actual audited v15.1355 first-order optical algorithm by importing its `experiment` function and temporarily overlaying the metric source `assemble` function; restore the original handle after each test and cache the unchanged complete metric arrays for source-neutral efficiency. Spatial sampling, null integrals, geodesic emitter/mirror displacements and proper clock all run through the same source-driven optical code. The test is not a second, specially tailored pure-gauge transfer formula.

The original source-free conformal metric is genuinely perturbed in coordinates. The separate optical terms are individually nonzero; only the physical combination can cancel if the preparation, two photon paths, geodesic endpoints and emitter proper time are consistent.

## Gate 1284 — local executed pure-gauge and physical-source overlay

Use same L=4π cell, x arm length d=.045, weak Maxwell electric amplitude A_EM=.1, N12 spatial grid and the v15.1355 exact Fourier spatial interpolation. Optical time sampling neta=9,17; internal Maxwell metric source integration nt=7. One set sets A_EM=0 (pure-background gauge null); another sets A_EM=.1 (physical sourced metric with coordinate overlay). The locally executed program reported:

| neta | A_EM | baseline physical delta proper time | transformed optical delta proper time | gauge-induced difference |
|---|---:|---:|---:|---:|
| 9 | 0 | 0 | +2.3214780378900584e−11 | +2.3214780378900584e−11 |
| 17 | 0 | 0 | +6.310959277220218e−12 | +6.310959277220218e−12 |
| 9 | .1 | +1.0250964811055272e−5 | +1.0250988025834896e−5 | +2.3214779623241316e−11 |
| 17 | .1 | +1.0250651225499479e−5 | +1.0250657536458375e−5 | +6.3109588965847875e−12 |

The gauge-induced difference with versus without Maxwell source agrees within 1e−18 absolute; its N9/N17 ratio is ≈3.678, in line with finite quadrature and derivative errors trending toward O(neta^-2). In a separate directly executed gauge-only optical transfer at neta=33 and 65, the pure-gauge residual further decreased to 1.649996751473023e−12 and 4.2208437993545295e−13 respectively, approximately factor 4 at refinement. It is a numerically converging **zero**, not a physical gauge-dependent timing shift. In particular the source-driven optical response ~1.025e−5 is **not removed** by this pure coordinate perturbation.

**Important scope:** This is a first-order linear superposition control at one x-directed arm and one spatially nontrivial pair of gauge generators. It proves neither invariance under arbitrary full 3D gauge transformations nor exact nonlinear coordinate covariance for an emitter/receiver with nonzero event displacement. The original v15.1355 signal is still severely *spatially nonconverged*, N12→N16 factor 2.61; do not promote it to continuum physical prediction or claim a distinct Cone-only effect.

## Gate 1285 — provenance, Audit, next tests

**Actually executed local Python:** `/mnt/data/cone_gate/k4_optical_event_gauge_null_v15_1377.py` imported the actual locally mounted prior v15.1355 program, cached source metric array contents, and ran N9/N17 pure background and sourced overlay comparisons, checking exact source-independence of gauge differences within 1e−12. A separate independently authored direct gauge transfer local test `/mnt/data/cone_gate/k4_optical_gauge_overlay_v15_1375.py` evaluated N9/17/33/65 to establish the asymptotic zero trend. **Additive GitHub reproducer:** `research-notes/k4_optical_event_gauge_null_v15_1377.py`, commit SHA **9fb8fc67e434837b5086d3bfb334d0ff99c9e0f3**, authored with the same cached-parent optical transfer and assertions. Exact committed-byte independent replay has **not yet been performed**, to be requested of external Audit.

**AUDIT HANDOFF:** independently run the GitHub v15.1377 reproducer with v15.1355 and v15.1351 in one clean checkout, verify that all gauge terms have correct passive-diffeomorphism signs, that the metric overlay does not accidentally modify cached physical source arrays, that the physical emitter event is fixed at eta=0 due cubic generators, and that `delta s_xx` includes the missing longitudinal spatial shear. Confirm the N9/N17 null and source-independent differences, and compare the N33/N65 direct gauge-only convergence. Distinguish the source-preserving pure gauge test from an arbitrary metric perturbation.

**NEXT:** independently test a nonzero emission-time generator and its explicit event-label correction, then examine several arm orientations and N24/32/40 with improved Maxwell source spatial convergence. Perform independent null-geodesic shooting for the same assembled physical metric and compare first-order timing. Then compute physical detector response relative to **exact same Einstein–Maxwell+identical K4 comparator**; that matched-theory difference is zero until a genuinely independently action-derived quarter-grid interaction enters. No such gravitational interaction, SI calibration, or G-free dimensionless novel observable has been established.
