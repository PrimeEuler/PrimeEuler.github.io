#!/usr/bin/env python3
"""
duality_cones.py -- third companion in the charge-at-the-seat run
(sandbox, 2026-11-17). Jeremy's two questions:

(1) "Could you swap E for B and get the same results?"
(2) "Could we couple E to T and B to X?" (the T-cone / X-cone toy
    of v15.1042)

Exact symbolic checks (sympy; SI conventions, duality map
D: E -> cB, B -> -E/c):

A. Duality flips both invariants, preserves their modulus.
   I1 = E^2 - c^2 B^2, I2 = E.B, F = I1 + 2 i c I2.
   Under D: I1 -> -I1, I2 -> -I2, F -> -F (the theta=90-degree
   case of F -> e^{+-2 i theta} F under a general duality
   rotation); |F| is invariant under the general rotation.
   So the field algebra of v15.1082/v15.1084 replays verbatim
   under the swap -- with E and B exchanged everywhere.

B. But the seat tag changes species: applying D to the seat's
   boosted Coulomb field gives, in the rest frame, E = 0 and
   B = -E'/c -- a pure MAGNETIC Coulomb field. The dual seat
   carries a magnetic charge, not an electric one. The swap is
   exact as field algebra and costs a monopole as a source.

C. The E->T / B->X coupling as stated fails, and its repair is
   a sorting. From v15.1084: the velocity field's B is T-sector
   data (slaved to E by tanh psi), and the radiation field's E
   is hinge data -- so neither field species belongs to one
   cone. What DOES sort by cone is the sign of I1:
       I1 > 0  electric-dominant  -> T side  (seat velocity field:
                                             I1 = E'^2 > 0, checked)
       I1 = 0  null               -> hinge  (radiation, checked)
       I1 < 0  magnetic-dominant  -> X side  (dual seat field:
                                             I1 = -c^2 B'^2 < 0)
   exactly as sign(uv) sorts pairs in v15.1042. And under this
   sorting, duality D is precisely the T <-> X swap map, with
   the hinge (radiation) fixed as a set.

D. Price tag of the dual seat (imported: Dirac quantization,
   Gaussian units): eg = n hbar c/2 gives the magnetic coupling
   alpha_g = g^2/(hbar c) = n^2/(4 alpha) ~= 34.25 for n = 1 --
   the dual Larmor readout of v15.1082 would be enormous where
   the electric one is alpha-suppressed.

Scope: dictionary level throughout; Maxwell + Dirac imported.
The sorting in C is a statement about field configurations,
not a dynamics on either cone. Nothing is selected.
"""
import sympy as sp

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


c = sp.symbols("c", positive=True)
Ex, Ey, Ez, Bx, By, Bz = sp.symbols("Ex Ey Ez Bx By Bz", real=True)
E = sp.Matrix([Ex, Ey, Ez])
B = sp.Matrix([Bx, By, Bz])
I1 = E.dot(E) - c**2 * B.dot(B)
I2 = E.dot(B)

# ---------- A. duality swap ----------
Ed = c * B
Bd = -E / c
I1d = sp.expand(Ed.dot(Ed) - c**2 * Bd.dot(Bd))
I2d = sp.expand(Ed.dot(Bd))
check("A1 duality: I1 -> -I1", sp.simplify(I1d + I1) == 0)
check("A2 duality: I2 -> -I2", sp.simplify(I2d + I2) == 0)
# general rotation: E' = E cos + cB sin ; cB' = cB cos - E sin
th = sp.symbols("theta", real=True)
Er = E * sp.cos(th) + c * B * sp.sin(th)
cBr = c * B * sp.cos(th) - E * sp.sin(th)
I1r = sp.expand(Er.dot(Er) - cBr.dot(cBr))
cI2r = sp.expand(Er.dot(cBr))
mod2 = sp.simplify(I1r**2 + 4 * cI2r**2 - (I1**2 + 4 * c**2 * I2**2))
check("A3 |F| invariant under general duality rotation", mod2 == 0)

# ---------- B. dual of the seat field is a magnetic seat ----------
v = sp.symbols("v", positive=True)
gamma = 1 / sp.sqrt(1 - v**2 / c**2)
# seat velocity field (v15.1084 part A), rest-frame data E'
Ev = sp.Matrix([Ex, gamma * Ey, gamma * Ez])
Bv = sp.Matrix([0, -gamma * v * Ez / c**2, gamma * v * Ey / c**2])
Ed2 = c * Bv
Bd2 = -Ev / c
check("B1 dual seat field at rest (v=0): E_dual = 0",
      all(sp.simplify(x.subs(v, 0)) == 0 for x in Ed2))
check("B2 dual seat field at rest: B_dual = -E'/c (pure magnetic Coulomb)",
      all(sp.simplify(Bd2[i].subs(v, 0) + [Ex, Ey, Ez][i] / c) == 0
          for i in range(3)))

# ---------- C. sorting by sign(I1) ----------
I1_seat = sp.simplify(Ev.dot(Ev) - c**2 * Bv.dot(Bv))
check("C1 seat velocity field: I1 = E'^2 > 0 (T side)",
      sp.simplify(I1_seat - (Ex**2 + Ey**2 + Ez**2)) == 0)
th2, a = sp.symbols("theta a", positive=True)
n = sp.Matrix([sp.cos(th2), sp.sin(th2), 0])
acc = sp.Matrix([a, 0, 0])
Erad = n.cross(n.cross(acc))
Brad = n.cross(Erad) / c
I1_rad = sp.simplify(Erad.dot(Erad) - c**2 * Brad.dot(Brad))
check("C2 radiation field: I1 = 0 (hinge)", I1_rad == 0)
I1_dual = sp.simplify(Ed2.dot(Ed2) - c**2 * Bd2.dot(Bd2))
check("C3 dual seat field: I1 = -E'^2 < 0 (X side)",
      sp.simplify(I1_dual + (Ex**2 + Ey**2 + Ez**2)) == 0)

# ---------- D. Dirac price tag (numeric, imported formula) ----------
alpha_val = 1 / 137.035999084
alpha_g = 1 / (4 * alpha_val)
print(f"ILLUSTRATION Dirac n=1: alpha_g = 1/(4 alpha) = {alpha_g:.2f}")
check("D1 alpha_g(n=1) ~= 34.25 (1%)", abs(alpha_g / 34.25 - 1) < 0.01)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
