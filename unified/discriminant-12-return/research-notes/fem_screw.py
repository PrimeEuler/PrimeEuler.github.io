"""
Full-A_a P1 FEM for Suzuki's Weil-form operator (Kim et al. 2607.24830 recipe).

Q_ij = Q_W^a(phi_i, phi_j) = ∫∫_{(-a,a)^2} g(x-y) phi_i'(x) phi_j'(y) dx dy
M_ij = ∫ phi_i phi_j   (standard P1 mass, Dirichlet H^1_0)
Solve generalized eigenproblem Q v = lambda M v for the lowest eigenvalue.

Assembly trick: phi_i' is piecewise constant, so each Q_ij is a sum of
rectangle integrals R(A,B) = ∫_A∫_B g(x-y) dx dy. With G2'' = g,
  R([a1,a2],[b1,b2]) = G2(a2-b1) - G2(a1-b1) - G2(a2-b2) + G2(a1-b2).
On a uniform mesh R_{pq} depends only on p-q -> Q is symmetric Toeplitz.
G2 is built once per (a, weight-variant) by cumulative trapezoid on a fine
grid + cubic spline (G2 is C^2 since g is C^0 with kinks in g').

g(t): Suzuki (1.3), 2606.09096 v3 — Lerch bracketing
  -1/4 ( Phi(1,2,1/4) - e^{-|t|/2} Phi(e^{-2|t|},2,1/4) )
confirmed by our v13.894 resolution and Suzuki v3.
F(t) = e^{-|t|/2} Phi(e^{-2|t|},2,1/4): power series (|t|<1, coeffs via mpmath),
direct Lerch series (|t|>=1).
"""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.linalg import toeplitz
from scipy.sparse.linalg import eigsh
from scipy.integrate import cumulative_trapezoid
import mpmath

mpmath.mp.dps = 30

# ---- high-precision constants ----
GAMMA  = float(mpmath.euler)
PSI14  = float(mpmath.digamma(mpmath.mpf('0.25')))   # -4.2274535333762655
PSI2   = float(mpmath.digamma(2))                    #  0.42278433509846713
ZETA214 = float(mpmath.hurwitz(2, mpmath.mpf('0.25')))  # 17.19732915450711
LOGPI  = float(mpmath.log(mpmath.pi))
A_SUZ  = 0.5*(float(mpmath.log(2*mpmath.pi)) - PSI2)  # 0.707546...

# power-series coeffs for F(t), |t|<1: c_n = zeta(2-n,1/4)/n!, n=2..41
_FC = [float(mpmath.hurwitz(2 - n, mpmath.mpf('0.25')) / mpmath.fac(n))
       for n in range(2, 42)]


def F_of_t(t):
    """F(t) = e^{-|t|/2} Phi(e^{-2|t|}, 2, 1/4), even. Vectorized."""
    t = np.abs(np.asarray(t, dtype=float))
    out = np.empty_like(t)
    m0 = (t == 0.0)
    out[m0] = ZETA214
    m1 = (~m0) & (t < 1.0)
    m2 = (~m0) & (t >= 1.0)
    if np.any(m1):
        tt = t[m1]
        s = ZETA214 + 2.0 * tt * (np.log(2.0 * tt) + PSI14 - PSI2)
        p = -2.0 * tt
        pw = p * p
        acc = np.zeros_like(tt)
        for n in range(2, 42):
            acc += _FC[n - 2] * pw
            pw = pw * p
        out[m1] = s + acc
    if np.any(m2):
        tt = t[m2]
        z = np.exp(-2.0 * tt)
        acc = np.zeros_like(tt)
        pw = np.ones_like(tt)
        for n in range(300):
            acc += pw / (n + 0.25) ** 2
            pw = pw * z
            if np.max(pw) < 1e-17:
                break
        out[m2] = np.exp(-tt / 2.0) * acc
    return out


def sieve(N):
    """primes up to N and von Mangoldt array."""
    is_p = np.ones(N + 1, bool)
    is_p[:2] = False
    for p in range(2, int(N ** 0.5) + 1):
        if is_p[p]:
            is_p[p * p::p] = False
    primes = np.nonzero(is_p)[0]
    lam = np.zeros(N + 1)
    lam[primes] = np.log(primes)
    for p in primes:
        if p * p > N:
            break
        q = p * p
        while q <= N:
            lam[q] = np.log(float(p))
            if q > N // p:
                break
            q *= p
    return primes, lam


_PRIMES, _LAM = sieve(100000)


def weight_array(variant, nmax):
    """w(n) for the prime sum in g(t)."""
    w = np.zeros(nmax + 1)
    if variant == 'lambda':      # full von Mangoldt
        w[:] = _LAM[:nmax + 1]
    elif variant == 'indicator':  # 1 on primes, 0 else
        ps = _PRIMES[_PRIMES <= nmax]
        w[ps] = 1.0
    elif variant == 'nopp':       # Lambda on primes only (drop p^k, k>=2)
        ps = _PRIMES[_PRIMES <= nmax]
        w[ps] = np.log(ps)
    else:
        raise ValueError(variant)
    return w


def make_g(variant, tmax):
    """g(t) per Suzuki (1.3) with chosen prime-sum weights. Vectorized."""
    nmax = int(np.floor(np.exp(tmax))) + 1
    w = weight_array(variant, nmax)
    ns = np.nonzero(w > 0)[0]
    logn = np.log(ns)
    wn = w[ns] / np.sqrt(ns)

    def g(t):
        t = np.asarray(t, dtype=float)
        at = np.abs(t)
        pole = -4.0 * (np.exp(at / 2.0) + np.exp(-at / 2.0) - 2.0)
        arch1 = -(at / 2.0) * (PSI14 - LOGPI)
        arch2 = -0.25 * (ZETA214 - F_of_t(at))
        d = at[..., None] - logn[None, :]
        psum = np.sum(wn[None, :] * np.maximum(d, 0.0), axis=-1)
        return pole + psum + arch1 + arch2

    return g


def build_G2(g, a, ngrid=40001):
    """G2(t) = ∫_0^t ∫_0^s g(r) dr ds, G2(0)=0, via cumulative trapezoid + spline."""
    tg = np.linspace(-2.0 * a, 2.0 * a, ngrid)
    gv = g(tg)
    G1 = cumulative_trapezoid(gv, tg, initial=0.0)
    i0 = ngrid // 2
    G1 = G1 - G1[i0]
    G2 = cumulative_trapezoid(G1, tg, initial=0.0)
    G2 = G2 - G2[i0]
    return CubicSpline(tg, G2)


def assemble_Q(a, N, G2):
    """Stiffness Q as dense symmetric Toeplitz (n = N-1 interior dofs)."""
    h = 2.0 * a / N
    n = N - 1
    pts = np.arange(-N, N + 1, dtype=float) * h      # (j-N)h, j=0..2N
    Gp = G2(pts)
    S = Gp[2:] - 2.0 * Gp[1:-1] + Gp[:-2]            # S_k, k=-(N-1)..N-1
    # T_k = 2 S_k - S_{k-1} - S_{k+1}; S index m <-> k = m-(N-1)
    T = 2.0 * S[1:-1] - S[:-2] - S[2:]               # k=-(N-2)..N-2
    # want T_k for k=0..n-1 (n=N-1); T[m] <-> k=m-(N-2)
    Tpos = T[(N - 2):(N - 2) + (N - 1)]
    Q = toeplitz(Tpos) / h ** 2
    return Q


def assemble_M(a, N):
    """Standard P1 mass matrix, Dirichlet (interior dofs only)."""
    h = 2.0 * a / N
    n = N - 1
    M = np.zeros((n, n))
    np.fill_diagonal(M, 2.0 * h / 3.0)
    if n > 1:
        M[np.arange(n - 1), np.arange(1, n)] = h / 6.0
        M[np.arange(1, n), np.arange(n - 1)] = h / 6.0
    return M


def lowest_eigs(a, N, G2, k=3):
    """k smallest algebraic eigenvalues of Q v = lam M v."""
    Q = assemble_Q(a, N, G2)
    M = assemble_M(a, N)
    vals, _ = eigsh(Q, k=k, M=M, which='SA', tol=1e-10, maxiter=10 * Q.shape[0])
    return np.sort(vals), Q, M


def richardson(lamN, lam2N):
    """3-point Richardson extrapolation for O(h^2) error."""
    return lam2N + (lam2N - lamN) / 3.0
