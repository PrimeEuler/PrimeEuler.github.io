#!/usr/bin/env python3
"""Finite Feshbach / buffer-anatomy audit for Suzuki's a=1 even-v sector.

This checkpoint continues v13.315.  It assembles the odd Dirichlet matrix

    A = C_cusp + B_prime + K_arch + P_pole

for odd modes n<401 without returning to the original 2-D quadrature:

* C_cusp uses the exact Si/Ci formulas from v13.301;
* B_prime uses the v13.315 exact joint-prime sequence factorization;
* K_arch is a smooth 1-D quadrature against the exact shift matrix element;
* P_pole is the exact positive rank-one pole contribution in the even sector.

The finite core is n<=19 and the finite buffer is 21<=n<=399.  The script
reports the numerical buffer spectrum, the finite Feshbach correction

    Delta = A_CB A_BB^{-1} A_BC,

and the high-precision spectrum of the 10x10 core block.

Important guardrail: external audit round 17 found a sign error in the earlier
v13.314 boxed shift formula, while independently confirming the v13.315
joint-prime formula used here.  No formula from the superseded v13.314 sign
convention is used in this script.

This is a numerical anatomy audit, not an interval-certified positivity proof.
In particular, positivity of the finite buffer block does not by itself prove
positivity of the infinite complement, and tiny finite eigenvalues do not
establish exact zero modes, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss
from scipy.special import sici

PI = math.pi
QS = (2, 3, 4, 5, 7)
WEIGHTS = (
    math.log(2.0)/math.sqrt(2.0),
    math.log(3.0)/math.sqrt(3.0),
    math.log(2.0)/2.0,
    math.log(5.0)/math.sqrt(5.0),
    math.log(7.0)/math.sqrt(7.0),
)
THETAS = tuple(0.5*PI*math.log(q) for q in QS)


def Aseq(n: int) -> float:
    return sum(w*math.sin(n*th) for w, th in zip(WEIGHTS, THETAS))


def cusp_entry(m: int, n: int) -> float:
    if m == n:
        si, ci = sici(n*PI)
        return math.log(n/4.0) - ci - si/(n*PI)
    sim, _ = sici(m*PI)
    sin, _ = sici(n*PI)
    return (2.0/PI)*(n*sim - m*sin)/(m*m - n*n)


def shift_entry(m: int, n: int, ell: float) -> float:
    """Exact <psi_m,S_ell psi_n> in the odd Dirichlet basis."""
    if m == n:
        k = n*PI/2.0
        return (2.0-ell)*math.cos(k*ell) + math.sin(k*ell)/k
    th = 0.5*PI*ell
    return (4.0/PI)*(n*math.sin(m*th)-m*math.sin(n*th))/(n*n-m*m)


def prime_entry(m: int, n: int) -> float:
    if m == n:
        return -sum(w*shift_entry(n, n, math.log(q))
                    for q, w in zip(QS, WEIGHTS))
    return -(4.0/PI)*(n*Aseq(m)-m*Aseq(n))/(n*n-m*m)


def rpp(t: np.ndarray) -> np.ndarray:
    """r''(t)=exp(-t/2)/(1-exp(-2t))-1/(2t), stable on GL nodes."""
    t = np.asarray(t, dtype=float)
    out = np.exp(-t/2.0)/(1.0-np.exp(-2.0*t)) - 1.0/(2.0*t)
    return out


def shift_matrix(ns: np.ndarray, t: float) -> np.ndarray:
    nrow = ns[:, None]
    ncol = ns[None, :]
    s = np.sin(ns*(PI*t/2.0))
    num = ncol*s[:, None] - nrow*s[None, :]
    den = ncol*ncol - nrow*nrow
    S = np.empty((len(ns), len(ns)), dtype=float)
    mask = den != 0
    S[mask] = (4.0/PI)*num[mask]/den[mask]
    k = ns*PI/2.0
    np.fill_diagonal(S, (2.0-t)*np.cos(k*t) + np.sin(k*t)/k)
    return S


def arch_matrix(ns: np.ndarray, order: int = 500) -> np.ndarray:
    gx, gw = leggauss(order)
    t = gx + 1.0  # [-1,1] -> [0,2], Jacobian 1
    h = rpp(t)
    K = np.zeros((len(ns), len(ns)), dtype=float)
    for tt, ww, hh in zip(t, gw, h):
        K += ww*(-hh)*shift_matrix(ns, float(tt))
    return K


def pole_matrix(ns: np.ndarray, order: int = 500) -> np.ndarray:
    gx, gw = leggauss(order)
    psi = np.sin((ns[:, None]*PI/2.0)*(gx[None, :]+1.0))
    c = psi @ (gw*np.cosh(gx/2.0))
    return 2.0*np.outer(c, c)


def finite_matrix(max_n: int = 399, arch_order: int = 500):
    ns = np.arange(1, max_n+1, 2, dtype=int)
    M = len(ns)
    C = np.empty((M, M), dtype=float)
    B = np.empty((M, M), dtype=float)
    for i, m in enumerate(ns):
        for j, n in enumerate(ns):
            C[i, j] = cusp_entry(int(m), int(n))
            B[i, j] = prime_entry(int(m), int(n))
    K = arch_matrix(ns, arch_order)
    P = pole_matrix(ns, arch_order)
    return ns, C+B+K+P


def buffer_sequence(A: np.ndarray, ns: np.ndarray,
                    cutoffs=(101,151,201,237,301,351,399)):
    rows = []
    for max_n in cutoffs:
        idx = np.where((ns >= 21) & (ns <= max_n))[0]
        e = np.linalg.eigvalsh(A[np.ix_(idx, idx)])
        rows.append((max_n, len(idx), float(e[0]), float(e[1]), float(e[2])))
    return rows


def feshbach_report(A: np.ndarray, ns: np.ndarray):
    ic = np.where(ns <= 19)[0]
    ib = np.where(ns >= 21)[0]
    Acc = A[np.ix_(ic, ic)]
    Abb = A[np.ix_(ib, ib)]
    Acb = A[np.ix_(ic, ib)]
    X = np.linalg.solve(Abb, Acb.T)
    Delta = Acb @ X
    F = Acc - Delta
    return {
        'buffer_eigs': np.linalg.eigvalsh(Abb),
        'core_buffer_norm2': float(np.linalg.norm(Acb, 2)),
        'core_buffer_fro': float(np.linalg.norm(Acb, 'fro')),
        'delta_eigs': np.linalg.eigvalsh(Delta),
        'delta_norm2': float(np.linalg.norm(Delta, 2)),
        'finite_feshbach_eigs': np.linalg.eigvalsh(F),
    }


def high_precision_core(dps: int = 60):
    """Independent 10x10 core build using mpmath and 1-D arch quadrature."""
    with mp.workdps(dps):
        core = list(range(1, 20, 2))
        qsm = (2,3,4,5,7)
        wsm = (mp.log(2)/mp.sqrt(2), mp.log(3)/mp.sqrt(3), mp.log(2)/2,
               mp.log(5)/mp.sqrt(5), mp.log(7)/mp.sqrt(7))

        def amp(j):
            return sum(w*mp.sin(j*mp.pi*mp.log(q)/2) for q,w in zip(qsm,wsm))

        def ce(m,n):
            if m == n:
                return mp.log(mp.mpf(n)/4)-mp.ci(n*mp.pi)-mp.si(n*mp.pi)/(n*mp.pi)
            return (2/mp.pi)*(n*mp.si(m*mp.pi)-m*mp.si(n*mp.pi))/(m*m-n*n)

        def se(m,n,t):
            if m == n:
                k=n*mp.pi/2
                return (2-t)*mp.cos(k*t)+mp.sin(k*t)/k
            th=mp.pi*t/2
            return (4/mp.pi)*(n*mp.sin(m*th)-m*mp.sin(n*th))/(n*n-m*m)

        def pe(m,n):
            if m == n:
                return -sum(w*se(n,n,mp.log(q)) for q,w in zip(qsm,wsm))
            return -(4/mp.pi)*(n*amp(m)-m*amp(n))/(n*n-m*m)

        def rr(t):
            if t == 0:
                return mp.mpf(1)/4
            return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)

        def pole_c(n):
            return mp.quad(lambda x: mp.sin(n*mp.pi*(x+1)/2)*mp.cosh(x/2), [-1,1])

        cvec = [pole_c(n) for n in core]
        A = mp.matrix(len(core))
        for i,m in enumerate(core):
            for j,n in enumerate(core):
                ar = mp.quad(lambda t: -rr(t)*se(m,n,t), [0,2])
                A[i,j] = ce(m,n)+pe(m,n)+ar+2*cvec[i]*cvec[j]
        vals, _ = mp.eigsy(A)
        return [vals[j] for j in range(len(core))]


def report():
    ns, A = finite_matrix()
    print('buffer convergence: max_n dim lambda1 lambda2 lambda3')
    for row in buffer_sequence(A, ns):
        print(*row)
    f = feshbach_report(A, ns)
    print('buffer first 10 =', f['buffer_eigs'][:10])
    print('||A_CB||_2 =', f['core_buffer_norm2'])
    print('||A_CB||_F =', f['core_buffer_fro'])
    print('Delta eigenvalues =', f['delta_eigs'])
    print('||Delta||_2 =', f['delta_norm2'])
    print('finite Feshbach eigenvalues =', f['finite_feshbach_eigs'])
    print('60-digit core eigenvalues')
    for x in high_precision_core():
        print(mp.nstr(x, 30))


if __name__ == '__main__':
    report()
