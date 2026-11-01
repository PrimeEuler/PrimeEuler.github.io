#!/usr/bin/env python3
"""
How does the parabolic grid see the boost hyperbolas?

Pair coordinates of the mesh: crossing (u, v) -> X = (u-v)/2 (offset),
T = (u+v)/2 (AM), Y = sqrt(uv) (GM).  Interval: T^2 - X^2 = uv.
A boost hyperbola is uv = s^2 (constant interval / constant GM);
a boost by rapidity psi is (u, v) -> (e^psi u, e^-psi v), sliding
along it.  Checks (exact rationals where possible):

1. Every row u = const and column v = const meets the hyperbola
   uv = s^2 exactly once.
2. Along the hyperbola, AM = (u + s^2/u)/2 >= s = GM, with equality
   only at the diagonal u = v = s (the vertex / rest point):
   X = s sinh(psi), T = s cosh(psi), AM/GM = cosh(psi)  [v14.621].
3. The INTEGER lattice points on the hyperbola uv = N are exactly
   the factor pairs (d, N/d) of N: the grid samples the continuous
   boost orbit only at divisor pairs -- and every crossing on the
   hyperbola shares the ladder amplitude sqrt(N) = GM.
4. Every mesh crossing is a triple intersection: row, column, and
   boost hyperbola.
"""
from fractions import Fraction as F
import numpy as np

print("1) one crossing per row/column (exact): row u meets uv=s^2 at v=s^2/u")
for s2 in [F(6), F(12), F(36)]:
    pts = [(u, s2 / u) for u in [F(1), F(2), F(3), F(4), F(6)] if s2 / u > 0]
    print(f"   s^2 = {s2}: " + ", ".join(f"(u={u}, v={v})" for u, v in pts))

print("\n2) AM >= GM along the hyperbola, equality only at the vertex:")
s = 6.0
us = np.array([1.0, 2.0, 3.0, 4.0, 6.0, 9.0, 12.0, 36.0])
AM = (us + s**2 / us) / 2
X = (us - s**2 / us) / 2
psi = np.arcsinh(X / s)
print("   u      AM      X      psi     cosh(psi)  AM/GM")
for u_, a_, x_, p_ in zip(us, AM, X, psi):
    print(f"   {u_:>4}  {a_:>7.3f} {x_:>7.3f} {p_:>7.3f}  {np.cosh(p_):>8.4f}   {a_/s:.4f}")
print(f"   min AM = {AM.min():.3f} at u = {us[np.argmin(AM)]} = s (the diagonal):"
      " the grid reads the boost hyperbola as AM = GM cosh(psi),")
print("   offset = GM sinh(psi) -- gamma = AM/GM = cosh(psi) of v14.621.")

print("\n3) lattice points on uv = N are exactly the factor pairs:")
for N in [6, 12, 36, 72]:
    pairs = [(d, N // d) for d in range(1, N + 1) if N % d == 0]
    print(f"   N = {N:>2}: {len(pairs)} lattice points {pairs}"
          f"  -- all with amplitude sqrt(N) = {np.sqrt(N):.3f}")
print("   A boost slides a crossing continuously along its hyperbola;")
print("   the discrete grid sees the orbit only where a factor pair sits.")

print("\n4) triple intersection: crossing (u, v) = row u x column v x hyperbola uv")
u, v = F(9), F(4)
X, T, Y = (u - v) / 2, (u + v) / 2, u * v
print(f"   (9, 4): X = {X}, T = {T}, uv = {Y}, T^2 - X^2 = {T*T - X*X} = uv OK;")
print("   in 3D the hyperbola lifts to the LEVEL curve Y = sqrt(uv) = GM:")
print("   boost hyperbolas run level at height GM while the mesh parabolas")
print("   climb -- every crossing is where a row, a column, and one level")
print("   boost hyperbola meet.")
