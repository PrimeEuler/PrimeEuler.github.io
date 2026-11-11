# Cone Derivation Ledger v15.679 — Gravity lane: propagating K4 tensor–EM phase matching, TT pair-vertex suppression, and static-field generator seed

**Date:** 2026-11-11, US Eastern. **Motivation:** owner proposes gravity interlay ±1/4 as EM ±1/2 wave parametric pump and remarks that preexisting static charge could supply a seed/generator configuration. **Parents:** v15.624 explicit EM +1/4 Casimir vs distinct unknown gravity Casimir; v14.925–928 and v14.935 K4 elastic solid, coupled SVT stability and tensor dispersion; v15.673 G-free tidal Poisson source; v15.676 externally modulated RLC Floquet pump with sourced energy requirement; **v15.678** homogeneous anisotropic shear Maxwell amplification and K4 coasting oscillation. **Status:** [D] exact local momentum matching, first-order transverse-traceless Maxwell vertex in a chosen polarization, static-electric-background linear source; [C] WKB transfer of time-dependent cosmological K4 tensor dispersion to local approximately stationary three-wave interaction; [O] self-consistent coupled Einstein–Maxwell–solid wave production, actual Cone G/EM grid frequency selection, physical pump amplitude and new G-free observable. **Immediately prewrite live HEAD:** d0b31d44d2fbdd932eebf3a068f27ae11863fcf1 (new additive reproducer); v15.679 ledger collision search empty. No protected Suzuki/far-tail modification, no new physics asserted from Suzuki quarter.

**Reference comparators:** Brandenberger, Delgado, Ganz, Lin, *Graviton to Photon Conversion via Parametric Resonance*, Physics of the Dark Universe 40 (2023) 101202, DOI 10.1016/j.dark.2023.101202 (massless traveling GW: no first vacuum resonance band, medium reopens it); Domcke, Garcia-Cely, Lee, *Gravitational Wave Scattering on Magnetic Fields*, JCAP 11 (2025) 016, DOI 10.1088/1475-7516/2025/11/016 (inverse Gertsenshtein conversion with static background magnetic fields); *Challenges and opportunities of gravitational-wave searches above 10 kHz*, Living Rev Relativity (2025), DOI 10.1007/s41114-025-00060-5. These are **conventional GR electrodynamics** comparators, not Cone predictions.

## Gate 202 — traveling-wave energy and momentum selection

In a local adiabatic/WKB patch, an approximately monochromatic traveling shear pump has physical four-frequency (Ω,K zhat). Two generated photon modes obey **Ω=ω₁+ω₂** and **K zhat=k₁+k₂**. Consider the symmetric pair k₁=(+q,0,K/2), k₂=(−q,0,K/2), with each photon obeying ω=v sqrt(q²+K²/4), v=1 for ordinary vacuum Maxwell and v<1 for an ideal nondispersive isotropic medium. Then the exact phase-matching condition is

**q²=[Ω²/v²−K²]/4**.

For an ordinary **massless** vacuum GR traveling wave Ω=K and v=1, q=0: the resonant photons must be collinear. Their transverse-traceless gravitational interaction vanishes at the linear-in-shear vertex in this configuration. This is not the homogeneous spatially uniform time-modulation case v15.678 and does not forbid all GR GW→EM conversion or higher resonance tongues.

In ordinary matter with v<1 and Ω=K, the first phase-matched channel opens **q²=K²(1−v²)/(4v²)>0**, in agreement with the established medium-enhanced parametric resonance literature. Material dispersion/loss and the pump amplitude must still be supplied; this is not novel Cone physics.

## Gate 203 — exact TT plus-polarization vertex tests the apparent K4 opportunity

Use the same explicitly prescribed weak plus-shear geometry as v15.678, now with **b=b(t,z)**:
ds²=−dt²+e^(2b)dx²+e^(−2b)dy²+dz².

For one y-polarized EM potential A_y(t,x,z), with zero charge/current and a simple uniform isotropic medium whose electric permittivity ε=1/v², the exact Maxwell-like quadratic density in these coordinates is

**L_y=1/2 e^(2b)[ε(∂t A_y)²−(∂z A_y)²]−1/2(∂x A_y)²**.

The O(b) interaction is **b[ε(∂t A_y)²−(∂z A_y)²]**. Insert two positive-frequency modes with k₁z=k₂z=K/2 and common ω=Ω/2. Their resonant pair coefficient is

**V_pair ∝ −ε ω²+K²/4=−q²**.

Thus the massless vacuum collinear first-order vertex indeed vanishes identically, not just because frequencies happen to match. The result applies to this explicit TT + polarization and y-polarized photon pair; it is not an exhaustive classification of all independent polarizations or higher-order processes.

The **existing** K4 elastic-solid TT action (v14.928/v14.935) gives a local WKB tensor dispersion **Ω²≈K²+m_T²**, with **m_T²=(8η/3)H²**. It is *timelike* at positive η even in the locally vacuum EM sector. For the symmetric photon pair in vacuum (v=1), the same exact algebra now permits

**q²=m_T²/4=(2η/3)H²>0**,

so the TT vertex is algebraically nonzero. This is a **conditional positive K4-versus-flat-GR kinematic difference**, contingent on the actual field-completion, background, WKB regime, and sourcing of the tensor mode. It does **not** imply a sustained Floquet instability or a measured new observable. Local-background curvature and standard cosmological Maxwell effects must be included in any precision GR comparison; the flat vacuum GR massless comparator by itself is not the full cosmological baseline.

## Gate 204 — quantify K4 opening: very small for subhorizon propagating waves

The previously certified local K4 stable interval is **3/8<η≤3/2**, with η unselected by Cone geometry. Accordingly **m_T²/H²=8η/3∈(1,4]**, and in the WKB regime K≫H,

**q/K=√(2η/3) H/K**, **|V_pair|/K²=(2η/3)(H/K)²**.

At K/H=100, q/K ranges just above 0.005 to 0.01, and the dimensionless TT coefficient ranges just above 2.5×10^(−5) to 10^(−4). At K/H=1000, q/K ranges 0.0005–0.001 and vertex/K² ranges 2.5×10^(−7)–10^(−6). These are NOT gain rates or experimental conversion probabilities: they are dimensionless *kinematic vertex suppression factors*. Physical gain depends on shear amplitude, coherent interaction time/length, damping, source flux and the correctly normalized gravitational sector. The quarter-grid u_G=1/4 vs u_EM=1/2 does not pick η, H, tensor momentum K, shear amplitude, phase or coupling.

In coasting K4 cosmology H changes, m_T²∝H²; exact global energy conservation and a constant Floquet rate cannot be assumed. Local WKB is only self-consistent for K/H≫1, exactly where the opening is strongly suppressed. The η window is a theoretical local linear-stability window, not an observational validation of that cosmological model.

## Gate 205 — **static charge/field** provides a distinct, linear-order generator seed

The user's observation that charge can already sit in a system points to a DIFFERENT channel from spontaneous two-photon parametric production. Add to the same exact Maxwell equation a static, externally prepared homogeneous transverse electric field E_y=E₀, locally represented by **A_y^(0)=−E₀t**. Let b(t,z) be weak and A_y=−E₀t+a_y(t,z). Then

**∂t[e^(2b)∂t A_y]−∂z[e^(2b)∂z A_y]=0**

linearizes exactly to

**(∂t²−∂z²)a_y=2 E₀ ∂t b**.

Thus an oscillating gravitational shear can **linearly convert a pre-existing static EM background into radiative EM**; the wave amplitude is first order in the gravitational strain times seed field, rather than the two-photon instability growth rate. This is in the conventional inverse Gertsenshtein family (usually a static *magnetic* background). For a real charged capacitor or inductor the supporting electrodes/current, finite spatial region, boundary impedance, polarization and self-consistent energy exchange cannot be omitted. A lone static charge is not automatically a resonant electromagnetic mode; the gravitational wave/pump must supply energy, and any externally held static field is an essential source input.

The linear seed-field conversion can occur for standard **massless GR** gravitational waves; unlike the first-order vacuum two-photon parametric resonance it does not require m_T²>0. Hence merely observing seed-mediated EM emission does **not** establish a Cone-specific gravitational response.

## Verdict, reproducibility and audit

**Positive conditional discovery:** the existing K4 shear tensor mass would kinematically reopen a first-order traveling-wave photon-pair channel closed for the ideal flat-vacuum massless-GR comparator, with explicit TT vertex proportional to m_T². **Negative observational test:** the channel is suppressed as (H/K)² in its own valid subhorizon WKB regime; the tensor/matter source still does not select amplitude, η, or the EM/G time-frequency correspondence. **Separate generator path:** static electric or magnetic fields allow ordinary linear gravitational-to-EM conversion with no initial EM oscillation, exactly matching the owner's 'charge waiting for movement' intuition, but this is already conventional Einstein–Maxwell physics, not an independent Cone force law. No Newton G or parameter-free gravity prediction is claimed.

Exact SymPy reproducibility script `research-notes/propagating_k4_tensor_em_pair_and_seed_v15_679.py` committed at d0b31d44d2fbdd932eebf3a068f27ae11863fcf1; independently executed fuller local script and report in `cone_propagating_k4_gates_202_205.zip`, local script SHA256 6a18294ae8bda812f705887cfae75a2253d9ff3f0b8fc6e0a6c9fc92a063531c. Checks phase/momentum constraints, TT pair vertex, ideal nondispersive medium reopen, K4 suppression across eta/K tables, and exact Maxwell expansion around a static electric field. No generated figures, no protected Suzuki changes.

**HANDOFF** to independent audit/gravity/sandbox: verify linearized Maxwell Lagrangian including spatial q gradient, collinear TT null for on-shell massless vacuum pump, qualified WKB K4 timelike dispersion and q²=m_T²/4, suppression factor (H/K)² (not a gain), whether standard cosmological background yields similarly small corrections, and seeded static-E source sign/factors plus inverse Gertsenshtein attribution. Flag any claim the quarter grid *causes* a 2:1 frequency lock: no such deduction. Preserve all protected Suzuki certificates and additive ledger protocol.

**Next:** test finite-size capacitor/solenoid boundary EM modes against a passing GR/K4 tensor with realistic phase matching. The most meaningful discriminator would be a normalized sideband/polarization ratio after standard inverse Gertsenshtein/matter response subtraction, with shear amplitude and η independently constrained. If none is fixed by the geometric sector, close as an engineering mechanism rather than a new gravitational prediction.
