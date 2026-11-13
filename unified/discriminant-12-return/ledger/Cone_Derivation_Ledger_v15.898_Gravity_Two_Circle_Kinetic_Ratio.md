# Cone Derivation Ledger v15.898 — Two-circle ratio as conditional relativistic kinetic-energy excess

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** v14.367 diameter–secant, v15.605 scale distinction, v15.895–897 rest/outer circles, shell rapidity and outer-circle acceleration parabola. **Live master HEAD checked before write:** e7ee127eb72109da7611341de15084b2a5622e7f. Target path checked absent. Strict additive-only, with no change to Audit, Suzuki, Sandbox or historical entries.

**Question from project owner:** Could the sqrt(n) rest-mass/action circle compared with the n+1 action circle and its acceleration parabola represent an increase in kinetic energy?

**Status:** [D] exact Lorentz hyperbolic identity and kinetic/rest-energy ratio under a stated calibration; [C] energy-momentum assignment to Cone geometry; [N] physical dynamics, acceleration/time scale, mass and coupling not selected; [O] force-work law and field-derived energy map.

## Gate 569 — complete energy-momentum triangle

For n>0 and factor unit u>0, keep the *distinct* circle radii and chord offset:
R_rest=u sqrt(n),
R_outer=u(n+1)/2,
X=u(n−1)/2,
so R_outer²=R_rest²+X² exactly. On the fixed-product shell the rapidity coordinate s=ln(n)/2 gives

R_outer/R_rest=cosh(s)=(n+1)/(2sqrt(n)),
X/R_rest=sinh(s)=(n−1)/(2sqrt(n)),
X/R_outer=tanh(s)=(n−1)/(n+1).

These are exact dimensionless hyperbolic identities. At n=1, s=0, R_outer=R_rest, X=0. For n<1, rapidity and signed momentum reverse; total kinetic energy remains nonnegative.

The *conditional physical calibration* E=mc²(R_outer/R_rest), p=mc(X/R_rest), and beta=v/c=X/R_outer gives E²−p²c²=m²c⁴. This is the standard SR energy-momentum map for any positive supplied rest mass m. It is not a proof that a geometrical action circle is a physical energy circle, nor does it produce m, G, hbar, time or force.

## Gate 570 — exact kinetic-energy excess between circles

Under that conditional energy calibration, let E_rest=mc² and K=E−E_rest. Then

**K/E_rest=R_outer/R_rest−1=(n+1)/(2sqrt(n))−1=(sqrt(n)−1)²/(2sqrt(n))=cosh(s)−1=2sinh²(s/2)**.

The positive radius gap is thus the exact kinetic-energy *excess* normalized by the rest circle, not a separate energy conservation theorem. At n=2,4,9,16, K/E_rest=0.0606601718,0.25,2/3,1.125. The ratio is independent of common geometric sector scale u at matched normalized n.

**Important competing interpretation:** if the two radii are instead declared independent Newtonian particle speeds with the same physical mass, their kinetic-energy ratio is (R_outer/R_rest)²=gamma², NOT gamma. Also, treating the radius difference as a velocity increase does not produce the SR kinetic energy without converting velocities to gamma. Since the project owner has proposed m/s circle radii, this dimensional fork must be retained, not silently collapsed. In the Lorentz map, X/R_outer=beta is the physical *normalized* speed; R_outer and R_rest are energy-scale coordinates, not both literal particle speeds. A velocity scale may be attached separately but does not establish the energy interpretation.

The earlier v15.890 toy oscillator energy circle is still another object and is not automatically identical to either original geometric circle.

## Gate 571 — does the outer acceleration parabola imply work?

Under a dynamically evolving shell variable s(t), E(t)=mc² cosh[s(t)] and p(t)=mc sinh[s(t)]. Exact time differentiation yields

dE/dt=mc² sinh(s) s_dot,
dp/dt=mc cosh(s) s_dot,
v=c tanh(s),

and therefore **dK/dt=v dp/dt=F v** if F=dp/dt, the standard SR power equation. This identity is compatible with any differentiable s(t), so does not select s_dot, acceleration a=dv/dt=c sech²(s)s_dot, or force F. The outer circle's independent geometric osculating parabola from v15.897 is still present; to call it an acceleration-time curve requires a physical embedding and angular/time parameter.

The exact kinetic-energy excess and the outer-circle curvature are therefore mutually consistent but insufficient to fix a restoring force, period, Compton/Rindler ratio rho, or novel EM/G coupling. A physical interaction may add a law for s(t) and thereby distinguish the two-circle energy interpretation experimentally.

## Gate 572 — verification and next discriminator

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_two_circle_relativistic_energy_ratio_v15_898.py`, committed at e7ee127eb72109da7611341de15084b2a5622e7f. Fresh local SymPy checks PASS for the hyperbolic triangle, gamma(beta) identity, energy-momentum invariant, positive kinetic/rest-energy excess and radius-squared alternative. Independent Audit pending.

**Next:** test a covariant or canonical action on s derived from the frozen Cone/K4/Maxwell model. Extract physical E,p and an actual force-work law without assuming that R_outer is E/mc²; compare free versus restoring s dynamics and two independently phased circle modes. Keep inner rest circle, outer total-energy circle, outer acceleration/rate parabola and half-offset factor parabola distinct. If no field term fixes s_dot or stiffness, retain the exact but standard-SR correspondence as a negative selector outcome.

**HANDOFF Audit/Muse:** verify alternative speed-squared versus energy-linear readings, n<1 orientation, physical dimensions, and that dK/dt=Fv holds identically for arbitrary s(t) but determines no force law.
