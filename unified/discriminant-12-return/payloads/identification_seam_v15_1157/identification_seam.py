#!/usr/bin/env python3
"""
identification_seam.py -- item 2 of the 2026-11-18 tasking
(sandbox). The seam (2026-10-28 assessment): pair-side hbar-Z
charges exist -- dressed L = cosh(s) p_s (v14.988), spinor
Noether charge q_chi = -rho sdot (v14.990) -- but their
identification with the K4 radial flux (v14.944) is
conjectural. Standard fixed in advance (2026-10-28): derived
from the structure at weld standard (v14.904/v14.914: integer
counts, no fitted joint), NOT kappaC=1-style matching.

Filed inputs used:
- Hessian pair metric (v14.952, quoted in v14.990's note):
  dl^2 = 2 drho^2 - 2 rho^2 ds^2; its s-shift charge Q_s has
  CONTINUOUS spectrum (v14.990 note).
- Spinor charge (v14.990, machine-verified there):
  q_chi = -rho * sdot, hbar-Z.
- Spinor dictionary (v14.990): tanh s = cos 2th,
  sech s = sin 2th, dth/ds = -1/(2 cosh s); at fixed rho the
  th-flow is -2 cosh(s) times the phi~-flow of v14.988, whose
  momentum is the dressed L.
- Radial flux (v14.944 [D]): conservation gives
  Jhat = Phi(tau)/(4 pi R^2) with Phi NOT fixed by
  conservation; point-source normalization N external;
  flags: independent_factor_Noether_charge=NOT_DERIVED,
  amplitude arbitrary.

Gates:
A. The two pair-side hbar-Z-adjacent charges are DIFFERENT
   functionals: p_s from the Hessian kinetic term is
   -2 rho^2 sdot, so q_chi / p_s = 1/(2 rho) -- state-
   dependent. No constant multiple identifies both with one
   flux.
B. The two U(1) momenta (v14.988's dressed L side and
   v14.990's q_chi side) are related through the square
   root by the flow factor -2 cosh(s): state-dependent,
   reducing to a constant only at the seat s = 0.
C. Static counterexample: at sdot = 0 both pair charges
   vanish, while v14.944's flux Phi != 0 is admissible --
   so no functional identity charge = flux exists.
D. The action that generates the radial/K4 side is the
   Hessian action, whose charge is the CONTINUOUS Q_s;
   the hbar-Z charges live on pair-mechanical actions with
   no radial sector, no sphere, no flux. The identification
   must cross actions -- the metric-selection choice
   v14.990 files as unforced ("Nothing yet forces the
   choice") -- plus fix the flux amplitude v14.944 files
   as free. Two unforced joints; weld standard allows zero.

Verdict: BROKEN at weld standard. Survives only as a
postulated dictionary line (Phi := q_chi, or Phi := L) of
kappaC=1 type -- the form the 2026-10-28 standard excluded
in advance. Reopening condition: a coupled action that
dynamically selects the pair kinetic metric.
"""
import sympy as sp

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: fails.append(name)

rho, s = sp.symbols("rho s", positive=True)
sdot, rhodot = sp.symbols("sdot rhodot", real=True)

# A. Hessian canonical momentum vs spinor charge
L_H = sp.Rational(1, 2) * (2 * rhodot**2 - 2 * rho**2 * sdot**2)
p_s = sp.diff(L_H, sdot)
check("A1 Hessian p_s = -2 rho^2 sdot", sp.simplify(p_s + 2 * rho**2 * sdot) == 0)
q_chi = -rho * sdot
ratio = sp.simplify(q_chi / p_s)
check("A2 q_chi / p_s = 1/(2 rho), state-dependent (d/drho != 0)",
      sp.simplify(ratio - 1 / (2 * rho)) == 0
      and sp.simplify(sp.diff(ratio, rho)) != 0)

# B. square-root flow factor
th = sp.acos(sp.tanh(s)) / 2
dth = sp.simplify(sp.diff(th, s))
check("B1 dth/ds = -1/(2 cosh s) from tanh s = cos 2th",
      sp.simplify(dth + 1 / (2 * sp.cosh(s))) == 0)
flow = -2 * sp.cosh(s)  # filed: th-flow is -2 cosh(s) x phi~-flow
check("B2 momentum ratio through the square root carries cosh(s): "
      "state-dependent (d/ds != 0), constant only at the seat s = 0",
      sp.simplify(sp.diff(flow, s)) != 0
      and sp.simplify(flow.subs(s, 0)) == -2)

# C. static counterexample values
check("C1 at sdot = 0: q_chi = 0 and p_s = 0 (flux Phi != 0 stays "
      "admissible per v14.944 -- no functional identity)",
      q_chi.subs(sdot, 0) == 0 and p_s.subs(sdot, 0) == 0)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
