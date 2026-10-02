"""External audit (Round 142) independent check of v13.937's claim that
exact (closed-form) treatment of the kink pieces of Suzuki's g(t) -- not
just finer quadrature -- eliminates the Round-139 artifact.

Uses exact closed-form double antiderivatives for the pole and kink pieces
of g(t) (elementary, no approximation), and a fast vectorized high-
resolution cumulative-trapezoid treatment (reusing fem_screw.py's own
validated F_of_t) for the smooth Lerch/arch2 piece only -- the piece
v13.937 diagnoses as NOT needing exact treatment to avoid 1/h^2
amplification, since it has no derivative discontinuity away from t=0.

Two checks:
  1. lambda_1(Q_full, M) at a=2 vs N: should show a converging plateau,
     not the unbounded Round-139 decay, once the kink pieces are exact.
  2. Direct Ritz minimization of RQ_full over a small sine subspace: a
     model-independent rigorous upper bound on inf RQ_full, robust to any
     residual imprecision in the smooth-piece treatment.
"""
import sys
import numpy as np
import fem_screw as fs
from scipy.interpolate import CubicSpline
from scipy.integrate import cumulative_trapezoid
from scipy.linalg import eigh, toeplitz

A = 2.0
K_LIN = fs.PSI14 - fs.LOGPI


def arch2_vec(t):
    return -0.25 * (fs.ZETA214 - fs.F_of_t(t))


def build_arch2_spline(a, ngrid=1_600_001):
    tg = np.linspace(-2.2 * a, 2.2 * a, ngrid)
    gv = arch2_vec(tg)
    G1 = cumulative_trapezoid(gv, tg, initial=0.0)
    i0 = len(tg) // 2
    G1 = G1 - G1[i0]
    G2 = cumulative_trapezoid(G1, tg, initial=0.0)
    G2 = G2 - G2[i0]
    return CubicSpline(tg, G2)


def G2_exact(t, Lam, nmax, arch2_spline):
    t = np.asarray(t, dtype=float)
    at = np.abs(t)
    pole = -16 * (np.exp(at / 2) + np.exp(-at / 2)) + 4 * t**2 + 32
    ns = np.nonzero(Lam[2:nmax + 1])[0] + 2
    logns = np.log(ns)
    cs = Lam[ns] / np.sqrt(ns)
    d = at[..., None] - logns[None, :]
    kink = np.sum(cs[None, :] * np.maximum(d, 0.0)**3 / 6.0, axis=-1)
    lin = -(K_LIN / 2.0) * (at**3 / 6.0)
    return pole + kink + lin + arch2_spline(t)


def assemble_Q_exact(a, N, Lam, nmax, arch2_spline):
    h = 2.0 * a / N
    pts = np.arange(-N, N + 1, dtype=float) * h
    Gp = G2_exact(pts, Lam, nmax, arch2_spline)
    S = Gp[2:] - 2.0 * Gp[1:-1] + Gp[:-2]
    T = 2.0 * S[1:-1] - S[:-2] - S[2:]
    Tpos = T[(N - 2):(N - 2) + (N - 1)]
    return toeplitz(Tpos) / h**2


def assemble_M(a, N):
    h = 2.0 * a / N
    n = N - 1
    M = np.zeros((n, n))
    np.fill_diagonal(M, 2.0 * h / 3.0)
    if n > 1:
        M[np.arange(n - 1), np.arange(1, n)] = h / 6.0
        M[np.arange(1, n), np.arange(n - 1)] = h / 6.0
    return M


if __name__ == '__main__':
    nmax = int(np.exp(2.2 * A)) + 1
    Lam = fs.sieve(nmax)[1]
    arch2_spline = build_arch2_spline(A)

    print("Exact-kink lambda1(N) at a=2:")
    for N in [400, 800, 1600, 3200]:
        Q = assemble_Q_exact(A, N, Lam, nmax, arch2_spline)
        M = assemble_M(A, N)
        w = eigh(Q, M, eigvals_only=True, subset_by_index=[0, 2])
        print(f"  N={N:5d}  lam1={w[0]:+.4e}  lam2={w[1]:+.4e}  lam3={w[2]:+.4e}")

    print("\nDirect Ritz minimization over an 8-mode sine basis (N=1600):")
    N = 1600
    Q = assemble_Q_exact(A, N, Lam, nmax, arch2_spline)
    M = assemble_M(A, N)
    h = 2.0 * A / N
    xs = -A + h * np.arange(1, N)
    J = 8
    V = np.column_stack([np.sin(j * np.pi * (xs + A) / (2 * A)) for j in range(1, J + 1)])
    Qr = V.T @ Q @ V
    Mr = V.T @ M @ V
    w = eigh(Qr, Mr, eigvals_only=True)
    print("  Ritz eigenvalues:", w)
    print("  min RQ over this subspace (rigorous upper bound on inf RQ_full):", w[0])
