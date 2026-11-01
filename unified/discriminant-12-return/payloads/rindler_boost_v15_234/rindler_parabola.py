#!/usr/bin/env python3
"""
What is the Galilean acceleration parabola in the Rindler frame?

Inertial frame (c = 1 units, Rindler length L = c^2/g set to 1 by
scaling): the true uniformly-accelerated observer sits on the
hyperbola X^2 - t^2 = 1 with X = x + 1 (vertex at the observer).
Rindler coordinates of that observer's frame:
    X = rho cosh(eta),  t = rho sinh(eta)
    rho^2 = X^2 - t^2 (interval from the horizon centre), eta = rapidity.

The Galilean parabola of the SAME g: x = t^2/2, i.e. X = 1 + t^2/2
(scaled u = t, xi = x: xi = u^2/2 as in accel_parabola.py).
"""
import numpy as np
import sympy as sp

t = sp.symbols('t', real=True)
X = 1 + t**2 / 2
rho2 = sp.expand(X**2 - t**2)
print("rho^2 = X^2 - t^2 =", rho2, " -- the t^2 terms CANCEL exactly:")
print("  rho^2 = 1 + (t^2/2)^2 = 1 + xi^2, xi = the parabola's own x.")
print("  (The cancellation IS the parabola-hyperbola tangency of v15.233.)")

def eta_rho(u):
    xi = u**2 / 2
    Xv = 1 + xi
    rho = np.sqrt(Xv**2 - u**2)
    eta = np.arctanh(u / Xv)
    return xi, rho, eta

print("\nparametric table (u = gt/c, xi = gx/c^2, rho in units of c^2/g):")
print(f"{'u':>7} {'xi':>8} {'rho':>9} {'eta':>9}")
for u in [0.0, 0.5, 1.0, np.sqrt(2), 2.0, 3.0, 5.0, 10.0]:
    xi, rho, eta = eta_rho(u)
    tag = "  <- eta MAX (the sigma=1 grazing point)" if abs(u - np.sqrt(2)) < 1e-9 else (
          "  <- inertial edge crossing (u=2)" if u == 2.0 else "")
    print(f"{u:>7.3f} {xi:>8.3f} {rho:>9.4f} {eta:>9.4f}{tag}")
print(f"eta_max = artanh(1/sqrt(2)) = ln(1+sqrt(2)) = {np.log(1+np.sqrt(2)):.6f}, "
      f"at u = sqrt(2), rho = sqrt(2).")
print("After the fold, eta DECREASES back toward 0 while rho -> infinity:")
print("in Rindler time the parabola runs backward on its outer branch.")

print("\nfamily scan: parabola of acceleration a in the Rindler frame of g")
print("(X = 1 + (a/g) u^2/2 in scaled units; horizon exit iff X = u has roots)")
for ag in [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 4.0]:
    # eta(u) = artanh(u / (1 + (ag/2) u^2)); formal fold at u^2 = 2/ag.
    uf = np.sqrt(2 / ag)
    dip = "rho dips first (a<g)" if ag < 1 else ("rho flat to 4th order (a=g)"
                                                 if ag == 1 else "rho grows at once (a>g)")
    if ag < 0.5:
        # horizon exit where 1 + (ag/2) u^2 = u, before the formal fold
        ue = (1 - np.sqrt(1 - 2 * ag)) / ag
        print(f"  a/g = {ag:>4}: EXITS the wedge at u = {ue:.3f} (eta -> inf at the"
              f" horizon) before the formal fold u = {uf:.3f}; {dip}")
    elif ag == 0.5:
        print(f"  a/g = {ag:>4}: fold exactly ON the horizon at u = {uf:.3f}"
              f" (eta_max = inf); {dip}")
    else:
        etamax = np.arctanh(uf / (1 + (ag / 2) * uf**2))
        print(f"  a/g = {ag:>4}: fold inside the wedge at u = {uf:.3f}, "
              f"eta_max = {etamax:.4f}; {dip}; stays in wedge")
print("\nReading: in its own Rindler frame the parabola is a curve that")
print("departs the observer monotonically in rho but folds in Rindler")
print("time at eta_max = ln(1+sqrt(2)) -- the fold point is exactly the")
print("sigma=1 grazing crossing of v15.233 seen from the accelerated frame.")
