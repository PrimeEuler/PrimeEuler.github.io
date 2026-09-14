#!/usr/bin/env python3
"""M16001 anisotropic tail-split diagnostic for a possible even index<=3 proof.

Purpose
-------
The M3999 scalar-direction budget fails as a seven-plane argument if the entire
T={4001,4003,...} tail inverse is replaced by the scalar coercivity bound
`delta^{-1} I`: the missing Q-v cross block produces an O(1e-11) Schur penalty.

This helper moves the finite/tail split outward to

    C={1,3,...,19},
    F={21,23,...,16001},
    T={16003,16005,...}.

The band 4001..16001 is therefore eliminated with the actual source-faithful
operator.  Only the remote tail is bounded through the certified coercivity
floor.  The remote residual Gram is accumulated explicitly through 2,000,000;
beyond that point, separate blockwise inverse-power envelopes are used for the
normalized certified six-plane and unresolved four-plane.  This avoids the very
large loss incurred by one isotropic ten-dimensional far-tail envelope.

Status: midpoint structural/certification target plus previously certified
remote coercivity floor.  Source-evaluation and arithmetic intervals are not yet
charged here.  No index<=3 theorem, exact-zero, RH, or GRH claim follows.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.special import sici

from suzuki_M3999_unresolved_fourplane_residual_gram_replay import (
    PI, ELLS, WEIGHTS, Q_HEX, L0_HEX, KEXP,
    arch_H, arch_diag, off_block, structured_ldl_solve, tail_Z,
)

STOP = 16001
REMOTE_START = 16003
EXPLICIT_STOP = 2_000_000
FAR_START = 2_000_001
DELTA_REMOTE = 4.6732 - 0.994**2 / 0.22


def fmat(H):
    return np.array([[float.fromhex(x) for x in row] for row in H], dtype=float)


def source_data_stop(stop=STOP):
    modes=np.arange(1,stop+1,2,dtype=int)
    H=np.array([arch_H(int(n)) for n in modes])
    D=np.array([arch_diag(int(n)) for n in modes])
    Si,Ci=sici(modes*PI)
    P=np.sum(WEIGHTS[None,:]*np.sin(modes[:,None]*PI*ELLS[None,:]/2),axis=1)
    k=modes*PI/2
    Pd=-np.sum(WEIGHTS[None,:]*((2-ELLS[None,:])*np.cos(k[:,None]*ELLS[None,:])+
                               np.sin(k[:,None]*ELLS[None,:])/k[:,None]),axis=1)
    cusp=np.log(modes/4)-Ci-Si/(modes*PI)
    Z=2*P+Si+2*H
    diag0=cusp+Pd+D
    c=2*k*math.cosh(.5)/(k*k+.25)
    return modes,Z,diag0,c


def finite_solve_stop(stop=STOP):
    modes,Z,diag0,c=source_data_stop(stop)
    low,high=modes[:10],modes[10:]
    ZC,ZF=Z[:10],Z[10:]
    cC,cF=c[:10],c[10:]
    A0CC=off_block(low,ZC,low,ZC)
    np.fill_diagonal(A0CC,diag0[:10])
    A0FC=off_block(high,ZF,low,ZC)
    ACC=A0CC+2*np.outer(cC,cC)
    AFC=A0FC+2*np.outer(cF,cC)
    X0,_=structured_ldl_solve(
        diag0[10:], ZF, high.astype(float), high.astype(float)**2,
        np.column_stack([AFC,cF]),
    )
    X0B,U=X0[:,:10],X0[:,10]
    den=1+2*cF@U
    X=X0B-U[:,None]*(2*(cF@X0B)[None,:]/den)
    S=ACC-AFC.T@X
    return modes,Z,c,X,(S+S.T)/2


def remote_gram(Basis,modes,Z,c,X):
    W=np.vstack([Basis,-X@Basis])
    jj=modes.astype(float)
    p=c@W
    d=Basis.shape[1]
    jld=jj.astype(np.longdouble)
    Wld=W.astype(np.longdouble)
    Zld=Z.astype(np.longdouble)
    aa=[]; bb=[]
    for k in range(KEXP):
        aa.append(np.sum((jld**(2*k+1))[:,None]*Wld,axis=0))
        bb.append(np.sum((Zld*jld**(2*k))[:,None]*Wld,axis=0))
    aa=np.array(aa,dtype=np.longdouble)
    bb=np.array(bb,dtype=np.longdouble)
    pp=np.array(p,dtype=np.longdouble)
    pild=np.longdouble(PI)
    cosh=np.longdouble(math.cosh(.5))
    G=np.zeros((d,d))
    start=REMOTE_START
    while start<=EXPLICIT_STOP:
        end=min(start+199998,EXPLICIT_STOP-1)
        ns=np.arange(start,end+1,2,dtype=float)
        nn=ns.astype(np.longdouble)
        Zn=tail_Z(ns).astype(np.longdouble)
        R=np.zeros((len(ns),d),dtype=np.longdouble)
        for k in range(KEXP):
            R+=(np.longdouble(2)/pild)*(
                Zn[:,None]*aa[k][None,:]/nn[:,None]**(2*k+2)
                -bb[k][None,:]/nn[:,None]**(2*k+1)
            )
        kn=nn*pild/2
        cn=2*kn*cosh/(kn*kn+np.longdouble(.25))
        R+=2*cn[:,None]*pp[None,:]
        R=np.asarray(R,dtype=float)
        G+=R.T@R
        start=end+2
    return G,W,p


def far_moments(W,p,Z,modes):
    N=float(FAR_START)
    rho=STOP/N
    jj=modes.astype(float)
    L=-(2/PI)*(Z@W)+(8*math.cosh(.5)/PI)*p
    B=(16/PI)/(1-rho*rho)*np.sum(np.abs(jj[:,None]*W),axis=0)
    C=(2/PI)/(1-rho*rho)*np.sum(np.abs((jj*jj*Z)[:,None]*W),axis=0) \
      +(8*math.cosh(.5)/PI**3)*np.abs(p)
    return L,B,C


def Ssum(power):
    N=float(FAR_START)
    return N**(-power)+1/(2*(power-1)*N**(power-1))


def block_far_bound(L,B,C,sl):
    return (
        np.linalg.norm(L[sl])*math.sqrt(Ssum(2))
        +np.linalg.norm(B[sl])*math.sqrt(Ssum(4))
        +np.linalg.norm(C[sl])*math.sqrt(Ssum(6))
    )**2


def report():
    modes,Z,c,X,S=finite_solve_stop()
    Q=fmat(Q_HEX)
    L0=fmat(L0_HEX)
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True)
    N=vh[6:].T

    # Work directly in normalized six-plane coordinates P=Q L0^{-T}.
    P=Q@np.linalg.inv(L0.T)
    B10=np.column_stack([P,N])
    G,W,p=remote_gram(B10,modes,Z,c,X)
    L,B,C=far_moments(W,p,Z,modes)

    fQ=block_far_bound(L,B,C,slice(0,6))
    fN=block_far_bound(L,B,C,slice(6,10))
    fX=math.sqrt(fQ*fN)

    A=np.block([
        [P.T@S@P, P.T@S@N],
        [N.T@S@P, N.T@S@N],
    ])
    Mexp=(A-G/DELTA_REMOTE)
    Mexp=(Mexp+Mexp.T)/2

    # Separate far envelopes by block instead of subtracting one global I_10 bound.
    AQ=Mexp[:6,:6]-fQ/DELTA_REMOTE*np.eye(6)
    FN=Mexp[6:,6:]-fN/DELTA_REMOTE*np.eye(4)
    BQN=Mexp[:6,6:]

    lamQ=float(np.linalg.eigvalsh(AQ)[0])
    cross=float(np.linalg.norm(BQN,2)+fX/DELTA_REMOTE)
    fnmax=float(np.linalg.eigvalsh(FN)[-1])
    schur_penalty=cross*cross/lamQ
    candidate=fnmax-schur_penalty

    print('remote certified floor =',DELTA_REMOTE)
    print('explicit remote residual Gram norm =',np.linalg.norm(G,2))
    print('far normalized-six-plane Gram bound =',fQ)
    print('far unresolved Gram bound =',fN)
    print('far cross Gram bound =',fX)
    print('normalized six-plane lower eigenvalue target =',lamQ)
    print('six-plane/unresolved cross norm target =',cross)
    print('best unresolved scalar before cross penalty =',fnmax)
    print('six-plane Schur penalty =',schur_penalty)
    print('best anisotropic seven-plane midpoint lower target =',candidate)

    assert fN < 1.4e-15
    assert lamQ > 0.67
    assert cross < 2.7e-7
    assert fnmax > 1.1e-12
    assert schur_penalty < 1.1e-13
    assert candidate > 1.0e-12
    print('PASS: M16001 anisotropic split leaves >1e-12 midpoint seventh-direction target')
    print('OPEN: outward source/arithmetic enclosure on this fixed split')
    print('GUARDRAIL: no index<=3 theorem yet')


if __name__=='__main__':
    report()
