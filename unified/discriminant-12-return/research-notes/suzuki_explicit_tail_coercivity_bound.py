#!/usr/bin/env python3
"""Explicit infinite-tail coercivity bound for Suzuki a=1 even-v sector.

This v13.303 control combines the rigorous decomposition

    A_even = D_log - H_odd + K_cusp + B_prime + K_smooth,

with explicit norm bounds.  Here

    (D_log)_nn = log(n/4),
    ||H_odd|| = pi/2,

B_prime is the finite prime-shift operator from v13.298, K_smooth is the
bounded pole+archimedean remainder from v13.299, and K_cusp is the
Hilbert-Schmidt cusp correction proved in v13.302.

The cusp HS bound below is deliberately elementary and conservative.  It uses

    K_mn = -2/(pi^2 m n) + E_mn,  m != n,

with the v13.302 remainder estimate

    |E_mn| <= (2/pi) (n d_m + m d_n)/|m^2-n^2|,
    d_j <= c/j^3,
    c = 2/pi^3 + 6/pi^4,

plus |m-n| >= 2 for distinct odd indices.  The diagonal is bounded by a
constant times n^-2.  These estimates yield a global HS bound < 0.706.

Hence on the odd-mode tail n>=N,

    <A_even c,c> >= [log(N/4)-C_pert] ||c||^2.

The resulting N is extremely conservative (millions of modes) because it uses
global triangle-inequality bounds rather than tail-localized norms.  It is an
explicit infinite-tail coercivity statement for this sector, not a proof of
ker(G_1)!={0}, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math


def cusp_hs_bound():
    # Rank-one leading term -2/(pi^2 mn) on odd positive indices.
    # Sum_{n odd} 1/n^2 = pi^2/8, so HS norm = (2/pi^2)*(pi^2/8)=1/4.
    rank_one = 0.25

    # d_j <= c/j^3.
    c = 2.0/math.pi**3 + 6.0/math.pi**4
    alpha = 2.0*c/math.pi

    # From |E_mn| <= alpha[1/(m^3|m-n|)+1/(n^3|m-n|)] and
    # (a+b)^2 <= 2(a^2+b^2), summing over distinct odd m,n gives
    # ||E||_HS^2 <= 4 alpha^2 (pi^2/12) Sum_{m odd} 1/m^6.
    # Sum_{m odd} 1/m^6 = pi^6/960.
    offdiag_error = math.sqrt(
        4.0*alpha**2*(math.pi**2/12.0)*(math.pi**6/960.0)
    )

    # Diagonal v13.302 bound:
    # |K_nn| <= 2/x^2+2/x^3+2/x^4+6/x^5, x=pi n.
    # For n>=1 this is <= C_diag/n^2.
    C_diag = (
        2.0/math.pi**2 + 2.0/math.pi**3 +
        2.0/math.pi**4 + 6.0/math.pi**5
    )
    # Sum_{n odd} 1/n^4 = pi^4/96.
    diagonal = C_diag*math.sqrt(math.pi**4/96.0)

    return {
        'rank_one_hs': rank_one,
        'offdiag_error_hs_bound': offdiag_error,
        'diagonal_hs_bound': diagonal,
        'global_cusp_hs_bound': rank_one + offdiag_error + diagonal,
    }


def perturbation_bound():
    cusp = cusp_hs_bound()['global_cusp_hs_bound']
    hilbert = math.pi/2.0

    # v13.298 exact triangle/operator bound, numerically evaluated.
    prime = 5.85247

    # v13.299: arch remainder Schur ~1.31476 and pole Schur ~4.70080.
    smooth = 1.31476 + 4.70080

    total = hilbert + prime + smooth + cusp
    return {
        'hilbert_bound': hilbert,
        'prime_bound': prime,
        'smooth_bound': smooth,
        'cusp_bound': cusp,
        'total_perturbation_bound': total,
    }


def coercive_cutoff():
    p = perturbation_bound()
    C = p['total_perturbation_bound']
    real_threshold = 4.0*math.exp(C)
    N = math.floor(real_threshold) + 1
    if N % 2 == 0:
        N += 1
    margin = math.log(N/4.0) - C
    return {
        'continuous_threshold': real_threshold,
        'first_reported_odd_cutoff': N,
        'coercivity_margin_at_cutoff': margin,
        **p,
        **cusp_hs_bound(),
    }


def print_report():
    r = coercive_cutoff()
    print('Suzuki v13.303 explicit infinite-tail coercivity bound')
    for k,v in r.items():
        print(k, '=', v)
    print('tail inequality: <A c,c> >= [log(N/4)-Cpert] ||c||^2')
    print('guardrail: this is a high-tail coercivity bound only; no RH/GRH claim')


if __name__ == '__main__':
    print_report()
