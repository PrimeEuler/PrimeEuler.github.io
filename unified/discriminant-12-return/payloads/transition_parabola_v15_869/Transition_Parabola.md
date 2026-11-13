# The transition–parabola connection

*Sandbox note (little Euler), 2026-11-13. Jeremy: what
is the connection between the acceleration parabolas
and the wave's + to − transitions — the parts of the
sine wave with the fastest rate of change? Three links,
verified in `transition_parabola.py`.*

## Link 1: at a transition, the rate crowns on a parabola [D]

|sin′| = |cos| attains its maximum (= 1) exactly at
the nodes θ = kπ — Jeremy's fastest-rate observation,
exact. At those same points the velocity wave cos sits
at its own vertex (extremum), and its osculating
parabola there is 1 − θ²/2: value, slope, and curvature
all match, the curvature being −1 in turn units — the
circle's own. The position wave at the node is locally
linear (sin θ = θ − θ³/6 + …, no quadratic term, zero
curvature). So the parabola at a sign transition
belongs to the *rate of change*, not the position: each
transition is where the wave's rate tops out on a
parabola of the mesh's species (constant curvature),
just as the acceleration parabolas are the trajectories
of a uniformly changing rate.

## Link 2: node and vertex are a quarter turn apart [D]

Nodes at turns k/2; antinodes — the turning points,
the seat passages — at the odd quarters (2k+1)/4
(v15.867's lattices, interleaved with offset exactly
¼ turn). The oscillator state makes the alternation
physical: at the node it is pure momentum (|p|
maximal, x = 0 — fastest change), at the antinode pure
position (p = 0 — rest at the seat). Fastest change
and the parabola's vertex are not the same point; they
are the two ends of a quarter-turn swing, which is why
the transition lattice (halves) and the vertex lattice
(odd quarters) interleave rather than coincide.

## Link 3: the parabola's wave governs transition layers [D]

The acceleration parabola's potential is linear
(U = Fx), and its wave equation reduces exactly —
ξ = (2mF/ħ²)^{1/3}(x − E/F) — to ψ″ = ξψ, Airy's
equation (coefficients match identically; corroborated
by the zeros). Near any simple turning point,
U(x) − E = U′(x_t)(x − x_t) + O((x−x_t)²), so every
wave's transition layer is locally the parabola's
problem. The Airy zeros carry the confined-transition
ladder: |a_n| = 2.338107, 4.087949, 5.520560 against
the asymptotic [3π(n − ¼)/2]^{2/3} at ratios 1.0077,
1.0015, 1.0006 — the bouncer comb's (n − ¼) of
v15.867, i.e. the acceleration parabola's own wave
counting the transitions that cost phase.

## Scope

Links 1–2 are exact kinematics on the circle; link 3
is the standard WKB transition structure, verified at
the equation and the zero asymptotics. The connection
is local (osculating) and wave-equation level: the
mesh parabolas are not hiding inside the sine's
position curve — they crown its rate at every
transition, sit a quarter turn from its vertices, and
supply the wave equation of every transition layer.
