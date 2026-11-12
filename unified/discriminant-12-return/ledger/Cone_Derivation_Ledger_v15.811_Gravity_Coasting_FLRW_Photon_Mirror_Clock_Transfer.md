# Cone Derivation Ledger v15.811 — Gravity: coasting-FLRW causal scalar/vector/tensor photon, free-mirror and proper-clock transfer

**Date:** 2026-11-12 US Eastern. **Parents:** v15.794 audited TT null-ray benchmark, v15.810 exact gauge-controlled local metric photon/mirror/clock transfer, v15.727–750 canonical positive-energy physical source and sourced K4 metric potentials, v15.787/788 independently audited full-Riemann compact-source tidal response. **Classification:** [D] leading linear metric-to-observer coasting FLRW optical transfer for generic supplied harmonic scalar/vector/tensor metric mode, including Hubble-damped freely falling mirror displacements and proper-time reception; [D] independent path/Green integral and flat-limit checks; [N] new Cone-specific interaction or fully retarded physical-source result; [O] insert actual v15.750/788 metric source histories, emission timing choices, both detector arms and complete gauge transformation test in FLRW. **Immediately prewrite HEAD:** 4cd2717d3210e06256305c42b239fc5445a05b55, path absent. All changes strictly additive, no Suzuki collision or certified object modification.

## Gate 416 — a well-defined FLRW optical and mirror boundary-value model

Use coasting a(τ)=τ/sqrt3. In conformal time η with **dη=dτ/a**, take the origin η_e=0 and **a(η)=a0 exp(ℋη)** where the *conformal* Hubble rate **ℋ=a'/a=1/sqrt3** is constant. The perturbative scalar/vector/tensor conformal metric is

**ds²=a²(η){−(1+2Φ)dη²−2V_i dη dx^i+[(1−2Ψ)δij+H_ij]dx^i dx^j}**.

Here Φ,Ψ are the gauge-invariant Newtonian scalar potentials, the transverse conformal vector metric shift V is the one used in v15.721 (V=B_V in that gauge), and H_ij is a tensor TT perturbation. Consider an arm of fixed **unperturbed comoving** length d and direction u with emission at η=0, reflection at η=d and reception at η=2d. For a supplied harmonic metric Fourier mode **exp[−iωη+i k·x]**, define λ=k·u, V=V_i u^i, H=H_ij u^i u^j, x=ωd, y=λd.

The first-order null-photon conformal coordinate travel-time integrals have exactly the same geometric phases as v15.810, replacing L by comoving d:

**O=d(−Φ−Ψ−V+H/2) F(y−x)**,

**I=d(−Φ−Ψ+V+H/2) exp[i(y−x)] F(−y−x)**,

**F(z)=exp(iz/2)sinc(z/2)**.

## Gate 417 — comoving free mirrors carry Hubble damping and vector drag

For freely falling slow mirrors in this conformal metric, linearizing the point-particle geodesic action in the metric and in the first-order mirror displacement yields, for a mirror projection along u,

**δx_u''+ℋ δx_u'=−∂uΦ+V_u'+ℋ V_u**.

For the harmonic mode the force coefficient is

**A=−iλ Φ+(−iω+ℋ)V**.

With initial coordinate displacement and velocity zero at η=0 in this fixed metric gauge, the causal mirror displacement is **δx_u(η)=A exp(iλx0) J_ℋ(η,ω)**, where

**J_ℋ(t,ω)=1/ℋ{[1−exp(−iωt)]/(iω)−[exp(−iωt)−exp(−ℋt)]/(ℋ−iω)}**.

The combined endpoint position correction at the conformal return event is

**M=A[2exp(iy)J_ℋ(d,ω)−J_ℋ(0,ω)−J_ℋ(2d,ω)]**.

This is the coasting FLRW analog of the free mirror term of v15.810 and is not optional if scalar/vector fields accelerate test masses. Preparation at η=0 must be specified; different initial mirror data add homogeneous peculiar-velocity solutions.

## Gate 418 — the correct quantity is the emitting observer's proper return time

The background roundtrip *proper* time is not 2d: **Δτ_background=∫_0^(2d) a(η)dη=a0[exp(2ℋd)−1]/ℋ**. At first order, the perturbation to the emitter-clock roundtrip proper time receives (i) a reception conformal-time shift O+I+M weighted by the scale factor at reception **a_r=a0 exp(2ℋd)**, and (ii) the clock lapse at the beam splitter:

**C=a0 Φ[exp((ℋ−iω)2d)−1]/(ℋ−iω)**.

Thus the full specified source-to-instrument *metric transfer* is

**δτ_RT = a0 exp(2ℋd)[O+I+M] + C**,

for the above prepared free-fall endpoints, emission time and harmonic metric input. This expression is linear in the four projected metric amplitudes Φ,Ψ,V,H. The dimensionless measured perturbation would require division by the background elapsed time and a specified source normalization and actual optical instrument. Even for a nonzero isotropic perturbation, its physically inferred arm length and clock synchronization must be consistently handled; do not compare absolute coordinate delays from unrelated gauge preparations.

## Gate 419 — two independent internal tests and a comparator warning

The additive reproducer evaluates three nontrivial mixed scalar/vector/tensor Fourier input configurations at **ℋ=1/sqrt3**. Each exact closed-form transfer is compared with separately integrated numerical outbound and inbound null paths, the free-mirror Hubble-friction Green integral and the beam-splitter lapse-weighted proper clock; every difference is below **3×10^-12**. It then evaluates the same metric input as ℋ→0 for ℋ=10^-2,10^-3,10^-4 and verifies linear convergence toward the already independently tested flat-space v15.810 photon/mirror/clock result, with error bounded by 0.12 ℋ in the stated normalized example. This is a nontrivial background/flat-limit check but is not an independent fully covariant detector gauge-invariance proof on FLRW; that requires transforming source, worldline Cauchy data and clock labels consistently.

**Reproducer:** research-notes/k4_coasting_photon_mirror_clock_transfer_v15_811.py, additive commit **adeaba7262ef4ac2aa43a8ddae2e6b3eefc4c5a9**. Locally executed numeric integration and analytic limit checks to PASS. No historical edits, no image generator.

**Negative/originality result:** these are standard first-order geometric optics and free geodesics in a standard FLRW relativistic metric. The original K4 action remains the **same Einstein–Hilbert + isotropic relativistic-solid action** as the matched ordinary GR comparator from independently audited v15.760. Therefore the difference in this photon/mirror/clock observable between the two matched descriptions is **zero identically**: a new length scale, operator or gravitational coupling is not selected by this transfer itself.

**HANDOFF — independent audit:** independently derive null coordinate travel-time shifts in the stated conformal metric, the plus sign in **V'+ℋV** for free-fall peculiar acceleration, the exact J_ℋ Green kernel and boundary preparation, the reception a_r and proper clock integral, numerical quadrature checks and ℋ→0 limit. Check v15.810 pure-gauge cancellation and its physically compatible initial worldlines. Do not equate this harmonic FLRW transfer with an actual source-driven K4 far-field signal.

**NEXT:** insert the **same sourced Φ_N(η),Ψ_N(η),B_V(η),γ_T(η)** histories generated from the compact canonical scalar field in v15.750/788 into a time-domain photon-and-mirror transfer and form an explicit two-arm differential observable, with light-travel times inside the source-history coverage. Then independently derive a comparator *new physical operator or selector* if a nonzero Cone-minus-GR residual is sought. The mathematical origin of the geometric 2/3 STF dyad does not fix detector normalization.
