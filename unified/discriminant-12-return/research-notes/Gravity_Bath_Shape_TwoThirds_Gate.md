# Gravity lane: 2/3 recurrence and the bath-to-phase eccentricity map

*2026-10-22. Parents: v14.696–704, v14.705–707. Producer: gravity_bath_shape_gate.py. [D] exact algebra; [N] reproducible evaluation; [I] interpretation; [P] physical prediction.*

## 1. The same letter does not mean the same coordinate [D]

The Maxwellian EFT bath v3.4 (deposited and summarized at v14.705/v14.707) uses the axis-ratio coordinate
\[
q=\sqrt{1-e^2}=b/a.
\]
The v14.698 phase-integral deformation instead uses
\[
\rho=\sqrt{\frac{1-e}{1+e}}=\frac{q}{1+e}.
\]
Both encode the *same geometric eccentricity* \(e\) when a shared physical ellipse is justified, but **q is not rho**. In particular, their numerical values are different away from a circle.

At the bath's hot-limit stable fixed point
\[
q_*^2=\frac13,\quad e_*^2=\frac23,\quad
\rho_*^2=\frac{1-\sqrt{2/3}}{1+\sqrt{2/3}}=5-2\sqrt6.
\]
Using the exact v14.701 angular Gram witness gives
\[
\boxed{\langle I_{00},I_{20}\rangle_*=\frac23(1-\rho_*^2)
=\frac{4\sqrt6-8}{3}\approx0.5993196570442375.}
\]
Incorrectly identifying q with rho would instead give 4/9. That is a coordinate error, not a novel physical coincidence.

This result is a **conditional algebraic consequence** of inserting the bath-selected classical eccentricity into the previously defined profile. It is not a quantum-transition prediction. By v14.703/v14.704, the raw rho!=1 profiles lack a positive-weight orthogonal sphere metric and a construction-native self-adjoint selector.

## 2. Two independent sources of 2/3 [D]

The phase-family factor 2/3 comes from the ordinary spherical moment
\[
\frac12\int_{-1}^{1}(1-x^2)\,dx=\frac23,
\]
which enters the overlap of an l=0 state and the distorted quadratic l=2 profile.

The bath's \(e_*^2=2/3\) follows instead from the particular hot-bath drift
\[
\dot q=-C\,\frac{3q^2-1}{q}, \qquad C>0.
\]
The stable point is q²=1/3; e²=1-q²=2/3. These values are fixed within the chosen bath equation, not by the spherical angular integral.

Their equality alone therefore does not establish one universal Cone or gravity constant.

## 3. Robustness gate: the selection is bath-model dependent [D]

For the more general stabilizing drift
\[
\dot q=-C\frac{a q^2-b}{q},\qquad a,b,C>0,\quad 0<b/a<1,
\]
the unique attracting interior equilibrium is
\[
q_*^2=b/a,\qquad e_*^2=1-b/a.
\]
Examples:
- (a,b)=(3,1): e²=2/3;
- (4,1): e²=3/4;
- (3,6/5): e²=3/5.

The 2/3 fixed point is **not structurally universal across this admissible drift family**. A claim that Maxwellian physics uniquely enforces a=3,b=1 must be derived from the specific collision operator and tested against other bath regimes; modifying coefficients without deriving a new bath does not refute the original Maxwellian result, but it refutes universality from Cone geometry alone.

## 4. Gravity observable Xi remains standard [D/P]

The v14.700 dimensionless ratio
\[
\Xi=\frac{1-R\Phi''/\Phi'}{3}
\]
depends on the physical radial potential, not directly on the bath's shape coordinate q or the phase integral rho. At the level of the already-defined model, fixing e=e_* changes neither the exact relation nor the Newtonian point-source prediction Xi=1.

An e-dependent correction to Xi cannot be inferred by substituting e_* into the Gram witness. It requires a derived bath-to-gravity coupling, an apparatus-level state-response rule, or a new radial field law with independent predictions.

## 5. Disposition and next gate

**[D]** Coordinate map and overlap evaluated exactly; two different mathematical sources for 2/3 separated. **[N]** Symbolic producer reproduces algebra. **[I]** The bath ray and phase profile can share classical eccentricity, but that identification alone supplies no new quantum or gravity dynamics. **[P]** No novel gravitational/tidal observable yet.

Next: derive the *actual* drift coefficients from the archived EFT v3.4, inspect their assumptions and asymptotic regime, and vary the collision/bath distribution within a physically derived model rather than an arbitrary drift. Independently search for a coupling from those dynamics to the measurable Xi channel. Retain the v14.703 Favard obstruction and the v14.704 audit's caveat that standard azimuthal dependence/metric were imported at rho=1.

No measured G inserted. Separatrix logarithm and apex initial-seat hypotheses remain physically unclosed. Suzuki far-tail remains untouched.
