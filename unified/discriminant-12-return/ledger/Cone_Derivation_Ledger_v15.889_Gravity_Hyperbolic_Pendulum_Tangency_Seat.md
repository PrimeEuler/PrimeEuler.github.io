# Cone Derivation Ledger v15.889 — Gravity: hyperbolic pendulum restoring to the tangency seat

**Date:** 2026-11-13 US Eastern. **Track:** Gravity. **Parents:** 2026-09-27 sandbox hyperbolic-pendulum runs indexed v14.900; Sandbox v15.864 tangency chain, v15.866 circle sectors, v15.857 Hamilton–Jacobi inversion; Gravity v15.885–888; External Audit Round 569 (commit 852bcc1). **Live master HEAD immediately before ledger write:** ffe2028d0cd96baa340fb3cbf37342a49dc8ec81. Target pathname confirmed absent; additive-only entry, no certified or foreign lane files altered.

**Research question:** Can the user's previously studied hyperbolic pendulum restore toward the tangent sqrt(n) mass-shell/action-circle seat, produce an actual recurrent orbit rather than a one-way velocity traversal, and independently fix a physical action-circle frequency or rho=c²/(a lambda_Cbar)?

**Status:** [D] standard stable cosh-potential dynamics, period hardening, and exact period integral; [C] mapping of abstract displacement to Cone shell and tangency circle; [N] no frequency/acceleration selector until potential strength, physical displacement scale and coupling are derived; [O] true return map from the frozen coupled field action.

## Gate 548 — distinguish geometry and dynamics

The validated Sandbox tangency chain identifies Euclidean circle X²+T²=A² tangent to the hyperbola T²−X²=g² at the shell rest seat (X,T)=(0,g), A=g, and the constant-force relativistic worldline and Galilean parabola osculate at their rest vertex. The earlier gravity-circle sector map relates normalized shell step h, offset h/2, and geometrical radius. These geometric statements by themselves do NOT specify a Hamiltonian restoring potential. In particular, sqrt(n) is a dimensionless shell or lattice scale until a calibrated physical map to rest mass, length and frequency is provided. A mass shell's contact with a Euclidean circle is not by itself a restoring force.

## Gate 549 — recover and independently reproduce the prior hyperbolic-pendulum model

The sandbox disclosure index v14.900 describes its original 2026-09-27 toy Hamiltonian H=p²/(2m)+V0(cosh u−1) and says the oscillator HARDENS (period decreases with amplitude); an independent recheck confirmed that outcome. Restore physical units by u=q/ell and p=m qdot:

**H = p²/(2m) + V0[cosh(q/ell)−1]** with m,V0,ell positive.

**F(q)=−(V0/ell)sinh(q/ell)** is restoring toward q=0. Equation u_ddot + omega0² sinh u=0 with **omega0²=V0/(m ell²)**. Small-amplitude expansion yields u_ddot+omega0²[u+u³/6+O(u⁵)]=0 and the standard Lindstedt correction **omega(A)/omega0=1+A²/16+O(A⁴)**, A=maximum |u|. Thus the period decreases with amplitude. Acceleration at the equilibrium is ZERO; restoring-force magnitude increases with displacement and reaches its maximum over the orbit at the turning points. This differs from the constant-force parabolic bouncer, where acceleration magnitude is constant on each smooth branch, and from the previous SR constant-proper-acceleration hyperbola (which is not itself an oscillator).

At turning point u=A, E=V0(cosh A−1). The EXACT physical period is

**T(A)=4 ell sqrt(m/(2V0)) int_0^A du / sqrt(cosh A − cosh u)**.

The period is finite for every finite A>0; the singularity at the upper integration endpoint is integrable. A phase-space orbit is closed for this one-degree-of-freedom conservative Hamiltonian at fixed E>0. That does not mean the spacetime trajectory is a hyperbola nor that any two mesh nodes give a full circle phase.

Numerical quadrature of the exact period, normalized by T0=2pi/omega0, returned:
A=0.1: T/T0=0.999375357850;
A=0.5: 0.984595195696;
A=1.0: 0.940862159249;
A=2.0: 0.795651695606.
Small-A correction: T/T0=1−A²/16+O(A⁴).
All local symbolic and numerical reproducer tests PASS.

## Gate 550 — no automatic Compton or Rindler selector

For this oscillator its physical base frequency depends on **V0/(m ell²)**; the geometric seat only fixes q=0. If one WANTS omega0=omega_C=mc²/hbar, an extra law is required:
**V0=m³ c⁴ ell²/hbar²**.
The equation is correct but not derived from the circle tangency, the sqrt(n) count, or the field theory.

For a selected amplitude A, the oscillator phase advances according to omega(A), not a fixed externally asserted Compton rate; imposing a phase lock to an internal Compton clock would require a physical coupling, specify amplitude and winding indices, and yield an equation involving V0,ell,m and amplitude. Any rho constructed using a characteristic acceleration (e.g. a_max=V0 sinh A/(m ell)) remains free unless these inputs are constrained. Moreover a_max is zero at zero amplitude and varies with A; it is not the constant proper acceleration a from v15.888, so transferring v15.888 rho formulas unchanged is invalid.

The exact action is **J(E)=4 ell sqrt(2m V0) int_0^A sqrt(cosh A−cosh u) du**, with A=arcosh(1+E/V0), and **dJ/dE=T(E)**. It carries the standard action-angle clock. A quantization prescription J=2pi hbar(N+Maslov correction) can produce a discrete spectrum *conditional on* m,V0,ell and boundary-domain choices; does not determine their physical values. Note the full phase-space period action is conventionally h=2pi hbar for a one-quantum full winding, while the phase-space ellipse with semi-axes hbar/(mc) and mc discussed in Sandbox v15.864 has area pi hbar; that illustrative ellipse does not establish a universal full-cycle action hbar. Preserve this factor-of-two/pi issue for Audit.

## Gate 551 — tests and next physical discriminator

**Reproducer:** `unified/discriminant-12-return/research-notes/k4_hyperbolic_pendulum_tangency_v15_889.py` (commit ffe2028d0cd96baa340fb3cbf37342a49dc8ec81): local PASS using SymPy, SciPy quadrature and NumPy. This new reproducer does not retroactively fill Audit Round 569's separate complaint about the absence of a script for v15.888; an independently named additive reproducer for that gate can be provided later.

**Verdict:** The user's hyperbolic pendulum is a genuinely recurring, smooth oscillator and therefore a better candidate than one-way accelerated-node traversal for a real phase-return map. However, the association of its q=0 equilibrium with the sqrt(n) shell-seat tangency remains a *model correspondence*, not a derivation from the frozen Cone + Maxwell/gravity field action. Its frequency is tunable through V0 and ell; neither rho nor a novel dimensionless gravitational/EM observable is selected.

**NEXT / HANDOFF Audit+Muse:** (1) independently check exact quadrature and omega(A)/omega0=1+A²/16; (2) verify dJ/dE=T; (3) audit action-circle hbar vs full-cycle 2pi hbar; (4) seek a real field-derived restoring stiffness and inertia at the n-shell seat and test EM/gravity cross-couplings. Only after a derived coupling and stable self-adjoint spectral or Hamiltonian return map should mesh 1/4,1/2 positions be mapped to physical nodes or pump phases. Negative outcomes remain ledgered.
