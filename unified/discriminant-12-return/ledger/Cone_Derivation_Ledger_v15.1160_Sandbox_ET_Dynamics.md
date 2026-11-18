# Cone Derivation Ledger v15.1160 — Sandbox: source-consistent e(t) dynamics for the cone ellipse — closed equation, parametric drive, no intrinsic clock

**Deposit type:** Sandbox exploration, independently checkable.
Follow-on item of Jeremy's 2026-11-18 tasking: v15.1110's
open end (v15.1111 Gate 984 and NEXT — a self-consistent
conserved mechanical source/action for the ellipse shape
coordinate, whose absence left e(t) an imposed excursion).
Producer re-executed at staging, exit 0 (all checks PASS).
Filed inputs (Gravity, Audit R596): I_plus(e), U_B(e)
(v15.1110); M(e) shape inertia and the reduced energy
balance (v15.1112); Gate 981's actuator requirement (the
time-varying field's rho, J sources, power port -int J.E).

Actuator: the field's support is a physical deformable
source frame (its shape IS the ellipse) with Hookean
shape elasticity (1/2) k_e e^2, damping gamma, and a
maintaining circuit holding psi0. The collective equation
is then closed — e(t) is solved, not imposed:
M(e) eddot + (1/2) M'(e) edot^2 + gamma edot + U_B'(e)
+ k_e e = -(h(t)/2) I_plus'(e), with h the filed tidal
pulse and normalization K = M(0) = 1 (filed scale
K/M(0) = c^2/C^2 at c = C = 1). Energy accounting closes
along the solution: dE_mech/dt = -(h/2) I_plus'(e) edot
- gamma edot^2 (verified, residual 2.8e-3 relative from
numerical differentiation).

Three derived facts replace imposed ones. (1) The tidal
drive is PARAMETRIC: I_plus'(0) = 0 exactly, so the tidal
force vanishes at e = 0, the circular state is an
equilibrium under the pulse (zero seed stays zero,
< 1e-9), and the pulse modulates the stiffness
k_e - K h(t). (2) The phase lag is an OUTPUT: at
omega_0 = 2 pi, gamma = 0.05, seed 0.05, h0 = 0.3 (model
units), the first descending zero crossing moves from
0.25937 (undriven) to 0.26189 — derived lag +0.0025
pulse-width units, not an inserted Delta. (3) The pure
field has NO CLOCK: U_B - U_B(0) has no e^2 term (series-
verified; e^4 coefficient K/8 — a quartic rest state), and
with k_e = gamma = h = 0 the measured periods are 71.36
at amplitude 0.15 and 37.94 at 0.30, scaling as 1/A
(frequency proportional to amplitude) at 1.02x and 1.09x
the exact pure-quartic values. Gate 984's "no physical
frequency is determined" is now quantitative.

Verdict: source-consistent e(t) dynamics exists and is
closed, at the price of the constitutive inputs any
actuator carries (k_e, gamma, circuit law — imported).
The cone contributes the geometry of M(e), U_B(e),
I_plus(e); the system is a standard electromechanical
parametric (Mathieu-Duffing) oscillator. No cone-specific
frequency, no selector, and the imposed sech profile is
not recovered as a dynamical law. G_derived = false.
Lane A files untouched.

**Payload:** `payloads/et_dynamics_v15_1160/` — ET_Dynamics_Source_Consistent.md `67af1a83c13451e8dde0c38a2cf0f79ea5889e2c09ad89b1af81bf2ddf0e7a1a`, et_dynamics.py `5a53a5e1df7c4cb4d2ba1a2ad73c2b6005803ffcf30cbb2de9d5f1c3b91db08d`.
