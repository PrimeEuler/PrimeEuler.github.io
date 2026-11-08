"""
The divisor-split sign test (2026-11-07, sandbox; Jeremy's
go-ahead, his sketch the same evening).

Jeremy's construction (his, 2016-era; sessions 2026-10-01/
02/08/13): the cone base at level n is the triangular array
T(n) = n(n+1)/2; D(n) = sum_{k<=n} d(k) marks the divisor-
hit positions (lattice points under xy <= n); A(n) =
T(n) - D(n) the misses; row recursion A(n+1) = A(n) +
(n+1) - d(n+1). Divisors pair around the seat at sqrt(n);
d(n) is odd iff n is a perfect square (the self-paired
divisor at sqrt(n) is the unpaired/DC mode); prime rows are
hollow (hits only at the two edges).

His proposal: the divisor count rides above and below its
average across boundaries (the parabola/circle crossings
of the mesh), and in the Suzuki screw picture -- circles
unwrapped to helix turns, stations at u_n = log n -- that
above/below split could embed a SELECTION. This test asks
the scoped question: do the fluctuation's crossings carry
cone geometry?

  Delta(n) = D(n) - M(n),  M(n) = n log n + (2 gamma - 1) n
  (the standard smooth trend of the Dirichlet summatory).

Known backdrop, stated in advance: Delta is provably
two-sided (Omega+-results; swings >= ~x^{1/4} both ways),
so the bare split cannot select. The test is therefore
about the crossings' ADDRESSES:
  Q1 census: how many sign crossings, what gap structure
     (in n and in the station coordinate t = log n)?
  Q2 seat proximity: are crossing shells closer to square
     shells (seat events) than chance (permutation null)?
  Q3 seat bias: is Delta at square shells, or the row
     excess e(k) = d(k) - (log k + 2 gamma) at square rows,
     systematically signed vs matched non-seat controls?
  Q4 seat extremality: is Delta(m^2) a local extremum in
     its seat window [m^2 - m, m^2 + m] more often than
     chance?
A seat-locked crossing pattern would give the coloring's
asymmetry a geometric address; a generic one files the
split as Dirichlet fluctuation in cone clothing.
"""
import numpy as np

rng = np.random.default_rng(20261107)
N = 2_000_000
GAMMA = 0.5772156649015329

# ---- divisor counts by sieve, summatory, fluctuation
d = np.zeros(N + 1, dtype=np.int32)
for k in range(1, N + 1):
    d[k::k] += 1
D = np.cumsum(d, dtype=np.int64)
n_arr = np.arange(N + 1, dtype=np.float64)
M = np.where(n_arr > 0, n_arr * np.log(np.maximum(n_arr, 1)) + (2 * GAMMA - 1) * n_arr, 0.0)
Delta = D - M

# Jeremy's partition check (record: A(300) = 43383)
T300 = 300 * 301 // 2
A300 = T300 - int(D[300])
print(f"partition check: A(300) = {A300} (record 43383): {A300 == 43383}")
# d(n) odd iff n square (record, checked n<2000 there; here to N)
sq_mask = np.zeros(N + 1, dtype=bool)
sq_mask[np.arange(1, int(N ** 0.5) + 1) ** 2] = True
odd = (d % 2) == 1
print(f"d(n) odd <=> n square, all n <= {N}: {bool(np.array_equal(odd[1:], sq_mask[1:]))}")

# ---- Q1: crossing census
sign = np.sign(Delta)
cross = np.nonzero(sign[1:] * sign[:-1] < 0)[0] + 1   # Delta changes sign at shell n
print(f"\nQ1 crossings: {len(cross)} sign changes of Delta for n <= {N}")
print(f"  first 20 crossing shells: {cross[:20].tolist()}")
gaps = np.diff(cross)
print(f"  gap in n: mean {gaps.mean():.1f}, median {np.median(gaps):.0f}, max {gaps.max()}")
per_decade = [int(((cross >= 10 ** e) & (cross < 10 ** (e + 1))).sum()) for e in range(1, 7)]
print(f"  crossings per decade [10^e, 10^(e+1)) e=1..6: {per_decade}")
t_cross = np.log(cross)
t_gaps = np.diff(t_cross)
print(f"  gap in t = log n: mean {t_gaps.mean():.4f}, median {np.median(t_gaps):.4f}")
print(f"  fraction of shells with Delta > 0: {(Delta[1:] > 0).mean():.4f}")

# ---- Q2: seat proximity of crossings (permutation null)
squares = np.arange(1, int(N ** 0.5) + 1) ** 2
def mean_dist_to_square(vals):
    idx = np.searchsorted(squares, vals)
    dl = np.where(idx > 0, vals - squares[np.clip(idx - 1, 0, len(squares) - 1)], np.inf)
    dr = np.where(idx < len(squares), squares[np.clip(idx, 0, len(squares) - 1)] - vals, np.inf)
    return np.minimum(dl, dr).mean()
obs = mean_dist_to_square(cross)
null = np.array([mean_dist_to_square(rng.integers(2, N, size=len(cross)))
                 for _ in range(2000)])
pct = (null <= obs).mean()
print(f"\nQ2 seat proximity: mean distance crossing->nearest square = {obs:.2f}")
print(f"  permutation null (2000 draws, same count): mean {null.mean():.2f} "
      f"+/- {null.std():.2f}; crossings at percentile {100 * pct:.1f} "
      f"({'closer to seats' if pct < 0.05 else 'not distinguishable from chance'})")
med = np.median(np.minimum(np.abs(cross[:, None] - squares[None, :]), axis=1)) \
    if len(cross) < 3000 else np.nan
print(f"  median distance: {med:.0f} (typical shell-to-square distance scale ~ sqrt(n)/2)")

# ---- Q3: seat bias of Delta and of the row excess
m_vals = np.arange(2, int(N ** 0.5) + 1)
sq_shells = m_vals ** 2
scale = sq_shells ** 0.25
d_sq = Delta[sq_shells] / scale
print(f"\nQ3 Delta at square shells (normalized by n^(1/4)): mean {d_sq.mean():+.4f}, "
      f"fraction positive {(d_sq > 0).mean():.3f}  ({len(sq_shells)} squares)")
for r in (-3, -2, -1, 1, 2, 3):
    nb = sq_shells + r
    d_nb = Delta[nb] / (nb ** 0.25)
    print(f"    offset {r:+d}: mean {d_nb.mean():+.4f}, fraction positive {(d_nb > 0).mean():.3f}")
e = d[2:].astype(np.float64) - (np.log(n_arr[2:]) + 2 * GAMMA)
sq_rows = sq_mask[2:]
print(f"  row excess e(k) = d(k) - (log k + 2 gamma): square rows mean {e[sq_rows].mean():+.4f} "
      f"(n={sq_rows.sum()}); non-square rows mean {e[~sq_rows].mean():+.4f}")
# primes (hollow rows) for contrast
is_p = np.ones(N + 1, dtype=bool)
is_p[:2] = False
for p in range(2, int(N ** 0.5) + 1):
    if is_p[p]:
        is_p[p * p::p] = False
e_p = d[2:][is_p[2:]] - (np.log(n_arr[2:][is_p[2:]]) + 2 * GAMMA)
print(f"  prime rows: mean e {e_p.mean():+.4f} (n={len(e_p)}; d(p) = 2 by construction, "
      f"so e(p) = 2 - log p - 2 gamma < 0 -- hollow rows ride below trend)")

# ---- Q4: seat extremality in the seat window
def frac_local_extremum(centers, halfwidths):
    hit = 0
    for c, h in zip(centers, halfwidths):
        seg = Delta[c - h:c + h + 1]
        hit += bool(Delta[c] == seg.max() or Delta[c] == seg.min())
    return hit / len(centers)
f_sq = frac_local_extremum(sq_shells, m_vals)
rand_c = rng.integers(1000, N - 2000, size=800)
f_rand = frac_local_extremum(rand_c, np.sqrt(rand_c).astype(int))
print(f"\nQ4 Delta(m^2) is a local extremum in [m^2-m, m^2+m]: fraction {f_sq:.3f} "
      f"({len(sq_shells)} squares)")
print(f"  random-shell control (same window rule): fraction {f_rand:.3f} (800 shells)")

print("""
Reading (assembled in the note): the split's crossings and
the seat events are compared on addresses, bias, and
extremality -- not on the existence of the fluctuation,
which is classical and two-sided.""")
