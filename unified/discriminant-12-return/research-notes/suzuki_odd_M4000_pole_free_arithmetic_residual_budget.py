#!/usr/bin/env python3
"""Conservative binary64 arithmetic budget for the pole-free shifted high block.

This checker is conditional on the supplied nominal matrix B.  It does not by
itself certify the exact source operator; that enclosure is a separate step.

Given

    B = A_FF^(0) - 0.53 I,

it computes a Cholesky factor L and an approximate triangular inverse X, then
charges matrix-product dot products with gamma_N.  The purpose is to show that
floating-point reconstruction/inverse verification is many orders of magnitude
smaller than the available positivity margin.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import solve_triangular
from suzuki_odd_M4000_pole_free_finite_high_replay import assemble


def gamma_n(n,u=2.0**-53):
    return (n*u)/(1.0-n*u)


def report():
    _,A0,_,_,_=assemble()
    B=A0-0.53*np.eye(len(A0))
    N=len(B)
    u=2.0**-53
    g=gamma_n(N,u)

    L=np.linalg.cholesky(B)
    LL=L@L.T
    R=B-LL

    # Dot-product accumulation envelope for LL^T plus one subtraction.
    abs_LL=np.abs(L)@np.abs(L).T
    mult_bound=g*np.linalg.norm(abs_LL,ord='fro')
    sub_bound=u*(np.linalg.norm(B,ord='fro')+np.linalg.norm(LL,ord='fro'))
    residual_point=np.linalg.norm(R,ord='fro')
    residual_outward=residual_point+mult_bound+sub_bound

    X=solve_triangular(L,np.eye(N),lower=True)
    LX=L@X
    E=np.eye(N)-LX
    abs_LX=np.abs(L)@np.abs(X)
    inv_mult_bound=g*np.linalg.norm(abs_LX,ord='fro')
    inv_sub_bound=u*(np.linalg.norm(np.eye(N),ord='fro')+np.linalg.norm(LX,ord='fro'))
    inv_res_point=np.linalg.norm(E,ord='fro')
    inv_res_outward=inv_res_point+inv_mult_bound+inv_sub_bound

    # If ||I-LX||_2 <= eta <1, then ||L^{-1}||_2 <= ||X||_2/(1-eta).
    # Use Frobenius norms throughout for a deliberately coarse verified scale.
    Xfro=np.linalg.norm(X,ord='fro')
    Linv_upper=Xfro/(1.0-inv_res_outward)
    factor_floor=1.0/(Linv_upper*Linv_upper)

    print('N =',N)
    print('gamma_N =',repr(g))
    print('point ||B-LL^T||_F =',repr(float(residual_point)))
    print('LL^T dot-product envelope =',repr(float(mult_bound)))
    print('subtraction envelope =',repr(float(sub_bound)))
    print('conditional outward reconstruction bound =',repr(float(residual_outward)))
    print('point ||I-LX||_F =',repr(float(inv_res_point)))
    print('inverse-product envelope =',repr(float(inv_mult_bound)))
    print('inverse subtraction envelope =',repr(float(inv_sub_bound)))
    print('conditional outward inverse residual =',repr(float(inv_res_outward)))
    print('||X||_F =',repr(float(Xfro)))
    print('conditional ||L^-1||_2 upper =',repr(float(Linv_upper)))
    print('conditional factor floor 1/||L^-1||^2 =',repr(float(factor_floor)))
    print('guardrail: source-operator enclosure remains separate')

    assert inv_res_outward < 1e-8
    assert residual_outward < 1e-8
    assert factor_floor > 1e-3


if __name__=='__main__':
    report()
