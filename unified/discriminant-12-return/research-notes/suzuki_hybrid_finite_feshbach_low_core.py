#!/usr/bin/env python3
"""Hybrid finite Feshbach audit for Suzuki a=1 even-v sector.

Continues v13.322.  The finite buffer is eliminated in ordinary floating
arithmetic, but the surviving 10x10 low-core block is reconstructed at high
precision before the Schur correction is applied.  This avoids the artificial
~1e-11 to 1e-12 floor produced when the entire matrix is assembled and
diagonalized in double precision.

For a cutoff M, with C={1,3,...,19} and B={21,23,...,M},

    F_M = A_CC^(hp) - A_CB A_BB^{-1} A_BC.

The script reports the low spectrum of F_M as M grows.  Values below the
quadrature / Schur-assembly uncertainty are anatomy only: signs near 1e-17 or
smaller are not certified and do not imply exact zero modes, lambda_1=0, RH,
or GRH.
"""
from __future__ import annotations

import numpy as np
import mpmath as mp

from suzuki_feshbach_buffer_anatomy import finite_matrix
from suzuki_active_core_feshbach_basis import high_precision_core_basis


def high_precision_core_matrix(dps: int = 70):
    vals, Q = high_precision_core_basis(dps=dps)
    A = mp.matrix(10)
    for i in range(10):
        for j in range(10):
            A[i,j] = sum(Q[i,k]*vals[k]*Q[j,k] for k in range(10))
    return A


def effective_core(max_buffer_n: int = 399, arch_order: int = 1200,
                   dps: int = 70):
    ns, A = finite_matrix(max_n=max_buffer_n, arch_order=arch_order)
    ic = np.where(ns <= 19)[0]
    ib = np.where((ns >= 21) & (ns <= max_buffer_n))[0]
    Acb = A[np.ix_(ic, ib)]
    Abb = A[np.ix_(ib, ib)]
    Delta = Acb @ np.linalg.solve(Abb, Acb.T)

    Ahp = high_precision_core_matrix(dps=dps)
    with mp.workdps(dps):
        F = mp.matrix(10)
        for i in range(10):
            for j in range(10):
                F[i,j] = Ahp[i,j] - mp.mpf(str(Delta[i,j]))
        vals, Q = mp.eigsy(F)
    return {
        'buffer_gap': float(np.linalg.eigvalsh(Abb)[0]),
        'delta_norm': float(np.linalg.norm(Delta,2)),
        'effective_eigenvalues': [vals[j] for j in range(10)],
    }


def report():
    for M in (101,151,201,237,301,351,399):
        r=effective_core(M)
        print('M=',M,'gap=',r['buffer_gap'],'||Delta||=',r['delta_norm'])
        print([mp.nstr(x,18) for x in r['effective_eigenvalues'][:6]])


if __name__ == '__main__':
    report()
