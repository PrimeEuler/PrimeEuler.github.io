# Cone Derivation Ledger v15.1102 — Finite acceleration pulse: EM dipole wavefront, gravitational quadrupole tidal waveform, and the necessary mechanical stress

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact analytic finite-pulse electric dipole and conventional weak-field GR quadrupole waveform in a leading slow-motion, long-wavelength, far-field approximation; [D] Newtonian stress-balance identity including an internal actuator; [N] no distinct Cone gravity contribution or time-independent single acceleration/secant shell for the entire pulse; [O] covariantly conserved complete Einstein–Maxwell–actuator source and frozen K4 elastic-solid retarded scalar/vector/tensor solution. **Live HEAD immediately before write:** 2eaa57106d5c8b799568034958080e947f1ba42b. Additive only and no protected Suzuki, Audit, Sandbox, Muse or prior certificate edits. v15.1102 collision checked against latest live commits.

## Prior ledger, audit and objective
External Audit Round 593/v15.1099 (commit 232b5900a66075575db14d93f37bee4e48813838) verified Gravity v15.1093–1098, including the prior disclosed original/corrected v15.1093 structural assertion. Gravity v15.1100 established that constant proper acceleration may be parameterized exactly by the confocal parabola/secant label k=R exp(u) and that its normalized circle has sech rapidity. Gravity v15.1101 connected individual accelerated-charge emission events to retarded spherical null fronts and their transverse circles; an individual outgoing Maxwell ray has null stress with zero TT projection along its own direction, but **this does not veto a global gravitational wave sourced by a complete extended conserved system**. User proposed 'potentially the tidal wave front'; this gate supplies an actual finite-time accelerated **two-body** source history and leading conventional gravitational tidal waveform instead of mistaking an EM field-line circle for a graviton. It is not yet a fully coupled or fully K4-constrained source.

## Gate 953 — bounded pulse, momentum conserving dipole mechanics
Take two equal point masses m at positions x1(t)=+x(t), x2(t)=-x(t) along x, with electrical charges +q and -q respectively. Prescribe for |s|<1 the dimensionless compact pulse g(s)=(1-s²)^4, s=t/T, and g(s)=0 outside. Let
x(t)=x0+epsilon g(t/T), x0>=0, epsilon small (|dot x|<<c, source extent << c T). g and its first three derivatives join continuously at endpoints. Both masses are at rest before and after, and the net total 3-momentum is identically zero. An internal actuator supplies F+=m xddot to the positive-x mass and F-=-m xddot to the other. **One cannot neglect that actuator as part of local momentum stress**.

In this Newtonian point-mass-plus-ideal-strut approximation, the integrated xx kinetic stress from masses is 2m xdot²; an ideal internal longitudinal strut with required force carries integrated xx stress 2x*m*xddot, with sign convention fixed by local momentum flux. With Ixx=2m x², exactly
integral Txx^(matter+strut) d³x = 2m(xdot²+x*xddot)=1/2 d²Ixx/dt².
This is the standard stress-to-quadrupole identity after including the *driver's* momentum support. An isolated pair of accelerated point masses without interaction stress is not a conserved source. This toy identity does **not** include electric Coulomb interactions, Maxwell field energy, radiation reaction, strut energy density and the complete relativistic four-divergence Tmunu=0. Thus it must not be presented as a fully covariantly conserved Einstein–Maxwell source.

For -1<s<1 the acceleration is
xddot=(epsilon/T²) g''(s),
g''(s)=8(1-s²)²(7s²-1).
The acceleration reverses sign at s=+-1/sqrt(7), and vanishes outside the pulse. Therefore the finite pulse is **not** one uniformly accelerated hyperbola on a fixed R=c²/a shell. A local instantaneous/osculating secant parameter can be defined while acceleration is nonzero, but R(t) diverges at the zero crossings and is not a global physical fixed-length selector. The exact uniform-acceleration/secant identities of v15.1100 remain correct for their own restricted class of trajectories.

## Gate 954 — EM dipole radiation, gravitational TT strain and tidal acceleration
In the same leading slow-motion dipole limit, the electric moment is p_x=2q x, so pdd_x=2q xddot. For an observation direction n=zhat perpendicular to the motion, the standard far-zone electric radiation amplitude along x is
E_rad,x= [pdd_x(t_r)]/[4pi epsilon_0 c² D]=q xddot(t_r)/(2pi epsilon_0 c² D).
The corresponding B radiation direction is n cross E_rad/c (azimuthal about the acceleration axis in the spherical emission geometry). Here t_r≈t-D/c and D≫x0+epsilon, D≫cT only insofar as the far-zone approximation is used; do NOT require D≫cT for wave propagation itself, but require D≫source size and retarded 1/D terms dominate. The leading standard radiated electric-dipole energy, ignoring radiation feedback, is
U_EM= integral pdd²/(6pi epsilon_0 c³) dt
= [131072/(5005 pi)]*q² epsilon²/(epsilon_0 c³ T³),
using exact integral ∫_-1^1 [g''(s)]² ds = 196608/5005. This is an imported conventional Maxwell result, not extra Cone energy; a physical actuator has to pay this energy through its power budget.

The mass quadrupole difference for the same source is Qxx-Qyy=2m x² (where Qij is the standard trace-free mass quadrupole, as the trace cancels in the difference), so
ddot(Qxx-Qyy)=4m(xdot²+x xddot).
For a distant observer along z, the standard weak-field Einstein far-zone plus strain is
h_+(t)=G/(c⁴ D)*ddot(Qxx-Qyy)
= [4Gm/(c⁴ D)] [xdot²+x xddot]_(t_r),
with h_xx^TT=h_+, h_yy^TT=-h_+. This is the ordinary leading Newtonian mass-quadrupole approximation of GR. In the local inertial, far-field TT interpretation the corresponding detector-relative tidal acceleration is
ddot xi_x/xi_x = (1/2)ddot h_+(t).
The physical tidal Weyl is proportional to -ddot h_+/(2c²) if the time coordinate in R_{0x0x} is ct. A finite source emits a gravitational pulse whose wavefront propagates at c in this approximation. The full Einstein–K4 **coasting elastic solid**, with background SVT modes, constraints and nonzero mass-sector response, has NOT been solved here and no claim of a K4-specific tidal signal is made.

The exact pulse-center values for s=0, g(0)=1,g'(0)=0,g''(0)=-8, are
E_rad,x(0)=-4q epsilon/(pi epsilon_0 c² D T²),
h_+(0)=-32Gm epsilon(x0+epsilon)/(c⁴ D T²),
(ddot xi_x/xi_x)(0)=96Gm epsilon(3x0+7epsilon)/(c⁴ D T⁴).
All three are analytic standard comparator quantities with G imported, rather than a G-free Cone prediction.

## Gate 955 — a clean parity/discriminant check
Under epsilon -> -epsilon at fixed nonzero x0, the electric dipole waveform changes sign identically, while the gravitational quadrupole waveform contains both a linear term x0*epsilon and a quadratic epsilon² term. For the **formal x0=0 limiting symmetric configuration**, the quadrupole waveform is entirely even in epsilon but the electric dipole is odd. This is a useful channel/representation check; the x0=0 limit would place point charges at coincident positions outside the pulse and is not a physically regular complete charged apparatus. It should not be promoted to a real laboratory prediction without finite-size, repulsion/attraction, and actuator dynamics. Neither symmetry derives a new tensor coupling or discretized wavelength from the Cone.

## Gate 956 — reproducibility and action selection status
Exact SymPy reproducer `research-notes/k4_finite_acceleration_pulse_em_gw_tidal_v15_1102.py`, additive commit **2eaa57106d5c8b799568034958080e947f1ba42b**. Complete script was locally executed before GitHub upload, exit 0, verifying pulse C³ matching, all kinetic-plus-strut/quadrupole stress identities, exact EM and GW far-zone expressions, finite radiated EM energy, peak tidal waveform, and epsilon parity in the x0->0 idealized limit. Independent external Audit pending.

**Positive:** an explicit finite accelerated source produces EM and gravitational null wavefronts and a nonzero tidal strain in standard weak-field theory, despite the vanishing collinear local TT stress of an individual EM radiation ray established in v15.1101. **Negative:** the waveform is conventional GR quadrupole plus Maxwell dipole radiation, no action-circle-selected Compton scale or quarter-mesh/G selector; no fully conserved total relativistic stress or K4-resolved Weyl from this toy model. **NEXT:** upgrade this bounded history to a genuinely conservative extended Einstein–Maxwell–matter driver with field stresses and finite-size sources; compute its retarded TT/SVT source and compare matched gravity actions. In parallel, examine whether the mesh/confocal secant supplies a *nontrivial invariant* of pulse wavefront sections beyond the algebraic null shell; do not paste a constant-a shell onto a sign-changing acceleration history.

**AUDIT HANDOFF:** verify exact coefficient in U_EM, quadrupole h_+ normalization, stress-from-internal-strut sign and integrated identity, smoothness at pulse endpoints and acceleration reversals, G import, and all limits of the leading nonrelativistic far-zone approximations. In particular distinguish a Newtonian integrated momentum-stress identity from covariant four-dimensional total stress-energy conservation, and ensure no claim that this gate solves frozen K4 ADM.
