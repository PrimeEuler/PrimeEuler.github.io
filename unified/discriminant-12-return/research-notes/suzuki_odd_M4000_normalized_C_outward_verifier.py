#!/usr/bin/env python3
"""Relaxed outward verifier for the frozen-8D odd normalized finite matrix.

Target
------
    C_odd >= 0.80 I.

Rather than reproduce the historical normalized midpoint to its last digits,
this verifier proves only the much weaker point-nominal statement

    Q8^T S_nom Q8 >= 0.998 L0 L0^T,

then subtracts the independently derived exact-source and finite-solve Schur
perturbations.  The remaining exact lower bound stays above 0.80.

The exact-vs-high-precision source envelope eps_A=2e-13 is the audited v13.357
input; finite-high positivity A_FF>=0.53 I is v13.434.  Q8,L0 are immutable
exact dyadic payloads.

No exact-zero, inertia, RH, or GRH claim follows from this file alone.
"""
from __future__ import annotations

from fractions import Fraction
import numpy as np

from suzuki_odd_M4000_frozen_dyadic_Q8_L0 import Q_HEX,L0_HEX
from suzuki_odd_M4000_frozen8_highprecision_nominal import build_nominal

EPS_A=2.0e-13
MU=0.53
CF=5.15
SOLVE_RESIDUAL_TARGET=1.0e-12
SCHUR_FORMATION_ERROR=1.0e-15
QNORM2_SQ_UPPER=1.000000000000002
NOMINAL_RATIO=0.998
# Covers binary64/longdouble formation of the raw 8x8 shifted nominal matrix.
RAW_POINT_FORMATION_ALLOWANCE=1.0e-14


def Fhex(x):
    n,d=float.fromhex(x).as_integer_ratio()
    return Fraction(n,d)


def exact_l0_floor():
    L=[[Fhex(x) for x in row] for row in L0_HEX]
    n=len(L)
    G=[[sum(L[i][k]*L[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    return min(G[i][i]-sum(abs(G[i][j]) for j in range(n) if j!=i)
               for i in range(n))


def source_schur_error():
    e=EPS_A; b=CF; m=MU
    return (e + e*b/m + b*b*e/(m*(m-e)) + b*e/(m-e))


def report():
    _,A,_,_=build_nominal()
    Q=np.array([[float.fromhex(x) for x in row] for row in Q_HEX])
    L0=np.array([[float.fromhex(x) for x in row] for row in L0_HEX])

    Acc=A[:10,:10]; Acf=A[:10,10:]; Aff=A[10:,10:]
    X=np.linalg.solve(Aff,Acf.T)
    solve_res=float(np.linalg.norm(Aff@X-Acf.T,2))
    print('point finite solve residual 2-norm =',repr(solve_res))
    assert solve_res < SOLVE_RESIDUAL_TARGET

    # Form the raw frozen-coordinate matrix with extended accumulator precision.
    ql=Q.astype(np.longdouble)
    sl=(Acc.astype(np.longdouble)
        -Acf.astype(np.longdouble)@X.astype(np.longdouble))
    G=ql.T@sl@ql
    G=np.asarray((G+G.T)/2,dtype=float)
    L0G=L0@L0.T
    M=G-NOMINAL_RATIO*L0G

    # A-posteriori 8x8 shifted-Cholesky positivity check.
    L=np.linalg.cholesky(M)
    Xi=np.linalg.solve(L,np.eye(8))
    unit=2.0**-53
    gamma=8*unit/(1.0-8*unit)
    recon_point=float(np.linalg.norm(M-L@L.T,'fro'))
    recon_scale=float(np.linalg.norm(np.abs(L)@np.abs(L).T,'fro'))
    recon_out=recon_point+gamma*recon_scale+RAW_POINT_FORMATION_ALLOWANCE
    xnorm=float(np.linalg.norm(Xi,'fro'))
    lx_point=float(np.linalg.norm(np.eye(8)-L@Xi,'fro'))
    lx_scale=float(np.linalg.norm(np.abs(L)@np.abs(Xi),'fro'))
    lx_out=lx_point+gamma*lx_scale
    factor_floor=(1.0-1e-10)**2/(1.8e6**2)
    point_margin=factor_floor-recon_out

    print('raw shifted-Cholesky residual point =',repr(recon_point))
    print('raw shifted reconstruction outward <',repr(recon_out))
    print('||L^{-1}||_F =',repr(xnorm))
    print('verified inverse residual <',repr(lx_out))
    print('raw factor floor >',repr(factor_floor))
    print('raw point nominal margin >',repr(point_margin))
    assert xnorm < 1.8e6
    assert lx_out < 1e-10
    assert point_margin > 2.9e-13

    # Exact frozen normalization denominator.
    l0floor=exact_l0_floor()
    assert float(l0floor)>1.6689e-10

    src=source_schur_error()
    solve=CF/MU*SOLVE_RESIDUAL_TARGET
    finite=src+solve+SCHUR_FORMATION_ERROR
    normalized_loss=QNORM2_SQ_UPPER*finite/float(l0floor)
    c_lower=NOMINAL_RATIO-normalized_loss

    print('exact lambda_min(L0 L0^T) floor >',float(l0floor))
    print('source Schur perturbation <',src)
    print('solve Schur perturbation <',solve)
    print('normalized total loss <',normalized_loss)
    print('certified C_odd lower >',c_lower)

    assert src < 2.298e-11
    assert normalized_loss < 0.196
    assert c_lower > 0.802
    assert c_lower > 0.80
    print('PASS: C_odd >= 0.80 I under the stated source/IEEE enclosure model')
    print('GUARDRAIL: H_odd residual-Gram closure remains separate')


if __name__=='__main__':
    report()
