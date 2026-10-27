"""Numeric scan: mode exponents m (pi ~ t^m solves pi'' + (3/t) pi' + Q pi = 0,
m^2 + 2m + Q t^2 = 0) and kinetic signs, scalar and vector, across k^2."""
import numpy as np

def Qs(k2): return k2 * (9 * k2 + 4) / (3 * k2 - 4)          # x t^2
def Qv(k2): return 9 * k2**2 / (3 * k2 - 4)                  # x t^2
def A_s(k2): return (3 * k2 - 4) / (3 * k2 - 1)              # sign of scalar kin. coeff
def A_v(k2): return (3 * k2 - 4)                             # sign of vector kin. coeff
def mplus(Qt2):
    d = 1 - Qt2
    return -1 + np.sqrt(d) if d >= 0 else None               # None -> oscillatory pair
print(f"{'k^2':>7} {'kphys/H':>8} | {'A_s':>6} {'Qs t2':>9} {'m+_s':>7} | {'A_v':>6} {'Qv t2':>9} {'m+_v':>7}")
for k2 in [0.01, 0.1, 0.25, 1/3, 0.5, 0.75, 1.0, 1.2, 4/3, 1.5, 2.0, 4.0, 10.0]:
    row = f"{k2:7.3f} {np.sqrt(3*k2):8.3f} | "
    for A, Q in [(A_s, Qs), (A_v, Qv)]:
        if abs(k2 - 1/3) < 1e-9 and A is A_s:
            row += "  EXCPT      ---     --- | " if A is A_s else ""
            continue
        if abs(k2 - 4/3) < 1e-9:
            row += "   0.0      inf     inf | " if A is A_s else "   0.0      inf     inf"
            continue
        mp = mplus(Q(k2))
        row += f"{np.sign(A(k2)):+6.0f} {Q(k2):+9.3f} {('%7.3f' % mp) if mp is not None else '   osc.'} | "
    print(row)
