#!/usr/bin/env python3
"""Parity-reduced H1 extension of the Suzuki a=1 kernel-candidate audit.

This v13.295 control works directly in the even-v Dirichlet sector.  At a=1,
even v corresponds to odd Dirichlet indices n=1,3,5,... .  Building only this
block roughly halves the dimension and allows the nested Ritz sequence to be
extended efficiently to M=20.

The script assembles the largest requested odd-index block once at arbitrary
precision and obtains all smaller mode counts as principal submatrices.  It
then reports lowest Ritz values, derivative norms, and successive L2/H1
Cauchy differences.

Numerical convergence of these finite sections is evidence only.  It does not
prove strong H1 convergence, ker(G_1) != {0}, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import mpmath as mp

from suzuki_componentwise_high_precision_audit import (
    arch_series_factory,
    frequency_mp,
    prime_data_mp,
    symmetric_overlap_mp,
)


def reduced_even_v_matrix(max_modes: int = 20, a: float = 1.0, dps: int = 36):
    """Build the odd-index/even-v block through max_modes once."""
    if max_modes < 2:
        raise ValueError("max_modes must be at least 2")
    with mp.workdps(dps):
        aa = mp.mpf(str(a))
        L = 2 * aa
        ns = list(range(1, max_modes + 1, 2))
        pdata = prime_data_mp(a)
        breaks = [mp.mpf(0)] + sorted(mp.log(n) for n, _ in pdata) + [L]
        arch = arch_series_factory(dps=dps)

        def pole(t):
            return -4 * (mp.e**(t/2) + mp.e**(-t/2) - 2)

        def prime(t):
            return mp.fsum(c * max(t-mp.log(n), mp.mpf(0)) for n, c in pdata)

        A = mp.matrix(len(ns))
        for i, m in enumerate(ns):
            for j in range(i, len(ns)):
                n = ns[j]
                S = lambda t: symmetric_overlap_mp(m, n, t, aa)
                val = mp.quad(lambda t: pole(t)*S(t), [0, L])
                val += mp.quad(lambda t: prime(t)*S(t), breaks)
                val += mp.quad(lambda t: arch(t)*S(t), [0, L])
                A[i, j] = A[j, i] = val
        return ns, A


def lowest_prefix(ns, A, modes: int):
    """Lowest normalized candidate in the even-v prefix associated with modes."""
    k = (modes + 1) // 2
    B = mp.matrix([[A[i, j] for j in range(k)] for i in range(k)])
    vals, Q = mp.eigsy(B)
    c = Q[:, 0]
    j = max(range(k), key=lambda r: abs(c[r]))
    if c[j] < 0:
        c = -c
    return vals[0], c


def derivative_norm(ns, c, a=1):
    aa = mp.mpf(str(a))
    return mp.sqrt(mp.fsum(
        frequency_mp(ns[j], aa)**2 * abs(c[j])**2 for j in range(len(c))
    ))


def nested_difference(ns, c0, c1, a=1):
    overlap = mp.fsum(c0[j]*c1[j] for j in range(len(c0)))
    sign = mp.mpf(1) if overlap >= 0 else mp.mpf(-1)
    d = []
    for j in range(len(c1)):
        old = c0[j] if j < len(c0) else mp.mpf(0)
        d.append(sign*c1[j] - old)
    l2 = mp.sqrt(mp.fsum(x*x for x in d))
    aa = mp.mpf(str(a))
    h1 = mp.sqrt(mp.fsum(
        frequency_mp(ns[j], aa)**2 * d[j]**2 for j in range(len(d))
    ))
    return abs(overlap), l2, h1


def sequence(mode_counts=(6,8,10,12,14,16,18,20), a=1, dps=36):
    with mp.workdps(dps):
        ns, A = reduced_even_v_matrix(max(mode_counts), a=a, dps=dps)
        candidates = {}
        rows = []
        for M in mode_counts:
            lam, c = lowest_prefix(ns, A, M)
            candidates[M] = c
            rows.append({
                'modes': M,
                'ritz_value': lam,
                'derivative_norm': derivative_norm(ns, c, a),
                'coefficients': [c[j] for j in range(len(c))],
            })

        steps = []
        for M0, M1 in zip(mode_counts[:-1], mode_counts[1:]):
            ov, l2, h1 = nested_difference(ns, candidates[M0], candidates[M1], a)
            d1 = derivative_norm(ns, candidates[M1], a)
            steps.append({
                'from_modes': M0,
                'to_modes': M1,
                'embedded_overlap': ov,
                'L2_difference': l2,
                'derivative_difference': h1,
                'relative_u_difference': h1/d1,
            })
        return rows, steps


def print_report():
    print('Suzuki v13.295 parity-reduced H1 extension')
    rows, steps = sequence()
    print('candidate sequence')
    for r in rows:
        print(r['modes'],
              'lambda=', mp.nstr(r['ritz_value'], 20),
              'D=', mp.nstr(r['derivative_norm'], 16))
    print('nested differences')
    for r in steps:
        print(r['from_modes'], r['to_modes'],
              'overlap=', mp.nstr(r['embedded_overlap'], 16),
              'L2diff=', mp.nstr(r['L2_difference'], 16),
              'Ddiff=', mp.nstr(r['derivative_difference'], 16),
              'relative_u_diff=', mp.nstr(r['relative_u_difference'], 16))


if __name__ == '__main__':
    print_report()
