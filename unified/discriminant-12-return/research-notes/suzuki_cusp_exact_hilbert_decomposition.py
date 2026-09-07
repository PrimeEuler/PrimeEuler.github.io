#!/usr/bin/env python3
"""Exact cusp Si/Ci formula and Hilbert-decomposition audit for Suzuki a=1.

This v13.301 control supersedes the compact-tail interpretation of v13.300.
For odd Dirichlet indices m,n (the even-v sector), let

    C_mn = int_0^2 [1/2 t log t + A t] S_mn(t) dt,
    A = 1/2(log(2*pi)+gamma-1).

For m != n, the odd-mode overlap simplifies exactly to

    S_mn(t) = 2 a b [b sin(b t)-a sin(a t)]/(a^2-b^2),
    a=m*pi/2, b=n*pi/2.

Using

    int_0^2 t log(t) sin(k t) dt
      = [-(2 k cos 2k - sin 2k)log2 + sin 2k - Si(2k)]/k^2,

and sin(n*pi)=0, cos(n*pi)=-1 for odd n, one obtains

    C_mn = (2/pi) [n Si(m*pi)-m Si(n*pi)]/(m^2-n^2),   m != n.

On the diagonal,

    C_nn = log(n/4) - Ci(n*pi) - Si(n*pi)/(n*pi).

Therefore the first non-diagonal asymptotic is NOT compact.  Since
Si(n*pi)=pi/2 + 1/(n*pi)+O(n^-3) for odd n,

    C_mn = -1/(m+n) + lower order,
    C_nn-log(n/4) = -1/(2n) + lower order.

Thus the correct leading model is

    C = D_log - H_odd + K,
    (D_log)_nn = log(n/4),
    (H_odd)_mn = 1/(m+n).

Under m=2j+1, n=2k+1, H_odd is exactly one half of the classical Hilbert
matrix, hence ||H_odd|| = pi/2 on l2.  The residual K is audited numerically
for Hilbert-Schmidt stabilization and high-mode tail decay.  The numerical
HS evidence does not replace a uniform analytic remainder estimate.

No RH/GRH, kernel, or lambda_1=0 conclusion follows from this script.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.special import sici


def cusp_exact(m: int, n: int) -> float:
    if m % 2 == 0 or n % 2 == 0:
        raise ValueError('use odd m,n for the even-v sector')
    if m == n:
        si, ci = sici(n*math.pi)
        return math.log(n/4.0) - ci - si/(n*math.pi)
    sim, _ = sici(m*math.pi)
    sin, _ = sici(n*math.pi)
    return (2.0/math.pi) * (n*sim - m*sin)/(m*m-n*n)


def hilbert_odd(m: int, n: int) -> float:
    return 1.0/(m+n)


def compact_candidate_entry(m: int, n: int) -> float:
    """K = C-D_log+H_odd."""
    d = math.log(n/4.0) if m == n else 0.0
    return cusp_exact(m,n) - d + hilbert_odd(m,n)


def residual_matrix(odd_modes: int):
    ns = list(range(1,2*odd_modes,2))
    K = np.array([[compact_candidate_entry(m,n) for n in ns] for m in ns],
                 dtype=float)
    return ns, K


def size_sequence(sizes=(10,20,40,80,160,320)):
    rows=[]
    for N in sizes:
        ns,K=residual_matrix(N)
        rows.append({
            'odd_modes':N,
            'max_n':ns[-1],
            'frobenius_HS_partial':float(np.linalg.norm(K,'fro')),
            'spectral_norm_partial':float(np.linalg.norm(K,2)),
        })
    return rows


def tail_sequence(max_n: int = 999, cutoffs=(1,11,21,41,81,161)):
    all_ns=list(range(1,max_n+1,2))
    rows=[]
    for cutoff in cutoffs:
        ns=[n for n in all_ns if n>=cutoff]
        K=np.array([[compact_candidate_entry(m,n) for n in ns] for m in ns],
                   dtype=float)
        rows.append({
            'cutoff':cutoff,
            'dimension':len(ns),
            'HS_tail_partial':float(np.linalg.norm(K,'fro')),
            'spectral_tail_partial':float(np.linalg.norm(K,2)),
        })
    return rows


def asymptotic_samples(pairs=((31,33),(31,41),(101,103),(201,203))):
    rows=[]
    for m,n in pairs:
        k=compact_candidate_entry(m,n)
        model=-2.0/(math.pi**2*m*n)
        rows.append({'m':m,'n':n,'Kmn':k,'rank1_model':model,'ratio':k/model})
    return rows


def report():
    return {
        'hilbert_odd_operator_norm_exact': math.pi/2.0,
        'size_sequence': size_sequence(),
        'tail_sequence': tail_sequence(),
        'asymptotic_samples': asymptotic_samples(),
    }


def print_report():
    r=report()
    print('Suzuki v13.301 exact cusp / Hilbert decomposition')
    print('||H_odd|| = pi/2 =',r['hilbert_odd_operator_norm_exact'])
    print('partial HS stabilization')
    for q in r['size_sequence']:
        print(q)
    print('high-mode residual tails')
    for q in r['tail_sequence']:
        print(q)
    print('K_mn versus -2/(pi^2 mn)')
    for q in r['asymptotic_samples']:
        print(q)


if __name__ == '__main__':
    print_report()
