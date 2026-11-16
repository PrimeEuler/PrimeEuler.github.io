# The signed-pair X-cone extension

*Sandbox note (little Euler), 2026-11-16. Jeremy: extend
the geometry — we have the T cone, what if there is an
X cone perpendicular to it? Verified in `x_cone.py`.*

## The extension [D]

A pair (u, v) of nonzero reals has coordinates
T = (u+v)/2, X = (u−v)/2 and the master identity
T² − X² = uv. With r = √|uv| the pair plane maps onto

**|T² − X²| = r²** —

two perpendicular cones in (T, X, r) space. Same-sign
pairs (uv > 0) lie on the **T cone** T² = X² + r² (axis
T: the state cone of the record). Opposite-sign pairs
(uv < 0) lie on the **X cone** X² = T² + r², axis along
X, perpendicular to the first. The four sign sectors
are the four wedges: (+,+) future T cone, (−,−) past
T cone, (+,−) right X cone, (−,+) left X cone.

## The hinge [D]

The two cone surfaces intersect only at r = 0 with
T² = X². In pair terms r = 0 iff uv = 0: the boundary
axes u = 0 and v = 0 map to the two null lines T = ±X
— the m/s hinge of v15.858/v15.860 is the seam where
the perpendicular cones meet, and the only place they
meet.

## The X cone's mesh and seat [D]

Its lattice is the same AM–GM mesh with roles swapped:
the pair (n, −q), n, q > 0 has axis X = (n+q)/2 =
AM(n, q), transverse T = (n−q)/2 (the offset, now
signed), radial r = √(nq) = GM, satisfying
X² − T² = r² exactly. Fixed-n rows are parabolas
r² = n(X − T). Its seat is the balanced crossed pair
(a, −a): T = 0, r = |X| = a — the mirror of the T
cone's seat u = v.

## Citizens: the X cone is the interaction sector [D]

States have uv = m² > 0 — T cone. Same-shell
difference pairs have product −4m² sinh²(Δψ/2) ≤ 0
(v15.488, recomputed) — X cone, reaching the hinge
iff Δψ = 0. General difference pairs fall in either
cone by the sign of (p₁−p₂)² = m₁² + m₂² − 2m₁m₂
cosh Δψ. So the perpendicular cone is not a second
state space: it is the cone of transfers, the
bilinear level's home (the kernel band lives on a
difference variable, v15.483/v15.488), given a
surface of its own.

## Lattice content [D]

Integer pairs with uv = −N (N > 0) number exactly
2 d(N) — d(N) in each crossed quadrant (enumerated,
N = 1…120 sample incl. 36, 60, 97, 120) — and the
crossed seats (a, −a) sit at N = a², perfect squares
again. The X cone inherits the divisor function,
doubled by orientation; no new arithmetic function
appears. The sign sector is a quadrant label, not new
arithmetic.

## Scope

A completion of the pair plane's geometry —
dictionary/kinematics species in the corridor of
v15.858. The uv sign flip is the Rindler mirror of
the 2026-10-05 exploration (uv = +c² vs −ρ²), and the
four sectors are the Rindler wedges, horizons on the
hinge. No dynamics is added and no selector appears;
the force-law scope of v15.487/v15.488 is untouched —
X-cone invariants are still (m₁, m₂, Δψ). What the
extension buys is architectural: states and transfers
now have perpendicular homes in one signed geometry,
joined only at the null hinge.
