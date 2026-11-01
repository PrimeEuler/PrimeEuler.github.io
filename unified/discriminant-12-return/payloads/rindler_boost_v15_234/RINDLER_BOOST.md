# The parabola in the Rindler frame; the grid's view of boost hyperbolas

Producers: `rindler_parabola.py`, `boost_grid.py` (+ outputs).

## A. The Galilean parabola in its own Rindler frame
Rindler frame of the true g-observer: X = x + c²/g (hyperbola
vertex at the observer), X = ρ cosh η, ct = ρ sinh η. The parabola
x = ½gt² becomes, exactly,

    ρ² = (c²/g)² + (½gt²)²

— the t² terms of X² − c²t² cancel identically (the algebraic form
of the v15.233 parabola–hyperbola tangency). ρ departs
monotonically (c²/g → ∞) but Rindler time FOLDS: η rises to
η_max = ln(1+√2) = 0.881374 at u = gt/c = √2, ρ = √2 c²/g, then
decreases to 0 as ρ → ∞. The fold point is exactly the σ = 1
grazing crossing of v15.233, seen from the accelerated frame; the
inertial edge crossing (u = 2) lies on the returning branch at
η = ½ ln 5 = 0.8047, the same η as the outbound u = 1 point.
Family (parabola a in frame g): ρ dips first iff a < g; the
parabola exits the wedge through the horizon before folding iff
a < g/2 (a/g = 1/4 exits at u = 1.172); at a = g/2 the fold is on
the horizon (η → ∞); for a > g/2 the fold is inside (η_max =
1.1462, 0.8814, 0.6585, 0.5493, 0.3695 at a/g = 3/4, 1, 3/2, 2, 4);
a = g is marginal — ρ flat to fourth order at departure.

## B. How the parabolic grid sees the boost hyperbolas
Pair coordinates: crossing (u, v), X = (u−v)/2, T = (u+v)/2,
Y = √(uv); boost hyperbola uv = s².
1. Resolution: every row u = const and column v = const meets the
   hyperbola exactly once (v = s²/u) — the grid is a complete
   coordinate system for the boost family.
2. Reading: GM = s is the hyperbola's label; along it
   AM = GM cosh ψ, offset = GM sinh ψ, γ = AM/GM = cosh ψ
   (v14.621's identity as grid-reading). AM is minimized at the
   diagonal u = v (vertex, ψ = 0 — the hyperbola's seat).
3. Sampling: the integer lattice points on uv = N are exactly the
   factor pairs (d, N/d), all with ladder amplitude √N = GM. A
   boost slides a crossing continuously along its hyperbola and
   meets the discrete grid only at factor pairs; boost composition
   is multiplication in the table.
4. Lift: the hyperbola is the LEVEL curve Y = GM in 3D, while the
   mesh parabolas climb; every mesh crossing is a triple
   intersection row ∩ column ∩ level hyperbola. (The Rindler
   frame's ρ = const lines are these hyperbolas — the accelerated
   observer's rulers are the grid's level sets.)
