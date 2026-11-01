#!/usr/bin/env python3
"""
The acceleration parabolas in F = ma; rest mass and the boost hyperbola.

Constant force F on mass m, starting from rest.
  Newton:     x_N = (1/2)(F/m) t^2                       -- the parabola
  Relativity: p = Ft exactly; E^2 = p^2 c^2 + m^2 c^4;
              x_R = (mc^2/F)( sqrt(1+(Ft/mc)^2) - 1 )    -- the hyperbola
With g := F/m (proper acceleration) and u = gt/c:
  x_R = (c^2/g)( sqrt(1+u^2) - 1 ),  (x_R + c^2/g)^2 - c^2 t^2 = (c^2/g)^2.
Checks: series gap parabola-minus-hyperbola; coordinate acceleration
under constant force; mass-shell tangent at the rest point.
"""
import sympy as sp

u = sp.symbols('u', real=True)
xR = sp.sqrt(1 + u**2) - 1          # in units of c^2/g
xN = u**2 / 2
print("x_R series:", sp.series(xR, u, 0, 9))
print("x_N series:", sp.series(xN, u, 0, 9))
print("gap x_N - x_R:", sp.series(xN - xR, u, 0, 9))
print("-> parabola and hyperbola agree through u^2 (position, velocity,")
print("   acceleration F/m at the rest point); first disagreement at u^4,")
print("   gap +u^4/8 - u^6/16 + ... -- the v15.233 tangency series verbatim.")
print("   Parabola lies OUTSIDE: Newton overshoots (relativity caps v < c,")
print("   the hyperbola bends to the null asymptote; the parabola runs past).")

# coordinate acceleration under constant force: v = pc^2/E, p = Ft
t, F, m, c = sp.symbols('t F m c', positive=True)
p = F * t
E = sp.sqrt(p**2 * c**2 + m**2 * c**4)
v = p * c**2 / E
a = sp.simplify(sp.diff(v, t))
print("\ncoordinate acceleration under constant force:")
print("   a(t) =", sp.simplify(a.rewrite(sp.sqrt)))
g = F / m
print("   with u = gt/c this is a = g (1+u^2)^(-3/2) = g/gamma^3:")
print("   check:", sp.simplify(a - g / (1 + (g * t / c)**2)**sp.Rational(3, 2)) == 0)
print("-> constant F is constant PROPER acceleration; coordinate a falls")
print("   as 1/gamma^3. The parabola (constant coordinate a) is the gamma->1")
print("   shadow of the hyperbola.")

# mass shell tangent at rest point
pp = sp.symbols('p', real=True)
Es = sp.sqrt(pp**2 * c**2 + m**2 * c**4)
print("\nmass shell E(p): dE/dp =", sp.diff(Es, pp), " = v; at p=0:", sp.diff(Es, pp).subs(pp, 0))
print("-> rest point is the vertex of the boost hyperbola E^2 - p^2c^2 = (mc^2)^2;")
print("   tangent there is E = mc^2 (horizontal); force slides the point along")
print("   the shell at dp/dt = F, mass = the shell's label (grid: GM = s).")
