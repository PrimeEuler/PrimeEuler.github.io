"""
The gravity tangency circle, built in the weld
dictionary (2026-11-13, sandbox; Jeremy: the EM hbar
unit circle has its transition parabola at 1/2 -- does
the 1/4 gravity parabola have a different circle?).

The machine is v14.620's diameter-secant split, run per
sector. A sector has step h (weld v14.904: EM h = 1,
vertices +-1/2, diagonal log n; G h = 1/2, vertices
+-1/4 = +-q, diagonal log(n/4), pair product (k/4)^2;
offset-lattice matching h = 2q). The sector's
transition (consecutive-node) split at level j is
(n, k) = ((j+1) h, j h):

  AM = h (j + 1/2),  GM = h sqrt(j (j+1)),
  offset = h/2,      AM^2 - offset^2 = GM^2,

and the pair point (offset, GM) lies on the secant
circle of radius AM (the master identity is the circle
equation). Checks:

1. The figure is h-similar: at fixed j every length of
   the G figure is exactly half the EM figure's. In the
   common plane the G circle is a different circle --
   radius (j + 1/2)/2 against j + 1/2 -- while the
   transition point's angular position on its circle,
   offset/AM = 1/(2j+1), is sector-independent.
2. The weld dictionary is one-parameter: q = h/2 and
   the diagonal's constant is c = 1/h^2 (EM: log(n/1);
   G: log(n/4)); the G sector's unit node sits at
   n = c = 4, EM's at n = 1.
3. What genuinely differs is the spectral correction
   offset^2 = h^2/4: EM 1/4 (the universal quarter of
   the Casimir/Langer/Maslov/bouncer record), G 1/16.
   Cross-check: the quarter grid's Casimir residues
   C = j(j+1) mod 1 are exactly {5/16, 13/16}
   (v15.544 sec.4), and 5/16 = q + q^2 at the G vertex
   q = 1/4, against EM's vertex value (1/2)(3/2) = 3/4.
4. The action quantum does NOT halve: per v14.620,
   hbar appears in none of the machine's formulas --
   it is the exchange rate (action per radian) named
   when the lattice is read as action, and the weld
   rescales the lattice, not the rate. The tangency
   circle of v15.864 (radius = the state's GM, cycle
   action exactly hbar) rescales the same way: the G
   state's circle has half the radius and twice the
   Compton period, product hbar again.

Verdict: YES a different circle (half radius at every
level, vertex at the quarter, correction 1/16 not 1/4,
unit node at n = 4); NO different quantum (hbar per
winding in both sectors). The dictionary is uniform in
j -- the shape P1 (h = 1/2 at every k) asserts, here
exhibited as construction, not evidence.
"""
from fractions import Fraction as Fr

import sympy as sp

j, h = sp.symbols("j h", positive=True)
AM = h * (j + sp.Rational(1, 2)); GM = h * sp.sqrt(j * (j + 1)); off = h / 2
print(f"master identity AM^2 - offset^2 - GM^2 = "
      f"{sp.simplify(AM**2 - off**2 - GM**2)} (identically, all h, j)")
print(f"circle radius AM: EM (h=1) = {AM.subs(h, 1)}, G (h=1/2) = {AM.subs(h, sp.Rational(1, 2))} "
      f"-- ratio exactly 1/2 at every j")
print(f"angular position offset/AM = {sp.simplify(off / AM)} -- no h: sector-independent")
print(f"offset^2 = {sp.simplify(off**2)}: EM {sp.Rational(1, 4)}, G {sp.Rational(1, 16)}")
print(f"dictionary: q = h/2 (EM 1/2, G 1/4); c = 1/h^2 (EM 1, G 4) -- weld values; "
      f"diagonal log(n h^2): unit node at n = 1/h^2")

print("\nquarter-grid Casimir residues (v15.544 sec.4 cross-check):")
res = sorted({(Fr(m, 4) * (Fr(m, 4) + 1)) % 1 for m in range(1, 40) if m % 2 == 1})
print(f"  j on the odd quarter grid: C mod 1 in {res} (record: {{5/16, 13/16}})")
q = Fr(1, 4)
print(f"  at the G vertex q = 1/4: q(1+q) = {q * (1 + q)} = q + q^2 = 1/4 + 1/16; "
      f"EM vertex (1/2)(3/2) = {Fr(1, 2) * Fr(3, 2)}")
half = sorted({(Fr(m, 2) * (Fr(m, 2) + 1)) % 1 for m in range(0, 20)})
print(f"  half grid (EM): C mod 1 in {half} (record v15.544: {{0, 3/4}} -- 0 at integers, 3/4 at halves)")

print("\nlevel table (j, EM circle radius, G circle radius, EM GM, G GM):")
for jj in range(0, 4):
    print(f"  j = {jj}: {jj + 0.5:.2f} / {(jj + 0.5) / 2:.3f} / "
          f"{(jj * (jj + 1)) ** 0.5:.4f} / {(jj * (jj + 1)) ** 0.5 / 2:.4f}")
print("\naction: tangency circle radius = GM (halves), Compton period = hbar/(GM c^2)")
print("(doubles), cycle action = hbar in both sectors -- the rate is not rescaled.")
