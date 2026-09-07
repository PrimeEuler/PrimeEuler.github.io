#!/usr/bin/env python3
"""Reconstruct the v13.292 near-null candidate and audit projected cancellation.

This v13.293 control takes the high-precision lowest Ritz vectors from the
componentwise Suzuki matrix and studies the candidate itself.  The even
Dirichlet sector at a=1 consists of odd n, and

    psi_(2j+1)(x) = (-1)^j cos((2j+1) pi x / 2).

The script therefore reports both Dirichlet coefficients and phase-corrected
ordinary cosine amplitudes, tracks stabilization across nested mode counts,
and evaluates the pole/prime/archimedean action vectors separately.

The key diagnostic is stronger than a small Rayleigh quotient: if c_M is a
projected kernel candidate, then

    (A_pole + A_prime + A_arch) c_M

should be small entrywise, while the three component action vectors may remain
O(1).  This remains numerical evidence, not a proof of ker(G_1) != {0}, RH, or
GRH.
"""
from __future__ import annotations

import mpmath as mp
import numpy as np

from suzuki_componentwise_high_precision_audit import component_matrices_mp


def lowest_candidate(modes: int = 14, a: float = 1.0, dps: int = 50):
    """Return high-precision lowest Ritz value and coefficient vector."""
    with mp.workdps(dps):
        P, R, H = component_matrices_mp(modes, a=a, dps=dps)
        A = P + R + H
        vals, Q = mp.eigsy(A)
        c = Q[:, 0]
        # Deterministic sign: largest coefficient positive.
        j = max(range(modes), key=lambda k: abs(c[k]))
        if c[j] < 0:
            c = -c
        return vals[0], c, P, R, H


def odd_sector_coefficients(c):
    """Report the even-v sector in Dirichlet and ordinary cosine conventions."""
    rows = []
    for j in range(0, len(c), 2):
        n = j + 1
        phase = -1 if ((n - 1) // 2) % 2 else 1
        rows.append({
            'n': n,
            'dirichlet': c[j],
            'cosine_amplitude': phase * c[j],
        })
    return rows


def embedded_overlap(c0, c1):
    """Absolute overlap after embedding the smaller coefficient vector."""
    z = mp.matrix(len(c1), 1)
    for j in range(len(c0)):
        z[j] = c0[j]
    n0 = mp.sqrt((z.T*z)[0])
    n1 = mp.sqrt((c1.T*c1)[0])
    return abs((z.T*c1)[0])/(n0*n1)


def component_action_report(modes: int = 14, a: float = 1.0, dps: int = 50):
    with mp.workdps(dps):
        lam, c, P, R, H = lowest_candidate(modes, a, dps)
        yp, yr, yh = P*c, R*c, H*c
        y = yp + yr + yh
        rows = []
        for j in range(0, modes, 2):
            rows.append({
                'n': j+1,
                'pole': yp[j],
                'prime': yr[j],
                'arch': yh[j],
                'sum': y[j],
            })
        return {
            'modes': modes,
            'ritz_value': lam,
            'coefficients': odd_sector_coefficients(c),
            'action_norms': {
                'pole': mp.norm(yp),
                'prime': mp.norm(yr),
                'arch': mp.norm(yh),
                'sum': mp.norm(y),
            },
            'mode_actions': rows,
        }


def stabilization_report(mode_counts=(6, 8, 10, 12, 14), a: float = 1.0,
                         dps: int = 50):
    candidates = {}
    rows = []
    for modes in mode_counts:
        lam, c, _, _, _ = lowest_candidate(modes, a, dps)
        candidates[modes] = c
        rows.append({
            'modes': modes,
            'ritz_value': lam,
            'coefficients': odd_sector_coefficients(c),
        })

    overlaps = []
    for m0, m1 in zip(mode_counts[:-1], mode_counts[1:]):
        overlaps.append({
            'from_modes': m0,
            'to_modes': m1,
            'embedded_overlap': embedded_overlap(candidates[m0], candidates[m1]),
        })
    return rows, overlaps


def print_report():
    print('Suzuki v13.293 kernel-candidate reconstruction')
    rows, overlaps = stabilization_report()
    for row in rows:
        print('M=', row['modes'], 'lambda=', mp.nstr(row['ritz_value'], 25))
        for q in row['coefficients']:
            print(' ', q['n'], mp.nstr(q['dirichlet'], 18),
                  mp.nstr(q['cosine_amplitude'], 18))
    print('embedded overlaps')
    for row in overlaps:
        print(row['from_modes'], row['to_modes'], mp.nstr(row['embedded_overlap'], 18))

    action = component_action_report()
    print('M=14 action norms')
    for key, value in action['action_norms'].items():
        print(key, mp.nstr(value, 18))
    print('entrywise component cancellation')
    for row in action['mode_actions']:
        print(row['n'], *(mp.nstr(row[k], 16) for k in ('pole','prime','arch','sum')))


if __name__ == '__main__':
    print_report()
