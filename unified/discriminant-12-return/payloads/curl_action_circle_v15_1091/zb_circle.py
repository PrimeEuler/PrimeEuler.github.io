#!/usr/bin/env python3
"""
zb_circle.py -- fourth in the charge-at-the-seat run (sandbox,
2026-11-17). Jeremy: "accelerating charge creates curl which
seems like the action circle."

Two exact blocks (sympy):

A. The curl is literal: the moving seat charge's B is PURELY
   AZIMUTHAL around the motion axis. From v15.1084's boosted
   Coulomb field, at field point with transverse coordinates
   (Y, Z) and Coulomb factor k (E' transverse = k(Y, Z)):
       B = gamma (v x E')/c^2 = (0, -gamma v k Z/c^2,
                                   gamma v k Y/c^2).
   Checks: B . rho_hat = 0 (no radial part), B_x = 0 (no axial
   part), B . phi_hat = |B| * rho (all of B is the circulating
   part). The magnetic field of the slid seat is a circulation
   around the trajectory -- field lines are circles about the
   axis, and the circulation oint B.dl = 2 pi rho B_phi != 0.

B. The action circle, with the charge ON it: the Dirac
   electron's Zitterbewegung circle. The velocity operator's
   eigenvalues are +-c and the position oscillates at the gap
   frequency; the associated circulation has
       r = hbar/(2mc),  omega = 2mc^2/hbar,  v = omega r = c.
   Checks against the seat's filed action data (v15.864):
     - circuit action oint p dx = (mc)(2 pi r) = pi hbar --
       EXACTLY the phase-space Compton-ellipse action
       oint p dx = pi hbar of v15.864;
     - circulation angular momentum L = m v r = hbar/2;
     - period tau_ZB = 2 pi/omega = pi * tau_C, with
       tau_C = hbar/(mc^2) the seat cycle of v15.864
       (E_rest tau_C = hbar) -- the ZB circuit is the pi hbar
       object, NOT the hbar object; the two stay distinct;
     - the circulating charge is a current loop:
       I = q omega/(2 pi), mu = I pi r^2 = q hbar/(4m) --
       the classical loop moment, mu/mu_B = 1/2 with
       mu_B = q hbar/(2m): the loop gives g = 1, Dirac gives
       g = 2. The missing factor is the spin-density curl of
       the Gordon decomposition (imported): the Dirac current
       splits into a convection part (the loop, g=1) and a
       polarization part that is literally a curl of the spin
       density (the second g=1).

Imported / scope: Zitterbewegung is a mathematical feature
of the Dirac equation (interference between the +E and -E
sectors -- in this run's language, the seat and its crossed
partner), not a literal classical orbit; the gated content
is the coincidence of scales (pi hbar, hbar/2, pi tau_C)
with the seat's action data. Dictionary level, as before.
"""
import sympy as sp

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


# ---------- A. B is purely azimuthal ----------
v, c, k = sp.symbols("v c k", positive=True)
Y, Z = sp.symbols("Y Z", real=True)
gamma = 1 / sp.sqrt(1 - v**2 / c**2)
B = sp.Matrix([0, -gamma * v * k * Z / c**2, gamma * v * k * Y / c**2])
rho_hat = sp.Matrix([0, Y, Z])
phi_hat = sp.Matrix([0, -Z, Y])
check("A1 B . rho = 0 (no radial component)", sp.simplify(B.dot(rho_hat)) == 0)
check("A2 B_x = 0 (no axial component)", B[0] == 0)
Bphi = sp.simplify(B.dot(phi_hat))  # = |B| * rho if B is purely azimuthal
Bmag2 = sp.simplify(B.dot(B))
check("A3 (B.phi)^2 = |B|^2 * rho^2 (B entirely azimuthal)",
      sp.simplify(Bphi**2 - Bmag2 * (Y**2 + Z**2)) == 0)

# ---------- B. the Zitterbewegung circle ----------
hbar, m, q = sp.symbols("hbar m q", positive=True)
r = hbar / (2 * m * c)
omega = 2 * m * c**2 / hbar
check("B1 omega * r = c (circulation at light speed)",
      sp.simplify(omega * r - c) == 0)
circuit_action = sp.simplify((m * c) * (2 * sp.pi * r))
check("B2 circuit action oint p dx = pi hbar (v15.864 ellipse action)",
      sp.simplify(circuit_action - sp.pi * hbar) == 0)
L = sp.simplify(m * c * r)
check("B3 circulation angular momentum L = hbar/2",
      sp.simplify(L - hbar / 2) == 0)
tau_C = hbar / (m * c**2)
tau_ZB = sp.simplify(2 * sp.pi / omega)
check("B4 period tau_ZB = pi * tau_C (the pi hbar object, not hbar)",
      sp.simplify(tau_ZB - sp.pi * tau_C) == 0)
I_loop = q * omega / (2 * sp.pi)
mu = sp.simplify(I_loop * sp.pi * r**2)
mu_B = q * hbar / (2 * m)
check("B5 loop moment mu = q hbar/(4m); mu/mu_B = 1/2 (loop g=1, Dirac g=2)",
      sp.simplify(mu - q * hbar / (4 * m)) == 0
      and sp.simplify(mu / mu_B - sp.Rational(1, 2)) == 0)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
