#!/usr/bin/env python3
"""Post-Feshbach tail-channel geometry for Suzuki a=1 even-v sector.

Continues v13.323.  For each finite buffer cutoff M, form the hybrid effective
10x10 low-core operator

    F_M = A_CC^(hp) - A_CB A_BB^{-1} A_BC,

then diagonalize F_M at high precision.  Project the exact leading remote-tail
coordinate channels onto the first k effective eigenvectors:

    prime: p_m = -(4/pi) A_m,
    cusp:  s_m = -(2/pi) Si(m pi),
    arch:  t_m = -(4/pi) H_m,

where

    A_m = sum_q Lambda(q)/sqrt(q) sin(m pi log(q)/2),
    H_m = int_0^2 h(t) sin(m pi t/2) dt,
    h(t)=r''(t).

The singular values of the k x 3 channel matrix quantify how many independent
leading 1/n channels act on the post-Feshbach effective near-null subspace.

This is numerical anatomy, not an interval certificate.  The first three
post-Feshbach eigenvalues lie below the reliable sign scale of the present
hybrid assembly.  No exact kernel, positivity, lambda_1=0, RH, or GRH claim is
made.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

from suzuki_feshbach_buffer_anatomy import finite_matrix, Aseq
from suzuki_hybrid_finite_feshbach_low_core import high_precision_core_matrix

CORE = np.arange(1,20,2,dtype=int)


def h(t):
    t=mp.mpf(t)
    if t == 0:
        return mp.mpf(1)/4
    return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)


def coordinate_channels(dps: int = 60):
    prime=np.array([-(4/math.pi)*Aseq(int(m)) for m in CORE],dtype=float)
    cusp=np.array([-(2/math.pi)*float(mp.si(int(m)*mp.pi)) for m in CORE],dtype=float)
    with mp.workdps(dps):
        Hv=[mp.quad(lambda t,m=int(m): h(t)*mp.sin(m*mp.pi*t/2), [0,2])
            for m in CORE]
    arch=np.array([-(4/math.pi)*float(x) for x in Hv],dtype=float)
    return prime,cusp,arch


def effective_basis_from_full_matrix(ns,A,max_buffer_n: int,dps: int = 70):
    ic=np.where(ns <= 19)[0]
    ib=np.where((ns >= 21) & (ns <= max_buffer_n))[0]
    Acb=A[np.ix_(ic,ib)]
    Abb=A[np.ix_(ib,ib)]
    Delta=Acb @ np.linalg.solve(Abb,Acb.T)
    Ahp=high_precision_core_matrix(dps=dps)
    with mp.workdps(dps):
        F=mp.matrix(10)
        for i in range(10):
            for j in range(10):
                F[i,j]=Ahp[i,j]-mp.mpf(str(Delta[i,j]))
        vals,Q=mp.eigsy(F)
    Qd=np.array([[float(Q[i,j]) for j in range(10)] for i in range(10)])
    return vals,Qd,float(np.linalg.eigvalsh(Abb)[0])


def channel_report(max_buffer_n: int = 399, arch_order: int = 800,
                   dps: int = 70, full_ns=None, full_A=None):
    if full_A is None:
        ns,A=finite_matrix(max_n=max_buffer_n,arch_order=arch_order)
    else:
        ns,A=full_ns,full_A
    vals,Q,gap=effective_basis_from_full_matrix(ns,A,max_buffer_n,dps=dps)
    p,s,a=coordinate_channels(dps=dps)
    rows={}
    for k in (3,4,5,6):
        M=np.column_stack([Q[:,:k].T@p,Q[:,:k].T@s,Q[:,:k].T@a])
        U,sv,Vt=np.linalg.svd(M,full_matrices=True)
        row={'channel_matrix':M,'singular_values':sv}
        if k == 3:
            q=U[:,-1]
            row['quasi_protected_vector']=q
            row['channel_residual']=M.T@q
            row['channel_residual_norm']=float(np.linalg.norm(M.T@q))
            row['coordinate_vector']=Q[:,:3]@q
            row['formal_effective_rayleigh']=float(sum(q[j]**2*float(vals[j]) for j in range(3)))
        if k == 4:
            q=U[:,3]
            row['computed_protected_line']=q
            row['channel_residual']=M.T@q
            row['coordinate_vector']=Q[:,:4]@q
            row['formal_effective_rayleigh']=float(sum(q[j]**2*float(vals[j]) for j in range(4)))
        rows[k]=row
    return {
        'cutoff':max_buffer_n,
        'buffer_gap':gap,
        'effective_eigenvalues':[vals[j] for j in range(10)],
        'rows':rows,
    }


def report():
    ns,A=finite_matrix(max_n=399,arch_order=800)
    for M in (101,151,201,237,301,351,399):
        r=channel_report(M,full_ns=ns,full_A=A)
        sv3=r['rows'][3]['singular_values']
        sv4=r['rows'][4]['singular_values']
        print('M',M,'lambda4',mp.nstr(r['effective_eigenvalues'][3],18))
        print('  sv3',sv3)
        print('  sv4',sv4)
    r=channel_report(399,full_ns=ns,full_A=A)
    print('effective first six')
    for x in r['effective_eigenvalues'][:6]:
        print(mp.nstr(x,20))
    print('3D quasi-protected vector',r['rows'][3]['quasi_protected_vector'])
    print('3D channel residual',r['rows'][3]['channel_residual'])
    print('3D residual norm',r['rows'][3]['channel_residual_norm'])
    print('3D formal Rayleigh',r['rows'][3]['formal_effective_rayleigh'])
    print('4D computed protected line',r['rows'][4]['computed_protected_line'])
    print('4D channel residual',r['rows'][4]['channel_residual'])
    print('4D formal Rayleigh',r['rows'][4]['formal_effective_rayleigh'])
    print('4D coordinate vector',r['rows'][4]['coordinate_vector'])


if __name__ == '__main__':
    report()
