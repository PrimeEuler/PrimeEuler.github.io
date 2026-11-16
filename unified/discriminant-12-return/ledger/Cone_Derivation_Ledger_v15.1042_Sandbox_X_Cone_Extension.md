# Cone Derivation Ledger v15.1042 — Sandbox: the signed-pair X-cone extension (the perpendicular cone is the interaction sector)

**Deposit type:** Sandbox exploration, independently checkable. Jeremy's
question 2026-11-16: extend the geometry — we have the T cone, what if
there is an X cone perpendicular to it? Producer re-executed at
staging, exit 0.

(1) The signed pair plane maps onto two perpendicular cones: with
T = (u+v)/2, X = (u−v)/2, r = √|uv|, the master identity T² − X² = uv
gives |T² − X²| = r² — same-sign pairs on the T cone T² = X² + r²
(states), opposite-sign pairs on the X cone X² = T² + r² (axis X,
perpendicular). The four sign sectors are the four wedges: future/past
T cones, right/left X cones. (2) The cones meet only at the hinge:
r = 0, T² = X² — in pair terms uv = 0, the boundary axes mapping to
the null lines T = ±X (the m/s hinge of v15.858/v15.860). (3) The
X cone's mesh is the same AM–GM mesh with roles swapped: pair
(n, −q) has axis X = AM(n, q), transverse T = offset (signed),
r = GM(n, q), rows r² = n(X − T); its seat is the balanced crossed
pair (a, −a) at T = 0. (4) Citizens: same-shell difference pairs
(product −4m² sinh²(Δψ/2) ≤ 0, v15.488 recomputed) live on the X
cone; general difference pairs fall in either cone by the sign of
(p₁−p₂)². The perpendicular cone is the interaction/transfer sector,
not a second state space. (5) Lattice content: integer pairs with
uv = −N number exactly 2 d(N), d(N) per crossed quadrant, seats at
N = a² — the X cone inherits the divisor function, doubled by
orientation; no new arithmetic function.

Scope: a completion of the pair plane's geometry (dictionary
species); the uv sign flip is the Rindler mirror of the 2026-10-05
exploration and the four sectors are the Rindler wedges. No dynamics
added, no selector; v15.487/v15.488 force-law scope untouched.

**Payload:** `payloads/x_cone_extension_v15_1042/` — X_Cone_Extension.md `51956fecd4d9d2b4f5da97db8a68fbaa8e01a9110a72e92528a7993fe74dc113`, x_cone.py `0cb5143aead0fca3acaf94ab5a2e562e6efb92f4b5bc00b003baa73baf305ce8`.
