#!/usr/bin/env python3
"""High-mode projected-equation / tail-resolvent audit for Suzuki's a=1 candidate.

This v13.297 control continues v13.296.  Rather than fitting coefficient decay,
it partitions the parity-reduced even-v Ritz matrix as

    [ A_LL  B^T ] [c_L] = lambda [c_L]
    [ B     T_N ] [c_T]          [c_T]

for an odd-mode cutoff N.  For the near-zero candidate this gives, up to the tiny
finite Ritz value,

    T_N c_T = -B c_L,

so whenever T_N is invertible,

    c_T = -T_N^{-1} B c_L,
    ||c_T|| <= ||T_N^{-1}|| ||B c_L||.

The purpose is to identify whether the observed rapid coefficient tail is forced
by the high-mode projected equation and whether a plausible infinite-tail
resolvent estimate exists.  All bounds reported here are FINITE-SECTION bounds.
They do not prove a lower bound for the infinite tail operator, H1 convergence,
ker(G_1) != {0}, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import math
import mpmath as mp
import numpy as np

from suzuki_parity_reduced_h1_extension import reduced_even_v_matrix, lowest_prefix


def matrix_and_candidate(max_modes: int = 20, a: float = 1.0, dps: int = 36):
    with mp.workdps(dps):
        ns, A = reduced_even_v_matrix(max_modes=max_modes, a=a, dps=dps)
        lam, c = lowest_prefix(ns, A, max_modes)
        Af = np.asarray([[float(A[i,j]) for j in range(len(ns))]
                         for i in range(len(ns))], dtype=float)
        cf = np.asarray([float(c[j]) for j in range(len(c))], dtype=float)
        return ns[:len(c)], float(lam), Af, cf


def row_balance(ns, A, c, n: int):
    i = ns.index(n)
    diag = A[i,i]
    earlier = float(A[i,:i] @ c[:i]) if i else 0.0
    later = float(A[i,i+1:] @ c[i+1:]) if i+1 < len(c) else 0.0
    forcing = earlier + later
    predicted = -forcing/diag
    residual = float(A[i,:] @ c)
    return {
        'n': n,
        'diagonal': diag,
        'coefficient': c[i],
        'predicted_from_row': predicted,
        'earlier_mode_forcing': earlier,
        'later_mode_forcing': later,
        'row_residual': residual,
    }


def tail_block_report(ns, A, c, cutoff: int, a: float = 1.0):
    tail = [i for i,n in enumerate(ns) if n >= cutoff]
    low = [i for i,n in enumerate(ns) if n < cutoff]
    T = A[np.ix_(tail, tail)]
    B = A[np.ix_(tail, low)]
    rhs = B @ c[low]
    s = np.linalg.svd(T, compute_uv=False)
    sigma_min = float(s[-1])
    sigma_max = float(s[0])
    predicted = -np.linalg.solve(T, rhs)
    actual = c[tail]
    l2_bound = float(np.linalg.norm(rhs)/sigma_min)
    n_tail = np.asarray([ns[i] for i in tail], dtype=float)
    kvals = n_tail*math.pi/(2*a)
    return {
        'cutoff': cutoff,
        'tail_dimension': len(tail),
        'sigma_min': sigma_min,
        'sigma_max': sigma_max,
        'condition_number': sigma_max/sigma_min,
        'forcing_L2': float(np.linalg.norm(rhs)),
        'actual_tail_L2': float(np.linalg.norm(actual)),
        'finite_resolvent_L2_bound': l2_bound,
        'solve_reconstruction_error': float(np.linalg.norm(predicted-actual)),
        'actual_tail_H1': float(np.linalg.norm(kvals*actual)),
        # Crude finite-dimensional conversion only; not an infinite H1 bound.
        'crude_finite_H1_bound': float(np.max(kvals)*l2_bound),
    }


def report(max_modes: int = 20, a: float = 1.0, dps: int = 36):
    ns, lam, A, c = matrix_and_candidate(max_modes, a, dps)
    rows = [row_balance(ns, A, c, n) for n in ns if n >= 9]
    blocks = [tail_block_report(ns, A, c, cutoff, a)
              for cutoff in (9,11,13,15,17)]
    return {
        'modes': max_modes,
        'ritz_value': lam,
        'high_mode_rows': rows,
        'tail_blocks': blocks,
    }


def print_report():
    r = report()
    print('Suzuki v13.297 high-mode resolvent audit')
    print('M=', r['modes'], 'lambda=', f"{r['ritz_value']:.16e}")
    print('row balances')
    for q in r['high_mode_rows']:
        print(q)
    print('tail blocks')
    for q in r['tail_blocks']:
        print(q)


if __name__ == '__main__':
    print_report()
