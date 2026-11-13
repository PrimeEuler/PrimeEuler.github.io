# Cone Derivation Ledger v15.890 — Exact velocity-space circle for the hyperbolic restoring oscillator

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** v15.889 hyperbolic pendulum; v15.864 shell/action-circle tangency; v15.885 physical m/s axis. **Master HEAD verified before write:** 1acc1ba5fee4ab01eb94160c1cf9194bddd85678. Target path checked absent. Additive only.

**Question:** Can the proposed sqrt(n) action-circle radius be interpreted as m/s without conflating velocity and action dimensions?

**[D] Exact oscillator-to-velocity-circle map.** For the already studied one-dimensional hyperbolic-pendulum Hamiltonian H = (m/2) qdot² + V0[cosh(q/ell)-1], with m,V0,ell>0, introduce v=qdot and w(q)=2 sqrt(V0/m) sinh[q/(2ell)]. BOTH coordinates have units m/s. Then

v²+w² = (2/m)H = 2E/m,

so every bounded fixed-energy oscillator trajectory maps onto a Euclidean velocity-space circle of radius **R_v(E)=sqrt(2E/m)** in (v,w). The map is exact, not a small-amplitude approximation: cosh x−1=2sinh²(x/2). It is an energy-shell coordinate transformation, not an independent derivation of a new conserved action; w is a velocity-like potential coordinate, not a second ordinary Cartesian velocity component. Consequently the label 'action circle' must not be read as identifying this Euclidean velocity area with canonical action.

**[D] Phase speed is nonuniform.** Define theta=atan2(w,v), oriented so theta increases. With qdot=v, vdot=−(V0/(m ell))sinh(q/ell)=−w dw/dq and wdot=(dw/dq)v, one gets

theta_dot = (v wdot − w vdot)/(v²+w²) = dw/dq = omega0 cosh[q/(2ell)],

where omega0=sqrt(V0/(m ell²)). This is minimum omega0 at the seat q=0 and maximum omega0 cosh(A/2) at the displacement turning points q=±ell A. The circle closes with phase increment 2pi for each physical oscillator period automatically. This is NOT an independently imposed physical Compton-clock quantization: the period remains a function of m,V0,ell and amplitude.

**[C] sqrt(n) test.** A circle with proposed physical radius R_v(n)=v_* sqrt(n) requires **E_n=(m v_*²/2)n**. The arithmetic shell index n is dimensionless, and velocity normalization v_* is not selected by geometry alone. In particular, setting v_*=c would give R_v>c when n>1; because w is a potential coordinate, however, R_v is not itself the instantaneous laboratory speed v. An SR-compatible extension must still bound |v|<c and define a relativistic Hamiltonian. The mass-shell action-circle of v15.864 is a different geometric construction; no proven map yet equates its radius to R_v(E).

**[N] Selector.** A conserved velocity-circle radius does not supply traversal rate; omega0 contains independent potential stiffness and length. Likewise writing E_n proportional to n amounts to a new spectral hypothesis until a field Hamiltonian and boundary conditions derive it. This map is exact and useful but does not fix the v15.886 rho selector or a gravity coupling without new dynamics.

**Verification:** independent SymPy identities of cosh-to-sinh² and d(w)/dq both evaluate to zero residual. Further differentiation of the energy identity using qdot and qddot supplies dot(theta) algebra. Independent Audit pending.

**NEXT:** compare nonlinear theta(t) with the physical action angle phi=2pi t/T(E); derive the exact nonlinear phase reparameterization and interrogate whether the 1/4 and 1/2 mesh sites have any invariant location on the (v,w) circle. Build relativistic version and derive field stiffness instead of inserting an n-linear spectrum.

**HANDOFF Audit/Muse:** check both dimensions, meaning of w vs v, phase evolution, and absence of a unique velocity calibration/clock.
