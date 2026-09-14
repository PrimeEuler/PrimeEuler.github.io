#!/usr/bin/env python3
"""Prime-source diagnostic for the unresolved even Suzuki terminal four-plane.

Uses the frozen exact-dyadic 10x6 positive basis on modes {1,3,...,19}.
The numerical orthogonal complement is compared with the mod-12 unit-residue
span.  Its principal unresolved vectors are then tested against the additive
raw prime-source blocks q=2,3,4,5,7.

Important: the prime blocks are additive pieces of the raw low-core quadratic
form.  This is NOT an additive decomposition of the nonlinear finite or
infinite Schur complement.  All outputs are structural diagnostics only.
"""
from __future__ import annotations

import math
import numpy as np

from suzuki_M3999_frozen_dyadic_Q_L0 import Q_HEX

VM_SOURCE={2:2,3:3,4:2,5:5,7:7}
QS=(2,3,4,5,7)


def frozen_Q():
    return np.array([[float.fromhex(x) for x in row] for row in Q_HEX],dtype=float)


def unresolved_complement(Q):
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True)
    return vh[Q.shape[1]:].T


def prime_block(modes,q):
    m=np.asarray(modes,dtype=float)
    k=m*math.pi/2.0
    ell=math.log(q)
    w=math.log(VM_SOURCE[q])/math.sqrt(q)
    P=w*np.sin(m*math.pi*ell/2.0)
    Z=2.0*P
    mm=m[:,None]; nn=m[None,:]
    den=nn*nn-mm*mm
    num=nn*Z[:,None]-mm*Z[None,:]
    np.fill_diagonal(den,1.0)
    A=-(2.0/math.pi)*num/den
    diag=-w*((2.0-ell)*np.cos(k*ell)+np.sin(k*ell)/k)
    np.fill_diagonal(A,diag)
    return 0.5*(A+A.T)


def report():
    modes=np.arange(1,20,2,dtype=int)
    Q=frozen_Q()
    N=unresolved_complement(Q)

    # Four V4 unit residue indicators.
    R=np.column_stack([(modes%12==r).astype(float) for r in (1,5,7,11)])
    V,_=np.linalg.qr(R)
    U,pc,_=np.linalg.svd(N.T@V,full_matrices=True)
    W=[N@U[:,i] for i in range(4)]

    print('principal cosines unresolved vs unit residues =',pc)
    print('least-V4-aligned direction =',list(zip(modes.tolist(),W[-1].tolist())))
    print('absolute n=3 coordinate =',abs(W[-1][1]))

    blocks={q:prime_block(modes,q) for q in QS}
    allr=[]
    for i,w in enumerate(W):
        rays={q:float(w@blocks[q]@w) for q in QS}
        allr.append(rays)
        print('raw prime Rayleigh direction',i+1,'=',rays)

    r=allr[-1]
    assert pc[0]>0.93 and pc[3]<0.24
    assert abs(W[-1][1])>0.94
    assert 0.58<r[2]<0.59
    assert -0.30<r[3]<-0.29
    assert -0.12<r[4]<-0.11
    assert -0.017<r[5]<-0.016
    assert abs(r[7])<2e-7
    print('GUARDRAIL: raw-core additive diagnostic only; no Schur/kernel/sign theorem')


if __name__=='__main__':
    report()
