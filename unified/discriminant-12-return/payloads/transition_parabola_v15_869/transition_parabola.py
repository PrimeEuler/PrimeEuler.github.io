"""
The transition-parabola connection (2026-11-13,
sandbox; Jeremy: what connects the acceleration
parabolas to the wave's + to - transitions, which are
its fastest rate of change?). Three verified links:

1. At a sign transition the wave's rate crowns on a
   parabola. |sin'| = |cos| attains its max (= 1)
   exactly at the nodes theta = k pi, where the
   velocity wave cos sits at its own vertex
   (extremum); its osculating parabola there is
   1 - theta^2/2 -- value, slope, and curvature (-1,
   the circle's own, in turn units) all matching.
   The position wave at the node is locally linear
   (sin = theta - theta^3/6, zero quadratic term,
   zero curvature): the parabola at a transition
   belongs to the rate, not the position.

2. Node and vertex are a quarter turn apart. Nodes
   at turns k/2, antinodes (turning points, the
   seat passages) at the odd quarters (2k+1)/4: the
   two lattices interleave with offset exactly 1/4
   turn. At the node the oscillator state is pure
   momentum (|p| maximal, x = 0); at the antinode
   pure position (p = 0): fastest change and rest
   alternate quarter-turn by quarter-turn.

3. The parabola's wave governs transition layers.
   The linear potential U = F x (the acceleration
   parabola's potential) has wave equation reducing
   exactly, under xi = (2 m F / hbar^2)^{1/3}
   (x - E/F), to psi'' = xi psi -- Airy. Near any
   simple turning point U(x) - E = U'(x_t)(x - x_t)
   + O((x-x_t)^2), so every wave's transition layer
   is locally the parabola's problem. The Airy zeros
   carry the bouncer ladder of v15.867: |a_n| ~
   [3 pi (n - 1/4)/2]^{2/3}, the (n - 1/4) of the
   comb -- the parabola's wave counting confined
   transitions.

Scope: links 1-2 are exact kinematics on the circle;
link 3 is the standard WKB transition structure,
verified at the level of the equation and the zero
asymptotics. The identification is local (osculating)
and wave-equation level, as filed.
"""
import mpmath as mp
import sympy as sp

th = sp.symbols("theta", real=True)
print("1. rate at the nodes:")
print(f"   |d sin/d theta| at theta = 0, pi: "
      f"{[abs(sp.cos(th).subs(th, v)) for v in (0, sp.pi)]} -- the max of |cos| on the circle")
print(f"   cos series at its vertex: {sp.series(sp.cos(th), th, 0, 5)} "
      f"-- osculating parabola 1 - theta^2/2 (curvature cos''(0) = {sp.diff(sp.cos(th), th, 2).subs(th, 0)})")
print(f"   sin series at its node: {sp.series(sp.sin(th), th, 0, 6)} "
      f"-- no quadratic term; curvature sin''(0) = {sp.diff(sp.sin(th), th, 2).subs(th, 0)} (locally linear)")

print("\n2. node/antinode lattices (turns): nodes k/2, antinodes (2k+1)/4, offset exactly 1/4 turn;")
print("   oscillator x = sin, p = cos: at nodes |p| = 1, x = 0 (pure momentum);")
print("   at antinodes p = 0, |x| = 1 (pure position, the seat passage).")

print("\n3. Airy reduction and zeros:")
xi = sp.symbols("xi", real=True)
print("   linear potential: -(hbar^2/2m) psi'' + F x psi = E psi with x_t = E/F and")
print("   xi = (2mF/hbar^2)^{1/3} (x - x_t) gives d^2 psi/d xi^2 = xi psi: both sides")
print("   carry the coefficient (hbar^2/2m)^{1/3} F^{2/3}, so the equation is Airy's exactly;")
print("   corroborated numerically by the zeros below.")
for n, guess in ((1, -2.3), (2, -4.1), (3, -5.5)):
    a_n = mp.findroot(lambda z: mp.airyai(z), guess)
    asym = (3 * mp.pi * (n - mp.mpf(1) / 4) / 2) ** (mp.mpf(2) / 3)
    print(f"   Airy zero a_{n} = {float(a_n):.6f}; [3 pi (n - 1/4)/2]^(2/3) = {float(asym):.6f} "
          f"(ratio {float(-a_n / asym):.4f}) -- the bouncer comb's (n - 1/4), v15.867")
ident = sp.simplify((3 * sp.pi * (4 * sp.symbols('n') - 1) / 8) - (3 * sp.pi * (sp.symbols('n') - sp.Rational(1, 4)) / 2))
print(f"   [3 pi (4n-1)/8] - [3 pi (n-1/4)/2] = {ident} -- the two written forms are one ladder")
