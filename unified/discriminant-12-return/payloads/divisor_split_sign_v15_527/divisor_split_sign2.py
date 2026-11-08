"""
Divisor-split sign test, Part 2 (2026-11-07, sandbox).
Jeremy's additions, mid-run: (i) the Klein-4 mod-12 units
comb {1,5,7,11}; (ii) the binary D(n) function.

(i) Residue split of the row excess e(k) by k mod 12; the
unit-restricted summatory D_U(n) = sum_{k<=n, (k,12)=1} d(k)
and its fluctuation Delta_U against its own main term.
Main term from the Dirichlet series
  sum_{(k,12)=1} d(k) k^-s = zeta(s)^2 (1-2^-s)^2 (1-3^-s)^2:
double-pole residue at s=1 gives
  Main_U(n) = (1/9) n log n + (1/9)(2 gamma - 1 + 2 log 2
              + log 3) n .
Seat bias split by the seat's own class: Delta(m^2) for
unit m ((m,12)=1, so m^2 = 1 mod 12 -- the comb's seats)
vs non-unit m.

(ii) The binary readout: b(k) = d(k) mod 2 is the square
indicator (Part 1 verified odd <=> square to 2e6), so its
summatory B(n) = #{k<=n : d(k) odd} = floor(sqrt(n))
EXACTLY -- the binary channel of the coloring is the seat
counter, with no fluctuation beyond the sawtooth.

(iii) Mechanism check for Part 1's headline (Delta(m^2)
positive at 99.9% of squares, normalized mean +2.19): the
Voronoi expansion writes Delta(x) as a sum of modes
~ d(k) k^-3/4 cos(4 pi sqrt(kx) - pi/4) (the circle-side
modes of the divisor problem). At x = m^2 the square modes
k = j^2 have phase 4 pi m j - pi/4 = -pi/4 (mod 2 pi) for
EVERY j -- they phase-lock, all pulling the same way,
while non-square modes stay spread. Evaluated truncated
(K modes) at sampled square and non-square x, with the
overall sign calibrated once against Delta itself, this
tests whether the lock reproduces the observed bias; the
square modes' coherent contribution in normalized units
is S/(2 pi), S = sum_j d(j^2) j^-3/2.
"""
import numpy as np
from math import log, pi, sqrt

rng = np.random.default_rng(20261107)
N = 2_000_000
GAMMA = 0.5772156649015329

try:
    d = np.load("d_cache.npy")
    assert len(d) == N + 1
except Exception:
    d = np.zeros(N + 1, dtype=np.int32)
    for k in range(1, N + 1):
        d[k::k] += 1
    np.save("d_cache.npy", d)
D = np.cumsum(d, dtype=np.int64)
n_arr = np.arange(N + 1, dtype=np.float64)
M = np.where(n_arr > 0, n_arr * np.log(np.maximum(n_arr, 1)) + (2 * GAMMA - 1) * n_arr, 0.0)
Delta = D - M

# ---- (ii) binary summatory = seat counter, exact
B = np.cumsum((d % 2).astype(np.int64))
tests = [10, 100, 1000, 12345, 999999, N]
ok = all(int(B[t]) == int(sqrt(t)) for t in tests)
print(f"(ii) binary summatory B(n) = floor(sqrt(n)) at n = {tests}: {ok}")
print(f"     B(N) = {int(B[N])} seats at or below N = {N} (sqrt(N) = {sqrt(N):.2f})")

# ---- (i) residue split of the row excess
e = d[2:].astype(np.float64) - (np.log(n_arr[2:]) + 2 * GAMMA)
res = (np.arange(2, N + 1) % 12)
UNITS = {1, 5, 7, 11}
print("\n(i) row excess e(k) by k mod 12 (U = Klein-4 unit class):")
for r in range(12):
    sel = res == r
    print(f"    k = {r:2d} mod 12 {'U' if r in UNITS else ' '}: mean e = {e[sel].mean():+.4f} "
          f"(n = {sel.sum()})")

# unit-restricted summatory and its fluctuation
unit_mask = np.zeros(N + 1, dtype=bool)
for r in UNITS:
    unit_mask[r::12] = True
unit_mask[0] = False
DU = np.cumsum(np.where(unit_mask, d, 0), dtype=np.int64)
MainU = np.where(n_arr > 0,
                 (n_arr * np.log(np.maximum(n_arr, 1))) / 9
                 + (2 * GAMMA - 1 + 2 * log(2) + log(3)) * n_arr / 9, 0.0)
DeltaU = DU - MainU
signU = np.sign(DeltaU)
crossU = np.nonzero(signU[1:] * signU[:-1] < 0)[0] + 1
print(f"\n    unit-restricted fluctuation: {len(crossU)} crossings to {N}; "
      f"fraction of shells Delta_U > 0: {(DeltaU[1:] > 0).mean():.4f}")

# seat bias split by the seat's class
m_vals = np.arange(2, int(N ** 0.5) + 1)
sq_shells = m_vals ** 2
norm = Delta[sq_shells] / sq_shells ** 0.25
unit_m = np.array([int(np.gcd(m, 12)) == 1 for m in m_vals])
print(f"\n    Delta(m^2) normalized, unit m (m^2 = 1 mod 12, the comb's seats): "
      f"mean {norm[unit_m].mean():+.4f}, fraction positive {(norm[unit_m] > 0).mean():.3f} "
      f"(n = {unit_m.sum()})")
print(f"    Delta(m^2) normalized, non-unit m: "
      f"mean {norm[~unit_m].mean():+.4f}, fraction positive {(norm[~unit_m] > 0).mean():.3f} "
      f"(n = {(~unit_m).sum()})")
normU = DeltaU[sq_shells] / sq_shells ** 0.25
print(f"    Delta_U at all square shells: mean {normU.mean():+.4f}, "
      f"fraction positive {(normU > 0).mean():.3f}")

# ---- (iii) Voronoi phase-lock check
K = 20000
kk = np.arange(1, K + 1, dtype=np.float64)
dk = d[1:K + 1].astype(np.float64)
coef = dk * kk ** (-0.75)
def voronoi(x, sgn):
    return sgn * (x ** 0.25 / (pi * sqrt(2))) * float(
        np.sum(coef * np.cos(4 * pi * np.sqrt(kk * x) - pi / 4)))
sample_sq = (rng.integers(200, int(N ** 0.5), size=60)) ** 2
sample_ns = rng.integers(40000, N, size=60)
for sgn in (+1, -1):
    vs = np.array([voronoi(int(x), sgn) for x in sample_sq])
    vn = np.array([voronoi(int(x), sgn) for x in sample_ns])
    ds = Delta[sample_sq] / sample_sq ** 0.25
    dn = Delta[sample_ns] / sample_ns ** 0.25
    print(f"\n(iii) truncated Voronoi (K={K}), overall sign {sgn:+d}: "
          f"corr with Delta/x^(1/4) at squares {np.corrcoef(vs / sample_sq ** 0.25, ds)[0, 1]:+.3f}, "
          f"at non-squares {np.corrcoef(vn / sample_ns ** 0.25, dn)[0, 1]:+.3f}")
# S via factorization of j (d(j^2) = prod (2a+1)); sieve only reaches sqrt(N)
J = 20000
spf = np.arange(J + 1)
for p in range(2, int(J ** 0.5) + 1):
    if spf[p] == p:
        spf[p * p::p] = np.minimum(spf[p * p::p], p)
def d_of_square(j):
    out, x = 1, j
    while x > 1:
        p = int(spf[x]); a = 0
        while x % p == 0:
            x //= p; a += 1
        out *= (2 * a + 1)
    return out
dj2 = np.array([d_of_square(j) for j in range(1, J + 1)], dtype=np.float64)
jj = np.arange(1, J + 1, dtype=np.float64)
S = float(np.sum(dj2 * jj ** (-1.5)))
print(f"     square-mode sum S = sum_j d(j^2) j^-3/2 (j<={J}) = {S:.3f}; "
      f"coherent normalized contribution S/(2 pi) = {S / (2 * pi):.3f} "
      f"(Part 1 measured Delta(m^2) normalized mean +2.1911)")
# square modes only, at sampled squares vs non-squares (normalized)
def voronoi_sq(x):
    return (x ** 0.25 / (pi * sqrt(2))) * float(
        np.sum(dj2 * jj ** (-1.5) * np.cos(4 * pi * jj * sqrt(x) - pi / 4)))
vsq_sq = np.array([voronoi_sq(int(x)) / int(x) ** 0.25 for x in sample_sq])
vsq_ns = np.array([voronoi_sq(int(x)) / int(x) ** 0.25 for x in sample_ns])
print(f"     square-modes-only contribution, normalized: at squares mean "
      f"{vsq_sq.mean():+.3f} (should equal S/(2 pi) exactly); at non-squares "
      f"mean {vsq_ns.mean():+.3f}, mean abs {np.abs(vsq_ns).mean():.3f}")

# ---- Q4 firmed up: max-only vs min-only seat extremality, bigger control
def extremum_frac(centers, halfwidths):
    mx = mn = 0
    for c, h in zip(centers, halfwidths):
        seg = Delta[c - h:c + h + 1]
        mx += bool(Delta[c] == seg.max())
        mn += bool(Delta[c] == seg.min())
    return mx / len(centers), mn / len(centers)
fmx, fmn = extremum_frac(sq_shells, m_vals)
rand_c = rng.integers(1000, N - 3000, size=5000)
rmx, rmn = extremum_frac(rand_c, np.sqrt(rand_c).astype(int))
print(f"\nQ4 firmed: Delta(m^2) is window MAX {fmx:.3f} / window MIN {fmn:.3f} "
      f"({len(sq_shells)} squares); random control MAX {rmx:.4f} / MIN {rmn:.4f} (5000 shells)")
