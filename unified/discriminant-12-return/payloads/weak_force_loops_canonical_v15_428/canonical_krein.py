"""
Loop program, step 5 (2026-11-04 evening, sandbox): the CANONICAL
operator. Applies steps 1-4's protocol to finite sections of Lane
A's frozen K_full kernel (DERIVATION.md sec. 0, dm490/far585/kfull):

  K_{N,m} = c*(m*z_N - N*z_m)/(N^2 - m^2) + 2*sigma*p_N*p_m  (N != m)
  K_{N,N} = d_N + 2*sigma*p_N^2,      c = 2/pi, t = 1/pi^2,
  d_N = log(N/4) + D_osc(N),  B := off-diagonal part (B_NN = 0 --
  the ledger's own split, tail_norm_probe.py), D := diag(K).

Float stack copied verbatim from the ledger's own scoping payload
(v15.310): z_float (certified-weight model of the remote z
sequence), p_float = L*n/(n^2+t) (float model of the floored p_n),
d_float (SEED_FORMULA displayed diagonal model, census.py).
STATUS: probe-grade [N], exactly the v15.310 SPEC's standing --
scales, not certified values; do not quote tighter than ~0.05.
Finite sections only: NO full-K transfer claim (the ledger has
FULL_K_TRANSFER INCONCLUSIVE; the Schur route is the certificate
path). The certified diagonal evaluator applies only for
n > R = 256000, so head-section diagonals are float-model only;
remote diagonals are spot-validated against it below.
"""
import sys
from fractions import Fraction as F
from math import e as EULER, log, pi, sqrt

import numpy as np
from scipy.linalg import eigvalsh

sys.path.insert(0, "/home/hatch/workspace/d12/laneA_modules")
import suzuki_certified_remote_diagonal as DG

# ------------------------------------------------------------ float stack
W_Q = {q: (log(2) / 2 if q == 4 else log(q) / sqrt(q)) for q in (2, 3, 4, 5, 7)}
TH_Q = {q: pi * log(q) / 2 for q in (2, 3, 4, 5, 7)}
S0 = (1 / EULER) / (1 - np.exp(-4))
C_KERNEL = 2.0 / pi
T_PK = 1.0 / pi**2
C_ENV = 1.745855454249828

def z_float(n, sigma):
    n = np.asarray(n, dtype=np.float64)
    tot = np.full(n.shape, pi / 2) + (1 - 4 * sigma * S0) / (n * pi)
    for q in (2, 3, 4, 5, 7):
        tot = tot + 2 * W_Q[q] * np.sin(n * TH_Q[q])
    return tot

def p_float(n, L):
    n = np.asarray(n, dtype=np.float64)
    return L * n / (n * n + T_PK)

def d_float(n):
    n = np.asarray(n, dtype=np.float64)
    tot = np.log(n / 4.0) - 1.0 / (2.0 * n) \
        + 2.0 * ((-1.0) ** n) / (n * pi) ** 2
    for q in (2, 3, 4, 5, 7):
        coef = W_Q[q] * (2.0 - log(q))
        tot = tot - coef * (np.cos(n * TH_Q[q])
                            + (2.0 / (n * pi)) * np.sin(n * TH_Q[q]))
    return tot

def build_B(rows, cols, sigma, L):
    r = np.asarray(rows, dtype=np.float64)
    c_ = np.asarray(cols, dtype=np.float64)
    zr = z_float(r, sigma); zc = z_float(c_, sigma)
    pr = p_float(r, L); pc = p_float(c_, L)
    N = r[:, None]; M = c_[None, :]
    den = (N - M) * (N + M)
    with np.errstate(divide="ignore", invalid="ignore"):
        B = C_KERNEL * (M * zr[:, None] - N * zc[None, :]) / den
    B = B + 2.0 * sigma * pr[:, None] * pc[None, :]
    if len(rows) == len(cols) and np.array_equal(np.asarray(rows), np.asarray(cols)):
        np.fill_diagonal(B, 0.0)
    return B

SECTORS = {
    "odd":  dict(sigma=+1, L=1.4357379705709206, b=512001, parity=1),
    "even": dict(sigma=-1, L=0.6634791495304894, b=512002, parity=0),
}

def section(sec, regime, S):
    if regime == "head":
        start = 1 if sec["parity"] == 1 else 2
        modes = start + 2 * np.arange(S, dtype=np.int64)
    else:
        modes = sec["b"] + 2 * np.arange(S, dtype=np.int64)
    a = d_float(modes) + 2.0 * sec["sigma"] * p_float(modes, sec["L"]) ** 2
    B = build_B(modes, modes, sec["sigma"], sec["L"])
    return modes, a, np.diag(a) + B, B

def bk_xi(ev0, ev1, z):
    """Tr[R_1 - R_0] via interval integration of xi; also xi profile."""
    f = lambda lam: 1.0 / (lam - z)
    pts = np.sort(np.concatenate([ev0, ev1]))
    tot = 0.0; ximax = 0
    for lo, hi in zip(pts[:-1], pts[1:]):
        mid = 0.5 * (lo + hi)
        xi = int(np.sum(ev0 <= mid) - np.sum(ev1 <= mid))
        ximax = max(ximax, abs(xi))
        tot += xi * (f(hi) - f(lo))
    lhs = np.sum(1.0 / (ev1 - z)) - np.sum(1.0 / (ev0 - z))
    return lhs, tot, ximax

print("=" * 76)
print("VALIDATION of the float stack")
print("=" * 76)
for name, sec in SECTORS.items():
    # certified spot-checks on remote modes (evaluator needs n > 256000)
    rng = np.random.default_rng(20261104)
    js = np.sort(rng.choice(np.arange(0, 20000), size=24, replace=False))
    modes = sec["b"] + 2 * js
    devs = []
    for n in modes:
        r = DG.evaluate(int(n))
        mid = float((F(r["lower_rational"]) + F(r["upper_rational"])) / 2)
        devs.append(abs(float(d_float(np.array([float(n)]))[0]) - mid))
    print(f"  [{name}] certified diagonal spot-check (24 remote modes): "
          f"max |d_float - certified mid| = {max(devs):.2e}")
# C_ENV census + head z per sector
ZHEAD = {}
for name, sec in SECTORS.items():
    worst = 0.0; amin = np.inf
    start = 1 if sec["parity"] == 1 else 2
    for lo in range(0, 2_000_000, 200_000):
        n = start + 2 * np.arange(lo, min(lo + 200_000, 2_000_000), dtype=np.int64)
        if len(n) == 0: continue
        d = d_float(n)
        worst = max(worst, float(np.max(np.abs(d - np.log(n / 4.0)))))
        a = d + 2.0 * sec["sigma"] * p_float(n, sec["L"]) ** 2
        amin = min(amin, float(np.min(a)))
    ZHEAD[name] = amin - 3.0
    print(f"  [{name}] census n<=4e6: max |d_float - log(n/4)| = {worst:.4f} "
          f"(certified bound for true d_n: {C_ENV}); min diag a_n = {amin:.4f}, "
          f"z_head = {ZHEAD[name]:.4f}")

print()
print("=" * 76)
print("KREIN PROTOCOL ON CANONICAL SECTIONS (per sector, per regime)")
print("=" * 76)
for name, sec in SECTORS.items():
    for regime, z in (("head", None), ("remote", 7.0)):
        zz = ZHEAD[name] if z is None else z
        for S in (200, 400, 800):
            modes, a, K, B = section(sec, regime, S)
            evK = eigvalsh(K)
            evD = np.sort(a)
            nB = float(max(abs(eigvalsh(B, subset_by_index=[0, 0])[0]),
                           abs(eigvalsh(B, subset_by_index=[S - 1, S - 1])[0])))
            weyl = float(np.max(np.abs(evK - evD)))
            HS2 = float(np.sum(B ** 2 / (a - zz)[None, :] ** 2))
            M = (K - zz * np.eye(S)) / (a - zz)[None, :]
            sgn, logdet = np.linalg.slogdet(M)
            line = (f"  [{name}/{regime}] S={S:>4}: ||B||={nB:.3f} Weyl={weyl:.3f} "
                    f"||B R_D||_HS^2={HS2:9.3f} logdet={logdet:+.4f} (sign {sgn:+.0f})")
            if S == 400:
                lhs, tot, ximax = bk_xi(evD, evK, zz)
                line += (f"\n      BK: Tr={lhs:+.8f} int f'xi={tot:+.8f} "
                         f"agree={abs(lhs - tot) < 1e-7}; max|xi|={ximax}")
                # xi at fixed lambda (section-stability probe)
                lam_fix = float(np.median(a))
                xi_fix = int(np.sum(evD <= lam_fix) - np.sum(evK <= lam_fix))
                line += f"; xi(median diag)={xi_fix}"
            print(line, flush=True)

print()
print("=" * 76)
print("CANONICAL INSERTION: the pole vertex 2*sigma*p x p (S=800)")
print("=" * 76)
for name, sec in SECTORS.items():
    for regime, z in (("head", None), ("remote", 7.0)):
        zz = ZHEAD[name] if z is None else z
        modes, a, K, B = section(sec, regime, 800)
        p = p_float(modes, sec["L"])
        x = np.linalg.solve(K - zz * np.eye(800), p)
        insK = 2.0 * sec["sigma"] * float(p @ x)
        insD = 2.0 * sec["sigma"] * float(np.sum(p ** 2 / (a - zz)))
        print(f"  [{name}/{regime}] 2s*<p,R_K p> = {insK:+.6f};  "
              f"2s*<p,R_D p> = {insD:+.6f};  difference {insK - insD:+.6f}")

print()
print("SCOPE: probe-grade float model (v15.310 SPEC standing, ~+/-0.05);")
print("finite sections only; no full-K transfer; B is the ledger's")
print("hollow off-diagonal part, so Tr(B R_D) = 0 on every section and")
print("the raw perturbation determinant IS its det_2 form here.")
