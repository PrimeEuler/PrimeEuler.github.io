"""Numeric check of claim D: fixed exponential V (kappa = 1, mu = sqrt(2), V0 = 2,
tracker r = sqrt(2) ln tau, a = tau/sqrt(3)), charged initial data Q = 1 and Q = 50,
modulus perturbed off-tracker. Integrate (a from Friedmann, r from its e.o.m.,
theta' = Q/(a^3 r^2)); report approach to coasting and charge decoupling."""
import numpy as np
from scipy.integrate import solve_ivp

mu = np.sqrt(2.0); V0 = 2.0
V = lambda r: V0 * np.exp(-mu * r)
Vp = lambda r: -mu * V(r)

def run(Q, dr0, t1=3000.0):
    t0 = 10.0
    a0 = t0 / np.sqrt(3.0); r0 = np.sqrt(2.0) * np.log(t0) + dr0; p0 = np.sqrt(2.0) / t0
    def rhs(t, y):
        a, r, p = y
        th = Q / (a**3 * r**2)
        rho = 0.5 * (p**2 + r**2 * th**2) + V(r)
        H = np.sqrt(rho / 3.0)
        return [a * H, p, -3 * H * p + r * th**2 - Vp(r)]
    sol = solve_ivp(rhs, [t0, t1], [a0, r0, p0], rtol=1e-10, atol=1e-12, dense_output=True)
    print(f"--- Q = {Q}, dr0 = {dr0} ---")
    print(f"{'tau':>7} {'rho tau^2':>9} {'H tau':>7} {'w':>8} {'q_chi':>10} {'charge E frac':>13} {'thetadot':>10}   (targets: 3, 1, -1/3)")
    for t in [10, 30, 100, 300, 1000, 3000]:
        a, r, p = sol.sol(t)
        th = Q / (a**3 * r**2)
        K = 0.5 * (p**2 + r**2 * th**2); rho = K + V(r); w = (K - V(r)) / rho
        print(f"{t:>7} {rho * t**2:>9.4f} {t * np.sqrt(rho / 3):>7.4f} {w:>8.4f} {Q / a**3:>10.2e} {0.5 * r**2 * th**2 / rho:>13.2e} {th:>10.2e}")

run(0.0, 0.0)   # control on-tracker: must sit at rho tau^2 = 3, w = -1/3 exactly
run(1.0, 0.3)   # charged, modulus perturbed off-tracker
run(50.0, 0.3)  # strongly charged (10% initial energy footprint): watch it die ~ a^-4 relative
