#!/usr/bin/env python3
"""Executable midpoint transcript for the corrected rank-four Suzuki high block.

This script rebuilds the scalar data for odd modes 21..16001, runs the
corrected O(N^2), O(N)-state displacement-generator LDL recurrence, and streams
three quantities needed by the renewed a-posteriori certificate:

  * min scalar pivot;
  * |||L|||_1 and |||L|||_inf;
  * y_max for ||L^{-1}||_inf, where
        y_i = 1 + sum_{j<i}|l_ij| y_j.

It is a midpoint diagnostic/reproducibility script, not the final
outward-rounded arithmetic certificate.
"""
from fractions import Fraction
from math import comb, factorial, log, pi, sqrt
import numpy as np
from scipy.special import sici

START, STOP, SHIFT = 21, 16001, 0.22
QS = (2, 3, 4, 5, 7)
LAMBDAS = (log(2), log(3), log(2), log(5), log(7))


def bernoulli_up_to(n):
    B = [Fraction(0) for _ in range(n+1)]
    B[0] = Fraction(1)
    for m in range(1, n+1):
        B[m] = -sum(Fraction(comb(m+1, k))*B[k] for k in range(m))/Fraction(m+1)
    return B


def euler_even_up_to(n):
    E = [0]*(n+1)
    E[0] = 1
    for j in range(1, n+1):
        E[j] = -sum(comb(2*j, 2*k)*E[k] for k in range(j))
    return E


def h_coefficients(N=32):
    B = bernoulli_up_to(2*N+2)
    E = euler_even_up_to(N+1)
    degree = 2*N+1
    a = [Fraction(0) for _ in range(degree+1)]
    for r in range(N+1):
        a[2*r] = Fraction(E[r], 4*factorial(2*r)*2**(2*r))
    for r in range(1, N+2):
        p = 2*r-1
        if p > degree:
            break
        a[p] = Fraction(2*(1-2**(2*r-1)), 4*factorial(2*r)*2**(2*r-1))*B[2*r]
    return np.array([float(x) for x in a], dtype=float)


def arch_HD(modes):
    coeff = h_coefficients(32)
    b = modes*pi/2.0
    degree = len(coeff)-1
    I = np.empty((degree+2, len(modes)), dtype=float)
    J = np.empty_like(I)
    I[0] = 0.0
    J[0] = 2.0/b
    for p in range(1, degree+2):
        I[p] = -(p/b)*J[p-1]
        J[p] = (2.0**p)/b + (p/b)*I[p-1]
    H = np.tensordot(coeff, J[:degree+1], axes=(0, 0))
    D = -sum(coeff[p]*(2*I[p]-I[p+1]+J[p]/b) for p in range(degree+1))
    return H, D


def scalar_state():
    modes = np.arange(START, STOP+1, 2, dtype=float)
    b = modes*pi/2.0
    A = np.zeros_like(modes)
    prime_diag = np.zeros_like(modes)
    for q, lam in zip(QS, LAMBDAS):
        ell = log(q)
        w = lam/sqrt(q)
        A += w*np.sin(modes*pi*ell/2.0)
        prime_diag -= w*((2.0-ell)*np.cos(b*ell)+np.sin(b*ell)/b)
    Si, Ci = sici(modes*pi)
    cusp_diag = np.log(modes/4.0)-Ci-Si/(modes*pi)
    H, arch_diag = arch_HD(modes)

    # Corrected two skew generator pairs.
    U = Si + 2.0*A
    V = modes.copy()
    P = modes.copy()
    Q = modes*modes*H
    d = cusp_diag + prime_diag + arch_diag - SHIFT
    x = modes*modes
    return modes, x, d, U, V, P, Q


def run():
    modes, x, d, U, V, P, Q = scalar_state()
    N = len(modes)
    yacc = np.zeros(N)
    y = np.zeros(N)
    row_abs = np.zeros(N)
    absL_one = 1.0
    dmin = float('inf')
    dmin_mode = None

    for k in range(N-1):
        a = d[k]
        if a < dmin:
            dmin, dmin_mode = float(a), int(modes[k])
        y[k] = 1.0 + yacc[k]
        den = x[k]-x[k+1:]
        ell = (((2.0/pi)*(U[k]*V[k+1:]-V[k]*U[k+1:])
                + pi*(P[k]*Q[k+1:]-Q[k]*P[k+1:]))/den)/a
        ae = np.abs(ell)
        row_abs[k+1:] += ae
        absL_one = max(absL_one, 1.0+float(ae.sum()))
        yacc[k+1:] += ae*y[k]
        d[k+1:] -= a*ell*ell
        U[k+1:] -= ell*U[k]
        V[k+1:] -= ell*V[k]
        P[k+1:] -= ell*P[k]
        Q[k+1:] -= ell*Q[k]

    if d[-1] < dmin:
        dmin, dmin_mode = float(d[-1]), int(modes[-1])
    y[-1] = 1.0+yacc[-1]
    ymax_i = int(np.argmax(y))
    ymax = float(y[ymax_i])
    absL_inf = 1.0+float(row_abs.max())
    allowance = dmin/(N*ymax*ymax)
    return {
        'dimension': N,
        'minimum_pivot': dmin,
        'minimum_pivot_mode': dmin_mode,
        'absL_one': absL_one,
        'absL_inf': absL_inf,
        'ymax': ymax,
        'ymax_mode': int(modes[ymax_i]),
        'crude_Linv2_bound': sqrt(N)*ymax,
        'midpoint_residual_allowance': allowance,
    }


if __name__ == '__main__':
    t = run()
    for k, v in t.items():
        print(f'{k} = {v}')
    print('guardrail: midpoint transcript only; directed-rounded arithmetic residual still required')
