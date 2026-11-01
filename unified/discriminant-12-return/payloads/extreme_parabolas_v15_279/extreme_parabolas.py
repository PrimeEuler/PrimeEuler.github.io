#!/usr/bin/env python3
"""
The +-1/2 as the EM ladder's extreme parabolas, focus at 0.
Row u: Y^2 = u^2 - 2uX (vertex +u/2); column u: Y^2 = u^2 + 2uX
(vertex -u/2); both have focus (0,0) for every u (v15.235). The
INNERMOST pair (smallest lattice step) has vertices at +-q where
q is the sector's charge quantum: EM step 1 -> vertices +-1/2;
gravity refined step 1/2 -> vertices +-1/4 (the weld's vertices,
v14.904: h = 2q). EM innermost crossing (1,1): the seat state.
j = 1/2 ladder: its extreme (only) states are m = +-1/2, its single
transition is the (1,1) pair with amplitude 1 = R = j + 1/2.
"""
import sympy as sp
from fractions import Fraction as Fr

X, Y, u = sp.symbols('X Y u', positive=True)
print("vertices and foci (symbolic, row family Y^2 = u^2 - 2uX):")
# Y^2 = -2u (X - u/2): vertex (u/2, 0), 4p = -2u, focus = vertex + p
for uu in [Fr(1, 2), Fr(1), Fr(3, 2), Fr(2), Fr(3)]:
    vertex = uu / 2
    p = -uu / 2
    print(f"  u={str(uu):>3s}: vertex X = +{vertex}, focus X = {vertex + p} "
          f"(column: vertex {-vertex}, focus {vertex + p})")
print("-> focus at 0 for EVERY u; the innermost vertices are +-u_min/2:")
print("   EM (step 1): +-1/2 = +-q_EM;  gravity (step 1/2): +-1/4 = +-q_G,")
print("   with q = h/2 the weld relation (v14.904). The extreme parabolas")
print("   of each sector carry the sector's charge quantum as their vertex")

print("\nEM innermost crossing (row 1 x column 1):")
n, k = 1, 1
print(f"  X = (n-k)/2 = {(n-k)//2}, Y = sqrt(nk) = 1, T = (n+k)/2 = 1")
print("  = the seat state (1,1): shell T = 1 = c_EM, the unit raw pair")
print("    of the weld (r = 0 sits at shell n = c_EM = 1).")
print("\nj = 1/2 ladder (EM fundamental): states m = -1/2, +1/2 (the extremes")
print("are the whole ladder); transitions: factor pairs of n+k = 2j+1 = 2:")
print("  pair (1,1): amplitude sqrt(1) = 1 = R = j + 1/2 -- the (1,1)")
print("  crossing's height. Casimir j(j+1) = 3/4: the EM class {0, 3/4}.")
print("So +-1/2 names three coincident extremes of the EM sector: the")
print("innermost parabola vertices, the j=1/2 ladder's end states, and")
print("the minimal pair charge s = +-1/2 (cone flip at s<0, v15.229).")
