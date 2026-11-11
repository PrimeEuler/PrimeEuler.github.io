# Cone Derivation Ledger v15.676 — Gravity lane: can the gravitational quarter-grid parametrically pump EM half-grid waves?

**Date:** 2026-11-11. **Motivation:** owner's proposal that the gravity ±1/4 interlay might act as a parametric oscillator, changing impedance/capacitance at the peaks of EM ±1/2 waves to supply energy. **Status:** [D] standard driven RLC energy/Floquet identities, conservative dynamical pump energy budget, conformally invariant Maxwell null; [C] hypothesized grid→time-frequency/circuit-parameter map; [O] physical gravity action and coupling, energy source, phase lock, new G-free prediction. **Prewrite live HEAD:** b73dc56db3a0790e4ce1fa7df06ea697bd8d9f46 (additive exact reproducer), v15.676 collision search empty. Other audit/Suzuki activity through External Audit Round 539 inspected; no protected changes.

**Provenance / redundancy:** v15.624 explicitly corrects that the established **EM** centered Casimir +1/4 is not the gravitational-sector operator Casimir; gravity ±1/4 vertex alone does not determine a gravity Casimir. v14.985 already has SU(1,1) Schwinger-pair squeeze and continuous shape squeeze but **no physical periodically varying EM capacitance** or pump strength. v13.607 has externally driven SU2 Floquet analysis, and v14.872 has rotating Larmor field sidebands but not a sourced gravity→EM parametric amplifier. v14.700 and v15.673 already show a pure quarter/half grid **spatial scale** change does not create novel normalized tidal Xi. Do not relabel any of these as a discovered pump.

## Gate 192 — exact impedance/capacitance energy-transfer model

For a series RLC with charge Q(t), current I=Qdot, L>0, R_s≥0, and positive time-varying C(t),

**L Qddot+R_s Qdot+Q/C(t)=0**,

**E_EM=(L/2)Qdot²+Q²/(2C(t))**,

and direct differentiation **Edot_EM=−R_s I²−Q² Cdot/(2C²)**.

Thus **decreasing C at a charge/voltage antinode adds energy** and increasing C near charge zero extracts little. At current maximum Q≈0, a capacitor change is less effective; an analogous *inductor* pump instead changes L when current is high. Source mechanical/electrical work is mandatory. A static spatial lattice, however fine, is not a time pump.

Adopt the positive capacitance **C(t)=C0/[1+h cos(Ω t+φ)]**, |h|<1 (the inverse capacitance, rather than C, is exactly sinusoidal). Then

**Qddot+2γ Qdot+ω0²[1+h cos(Ωt+φ)]Q=0**,
ω0=(LC0)^(-1/2), γ=R_s/(2L), Qqual=ω0/(2γ)=ω0 L/R_s.

This is the standard parametrically modulated Mathieu equation. In the weak-modulation/damping rotating-wave regime with Δ=Ω−2ω0, its *maximal amplitude* Floquet exponent is

**σ_+=−γ+Re sqrt[(hω0/4)²−(Δ/2)²]+higher-order corrections.**

At exact 2:1 resonance, the growth condition **h>4γ/ω0=2/Qqual** is a real physical loss threshold; phase decides whether a given seeded quadrature amplifies or deamplifies. This is known physics, e.g. Josephson flux-pumped parametric amplifiers (NJP 15 125013 (2013), DOI 10.1088/1367-2630/15/12/125013), and an LC parametric acoustic sensor (PMC5524589, 2017).

## Gate 193 — exact Floquet monodromy numerical witness, controls and threshold

The accompanying script computes the 2×2 fundamental monodromy by high-accuracy SciPy integration of **the exact equation**, over one pump period T=2π/Ω, and returns σ_max=(1/T) max log|λ_i(monodromy)|. In dimensionless units L=C0=ω0=1 and Qqual=100, damping γ=0.005, the results are:

|h|Ω/ω0|σ_max/ω0|
|---:|---:|---:|
|0|2|−0.00500000|
|0.01|2|−0.00250002|
|0.02|2|−0.00000003|
|0.03|2|+0.00249986|
|0.06|2|+0.00999855|
|0.06|2.02|+0.00611705|
|0.06|2.05|−0.00500000|
|0.06|1|−0.00467621|

Hence the claimed resonance exists; it depends on pump **strength, loss and detuning**, not on a bare u_EM/u_G ratio. The 2:1 frequency condition is necessary near the primary instability tongue, not sufficient for gain.

## Gate 194 — a dynamic gravity/EM coupling supplies conserved pump energy, but its strength is free

Introduce a *separate hypothetical physical pump coordinate* x with conjugate P_x, inertia M and natural frequency Ω_G. A minimal test Hamiltonian is

**H=p_Q²/(2L)+(1+κx)Q²/(2C0)+P_x²/(2M)+MΩ_G²x²/2**,

where 1+κx>0. Hamiltonian evolution implies exact

**dE_EM/dt=+κ Q² xdot/(2C0), dE_G/dt=−κ Q² xdot/(2C0), dH/dt=0**.

There is no energy from geometry alone. If x(t)=X cos Ω_Gt is maintained by an external drive, then **h=κX**, and backreaction energy loss is replaced by the external work source. If κ=0, which is compatible with all the existing factor-grid identities, the two systems are uncoupled and pump transfer is identically zero; κ≠0 gives a different completion with the *same grid*. Thus the grid does **not** select κ or pump energy. No source-derived free oscillatory gravitational coordinate x, metric action, wave frequency or field equation for x has been established in the Cone.

The ratio of vertex scale labels u_G=1/4, u_EM=1/2 is exactly 1/2, but **does not imply Ω_G=2ω_EM** without a physical wavelength/propagation/phase dictionary. If both become actual wavelengths in a common medium with identical propagation speeds, this is a conditional *frequency* identification, still not a coupling/amplitude or phase lock. Further, the v15.624 EM +1/4 Casimir completion **must not** be copied as the gravity operator Casimir.

## Gate 195 — four-dimensional free-Maxwell conformal geometry gives an exact pump-null test

Let S_EM=−(1/4) ∫d⁴x √(−g) g^{μα}g^{νβ} F_{μν}F_{αβ}. Under **pure conformal g_μν→a²(η)g_μν**, √−g scales a^4 while two inverse metrics each scale a^(−2). Their product is **a^4 a^(−2) a^(−2)=1** exactly. Therefore classical free 4D Maxwell action remains unchanged; in a conformally flat background, there is no automatic Mathieu instability or creation of free Maxwell photons from a uniform a(t) scale wave. This does **not** claim the absence of observer-frame redshift or exclude boundaries, material dielectric/inductance changes, anisotropic metric waves, charged matter, quantum anomalies or nonconformal couplings. This is a precise falsification gate for a gravity **uniform-squeeze-only** interpretation of the quarter interlay. See Maxwell field in spatially flat FLRW spacetimes, EPJC 81, 908 (2021), DOI 10.1140/epjc/s10052-021-09698-1.

Known physical gravitational→EM parametric interactions **do** occur in appropriate anisotropic/medium settings and are **not Cone novelty**: e.g. Mahajan & Asenjo, Phys. Rev. E 107, 035205 (2023), DOI 10.1103/PhysRevE.107.035205, and Brandenberger et al., Physics of the Dark Universe 40, 101202 (2023), DOI 10.1016/j.dark.2023.101202; the latter identifies different resonance tongues in vacuum and dispersive media. A claim of Cone-specific gain needs a distinct metric/matter mechanism or a fixed amplitude/phase discriminator beyond these.

## Gate 196 — strict source selector and proposed next discriminant

The user intuition supplies a **physically implementable mechanism** but the Cone has not yet produced the temporal pump or energy carrier. To promote this to a gravitational prediction, specify all of: (1) metric and/or covariant gravity-sector variable x and its source equation; (2) physical Ω_G/ω_EM from quarter/half grid, distinct from just geometric scale; (3) coupling κ=∂ln(1/C)/∂x (or actual covariant Maxwell response tensor) from action; (4) pump source amplitude X, work budget and synchronization; (5) loss Qqual and geometry/calibration; (6) a gain or sideband ratio exceeding the fully calculated conventional Maxwell/electromechanical/GR comparator without importing measured G. The dimensionless threshold **h Qqual/2>1** is standard; not Cone-specific. A physically interesting *null* candidate is testing whether a Cone-sourced nonconformal, time-dependent gravitational shear supplies a fixed κ and a resonant modulation while a conformal-only control remains null.

**Verdict:** [D] parametric peak pumping is viable under explicit time-dependent capacitance/impedance and receives pump energy; [D] exact 2:1 Floquet gain threshold and conformal Maxwell null; [O] the actual quarter gravity grid has **not** been demonstrated to be an oscillator, or to drive EM, or to supply a normalized κ, time frequency, or pump source. No novel G-free gravity observable, G, or independent physical gravitational Casimir follows.

**Reproducibility:** exact SymPy conservation/energy and Maxwell conformal identities, independent 2×2 Floquet numerics, and 8-case table in `research-notes/gravity_em_parametric_pump_v15_676.py` (commit b73dc56db3a0790e4ce1fa7df06ea697bd8d9f46), executed successfully as local producer at `/mnt/data/cone_parametric_gate/reproduce.py`; companion `REPORT.md` archived as `cone_parametric_gate_192_196.zip`. Initial exploratory local sign assertion for sin in C(t) was identified as wrong and fixed *before* publishing; the final energy balance is checked symbolically. No image generator used. No Suzuki/far-tail production affected.

**HANDOFF:** external-audit, gravity, sandbox. Independently check exact C-dot sign, pump energy source Hamiltonian, rotating-wave threshold versus numerical Floquet controls, relation u_G/u_EM versus physical frequency, conformal Maxwell cancellation scope, and novelty comparisons to established Josephson and gravitational/EM parametric amplification. Do not infer gravitational pump from a static grid. If work on a physical gravity-sector action is available, derive its **linearized time-dependent nonconformal metric/constitutive response**, and check whether κ is fixed rather than postulated. Preserve all prior certified objects and Suzuki-quarter parked physical correspondence.
