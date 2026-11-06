"""
Are the acceleration dynamics of the parabolas also the 2/3
parabola relation? (2026-11-06, sandbox; Jeremy's question.)

Yes -- and the mediation is an identity, not an analogy. For
constant force the phase-space orbit is a parabola, and the
action is that parabola's segment area. So the dynamics
carries the segment constant 2/3 inside its action, and the
reciprocal exponent 2/3 in its quantization. Checks:

 1. Archimedes on the cone's OWN mesh parabola,
    T(Y) = Y^2/(2u) + u/2 (a row/column of the canonical
    mesh): segment / circumscribing parallelogram = 2/3
    exactly, at every height h and every mesh parameter u.
 2. The constant-acceleration (bouncer) action: the orbit
    p(z) = sqrt(2m(E - maz)) is a parabola; its enclosed area
    is J(E) = (4m sqrt(2a)/3) h^(3/2) -- the 2/3 enters as
    int_0^h sqrt(h-z) dz = (2/3) h^(3/2), the segment integral
    of the square-root profile (the parabola read through its
    inverse function: the rectangle splits 2/3 + 1/3).
    Hence J ~ E^(3/2) and quantization J = 2 pi hbar (n - 1/4)
    gives the Airy comb E_n ~ (n - 1/4)^(2/3) -- checked
    against the true Airy zeros (asymptotic, < 1%).
 3. The acceleration locus: the evolute of the f = 1/2
    parabola y = x^2/2 -- the locus of centers of curvature,
    i.e. where the normal acceleration of a point riding the
    curve is aimed -- is exactly 27 X^2 = 8 (Y - 1)^3, the
    semicubical parabola of v14.592: the 2/3 curve itself.

Type discipline (2026-11-04, unchanged): the 2/3 fails as an
additive CHARGE; its home is the action/phase/spectrum of
constant-acceleration motion -- the dynamics sector, which is
where masses live. This grounds the type remark filed with
the Koide observation (v15.468 sec.1.3): the cone's 2/3 is a
constant of its acceleration dynamics, not a static curiosity.
"""
import sympy as sp

print("=" * 76)
print("1. Archimedes on the cone's mesh parabola T(Y) = Y^2/(2u) + u/2")
print("=" * 76)
Y, h, u = sp.symbols('Y h u', positive=True)
T = Y**2 / (2 * u) + u / 2
Th = h**2 / (2 * u) + u / 2
seg = sp.integrate(Th - T, (Y, -h, h))
par = 2 * h * (Th - u / 2)
print(f"  segment area        = {sp.simplify(seg)}")
print(f"  parallelogram area  = {sp.simplify(par)}")
print(f"  ratio = {sp.simplify(seg / par)}   (Archimedes 2/3, for all h, u)")

print()
print("=" * 76)
print("2. constant-acceleration action = parabolic segment area")
print("=" * 76)
z, E, m, a = sp.symbols('z E m a', positive=True)
hz = E / (m * a)
p = sp.sqrt(2 * m * (E - m * a * z))
J = 2 * sp.integrate(p, (z, 0, hz))
print(f"  J(E) = ointegral p dz = {sp.simplify(J)}")
prof = sp.integrate(sp.sqrt(hz - z), (z, 0, hz))
print(f"  the profile integral int sqrt(h-z) dz = {sp.simplify(prof)}"
      f"  = (2/3) h^(3/2): {sp.simplify(prof - sp.Rational(2, 3) * hz**sp.Rational(3, 2)) == 0}")
print("  J ~ E^(3/2) with the segment constant 2/3 inside; quantize")
print("  J = 2 pi hbar (n - 1/4)  =>  E_n ~ (n - 1/4)^(2/3). Check vs")
print("  true Airy zeros |a_n| (bouncer spectrum, units of the")
print("  asymptotic scale [(3 pi/2)(n - 1/4)]^(2/3)):")
airy = [2.338107, 4.087949, 5.520560, 6.786708, 7.944134, 9.022651,
        10.040174, 11.008524]
import math
for n, az in enumerate(airy, start=1):
    asym = (1.5 * math.pi * (n - 0.25)) ** (2 / 3)
    print(f"    n = {n}: |a_n| = {az:.6f}, asymptotic = {asym:.6f}, "
          f"err = {100 * (asym - az) / az:+.2f}%")

print()
print("=" * 76)
print("3. the acceleration locus: evolute of y = x^2/2 (f = 1/2)")
print("=" * 76)
x = sp.symbols('x', real=True)
yy = x**2 / 2
yp, ypp = sp.diff(yy, x), sp.diff(yy, x, 2)
Xc = sp.simplify(x - yp * (1 + yp**2) / ypp)
Yc = sp.simplify(yy + (1 + yp**2) / ypp)
print(f"  center of curvature: X = {Xc},  Y = {Yc}")
ident = sp.simplify(27 * Xc**2 - 8 * (Yc - 1)**3)
print(f"  27 X^2 - 8 (Y-1)^3 on the evolute = {ident}  -> the semicubical")
print("  parabola 27 X^2 = 8 (Y-1)^3 of v14.592, cusp at (0, 1): the")
print("  locus the acceleration vector aims at is the 2/3 curve.")

print()
print("=" * 76)
print("VERDICT")
print("=" * 76)
print("Yes: same structure, mediated by an identity. The mesh")
print("parabolas are the cone's constant-acceleration atlas")
print("(v15.270s); constant force makes the phase orbit a")
print("parabola; the action is its segment area; so the segment")
print("constant 2/3 sits inside the action, its reciprocal in")
print("the spectrum (n - 1/4)^(2/3), and the acceleration locus")
print("is the semicubical 2/3 curve. The 2/3's home type is the")
print("dynamics/action sector -- where masses live -- which is")
print("why it failed as a charge (2026-11-04) and why a")
print("mass-sector relation (Koide, v15.468) is its right type")
print("of fingerprint. The constant is one; the sectors differ.")
