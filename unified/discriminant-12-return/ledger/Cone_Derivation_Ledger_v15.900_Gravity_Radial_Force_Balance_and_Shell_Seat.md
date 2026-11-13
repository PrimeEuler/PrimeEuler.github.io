# Cone Derivation Ledger v15.900 — Two-circle turning-point force balance and radial return

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** Gravity v15.895–899 (the two circles, shell rapidity, outer acceleration parabola, conditional SR kinetic ratio, and angular-momentum spin-up); external Audit Round 570. **Live master HEAD checked immediately before ledger write:** 9ff418d088178f56665dd0d7357a1bbfc914d6d1. Target path checked absent. Additive-only. Previous certified, Audit, Sandbox and Suzuki material preserved.

**Question:** Can the two distinct geometric radii be the inner/outer turning radii of one angular-momentum-conserving rotor with an inward force, giving an acceleration law? What is fixed and what remains free?

**Status:** [D] exact conditional force matching for constant-inward-force model, two turning-point accelerations, bounded orbital return, generalized small-oscillation frequency-ratio family; [N] actual force potential/physical units/absolute clock not supplied by Cone tangencies; [O] derive physical radial potential from field stress and inertia.

## Gate 576 — fixed angular momentum plus two turning points constrains a constant inward force

Define r_i=ell_*u sqrt(n), r_o=ell_*u(n+1)/2 for ell_*,u>0 and n>1, with gamma=r_o/r_i=(n+1)/(2sqrt(n))>1. These are **candidate physical lever-arm lengths**; their calibration to the original geometric circles (and especially to previously suggested m/s radii) is *not* independently derived. Treat mass M and conserved angular momentum L>0 as specified. A simple radial Hamiltonian for a breathing thin hoop / point mass is

H_rad = (M/2) r_dot² + U_eff(r),
U_eff(r)=L²/(2Mr²)+F0 r,

where F0>0 is the magnitude of an assumed constant inward force; its acceleration parabola is local in time, not a global constant-acceleration orbit because the centrifugal term varies with radius. Radial equation:

**M r_ddot=L²/(Mr³)−F0**, and theta_dot=L/(Mr²).

Impose both radii as turning points of the **same orbit**: r_dot=0 at r_i and r_o, so U_eff(r_i)=U_eff(r_o). Solving the equality uniquely within this **assumed constant-force family** gives

**F0= [L²/(2M)] (r_o+r_i)/(r_i² r_o²) = [L²/(2M r_i³)] (gamma+1)/gamma².**

At n=1, the two radii merge; the two distinct-turning-point matching condition degenerates and does not determine F0 from two different endpoints. In the n→1+ limiting model, F0→L²/(Mr_i³), the circular equilibrium balance, but the exact coincident-radius condition by itself is weaker.

The raw angular-momentum conservation does NOT select F0. The formula depends on assuming the potential is F0 r, prescribing BOTH endpoints as turning radii and supplying M,L and the length calibration.

## Gate 577 — signed accelerations and the actual radial work

At inner and outer turning points:

**a_i=r_ddot(r_i)=[L²/(2 M² r_i³)] [(gamma−1)(2gamma+1)/gamma²] >0** (outward radial reversal),

**a_o=r_ddot(r_o)=−[L²/(2 M² r_i³)] [(gamma−1)(gamma+2)/gamma³] <0** (inward radial reversal).

Therefore near each turning event, r(t)=r_turn+(1/2)a_turn(t−t0)²+O((t−t0)^4). These local acceleration/deceleration parabolas exist as bona fide physical trajectories in this rotor control, but their coefficients depend on M,L,ell_* and F0. The outer *circle's geometrical osculating parabola* from v15.897 is distinct from this physical radial-time parabola and cannot be equated without a coordinate/time map.

The equilibrium radius lies strictly between both turning radii:

**r_eq=(L²/(M F0))^(1/3)=r_i [2gamma²/(gamma+1)]^(1/3)**.

This is a stable minimum of U_eff, because U_eff''(r_eq)=3L²/(M r_eq^4)>0. The inner turning point is NOT this stable equilibrium when gamma>1. This keeps mechanical rest, radial instantaneous rest, and the earlier geometrical shell-rest seat separate.

Energy transfer: inward contraction under −F0 does positive work F0(r_o−r_i), while the centrifugal barrier grows by the matching amount. Explicitly F0(r_o−r_i) = L²/(2M)(1/r_i²−1/r_o²)=Delta K_rot. Radial kinetic energy vanishes at both endpoints, and rises between them. No energy is created by angular momentum conservation.

## Gate 578 — numerical return and nonclosure of the spatial orbit

For a **dimensionless mathematical control** n=4, ell_*u=1, M=L=1, we get r_i=1, r_o=5/4, F0=0.72, a_i=+0.28, a_o=−0.208. Integrating the radial/angle ODE with zero initial r_dot at r_o returns to inner r=1.000000000000002 at t=2.269586379853574 (dimensionless time units); angle advanced by 1.811927366011686 radians over this half radial oscillation. Maximum total-energy drift 6.7e−16. The full radial oscillation thus sweeps approximately 3.623854732 radians in angle, rather than exactly 2pi: a *precessing bounded orbit*, not a closed planar circle. The exact two-circle turning-point correspondence does not imply spatial phase-locking.

Reproducer: `unified/discriminant-12-return/research-notes/k4_two_circle_radial_force_v15_900.py`, commit **9ff418d088178f56665dd0d7357a1bbfc914d6d1**. Fresh local SymPy/SciPy executable PASS: force matching, signs, energy equality, p-family frequency ratio, ODE return, energy conservation.

## Gate 579 — ratio of radial and angular clocks depends on chosen potential

For more general attractive radial potentials V(r)=C r^p/p with C>0, p real, and a nonzero stable circular radius r_*, equilibrium requires L²/M=C r_*^(p+2). The circular angular frequency squared is omega_theta²=L²/(M² r_*^4); the linearized radial frequency is

**omega_r²=(p+2) omega_theta²**, stable iff p>−2.

Concrete controls: p=1 constant inward force gives omega_r/omega_theta=sqrt(3); p=2 harmonic radial well gives 2; p=−1 Newton inverse-square (V=−C/r) gives 1. These are standard Newtonian central-force results, not newly selected numbers; changing the restoring-force law changes the measurable dimensionless frequency ratio while preserving the same two-circle geometry. This is a direct **counterfamily** to any claim that tangency and conserved L uniquely determine radial frequency.

## Gate 580 — subtle shell-coordinate mapping and selector verdict

On the original fixed-product shell with radius r_i, one can formally write r(s)=r_i cosh(s), s∈[0,(1/2)ln n], mapping the rest-shell seat to the inner radial turning point and the outer divisor-pair station to r_o. But **dr/ds=r_i sinh(s) vanishes at the inner seat s=0**. In the simple physical radial kinetic energy (M/2)r_dot², the induced s-coordinate metric M r_i² sinh²(s) is degenerate at s=0. The inverse s=arcosh(r/r_i) is not smooth across the radial bounce unless signed branches are specified. A separate nondegenerate s kinetic term would be an extra model input. Thus the hyperbolic coordinate map alone does not identify a smooth independent force-carrying degree of freedom at the seat.

**Verdict:** In an explicit mechanically consistent constant-inward-force rotor, the two Cone-circle radii **as stipulated turning radii** fix the required force strength in terms of L,M,length and produce genuine parabolic radial accelerations, kinetic-energy transfer, and oscillatory radial return. But the physical force is not derived from Cone/K4/Maxwell; angular momentum only fixes the centrifugal part. A physically distinct family of restoring potentials gives different radial/azimuthal frequency ratios. No unique force, fundamental clock, Newton G, or new experimentally distinct gravity observable has been shown.

**NEXT / HANDOFF Audit+Muse:** independently reproduce matching F0, inner/outer acceleration signs, orbit angle and energy drift, p-family ratios, and degeneracy of r(s) at s=0. Seek field-derived radial force and kinetic metric; compare gravitational and EM sectors with independently specified physical radii; test genuine conserved-source response before claiming intrinsic acceleration. Older v15.888/v15.890 missing-script gaps remain outstanding.
