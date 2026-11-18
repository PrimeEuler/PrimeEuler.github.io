# A lattice field on the cone's null grid

Sandbox note (little Euler), 2026-11-18. Origin:
Jeremy's correction on the Craig mapping (the counting
lattice is only one lattice on the cone; spacetime lands
on it too, so a grid should be putable on that as well),
followed by his call the same day: "Go bigger: build a
lattice field on the null grid." Producer:
`null_grid_field.py`, 11 checks, ALL PASS.

Conventions: u = T + X, v = T − X on ℤ², unit spacing;
(∂T² − ∂X²) = 4∂u∂v; one-sided differences Δu, Δv;
lattice wave operator ΔuΔv. The grid is the integer
pair plane — the cone's spacetime, whose uv > 0 shells
are the T-cone states and uv < 0 the X-cone crossed
sector (v15.1042).

## A. The massless scalar is EXACT on this grid

The equation ΔuΔv φ = 0 has exactly the continuum
solution space: φ = f(u) + g(v) solves it identically
(integer-exact), and every solution marched from
characteristic boundary data is of that form (converse
verified exactly). The retarded propagator, marched by
the recursion with unit characteristic data, is exactly
the quadrant indicator θ(u)θ(v) — in (u,v)
normalization it IS the continuum propagator, not an
approximation of it. A Cartesian spacetime lattice does
none of this: its wave operator has lattice dispersion
throughout. The null grid's massless sector has no
lattice artifacts at all, because the operator
factorizes along the grid's own directions.

## B. The massive scalar: the scheme is a real choice

μ² = m²/4. Three discretizations, three verdicts:

- **Forward** (mass term at the corner): dispersion
  (e^{ip}−1)(e^{iq}−1) = −μ² is close to the shell
  (at p = 0.5, μ = 0.1: Re q = 0.01948 vs continuum
  0.02000) but COMPLEX — Im q = −0.00518, a phase drift
  per step. In the marched propagator the drift
  accumulates: deviation from J0(m√(uv)) on the
  diagonal is 0.035 at (10,10), 0.080 at (20,20),
  0.126 max by n = 40. Filed as the scheme's defect.
- **Box** (mass term on the cell average): dispersion
  is REAL and exact in the form tan(p/2)·tan(q/2) =
  μ²/4 (at p = 0.5: q = 0.01958 vs 0.02000, no drift).
  The marched propagator tracks J0(m√(uv)) on the
  diagonal to max deviation 0.00194 over n ≤ 40 —
  sixty times better than the forward scheme. This is
  the grid's working massive discretization.
- **Centered**: symbol sin p · sin q — real dispersion,
  but the massless zero set gains doubler lines at
  p = π and q = π. The symmetric scheme reintroduces
  exactly what the null grid avoids.

## C. The massless Dirac operator has no doublers

With one-sided differences (Δv ψ_R = −(m/2)ψ_L,
Δu ψ_L = +(m/2)ψ_R — the pair spinor's sector split,
right-movers constant along v, left-movers along u),
the symbol product is (e^{ip}−1)(e^{iq}−1); at m = 0
its zero set in the Brillouin zone is exactly the two
chiral lines p = 0 and q = 0 (scan: minimum off the
lines 0.01006 at the strip edge, value 4.0 at (π,π)).
No fermion doubling. The price is stated plainly: the
one-sided operator is not anti-Hermitian, which is the
standard light-front evasion of the Nielsen–Ninomiya
hypotheses — known structure in the lattice
light-front literature, claimed here only as verified
on this grid, not as new.

## D. Sectors and one sourced solution

The crossed-sector propagator is the same recursion
marched in (u, −v): the quadrant indicator on the
crossed quadrant. The full propagator support is
therefore the sector decomposition itself — future
T cone, past T cone, and the two X-cone crossed
quadrants, each with its own marching direction. One
sourced solution, exact: an eternal worldline source
on the diagonal (ΔuΔv φ = δ on u = v cells) gives
φ = g·min(u,v) identically — the field strength along
each null direction is constant, which is the 1+1
linear potential (constant force) written in null
form. Superposition is exact at this (free) level.

## E. Refinement: the Craig-flavored statement, on our grid

The coarse ΔuΔv over a 2×2 block of fine cells equals
the sum of the four fine ΔuΔv exactly (telescoping
identity, verified numerically) — so the massless
solution space is a single function space sampled at
every dyadic refinement: refinement-INVARIANT, exactly,
in the massless sector. The massive box propagator is
not invariant but converges: at (4,4) the deviation
from J0 is ~1×10⁻⁵ at unit spacing and smaller at
half spacing. Grid-to-grid consistency — the shape of
Craig's construction — exists on the cone's spacetime
grid as an elementary exact fact about the free field,
because the content was put in the factorized operator,
not in a comparison current.

## Scope, plainly

This is 1+1-dimensional free field theory (scalar +
Dirac) plus one sourced solution, on the pair plane.
Cone-specific content: the grid IS the frame's
spacetime (sectors, hinge, shells), the massless
exactness and doubler-freedom are properties of the
null factorization, and the propagator's support is
the sector decomposition. NOT present: gauge fields,
interacting dynamics beyond the sourced free field,
a fermion measure, 3+1 dimensions, any continuum-limit
theorem. Craig's question — a gauge-invariant measure
for chiral fermions — is still not posable here; what
this build changes is that the arena his question
would need now has filed field content on it, with
two exactness properties (massless sector, Dirac zero
set) that a Cartesian arena does not have. Corridor
classification: dictionary/transport species — the
field carries no selector and touches no door.

Flags: massless_scalar = EXACT (solution space +
propagator); massive_box = REAL dispersion, J0 to
0.00194; forward_scheme = DRIFT, filed; dirac =
NO DOUBLERS (one-sided price stated); refinement =
INVARIANT massless, convergent massive;
gauge_fields = ABSENT; measure = ABSENT; dim = 1+1.
