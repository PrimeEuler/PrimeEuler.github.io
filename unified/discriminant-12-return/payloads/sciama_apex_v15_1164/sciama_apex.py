#!/usr/bin/env python3
"""
sciama_apex.py -- final item of Jeremy's 2026-11-18
tasking (sandbox): Sciama's apex at 0. The apex ledger
(v15.230 sec.2; Jeremy's apex-pair identification
2026-11-02, ledgered as addendum to v15.279): seat -1/2
[derived, local: the counter/column parabola vertex],
cosmic balance +1/2 [measured: B = GM_H/(R_H c^2) =
Omega/2 = 0.4996 +- 0.0009, H0-immune], apex 0 = their
sum, with no dynamics performing it. This entry
re-verifies the local geometry, evaluates the cosmic
half inside the framework's own cosmology (K4), and
prices the remaining identification.

Gates:
A1. Apex-pair geometry (canonical mesh profiles):
    row n: Y^2 = n^2 - 2nX (vertex +n/2, focus 0);
    column k: Y^2 = k^2 + 2kX (vertex -k/2, focus 0).
    Crossing offset (n-k)/2, vertex midpoint (n-k)/4,
    profile-curvature sum 1/k - 1/n: all three vanish
    together iff n = k. At n = k = 1: crossing (0,1)
    (the seat state), vertices +-1/2, curvatures -+1.
A2. Cosmic half in a flat FLRW inventory: B = Omega/2
    identically, H cancelling; at Omega = 1 (the K4
    ansatz's flatness), B = 1/2 at all times.
A3. Row selection by measurement: filed B = 0.4996
    +- 0.0009 sits 0.45 sigma from n = 1's 1/2, and
    ~556 sigma from n = 2 (B = 1) and n = 0 (B = 0):
    conditional on the identification, the row is
    uniquely selected -- by measurement.
"""
import sympy as sp

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: fails.append(name)

X, Y = sp.symbols("X Y", real=True)
n, k = sp.symbols("n k", positive=True)

# A1: general pair
row = n**2 - 2 * n * X        # Y^2
col = k**2 + 2 * k * X
Xc = sp.solve(sp.Eq(row, col), X)[0]
check("A1a crossing offset X_c = (n-k)/2", sp.simplify(Xc - (n - k) / 2) == 0)
mid = (n / 2 + (-k / 2)) / 2
check("A1b vertex midpoint = (n-k)/4", sp.simplify(mid - (n - k) / 4) == 0)
Xrow = (n**2 - Y**2) / (2 * n)
Xcol = (Y**2 - k**2) / (2 * k)
curv_sum = sp.simplify(sp.diff(Xrow, Y, 2) + sp.diff(Xcol, Y, 2))
check("A1c curvature sum = 1/k - 1/n (vanishes iff n = k)",
      sp.simplify(curv_sum - (1 / k - 1 / n)) == 0)
# n = k = 1 specifics
Y2_at_cross = sp.simplify(row.subs({n: 1, X: 0}))
check("A1d at n=k=1: crossing (0,1) is the seat state, vertices +-1/2, "
      "curvatures -1/+1 cancel",
      Y2_at_cross == 1
      and sp.diff(Xrow.subs(n, 1), Y, 2) == -1
      and sp.diff(Xcol.subs(k, 1), Y, 2) == 1)

# A2: B in flat FLRW
G, H, c, Om = sp.symbols("G H c Omega", positive=True)
rho_c = Om * 3 * H**2 / (8 * sp.pi * G)
RH = c / H
MH = sp.Rational(4, 3) * sp.pi * rho_c * RH**3
B = sp.simplify(G * MH / (RH * c**2))
check("A2a B = Omega/2 identically, H cancelling (H0-immunity in miniature)",
      sp.simplify(B - Om / 2) == 0)
check("A2b at Omega = 1 (K4 flatness): B = 1/2 exactly",
      sp.simplify(B.subs(Om, 1) - sp.Rational(1, 2)) == 0)

# A3: measurement margins
B_meas, sig = 0.4996, 0.0009
z1 = abs(B_meas - 0.5) / sig
z2 = abs(1.0 - B_meas) / sig
z0 = abs(B_meas - 0.0) / sig
print(f"   z(n=1) = {z1:.2f}, z(n=2) = {z2:.0f}, z(n=0) = {z0:.0f}")
check("A3 row n=1 within 0.5 sigma; n=0 and n=2 excluded at >500 sigma",
      z1 < 0.5 and z2 > 500 and z0 > 500)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
