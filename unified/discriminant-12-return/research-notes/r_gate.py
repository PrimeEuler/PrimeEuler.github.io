"""Assembly + solve for the r_{0,A}/r_{1,A} gate. Sandbox only.

Definitions [D] (v13.758 S1, v13.757 S7):
  L_A = integral operator on (-A,A) with kernel k(x,y) = g(x-y) - lam*N(x,y)
        (Suzuki v2 S8.3: "Let k(x, y) = g(x - y) - lam N(x, y)"; S_a = G_a - lam(-Delta_N)^{-1})
  N(x,y) = (x^2+y^2)/(4A) - |x-y|/2 + A/6   [D, Suzuki v2 S8.2]
  R_A = L_A^{-1};  l0(v) = int k(0,y)v(y)dy;  l1(v) = int k_x(0,y)v(y)dy
  M00 = l0(R_A 1),  M1x = l1(R_A x),  M0e = l0(R_A (cosh-1)),  M1e = l1(R_A (sinh-x))
  r0 = M0e/(1+M00),  r1 = M1e/(1+M1x);  d0 = |1+M00|, d1 = |1+M1x|
Gate: r1 = o(e^A/A), r0 = o(e^A).  lam = -1 ONLY (expedition canary).
"""
import numpy as np
from scipy.linalg import solve, eigvalsh, toeplitz
from scipy.interpolate import CubicSpline
from numpy.polynomial.legendre import leggauss
import fem_screw as fs


def build_g_spline(A, ngrid=None):
    g = fs.make_g('lambda', 2.0 * A)
    if ngrid is None:
        ngrid = max(40001, int(20000 * A))
    tg = np.linspace(-2 * A, 2 * A, ngrid)
    return CubicSpline(tg, g(tg))


def assemble(A, N, lam, q=8):
    """Returns K, k0, kx0, b (dict of 4 sources), diag dict."""
    h = 2.0 * A / N
    xs = -A + h * np.arange(N + 1)
    gsp = build_g_spline(A)
    gp = gsp.derivative()
    u, w = leggauss(q)
    Lam = 1.0 - np.abs(u)
    Wu = w * Lam
    W2 = np.outer(Wu, Wu)  # (q,q)
    d = np.arange(N + 1)
    # pairwise args: h*(d + u_p - u_q), shape (N+1, q, q)
    arg = h * (d[:, None, None] + u[None, :, None] - u[None, None, :])
    Tg = h ** 2 * np.einsum('pq,dpq->d', W2, gsp(arg))
    Ta = h ** 2 * np.einsum('pq,dpq->d', W2, np.abs(arg))
    Kg = toeplitz(Tg)
    Ka_abs = toeplitz(Ta)
    # 1D moments m_i = int phi_i, mx2_i = int x^2 phi_i (element Gauss, exact)
    u2, w2 = leggauss(4)
    m = np.zeros(N + 1)
    mx2 = np.zeros(N + 1)
    for e in range(N):
        x0, x1 = xs[e], xs[e + 1]
        xq = 0.5 * (x0 + x1) + 0.5 * h * u2
        # phi_e = (x1-x)/h, phi_{e+1} = (x-x0)/h
        pe = (x1 - xq) / h
        pe1 = (xq - x0) / h
        wq = 0.5 * h * w2
        m[e] += np.sum(wq * pe)
        m[e + 1] += np.sum(wq * pe1)
        mx2[e] += np.sum(wq * pe * xq ** 2)
        mx2[e + 1] += np.sum(wq * pe1 * xq ** 2)
    KN = ((np.outer(mx2, m) + np.outer(m, mx2)) / (4.0 * A)
          - 0.5 * Ka_abs + (A / 6.0) * np.outer(m, m))
    K = Kg - lam * KN
    # boundary functional vectors: element Gauss
    uq, wq = leggauss(q)
    k0 = np.zeros(N + 1)
    kx0 = np.zeros(N + 1)
    for e in range(N):
        x0, x1 = xs[e], xs[e + 1]
        xg = 0.5 * (x0 + x1) + 0.5 * h * uq
        pe = (x1 - xg) / h
        pe1 = (xg - x0) / h
        wgt = 0.5 * h * wq
        N0 = xg ** 2 / (4.0 * A) - np.abs(xg) / 2.0 + A / 6.0
        kval = gsp(xg) - lam * N0
        k0[e] += np.sum(wgt * pe * kval)
        k0[e + 1] += np.sum(wgt * pe1 * kval)
        sgn = np.sign(xg)
        kxval = -gp(xg) - lam * sgn / 2.0
        kx0[e] += np.sum(wgt * pe * kxval)
        kx0[e + 1] += np.sum(wgt * pe1 * kxval)
    # source vectors
    srcs = {'one': lambda x: np.ones_like(x),
            'x': lambda x: x,
            'cosh-1': lambda x: np.cosh(x) - 1.0,
            'sinh-x': lambda x: np.sinh(x) - x}
    b = {}
    for name, f in srcs.items():
        bv = np.zeros(N + 1)
        for e in range(N):
            x0, x1 = xs[e], xs[e + 1]
            xg = 0.5 * (x0 + x1) + 0.5 * h * uq
            pe = (x1 - xg) / h
            pe1 = (xg - x0) / h
            wgt = 0.5 * h * wq
            fv = f(xg)
            bv[e] += np.sum(wgt * pe * fv)
            bv[e + 1] += np.sum(wgt * pe1 * fv)
        b[name] = bv
    return K, k0, kx0, b, dict(h=h, xs=xs, m=m)


def neumann_check(A, N=400):
    """Verify N(x,y) inverts -d^2/dx^2 on Neumann modes [D-check]."""
    h = 2.0 * A / N
    xs = -A + h * np.arange(N + 1)
    # target mode: cos(pi*(x+A)/(2A)), eigenvalue (2A/pi)^2
    phi = np.cos(np.pi * (xs + A) / (2 * A))
    ev = (2 * A / np.pi) ** 2
    # (K_N phi)(x) = int N(x,y) phi(y) dy via fine quadrature
    u, w = leggauss(16)
    res = np.zeros(N + 1)
    for e in range(N):
        x0, x1 = xs[e], xs[e + 1]
        yg = 0.5 * (x0 + x1) + 0.5 * h * u
        wgt = 0.5 * h * w
        phig = np.cos(np.pi * (yg + A) / (2 * A))
        for i, x in enumerate(xs):
            Nxy = (x ** 2 + yg ** 2) / (4 * A) - np.abs(x - yg) / 2 + A / 6
            res[i] += np.sum(wgt * Nxy * phig)
    err = np.max(np.abs(res - ev * phi)) / np.max(np.abs(ev * phi))
    return err


def solve_moments(A, N, lam=-1.0, q=8, want_cond=True):
    K, k0, kx0, b, info = assemble(A, N, lam, q)
    out = dict(A=A, N=N, lam=lam, q=q, h=info['h'])
    if want_cond:
        w = eigvalsh(K)
        out['eig_min'] = w[0]
        out['eig_max'] = w[-1]
        out['cond'] = abs(w[-1]) / max(abs(w[0]), 1e-300)
    sols = {}
    maxres = 0.0
    for name, bv in b.items():
        c = solve(K, bv, assume_a='sym')
        sols[name] = c
        maxres = max(maxres, np.max(np.abs(K @ c - bv)) / np.max(np.abs(bv)))
    out['res'] = maxres
    c1, cx, ce, cs = sols['one'], sols['x'], sols['cosh-1'], sols['sinh-x']
    # parity canaries [D]: even sources -> even response; odd -> odd
    n = N + 1
    out['par_one'] = np.max(np.abs(c1 - c1[::-1])) / np.max(np.abs(c1))
    out['par_x'] = np.max(np.abs(cx + cx[::-1])) / np.max(np.abs(cx))
    out['cross_kx0_c1'] = abs(kx0 @ c1) / (np.linalg.norm(kx0) * np.linalg.norm(c1))
    out['cross_k0_cx'] = abs(k0 @ cx) / (np.linalg.norm(k0) * np.linalg.norm(cx))
    M00 = k0 @ c1
    M1x = kx0 @ cx
    M0e = k0 @ ce
    M1e = kx0 @ cs
    out.update(M00=M00, M1x=M1x, M0e=M0e, M1e=M1e)
    out['d0'] = abs(1 + M00)
    out['d1'] = abs(1 + M1x)
    out['r0'] = M0e / (1 + M00)
    out['r1'] = M1e / (1 + M1x)
    return out


if __name__ == '__main__':
    import sys
    A = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    print(f"Neumann kernel check (A={A}): rel err = {neumann_check(A):.2e}", flush=True)
    o = solve_moments(A, N)
    for k in ['eig_min', 'eig_max', 'cond', 'res', 'par_one', 'par_x',
              'cross_kx0_c1', 'cross_k0_cx', 'M00', 'M1x', 'M0e', 'M1e',
              'd0', 'd1', 'r0', 'r1']:
        print(f"  {k} = {o[k]:.6e}", flush=True)
