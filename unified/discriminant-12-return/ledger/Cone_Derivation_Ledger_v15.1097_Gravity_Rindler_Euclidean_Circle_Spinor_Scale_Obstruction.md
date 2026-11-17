# Cone Derivation Ledger v15.1097 — Acceleration parabola, Euclidean Rindler circle and spinor holonomy do not select the Compton scale

**Date:** 2026-11-17 Eastern. **Gravity/Cone track.** **Status:** [D] exact Euclidean Rindler circumference and smoothness angle, common radius with the chart-defined acceleration hyperbola's osculating circle, standard spin-half double-cover sign and Unruh/Compton ratio; [N] no unique dimensionless ratio rho, radius or physical G-free new observable; [O] an independently selected spin-current/acceleration or spectral boundary-value problem. **Live HEAD immediately before writing:** 98d9f843f40baa30d726c6bcd9e22330ec19c2db (this gate's reproducer). Additive only. No edits to Suzuki, Audit, Muse, Sandbox or historic certificates.

## Live ledger and collision/redundancy
The last independently finished Audit Round 592/v15.1092 (commit ba571054759c6b4d727c33db57812ef483923871) verified Sandbox v15.1091 Zitterbewegung/curl and earlier Gravity v15.1089–1090. Gravity v15.1093–1096 are awaiting independent Audit. Earlier Gravity v15.886 already showed Rindler-length/Compton-length match is merely conditional and leaves rho free. Gravity v15.1096 found the acceleration parabola focus f=c²/(2a) equals the idealized ZB radius hbar/(2mc) if and only if rho=1. Gravity v15.1095 found Gaussian spin-current magnetic energy ~L^-3 with arbitrary localization L. This v15.1097 gate asks whether *Euclidean Rindler regularity or spin-half sign* independently fixes rho, rather than repeating the coordinate circle coincidence.

## Gate 937 — Rindler metric Euclidean circle and factor-of-two structure
For a uniformly accelerated trajectory of proper acceleration a>0 in flat Minkowski spacetime, define R=c²/a and Rindler spatial coordinate r>0 such that the 1+1 physical metric in its right wedge is
ds²=-(a r/c²)² c² dt_R²+dr².
The observer at r=R has proper time t_R. Wick rotate t_R -> -i t_E and set angle theta=a t_E/c, obtaining
ds_E²=dr²+r²dtheta².
The mapping X=r cos theta,Y=r sin theta is ordinary flat Euclidean-plane polar coordinates. Smoothness **at the origin** when the origin is included requires theta to have period 2pi, hence the Euclidean Rindler time t_E has period beta_R=2pi c/a. This is the usual local geometric regularity/Unruh periodicity structure for the Minkowski vacuum. It fixes **angular period, not the radius R or acceleration a**. Rindler curvature away from a possible conical tip is zero, so no new gravity is being derived by drawing the Euclidean circle.

In the inertial chart (x,ct), the uniformly accelerated worldline from v15.1096 has near-seat parabola focus f=R/2 and Euclidean osculating circle radius R. The Euclidean Rindler orbit of the observer at r=R has the same **numerical** radius R and half-radius focus R/2. The two circles are in different constructions: the hyperbola's Euclidean osculating circle uses (x,ct) plotting metric, whereas the Rindler thermal circle uses imaginary time; this is NOT a literal common closed worldline or coordinate-free curvature invariant. Magnetic velocity-field circles remain spatial transverse loops, yet another geometrical plane.

## Gate 938 — spinorial 2pi sign and lack of acceleration selection
A spin-half representation has double-cover rotation holonomy: exp(i theta sigma_z/2), and changing theta by 2pi multiplies the spin representation by -1. On a Euclidean thermal circle, fermionic fields are antiperiodic in the appropriate thermal frame; this boundary condition is standard Dirac theory and is independent of circle radius R. A local rotating frame can produce an apparent -1 even in flat space; it does not automatically signify a physical magnetic flux or an independent charged-seat path.

The natural local angular frequency of the Rindler Euclidean circle is omega_R=a/c, whereas the idealized Dirac Zitterbewegung angular frequency of Sandbox v15.1091 is omega_ZB=2mc²/hbar=2omega_C. Define rho=R/lambda_Cbar, lambda_Cbar=hbar/(mc). Then
a=mc³/(rho hbar),
f=R/2=rho hbar/(2mc)=rho r_ZB,
omega_R=omega_C/rho,
omega_ZB/omega_R=2rho.
Neither theta-periodicity nor the spinor minus sign sets rho=1. At rho=1 these natural angular frequencies differ by a factor of two, so it is especially incorrect to identify Euclidean thermal angular frequency with Zitterbewegung angular frequency without specifying which spin-half factor or model is used.

## Gate 939 — Unruh comparison is dimensionless but carries the unfixed rho
For an observer uniformly accelerated through the Minkowski vacuum, the standard Unruh temperature is T_U=hbar a/(2pi c k_B). The ratio to the rest-energy temperature scale is
k_B T_U/(mc²)=hbar a/(2pi m c³)=1/(2pi rho).
A formal thermal Boltzmann ratio for an energy gap mc² is exp[-mc²/(k_B T_U)]=exp(-2pi rho). This gap ratio is not an automatic probability for a concrete detector; detector response depends on worldline, coupling, gap and switching. At rho=1 the temperature ratio is 1/(2pi), a conventional conditional number; Unruh thermality is already standard QFT in accelerating frames. Every rho>0 produces a regular Euclidean circle and compatible spinor antiperiodicity.

As the same acceleration a may describe arbitrarily many observers with different masses m, no universal relation a=mc³/hbar can arise from smoothness of the background Rindler plane alone. Fixing rho would require an independent physical source/detector condition that involves mass and acceleration on equal footing.

## Gate 940 — reproducibility, verdict, next selector
Exact SymPy script research-notes/k4_rindler_euclidean_spinor_circle_selector_v15_1097.py, commit 98d9f843f40baa30d726c6bcd9e22330ec19c2db. Locally executed: PASS for Euclidean metric via polar coordinate map, regular-circle angular period 2pi c/a, 2pi spinor -1, parabola focus/r_ZB=rho and omega_ZB/omega_R=2rho, Unruh/Compton ratio 1/(2pi rho), formal thermal e^-2pi rho and four inequivalent positive rho witnesses. The formulas were checked exactly; independent Audit pending.

**Positive:** The accelerated observer's Euclidean circle has the same length radius R=c²/a as the *coordinate-diagram* osculating circle, so parabola-focus=half-R aligns structurally with the spin-half circle, giving a clean geometric comparison and precise factor of two. **Negative:** The uniform-acceleration Rindler circle has no preferred radius: smoothness and spinor sign impose angular periodicity for every rho and do not pick the idealized Compton/ZB loop, charge, G or an extra K4 operator.

**NEXT:** formulate a mass-dependent, covariant, conserved Dirac/Maxwell detector spectral problem with physically specified states and boundaries. Only an actual eigenvalue/regularity/force relation involving m,a,field strength and physical coupling could select rho; compare any candidate to standard Unruh/Dirac acceleration physics and matched Einstein+elastic-solid theory. No use of Euclidean thermal circle as literal charged motion, no conflation of action integral pi*hbar with a thermodynamic period.

**Audit handoff:** distinguish Euclidean polar geometric smoothness from Minkowski dynamics; spinor antiperiodicity and moving-frame sign; show rho remains free; check factors 2,pi, c; note spin frequency and Euclidean Rindler frequency differ by 2rho; compare to v15.886 and v15.1096; preserve additive protocol.
