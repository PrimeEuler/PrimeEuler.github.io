"""
The metres-per-second tag (2026-11-13, sandbox; short
addendum to the leverage split v15.859, at Jeremy's
direction: "those accel/decell parabolas have a meters
per second tag").

Each parabola belongs to one null ray, so each carries
its ray's velocity as a tag: the accel parabola the
+c ray's, the decel parabola the -c ray's. In SI the
arms are u = E + p c and v = E - p c -- the state's
energy-momentum read along the +c ray and the -c ray.
With E = gamma m c^2 and p = gamma m vel:

  u = gamma m c (c + vel),   v = gamma m c (c - vel),

so the v15.859 leverage reads (1 + beta)/(1 - beta) =
(c + vel)/(c - vel): the state's metres per second
measured against each parabola's own m/s tag. The
force's action shares are (c + vel)/(2c) through the
+c-tagged parabola and (c - vel)/(2c) through the
-c-tagged one (from du/dt = F(vel + c), dv/dt =
F(vel - c)). Null limit: vel -> c sends the decel
share to zero -- the lever's extreme is the null
channel of v15.858, where the state and the tag
coincide. All forms symbolic; the 1 MeV electron
rechecks the v15.859 number 13.24 : 1.
"""
import sympy as sp

m, c, vel, F = sp.symbols("m c vel F", positive=True)
gamma = 1 / sp.sqrt(1 - vel**2 / c**2)
E = gamma * m * c**2
p = gamma * m * vel
u = sp.simplify(E + p * c)
v = sp.simplify(E - p * c)
print(f"u = E + pc = {u}  [= gamma m c (c + vel): "
      f"{sp.simplify(u - gamma * m * c * (c + vel)) == 0}]")
print(f"v = E - pc = {v}  [= gamma m c (c - vel): "
      f"{sp.simplify(v - gamma * m * c * (c - vel)) == 0}]")
lev = sp.simplify(u / v)
print(f"leverage u/v = {lev}; (c+vel)/(c-vel): "
      f"{sp.simplify(lev - (c + vel) / (c - vel)) == 0}")
du = F * (vel + c)          # dE/dt = F vel, d(pc)/dt = c F
dv = F * (vel - c)
share_u = sp.simplify(du / (du - dv)); share_v = sp.simplify(-dv / (du - dv))
print(f"du/dt = F(vel + c), dv/dt = F(vel - c); shares: "
      f"{share_u} and {share_v} -- i.e. (c+vel)/(2c) and (c-vel)/(2c): "
      f"{sp.simplify(share_u - (c + vel) / (2 * c)) == 0 and sp.simplify(share_v - (c - vel) / (2 * c)) == 0}")
print(f"null limit vel -> c: decel share -> {sp.limit(share_v, vel, c, dir='-')}, "
      f"accel share -> {sp.limit(share_u, vel, c, dir='-')} (the v15.858 channel)")
import numpy as np
beta_e = float(np.tanh(1.2917))
print(f"electron at 1 MeV (psi = 1.2917, beta = {beta_e:.4f}): leverage = "
      f"{(1 + beta_e) / (1 - beta_e):.4f} : 1 (v15.859's 13.2421), "
      f"shares {(1 + beta_e) / 2:.4f} / {(1 - beta_e) / 2:.4f}")
