# Cone Derivation Ledger v15.897 — Preserve the outer action circle's own acceleration/rate parabola

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** v13.177, v15.869 transition/rate parabola, v15.872 half/quarter wave-rate gate, v15.895 two circles, v15.896 shared shell map. **Live HEAD checked before write:** 84130f6f2e3000d6493b53c003d62bcdf2e8d9c8. Target checked absent. Additive only; no older objects modified.

**User correction:** The outer n+1 circle has its own acceleration/deceleration parabola; it cannot be treated merely as an intersection target for the unit factor-grid parabola. Distinguish geometric osculation from a time-parametrized physical acceleration.

## Gate 566 — outer circle's intrinsic osculating parabola

At factor unit u>0, define R_o=u(n+1)/2, R_i=u sqrt(n), and C_o: X²+Y²=R_o². Near its upper crown X=0,

Y_o(X)=sqrt(R_o²−X²)=R_o−X²/(2R_o)−X⁴/(8R_o³)+O(X⁶)
=u(n+1)/2−X²/[u(n+1)]−X⁴/[u³(n+1)³]+O(X⁶).

Thus its local osculating parabola is **Y=R_o−X²/[u(n+1)]**, with signed crown curvature −1/R_o=−2/[u(n+1)] in Euclidean coordinate units. This is intrinsic to the OUTER circle, and entirely distinct from the factor-row parabola **Y²=u²+2uX** whose vertex is at X=−u/2 and whose upper branch crosses C_o at (u(n−1)/2,u sqrt(n)). They are not interchangeable.

At the outer-circle chord intersection, the circle's curvature magnitude is 1/R_o=2/[u(n+1)], while the factor-row parabola's Euclidean curvature magnitude there is 1/[u(n+1)^(3/2)]. Their ratio is 2sqrt(n+1), and their tangent directions are unequal (a transverse crossing, as in v15.895). A circle's local osculating parabola at that intersection must be expressed in coordinates aligned with its own tangent/normal, not identified with the global factor-row curve.

## Gate 567 — its acceleration parabola requires a physical clock

Suppose the outer circle is embedded in velocity space with calibrated physical radius V_o=v_* R_o and components V_x=V_o cos(theta(t)), V_y=V_o sin(theta(t)). Then its time acceleration vector is

a=V_o theta_dot (−sin(theta),cos(theta)),

and its second time derivative includes both theta_ddot and theta_dot² terms. At a fixed nondegenerate turning/rate-crown angle theta=0, locally V_x(t)=V_o−[V_o/2] theta_dot(t0)²(t−t0)² + O((t−t0)³) if theta(t0)=0; in general a cubic term appears when theta_ddot(t0) is nonzero. For constant theta_dot=Omega the expression is V_x(t)=V_o−(V_o Omega²/2)(t−t0)²+O((t−t0)^4) and a physical acceleration magnitude V_o |Omega|. The existing circle curvature fixes the geometrical coefficient relative to X-coordinate but does NOT fix Omega, nor make theta the oscillator's canonical action angle.

For the inner rest circle with physical velocity radius V_i=v_*u sqrt(n), a separate angular law must be supplied. If a common angular speed Omega is *assumed*, the speed/acceleration radius ratio is the known R_o/R_i=(n+1)/(2sqrt(n)); it is not forced that the two circles rotate with the same physical angular speed.

## Gate 568 — explicit inventory and status

Keep all of these distinct:
(1) the inner sqrt(n) rest-shell tangency circle in its auxiliary (X,T) section;
(2) the outer n+1 diameter/secant circle in (X,Y);
(3) the outer circle's OWN osculating velocity-rate parabola;
(4) the half-offset factor-grid parabola intersecting the outer chord endpoint;
(5) the optional small radius-u/2 circle tangent to that grid parabola at its vertex.

The outer-rate parabola is a valid curvature construction, but its identification with the original physical constant-acceleration parabola remains conditional because coordinate orientation, physical m/s normalization and time evolution must be justified. The geometry alone still selects no physical acceleration, Rindler/Compton rho, stiffness, gravitational G, or oscillator frequency.

**Verification:** fresh local SymPy series to fourth order, plus independent curvature derivative for the row parabola, PASS. Independent Audit pending.

**NEXT:** build a coupled two-circle phase model with independent angles theta_o and theta_i, and test whether any preserved Cone constraints enforce a phase relation, rather than imposing synchronized angular rates. Derive any time law from physical K4+Maxwell field equations before declaring a clock or an EM/G pump. **Audit/Muse:** check the two different parabolic constructions and u dependence.
