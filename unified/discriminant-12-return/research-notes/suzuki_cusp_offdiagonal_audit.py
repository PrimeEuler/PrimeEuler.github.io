#!/usr/bin/env python3
"""Cusp off-diagonal / logarithmic-diagonal audit for Suzuki a=1.

This v13.300 control isolates

    s(t) = 1/2 t log t + A t,
    A = 1/2 (log(2*pi)+gamma-1),

in the even-v (odd Dirichlet mode) sector.  It builds the cusp matrix

    C_mn = int_0^2 s(t) S_mn(t) dt

using the exact overlap S_mn from the one-dimensional reduction, subtracts

    D_nn = log(n)-log(4),

and studies the residual R=C-D on nested high-mode tails.

Exact simplification: for v in H_0^1(-1,1),

    int int v'(x) A|x-y| v'(y) dx dy = -2A ||v||_2^2,

so the linear At term is exactly diagonal.  All off-diagonal cusp structure
comes from 1/2 |x-y| log|x-y|.

The reported residual spectral norms are finite-section numerical evidence.
Their decay on high-mode tails is consistent with, but does not prove, that
C-diag(log n-log4) is compact.  No RH/GRH or kernel conclusion follows.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad

from suzuki_componentwise_high_precision_audit import symmetric_overlap_mp

EULER_GAMMA = 0.5772156649015328606
A_CONST = 0.5*(math.log(2*math.pi)+EULER_GAMMA-1.0)


def cusp(t: float) -> float:
    if t == 0.0:
        return 0.0
    return 0.5*t*math.log(t) + A_CONST*t


def overlap_float(m: int, n: int, t: float) -> float:
    # Use a direct float form equivalent to symmetric_overlap_mp.
    L = 2.0
    A = m*math.pi/2.0
    B = n*math.pi/2.0

    def one(p, q, P, Q):
        def int_cos(w, phase):
            if abs(w) < 1e-13:
                return (L-t)*math.cos(phase)
            return (math.sin(w*L+phase)-math.sin(w*t+phase))/w
        return 0.5*P*Q*(int_cos(P-Q, Q*t)+int_cos(P+Q, -Q*t))

    return one(m,n,A,B)+one(n,m,B,A)


def cusp_entry(m: int, n: int) -> float:
    # t=2u^2 resolves the logarithmic endpoint smoothly.
    f = lambda u: cusp(2*u*u)*overlap_float(m,n,2*u*u)*4*u
    return quad(f, 0.0, 1.0, epsabs=2e-10, epsrel=2e-10, limit=300)[0]


def cusp_matrix(odd_modes: int = 30):
    ns = list(range(1,2*odd_modes,2))
    C = np.zeros((odd_modes,odd_modes), dtype=float)
    for i,m in enumerate(ns):
        for j in range(i, odd_modes):
            v = cusp_entry(m,ns[j])
            C[i,j] = C[j,i] = v
    return ns,C


def residual_matrix(ns, C):
    D = np.diag([math.log(n)-math.log(4.0) for n in ns])
    return C-D


def tail_norms(ns, R, cutoffs=(1,11,21,31,41)):
    rows=[]
    for cutoff in cutoffs:
        idx=[i for i,n in enumerate(ns) if n>=cutoff]
        if not idx:
            continue
        T=R[np.ix_(idx,idx)]
        rows.append({
            'cutoff':cutoff,
            'dimension':len(idx),
            'spectral_norm':float(np.linalg.norm(T,2)),
            'max_abs_row_sum':float(np.max(np.sum(np.abs(T),axis=1))),
        })
    return rows


def offdiagonal_samples(ns,C):
    out=[]
    for m,n in ((1,3),(3,5),(9,11),(31,33),(31,35),(31,41)):
        if m in ns and n in ns:
            i,j=ns.index(m),ns.index(n)
            out.append({'m':m,'n':n,'Cmn':float(C[i,j])})
    return out


def report(odd_modes: int = 30):
    ns,C=cusp_matrix(odd_modes)
    R=residual_matrix(ns,C)
    return {
        'odd_modes':odd_modes,
        'max_n':ns[-1],
        'full_residual_spectral_norm':float(np.linalg.norm(R,2)),
        'tail_norms':tail_norms(ns,R),
        'offdiagonal_samples':offdiagonal_samples(ns,C),
        'last_diagonal_error':float(R[-1,-1]),
    }


def print_report():
    r=report()
    print('Suzuki v13.300 cusp off-diagonal audit')
    print('odd_modes=',r['odd_modes'],'max_n=',r['max_n'])
    print('full residual norm=',r['full_residual_spectral_norm'])
    print('last diagonal error=',r['last_diagonal_error'])
    print('tail norms')
    for q in r['tail_norms']:
        print(q)
    print('offdiagonal samples')
    for q in r['offdiagonal_samples']:
        print(q)


if __name__ == '__main__':
    print_report()
