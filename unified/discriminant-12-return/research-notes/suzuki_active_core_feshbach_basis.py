#!/usr/bin/env python3
"""Active-core Feshbach basis audit for Suzuki's a=1 even-v sector.

This checkpoint continues v13.316.  The coordinate core n=1,3,...,19 is
replaced by the 60-digit eigenbasis of its 10x10 matrix.  The finite buffer
21<=n<=399 is eliminated numerically and the Schur correction

    Delta = A_CB A_BB^{-1} A_BC

is rotated into that high-precision core eigenbasis.

The purpose is to determine how many genuinely active near-null directions
must be retained before the remaining low-core directions and finite buffer
can be treated as stiff complement.  The matrix assembly follows v13.316 and
uses the v13.315 joint-prime factorization; the superseded v13.314 sign
convention is not used.

This is a numerical anatomy audit, not an interval-certified proof. Tiny
Feshbach eigenvalues near double precision are not sign certificates and do
not establish exact zero modes, lambda_1=0, RH, or GRH.
"""
from __future__ import annotations

import numpy as np
import mpmath as mp

from suzuki_feshbach_buffer_anatomy import finite_matrix
from suzuki_feshbach_buffer_anatomy import high_precision_core


def high_precision_core_basis(dps: int = 60):
    """Rebuild the high-precision 10x10 core and return eigenpairs.

    This mirrors v13.316's independent mpmath construction but retains the
    eigenvectors.  The implementation is kept local so the basis convention
    is explicit and auditable.
    """
    with mp.workdps(dps):
        core = list(range(1, 20, 2))
        qsm = (2,3,4,5,7)
        wsm = (mp.log(2)/mp.sqrt(2), mp.log(3)/mp.sqrt(3), mp.log(2)/2,
               mp.log(5)/mp.sqrt(5), mp.log(7)/mp.sqrt(7))

        def amp(j):
            return sum(w*mp.sin(j*mp.pi*mp.log(q)/2) for q,w in zip(qsm,wsm))

        def ce(m,n):
            if m == n:
                return mp.log(mp.mpf(n)/4)-mp.ci(n*mp.pi)-mp.si(n*mp.pi)/(n*mp.pi)
            return (2/mp.pi)*(n*mp.si(m*mp.pi)-m*mp.si(n*mp.pi))/(m*m-n*n)

        def se(m,n,t):
            if m == n:
                k=n*mp.pi/2
                return (2-t)*mp.cos(k*t)+mp.sin(k*t)/k
            th=mp.pi*t/2
            return (4/mp.pi)*(n*mp.sin(m*th)-m*mp.sin(n*th))/(n*n-m*m)

        def pe(m,n):
            if m == n:
                return -sum(w*se(n,n,mp.log(q)) for q,w in zip(qsm,wsm))
            return -(4/mp.pi)*(n*amp(m)-m*amp(n))/(n*n-m*m)

        def rr(t):
            if t == 0:
                return mp.mpf(1)/4
            return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)

        def pole_c(n):
            return mp.quad(lambda x: mp.sin(n*mp.pi*(x+1)/2)*mp.cosh(x/2), [-1,1])

        cvec = [pole_c(n) for n in core]
        A = mp.matrix(len(core))
        for i,m in enumerate(core):
            for j,n in enumerate(core):
                ar = mp.quad(lambda t: -rr(t)*se(m,n,t), [0,2])
                A[i,j] = ce(m,n)+pe(m,n)+ar+2*cvec[i]*cvec[j]
        vals, Q = mp.eigsy(A)
        return vals, Q


def active_basis_report(max_n: int = 399, arch_order: int = 700, dps: int = 60):
    ns, A = finite_matrix(max_n=max_n, arch_order=arch_order)
    ic = np.where(ns <= 19)[0]
    ib = np.where(ns >= 21)[0]
    Abb = A[np.ix_(ib, ib)]
    Acb = A[np.ix_(ic, ib)]

    X = np.linalg.solve(Abb, Acb.T)
    Delta = Acb @ X

    vals_mp, Q_mp = high_precision_core_basis(dps=dps)
    lam = np.array([float(vals_mp[j]) for j in range(10)])
    Q = np.array([[float(Q_mp[i,j]) for j in range(10)] for i in range(10)])
    D = Q.T @ Delta @ Q

    rows = []
    for r in range(1, 11):
        coupling = 0.0 if r == 10 else float(np.linalg.norm(D[:r, r:], 2))
        Fr = np.diag(lam[:r]) - D[:r, :r]
        rows.append({
            'active_dim': r,
            'active_to_stiff_correction_norm': coupling,
            'active_feshbach_eigs': np.linalg.eigvalsh(Fr),
        })

    return {
        'core_eigenvalues_hp': lam,
        'buffer_gap': float(np.linalg.eigvalsh(Abb)[0]),
        'delta_in_core_eigenbasis': D,
        'delta_diagonal_in_core_eigenbasis': np.diag(D),
        'rows': rows,
    }


def report():
    r = active_basis_report()
    print('buffer gap =', r['buffer_gap'])
    print('high-precision core eigenvalues')
    for x in r['core_eigenvalues_hp']:
        print(f'{x:.18e}')
    print('Delta diagonal in core eigenbasis')
    for x in r['delta_diagonal_in_core_eigenbasis']:
        print(f'{x:.18e}')
    print('active dimension / coupling to stiff low-core complement')
    for row in r['rows']:
        print(row['active_dim'], row['active_to_stiff_correction_norm'],
              row['active_feshbach_eigs'][:min(4,row['active_dim'])])


if __name__ == '__main__':
    report()
