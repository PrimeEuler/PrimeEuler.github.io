# Cone Derivation Ledger v15.1111 — Dynamical cone-ellipse Maxwell source, sech timing and tidal-work phase-lag selector

**Date:** 2026-11-17 Eastern. **Lane:** Gravity/Cone. **Classification:** [D] exact full Maxwell constraints and Poynting identity for arbitrarily time-varying compact vector potential tracing the projected Cone ellipse; [D] parity-induced zero first-order metric work for a synchronized even tidal pulse and even sech eccentricity excursion; [C] nonzero signed work and opposite signs for nonzero lead/lag in a fully specified prescribed-source example; [N] sech geometric law does not determine physical frequency, delay, driving stress, net power source or a parameter-free G-free observable; [O] a self-consistent conserved mechanical source/action and the K4 ADM-retarded tide. **Live HEAD pre-ledger write:** c70061c5a8d6405cfd60372cca3026a8a071ad2b. v15.1111 unique; additive-only, no prior certified, Suzuki, Sandbox, Muse or Audit edits.

## Earlier work, Audit and source scope
External Audit Round 595/v15.1109 commit cd4196eaf8b1a450f6fdc2386f49754842c4edc6 independently confirmed Gravity v15.1105–1108 including the v15.1107 constraint-corrected magnetic curl. Gravity v15.1110, not yet independently audited, gave an explicit finite-support, divergence-free Maxwell magnetic field whose streamfunction level contours are nested ellipses shaped by Paper A's projected Cone cut. Its integrated plus-TT stress and magnetic energy are
Iplus(e)= -K e²/sqrt(1-e²), K=4 pi psi0²/(7 mu0), and U_B= (K/2)(2-e²)/sqrt(1-e²). The physical translation of the rest-center drops out of the integrated stress; eccentricity determines its anisotropy. Crucially the scalar cutting-plane coordinate cos(phi)=tanh(u), sin(phi)=sech(u) from v15.1108 is an exact *geometric* parametrization, NOT a physical clock. This gate tests an **independently imposed sech-shaped eccentricity excursion** on the v15.1110 field against a finite tidal pulse, including the exact necessary electromagnetic charge/current sources.

## Gate 981 — time-dependent compact field is Maxwell-consistent but needs a real actuator
Let the compactly supported vector potential be A=(Psi(x,y,z,t),0,0), scalar potential Phi=0 (temporal gauge), where Psi=psi0 f(x) F(q_{e(t)}(y,z)), F(q)=(1-q)^4 for q<1 and zero elsewhere, q_e=((y-d(e))/A(e))²+(z/B(e))², d=-Ce/(1-e²), A=C/(1-e²), B=C/sqrt(1-e²). Use an externally assigned smooth e(t) with |e(t)|<1. In c=epsilon0=mu0=1 and a flat local electromagnetic patch, exact fields and source are
E=(-Psi_t,0,0), B=(0,Psi_z,-Psi_y),
rho=-Psi_xt,
J=(Psi_tt-Psi_yy-Psi_zz, Psi_xy, Psi_xz).
Then div B=0, curl E+partial_t B=0, div E=rho, curl B-partial_t E=J and partial_t rho+div J=0 **identically**. The pointwise Poynting identity
partial_t[(E²+B²)/2]+div(E cross B)=-J dot E
also holds exactly. With compact support the integrated Poynting flux at infinity vanishes, so field energy changes according to the electrical source work -int J dot E. Therefore arbitrary sech-shaped e(t) cannot be called a passive self-oscillating field: the required supporting charge/current and actuator supply/receive whatever energy the prescribed geometry demands. At nonzero e_dot, the electric field and its energy must not be neglected.

This flat-patch Poynting identity is distinct from the weak-curved-metric gravitational strain work; adding the GW requires a consistently covariant stress/energy budget and the mechanical supports. The metric-work cross term below is a **first-order external pump comparator** evaluated on the prescribed source history, not proof of exact global energy conservation for the combined GW+current+wall system.

## Gate 982 — time-reversal parity gives a strict zero for synchronized sech and tidal histories
Take a finite, even, externally imposed tidal strain pulse
h(t)=h0 (1-(t/T)²)^4 for |t|<T and 0 otherwise.
Let the cone-ellipse deformation be an even excursion, with prescribed shape
e(t)=e0+delta_e sech[(t-Delta)/sigma],
restricted to |e(t)|<1, with shape center delay Delta and width sigma independent of the arbitrary geometric rapidity parameter. The local weak-TT magnetic stress contribution in the quasi-static magnetic approximation is
W_g = -1/2 int h_dot(t) Iplus[e(t)] dt,
with Iplus=-K e²/sqrt(1-e²).
For Delta=0, h(t) and e(t) are even, Iplus[e(t)] is even, h_dot(t) is odd, hence
**W_g(Delta=0)=0 exactly at first order in the imposed tidal metric.**
A peak-aligned, symmetric response therefore does NOT automatically gain net energy even when the instantaneous Maxwell tension and h_dot each are nonzero. The rate and signed phase/time lag both matter. At Delta≠0 the field stress is not symmetric about the pulse center and work is generically nonzero. The identity
**W_g(-Delta)=-W_g(+Delta)**
holds for this time-symmetric h and the chosen shifted-even sech history (without choosing a dynamical equation). A genuine passive response could have a phase lag from damping, inertia or material/circuit dispersion, but no such lag is derived here.

## Gate 983 — reproducible signed dimensionless example
Choose normalized time T=1 and use K=1 only to display dimensionless W_g/K, with h0=1e-4, e0=.30, delta_e=.07, sigma=.55, and Delta in units of T. Exact adaptive quadrature with scipy yields:
Delta/T=0 -> W_g/K=0,
Delta/T=+0.15 -> W_g/K=-6.284263290862405e-7,
Delta/T=+0.35 -> W_g/K=-1.2702049626021465e-6,
Delta/T=-0.15 -> W_g/K=+6.284263290862405e-7,
Delta/T=-0.35 -> W_g/K=+1.2702049626021465e-6.
This example is **not** a physical prediction: the strain amplitude, ellipse eccentricity profile, excursion duration and shift were externally specified, and even the tidal work is the metric contribution only, without the source's J dot E work, electric-field stress corrections or the backreaction of h. Nonetheless it discriminates geometrically synchronized vs phase-lagged deformation and corrects any suggestion that tidal work must be maximal at an ellipse rest-state peak.

## Gate 984 — unchanged geometric obstruction and next dynamical gate
The shape parameter u of the exact Cone ellipse satisfies cos(phi)=tanh u and sin(phi)=sech u, so it encodes **locations along a conic**. The time e(t) above separately uses an illustrative sech envelope; their shared analytical function does not identify the two variables or determine sigma or Delta. The Kepler radial accelerations in v15.1108 relied on an *independently imposed* areal clock J. A physical time-evolution selector would require an action with e as a collective coordinate, its kinetic coefficient obtained from electric field energy and/or elastic matter inertia, a restoring potential, damping, and a sourced metric drive. Only then could a response phase be derived and compared to Einstein–Maxwell+the SAME K4 solid. If no new operator appears, the comparison remains a standard electromechanical parametric response. No measured G, new quarter-grid coupling, Compton frequency, e, J, sigma or Delta is derived from Cone alone.

## Reproducibility and audit
Canonical reproducer `research-notes/k4_dynamic_cone_ellipse_sech_tidal_timing_v15_1111.py`, additive commit c70061c5a8d6405cfd60372cca3026a8a071ad2b. Local independent SymPy differential-identity and numerical scipy quadrature harness was executed: PASS Maxwell source continuity/Poynting identities, even-shape parity, opposite-delay signs, nonzero delay witnesses. The committed script is the canonical full reproducer, for independent byte-for-byte re-execution by Audit. **AUDIT HANDOFF:** check all Maxwell source components and sign convention, full Poynting identity, use of quasi-static magnetic Iplus versus induced E when e_dot nonzero, no unjustified exact energy-conservation claim for externally prescribed metric, parity proof, sign of delayed work, and non-selection of physical time by real sech projective compactification. **NEXT:** derive a finite positive collective-coordinate mass/inertance M(e)=int(∂ePsi)^2 (electric-field contribution) and source/elastic restoring action, with a fully explicit physical temporal constitutive law, then compute forced phase lag and total energy accounting; compare it against the matched standard Einstein–Maxwell+K4 system.
