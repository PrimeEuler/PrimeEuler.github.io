# Cone Derivation Ledger v15.1103 — Finite acceleration-generated tidal wave parametrically transfers energy to a transverse seeded EM cavity

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] ordinary Einstein–Maxwell first-order weak-TT tidal coupling of a specified transverse cavity electromagnetic mode; [D] exact first-order finite-pulse phase-sensitive work and Fourier/spectral overlap using the **specific** two-mass v15.1102 quadrupole waveform; [N] no quarter-grid/Cone frequency, coupling or h amplitude selected, no background-free classical oscillation from precisely zero fields; [O] true K4 ADM-constrained source, complete charged/actuator stress, cavity mechanical boundary and gravitational backreaction. **Immediately prewrite live HEAD:** 1d35eb728c6965a123bac45b904fb26c48139ed1. Collision checked for v15.1103; strictly additive; protected Suzuki, prior Audit, Sandbox and Muse unchanged.

## Audit, precedent and exact goal
Latest completed External Audit Round 593/v15.1099, commit 232b5900a66075575db14d93f37bee4e48813838, independently verified earlier v15.1093–1098; Gravity v15.1100–1102 have not yet been externally audited. This is NOT a rediscovery of gravity-to-EM parametric transfer. Gravity v15.676–681 already proved generic RLC/EM modulation, GW-to-photon amplitude/momentum selection, and the distinction between a static B0/E0 seeded inverse Gertsenshtein channel and unseeded two-photon parametric transfer. Gravity v15.873–876 already analyzed conservative oscillator phase transfer and local Fermi tidal dynamics. Published comparator: Brandenberger, Delgado, Ganz and Lin, *Graviton to photon conversion via parametric resonance*, Physics of the Dark Universe 40 (2023) 101202, https://doi.org/10.1016/j.dark.2023.101202, reports that the first parametric band is absent for its **traveling vacuum plane-wave** configuration and appears in appropriate subluminal media. Do not transplant a homogeneous-metric Mathieu result directly to collinear vacuum waves. A 2026 proposal for quantum cavity-based transduction, https://arxiv.org/abs/2603.27687, explicitly exploits cavity confinement to break momentum and isotropy symmetry. Our *new narrow gate* is to insert the **actual finite gravitational waveform derived in v15.1102** into a definite, noncollinear cavity mode and quantify its seeded phase-sensitive transfer without confusing the two earlier branches.

## Gate 957 — metric Maxwell action supplies the parametric EM coefficient
Consider a small plus-polarized GW traveling in +z and a transversely oriented cavity with EM standing-wave vector along x, electric potential A_y(t,x)=Q(t) sin(kx) and proper support narrow along z compared with the GW's characteristic wavelength. Assume fixed ideal reflecting boundary conditions, a well-isolated EM mode, and negligible backreaction. The weak TT metric, locally over the narrow z aperture, is
ds²=-dt²+(1+h(t))dx²+(1-h(t))dy²+dz², in units c=1 for this local field-action derivation, with |h|<<1.
For A_y the Maxwell action -1/4 ∫ sqrt(-g)F² has electric coefficient sqrt(-g)(-g^{00}g^{yy})=1+h+O(h²) and magnetic coefficient sqrt(-g)g^{xx}g^{yy}=1+O(h²). After ordinary spatial-mode normalization, the quadratic effective mode Lagrangian is
**L_EM=1/2 [(1+h)Qdot²-omega0² Q²]+O(h²)**.
Consequently
**(1+h)Qddot+hdot Qdot+omega0² Q=0**.
The canonical instantaneous mode energy, E=1/2[(1+h)Qdot²+omega0² Q²], obeys the exact-for-this-truncated-L equation
**dE/dt=-(1/2)hdot Qdot²**.
This is standard Maxwell coupling to gravitational shear, not a newly invented free pump constant. The gravitational strain is imposed from the remote source; energy gained by the EM mode must come from the incident tidal field together with external boundary/support work in a fully conservative model.

This cavity deliberately breaks translation symmetry along x, and it is transverse to the GW propagation direction. A freely propagating vacuum EM plane wave *collinear* with a massless traveling GW has the leading TT pair vertex zero in the corresponding idealized channel (v15.679), so the transverse cavity result cannot be generalized to a vacuum, infinite, freely traveling wave instability. Static B0/E0 seed conversion (inverse Gertsenshtein) is a separate **linear drive**; it requires an externally supported field and is not the homogeneous zero-field parametric effect tested here.

## Gate 958 — exact first-order work for an existing EM seed
Treat h=O(epsilon_g) as weak, with a pre-existing unperturbed seeded solution Q0(t)=A cos(omega0 t+phi). For h vanishing at ±infinity, first-order energy change is
Delta E=-(1/2)∫ hdot Qdot0² dt
= +(1/2)∫ h d/dt(Qdot0²) dt
= (A² omega0³/2)∫ h(t)sin(2omega0 t+2phi)dt.
Because E0=A²omega0²/2, the **fractional first-order transfer** is
**Delta E/E0=omega0 ∫ h(t)sin(2omega0 t+2phi)dt+O(h²)**.
Our finite pulse is even in time about its center, hence
**Delta E/E0=omega0 sin(2phi) Hcos(2omega0)+O(h²)**,
where Hcos(2omega0)=∫ h(t)cos(2omega0 t)dt.
For a zero phase seed phi=0, first-order net work is zero for this symmetric waveform; phi=pi/4 maximizes its signed magnitude, with sign controlled by h's Fourier coefficient. An initially vanishing **classical** cavity mode Q=Qdot=0 stays zero under this homogeneous linear equation. Quantum spontaneous pair creation requires a separate quantized field calculation and cannot be conflated with classical generation from static charge. A pre-existing static electric or magnetic field can instead produce an O(h*E0) or O(h*B0) driven response per v15.679.

## Gate 959 — finite v15.1102 accelerated quadrupole yields a closed spectral overlap
Use the previously derived finite two-mass GR plus strain, as a *conventional weak-field far-zone comparator* at the cavity:
h(t)= 4Gm/(c^4 D) [xdot(t)^2+x(t) xddot(t)],
x(t)=x0+epsilon g(t/T), g(s)=(1-s²)^4 for |s|<1 and zero outside.
We write the retarded-time origin so the pulse is centered on t=0 at the detector. This **G-dependent** strain is supplied by v15.1102, not derived from Cone's gravitational quarter grid. Let xi=2omega0 T, and define real compact shape transforms
F_n(xi)=∫_-1^1(1-s²)^n cos(xi s) ds.
Then
h(t)= [4Gm/(c^4 D T²)][x0 epsilon g''(t/T)+(epsilon²/2)(g²)''(t/T)].
By two integrations by parts (all required endpoint derivatives vanish), the **exact leading-order strain transform** for this prescribed quadrupole pulse is
**Hcos(2omega0)= -[4Gm/(c^4 D T)] xi² [x0 epsilon F_4(xi)+(epsilon²/2) F_8(xi)]**.
It follows that
**Delta E/E0 = -[4Gm omega0/(c^4 D T)] xi² sin(2phi) [x0 epsilon F_4(xi)+(epsilon²/2)F_8(xi)] + O(h²)**.
This is dimensionless. It contains the *physical* externally specified source parameters (G,m,epsilon,x0,T,D) and resonator omega0, not a new G-free tidal constant. In particular \int h(t)dt=0 for this compact quadrupole pulse; the low-frequency Fourier factor is suppressed as xi². A finite pulse's peak strain by itself is insufficient to predict transfer; the **spectral overlap** at twice the mode frequency is decisive. The source pulse is not eternal or periodic, so a Mathieu long-time exponential Floquet exponent cannot simply be assigned.

Exact checks of the bump moments give F_4(0)=256/315, F_8(0)=65536/109395. Numerical high-precision quadrature checks give F_4(pi)=0.5102410680256 and F_4(2pi)=0.09162140342465; the linear-in-epsilon first-order spectral factor -xi²F_4 at xi=pi is -5.035877490602. The reproducer checks the Fourier-by-parts identity directly at xi=0.4, pi, 2pi, and 11 with 40-digit precision, including a nonlinear epsilon² contribution (tested as a 1/4 shape factor).

## Gate 960 — selection rules, source limitations and physical verdict
The orientation of the EM mode relative to the GW matters. The ideal collinear traveling plane-wave vacuum TT pair vertex is zero at leading order, unlike the transversely oriented, boundary-confined mode above. Even this cavity calculation assumes the tidal wave is locally homogeneous **across the narrow z-direction**, which can be arranged independently of its x-axis longitudinal resonance dimension. Real cavity walls are elastic, and a physical GW can also move/deform them; boundary terms, losses, quality factor, material response and finite spatial wavefront curvature are essential for an actual instrument. The full v15.1102 source has only a Newtonian integrated actuator-stress identity, not a fully covariantly conserved charged/Maxwell/driver stress, and its K4 coasting solid's constrained SVT retarded tidal field remains open. Thus this gate is a valid *standard weak-GR imposed-pulse* model, not a fully sourced Cone prediction or an energetic generator proposal.

There is no new coupling from the gravity ±1/4 versus EM ±1/2 lattice, no derived drive frequency from the confocal acceleration secant, no Compton-scale orbit selected and no normalized new G-free observable. This sharpens the research question: whether the confocal secant/quarter-grid can derive the **spectrum of the physical tidal pulse** or a phase-lock boundary condition without externally prescribing x(t), T, mode omega0 or seed phase. Until then the derived transfer is ordinary Einstein–Maxwell parametric work.

**Reproducer:** research-notes/k4_finite_tidal_pulse_em_parametric_v15_1103.py, additive commit 1d35eb728c6965a123bac45b904fb26c48139ed1. An equivalent full script was executed in the local container (exit 0): SymPy source-strain equality, integrated Maxwell mode energy equation, compact shape moments and high-precision independent numerical Fourier/integration-by-parts checks all PASS. Exact committed script is a close transcription; independent committed-byte Audit remains pending.

**AUDIT HANDOFF:** reexecute committed script and verify all factors and units in Maxwell TT mode action, energy-work sign, gravitational waveform normalization inherited from v15.1102, exact two-derivative shape transform, 0 and pi/4 seed-phase rules, collinear plane-wave TT suppression versus transverse cavity coupling, plus full K4 and actuator limitations. Note that the finite-pulse **spectral-overlap calculation** and source-specific first-order energy transfer are the contribution; generic parametric pumping and inverse Gertsenshtein were already present in earlier ledger v15.676–681 and v15.873–876.

**NEXT:** construct an explicit, jointly conserved source-to-wave-to-cavity energy budget including cavity supports and energy flux, or derive a selection law for the source pulse's temporal spectrum from confocal/quarter-grid action rather than choosing it. Test matched standard GR+elastic solid predictions with identical apparatus before claiming a Cone-only effect.
