#!/usr/bin/env python3
"""Arithmetic cross-check for the shifted M16001 even index-3 target.

This helper keeps the same binary64 source scalar payload as the midpoint branch
but reruns the structured finite solve in numpy.longdouble.  Its purpose is only
to isolate solve/matrix-arithmetic sensitivity from the separately certified
exact-vs-nominal source-operator enclosure.

No theorem is promoted here.
"""
from __future__ import annotations
import math
import numpy as np

from suzuki_M16001_even_index3_shifted_nominal_target import (
    EPS, finite_solve_shifted,
)
from suzuki_M16001_even_index3_anisotropic_tail_split import (
    PI, Q_HEX, source_data_stop, off_block,
)


def fmat(H):
    return np.array([[float.fromhex(x) for x in row] for row in H],dtype=float)


def structured_ldl_longdouble(diag,u,v,x,RHS):
    ld=np.longdouble
    d=np.array(diag,dtype=ld)
    ug=np.array(u,dtype=ld)
    vg=np.array(v,dtype=ld)
    xg=np.array(x,dtype=ld)
    B=np.array(RHS,dtype=ld)
    n=len(d); nr=B.shape[1]
    cc=ld(2)/ld(str(PI))
    piv=np.empty(n,dtype=ld)
    Y=np.empty((n,nr),dtype=ld)
    ls=[]
    for k in range(n-1):
        a=d[0]; piv[k]=a; Y[k]=B[0]
        b=cc*(ug[0]*vg[1:]-vg[0]*ug[1:])/(xg[0]-xg[1:])
        l=b/a; ls.append(l.copy())
        B=B[1:]-l[:,None]*B[0]
        d=d[1:]-b*b/a
        ug=ug[1:]-l*ug[0]
        vg=vg[1:]-l*vg[0]
        xg=xg[1:]
    piv[-1]=d[0]; Y[-1]=B[0]
    X=Y/piv[:,None]
    for k in range(n-2,-1,-1):
        X[k]-=ls[k]@X[k+1:]
    return X


def finite_solve_shifted_longdouble():
    modes,Z,diag0,c=source_data_stop()
    diag0=diag0-EPS
    low,high=modes[:10],modes[10:]
    ZC,ZF=Z[:10],Z[10:]
    cC,cF=c[:10],c[10:]
    A0CC=off_block(low,ZC,low,ZC)
    np.fill_diagonal(A0CC,diag0[:10])
    A0FC=off_block(high,ZF,low,ZC)
    ACC=A0CC+2*np.outer(cC,cC)
    AFC=A0FC+2*np.outer(cF,cC)
    X0=structured_ldl_longdouble(
        diag0[10:],ZF,high.astype(float),high.astype(float)**2,
        np.column_stack([AFC,cF]),
    )
    ld=np.longdouble
    cF=np.array(cF,dtype=ld)
    X0B,U=X0[:,:10],X0[:,10]
    den=ld(1)+ld(2)*(cF@U)
    X=X0B-U[:,None]*(ld(2)*(cF@X0B)[None,:]/den)
    AFC=np.array(AFC,dtype=ld)
    S=np.array(ACC,dtype=ld)-AFC.T@X
    return (S+S.T)/ld(2),X


def report():
    _,_,_,Xd,Sd=finite_solve_shifted()
    Sld,Xld=finite_solve_shifted_longdouble()

    Q=fmat(Q_HEX)
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True)
    N=vh[6:].T
    F=(N.T@Sd@N)
    F=(F+F.T)/2
    ev,U=np.linalg.eigh(F)
    v=N@U[:,-1]

    ray_double=float(v@Sd@v)
    ray_long=np.longdouble(v)@Sld@np.longdouble(v)
    ray_diff=float(ray_long-np.longdouble(ray_double))
    Sdiff=float(np.max(np.abs(np.asarray(Sld,dtype=float)-Sd)))
    Xdiff=float(np.max(np.abs(np.asarray(Xld,dtype=float)-Xd)))

    print('max low-core Schur double/longdouble difference =',Sdiff)
    print('max finite-solve coefficient difference =',Xdiff)
    print('largest unresolved shifted Rayleigh, double =',ray_double)
    print('same Rayleigh with longdouble solve =',ray_long)
    print('Rayleigh arithmetic difference =',ray_diff)

    assert Xdiff<4.0e-15
    assert abs(ray_diff)<2.0e-16
    print('PASS: structured-solve arithmetic is far below the shifted-target slack')
    print('GUARDRAIL: source-generation/outward interval certification remains separate')


if __name__=='__main__':
    report()
