#!/usr/bin/env python3
"""Level-1c: mixed q=5/q=7 Schur interaction diagnostic.

Continue v13.496.  The purpose is to explain the strong dependence of the
first derivative dS_7 on whether q=5 and q=7 are already present in the
nonlinear Suzuki background.

For source parameters alpha,beta multiplying q=5,q=7, compute the mixed
Frechet derivative D^2 S[x5,x7] at selected canonical backgrounds, project it
to the same frozen unresolved four-plane N, and test whether the observed
Q=5 -> Q=7 change in B7 is quantitatively predicted by integrating the mixed
response along the q=7 background path.

No terminal direction is inspected. Numerical diagnostic only; no bridge or
RH/GRH claim.
"""
from __future__ import annotations
import importlib.util, pathlib, math
import numpy as np

HERE=pathlib.Path(__file__).resolve().parent
P=HERE/'suzuki_chi12_prime_phase_bridge_level1_schur_derivative.py'
spec=importlib.util.spec_from_file_location('L1',P)
L1=importlib.util.module_from_spec(spec); spec.loader.exec_module(L1)

SUPPORT=((2,2),(3,3),(4,2),(5,5),(7,7))


def source_background(Qcut:int):
    modes,Z,diag0,c=L1.source_with_components()
    # Remove prime-source pieces above Qcut from Z and diagonal, leaving all
    # archimedean/cusp/rank-one terms untouched.
    for q,vm in SUPPORT:
        if q>Qcut:
            dZ,dd=L1.channel_arrays(q,vm,modes.astype(float))
            Z=Z-dZ; diag0=diag0-dd
    return modes,Z,diag0,c


def schur(modes,Z,diag0,c):
    *_,ACC,AFC,ZC,ZF,cC,cF=L1.build_blocks(modes,Z,diag0,c)
    AFF=L1.dense_ff(modes,Z,diag0,c)
    X=np.linalg.solve(AFF,AFC)
    S=ACC-AFC.T@X
    return (S+S.T)/2


def first_derivative_at(Qcut:int,q:int,vm:int):
    modes,Z,diag0,c=source_background(Qcut)
    dZ,dd=L1.channel_arrays(q,vm,modes.astype(float))
    dCC,dFC,dFF=L1.derivative_blocks(modes,Z,dZ,dd)
    *_,ACC,AFC,ZC,ZF,cC,cF=L1.build_blocks(modes,Z,diag0,c)
    AFF=L1.dense_ff(modes,Z,diag0,c)
    X=np.linalg.solve(AFF,AFC); Y=np.linalg.solve(AFF,dFC)
    dS=dCC-dFC.T@X-AFC.T@Y+X.T@dFF@X
    return (dS+dS.T)/2


def mixed_fd_at_background(Qcut:int,h:float=2**-8):
    modes,Z,diag0,c=source_background(Qcut)
    dZ5,dd5=L1.channel_arrays(5,5,modes.astype(float))
    dZ7,dd7=L1.channel_arrays(7,7,modes.astype(float))
    def S(a,b): return schur(modes,Z+a*dZ5+b*dZ7,diag0+a*dd5+b*dd7,c)
    return (S(h,h)-S(h,-h)-S(-h,h)+S(-h,-h))/(4*h*h)


def derivative7_continuous_q7_background(t:float):
    # Base Q=5, then turn on t times q=7.  q=5 is already present.
    modes,Z,diag0,c=source_background(5)
    dZ7,dd7=L1.channel_arrays(7,7,modes.astype(float))
    Z=Z+t*dZ7; diag0=diag0+t*dd7
    dCC,dFC,dFF=L1.derivative_blocks(modes,Z,dZ7,dd7)
    *_,ACC,AFC,ZC,ZF,cC,cF=L1.build_blocks(modes,Z,diag0,c)
    AFF=L1.dense_ff(modes,Z,diag0,c)
    X=np.linalg.solve(AFF,AFC); Y=np.linalg.solve(AFF,dFC)
    dS=dCC-dFC.T@X-AFC.T@Y+X.T@dFF@X
    return (dS+dS.T)/2


def cosine(A,B):
    return float(np.vdot(A,B).real/(np.linalg.norm(A,'fro')*np.linalg.norm(B,'fro')))


def main():
    Q,N=L1.qbasis()
    B5_5=N.T@first_derivative_at(5,5,5)@N
    B7_5=N.T@first_derivative_at(5,7,7)@N
    B5_7=N.T@first_derivative_at(7,5,5)@N
    B7_7=N.T@first_derivative_at(7,7,7)@N
    print('endpoint Q=5 cosine',cosine(B5_5,B7_5))
    print('endpoint Q=7 cosine',cosine(B5_7,B7_7))
    print('||B7(Q7)-B7(Q5)||F',np.linalg.norm(B7_7-B7_5,'fro'))
    print('||B5(Q7)-B5(Q5)||F',np.linalg.norm(B5_7-B5_5,'fro'))

    # Track the derivative response continuously as q=7 is switched on.
    ts=np.linspace(0,1,11)
    print('t, ||B7(t)||F, cos(B5_Q5,B7(t)), cos(B5_Q7,B7(t))')
    vals=[]
    for t in ts:
        B=N.T@derivative7_continuous_q7_background(float(t))@N
        vals.append(B)
        print(f'{t:.1f} {np.linalg.norm(B,"fro"):.17g} '
              f'{cosine(B5_5,B):+.15f} {cosine(B5_7,B):+.15f}')

    # Fundamental-theorem check: integrate d/dt B7(t), which is the q7,q7
    # self-Hessian along this path.  This explains the Q5->Q7 background change;
    # the q5,q7 mixed Hessian is separately reported below.
    # Simpson on 20 subintervals, derivative by centered t finite difference.
    grid=np.linspace(0,1,21); eps=2**-10; H=[]
    for t in grid:
        tp=min(1,float(t)+eps); tm=max(0,float(t)-eps)
        Bp=N.T@derivative7_continuous_q7_background(tp)@N
        Bm=N.T@derivative7_continuous_q7_background(tm)@N
        H.append((Bp-Bm)/(tp-tm))
    integ=H[0]+H[-1]+4*sum(H[1:-1:2])+2*sum(H[2:-1:2]); integ/=60.0
    delta=B7_7-B7_5
    print('self-Hessian path integral relerr',np.linalg.norm(integ-delta,'fro')/np.linalg.norm(delta,'fro'))

    # Mixed q5,q7 Hessian at backgrounds Q=4,5,7; h sweep for stability.
    for Qcut in (4,5,7):
        print('mixed Hessian background Q=',Qcut)
        prev=None
        for e in (6,7,8,9,10):
            H57=N.T@mixed_fd_at_background(Qcut,2.0**-e)@N
            print(e,np.linalg.norm(H57,'fro'),
                  'successive_rel',None if prev is None else np.linalg.norm(H57-prev,'fro')/np.linalg.norm(H57,'fro'))
            prev=H57
    print('AUDIT: background transition is decomposed into Hessian interactions; no terminal direction inspected.')

if __name__=='__main__': main()
