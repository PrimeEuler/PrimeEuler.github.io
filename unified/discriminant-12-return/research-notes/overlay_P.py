#!/usr/bin/env python3
"""
Overlay P in the distribution class — sandbox run 2026-10-18 (LIttle Euler).
Continues runs/20260928-010240-spherical-archimedean-2 (archimedean_report_2
sec.3-4) and the PRODUCT_FORM_BRIEF (20260928-005525): brief step 2, exhibit
P with E.P = A12, E = Atilde >= 0, following the construction prescribed in
archimedean_report_2 sec.4 / STATUS: P as the measured 1/n tempered
distribution, conditional convergence studied directly.

Construction (D_exp dictionary, L = 12/11, x = L e^{-t}):
  T~(x) = a0/2 + sum_{n>=1} a_n cos(pi n x / L),
  a_n = (2/L) int_0^L T~(x) cos(pi n x/L) dx = 2 int_0^1 T(-log u) cos(pi n u) du.
Analytic split: a_n = -s/n + r_n, s = -C1/12, where the -s/n part resums in
closed form:  sum_{n>=1} (-s/n) cos(pi n x/L) = s * log(2 sin(pi x/(2L))).
Hence  P(x) = a0/2 + s*log(2 sin(pi x/(2L))) + sum_{n>=1} r_n cos(pi n x/L),
with r_n = O(n^{-3/2} log n) (absolutely summable -> the remainder is an
honest bounded helix overlay; the log kernel carries the distribution part).

Stages (checkpointed to results.json / grid.npz):
  0 constants + sanity vs STATUS (bump max, t0, T tail at t=30)
  1 h-grid (log-singularity subtracted) on Chebyshev-Lobatto points,
    Clenshaw-Curtis cosine coefficients a_n, n <= 512
  2 mpmath anchors for a_n (independent quadrature), n in {1,2,3,5,8,13,21}
  3 r_n tail fit: r_n ~ A n^{-3/2} + B (-1)^n (log n) n^{-3/2} + C n^{-5/2}
  4 reconstruction P_sum (kernel + r-sum + resummed tails) and the product
    verification |Atilde(t) P(x(t)) - A12(t)| on a t-grid; zero of P vs t0;
    constant check a0/2 + s log pi + R(0) vs zeta(2,1/4)/24
  5 raw partial sums: S_N(0) + s log N law; crossover at x ~ L/N
"""
import json, time
import numpy as np
import mpmath as mp

T_START = time.time()
OUT = {}
def log(*a):
    print(f"[{time.time()-T_START:7.1f}s]", *a, flush=True)

# ---------- Stage 0: constants (definitions verbatim from probe_arch2.py) ----------
mp.mp.dps = 40
A = mp.mpf(1) / 4
Z = mp.zeta(2, A)                                    # zeta(2,1/4)
C1 = mp.digamma(A) + mp.log(12 / mp.pi)              # psi(1/4)+log(12/pi)
L = mp.mpf(12) / 11
S = -C1 / 12                                         # s = 0.24060639745313878...
log(f"s = {mp.nstr(S, 20)}   (expect 0.24060639745313878)")
log(f"zeta(2,1/4) = {mp.nstr(Z, 20)}   C1 = {mp.nstr(C1, 20)}")

def A12(t):
    t = mp.mpf(t)
    return (t / 2) * C1 + mp.mpf('0.25') * (Z - mp.e ** (-t / 2) * mp.lerchphi(mp.e ** (-2 * t), 2, A))

def Atilde(t):
    t = mp.mpf(t)
    return 6 * mp.sqrt(1 - mp.e ** (-2 * t))

def Tfun(t):
    t = mp.mpf(t)
    if t == 0:
        return mp.mpf(0)
    if t > 25:  # exact tail (STATUS, verified 2.8e-26 at t=30 in run 2)
        return (C1 / 12) * t + Z / 24 - mp.mpf(2) / 3 * mp.e ** (-t / 2)
    return A12(t) / Atilde(t)

# sanity: zero crossing and bump vs STATUS values
lo, hi = mp.mpf('1.91'), mp.mpf('1.92')
for _ in range(80):
    mid = (lo + hi) / 2
    if A12(mid) > 0: lo = mid
    else: hi = mid
t0 = (lo + hi) / 2
log(f"t0 = {mp.nstr(t0, 18)}  (STATUS: 1.9120492808650985)")
grid = [t0 * i / 400 for i in range(1, 400)]
bump = max((A12(t), t) for t in grid)
log(f"bump max A12 = {mp.nstr(bump[0], 12)} at t = {mp.nstr(bump[1], 8)}  (STATUS: 0.4410123794637466 at 0.7514772294417866)")
tail30 = (C1 / 12) * 30 + Z / 24 - mp.mpf(2) / 3 * mp.e ** (-15)
log(f"T(30) direct = {mp.nstr(Tfun(30), 15)}   tail formula = {mp.nstr(tail30, 15)}")
OUT['stage0'] = {'s': str(S), 't0': str(t0), 'bump': str(bump[0]), 'bump_t': str(bump[1])}

# ---------- Stage 1: h-grid + Clenshaw-Curtis coefficients ----------
mp.mp.dps = 30
M = 8192
NMAX = 512
j = np.arange(M + 1)
u = 0.5 * (1 - np.cos(np.pi * j / M))               # Chebyshev-Lobatto on [0,1]
sf = float(S)
h = np.empty(M + 1)
h[0] = float(Z / 24)                                  # limit of T(-log u) - s log u at u=0
h[M] = 0.0                                            # endpoint u=1: T(0) - s*log(1) = 0
log("evaluating h-grid (8191 lerchphi evals, dps=30)...")
for jj in range(1, M):
    uu = mp.mpf(float(u[jj]))
    tt = -mp.log(uu)
    h[jj] = float(Tfun(tt) - S * mp.log(uu))
    if jj % 2048 == 0:
        log(f"  grid {jj}/{M}")
        np.savez('grid.npz', u=u, h=h)
np.savez('grid.npz', u=u, h=h)
# Clenshaw-Curtis weights on [0,1] (Trefethen's clencurt, mapped from [-1,1])
theta = np.pi * j / M
w = np.zeros(M + 1)
ii = np.arange(1, M)
v = np.ones(M - 1)
if M % 2 == 0:
    w[0] = w[M] = 1.0 / (M * M - 1 + (M % 2))
    for k in range(1, M // 2):
        v -= 2 * np.cos(2 * k * theta[ii]) / (4 * k * k - 1)
    v -= np.cos(M * theta[ii]) / (M * M - 1)
else:
    w[0] = w[M] = 1.0 / (M * M)
    for k in range(1, (M + 1) // 2):
        v -= 2 * np.cos(2 * k * theta[ii]) / (4 * k * k - 1)
w[1:M] = 2 * v / M
w *= 0.5                                              # map [-1,1] -> [0,1]
assert abs(w.sum() - 1.0) < 1e-12, w.sum()
# coefficients: a_n = 2 * [ int h cos(pi n u) du - s * Si(pi n)/(pi n) ], n>=1
n_arr = np.arange(1, NMAX + 1)
COS = np.cos(np.pi * np.outer(n_arr, u))              # (512, 8193)
int_h = (COS * (w * h)).sum(axis=1)
si = np.array([float(mp.si(mp.pi * n)) for n in n_arr])
a = 2 * (int_h - sf * si / (np.pi * n_arr))
a0half = float((w * h).sum() - sf)                    # int_0^1 g du = int h du - s
log(f"a0/2 = {a0half:.12f}")
log(f"a_1 = {a[0]:.10f}  (law: -s + r_1)   a_2 = {a[1]:.10f}   a_10 = {a[9]:.10f}  -s/10 = {-sf/10:.10f}")
np.savez('coeffs.npz', a=a, a0half=a0half)
OUT['stage1'] = {'a0half': a0half, 'a1': float(a[0]), 'a2': float(a[1]), 'a10': float(a[9])}
json.dump(OUT, open('results.json', 'w'), indent=1)
log("stage 1 done")

# ---------- Stage 2: mpmath anchors (independent quadrature, dps 40) ----------
mp.mp.dps = 40
anchors = {}
for n in [1, 2, 3, 5, 8, 13, 21]:
    val = 2 * mp.quad(lambda uu: Tfun(-mp.log(uu)) * mp.cos(mp.pi * n * uu),
                      [0, mp.mpf('0.5'), 1])
    anchors[n] = (float(val), float(a[n - 1]), abs(float(val) - float(a[n - 1])))
    log(f"anchor n={n}: quad={float(val):.12f}  grid={float(a[n-1]):.12f}  |diff|={anchors[n][2]:.2e}")
OUT['stage2'] = {str(k): v for k, v in anchors.items()}

# ---------- Stage 3: r_n tail fit ----------
r = a + sf / n_arr                                    # r_n = a_n + s/n
fit_lo = 48
nn = n_arr[fit_lo - 1:].astype(float)
yy = r[fit_lo - 1:] * nn ** 1.5
X = np.column_stack([np.ones_like(nn), ((-1) ** nn) * np.log(nn), 1.0 / nn])
coef, *_ = np.linalg.lstsq(X, yy, rcond=None)
Af, Bf, Cf = coef
resid = yy - X @ coef
log(f"tail fit on n in [48,512]: A={Af:.6f} (expect ~0.15), B={Bf:.6f}, C={Cf:.4f}, rms resid={resid.std():.2e}")
log(f"r_512 = {r[-1]:.3e};  sum|r_n| (n<=512) = {np.abs(r).sum():.4f}")
OUT['stage3'] = {'A': float(Af), 'B': float(Bf), 'C': float(Cf), 'fit_rms': float(resid.std())}

# ---------- Stage 4: reconstruction + product verification ----------
mp.mp.dps = 30
Lf = 12 / 11
_NT = np.arange(NMAX + 1, 3_000_001, dtype=float)
_NT_W = np.column_stack([_NT ** -1.5, np.log(_NT) * _NT ** -1.5, _NT ** -2.5])
def tail_resum(theta):
    """sum_{n>512} [A n^-3/2 + B (-1)^n log n n^-3/2 + C n^-5/2] cos(n theta),
    direct float summation of the fitted model tail (truncation < 3e-4)."""
    c1 = np.cos(_NT * theta)
    c2 = np.cos(_NT * (np.pi - theta))
    return float(Af * (_NT_W[:, 0] * c1).sum()
                 + Bf * (_NT_W[:, 1] * c2).sum()
                 + Cf * (_NT_W[:, 2] * c1).sum())

def P_sum(x):
    th = np.pi * x / Lf
    kern = sf * np.log(2 * np.sin(th / 2))
    rsum = float((r * np.cos(n_arr * th)).sum())
    return a0half + kern + rsum + tail_resum(th)

def R_of(x):
    th = np.pi * x / Lf
    return float((r * np.cos(n_arr * th)).sum()) + tail_resum(th)

# constant check at the centre: a0/2 + s log pi + R(0) ?= Z/24
R0 = R_of(0.0)
const_lhs = a0half + sf * np.log(np.pi) + R0
log(f"constant check: a0/2 + s*log(pi) + R(0) = {const_lhs:.10f}   Z/24 = {float(Z/24):.10f}   diff = {abs(const_lhs - float(Z/24)):.2e}")
OUT['stage4_const'] = {'lhs': const_lhs, 'Z24': float(Z / 24), 'R0': R0}

# product verification on a t-grid
ts = np.concatenate([np.logspace(np.log10(0.02), np.log10(30), 50),
                     np.linspace(0.3, 3.0, 28)])
ts = np.unique(np.round(ts, 10))
errs = []
for t in ts:
    x = Lf * np.exp(-t)
    pv = P_sum(x)
    exact = float(A12(mp.mpf(float(t))))
    got = float(Atilde(mp.mpf(float(t)))) * pv
    errs.append((float(t), got - exact, exact))
errs = np.array(errs)
imax = np.argmax(np.abs(errs[:, 1]))
log(f"product check on {len(ts)} t-points in [0.02, 30]: max |err| = {np.abs(errs[:,1]).max():.3e} at t={errs[imax,0]:.3f}; rms = {np.sqrt((errs[:,1]**2).mean()):.3e}")
big = np.abs(errs[:, 2]) > 1
log(f"  max rel err (|A12|>1): {(np.abs(errs[big,1]/errs[big,2])).max():.3e}")
OUT['stage4_product'] = {'max_abs_err': float(np.abs(errs[:, 1]).max()), 't_at_max': float(errs[imax, 0]),
                         'rms': float(np.sqrt((errs[:, 1] ** 2).mean())),
                         'max_rel_err_big': float((np.abs(errs[big, 1] / errs[big, 2])).max())}
np.savez('product_grid.npz', errs=errs)

# zero of the reconstruction vs t0
def P_of_t(t):
    return P_sum(Lf * np.exp(-t))
lo2, hi2 = 1.5, 2.5
assert P_of_t(lo2) > 0 and P_of_t(hi2) < 0
for _ in range(60):
    mid = 0.5 * (lo2 + hi2)
    if P_of_t(mid) > 0: lo2 = mid
    else: hi2 = mid
log(f"P zero at t = {0.5*(lo2+hi2):.12f}   exact t0 = {float(t0):.12f}   diff = {abs(0.5*(lo2+hi2)-float(t0)):.2e}")
OUT['stage4_zero'] = {'P_zero_t': 0.5 * (lo2 + hi2), 't0': float(t0)}

# ---------- Stage 5: raw partial sums (conditional convergence) ----------
def a_model(n):
    n = np.asarray(n, dtype=float)
    return -sf / n + Af * n ** -1.5 + Bf * ((-1) ** n) * np.log(n) * n ** -1.5 + Cf * n ** -2.5
law = {}
for N in [64, 256, 1024, 4096]:
    if N <= NMAX:
        ssum = a0half + float(a[:N].sum())
    else:
        ssum = a0half + float(a.sum()) + float(a_model(np.arange(NMAX + 1, N + 1)).sum())
    law[N] = ssum + sf * np.log(N)
    log(f"S_N(0) + s log N, N={N}: {law[N]:.8f}   (target a0/2 + R(0) - s*gamma = {a0half + R0 - sf*0.5772156649015329:.8f})")
OUT['stage5_sat'] = {str(k): v for k, v in law.items()}
# crossover: raw partial sum (computed a_n only) vs T~ at x = c*L/512
cross = {}
for c in [0.5, 1.0, 2.0, 4.0]:
    x = c * Lf / NMAX
    raw = a0half + float((a * np.cos(n_arr * np.pi * x / Lf)).sum())
    exact = float(Tfun(-mp.log(mp.mpf(x / Lf))))
    cross[c] = (raw, exact, abs(raw - exact))
    log(f"crossover c={c}: x={x:.5f} raw512={raw:.6f} exact T~={exact:.6f} |err|={abs(raw-exact):.4f}")
OUT['stage5_cross'] = {str(k): v for k, v in cross.items()}

json.dump(OUT, open('results.json', 'w'), indent=1)
log("ALL STAGES DONE")
