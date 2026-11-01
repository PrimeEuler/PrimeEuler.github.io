#!/usr/bin/env python3
"""
Each mesh point is where two parabolas of opposite sign intersect.

Projected (T-view) canonical parabolas (record's figure convention):
    row n:    Y^2 = n^2 - 2nX      (sign -, opens toward -X)
    column k: Y^2 = k^2 + 2kX      (sign +, opens toward +X)
Checks: (1) intersections of a row/column pair; (2) foci of both
families; (3) the count over a patch of the mesh.
"""
import sympy as sp

X, Y = sp.symbols('X Y', real=True)
n, k = sp.symbols('n k', positive=True)

row = Y**2 - (n**2 - 2 * n * X)
col = Y**2 - (k**2 + 2 * k * X)
sol = sp.solve([row, col], [X, Y], dict=True)
print("intersections of row n and column k (symbolic):")
for s in sol:
    print("   X =", sp.simplify(s[X]), ", Y =", sp.simplify(s[Y]))
print("-> exactly TWO: the crossing ((n-k)/2, +sqrt(nk)) and its mirror")
print("   ((n-k)/2, -sqrt(nk)) -- the two nappes of the cone.")

print("\nfoci: row Y^2 = -2n (X - n/2): vertex (n/2, 0), 4p = -2n,")
print("focus = (n/2 - n/2, 0) = (0, 0).")
print("      col Y^2 = +2k (X + k/2): vertex (-k/2, 0), 4p = +2k,")
print("focus = (-k/2 + k/2, 0) = (0, 0).")
print("-> BOTH families are confocal at the ORIGIN (the apex): the mesh")
print("   is exactly the classical confocal-parabola system that defines")
print("   parabolic coordinates -- which is why the HJ equation separates")
print("   there (MIC v14.731, TN tn_sector.py).")

print("\npatch check (n, k in 1..8): every crossing is one row-parabola")
cnt = 0
for nn in range(1, 9):
    for kk in range(1, 9):
        Xv = sp.Rational(nn - kk, 2)
        Yv2 = nn * kk
        assert (nn**2 - 2 * nn * Xv) == Yv2 and (kk**2 + 2 * kk * Xv) == Yv2
        cnt += 1
print(f"   x one column-parabola intersection: {cnt}/64 crossings verified,")
print("   each the meeting of a '-' parabola (row) and a '+' parabola (column).")
