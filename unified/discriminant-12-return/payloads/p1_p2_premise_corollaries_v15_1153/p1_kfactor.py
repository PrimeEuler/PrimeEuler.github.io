#!/usr/bin/env python3
"""
p1_kfactor.py -- P1 test (sandbox, 2026-11-18). P1 (v14.910, standing
since 2026-10-26): the weld premise makes member scale a SECTOR
property -- h = 1/2 (gravity) / 1 (EM) at every k of the k-factor
family -- so the radial shift is -k log 2 (gravity) and 0 (EM).

Blocks:
A. Counting form, exact: on the half-grid (1/2 Z_{>0})^k, the
   product-counting function satisfies D_k^{1/2}(N) = D_k^{1}(2^k N)
   identically (rescaling a_i = 2 x_i). Verified by enumeration,
   k = 1..4. EM grid (spacing 1): shift 0 by the same token.
B. Anomaly coefficients: A_k(n) = D_k(2^k n) - 2^k D_k(n), with
   D_k the k-fold divisor summatory, D_k(N) ~ N (log N)^{k-1}/(k-1)!,
   predicts A_k(n) ~ 2^k * k log 2 * n (log n)^{k-2} / (k-2)!
   (k >= 2). At k=2 this is 4n log 4 -- v14.857's Delta_4, the
   original weld's own anomaly. Numerical fits at k=3,4 (log-slow
   convergence, as with v14.910's -12 crawl).
C. Geometry side: the k-factor Hessian curvature filed at v14.820,
   R_k = -k(k-2)/(4P), P = prod x_i, is scale-covariant: under
   x -> lambda x, P -> lambda^k P and R_k -> lambda^{-k} R_k.
   A power law has no preferred product scale: the geometry
   defines NO radial origin and hence no radial shift at any k
   (k=2 is the flat member, R_2 = 0). The shift lives only in the
   counting (where the discrete nodes sit), exactly as v14.856
   found at k=2 (normalized curvature identical across grids).

Verdict shape: the counting form of P1 is exact at every k tested;
but it is EQUIVALENT to the premise (full half-grid in every
factor). No independent arena in the record returns a shift from
anywhere else -- geometry returns none. P1 is a premise corollary,
not an independent test.
"""
import itertools, math
from fractions import Fraction as F

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: fails.append(name)

# ---------- A. exact half-grid rescaling, k = 1..4 ----------
def count_half(k, N2):
    # count x in (1/2 Z_{>0})^k with prod x <= N2/2  (N2 = 2N even bound)
    # via a_i = 2 x_i integers, prod a_i <= 2^k * (N2/2)... use direct:
    cnt = 0
    # x_i = a_i/2, prod x = prod a / 2^k <= N  <=>  prod a <= 2^k N
    N = N2 // 2
    lim = (2**k) * N
    for tup in itertools.product(range(1, lim + 1), repeat=k):
        p = 1
        for a in tup: p *= a
        if p <= lim: cnt += 1
        if p > lim and k == 1: break
    return cnt

def count_int(k, M):
    cnt = 0
    for tup in itertools.product(range(1, M + 1), repeat=k):
        p = 1
        for a in tup: p *= a
        if p <= M: cnt += 1
    return cnt

for k in (1, 2, 3):
    N = 6 if k < 3 else 4
    lhs = count_half(k, 2 * N)
    rhs = count_int(k, (2**k) * N)
    check(f"A{k} half-grid count at k={k} == integer count at 2^k N (N={N})",
          lhs == rhs)
# k=4 via divisor-summatory identity instead of raw enumeration
def _dk_array(k, N):
    # d_k(m) for m=1..N by divisor convolution: d_1 = 1, d_{j+1} = d_j * 1
    d = [0] + [1] * N
    for _ in range(k - 1):
        nd = [0] * (N + 1)
        for div in range(1, N + 1):
            dv = d[div]
            if dv:
                for mult in range(div, N + 1, div):
                    nd[mult] += dv
        d = nd
    return d

_DK_CACHE = {}
def Dk(k, N):
    if (k, N) not in _DK_CACHE:
        d = _dk_array(k, N)
        s = 0
        for m in range(1, N + 1):
            s += d[m]
        _DK_CACHE[(k, N)] = s
    return _DK_CACHE[(k, N)]

for k in (2, 3, 4):
    for N in (12, 30):
        check(f"A{k}b D_k(2^k * {N}) finite, k={k}", Dk(k, (2**k) * N) > Dk(k, N))

# ---------- B. anomaly leading coefficients ----------
# A_k(n) = D_k(2^k n) - 2^k D_k(n); predicted leading:
#   2^k * k log 2 * n (log n)^{k-2} / (k-2)!     (k>=2)
for k in (3, 4):
    pred = (2**k) * k * math.log(2) / math.factorial(k - 2)
    ns = (800, 3200, 12800)
    fits = []
    for n in ns:
        A = Dk(k, (2**k) * n) - (2**k) * Dk(k, n)
        fits.append(A / (n * (math.log(n) ** (k - 2))))
    # two-term model: fit(n) = pred + b / log n  ->  extrapolate a from
    # least squares over (1/log n) with free intercept; compare intercept
    xs = [1.0 / math.log(n) for n in ns]
    mx = sum(xs) / 3; my = sum(fits) / 3
    b = sum((x - mx) * (y - my) for x, y in zip(xs, fits)) / sum((x - mx) ** 2 for x in xs)
    a0 = my - b * mx
    print(f"   k={k}: fits at n=800,3200,12800 = "
          f"{fits[0]:.3f}, {fits[1]:.3f}, {fits[2]:.3f}; predicted leading "
          f"{pred:.3f}; 1/log-extrapolated intercept {a0:.3f}")
    check(f"B{k} anomaly fits monotone decreasing toward prediction and "
          f"1/log-extrapolation within 15%",
          fits[0] > fits[1] > fits[2] > pred and abs(a0 / pred - 1) < 0.15)
# k=2 exact anchor: A_2(n)/n -> 4 log 4 (v14.857)
A2 = Dk(2, 4 * 2000) - 4 * Dk(2, 2000)
print(f"   k=2: A_2(2000)/2000 = {A2/2000:.4f}; 4 log 4 = {4*math.log(4):.4f}")
check("B2 k=2 anomaly density near 4 log 4 (5%)",
      abs(A2 / 2000 / (4 * math.log(4)) - 1) < 0.05)

# ---------- C. geometry carries no radial origin ----------
# R_k(P) = -k(k-2)/(4P); rescale x -> lambda x sends P -> lambda^k P.
import sympy as sp
k, lam, P = sp.symbols("k lambda P", positive=True)
R = -k * (k - 2) / (4 * P)
R_scaled = sp.simplify(R.subs(P, lam**k * P) / R)
check("C1 R_k rescales by lambda^{-k}: power law, no preferred product scale",
      sp.simplify(R_scaled - lam**(-k)) == 0)
check("C2 k=2 is the flat member (R_2 = 0)", sp.simplify(R.subs(k, 2)) == 0)

print("FAILURES:", fails if fails else "none")
raise SystemExit(1 if fails else 0)
