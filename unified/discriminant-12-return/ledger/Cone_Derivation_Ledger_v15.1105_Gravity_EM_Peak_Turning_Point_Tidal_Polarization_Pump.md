# Cone Derivation Ledger v15.1105 — Exact EM turning-point tidal pumping, polarization exchange, and static-field rest-state boundary

**Date:** 2026-11-17 Eastern. **Gravity/Cone track. Status:** [D] two physically distinct transverse Maxwell cavity polarizations in the same weak plus-TT gravitational metric have opposite strain-to-electric/magnetic-energy vertices; [D] phase-resolved instantaneous and smooth finite-pulse work, including a seeded mode's turning-point response; [N] no universal photon rest state, no field-independent gravitational EM startup, no quarter-mesh selector or new gravity coupling; [O] realistic moving cavity walls, material response, actual K4 ADM tidal pulse, full two-way gravitational energy accounting. **Live HEAD immediately prior to ledger write:** ee9a4584f1d1b9033014852b37c9e005ef2ae6e5; v15.1104 belongs to External Audit Round 594, v15.1105 free. Strict additive-only; no certified Suzuki, Audit, Sandbox or Muse files altered.

## Latest ledger, Audit and previous parametric gates
External Audit Round 594/v15.1104, commit 901047a8e0e57f777f0c6a75d91efacbd75935b9, independently rederived and executed all Gravity v15.1100–1103 results, **all PASS with no corrections**, including the finite acceleration pulse and tidal-driven Maxwell cavity. Gravity v15.1103 gave L_y=1/2[(1+h)Qdot²-omega0²Q²], exact weak-TT work dE_y/dt=-hdot Qdot²/2 and first-order finite tidal-pulse energy exchange; its analyzed cavity electromagnetic polarization was A_y(t,x), GW propagating along z. Gravity v15.676–681 had already established standard EM parametric transfer and phase matching, and v15.873–876 ordinary conservative oscillators and Fermi tidal parametric couplings. This entry is narrowly new in the ledger: it tests the user's conjecture **'at a peak of the EM wave, its rest state before accelerating through a node; contraction/expansion then changes kinetic energy'** using the other, equally physical, Maxwell polarization and showing exactly what may pump at a standing-wave turning point.

## Gate 961 — metric action distinguishes electric and magnetic energy coefficients
Consider plus-polarized weak-TT metric ds²=-dt²+(1+h(t))dx²+(1-h(t))dy²+dz², where c=1 in the local Maxwell action. The incident GW travels in z and over the narrow z extent of the cavity h is approximately homogeneous; h can have a smooth finite pulse inherited from the distant source v15.1102, but that source is not solved again here. The EM standing wave varies along x, with vector potential either A_y=Q_y(t)f(x) or A_z=Q_z(t)f(x), normalized so ∫f² and ∫(f')² give unperturbed oscillator frequency omega0. To first order in h, sqrt(-g)=1+O(h²).

For A_y, electric kinetic coefficient sqrt(-g)(-g^{00}g^{yy})=1+h+O(h²); magnetic stiffness coefficient sqrt(-g)g^{xx}g^{yy}=1+O(h²). Thus
L_y=[(1+h)Qdot_y²-omega0² Q_y²]/2+O(h²).
For A_z, electric coefficient sqrt(-g)(-g^{00}g^{zz})=1+O(h²), magnetic stiffness sqrt(-g)g^{xx}g^{zz}=1-h+O(h²). Thus
**L_z=[Qdot_z²-omega0²(1-h)Q_z²]/2+O(h²).**
Both follow from the very same ordinary Maxwell action; the difference is polarization and cavity alignment, not a new EM/G coupling.

The Euler–Lagrange equations and canonical instantaneous energies are
(1+h)Qddot_y+hdot Qdot_y+omega0² Q_y=0,
E_y=[(1+h)Qdot_y²+omega0² Q_y²]/2,
**dE_y/dt=-hdot Qdot_y²/2**;
Qddot_z+omega0²(1-h)Q_z=0,
E_z=[Qdot_z²+omega0²(1-h)Q_z²]/2,
**dE_z/dt=-omega0² hdot Q_z²/2**.
These identities are exact within the explicitly first-order-in-h truncated Lagrangians; omitted O(h²) metric terms and moving boundaries can alter higher-order energy balances. A *constant* h in a fixed support region does not supply continuing energy, since hdot=0. The transfer is work from a time-changing tidal background, with realistic boundary/support work and gravitational backreaction to be accounted for.

## Gate 962 — the standing-wave peak versus crossing: a sharp polarization test
With unperturbed Q=A cos(omega0 t+phi), Qdot=-A omega0 sin(omega0 t+phi), the mode's electric field is proportional to Qdot while magnetic field is proportional to Q. Therefore:
- At a vector-potential **turning point** omega0 t+phi=0 mod pi: Q=±A, Qdot=0, electric field zero, magnetic energy maximal. For y-polarized mode dE_y/dt=0 instantaneously (to first order) but for z-polarized mode dE_z/dt=-omega0² hdot A²/2, generally nonzero and of largest magnitude at fixed hdot.
- At a **node crossing** omega0 t+phi=pi/2 mod pi: Q=0, electric field energy maximal, magnetic field momentarily zero. For y-polarized mode dE_y/dt=-hdot A²omega0²/2, maximally sensitive; for z-polarized mode its first-order instantaneous work is zero.
- At the **tidal strain extremum** hdot=0, BOTH work rates vanish instantaneously regardless of electromagnetic phase. The pump's rate of change, not its amplitude maximum alone, is the instantaneous selector.

For a formal sudden change of h by small delta at fixed canonical momentum p=∂L/∂Qdot and fixed Q, H_y=p²/[2(1+delta)]+omega0²Q²/2 and H_z=p²/2+omega0²(1-delta)Q²/2. At zero strain and with E0=A²omega0²/2 this gives
**Delta E_y/E0=-delta sin²theta+O(delta²)**,
**Delta E_z/E0=-delta cos²theta+O(delta²)**,
theta the standing-wave phase at the change. These are polarization/phase dependent. A discontinuous metric is only an idealized fast-modulation limit, not a physically generated instantaneous gravitational wave; actual smoothly varying h(t) must be integrated using the work equations.

The 'rest state' language refers only to a confined standing mode's temporarily vanishing one field quadrature; a freely propagating electromagnetic null wave has no rest frame or global stop. At a turning point Qdot=0 the EM mode is not energy-free: its magnetic field energy is maximal. Recasting electrostatic energy as automatically 'kinetic' energy is incorrect.

## Gate 963 — smooth finite pulse: opposite phase-sensitive work kernels
With h(t) compact in time and a seeded zeroth-order Q=A cos(omega0 t+phi), integrate the work rates by parts. The exact **first-order** energy transfers are
**Delta E_y/E0=+omega0 ∫ h(t) sin(2omega0 t+2phi) dt +O(h²)**,
**Delta E_z/E0=-omega0 ∫ h(t) sin(2omega0 t+2phi) dt +O(h²)**.
For the *even* finite source pulse of v15.1102, with Hcos(2omega0)=∫h(t)cos(2omega0t)dt,
Delta E_y/E0=+omega0 sin(2phi)Hcos(2omega0)+O(h²),
Delta E_z/E0=-omega0 sin(2phi)Hcos(2omega0)+O(h²).
The opposite signs are a clean polarization comparison in the fixed geometry, not a free gain: energy can be transferred back to the tidal pump depending on phase. The time-domain strain spectral overlap from v15.1103 is retained unchanged; no physical frequency or phase lock is selected by the ±1/4 and ±1/2 arithmetic grids.

For an independent smooth pulse test in c=1 units, choose h(t)=10^-5(1-t²)^4 on |t|<1, zero outside; omega0=2, phi=pi/4 and integrate the y/z Hamilton canonical equations from t=-4 to t=4 with the same initial Q=cos(omega0 t+phi), p=-omega0 sin(omega0 t+phi). Numerical ODE integration (scipy, tolerances 1e-11/1e-12) gives Delta E_y/E0=+7.4935762897e-6 and Delta E_z/E0=-7.4936165968e-6, against first-order Fourier predictions ±7.4935839390e-6. Residuals are O(h²) in absolute magnitude and entirely consistent with the assumptions. This supplement is a local independent numerical check, not a claim of a physical measured GW amplitude.

## Gate 964 — static charge or 'EM rest' background does NOT automatically oscillate
With no initial *oscillating cavity mode* Q=Qdot=0, the homogeneous parametric equations leave the classical mode identically zero. A nonzero static electric field held by electrodes is instead an externally supplied *background* that can source a **linear** GW-to-EM field conversion term in an appropriate polarization, as previously derived in v15.679:
(∂t²-∂z²) a_y = 2E_static ∂t b
for the specified plus-shear and seeded static field. This channel can initiate radiation from zero dynamical signal, but the static field, electrodes, gravitational pump and their stress/energy budgets are compulsory. It is a conventional inverse-Gertsenshtein-type effect, not a universal preexisting electron/charge activation at each wave peak.

A fixed-charge capacitor has U_E=Q_charge²/(2C); changing physical capacitance gives dU_E=-Q_charge² dC/(2C²) at fixed charge, with the difference compensated by work/field/gravity/support. At fixed imposed voltage the external power supply must be included. The geometry alone cannot create net energy without a physical pump. Static EM stress can respond to tidal strain through the usual Einstein–Maxwell stress/work vertex, but there is no universal EM 'rest state' or fixed quantum vacuum pump frequency in this result.

## Gate 965 — reproducibility, new insight and next discriminant
Canonical source `research-notes/k4_tidal_em_turning_point_polarization_v15_1105.py` committed ee9a4584f1d1b9033014852b37c9e005ef2ae6e5. Its exact code matches the locally executed SymPy check with PASS: TT metric coefficients, both Lagrangian energy work identities, canonical impulse turning-point selection and opposite first-order smooth-pulse kernels. Independent numerical finite-pulse ODE check reported above. Independent external Audit pending.

**Positive:** the user's peak-pump picture survives as a **polarization-dependent parametric work law**: at a standing-wave magnetic turning point a TT tide can pump the z-polarized cavity mode at leading order; the orthogonal mode instead pumps at its electric-field peak. **Negative:** this is already implied by standard Maxwell curved-spacetime action; no universal rest-state energy transfer, phase lock, Cone mesh frequency, new tidal operator or parameter-free G emerges. Our *new ledger contribution* is a precise phase/polarization comparison tied to the latest finite source-to-cavity work history, not discovery of classical parametric resonance.

**NEXT:** compute a **same-cavity two-polarization normalized response** to the same finite tidal pulse, including the physical cavity shape, wall motion, quality factors and polarization degeneracy. Test whether any amplitude- or G-independent response ratio is not already conventional Einstein–Maxwell boundary mechanics; continue to keep the K4 EH+same isotropic-solid action as matched comparator and full ADM SVT as open.

**AUDIT HANDOFF:** verify Maxwell metric coefficients for A_y(t,x), A_z(t,x), gauge/divergence constraints for each, physical EM E/B quadratures, both instantaneous canonical work signs, sudden idealization versus smooth pulse, O(h²) numerical residual, nonuniversal rest-state caveat, static field linear inverse Gertsenshtein distinction, lack of a quarter-grid frequency selector. Never conflate static field energy with mechanical kinetic energy or claim G derived.
