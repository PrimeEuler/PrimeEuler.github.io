#!/usr/bin/env python3
"""Asymptotic matrix anatomy for Suzuki's a=1 even-v sector.

This v13.298 audit separates the high-mode matrix into three structural pieces:

  1. the local archimedean cusp s(t)=1/2 t log t + A t,
  2. the finite prime-power ramp sum,
  3. the smooth pole + archimedean remainder.

For odd Dirichlet mode n with k_n=n*pi/2, the symmetric self-overlap is

    S_nn(t)=k_n^2 (2-t) cos(k_n t) - k_n sin(k_n t).

For one ramp h_l(t)=(t-l)_+, direct integration gives exactly

    int_l^2 h_l(t) S_nn(t) dt
      = (l-2) cos(k_n l) - sin(k_n l)/k_n.

Thus every prime-power kink contributes only an O(1) oscillatory diagonal term.
Equivalently, after two integrations by parts on H_0^1,

    Q_l(v) = - int v(x) [v(x-l)+v(x+l)] dx

with the shifts truncated to [-1,1], so each ramp defines a bounded L2 operator
of norm at most 2.  At a=1 only the five kinks log(2), log(3), log(4),
log(5), log(7) occur.

The local cusp diagonal is evaluated at high precision and compared against
log(n)-log(4).  Numerically its error decays to zero, while the smooth pole and
archimedean remainder decay.  This supports the tail model

    A_even = diag(log n - log 4) + B_prime + K,

where B_prime is bounded and K is lower order.  This script is an asymptotic
numerical/theoretical audit, not a proof of the required infinite-tail lower
bound, ker(G_1) != {0}, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math
import mpmath as mp

from suzuki_componentwise_high_precision_audit import (
    arch_series_factory,
    frequency_mp,
    prime_data_mp,
    symmetric_overlap_mp,
)


def local_cusp(t):
    t = abs(mp.mpf(t))
    if t == 0:
        return mp.mpf(0)
    A = mp.mpf('0.5') * (mp.log(2*mp.pi) + mp.euler - 1)
    return mp.mpf('0.5')*t*mp.log(t) + A*t


def ramp_diagonal_exact(n: int, ell, a=1):
    if a != 1:
        raise NotImplementedError('closed form here is specialized to a=1')
    k = frequency_mp(n, mp.mpf(1))
    ell = mp.mpf(ell)
    return (ell-2)*mp.cos(k*ell) - mp.sin(k*ell)/k


def prime_diagonal_exact(n: int):
    total = mp.mpf(0)
    for q, weight in prime_data_mp(1.0):
        total += weight * ramp_diagonal_exact(n, mp.log(q))
    return total


def diagonal_components(n: int, dps: int = 50):
    if n % 2 == 0:
        raise ValueError('use odd n for the even-v sector')
    with mp.workdps(dps):
        arch = arch_series_factory(dps=dps)
        S = lambda t: symmetric_overlap_mp(n, n, t, mp.mpf(1))
        cusp = mp.quad(lambda t: local_cusp(t)*S(t), [0,2])
        archv = mp.quad(lambda t: arch(t)*S(t), [0,2])
        pole = mp.quad(
            lambda t: -4*(mp.e**(t/2)+mp.e**(-t/2)-2)*S(t), [0,2]
        )
        prime = prime_diagonal_exact(n)
        model = mp.log(n) - mp.log(4)
        return {
            'n': n,
            'cusp': cusp,
            'log_model': model,
            'cusp_minus_log_model': cusp-model,
            'arch': archv,
            'arch_minus_cusp': archv-cusp,
            'pole': pole,
            'prime': prime,
            'full': archv + pole + prime,
        }


def prime_operator_norm_bound():
    """Triangle-inequality L2 norm bound for the finite prime-ramp operator."""
    weights = [weight for _, weight in prime_data_mp(1.0)]
    return 2*mp.fsum(weights)


def report(ns=(9,11,13,15,17,19,21,25,31,41,61), dps=50):
    return {
        'rows': [diagonal_components(n, dps=dps) for n in ns],
        'prime_kinks': [q for q,_ in prime_data_mp(1.0)],
        'prime_operator_norm_bound': prime_operator_norm_bound(),
    }


def print_report():
    r = report()
    print('Suzuki v13.298 asymptotic matrix anatomy')
    print('prime kinks:', r['prime_kinks'])
    print('prime operator norm triangle bound:', mp.nstr(r['prime_operator_norm_bound'], 16))
    for q in r['rows']:
        print(q['n'],
              'cusp=', mp.nstr(q['cusp'], 14),
              'cusp-log=', mp.nstr(q['cusp_minus_log_model'], 10),
              'arch-cusp=', mp.nstr(q['arch_minus_cusp'], 10),
              'pole=', mp.nstr(q['pole'], 10),
              'prime=', mp.nstr(q['prime'], 10),
              'full=', mp.nstr(q['full'], 12))


if __name__ == '__main__':
    print_report()
