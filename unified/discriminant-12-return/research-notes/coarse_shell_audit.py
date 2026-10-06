#!/usr/bin/env python3
"""Sandbox audit of v14.076 coarse 16k->32k shell budget.

1. Independently recompute the conditional interval (verify v14.076 s2 arithmetic).
2. Compute max admissible theta_e^{32k} for which the shell stays strictly negative.
3. Document the transport obstruction (Outcome B).
"""
from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal

RCAP = D("1e-7")
THETA_E_OLD = D("3.899270146651301e-6")
THETA_O_OLD = D("9.69258681013552e-11")

C16_E = D("7.499901498486917e-30")
C32_E = D("7.485609640013522e-30")
C16_O = D("2.1622076013239955e-25")
C32_O = D("2.158138843073839e-25")

def neglog1m(x):
    s = D(0); p = x
    for k in range(1, 40):
        s += p / D(k); p *= x
    return s

def shell_interval(theta_e, theta_o):
    """Return (mid, W, lo, hi) for the coarse 16k->32k shell."""
    eta_e = C16_E / C32_E - D(1)
    eta_o = C16_O / C32_O - D(1)
    mid = eta_o - eta_e
    def R_eta(eta, theta):
        Lsrc = D(2) * neglog1m(theta)
        Lsolve = D(2) * neglog1m(RCAP)
        L = Lsrc + Lsolve
        return (D(1) + eta) * (L + L * L)  # expm1_up
    W = R_eta(eta_e, theta_e) + R_eta(eta_o, theta_o)
    return mid, W, mid - W, mid + W

print("=== 1. Recompute v14.076 s2 conditional interval ===")
mid, W, lo, hi = shell_interval(THETA_E_OLD, THETA_O_OLD)
print(f"mid = {mid:.6e}")
print(f"W   = {W:.6e}")
print(f"interval = [{lo:.6e}, {hi:.6e}]")
print(f"v14.076 cites: [-3.21500419317947e-5, -1.57211176651012e-5]")
print(f"upper < 0: {hi < 0}")
assert hi < 0

print()
print("=== 2. Max admissible theta_e for strict negativity ===")
# Binary search on theta_e (theta_o fixed at old value; its contribution is negligible).
lo_t, hi_t = D("1e-9"), D("1e-3")
for _ in range(200):
    t = (lo_t + hi_t) / 2
    _, _, _, h = shell_interval(t, THETA_O_OLD)
    if h < 0:
        lo_t = t
    else:
        hi_t = t
print(f"max theta_e = {lo_t:.6e}")
print(f"old theta_e = {THETA_E_OLD:.6e}")
print(f"headroom factor = {lo_t / THETA_E_OLD:.2f}x")
# Sanity: at max theta_e, upper endpoint should be ~0.
_, _, _, h = shell_interval(lo_t, THETA_O_OLD)
print(f"upper endpoint at max theta_e: {h:.3e} (should be ~0)")

print()
print("=== 3. Sensitivity: what if theta_e must grow? ===")
for te in [D("3.9e-6"), D("1e-5"), D("2e-5"), D("5e-5")]:
    m, w, l, h = shell_interval(te, THETA_O_OLD)
    print(f"theta_e={te:.1e}: interval=[{l:.3e},{h:.3e}], negative={h < 0}")
