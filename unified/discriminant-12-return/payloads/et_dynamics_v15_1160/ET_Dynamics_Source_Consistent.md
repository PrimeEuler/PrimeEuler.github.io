# Source-consistent e(t) dynamics for the cone ellipse — the actuator, the closed equation, and what the dynamics does not give

Sandbox note (little Euler), 2026-11-18; follow-on item
of Jeremy's 2026-11-18 tasking (v15.1110's open end,
v15.1111 Gate 984 and its NEXT gate). Producer:
`et_dynamics.py` (sympy + scipy; all checks PASS).
Filed inputs (Gravity, Audit R596-verified): I_plus(e)
and U_B(e) (v15.1110), the shape inertia M(e) from the
electric-field energy and the reduced energy balance
(v15.1112), and Gate 981's finding that a prescribed
e(t) needs explicit charge/current sources — an
actuator — whose power port is −∫J·E dV.

## The actuator and the closed equation

The field's support is a physical object: a deformable
source frame (the winding/support whose shape *is* the
ellipse), held at amplitude ψ₀ by a maintaining
circuit. Give the frame its ordinary constitutive
physics — Hookean shape elasticity (1/2)k_e·e² and
damping γ — and the collective coordinate obeys a
closed equation in which e(t) is solved, not imposed:

    M(e)ë + (1/2)M′(e)ė² + γė + U_B′(e) + k_e·e
        = −(h(t)/2)·I_plus′(e)                     (★)

with h(t) v15.1111's filed tidal pulse and M(e),
U_B, I_plus the cone-ellipse field's own functions
(normalization c = C = 1, so K = M(0) = 1 by
v15.1112's filed scale K/M(0) = c²/C²). Energy
accounting closes along the numerical solution:
dE_mech/dt = −(h/2)I_plus′(e)ė − γė² identically
(verified to 2.8×10⁻³ relative, the residual being
numerical differentiation) — the source-consistency
the imposed-excursion treatment lacked.

## Three derived facts that replace imposed ones

1. **The tidal drive is parametric, not additive.**
   I_plus′(0) = 0 exactly, so the tidal force in (★)
   vanishes at e = 0: the circular state is an
   equilibrium under the pulse (verified: a zero seed
   stays zero to <10⁻⁹), and the pulse acts by
   modulating the effective stiffness k_e − K·h(t).
   v15.1111's imposed sech excursion, with its
   externally chosen Δ, could not show this.
2. **The phase lag is now an output.** With
   ω₀ = √(k_e/M(0)) = 2π, γ = 0.05, seed e(0) = 0.05
   and h₀ = 0.3 (model units, chosen so the effect is
   resolvable), the first descending zero crossing
   moves from t = 0.25937 (undriven) to t = 0.26189 —
   a derived lag of **+0.0025** pulse-width units,
   produced by the equation rather than inserted as a
   parameter.
3. **The pure field has no clock.** U_B − U_B(0) has
   *no* e² term at all (series-verified; the e⁴
   coefficient is K/8): the field's own rest state is
   quartic. With k_e = γ = h = 0 the measured periods
   are T = 71.36 at amplitude 0.15 and T = 37.94 at
   0.30 — scaling as 1/A (frequency ∝ amplitude), at
   1.02× and 1.09× the exact pure-quartic values
   (excess from M(e)'s growth and the filed
   (1−e²)^{−3/2} stiffening). Gate 984's "the sech law
   does not determine a physical frequency" is now
   quantitative: without the frame there is no
   frequency to determine, at any amplitude-independent
   value.

## Verdict

Source-consistent e(t) dynamics **exists and is
closed**: the actuator is the deformable source frame
plus its maintaining circuit; (★) is its law; the
lag, the work and the energy budget are derived
quantities. The price is exactly the constitutive
inputs any actuator carries — k_e, γ, the circuit
law — which are the frame's physics, imported. What
the cone contributes is the geometry of M(e), U_B(e),
I_plus(e) (Gravity's filed functions). The resulting
system is a standard electromechanical parametric
(Mathieu–Duffing) oscillator: no cone-specific
frequency, no selector, and the imposed sech profile
is not recovered as a dynamical law — it was one
prescribed history among many, and the dynamics
replaces it.

Flags: e_dynamics = CLOSED (source-consistent);
drive = PARAMETRIC; intrinsic_frequency = NONE
(quartic rest state, ω ∝ A); derived_lag = +0.0025
(stated parameters); constitutive_inputs = k_e, γ,
circuit law (imported); selector = NONE; G = false.
