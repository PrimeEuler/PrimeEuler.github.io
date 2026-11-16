"""
The signed-pair X-cone extension (2026-11-16, sandbox;
Jeremy: extend the geometry -- a cone perpendicular to
the T cone, axis along X). Verified content:

Setup: a pair (u, v) of nonzero reals, coordinates
T = (u+v)/2, X = (u-v)/2, product s = uv. Master
identity: T^2 - X^2 = s.

1. Two perpendicular cones. With r = sqrt(|s|):
   s > 0 gives T^2 = X^2 + r^2 (the T cone, axis T);
   s < 0 gives X^2 = T^2 + r^2 (the X cone, axis X,
   perpendicular). The signed pair plane therefore
   maps onto |T^2 - X^2| = r^2: two perpendicular
   cones in (T, X, r) space. The four sign sectors
   are the four wedges: (+,+) future T cone (T > 0),
   (-,-) past T cone (T < 0), (+,-) right X cone
   (X > 0), (-,+) left X cone (X < 0).

2. The cones meet only at the hinge. Solving both
   cone equations gives r = 0 and T^2 = X^2. In pair
   terms r = 0 iff uv = 0: the boundary axes u = 0
   (T = -X) and v = 0 (T = +X) -- the two null lines,
   the m/s hinge of v15.858/v15.860.

3. The X cone's mesh is the same AM-GM mesh with
   roles swapped. Pair (n, -q), n, q > 0: axis
   X = (n+q)/2 = AM(n, q), transverse T = (n-q)/2
   (the offset, signed), radial r = sqrt(nq) = GM.
   Fixed-n rows are parabolas r^2 = n (X - T) in the
   (X-T, r) reading. Its seat is the balanced crossed
   pair (a, -a): T = 0, r = |X| = a.

4. Citizens. Same-shell difference pairs (v15.488)
   have product -4 m^2 sinh^2(dpsi/2) <= 0: they live
   on the X cone (hinge iff dpsi = 0). General
   difference pairs fall in either cone by the sign
   of (p1-p2)^2 = m1^2 + m2^2 - 2 m1 m2 cosh(dpsi).
   States (uv = m^2 > 0) live on the T cone; transfers
   live on the X cone: the perpendicular cone is the
   interaction sector, not a second state space.

5. Lattice content. Integer pairs with uv = -N
   (N > 0): exactly 2 d(N) of them, d(N) in each
   crossed quadrant -- the X cone inherits the same
   divisor function, doubled by orientation; seats
   (a, -a) at N = a^2, perfect squares again. No new
   arithmetic function appears; the sign sector is a
   quadrant label.

Scope: a completion of the pair plane's geometry
(dictionary/kinematics species, v15.858's corridor).
The uv sign flip is the Rindler mirror of the
2026-10-05 report (uv = +c^2 vs -rho^2); the four
sectors are the Rindler wedges. No dynamics, no
selector, and the force-law scope of v15.487/v15.488
is untouched: X-cone invariants are still
(m1, m2, dpsi).
"""
import sympy as sp
from fractions import Fraction as Fr

u, v = sp.symbols("u v")
T = (u + v) / 2
X = (u - v) / 2
assert sp.simplify(T**2 - X**2 - u * v) == 0
print("master identity: T^2 - X^2 = uv  [exact]")

# sector census on exact rational pairs
def sector(a, b):
    s = a * b
    t, x = (a + b) / 2, (a - b) / 2
    if s > 0:
        return "T-future" if t > 0 else "T-past"
    return "X-right" if x > 0 else "X-left"

tests = [(Fr(3), Fr(1)), (Fr(-3), Fr(-1)), (Fr(3), Fr(-1)), (Fr(-1), Fr(3)),
         (Fr(5, 2), Fr(1, 3)), (Fr(-5, 2), Fr(-1, 3)), (Fr(1, 3), Fr(-5, 2)), (Fr(-1, 3), Fr(5, 2))]
for a, b in tests:
    t, x = (a + b) / 2, (a - b) / 2
    r2 = abs(a * b)
    lhs = t * t - x * x
    assert lhs == a * b
    if a * b > 0:
        assert t * t == x * x + r2
    else:
        assert x * x == t * t + r2
    print(f"   ({a}, {b}): T={t}, X={x}, r^2={r2} -> {sector(a, b)}")

# hinge: intersection of the two cone surfaces
Tt, Xx, rr = sp.symbols("T X r", real=True)
sol = sp.solve([Tt**2 - Xx**2 - rr**2, Xx**2 - Tt**2 - rr**2], (Tt**2, rr), dict=True)
print(f"intersection of the cones: {sol} -- r = 0 and T^2 = X^2 (the null hinge)")

# X-cone mesh: pair (n, -q)
n, q = sp.symbols("n q", positive=True)
Xm = (n + q) / 2
Tm = (n - q) / 2
rm = sp.sqrt(n * q)
assert sp.simplify(Xm**2 - Tm**2 - rm**2) == 0
assert sp.simplify(rm**2 - n * (Xm - Tm)) == 0
print("X-cone mesh (n, -q): axis X = AM(n,q), transverse T = offset, r = GM;")
print("   X^2 - T^2 = r^2 exactly; fixed-n rows: r^2 = n (X - T), parabolas.")
a = sp.symbols("a", positive=True)
print(f"   seat (a, -a): T = {(a - a) / 2}, X = {(a + a) / 2}, r = a -- balanced crossed pair.")

# difference pairs
m, dpsi = sp.symbols("m dpsi", positive=True)
prod_same = -4 * m**2 * sp.sinh(dpsi / 2)**2
direct = m**2 * (2 - sp.exp(dpsi) - sp.exp(-dpsi))
assert sp.simplify(sp.expand(prod_same.rewrite(sp.exp)) - direct) == 0 or \
       sp.simplify(prod_same - (-2 * m**2 * (sp.cosh(dpsi) - 1))) == 0
print("same-shell difference product = -4 m^2 sinh^2(dpsi/2) <= 0 -> X cone [v15.488 recomputed]")

# lattice content
def dcount(N):
    return sum(1 for d in range(1, N + 1) if N % d == 0)

for N in (1, 2, 6, 12, 36, 60, 97, 120):
    pos = sum(1 for a in range(-N, N + 1) for b in range(-N, N + 1) if a * b == N and a != 0)
    neg = sum(1 for a in range(-N, N + 1) for b in range(-N, N + 1) if a * b == -N and a != 0)
    cross_r = sum(1 for a in range(1, N + 1) for b in range(-N, 0) if a * b == -N)
    cross_l = sum(1 for a in range(-N, 0) for b in range(1, N + 1) if a * b == -N)
    assert pos == 2 * dcount(N) and neg == 2 * dcount(N) and cross_r == cross_l == dcount(N)
    print(f"   N={N}: d(N)={dcount(N)}; integer pairs uv=+N: {pos}, uv=-N: {neg} "
          f"(right {cross_r} + left {cross_l}) -- X cone inherits d(N), doubled by orientation")
print("ALL CHECKS PASS")
