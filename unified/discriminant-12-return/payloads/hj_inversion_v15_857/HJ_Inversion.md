# Hamilton–Jacobi inversion on the cone's phase field: force from energy, executed

*Sandbox note (little Euler), 2026-11-13. Jeremy's
question that morning: a force accelerates an object and
transfers energy (joules); energy × time is action
(joule-seconds — the cone's native circles); shouldn't
force be derivable from the energy? This is the strongest
form of that route, the one v15.489 scoped but left
unexecuted: a complete phase field determines a
potential (Hamilton–Jacobi: p = ∂S/∂x, U = E − p²/2m;
for closed-orbit data J(E), Abel inversion). Executed
here on the cone's own field, with the other families of
the record as controls. Producer: `hj_inversion.py`.*

## The cone's field, inverted [D]

The cone's phase data is the constant-force family's
action function, the bouncer J(E) = (4√2/(3a√m))·E^{3/2}
(v15.469, exact record constant; its 2/3 is the parabola
segment law). Abel inversion,

x_tp(U) = (1/(π√(2m))) ∫₀^U J'(E)/√(U−E) dE

(bouncer J is a half-loop, so the image is the
turning-point function), with kernel integrals
∫₀¹√(t/(1−t)) dt = π/2 and ∫₀¹(1−t)^{−1/2} dt = 2 exact,
gives **x_tp(U) = U/(ma)** symbolically. Inverted: the
recovered potential is **U(x) = ma·x** — the linear
potential, whose slope is the family's own acceleration
times m. The inversion is faithful: it hands back
exactly the law whose action we fed it.

## The dictionary is impartial [D]

Same machinery, the record's other families:

- **Harmonic** J(E) = 2πE/ω inverts symbolically to
  width 2√(2U/(mω²)) — the quadratic well, exact match.
- **Kepler** radial data: J_r(E)'s measured log-log
  slope is **−0.5000**, and its turning-point function
  r_t(E) = k/|E| reads off E = −k/r_t — the inverse law
  U(r) = −k/r.

Numeric round trips (U → J by quadrature → Abel → width)
close at 1.0×10⁻³ (linear V-well) and 1.7×10⁻⁸
(harmonic). Each family's phase data returns its own
potential and no other: phase field and potential are
**one datum in two coordinates**, and a dictionary has
no preferences. Newton's law is unreachable from the
cone's data for the same reason the cone's law is
unreachable from Kepler's — the inversion creates
nothing.

## HJ directly, and the constant's fate [D]

On the cone's abbreviated action
S(x,E) = ∫₀ˣ √(2m(E − Fx′)) dx′: p = ∂S/∂x =
√(2m(E − Fx)) and U := E − p²/(2m) = **F·x identically**
(sympy, exact). And the family's parameter passes
through untouched: at a = 1, 2, 7 the recovered slope is
m·a each time. The inversion determines the law's
*form* from the family and leaves the family's constant
a supplied real in the output — Door III's shape,
appearing inside dynamics: the phase field fixes
everything except the number it was built from.

## Verdict

Force **is** derivable from the energy data — in the
only sense it ever is: from the energy as a *function*
(the complete phase field), never from energy as a
number, and the derivation is an exact inversion that
returns the family that generated the data. This closes
the Hamilton–Jacobi route scoped in v15.489 and stands
as the fourth exhibit of the input/output direction
(Kepler audit v15.277; force-law scan v15.487;
phase-integration readout v15.489): the cone's action
machinery — joule-second circles, segment areas,
single-valuedness — is complete and faithful, and it
transports laws without selecting them. What Jeremy's
chain E×t = action reaches is the dictionary; the
selector that would choose the family is not in the
dictionary, and now that is proved at the HJ level too,
not just scoped.
