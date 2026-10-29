"""
Casimir distinction (sandbox, 2026-10-29): Jeremy's correction -- "the
casimirs are different."

Refined table as in table_test.py: (p, q) in Z^2, X = (p-q)/4, T = (p+q)/4,
j = T (Schwinger: j = (n1+n2)/2). Casimir C = j(j+1) = (j+1/2)^2 - 1/4.
The Casimir commutes with the whole EM ladder algebra, so it is an
EM-internal observable. Checks:
 1. C mod 1 by diagonal class: even diagonals (EM sector) vs odd
    diagonals (gravity-only) -- are the value classes disjoint?
 2. Within one EM shell: ladder (transition) circle radius^2 = (j+1/2)^2
    vs Casimir circle radius^2 = j(j+1): the cone's two landing families
    differ by exactly 1/4 in squared radius (Paper C / 2026-10-08).
 3. The gravity step (1, 0) changes diagonal class at every node; EM
    moves never cross the diagonal boundary (table_test.py, rechecked
    here through the Casimir classes).
"""
from fractions import Fraction as F
from collections import defaultdict

W = 24
mods = defaultdict(set)
counts = defaultdict(int)
for p in range(-W, W + 1):
    for q in range(-W, W + 1):
        T = F(p + q, 4)
        C = T * (T + 1)
        cls = 'even diagonals (EM)' if (p - q) % 2 == 0 else 'odd diagonals (gravity-only)'
        mods[cls].add(C % 1)
        counts[cls] += 1

for name in ['even diagonals (EM)', 'odd diagonals (gravity-only)']:
    print(f"{name:28s} count {counts[name]:5d}   C mod 1 = {sorted(str(x) for x in mods[name])}")
print("1) Casimir classes disjoint between sectors:",
      mods['even diagonals (EM)'].isdisjoint(mods['odd diagonals (gravity-only)']))

ok = True
for j2 in range(0, 21):                      # j = j2/2 in (1/2)Z
    j = F(j2, 2)
    if (j + F(1, 2)) ** 2 - j * (j + 1) != F(1, 4):
        ok = False
print("2) (j+1/2)^2 - j(j+1) = 1/4 exactly for all shells j in (1/2)Z:", ok,
      " -- ladder and Casimir landing circles never coincide")

def diag_cls(p, q):
    return (p - q) % 2 == 0
base = [(p, q) for p in range(-8, 9) for q in range(-8, 9)]
print("3) gravity step (1,0) flips diagonal class at every node:",
      all(diag_cls(p + 1, q) != diag_cls(p, q) for (p, q) in base))
em_moves = [(2, -2), (-2, 2), (2, 2), (2, 0), (0, 2)]
print("   EM moves preserve diagonal class at every node:",
      all(diag_cls(p + dp, q + dq) == diag_cls(p, q) for (p, q) in base for (dp, dq) in em_moves))
print("ALL CHECKS DONE")
