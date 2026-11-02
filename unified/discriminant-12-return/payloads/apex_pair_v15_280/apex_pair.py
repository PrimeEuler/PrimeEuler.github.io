#!/usr/bin/env python3
"""
The apex sum performed by the innermost pair.
Mass parabola: row 1, Y^2 = 1 - 2X, vertex +1/2 (the +1/2 of the
bookkeeping -- Sciama's entry is a mass inventory, GM/Rc^2).
Counter parabola: column 1, Y^2 = 1 + 2X, vertex -1/2 (the seat --
the inertial counter side). Checks: their crossing lies on the
axis X = 0 at the seat state (0, 1); the vertex midpoint is 0;
their profile curvatures at the crossing are exactly opposite.
General pair (n, k): vertex midpoint = (n-k)/4 = X_cross/2 -- the
vertex sum vanishes iff the pair is on the diagonal.
"""
import sympy as sp
from fractions import Fraction as Fr

Y = sp.symbols('Y', real=True)
Xr = (1 - Y**2) / 2     # row 1 solved for X(Y): vertex +1/2
Xc = (Y**2 - 1) / 2     # column 1 solved for X(Y): vertex -1/2
print("innermost pair (n = k = 1):")
print("  vertices: row +1/2 (mass), column -1/2 (counter); midpoint = 0")
print("  crossing: X_row = X_col -> Y^2 = 1, X = 0: the seat state (0,1),")
print("            ON the apex axis -- the sum -1/2 + +1/2 = 0 is the")
print("            crossing's own X-coordinate.")
print(f"  curvatures at crossing: row d2X/dY2 = {sp.diff(Xr, Y, 2)}, "
      f"column d2X/dY2 = {sp.diff(Xc, Y, 2)} -- exactly opposite (net 0):")
print("            the counter parabola cancels the mass parabola's")
print("            curvature at their meeting point.")
print("\ngeneral pair (n, k): row vertex +n/2, column vertex -k/2,")
for n, k in [(1, 1), (2, 1), (3, 1), (6, 3), (5, 5)]:
    mid = Fr(n - k, 4); xc = Fr(n - k, 2)
    print(f"  (n,k)=({n},{k}): vertex midpoint {mid}, crossing X {xc}, "
          f"curvatures -1/{n}, +1/{k} "
          f"({'balanced (diagonal)' if n == k else 'imbalanced'})")
print("-> the vertex sum and the curvature sum vanish together, exactly")
print("   on the diagonal: balance is one condition in three readings.")
