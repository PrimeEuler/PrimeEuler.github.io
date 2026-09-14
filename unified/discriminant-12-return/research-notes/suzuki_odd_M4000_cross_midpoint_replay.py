#!/usr/bin/env python3
"""Independent midpoint/provenance replay for the odd M=4000 F<->T cross block.

This reconstructs the historical cross constants from the source-faithful
same-parity formula instead of importing them from the old fail-closed
transcript.

Split
-----
    F      = {22,24,...,4000}
    Tnear  = {4002,4004,...,16000}
    Trem   = {16002,16004,...,2000000}
    Tfar   = {2000002,2000004,...}

For m in F, n in T,

    A_mn = -(2/pi) (n Z_m - m Z_n)/(n^2-m^2) + 2 d_m d_n,

    d_n = 2 k_n sinh(1/2)/(k_n^2+1/4),  k_n=n*pi/2.

The even-mode arch/cusp combination is evaluated through the equivalent
source-faithful identity

    Si(n*pi) + 2 H_n
      = Im psi(1/4+i n*pi/4)
        - n*pi sum_{j>=0} exp(-2 a_j)/(a_j^2+(n*pi/2)^2),

    a_j = 2j+1/2.

Twenty exponential terms are far beyond binary64 relevance here.

Near band
---------
The explicit 1990 x 6000 cross matrix is formed, its leading rank-12 SVD is
computed, and the discarded Frobenius norm is obtained from

    ||R||_F^2 = ||A||_F^2 - sum_{j<=12} sigma_j^2.

This reproduces the historical ~0.0023073371285 residual.

Remote through 2e6
------------------
For n>=16002, m<=4000, expand

    1/(n^2-m^2) = n^-2 sum_{r>=0} (m/n)^(2r).

Each r contributes two separable channels.  Eight r-levels are retained,
plus the exact pole channel.  The displayed convergence across 4..8 levels is
used only as a midpoint provenance check; an outward remainder charge is still
required for theorem use.

Far tail
--------
The leading 1/n vector is

    L = -(2/pi) Z_F + (8 sinh(1/2)/pi) d_F.

Using |Z_n|<8 and rho=4000/N for N=2000002 gives

    ||column_n - L/n||_2 <= B/n^2 + C/n^3,

    B = (16/pi)/(1-rho^2) ||F||_2,
    C = (2/pi)/(1-rho^2) ||F^2 Z_F||_2
        + (8 sinh(1/2)/pi^3) ||d_F||_2.

The Frobenius sum of this remainder, combined with the exact rank-one 1/n
channel sum, reproduces the historical <0.03519 far-tail target.

STATUS
------
This file uses binary64/scipy special functions and SVD/eigensolvers.  It is a
midpoint/regression/provenance artifact, NOT an outward certificate for
||A_FT||<1.015.  The next certification step is to replace Z_F and tail-source
moments by rational/certified enclosures and explicitly charge linear algebra
roundoff and the inverse-power truncation.

No inertia, exact-zero, RH, or GRH conclusion follows from this file alone.
"""
from __future__ import annotations

from math import exp, log, pi, sinh, sqrt
import numpy as np
from scipy.special import digamma, polygamma, zeta as hurwitz_zeta
from scipy.sparse.linalg import svds

QS = (2, 3, 4, 5, 7)
LAMBDAS = (log(2), log(3), log(2), log(5), log(7))
ELLS = tuple(log(q) for q in QS)
WEIGHTS = tuple(L/sqrt(q) for L, q in zip(LAMBDAS, QS))

F = np.arange(22, 4001, 2, dtype=float)
TNEAR = np.arange(4002, 16001, 2, dtype=float)
TREM = np.arange(16002, 2000001, 2, dtype=float)
NFAR = 2000002
M_SCALE = 4000.0


def Z_even(modes: np.ndarray, exp_terms: int = 20) -> np.ndarray:
    """Source-faithful midpoint Z_n for even modes."""
    modes = np.asarray(modes, dtype=float)
    prime = np.zeros_like(modes)
    for w, ell in zip(WEIGHTS, ELLS):
        prime += w*np.sin(modes*pi*ell/2.0)

    b = modes*pi/2.0
    y = modes*pi/4.0
    arch_cusp = np.imag(digamma(0.25 + 1j*y))
    correction = np.zeros_like(modes)
    for j in range(exp_terms):
        a = 2.0*j + 0.5
        correction += modes*pi*exp(-2.0*a)/(a*a+b*b)
    arch_cusp -= correction
    return 2.0*prime + arch_cusp


def d_even(modes: np.ndarray) -> np.ndarray:
    k = np.asarray(modes, dtype=float)*pi/2.0
    return 2.0*k*sinh(0.5)/(k*k+0.25)


def near_matrix(ZF: np.ndarray, ZT: np.ndarray) -> np.ndarray:
    m = F[:, None]
    n = TNEAR[None, :]
    A = -(2.0/pi)*(n*ZF[:, None]-m*ZT[None, :])/(n*n-m*m)
    A += 2.0*d_even(F)[:, None]*d_even(TNEAR)[None, :]
    return A


def rank12_near(A: np.ndarray):
    U, s, _ = svds(A, k=12, which='LM', return_singular_vectors=True,
                   tol=1e-11, maxiter=1000)
    order = np.argsort(s)[::-1]
    U = U[:, order]
    s = s[order]
    fro = float(np.linalg.norm(A, 'fro'))
    residual = sqrt(max(0.0, fro*fro-float(np.dot(s, s))))
    return U, s, fro, residual


def remote_low_rank(ZF: np.ndarray, ZR: np.ndarray, levels: int):
    """Return F-side factor U and tail feature Gram for r=0..levels-1 + pole."""
    xF = F/M_SCALE
    xR = M_SCALE/TREM
    Ucols = []
    Crows = []
    for r in range(levels):
        Ucols.append(-(2.0/pi)*ZF*xF**(2*r))
        Crows.append(xR**(2*r)/TREM)
        Ucols.append((2.0/pi)*xF**(2*r+1))
        Crows.append(xR**(2*r+1)*ZR/TREM)
    Ucols.append(2.0*d_even(F))
    Crows.append(d_even(TREM))
    U = np.column_stack(Ucols)
    C = np.vstack(Crows)
    return U, C@C.T


def top_from_gram(G: np.ndarray) -> float:
    return sqrt(float(np.linalg.eigvalsh(G)[-1]))


def far_tail_bound(ZF: np.ndarray):
    dF = d_even(F)
    L = -(2.0/pi)*ZF + (8.0*sinh(0.5)/pi)*dF

    # Even n>=2000002 are n=2j, j>=1000001.
    j0 = NFAR//2
    S2 = float(polygamma(1, j0))/4.0
    leading = float(np.linalg.norm(L))*sqrt(S2)

    rho = 4000.0/NFAR
    B = (16.0/pi)/(1.0-rho*rho)*float(np.linalg.norm(F))
    C = ((2.0/pi)/(1.0-rho*rho)*float(np.linalg.norm(F*F*ZF))
         + (8.0*sinh(0.5)/pi**3)*float(np.linalg.norm(dF)))

    # sum over n=2j, j>=j0.
    S4 = 2.0**-4*float(hurwitz_zeta(4, j0))
    S5 = 2.0**-5*float(hurwitz_zeta(5, j0))
    S6 = 2.0**-6*float(hurwitz_zeta(6, j0))
    remainder = sqrt(B*B*S4 + 2.0*B*C*S5 + C*C*S6)
    return leading, remainder, leading+remainder, B, C


def source_error_maps_near():
    """Operator norms mapping uniform Z_F/Z_T errors into near cross errors."""
    m = F[:, None]
    n = TNEAR[None, :]
    P = n/(n*n-m*m)
    Q = m/(n*n-m*m)
    pnorm = float(svds(P, k=1, which='LM', return_singular_vectors=False)[0])
    qnorm = float(svds(Q, k=1, which='LM', return_singular_vectors=False)[0])
    return (2.0/pi)*pnorm, (2.0/pi)*qnorm


def report():
    ZF = Z_even(F)
    ZT = Z_even(TNEAR)
    A = near_matrix(ZF, ZT)
    U12, s12, near_fro, near_residual = rank12_near(A)
    Gnear12 = (U12*(s12*s12))@U12.T

    print('near dimensions =', A.shape)
    print('near top singular value =', repr(float(s12[0])))
    print('near Frobenius norm =', repr(near_fro))
    print('near rank-12 residual Frobenius =', repr(near_residual))

    ZR = Z_even(TREM)
    combined = {}
    remote = {}
    for levels in range(4, 9):
        Urem, Gfeat = remote_low_rank(ZF, ZR, levels)
        Grem = Urem@Gfeat@Urem.T
        remote[levels] = top_from_gram(Grem)
        combined[levels] = top_from_gram(Gnear12+Grem)
        print('remote levels', levels,
              'remote low-rank norm =', repr(remote[levels]),
              'combined near12+remote =', repr(combined[levels]))

    explicit_mid = combined[8] + near_residual
    print('combined midpoint + near residual =', repr(explicit_mid))
    print('historical rounded explicit target = 0.97957')

    leading, rem, far, B, C = far_tail_bound(ZF)
    print('far leading 1/n channel =', repr(leading))
    print('far Frobenius remainder =', repr(rem))
    print('far total midpoint-coefficient bound =', repr(far))
    print('far B =', repr(B))
    print('far C =', repr(C))
    print('historical rounded far target = 0.03519')

    eFmap, eTmap = source_error_maps_near()
    print('(2/pi)||P|| near finite-side error map =', repr(eFmap))
    print('(2/pi)||Q|| near tail-side error map =', repr(eTmap))

    # Regression/provenance guards only; they are not proof inequalities.
    assert 0.9227 < s12[0] < 0.9229
    assert abs(near_residual-0.0023073371285179897) < 1e-9
    assert 0.9771 < combined[8] < 0.9774
    assert explicit_mid < 0.97958
    assert far < 0.03519
    assert 0.44 < eFmap < 0.46
    assert 0.37 < eTmap < 0.39
    print('PASS: historical odd cross constants independently reproduced at midpoint scale')
    print('GUARDRAIL: outward source/arithmetic/inverse-power certification still required')


if __name__ == '__main__':
    report()
