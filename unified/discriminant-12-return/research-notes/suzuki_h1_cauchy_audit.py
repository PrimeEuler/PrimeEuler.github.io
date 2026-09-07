#!/usr/bin/env python3
"""H1 / derivative-norm convergence audit for the Suzuki a=1 kernel candidate.

This v13.294 control continues v13.293.  The direct Dirichlet basis is
orthonormal in L2 and diagonalizes the derivative seminorm:

    psi_n(x) = a^{-1/2} sin(n*pi*(x+a)/(2a)),
    ||Dv||_2^2 = sum_n k_n^2 |c_n|^2,
    k_n = n*pi/(2a).

For nested Ritz vectors v_M and v_N, after a consistent sign alignment,

    ||v_N-v_M||_2^2 = sum_n |dc_n|^2,
    ||D(v_N-v_M)||_2^2 = sum_n k_n^2 |dc_n|^2.

The corresponding u_M=Dv_M has exactly these derivative coefficients.  Thus
strong H1 convergence of v_M is equivalent to strong L2 convergence of u_M.

This is a numerical compactness audit only.  Bounded derivative norms do not
prove convergence, ker(G_1) != {0}, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import mpmath as mp

from suzuki_kernel_candidate_reconstruction import lowest_candidate


def frequencies(modes: int, a=1):
    aa = mp.mpf(a)
    return [mp.mpf(n) * mp.pi / (2*aa) for n in range(1, modes+1)]


def l2_norm(c):
    return mp.sqrt(mp.fsum(abs(c[j])**2 for j in range(len(c))))


def derivative_norm(c, a=1):
    k = frequencies(len(c), a)
    return mp.sqrt(mp.fsum(k[j]**2 * abs(c[j])**2 for j in range(len(c))))


def sign_aligned_difference(c0, c1):
    """Embed c0 in c1-space and choose the sign of c1 maximizing overlap."""
    z = mp.matrix(len(c1), 1)
    for j in range(len(c0)):
        z[j] = c0[j]
    overlap = (z.T*c1)[0]
    s = mp.mpf(1) if overlap >= 0 else mp.mpf(-1)
    return s*c1 - z


def cauchy_step(c0, c1, a=1):
    d = sign_aligned_difference(c0, c1)
    return {
        'L2_difference': l2_norm(d),
        'derivative_difference': derivative_norm(d, a),
        'larger_derivative_norm': derivative_norm(c1, a),
        'relative_u_difference': derivative_norm(d, a) / derivative_norm(c1, a),
    }


def sequence(mode_counts=(6,8,10,12,14), a=1, dps=50):
    with mp.workdps(dps):
        candidates = {}
        rows = []
        for M in mode_counts:
            lam, c, _, _, _ = lowest_candidate(M, a=a, dps=dps)
            candidates[M] = c
            rows.append({
                'modes': M,
                'ritz_value': lam,
                'L2_norm': l2_norm(c),
                'derivative_norm': derivative_norm(c, a),
            })

        steps = []
        for M0, M1 in zip(mode_counts[:-1], mode_counts[1:]):
            row = {'from_modes': M0, 'to_modes': M1}
            row.update(cauchy_step(candidates[M0], candidates[M1], a))
            steps.append(row)
        return rows, steps


def print_report():
    print('Suzuki v13.294 H1 Cauchy audit')
    rows, steps = sequence()
    print('candidate norms')
    for row in rows:
        print(row['modes'],
              'lambda=', mp.nstr(row['ritz_value'], 20),
              'L2=', mp.nstr(row['L2_norm'], 16),
              'D=', mp.nstr(row['derivative_norm'], 16))
    print('successive nested differences')
    for row in steps:
        print(row['from_modes'], row['to_modes'],
              'L2diff=', mp.nstr(row['L2_difference'], 16),
              'Ddiff=', mp.nstr(row['derivative_difference'], 16),
              'relative_u_diff=', mp.nstr(row['relative_u_difference'], 16))


if __name__ == '__main__':
    print_report()
