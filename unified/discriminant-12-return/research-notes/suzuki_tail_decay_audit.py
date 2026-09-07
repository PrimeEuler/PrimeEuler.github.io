#!/usr/bin/env python3
"""Coefficient-tail and H1-tail audit for the Suzuki a=1 kernel candidate.

This v13.296 control continues the parity-reduced v13.295 calculation through
M=20 and asks a more targeted question: is the observed odd-mode tail small
enough to support a plausible H1 limiting picture?

For the even-v candidate

    v(x) = sum_{n odd} c_n psi_n(x),

we have

    ||Dv||_2^2 = sum_{n odd} (n*pi/2)^2 |c_n|^2.

The script reports the observed coefficient tail and cumulative L2/H1 tail
contained in the finite M=20 Ritz vector.  It also computes descriptive
log-linear (exponential) and log-log (power-law) fits on a user-selected tail
window.  These fits are diagnostics only: finite-section coefficient decay is
not a rigorous bound on the infinite tail and does not prove H1 convergence,
ker(G_1) != {0}, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math
import mpmath as mp
import numpy as np

from suzuki_parity_reduced_h1_extension import (
    reduced_even_v_matrix,
    lowest_prefix,
    frequency_mp,
)


def candidate(max_modes: int = 20, a: float = 1.0, dps: int = 36):
    with mp.workdps(dps):
        ns, A = reduced_even_v_matrix(max_modes=max_modes, a=a, dps=dps)
        lam, c = lowest_prefix(ns, A, max_modes)
        return ns[:len(c)], lam, c


def cumulative_tail(ns, c, cutoff: int, a: float = 1.0):
    """Observed finite-vector tail over n>=cutoff."""
    aa = mp.mpf(str(a))
    idx = [j for j, n in enumerate(ns) if n >= cutoff]
    l2_sq = mp.fsum(abs(c[j])**2 for j in idx)
    h1_sq = mp.fsum(
        frequency_mp(ns[j], aa)**2 * abs(c[j])**2 for j in idx
    )
    return mp.sqrt(l2_sq), mp.sqrt(h1_sq)


def tail_fit(ns, c, nmin: int = 11):
    """Descriptive exponential and power fits for |c_n|, n>=nmin."""
    x = np.asarray([float(n) for n in ns if n >= nmin], dtype=float)
    y = np.asarray([
        float(abs(c[j])) for j, n in enumerate(ns) if n >= nmin and abs(c[j]) > 0
    ], dtype=float)
    if len(x) != len(y) or len(x) < 3:
        raise ValueError('tail window needs at least three positive coefficients')
    logy = np.log(y)

    Xe = np.column_stack([np.ones_like(x), x])
    ae, be = np.linalg.lstsq(Xe, logy, rcond=None)[0]
    prede = Xe @ np.array([ae, be])

    Xp = np.column_stack([np.ones_like(x), np.log(x)])
    ap, bp = np.linalg.lstsq(Xp, logy, rcond=None)[0]
    predp = Xp @ np.array([ap, bp])

    ss0 = float(np.sum((logy - np.mean(logy))**2))
    r2e = 1.0 - float(np.sum((logy-prede)**2))/ss0
    r2p = 1.0 - float(np.sum((logy-predp)**2))/ss0
    return {
        'nmin': nmin,
        'points': len(x),
        'exp_log_slope_per_n': float(be),
        'exp_ratio_per_plus_2_modes': float(math.exp(2*be)),
        'exp_R2_log': r2e,
        'power_exponent_p': float(-bp),
        'power_R2_log': r2p,
    }


def report(max_modes: int = 20, a: float = 1.0, dps: int = 36):
    ns, lam, c = candidate(max_modes=max_modes, a=a, dps=dps)
    coeffs = [{'n': n, 'abs_c': abs(c[j]), 'c': c[j]} for j, n in enumerate(ns)]
    tails = []
    for cutoff in (9, 11, 13, 15, 17):
        l2, h1 = cumulative_tail(ns, c, cutoff, a)
        tails.append({'cutoff': cutoff, 'L2_tail': l2, 'H1_tail': h1})
    return {
        'modes': max_modes,
        'ritz_value': lam,
        'coefficients': coeffs,
        'tail_fit_n_ge_11': tail_fit(ns, c, nmin=11),
        'observed_cumulative_tails': tails,
    }


def print_report():
    r = report()
    print('Suzuki v13.296 coefficient-tail audit')
    print('M=', r['modes'], 'lambda=', mp.nstr(r['ritz_value'], 24))
    print('coefficients')
    for q in r['coefficients']:
        print(q['n'], mp.nstr(q['c'], 20), 'abs=', mp.nstr(q['abs_c'], 12))
    print('descriptive fit n>=11')
    print(r['tail_fit_n_ge_11'])
    print('observed finite-vector cumulative tails')
    for q in r['observed_cumulative_tails']:
        print(q['cutoff'], 'L2=', mp.nstr(q['L2_tail'], 16),
              'H1=', mp.nstr(q['H1_tail'], 16))


if __name__ == '__main__':
    print_report()
