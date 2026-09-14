#!/usr/bin/env python3
"""High-precision nominal generator for the odd M=4000 frozen-8D Schur block.

This is the point generator used by the relaxed normalized-C audit.  It is
logically separated from the exact-source enclosure: v13.357 supplies the
operator source budget ||Delta A||<2e-13; here mpmath is used only to generate
a highly resolved point nominal before binary64 linear algebra.

The archimedean source uses the exact rational h_32 polynomial.  Low modes are
evaluated at high precision to avoid catastrophic cancellation of the
parity-correct polynomial recurrence.  Prime and cusp scalars are also
computed at high precision.  The resulting 2000x2000 matrix is then converted
to binary64 for the finite solve.

No theorem is claimed by this file alone.
"""
from __future__ import annotations

import mpmath as mp
import numpy as np

from suzuki_even_arch_symbolic_rational_certificate import HD_polynomials

QS=(2,3,4,5,7)
VM_SOURCE={2:2,3:3,4:2,5:5,7:7}


def eval_poly_mp(poly,y):
    out=mp.mpf('0')
    for k,c in poly.items():
        out += mp.mpf(c.numerator)/c.denominator*y**k
    return out


def build_nominal(dps: int=60):
    mp.mp.dps=dps
    Hp,Dp=HD_polynomials()
    modes=np.arange(2,4001,2,dtype=int)
    N=len(modes)
    H=np.empty(N); D=np.empty(N)
    P=np.empty(N); Pd=np.empty(N); Si=np.empty(N); cusp=np.empty(N)

    for a,n0 in enumerate(modes):
        n=int(n0); r=n//2
        y=1/(mp.mpf(r)*mp.pi)
        H[a]=float(eval_poly_mp(Hp,y))
        D[a]=float(eval_poly_mp(Dp,y))

        k=mp.mpf(n)*mp.pi/2
        ps=mp.mpf('0'); pdiag=mp.mpf('0')
        for q in QS:
            ell=mp.log(q)
            vm=mp.log(VM_SOURCE[q])
            w=vm/mp.sqrt(q)
            ang=mp.mpf(n)*mp.pi*ell/2
            ps += w*mp.sin(ang)
            pdiag -= w*((2-ell)*mp.cos(ang)+mp.sin(ang)/k)
        P[a]=float(ps); Pd[a]=float(pdiag)

        x=mp.mpf(n)*mp.pi
        si=mp.si(x); ci=mp.ci(x)
        Si[a]=float(si)
        cusp[a]=float(mp.log(mp.mpf(n)/4)-ci-si/x)

    mf=modes.astype(float)
    Z=2.0*P+Si+2.0*H
    m=mf[:,None]; n=mf[None,:]
    den=n*n-m*m
    num=n*Z[:,None]-m*Z[None,:]
    np.fill_diagonal(den,1.0)
    A=-(2.0/float(mp.pi))*num/den
    np.fill_diagonal(A,cusp+Pd+D)

    k=mf*float(mp.pi)/2.0
    d=2.0*k*float(mp.sinh(mp.mpf('0.5')))/(k*k+0.25)
    A += 2.0*np.outer(d,d)
    A=0.5*(A+A.T)
    return modes,A,Z,d


if __name__=='__main__':
    from scipy.linalg import eigvalsh
    modes,A,_,_=build_nominal()
    Acc=A[:10,:10]; Acf=A[:10,10:]; Aff=A[10:,10:]
    X=np.linalg.solve(Aff,Acf.T)
    S=0.5*((Acc-Acf@X)+(Acc-Acf@X).T)
    print('dimension =',len(modes))
    print('finite Schur first levels =',eigvalsh(S)[:5])
    print('guardrail: high-precision point nominal only; source/outward budgets separate')
