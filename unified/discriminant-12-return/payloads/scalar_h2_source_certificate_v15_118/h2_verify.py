#!/usr/bin/env python3
"""Cross-checks for h2_substitution.py's on-shell <H2> quadratic form:
(1) exact small-k leading coefficients of A, B, C;
(2) numeric term-by-term reassembly at sample points, independent of the
    symbolic assembly path (dictionary re-applied numerically).
"""
import sympy as sp

t, k, pv, pdv = sp.symbols("t k pv pdv", positive=True)
A = -(3 * k**6 + 7 * k**4 + 15 * k**2 + 16) / (3 * k**2 * t**2 * (k**2 + 1) ** 2)
B = -2 * (2 * k**4 + 3 * k**2 - 4) / (3 * k**4 * t * (k**2 + 1) ** 2)
C = -(k**6 + k**4 + 2 * k**2 - 3) / (3 * k**4 * (k**2 + 1) ** 2)
print("k->0 leading terms:")
print("  A ~ (", sp.limit(A * k**2 * t**2, k, 0), ") / (k^2 t^2)")
print("  B ~ (", sp.limit(B * k**4 * t, k, 0), ") / (k^4 t)")
print("  C ~ (", sp.limit(C * k**4, k, 0), ") / k^4")
print("  A sign for k>0: numerator 3k^6+7k^4+15k^2+16 > 0, overall minus -> A < 0 for all k")
_x = sp.Symbol("x")
print("  C zero at k^2 =", sp.nsolve(_x**3 + _x**2 + 2 * _x - 3, 0.8), "(k^2 root), C > 0 below it, C < 0 above")

def closed(kv, tv, p, pd):
    Av = float(A.subs({k: kv, t: tv})); Bv = float(B.subs({k: kv, t: tv})); Cv = float(C.subs({k: kv, t: tv}))
    return Av * p**2 + Bv * p * pd + Cv * pd**2

def termwise(kv, tv, p, pd):
    import numpy as np
    a = tv / np.sqrt(3); H = 1 / tv
    psi = (-kv**2 * p + tv * pd) / (3 * kv**2 * (kv**2 + 1))
    psid = (-(kv**2 + 2) * pd - ((3 * kv**2 + 4) / tv) * p) / (3 * kv**2 * (kv**2 + 1))
    alpha = ((3 * kv**2 + 4) * p + tv * pd) / (3 * kv**2 * (kv**2 + 1))
    Bsol = 0.0; theta = 0.0
    h = 0.5
    H2 = (-10 / a**2 * (h * kv**2 * psi**2) + 6 * (h * psid**2)
          + 24 * H * (h * alpha * psid - h * psi * psid) + 18 * H**2 * (h * alpha**2)
          - 12 * H * (h * psi * theta) + 4 * (h * psid * theta) + 8 * H * (h * alpha * theta)
          - (2 / 3) * (h * (pd / kv + (kv / a) * Bsol) ** 2)
          - (2 / (3 * a**2)) * (h * p**2 + 2 * p * psi + 6 * psi**2))
    return H2

for kv, tv, p, pd in [(1.0, 2.0, 0.7, -0.2), (0.3, 1.5, 1.1, 0.4), (2.5, 3.0, -0.5, 0.9)]:
    c1, c2 = closed(kv, tv, p, pd), termwise(kv, tv, p, pd)
    print(f"  k={kv}, t={tv}: closed={c1:.12f} termwise={c2:.12f} diff={abs(c1-c2):.2e}")
    assert abs(c1 - c2) < 1e-9 * max(1.0, abs(c1))
print("H2 QUADRATIC FORM CROSS-CHECK PASSED")
