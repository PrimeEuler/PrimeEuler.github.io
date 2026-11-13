#!/usr/bin/env python3
"""Gravity v15.916: corrected additive copy of v15.912: standard Fermi TT tidal quadratic operator on Cone Schwinger shells.
For test matrices hbar=M=omega*=1. E=[[A,B],[B,-A]].
Full quadratic oscillator coupling includes Delta N=0,+2,-2; fixed-D
projection is (hbar/omega*)*(A Jz+B Jx). K4 tensor matter sourcing is NOT derived.
"""
import numpy as np
from scipy.linalg import expm
basis=[(a,N-a) for N in range(9) for a in range(N+1)]
idx={v:i for i,v in enumerate(basis)}
ops=[]
for which in (0,1):
    op=np.zeros((len(basis),len(basis)),complex)
    for i,st in enumerate(basis):
        if st[which]>0:
            target=list(st); target[which]-=1
            op[idx[tuple(target)],i]=np.sqrt(st[which])
    ops.append(op)
a,b=ops
q1=(a+a.conj().T)/np.sqrt(2)
q2=(b+b.conj().T)/np.sqrt(2)
HA=(q1@q1-q2@q2)/2
HB=q1@q2
for N in range(1,7):
    ids=[i for i,(aa,bb) in enumerate(basis) if aa+bb==N]
    D=N+1
    jp=np.zeros((D,D),complex)
    for aa in range(D-1):
        jp[aa+1,aa]=np.sqrt((aa+1)*(D-aa-1))
    jx=(jp+jp.conj().T)/2
    jz=np.diag(np.arange(D)-N/2)
    assert np.max(np.abs(HA[np.ix_(ids,ids)]-jz))<1e-12
    assert np.max(np.abs(HB[np.ix_(ids,ids)]-jx))<1e-12
    if N==4:
        for ratio in (0.,.2,.5,1.):
            p=np.abs(expm(-1j*np.pi/2*(jx+ratio*jz))[:,3])**2
            assert abs(p.sum()-1)<1e-12
            print('D=5, A/B=',ratio,'P(center)=',p[2],'populations=',np.round(p,10))
            if ratio==0: assert p[2]<1e-25
            if ratio==.2: assert abs(p[2]-.00010977201163581694)<1e-12
for i,(ai,bi) in enumerate(basis):
    for j,(aj,bj) in enumerate(basis):
        if abs((ai+bi)-(aj+bj)) not in (0,2):
            assert abs(HA[i,j])<1e-12 and abs(HB[i,j])<1e-12
print('PASS: fixed-D projections D=2..7, off-shell +-2 selection, conventional detuning dark-node lift')
