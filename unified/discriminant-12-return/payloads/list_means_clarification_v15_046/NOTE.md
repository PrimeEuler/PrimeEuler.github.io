# Clarification: list AM–GM, the Lorentzian n+1 (the "1" is the list sum), and the monopole as dimension 1 (Sandbox)

Companion to v15.008 (the ladder). Here the object is a LIST of n
numbers — Jeremy's clarification that the question was the n-number
AM–GM itself, not the ladder or diameter 12. All identities [D],
machine-checked (payload script); identifications marked [I].

## List pictures [D]

Point picture: (x_1..x_n) as a point in R^n. Sphere through the
point (center origin) has radius sqrt(n) Q. **cos(angle to the
diagonal) = A/Q exactly**; distance to the diagonal = sqrt(n)
sqrt(Q^2 − A^2) = sqrt(n) x std — variance is a radial distance;
equality in every mean inequality is the diagonal.
Volume picture: the ellipsoid with semi-axes x_i has volume
V_n(1) G^n, so **G is the radius of the equal-volume ball**, and
AM–GM is ellipsoid/ball(A) = (G/A)^n <= 1. H is the dual reading,
H(x) = 1/A(1/x). Ladder corollary (v15.008): the ladder ellipsoid
was this theorem applied to the rung list (ratio 11!/6^11 = 0.110).
No equality between axis products and ball volumes is possible:
products are algebraic, ball volumes carry pi^{d/2} (pi
transcendental); V_n(1) peaks at d = 5 and decays — the ball is the
shape factor, the list supplies the axis product.
The chord picture does NOT generalize: power of a point gives a
product of exactly two segments in any dimension. n-fold products
live in the volume reading only — pairs are the atoms, lists
aggregate by volume.

## The Lorentzian n+1 — Jeremy's observation [D]

Coordinates (t; x_1..x_n) in R^{1,n} with **t = sqrt(n) A: the "1"
is the list sum**. Lorentz form:
  t^2 − |x|^2 = −sum (x_i − A)^2 = −n(Q^2 − A^2) <= 0.
Every list is timelike-or-null; the light cone is the equality
locus (all entries equal — isotropy is null); the Lorentzian norm
is minus the variance; Q >= A is "never spacelike".
Pair specialization: u, v are the null coordinates of the (T, X)
plane, **G^2 = uv = T^2 − X^2 is the Lorentzian interval** (twin of
the circle identity), and **s is the boost rapidity** (boost
u -> e^mu u shifts s by mu) — the Lorentzian reason the flux chain
found p_s to be a boost generator of continuous spectrum
(v14.949/950). The crossing matrix [[u, Y],[Y, v]] has trace = the
sum (the "1" as trace slot), det = uv − Y^2 = 0 (null), and is
rank-1 = chi chi^T: the pair spinor is the square root of a null
matrix (v14.990 in Lorentzian dress).
Boundary: for n >= 3 the quadratic form sees exactly (A, Q); G is
degree-n (a determinant), quadratic only at n = 2.

## Trace bounds determinant; the content ladder [D]

AM–GM for a list is **(tr/n)^n >= det** for diag(x_i): the sum
raised to the dimension bounds the content G^n. The content's name
is the dimension: n = 1 length, n = 2 area (at n = 2 det = the
Lorentzian interval = null-rectangle area — quadratic forms
measure areas, hence the Lorentzian stops at pairs), n = 3 volume,
n >= 4 n-content. G is always a length: the side of the
equal-content cube. The ladder (v15.008) climbs contents by
multiplying in one G per step.

## Monopole = dimension 1 — Jeremy's identification [I, exact backing]

Multipole moments of a charge list are power sums p_k = sum q_i
x_i^k: **p_0 = the list sum = the monopole = the Lorentzian "1"**.
A list of n charges carries n independent moments. The pair has
exactly two: p_0 = 2T (monopole), p_1 = 2X (dipole), p_2 = p_0 —
pair = monopole + dipole, carried on (T, X); the bicone is the
dipole's shape (two nappes, two poles), the monopole one cone.
List of 1 (the 1st AM–GM dimension, the un-split diameter): all
means coincide, dipole about its own center identically zero —
monopole only. Degenerate checks: seat u = v has p_1 = 0 (the
isotropic pair is monopole-only, pure sum on the diagonal);
vertex v = 0 kills G and leaves only the sum.

## Gravity assessment (asked and answered in-session)

- Selector/kappaC: NO new leverage, one sharpening — the source
  amplitude multiplies a bare sum (W = C A_B); dimension 1 has no
  internal structure from which a number could be derived, which
  is why the matching never becomes a derivation.
- Compression [I]: the k4 background is a pure-monopole
  (dimension-1) configuration; the three pair-charge negatives —
  Q_phi = Q_s collapse at s_0 = 0 (v14.988), triplet zero charge
  (v14.992), spinor decoupling (v15.014) — are one fact:
  dimension-2 data cannot live on a dimension-1 background.
- Pointer [I, heuristic only]: a derived amplitude, if one
  exists, must be imported from pair (dimension-2) data — the
  quarter's home; the record's own order is monopole-first
  (quarter from Taub–NUT/Misner, v14.731) then squared into the
  pair product (k/4)^2. The physical weld remains PARKED
  (v14.916); this clarification names the door, it does not open it.
- ADM zero modes are the monopole sector in Fourier dress —
  shared vocabulary, no new estimate. Pantheon untouched.

**Payload:** list_means.py, this NOTE.
