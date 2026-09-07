#!/usr/bin/env python3
"""Archimedean remainder regularity / bounded-operator audit for Suzuki a=1.

This v13.299 control isolates the local singular model

    s(t) = 1/2 t log t + A t,
    A = 1/2 (log(2*pi) + gamma - 1),

from Suzuki's archimedean contribution and writes

    g_arch(t) = s(t) + r(t).

Using the convergent pre-(2.2) series on 0 <= t <= 2 < pi,

    r(t) = 1/4 sum_{m>=2} zeta(2-m,1/4) (-2)^m t^m / m!.

Thus r(0)=r'(0)=0.  For v in H_0^1(-1,1), two integrations by parts give

    int int v'(x) r(|x-y|) v'(y) dx dy
      = - int int v(x) r''(|x-y|) v(y) dx dy,

with NO delta term at x=y because r'(0)=0.  Therefore the remainder defines
an ordinary bounded L2 integral operator with kernel -r''(|x-y|).

The script evaluates a convergent-series L1 majorant

    int_0^2 |r''(t)| dt
      <= sum_{m>=2} |a_m| m 2^(m-1),

where a_m is the coefficient of t^m in r.  The finite truncation reported here
is a numerical evaluation of a convergent majorant; it is not interval-certified
and does not by itself prove the infinite-tail coercivity statement, ker(G_1)
!= {0}, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import mpmath as mp


def remainder_coefficient(m: int):
    if m < 2:
        return mp.mpf(0)
    q = mp.mpf('0.25')
    return (mp.mpf('0.25') * mp.zeta(2-m, q) * (-2)**m / mp.factorial(m))


def remainder_series(t, nmax: int = 90):
    t = mp.mpf(t)
    return mp.fsum(remainder_coefficient(m) * t**m for m in range(2, nmax+1))


def remainder_second_derivative(t, nmax: int = 90):
    t = mp.mpf(t)
    return mp.fsum(
        remainder_coefficient(m) * m * (m-1) * t**(m-2)
        for m in range(2, nmax+1)
    )


def l1_majorant(nmax: int = 90):
    """Series triangle majorant for int_0^2 |r''(t)| dt."""
    return mp.fsum(
        abs(remainder_coefficient(m)) * m * 2**(m-1)
        for m in range(2, nmax+1)
    )


def crude_schur_bound(nmax: int = 90):
    """Safe symmetric-interval row bound using two copies of [0,2]."""
    return 2 * l1_majorant(nmax=nmax)


def pole_operator_bound():
    """Schur bound after two integrations by parts for the smooth pole term.

    p(t)=-8(cosh(t/2)-1), so -p''(t)=2 cosh(t/2).  The maximal row integral
    over [-1,1] is attained at an endpoint and equals 4 sinh(1).
    """
    return 4 * mp.sinh(1)


def report(dps: int = 60, nmax: int = 90):
    with mp.workdps(dps):
        samples = []
        for t in (0, mp.mpf('0.5'), 1, mp.mpf('1.5'), 2):
            samples.append({
                't': t,
                'r_second': remainder_second_derivative(t, nmax=nmax),
            })
        tail_terms = []
        for m in (10,20,30,40,50,60,70,80,90):
            if m <= nmax:
                tail_terms.append({
                    'm': m,
                    'majorant_term': abs(remainder_coefficient(m))*m*2**(m-1),
                })
        return {
            'nmax': nmax,
            'r0': remainder_series(0, nmax=nmax),
            'r1_at_0': mp.mpf(0),
            'second_derivative_samples': samples,
            'l1_series_majorant_0_to_2': l1_majorant(nmax=nmax),
            'crude_schur_bound_arch_remainder': crude_schur_bound(nmax=nmax),
            'pole_schur_bound': pole_operator_bound(),
            'combined_smooth_bound': crude_schur_bound(nmax=nmax) + pole_operator_bound(),
            'selected_majorant_terms': tail_terms,
        }


def print_report():
    r = report()
    print('Suzuki v13.299 archimedean remainder bounded-operator audit')
    print('nmax=', r['nmax'])
    print('r(0)=', mp.nstr(r['r0'], 16), "r'(0)=0 exactly from series start m=2")
    print('r_second samples')
    for q in r['second_derivative_samples']:
        print(mp.nstr(q['t'], 8), mp.nstr(q['r_second'], 18))
    print('L1 majorant=', mp.nstr(r['l1_series_majorant_0_to_2'], 18))
    print('arch crude Schur=', mp.nstr(r['crude_schur_bound_arch_remainder'], 18))
    print('pole Schur=', mp.nstr(r['pole_schur_bound'], 18))
    print('combined smooth=', mp.nstr(r['combined_smooth_bound'], 18))
    print('selected majorant terms')
    for q in r['selected_majorant_terms']:
        print(q['m'], mp.nstr(q['majorant_term'], 12))


if __name__ == '__main__':
    print_report()
