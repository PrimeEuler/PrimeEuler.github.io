"""
Divisor-split addendum, checks (2026-11-07, sandbox).
(1) Higher-precision kernel-shell means (the first kernel
run printed s=10 and s=30 with the same 4-decimal mean --
verify). (2) Offset controls for s >= 2 (the first run's
control crashed on an index cap at s*m^2 = N exactly).
(3) The prediction P_s with S_s extended by factorization
to j <= 20000, as in Part 2 for s = 1: if the extended
mode sums close the gap to the measured means, the lock
accounts for the kernel biases too; if not, a second
component (local elevation around divisor-rich shells)
is present and sized here.
"""
import numpy as np
from math import pi

N = 2_000_000
GAMMA = 0.5772156649015329
d = np.zeros(N + 1, dtype=np.int32)
for k in range(1, N + 1):
    d[k::k] += 1
D = np.cumsum(d, dtype=np.int64)
n_arr = np.arange(N + 1, dtype=np.float64)
M = np.where(n_arr > 0, n_arr * np.log(np.maximum(n_arr, 1)) + (2 * GAMMA - 1) * n_arr, 0.0)
Delta = D - M

def kernel_stats(s, offset=0):
    mmax = int(((N - 1 - offset) // s) ** 0.5)
    ms = np.arange(2, mmax + 1)
    shells = s * ms ** 2 + offset
    vals = Delta[shells] / shells ** 0.25
    return vals.mean(), (vals > 0).mean(), len(shells)

print("(1)+(2) kernel means at 6 decimals, with +1 offsets:")
for s in (1, 2, 3, 5, 6, 7, 10, 30):
    m0, f0, c0 = kernel_stats(s, 0)
    m1, f1, _ = kernel_stats(s, 1)
    print(f"  s={s:2d}: mean {m0:+.6f} (frac {f0:.3f}, n={c0}); "
          f"offset+1 mean {m1:+.6f} (frac {f1:.3f})")

# (3) extended S_s by factorization
J = 20000
spf = np.arange(J + 1)
for p in range(2, int(J ** 0.5) + 1):
    if spf[p] == p:
        spf[p * p::p] = np.minimum(spf[p * p::p], p)
def factorize(x):
    out = {}
    while x > 1:
        p = int(spf[x]); a = 0
        while x % p == 0:
            x //= p; a += 1
        out[p] = a
    return out
jfac = [factorize(j) for j in range(1, J + 1)]
print("\n(3) extended coherent sums (j <= 20000 by factorization):")
for s in (1, 2, 3, 5, 6, 7, 10, 30):
    sf = factorize(s)
    tot = 0.0
    for j in range(1, J + 1):
        exps = dict(sf)
        for p, b in jfac[j - 1].items():
            exps[p] = exps.get(p, 0) + 2 * b
        dv = 1
        for a in exps.values():
            dv *= (a + 1)
        tot += dv * j ** (-1.5)
    P = (s ** (-0.75)) * tot / (2 * pi)
    print(f"  s={s:2d}: S_s = {tot:.3f}, P_s(extended) = {P:+.4f}")
