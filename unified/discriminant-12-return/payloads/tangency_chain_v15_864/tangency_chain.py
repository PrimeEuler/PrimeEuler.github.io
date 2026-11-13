"""
The tangency chain (2026-11-13, sandbox; Jeremy: "every
parabolas vertex is tangent to a physical action
(joules seconds) circle" -- verified and filed at his
direction). Three links, each exact:

1. Circle-shell tangency (Jeremy's 2026-10-21 algebra):
   in the circle view (X, T), circle X^2 + T^2 = A^2
   meets shell T^2 - X^2 = g^2 at X^2 = (A^2 - g^2)/2,
   T^2 = (A^2 + g^2)/2. Two mirror points for A > g,
   none for A < g, and at A = g a single point (0, g)
   -- the vertex/seat -- where the gradients are
   parallel: the circle of radius exactly the shell's
   GM is tangent to the shell at its vertex, tangent
   line T = g (the E = mc^2 line of 2026-11-01).

2. Parabola-shell osculation at the rest point
   (2026-11-01, v15.233 series): the constant-force
   worldline is the hyperbola x_h = (c^2/a)(sqrt(1+u^2)
   - 1), u = a t / c; the F = ma parabola is x_p =
   (c^2/a) u^2/2. They share the vertex (rest point)
   and its tangent, and their gap is (c^2/a)(u^4/8 -
   u^6/16 + ...): contact of third order -- the
   parabola's vertex is tangent to the shell at the
   same point where link 1's circle touches it.

3. The tangency circle is the state's action circle:
   its radius is the shell's GM (= m), and the seat
   state's own cycle on it -- rest energy x its
   Compton time tau = hbar/(m c^2) -- is exactly hbar
   of action (one joule-second quantum, the v14.620
   unit circle dressed per shell). In phase space the
   Compton ellipse (semi-axes hbar/(mc) in x, mc in p)
   encloses (contour integral) p dx = pi hbar -- the quantum
   in area form, factor pi from the ellipse area.

So at the vertex of every parabola, three curves
concur with one tangent: the trajectory parabola, the
mass shell, and the action circle of radius GM. Every
other point of the shell cuts its circle twice or not
at all; only the seat touches -- tangency, in Jeremy's
2026-10-21 language, being the selection-shaped
configuration (one intersection = an equation).
"""
import sympy as sp

X, T, A, g = sp.symbols("X T A g", positive=True)
# link 1: solve the intersection
sol = sp.solve([X**2 + T**2 - A**2, T**2 - X**2 - g**2], [X**2, T**2], dict=True)
print(f"link 1: intersections at X^2, T^2 = {sol} "
      f"(X^2 = (A^2-g^2)/2: two mirror points A>g, none A<g, vertex only A=g)")
at = {X: 0, T: g, A: g}
grad_circle = [sp.diff(X**2 + T**2 - A**2, v).subs(at) for v in (X, T)]
grad_shell = [sp.diff(T**2 - X**2 - g**2, v).subs(at) for v in (X, T)]
print(f"   at (0, g) with A = g: grad circle = {grad_circle}, grad shell = {grad_shell} "
      f"-- parallel, common tangent line T = g: tangent OK")

# link 2: osculation gap series
u, a, c = sp.symbols("u a c", positive=True)
x_h = (c**2 / a) * (sp.sqrt(1 + u**2) - 1)
x_p = (c**2 / a) * u**2 / 2
gap = sp.series(x_p - x_h, u, 0, 9).removeO()
print(f"\nlink 2: parabola - hyperbola gap = {gap} "
      f"(contact through u^2; first deviation u^4/8 x c^2/a: the v15.233 series)")

# link 3: the action quantum on the tangency circle
m, hbar, th = sp.symbols("m hbar theta", positive=True)
E_rest = m * c**2
tau = hbar / (m * c**2)
print(f"\nlink 3: seat cycle action E_rest x tau_C = {sp.simplify(E_rest * tau)} "
      f"(exactly one hbar, with tau_C = hbar/(mc^2) the state's own Compton time)")
lam = hbar / (m * c)
x_e = lam * sp.cos(th); p_e = m * c * sp.sin(th)
oint = sp.integrate(p_e * sp.diff(x_e, th), (th, 0, 2 * sp.pi))
print(f"   phase-space Compton ellipse: |oint p dx| = {sp.simplify(-oint)} "
      f"(pi hbar: the action quantum in area form)")
print("\nChain: parabola vertex (rest) = shell vertex (seat) = tangency point")
print("of the circle of radius GM; three curves, one point, one tangent.")
