#!/usr/bin/env python3
"""
dipole_silence.py -- support check for the cross-reference entry
(sandbox, 2026-11-17): the single mass seat is dipole-silent;
the single charge seat is not.

Newtonian core, exact (sympy). Two particles, internal force f
(particle 1 feels +f, particle 2 feels -f; Newton's third law),
external force zero (isolated system):

  mass dipole    Dm = m1 x1 + m2 x2
  Dm'' = m1 a1 + m2 a2 = f - f = 0.
  The mass dipole's second derivative is the total momentum's
  derivative: identically zero for ANY isolated system, any N
  (pairwise cancellation). Hence no dipole gravitational
  radiation from a seat (or any isolated mass distribution);
  the leading gravitational channel is quadrupole. In GR the
  same statement reads: the mass dipole is the total energy
  times the center-of-energy position, whose rate is the
  conserved total momentum (imported textbook fact).

  electric dipole    De = q1 x1 + q2 x2
  De'' = q1 a1 + q2 a2 = f (q1/m1 - q2/m2),
  which vanishes only if q1/m1 = q2/m2. For one charge,
  De'' = q a != 0: the Larmor channel of v15.1082. The
  electric dipole radiates precisely because q/m is a
  per-particle ratio that need not be universal -- and the
  gravitational dipole is silent precisely because gravity's
  q/m is 1 for everything (the seat's single tag, v15.866
  side of the weld dictionary).

Checks: Dm'' == 0 identically; De'' == f(q1/m1 - q2/m2);
De'' == 0 iff q1/m1 == q2/m2 (sub q2 = q1 m2/m1); single-charge
De'' = q a.
"""
import sympy as sp

fails = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


m1, m2, q1, q2, f = sp.symbols("m1 m2 q1 q2 f", nonzero=True)
a1, a2 = f / m1, -f / m2  # internal forces, third law

Dm2 = m1 * a1 + m2 * a2
check("A1 mass dipole: Dm'' = 0 identically (isolated system)",
      sp.simplify(Dm2) == 0)

De2 = q1 * a1 + q2 * a2
check("A2 electric dipole: De'' = f (q1/m1 - q2/m2)",
      sp.simplify(De2 - f * (q1 / m1 - q2 / m2)) == 0)
check("A3 De'' = 0 when q/m is universal (q2 = q1 m2/m1): the "
      "gravitational case, one tag",
      sp.simplify(De2.subs(q2, q1 * m2 / m1)) == 0)
q, a = sp.symbols("q a", nonzero=True)
check("A4 single charge seat: De'' = q a != 0 (Larmor channel open)",
      sp.simplify(q * a) != 0)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
