"""
Cone-selection test (sandbox, 2026-10-29): Jeremy's claim -- the cone
selects the EM sector, and the EM ladder operators are the even diagonals
of the multiplication table.

Table: the mesh is the (n1, n2) multiplication table (Paper C remark,
2026-10-08). At gravity resolution h = 1/2 the row/column labels run over
half-integers: refined indices (p, q) in Z^2, (n, k) = (p/2, q/2).
Node coordinates (mesh formulas): X = (n-k)/2 = (p-q)/4 (offset),
T = (n+k)/2 = (p+q)/4 (AM). A diagonal of the table is constant p - q,
i.e. constant X. Checks:
 1. diagonal parity == sector: p-q even  <=>  X, T in (1/2)Z (EM);
    p-q odd  <=>  X, T odd quarters (gravity-only).
 2. smallest positive |X| per class: even -> 1/2 (EM vertex),
    odd -> 1/4 (gravity vertex = pair quantum q_G).
 3. ladder moves: every EM move (double steps in refined indices)
    changes the diagonal index by an EVEN amount and preserves the
    sector; the gravity single steps change it by 1 and swap sector.
 4. Schwinger shell fact: at fixed shell s = n1 + n2 all offsets
    n1 - n2 share s's parity; the in-shell ladder step changes the
    offset by exactly 2.
"""
from fractions import Fraction as F

W = 16
pts = {}
for p in range(-W, W + 1):
    for q in range(-W, W + 1):
        X, T = F(p - q, 4), F(p + q, 4)
        pts[(p, q)] = (X, T)

bad = 0
counts = {'even': 0, 'odd': 0}
minX = {'even': None, 'odd': None}
for (p, q), (X, T) in pts.items():
    cls = 'even' if (p - q) % 2 == 0 else 'odd'
    counts[cls] += 1
    if cls == 'even' and not (X.denominator <= 2 and T.denominator <= 2):
        bad += 1
    if cls == 'odd' and not (X.denominator == 4 and T.denominator == 4):
        bad += 1
    if X > 0 and (minX[cls] is None or X < minX[cls]):
        minX[cls] = X
print("1) diagonal parity == sector: violations =", bad, " counts =", counts)
print("2) smallest positive offset |X|: even diagonals ->", minX['even'],
      " (EM vertex)   odd diagonals ->", minX['odd'], " (gravity vertex)")

moves = {
    'J+  (n1+1, n2-1)': (2, -2), 'J-  (n1-1, n2+1)': (-2, 2),
    'shell ladder (n1+1, n2+1)': (2, 2), 'oscillator a1+ (n1+1)': (2, 0),
    'oscillator a2+ (n2+1)': (0, 2),
    'GRAVITY row step': (1, 0), 'GRAVITY column step': (0, 1),
}
print("3) ladder moves (delta diagonal index, sector behaviour):")
for name, (dp, dq) in moves.items():
    dd = dp - dq
    swaps = all((((p - q) % 2) != ((p + dp - (q + dq)) % 2)) for (p, q) in list(pts)[:50])
    keeps = all((((p - q) % 2) == ((p + dp - (q + dq)) % 2)) for (p, q) in list(pts)[:50])
    print(f"   {name:28s} d_diag = {dd:+d}   preserves sector: {keeps}   swaps sector: {swaps}")

print("4) Schwinger shells (integer table): offset parity == shell parity")
ok = True
for s in range(0, 25):
    offs = {n1 - (s - n1) for n1 in range(0, s + 1)}
    if any((o - s) % 2 != 0 for o in offs):
        ok = False
print("   all offsets n1-n2 = s (mod 2) at fixed shell s:", ok,
      " -> in-shell ladder step (+1,-1) changes offset by exactly 2")
print("ALL CHECKS DONE")
