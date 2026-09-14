#!/usr/bin/env python3
"""Shifted-nominal M16001 target for a possible even-sector index<=3 proof.

Use the already-certified global source enclosure

    A_exact >= A_nom - EPS I,   EPS=2e-13.

Rather than perturbing the anisotropic seven-plane certificate term by term,
this helper reruns the M16001 split directly on the shifted nominal operator
A_nom-EPS I.  If that shifted nominal operator can be outward-certified to have
a seven-dimensional positive subspace, then the same index bound follows for
A_exact by operator monotonicity.

Status: midpoint numerical target.  Arithmetic/source-generation outward replay
is still open.  No theorem is promoted here.
"""
from __future__ import annotations
import math
import numpy as np

from suzuki_M16001_even_index3_anisotropic_tail_split import (
    PI, STOP, REMOTE_START, EXPLICIT_STOP, FAR_START, KEXP,
    Q_HEX, L0_HEX, source_data_stop, off_block, structured_ldl_solve,
    remote_gram, far_moments, block_far_bound, fmat,
)

EPS=2.0e-13
# Shift the previously certified raw/coercive inputs consistently.  The 2*EPS
# loss is deliberately conservative for comparing the shifted nominal branch to
# the exact branch through the already-certified enclosure.
DELTA_REMOTE_SHIFTED=(4.6732-EPS)-0.994**2/(0.22-EPS)


def finite_solve_shifted(stop=STOP):
    modes,Z,diag0,c=source_data_stop(stop)
    diag0=diag0-EPS
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


def report():
    modes,Z,c,X,S=finite_solve_shifted()
    Q=fmat(Q_HEX)
    L0=fmat(L0_HEX)
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True)
    N=vh[6:].T
    P=Q@np.linalg.inv(L0.T)
    B10=np.column_stack([P,N])

    G,W,p=remote_gram(B10,modes,Z,c,X)
    L,B,C=far_moments(W,p,Z,modes)
    fQ=block_far_bound(L,B,C,slice(0,6))
    fN=block_far_bound(L,B,C,slice(6,10))
    fX=math.sqrt(fQ*fN)

    A=np.block([[P.T@S@P,P.T@S@N],[N.T@S@P,N.T@S@N]])
    M=A-G/DELTA_REMOTE_SHIFTED
    M=(M+M.T)/2
    AQ=M[:6,:6]-fQ/DELTA_REMOTE_SHIFTED*np.eye(6)
    FN=M[6:,6:]-fN/DELTA_REMOTE_SHIFTED*np.eye(4)
    BQN=M[:6,6:]

    lamQ=float(np.linalg.eigvalsh(AQ)[0])
    cross=float(np.linalg.norm(BQN,2)+fX/DELTA_REMOTE_SHIFTED)
    fnmax=float(np.linalg.eigvalsh(FN)[-1])
    penalty=cross*cross/lamQ
    margin=fnmax-penalty

    print('EPS source shift =',EPS)
    print('shifted remote floor =',DELTA_REMOTE_SHIFTED)
    print('shifted finite Schur first six =',np.linalg.eigvalsh(S)[:6])
    print('shifted normalized Q lower target =',lamQ)
    print('shifted Q/N cross upper target =',cross)
    print('shifted best unresolved scalar =',fnmax)
    print('shifted six-plane Schur penalty =',penalty)
    print('shifted anisotropic seven-plane midpoint target =',margin)

    assert lamQ>0.67
    assert cross<2.7e-7
    assert fnmax>9.1e-13
    assert penalty<1.1e-13
    assert margin>8.0e-13
    print('PASS: shifted nominal midpoint target remains positive by >8e-13')
    print('OPEN: outward arithmetic/source-generation replay of the shifted nominal branch')
    print('GUARDRAIL: no index<=3 theorem yet')


if __name__=='__main__':
    report()
