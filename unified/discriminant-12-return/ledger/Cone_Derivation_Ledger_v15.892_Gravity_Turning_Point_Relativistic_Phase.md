# Cone Derivation Ledger v15.892 — Gravity: parabolic turning-point contact and relativistic hyperbolic-pendulum phase control

**Date:** 2026-11-13 US Eastern. **Lane:** Gravity. **Parents:** v15.864 tangent shell/rest action circle; v15.889 cosh restoring pendulum; v15.890 exact nonrelativistic velocity circle; v15.891 elliptic action-angle marker phase. **Live HEAD immediately before ledger write:** b87a9bd66e80ec878f5e9bf86da6957ab434744e. Target checked absent. Additive only: previous certified/Suzuki/Audit/Sandbox files left intact.

**Question:** Do the acceleration/deceleration parabolas contact physically distinguished points of the hyperbolic restoring oscillator, and does a relativistic realization keep the same 1/4-to-1/2 phase markers or select a clock?

**Status:** [D] exact local turning-point parabola, relativistic canonical model, bounded physical velocity and phase integral; [N] 1/4-to-1/2 marker interval changes with relativistic energy parameter; no clock, G, or rho selector; [C] original Cone shell-seat/action circle matching remains an unproven physical embedding.

## Gate 555 — distinguish equilibrium seat from instantaneous rest

In the cosh well V(q)=V0[cosh(q/ell)−1], the equilibrium seat is q=0 where F=−V0 sinh(q/ell)/ell=0. For any positive-energy periodic orbit, speed is maximal (not zero) when crossing q=0. Actual instantaneous lab rest happens at q=±Q turning points where the restoring-force magnitude is maximal. A local acceleration/deceleration parabola is centered at each turning point, not at the equilibrium crossing. Thus conflating the earlier v15.864 geometric "rest seat" shell tangency with the physical turning-point event is invalid unless zero amplitude or a separate map between states is proved.

For a turning point Q>0 at t=t0,

q(t)=Q + [F(Q)/(2m)](t−t0)^2 + O((t−t0)^4),

since velocity and the third time derivative vanish at t0. In this sense the nonlinear hyperbolic restoring oscillator has locally parabolic trajectory arcs, without globally tracing a constant-force parabola.

## Gate 556 — relativistic control without superluminal physical speed

Use the *conditional* standard special-relativistic Hamiltonian

H_SR(q,p)=sqrt(m²c⁴+p²c²)+V0[cosh(q/ell)−1].

Let E=H_SR−mc² be conserved excitation energy, Q=ell A>0 the turning displacement, E=V0(cosh A−1), and K(q)=E−V(q) >=0 on the allowed orbit. The physical speed magnitude is

|v(q)|/c = sqrt(1−[1+K(q)/(mc²)]^(−2)) <1.

The equation of motion obeys dot p=F(q) and dot v=F(q)/(m gamma³), with gamma=1+K/(mc²). At the turning point v=0, gamma=1, so a_turn=F(Q)/m is the same local parabola coefficient as Newtonian theory.

The first relativistic correction at the turning point is in the quartic coefficient:

q''''(t0)=F'(Q)F(Q)/m²−3F(Q)^3/(m³c²).

For F(Q)=−V0 sinh(A)/ell and F'(Q)=−V0 cosh(A)/ell²,

q''''(t0)=V0² sinh(A)cosh(A)/(m²ell³)+3V0³ sinh³(A)/(m³ell³c²).

Positive quartic correction is exact, and vanishes toward the nonrelativistic quartic when c→infinity. This establishes shared second-order parabola tangency and a physically distinguishable next-order departure.

## Gate 557 — exact relativistic phase map and moving 1/4→1/2 marker gap

Reuse v15.890 coordinates w=2 sqrt(V0/m)sinh(q/2ell) and define a SECOND energy coordinate b=sqrt(2K/m), so b²+w²=2E/m. Importantly b is a *kinetic-energy-equivalent speed*, NOT the physical laboratory velocity v in SR; it can exceed c while actual |v| remains below c. Put b=R cos(theta), w=R sin(theta), R=2 sqrt(V0/m) sinh(A/2), and theta between 0 and pi/2 on the outgoing quarter orbit. Write k=sinh(A/2), epsilon=V0/(mc²)>0. Exact differentiation and SR velocity then give

dt/dtheta = (1/omega0) [1+2 epsilon k² cos²(theta)] / {sqrt[1+k² sin²(theta)] sqrt[1+epsilon k² cos²(theta)]},

where omega0=sqrt(V0/(m ell²)), and the formula extends continuously to the turning point theta=pi/2. Define G(theta;A,epsilon) as the dimensionless factor in square brackets/divided by denominators. The full period is

T_SR(A,epsilon)= (4/omega0) integral_0^(pi/2) G(theta;A,epsilon) dtheta.

The uniformly advancing action-angle variable is phi(theta)=(pi/2) [integral_0^theta G dt]/[integral_0^(pi/2) G dt], with global unwrapping by quadrant. For epsilon→0 this reduces to the exact Newtonian elliptic map of v15.891.

Conditionally place the 1/4 and 1/2 markers at w/R=1/4 and 1/2 on the positive-b branch, i.e. theta1=asin(1/4), theta2=asin(1/2). The resulting physical phase gap is

Delta phi_SR = (pi/2) [integral_theta1^theta2 G(theta) dtheta]/[integral_0^(pi/2) G(theta)dtheta].

Local numerics using independent quadrature and Newtonian elliptic K/F control:

| amplitude A | Newtonian epsilon=0 | relativistic epsilon=0.01 | epsilon=0.1 | epsilon=1 |
|---:|---:|---:|---:|---:|
| 0.1 | 0.271037817 | 0.271041400 | 0.271073640 | 0.271395106 |
| 0.5 | 0.273871867 | 0.273963195 | 0.274779027 | 0.282374050 |
| 1 | 0.282366535 | 0.282753787 | 0.286129794 | 0.311720472 |
| 2 | 0.310790019 | 0.312691410 | 0.327287167 | 0.381727996 |
| 4 | 0.348274318 | 0.360305726 | 0.398997887 | 0.422694276 |

Thus relative phase is NOT invariant under relativistic corrections. At A=2, epsilon=1, phase gap is 0.381728 radians rather than 0.310790. Neither the node fractions nor the tangency alone select epsilon, A or omega0. These marker positions are on the encoded energy circle, not established literal v/c velocity nodes or physical Cone EM/G mesh points.

## Gate 558 — selector status and audit handoff

One can vary ell while holding dimensionless (A,epsilon) fixed; this scales omega0 and the whole period inversely, leaving all normalized phase gaps identical. Even at fixed R (requiring E/m held constant), ell remains free. Therefore the relativistic bound |v|<c eliminates superluminal kinematics without determining a frequency, rho, Newton's G, or a new dimensionless measurable gravity/EM observable. The SR Hamiltonian is an illustrative *control*, not a derivation from the frozen K4+Maxwell gravity action.

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_relativistic_hyperbolic_phase_v15_892.py`, commit b87a9bd66e80ec878f5e9bf86da6957ab434744e. Local executed Python+SymPy+SciPy+NumPy: PASS for half-angle hyperbolic identity, positive-quarter-arc derivative identity, turning-point quartic derivative, Newtonian elliptic limit at five amplitudes, finite phase gap and SR dependence. **Independent Audit pending**.

**Next:** derive (or fail to derive) the restoring force, inertia, and physical frequency from the actual frozen field action at the geometric sqrt(n) seat; compute the Hessian/kinetic metric, generalized eigenfrequencies and EM/gravity cross-sector coupling. Without this, the coherent parabola/hyperbola/circle contact remains a correspondence, not a new gravitational clock.

**HANDOFF External Audit/Muse:** check the physical distinction between equilibrium crossing and mechanical turning-point rest, q'''' SR sign/factor 3, beta(K), quadrature cancellation at pi/2, and separate status of energy-circle b vs physical velocity. Preserve all negative selector findings; note outstanding v15.888 reproducer omission from Audit Round 569.
