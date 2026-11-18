#!/usr/bin/env python3
"""
p2_w2_packages.py -- P2 test (sandbox, 2026-11-18). P2 (v14.910):
the W2 contact cutoff is 4n in any independent gravity-side
seat-Casimir derivation (package: cutoff 4n, normalization 64,
anomaly -12 n^2 ln n).

Method: (i) reproduce the filed package in exact arithmetic
(W2 from v14.910's own closed form; shell(12) = 113 is
v14.858's value); (ii) compute the ALTERNATIVE package -- if the
seat Casimir sum were built on the dyon product grid (q = 1/4)
instead of the state grid (h = 1/2), the cutoff multiplier
would be c = 16, normalization 16^3 = 4096, and the anomaly
log-coefficient would be -(c^2 (c-1))/4 = -960, cleanly
distinguishable from -12; (iii) identify what forces c = 4:
the seat Casimir counts STATES, states live on the h-grid
(h = 2q, node = state), 2D density 1/h^2 = 4. The forcing
chain runs through the weld premise itself.

General coefficient (from W2(N) = C3 N^3 + (1/4) N^2 ln N +
O(N^2)): Delta_c(n) = W2(cn) - c^3 W2(n) has n^2 ln n
coefficient (1/4)(c^2 - c^3) = -c^2 (c-1)/4.
"""
from fractions import Fraction as F
import mpmath as mp
import sympy as sp

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: fails.append(name)

def W2(N):
    tot = F(0)
    for a in range(1, N + 1):
        M = N // a
        s1 = M * a + M * (M + 1) // 2
        s2 = M * a * a + a * M * (M + 1) + M * (M + 1) * (2 * M + 1) // 6
        tot += F(s2 - 2 * s1, 4)
    return tot

def shell(n):
    tot = F(0)
    for a in range(1, n + 1):
        if n % a == 0:
            b = n // a
            j = F(a + b - 2, 2)
            tot += j * (j + 1)
    return tot

def F2M(fr):
    return mp.mpf(fr.numerator) / fr.denominator

check("A1 shell(12) = 113 exact (v14.858's value)", shell(12) == 113)

c = sp.symbols("c", positive=True)
coef = sp.expand((c**2 - c**3) / 4)
check("A2 anomaly log-coefficient -c^2(c-1)/4: c=4 -> -12 (filed package)",
      sp.simplify(coef.subs(c, 4)) == -12)
check("A3 same formula: c=16 -> -960 (dyon-grid alternative package)",
      sp.simplify(coef.subs(c, 16)) == -960)

for n in (4000, 16000):
    w_n = W2(n)
    d64 = F2M(W2(4 * n) - 64 * w_n) / (n**2 * mp.log(n))
    d16 = F2M(W2(16 * n) - 4096 * w_n) / (n**2 * mp.log(n))
    ratio = F2M(W2(4 * n)) / F2M(w_n)
    print(f"   n={n}: W2(4n)/W2(n) = {mp.nstr(ratio, 7)} (-> 64); "
          f"Delta_64/(n^2 ln n) = {mp.nstr(d64, 6)} (-> -12); "
          f"Delta_4096/(n^2 ln n) = {mp.nstr(d16, 6)} (-> -960)")
    if n == 16000:
        check("B1 filed package: ratio in (60, 64) and Delta_64 fit in (-13, -7)",
              60 < float(ratio) < 64 and -13 < float(d64) < -7)
        check("B2 alternative package cleanly separated: Delta_4096 fit < -400",
              float(d16) < -400)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
