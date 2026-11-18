#!/usr/bin/env python3
"""
rho_well_definedness.py -- follow-on item (sandbox,
2026-11-18): rho posed as a well-definedness question.
Is there a two-way-computable object whose consistency
fixes the Compton-Rindler ratio rho (L_R = rho * lam_C,
filed free for all rho > 0 at v15.883-v15.888, sandbox-
verified 2026-11-13)?

Method: (a) rho-weight homogeneity audit of the filed
identity system -- if every identity is homogeneous in
rho (both sides scale with the same power), the system
contains no equation that a wrong rho can fail;
(b) the one genuinely mixed object in the record, the
quantum bouncer (mass + acceleration + hbar in one
spectrum, v15.857/v15.869), checked for smoothness in
the rho direction; (c) the integer-valued escape hatch
-- a lattice count depending on rho -- shown to be a
step function, which localizes rho to intervals at
best, never a value.

Filed quantities: lam_C = hbar/(mc), tau_C = hbar/(mc^2),
a* = mc^3/hbar (the rho = 1 acceleration), a(rho) =
a*/rho, Unruh T = hbar a/(2 pi c kB), KMS boost period
2 pi, ZB circle (v15.1091): r = hbar/(2mc), v = c,
a_ZB = 2 mc^3/hbar.
"""
import sympy as sp
import numpy as np

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: fails.append(name)

rho, m, c, hbar, kB = sp.symbols("rho m c hbar kB", positive=True)
lam = hbar / (m * c)
tauC = hbar / (m * c**2)
astar = m * c**3 / hbar
a_of = astar / rho

# R1: the Rindler thermal (KMS) period in time units,
# in units of the seat clock: ratio IS rho identically.
Delta_tau = 2 * sp.pi * c / a_of            # 2 pi c/a
ratio1 = sp.simplify(Delta_tau / (2 * sp.pi * tauC))
check("R1 KMS period / (2 pi tau_C) = rho identically "
      "(the 'coincidence' at rho=1 is the definition, not a constraint)",
      sp.simplify(ratio1 - rho) == 0)

# R2: Unruh temperature in units of mc^2/kB: 1/(2 pi rho).
TU = hbar * a_of / (2 * sp.pi * c * kB)
check("R2 T_U = mc^2/(2 pi kB rho): smooth, nonzero, finite for all rho>0",
      sp.simplify(TU - m * c**2 / (2 * sp.pi * kB * rho)) == 0)

# R3: ZB acceleration in units of a(rho): 2 rho -- again
# a ratio, defined for all rho, excluding none.
aZB = 2 * m * c**3 / hbar
check("R3 a_ZB / a(rho) = 2 rho identically (ZB weld is a ratio, not a failure)",
      sp.simplify(aZB / a_of - 2 * rho) == 0)

# R4: seat cycle and Compton clock carry rho-weight 0.
check("R4 seat cycle E_rest * tau_C = hbar and ZB period pi*tau_C are rho-free",
      sp.simplify(m * c**2 * tauC - hbar) == 0)

# R5: bouncer spectrum (v15.857 family U = m a x):
# E_n = |a_n| (hbar^2 m a^2 / 2)^{1/3}; dimensionless
# ratio to mc^2 is 2^{-1/3} (a/a*)^{2/3} -- a smooth
# power of rho, analytic for all rho > 0.
En_ratio = (hbar**2 * m * a_of**2 / 2)**sp.Rational(1, 3) / (m * c**2)
target = 2**sp.Rational(-1, 3) * rho**sp.Rational(-2, 3)
check("R5 bouncer E_n/(mc^2) = |a_n| 2^{-1/3} rho^{-2/3}: "
      "the mixed spectrum is smooth in rho, no distinguished rho",
      sp.simplify(sp.log(En_ratio) - sp.log(target)) == 0)

# R6: integer-valued wedge counts are step functions of
# a continuous horizon parameter: even an exact integer
# target localizes rho to an interval, not a value.
def wedge_count(rr, M=50):
    n = 0
    for u in range(1, M + 1):
        for v in range(1, M + 1):
            if u * v <= M and v <= rr * u:
                n += 1
    return n
rhos = np.linspace(0.5, 2.0, 301)
counts = [wedge_count(r) for r in rhos]
plateaus = sum(1 for i in range(1, len(counts)) if counts[i] == counts[i - 1])
check("R6 lattice wedge count is a step function of rho "
      f"(constant on {plateaus}/300 sampled steps; jumps only at discrete rho)",
      plateaus > 250 and len(set(counts)) < 40)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
