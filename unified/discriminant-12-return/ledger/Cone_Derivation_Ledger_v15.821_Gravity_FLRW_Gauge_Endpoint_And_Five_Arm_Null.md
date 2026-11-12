# Cone Derivation Ledger v15.821 — Gravity: coasting-FLRW pure-diffeomorphism photon/mirror/clock/emission-event cancellation and five-arm gauge null

**Date:** 2026-11-12 US Eastern. **Parents:** v15.794 photon roundtrip TT benchmark; v15.810 local Minkowski pure-gauge null; independently audited v15.811 coasting-FLRW photon/mirror/clock transfer; independently audited v15.812 and v15.818 positive-energy canonical matter source to optical responses; independently audited v15.815 five-helicity optical geometry. **Audit:** Round 561/v15.819 independently confirmed v15.815/816/818 and source-only v15.817 with a small numerical text correction, recorded additively as v15.820. **Immediately prewrite live HEAD:** 2710513ba0f60e56b42999a995164c9f043980fb. Target absent; additive-only, Suzuki and historical certified files untouched.

**Status:** [D] explicit off-shell pure-diffeomorphism metric gauge transformation and exact photon/worldline/clock endpoint cancellation in conformal coasting-FLRW; [N] the previously unaccounted emission-event label can produce a spurious individual-arm optical coefficient at nonzero conformal emission time; [D] this common bias cancels in all five equal-arm differential channels in a nine-arm geometry; [O] arbitrary spatially varying 3+1 diffeomorphisms, boundary and emitter clock preparation transformations on on-shell full K4 sources, non-equal arms and realistic emitter/receiver separation.

## Gate 440 — transform *events and worldlines*, not only metric coefficients

Work in conformal time η on the coasting FLRW background **ds²=a(η)²(−dη²+d\mathbf x²)** with **a(η)=a0 exp(ℋη)** and **ℋ=1/sqrt3**. Restrict initially to one detector arm coordinate x, and apply an infinitesimal *passive* diffeomorphism

**η_new=η+ε T(η,x), x_new=x+ε U(η,x)**.

On the arm, the pure-gauge perturbed metric in the same sign conventions as v15.811,

**ds²=a²{−(1+2Φ)dη²−2V dη dx+(1−2Ψ_arm)dx²}**,

has

**Φ=−(T_η+ℋ T), Ψ_arm=ℋ T+U_x, V=U_η−T_x**.

The label Ψ_arm is an *arm-projected spatial metric coefficient*: away from a one-dimensional projection, an arbitrary spatial diffeomorphism generates scalar shear and possible vector components, and **must not** be silently restricted to Newtonian-gauge isotropic Ψ alone. A pure diffeomorphism changes coordinates but not physical optical travel times when worldlines and physical emission/reception events are transformed consistently.

For independently quadrature-testable examples choose

**T=A η³ exp(−iωη+iλx), U=B η³ exp(−iωη+iλx)**.

The η³ factor ensures both gauge displacement and first derivative vanish on the initial η=0 slice, so the freely falling mirror preparation with initial perturbative coordinate displacement/velocity zero is compatible in both descriptions. Complex coefficients are Fourier controls, with real fields obtained by pairing conjugates.

## Gate 441 — exact nontrivial photon, free-mirror and proper-clock cancellations

The free-mirror longitudinal conformal geodesic equation of v15.811 is

**δx''+ℋ δx'=−∂xΦ+V'+ℋ V**.

For the pure gauge above, the force simplifies **identically** to

**−∂xΦ+V'+ℋ V=U''+ℋ U'**.

Thus the freely falling physical mirror coordinate perturbation is **δx=U** with the correctly transformed initial conditions. Define an arm of comoving length d, physical emission at reference conformal time η_e, unperturbed mirror reflection at η_e+d and reception at η_e+2d. Let **T_e=T(η_e,0)**, **T_r=T(η_e+2d,0)**, and scale factors **a_e=a(η_e)**, **a_r=a(η_e+2d)**.

Direct integration of the usual outbound/return *unperturbed null paths* and the mirror/end-point correction gives

**O+I+M=T_r−T_e**.

The emitter proper-clock lapse contributes

**C=∫_(η_e)^(η_e+2d) a(η)Φ(η,0)dη=−a_r T_r+a_e T_e**,

because **aΦ=−(aT)'**. Consequently the previously used *fixed-coordinate-emission-label* optical combination is

**δτ_fixed=a_r(O+I+M)+C=−(a_r−a_e)T_e**.

This is GENERALLY NONZERO at η_e>0, despite the spacetime being exactly the original FLRW metric in different coordinates. It measures the difference in the *identified emission event*: keeping η_e fixed as a coordinate label after the diffeomorphism is not the same physical emission event.

The physical emission-event shift contributes the background proper-time interval change

**δτ_emission=(a_r−a_e)T_e**,

so the complete physically event-anchored result is

**δτ_physical=δτ_fixed+δτ_emission=0**.

At η_e=0 for the η³ generators, T_e=0 and the fixed-coordinate quantity already vanishes. At η_e>0 the extra term is required for an individual-arm absolute round-trip proper-time perturbation.

## Gate 442 — direct numerical integration and the nine-arm equal-length control

The reproducer numerically integrates outbound and inbound photon null paths, the Green kernel of the FLRW Hubble-damped mirror equation, and the emitter proper-clock lapse. Independently it evaluates the exact transformed endpoint functions T,U. In five nontrivial combinations of A,B,ω,λ,d,η_e, all exact endpoint identities pass and the *full physical* proper-time change vanishes with residuals below 2×10^-11 (typically 10^-18–10^-16).

Example **A=0.17, B=0.12, ω=1.1, λ=0.8, d=0.23, η_e=0.08**:

**δτ_fixed≈−2.76208683959306×10^-5+2.43693019798610×10^-6 i**,

**δτ_emission≈+2.76208683959304×10^-5−2.43693019798048×10^-6 i**,

**δτ_physical≈−1.5×10^-19+5.6×10^-18 i**.

Now use the exact **nine arms** from the v15.815 five-helicity detector: **n,e,b,(n±e)/sqrt2,(n±b)/sqrt2,(e±b)/sqrt2**, with K=(2,0,1), a common arm length d=0.075 and emission η_e=0.08. For the same general *three-dimensional* Fourier gauge generator with spatial vector amplitude **X=(0.12,−0.06,0.08)**, each arm receives its correctly projected U=u·X and λ=K·u. Every arm's fixed-coordinate pure-gauge optical response has the *same* nonzero endpoint-label bias **−(a_r−a_e)T_e**, independent of arm direction, because each has the same emission event and return time. Therefore all five equal-arm differential outputs cancel to numerical roundoff (~10^-19), even **before** adding the common physical emission-event correction. This is a useful gauge-null property of that geometry.

The calculation involves the *full arm-projected* gauge-generated spatial metric including the projected shear. It does not assert that simply inserting Newtonian-gauge scalar Ψ into an arbitrary diffeomorphism creates a complete 3D transformation. Nor does it replace a proof of the source/mirror/clock observable under all 3+1 cosmological gauge transformations and nontrivial source perturbations.

## Gate 443 — implications for previous detector numbers

**Positive:** the optical transfer has a nontrivial explicit coasting-FLRW pure-gauge control with photon, geodesic mirrors, proper emitter clock and emission-event identification. Its nine equal-arm differential signals are confirmed immune to this specific common bias. The local Minkowski gauge null in v15.810 and the finite-arm coasting transfer in v15.811 are thereby linked by a genuine background-dependent boundary test.

**Negative/caution:** the absolute single-arm numbers of v15.811, and the fixed-η_e source-to-detector inputs of v15.812/818, cannot be presented as *unconditionally cosmologically gauge invariant* without specifying the transformed physical emission event and observer/mirror preparation. This does **not** invalidate their already independently audited numerical outputs in their specified coordinate gauge, nor does it show their equal-arm differential signals are gauge artifacts. The particular bias tested here cancels from those equal-arm differentials; complete arbitrary-gauge invariance remains open.

**Reproducer:** research-notes/k4_flrw_gauge_endpoint_control_v15_821.py, additive commit **4a33589cfcf2f6c6b0fe3f3d1be372f41f766a34**. Equivalent local Python program executed to PASS for multiple independent quadratures, endpoint identities, zero physical proper time under pure gauge, nine-arm five-difference null. The newly committed file awaits external post-commit independent audit. No image generation or prior source rewrite.

**HANDOFF — external audit:** rederive the passive FLRW diffeomorphism signs and spatial shear, photon/mirror/end-event identities and clock integral; reproduce the explicit nonzero coordinate-emission bias, its event correction, and five equal-arm nulls. Distinguish the *special pure-coordinate test* from a universal on-shell gauge covariance theorem, and check event-preparation consistency for the physical source-driven v15.818 numerical response.

**NEXT:** quantify the unequal-arm false differential if emission events are not correctly reidentified, then implement a full general 3D cosmological gauge transformation of the metric, canonical source, moving worldlines and photon clock data. Preserve the exact conventional GR+solid matched-action novelty null until an independently selected Cone interaction is derived.
