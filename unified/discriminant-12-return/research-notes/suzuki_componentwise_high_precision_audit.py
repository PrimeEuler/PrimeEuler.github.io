#!/usr/bin/env python3
"""Componentwise high-precision audit of Suzuki's a=1 direct quadratic form.

This v13.291 control continues the one-dimensional reduction of v13.290.  It
splits the matrix exactly at the source-formula level into

    A = A_pole + A_prime + A_arch,

and evaluates the resulting one-dimensional matrix elements with arbitrary
precision.  The purpose is to distinguish genuine near-zero structure from
floating-point sign loss caused by cancellation of O(1) source components.

The direct Dirichlet basis is

    psi_n(x) = a^{-1/2} sin(n*pi*(x+a)/(2a)).

Important parity convention: odd n gives EVEN psi_n, while even n gives ODD
psi_n.  This is opposite to the parity of the differentiated Neumann mode
u=Dv, because differentiation reverses parity.

This script is a numerical audit.  Positivity of finite Ritz sections does not
prove lambda_a>0, RH, or admissibility of any chosen lambda.
"""
from __future__ import annotations

from math import log, pi
import mpmath as mp
import numpy as np

from suzuki_riemann_screw_calibration import riemann_prime_powers


def _prime_base_of_prime_power(n: int) -> int:
    """Return p when n=p^k; input is supplied by riemann_prime_powers."""
    for p in range(2, int(n**0.5) + 2):
        if n % p == 0:
            return p
    return n


def prime_data_mp(a: float = 1.0):
    out = []
    for n, _ in riemann_prime_powers(2.0*a):
        p = _prime_base_of_prime_power(int(n))
        out.append((int(n), mp.log(p) / mp.sqrt(n)))
    return out


def frequency_mp(n: int, a) -> mp.mpf:
    return mp.mpf(n) * mp.pi / (2*a)


def overlap_one_mp(m: int, n: int, t, a) -> mp.mpf:
    """Analytic x-overlap of derivative Dirichlet modes for t>=0."""
    L = 2*a
    A = frequency_mp(m, a)
    B = frequency_mp(n, a)

    def int_cos(w, phase):
        if abs(w) < mp.eps * 100:
            return (L-t) * mp.cos(phase)
        return (mp.sin(w*L + phase) - mp.sin(w*t + phase)) / w

    I = mp.mpf('0.5') * (
        int_cos(A-B, B*t) + int_cos(A+B, -B*t)
    )
    return (A*B/a) * I


def symmetric_overlap_mp(m: int, n: int, t, a) -> mp.mpf:
    return overlap_one_mp(m, n, t, a) + overlap_one_mp(n, m, t, a)


def arch_series_factory(dps: int = 50, nmax: int = 90):
    """High-precision Suzuki pre-(2.2) series, valid for 2a<pi."""
    q = mp.mpf('0.25')
    coeff = [mp.mpf(0), mp.mpf(0)]
    for r in range(2, nmax + 1):
        coeff.append(mp.zeta(2-r, q) * (-2)**r / mp.factorial(r))
    psiq = mp.digamma(q)
    psi2 = mp.digamma(2)
    logpi = mp.log(mp.pi)

    def arch(t):
        t = abs(mp.mpf(t))
        if t == 0:
            return mp.mpf(0)
        poly = mp.mpf(0)
        for r in range(len(coeff)-1, 1, -1):
            poly = (poly + coeff[r]) * t
        poly *= t
        delta = 2*t*(mp.log(2*t) + psiq - psi2) + poly
        return -mp.mpf('0.5')*t*(psiq-logpi) + mp.mpf('0.25')*delta

    return arch


def component_matrices_mp(modes: int = 14, a: float = 1.0, dps: int = 40):
    """Return (pole, prime, arch) matrices at arbitrary precision."""
    if 2*a >= pi:
        raise ValueError('series control currently requires 2a < pi')

    with mp.workdps(dps):
        aa = mp.mpf(str(a))
        L = 2*aa
        pdata = prime_data_mp(a)
        arch = arch_series_factory(dps=dps)
        breakpoints = [mp.mpf(0)] + sorted(mp.log(n) for n, _ in pdata) + [L]

        def pole(t):
            return -4*(mp.e**(t/2) + mp.e**(-t/2) - 2)

        def prime(t):
            return sum(c*max(t-mp.log(n), mp.mpf(0)) for n, c in pdata)

        P = mp.matrix(modes)
        R = mp.matrix(modes)
        H = mp.matrix(modes)
        for i in range(modes):
            for j in range(i, modes):
                m, n = i+1, j+1
                S = lambda t: symmetric_overlap_mp(m, n, t, aa)
                pv = mp.quad(lambda t: pole(t)*S(t), [0, L])
                rv = mp.quad(lambda t: prime(t)*S(t), breakpoints)
                hv = mp.quad(lambda t: arch(t)*S(t), [0, L])
                P[i,j] = P[j,i] = pv
                R[i,j] = R[j,i] = rv
                H[i,j] = H[j,i] = hv
        return P, R, H


def parity_indices_v(modes: int, parity: str) -> list[int]:
    """Parity of v in the direct Dirichlet basis, not parity of u=Dv."""
    if parity == 'even':
        return [j for j in range(modes) if (j+1) % 2 == 1]
    if parity == 'odd':
        return [j for j in range(modes) if (j+1) % 2 == 0]
    raise ValueError("parity must be 'even' or 'odd'")


def spectral_report(modes: int = 14, a: float = 1.0, dps: int = 40) -> dict:
    with mp.workdps(dps):
        P, R, H = component_matrices_mp(modes, a, dps)
        A = P + R + H
        vals, Q = mp.eigsy(A)

        even = parity_indices_v(modes, 'even')
        odd = parity_indices_v(modes, 'odd')
        Ae = mp.matrix([[A[i,j] for j in even] for i in even])
        Ao = mp.matrix([[A[i,j] for j in odd] for i in odd])
        ve, _ = mp.eigsy(Ae)
        vo, _ = mp.eigsy(Ao)

        cancellations = []
        for j in range(min(4, modes)):
            c = Q[:,j]
            rp = (c.T*P*c)[0]
            rr = (c.T*R*c)[0]
            rh = (c.T*H*c)[0]
            cancellations.append({
                'index': j+1,
                'eigenvalue': mp.nstr(vals[j], 20),
                'pole': mp.nstr(rp, 16),
                'prime': mp.nstr(rr, 16),
                'arch': mp.nstr(rh, 16),
            })

        return {
            'modes': modes,
            'dps': dps,
            'lowest': mp.nstr(vals[0], 20),
            'first_eigenvalues': [mp.nstr(vals[j], 20) for j in range(min(8,modes))],
            'even_v_min': mp.nstr(ve[0], 20),
            'odd_v_min': mp.nstr(vo[0], 20),
            'cancellation_diagnostics': cancellations,
        }


def mode_sequence(mode_counts=(6,8,10,12,14,16), dps: int = 36):
    return [spectral_report(m, dps=dps) for m in mode_counts]


if __name__ == '__main__':
    print('Suzuki v13.291 componentwise high-precision audit')
    for row in mode_sequence():
        print(row)
