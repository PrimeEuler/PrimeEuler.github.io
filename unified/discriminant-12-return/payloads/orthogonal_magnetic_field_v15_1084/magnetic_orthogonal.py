#!/usr/bin/env python3
"""
magnetic_orthogonal.py -- companion to charge_at_seat.py (sandbox,
2026-11-17). Jeremy's follow-on: "and the accelerating charged mass
creates the orthogonal magnetic field."

Exact symbolic checks (sympy; SI field transformations):

A. The magnetic field is the boost's shadow of the electric field.
   In the seat's rest frame S' the charge's velocity field is pure
   Coulomb: E' arbitrary, B' = 0. Boost along x at speed v
   (gamma = 1/sqrt(1-beta^2)):
       E = (Ex, gamma Ey, gamma Ez),
       B = (0, -gamma v Ez/c^2, gamma v Ey/c^2)   [= gamma (v x E')/c^2].
   Checks: B.v = 0 (B orthogonal to the motion); E.B = 0;
   E^2 - c^2 B^2 = E'^2 (the pair's invariant is the rest-frame
   Coulomb value -- boost-invariant, like uv = m^2 for the state
   pair); and c|B| / |E_perp| = v/c = tanh(psi): the magnetic
   component is the electric component times the pair's own
   leverage function.

B. The radiation field is an orthogonal null pair, and its B
   leaves the plane. At emission (rest frame), acceleration a
   along x, field point in the xy-plane (the plane containing the
   motion), n = (cos th, sin th, 0):
       E_rad ~ n x (n x a)  (Lienard-Wiechert radiation term),
       B_rad = (n x E_rad)/c.
   Checks: E_rad.n = 0, B_rad.n = 0, E_rad.B_rad = 0,
   |E_rad| = c|B_rad| (null pair: both invariants zero -- the
   hinge data), E_rad lies IN the plane (z-component 0) while
   B_rad is PURELY z: orthogonal to the entire (motion) plane.
   |E_rad| ~ a sin(th): the transverse projection of a.

Imported, not re-derived: the Lienard-Wiechert formulas
themselves and B = (n_ret x E)/c for the total field. Scope:
dictionary level, same fence as v15.1082 -- Maxwell dynamics is
the imported channel; nothing here selects a coupling.
"""
import sympy as sp

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


# ---------- A. boost generates B ----------
v, c = sp.symbols("v c", positive=True)
Ex, Ey, Ez = sp.symbols("Ex Ey Ez", real=True)
gamma = 1 / sp.sqrt(1 - v**2 / c**2)
E = sp.Matrix([Ex, gamma * Ey, gamma * Ez])
B = sp.Matrix([0, -gamma * v * Ez / c**2, gamma * v * Ey / c**2])
vel = sp.Matrix([v, 0, 0])
check("A1 B.v = 0 (B orthogonal to the motion)", sp.simplify(B.dot(vel)) == 0)
check("A2 E.B = 0", sp.simplify(E.dot(B)) == 0)
inv = sp.simplify(E.dot(E) - c**2 * B.dot(B))
check("A3 E^2 - c^2 B^2 = E'^2 (boost-invariant pair product)",
      sp.simplify(inv - (Ex**2 + Ey**2 + Ez**2)) == 0)
Eperp2 = (gamma * Ey)**2 + (gamma * Ez)**2
cB2 = c**2 * B.dot(B)
ratio2 = sp.simplify(cB2 / Eperp2)
check("A4 c^2 B^2 / E_perp^2 = v^2/c^2 = tanh^2(psi)",
      sp.simplify(ratio2 - v**2 / c**2) == 0)

# ---------- B. radiation pair ----------
th, a = sp.symbols("theta a", positive=True)
n = sp.Matrix([sp.cos(th), sp.sin(th), 0])
acc = sp.Matrix([a, 0, 0])
Erad = n.cross(n.cross(acc))          # ~ radiation E (up to LW prefactor)
Brad = n.cross(Erad)                   # B_rad = (n x E_rad)/c, c factored out
check("B1 E_rad.n = 0", sp.simplify(Erad.dot(n)) == 0)
check("B2 B_rad.n = 0", sp.simplify(Brad.dot(n)) == 0)
check("B3 E_rad.B_rad = 0", sp.simplify(Erad.dot(Brad)) == 0)
check("B4 |E_rad| = c|B_rad| (null pair: E^2 - c^2 B^2 = 0)",
      sp.simplify(Erad.dot(Erad) - Brad.dot(Brad)) == 0)
check("B5 E_rad lies in the motion plane (z-component = 0)",
      sp.simplify(Erad[2]) == 0)
check("B6 B_rad is purely off-plane (x,y components = 0, z = a sin th)",
      sp.simplify(Brad[0]) == 0 and sp.simplify(Brad[1]) == 0
      and sp.simplify(Brad[2] - a * sp.sin(th)) == 0)
check("B7 |E_rad| = a sin(th): transverse projection of the acceleration",
      sp.simplify(Erad.dot(Erad) - a**2 * sp.sin(th)**2) == 0)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
