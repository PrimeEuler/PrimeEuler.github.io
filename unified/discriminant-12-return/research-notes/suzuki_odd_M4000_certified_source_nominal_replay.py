#!/usr/bin/env python3
"""Certified-source nominal replay for the odd M=4000 finite-high block.

This assembles the pole-free matrix B=A_FF^(0)-0.53 I from the rational/source
certificates rather than scipy quadrature or scipy Si/Ci values:

  * arch: exact h_32 Bernoulli/Euler polynomial + even-mode recurrence;
  * prime: rational pi/log/sqrt brackets + Taylor base rotations;
  * cusp: rational range-reduced logarithms + Laplace F/G expansions.

Binary64 is used only for the final deterministic nominal assembly and linear
algebra.  The source-vs-nominal uncertainty is separately budgeted below.
No exact-zero, RH, or GRH conclusion follows.
"""
from __future__ import annotations

import numpy as np
from scipy.sparse.linalg import eigsh

from suzuki_prime_trig_rational_certificate import (
    QS, LOG_K, VM_SOURCE, SQRT_BRACKETS,
    pi_interval as prime_pi_interval,
    log_interval, mul_pos, div_pos, trig_base,
)
from suzuki_even_cusp_rational_certificate import (
    PI, FG_interval, log_n_over_4_interval, iadd, iscale, ineg, idiv,
)
from suzuki_even_arch_symbolic_rational_certificate import HD_polynomials

SENSITIVITY_Z = 4.76188937
ARCH_ANALYTIC_OPERATOR = 1.22e-13
# Exact-rational prime helper gives <1e-9 sequence and <4e-10 diagonal.
# Add 1e-11 to each for binary64 rotation/weight recurrence arithmetic.
PRIME_SEQUENCE_ERROR = 1.01e-9
PRIME_DIAGONAL_ERROR = 4.1e-10
# Exact-rational cusp widths are <4.3e-14 (Si) and <7.4e-15 (diag).
# The nominal is the interval center; these rounded radii include conversion.
CUSP_SI_ERROR = 3.0e-14
CUSP_DIAGONAL_ERROR = 1.0e-14
# Polynomial pi-interval widths are ~1e-22.  1e-12 is an intentionally loose
# allowance for binary64 polynomial evaluation, far above gamma-style estimates.
ARCH_NUMERICAL_OPERATOR = 1.0e-12
# Final matrix-entry assembly uses a bounded number of binary64 operations.
# With |Z_n|<8, n<=4000 and |n^2-m^2|>=92, a direct gamma accounting is well
# below this deliberately coarse operator allowance.
ASSEMBLY_OPERATOR = 1.0e-8


def center(I):
    return float((I[0]+I[1])/2)


def build_nominal():
    modes=np.arange(22,4001,2,dtype=int)
    r=modes//2
    N=len(modes)
    pi0=center(PI)

    # Arch polynomial H,D in y=1/(r*pi).
    Hp,Dp=HD_polynomials()
    y=1.0/(r*pi0)
    Harch=np.zeros(N)
    Darch=np.zeros(N)
    for k,c in Hp.items(): Harch += float(c)*y**k
    for k,c in Dp.items(): Darch += float(c)*y**k

    # Prime source by certified base rotations, propagated recursively.
    p=prime_pi_interval()
    logs={q:log_interval(q,LOG_K[q]) for q in (2,3,5,7)}
    logs[4]=(2*logs[2][0],2*logs[2][1])
    prime_seq=np.zeros(N)
    prime_diag=np.zeros(N)
    for q in QS:
        sint,cost,_=trig_base(mul_pos(p,logs[q]))
        s0=center(sint); c0=center(cost)
        c=1.0; s=0.0
        cvals=np.empty(1990); svals=np.empty(1990)
        out=0
        for rr in range(1,2001):
            c,s=c*c0-s*s0, s*c0+c*s0
            if rr>=11:
                cvals[out]=c; svals[out]=s; out+=1
        w=center(div_pos(logs[VM_SOURCE[q]],SQRT_BRACKETS[q]))
        ell=center(logs[q])
        prime_seq += w*svals
        prime_diag -= w*((2.0-ell)*cvals+svals/(r*pi0))

    # Cusp source from exact rational intervals.
    Si=np.empty(N)
    cusp=np.empty(N)
    for j,n in enumerate(modes):
        F,G,x=FG_interval(int(n))
        si=iadd(iscale(PI,1/2),ineg(F))
        L=log_n_over_4_interval(int(n))
        cd=iadd(iadd(L,G),ineg(idiv(si,x)))
        Si[j]=center(si)
        cusp[j]=center(cd)

    Z=2.0*prime_seq+Si+2.0*Harch
    mf=modes.astype(float)[:,None]
    nf=modes.astype(float)[None,:]
    den=nf*nf-mf*mf
    num=nf*Z[:,None]-mf*Z[None,:]
    np.fill_diagonal(den,1.0)
    A=-(2.0/pi0)*num/den
    np.fill_diagonal(A,cusp+prime_diag+Darch)
    A=0.5*(A+A.T)
    return modes,A


def proof_budget():
    prime_op=(SENSITIVITY_Z*(2.0*PRIME_SEQUENCE_ERROR)
              + PRIME_DIAGONAL_ERROR)
    cusp_op=SENSITIVITY_Z*CUSP_SI_ERROR+CUSP_DIAGONAL_ERROR
    arch_op=ARCH_ANALYTIC_OPERATOR+ARCH_NUMERICAL_OPERATOR
    total=prime_op+cusp_op+arch_op+ASSEMBLY_OPERATOR
    return prime_op,cusp_op,arch_op,total


def report():
    modes,A=build_nominal()
    N=len(modes)
    B=A-0.53*np.eye(N)
    lam=float(eigsh(A,k=1,which='SA',return_eigenvectors=False,tol=1e-12)[0])
    shifted=float(eigsh(B,k=1,which='SA',return_eigenvectors=False,tol=1e-12)[0])
    L=np.linalg.cholesky(B)
    R=B-L@L.T
    residual=float(np.linalg.norm(R,'fro'))

    # v13.424 verified-inverse route, replayed on this deterministic nominal.
    X=np.linalg.solve(L,np.eye(N))
    xnorm=float(np.linalg.norm(X,'fro'))
    lx_point=float(np.linalg.norm(np.eye(N)-L@X,'fro'))
    u=2.0**-53
    gamma=N*u/(1.0-N*u)
    recon_scale=float(np.linalg.norm(np.abs(L)@np.abs(L).T,'fro'))
    lx_scale=float(np.linalg.norm(np.abs(L)@np.abs(X),'fro'))
    recon_out=residual+gamma*recon_scale
    lx_out=lx_point+gamma*lx_scale

    factor_floor=(1.0-1e-8)**2/(28.0**2)
    prime_op,cusp_op,arch_op,source_total=proof_budget()
    certified_margin=factor_floor-recon_out-source_total

    print('dimension =',N)
    print('lambda_min certified-source nominal A0 =',repr(lam))
    print('lambda_min shifted nominal =',repr(shifted))
    print('point Cholesky residual =',repr(residual))
    print('||X||_F =',repr(xnorm))
    print('point ||I-LX||_F =',repr(lx_point))
    print('outward reconstruction budget <',repr(recon_out))
    print('outward LX budget <',repr(lx_out))
    print('prime operator source budget <',prime_op)
    print('cusp operator source budget <',cusp_op)
    print('arch operator source budget <',arch_op)
    print('total source+assembly operator budget <',source_total)
    print('relaxed factor floor >',factor_floor)
    print('certified shifted margin >',certified_margin)

    assert 0.5328 < lam < 0.5329
    assert shifted > 0.0028
    assert residual < 1e-12
    assert xnorm < 28.0
    assert lx_out < 1e-8
    assert recon_out < 6e-11
    assert source_total < 2.1e-8
    assert certified_margin > 0.00125


if __name__=='__main__':
    report()
