#!/usr/bin/env python3
"""Active-tail channel reduction for Suzuki's a=1 even-v sector.

Continues v13.318.  In the first four high-precision core eigenvectors q^(j),
the projected prime tail has leading rank-one form

    g_j^p(n) = -(4/pi) L_j/n + O(n^-2),
    L_j = sum_m q_m^(j) A_m.

This checkpoint makes the remainder explicit:

    R^p_mn = B^p_mn + (4/pi) A_m/n
           = -(4/pi)/(1-m^2/n^2)
             [ A_m m^2/n^3 - m A_n/n^2 ].

Hence the prime remainder is O(n^-2) for every fixed core mode and its
active-tail Hilbert-Schmidt norm is O(N^-3/2).

For the cusp piece, using

    C_cusp = D_log - H_odd + K_cusp,
    H_mn = 1/(m+n),
    K_mn = -2/(pi^2 m n) + E_mn,

one gets the active leading 1/n coefficient

    C_j = -sum_m q_m^(j) - (2/pi^2) sum_m q_m^(j)/m.

Thus the leading remote active-tail geometry is already confined to the span
of two vectors L and C (prime and cusp channels), up to lower-order remainders
and the smooth archimedean/pole pieces.

The displayed decimals are ordinary floating evaluations of analytic formulas,
not interval-certified enclosures. No exact zero mode, lambda_1=0, RH, or GRH
conclusion follows.
"""
from __future__ import annotations

import math
import numpy as np
import mpmath as mp

CORE = tuple(range(1,20,2))
QS = (2,3,4,5,7)


def odd_tail_bound(N: int, p: int) -> float:
    """Elementary upper bound for sum_{odd n>=N} n^-p."""
    return N**(-p) + 1.0/(2.0*(p-1))*N**(1-p)


def high_precision_active_basis(dps: int = 60):
    """Rebuild the 10x10 core and return the first four eigenvectors."""
    with mp.workdps(dps):
        ws = (mp.log(2)/mp.sqrt(2), mp.log(3)/mp.sqrt(3), mp.log(2)/2,
              mp.log(5)/mp.sqrt(5), mp.log(7)/mp.sqrt(7))
        th = tuple(mp.pi*mp.log(q)/2 for q in QS)

        def amp(j):
            return sum(w*mp.sin(j*t) for w,t in zip(ws,th))

        def cusp(m,n):
            if m == n:
                return mp.log(mp.mpf(n)/4)-mp.ci(n*mp.pi)-mp.si(n*mp.pi)/(n*mp.pi)
            return (2/mp.pi)*(n*mp.si(m*mp.pi)-m*mp.si(n*mp.pi))/(m*m-n*n)

        def shift(m,n,t):
            if m == n:
                k=n*mp.pi/2
                return (2-t)*mp.cos(k*t)+mp.sin(k*t)/k
            theta=mp.pi*t/2
            return (4/mp.pi)*(n*mp.sin(m*theta)-m*mp.sin(n*theta))/(n*n-m*m)

        def prime(m,n):
            if m == n:
                return -sum(w*shift(n,n,mp.log(q)) for q,w in zip(QS,ws))
            return -(4/mp.pi)*(n*amp(m)-m*amp(n))/(n*n-m*m)

        def rr(t):
            if t == 0:
                return mp.mpf(1)/4
            return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)

        def pole_c(n):
            k=n*mp.pi/2
            return 2*k*mp.cosh(mp.mpf('0.5'))/(k*k+mp.mpf('0.25'))

        cv=[pole_c(n) for n in CORE]
        A=mp.matrix(10)
        for i,m in enumerate(CORE):
            for j in range(i,10):
                n=CORE[j]
                ar=mp.quad(lambda t: -rr(t)*shift(m,n,t), [0,2])
                v=cusp(m,n)+prime(m,n)+ar+2*cv[i]*cv[j]
                A[i,j]=A[j,i]=v
        vals,Q=mp.eigsy(A)
        Avec=mp.matrix([amp(m) for m in CORE])
        L=[(Q[:,j].T*Avec)[0] for j in range(4)]
        return vals,Q,L,[amp(m) for m in CORE],sum(ws)


def prime_remainder_hs_bound(N: int, dps: int = 60):
    """Rigorous-formula / floating-evaluation HS bound after rank-one subtraction."""
    vals,Qmp,Lmp,Amp,Wmp=high_precision_active_basis(dps=dps)
    Q=np.array([[float(Qmp[i,j]) for j in range(4)] for i in range(10)])
    m=np.array(CORE,dtype=float)
    A=np.array([float(x) for x in Amp])
    W=float(Wmp)
    rows=[]
    for j in range(4):
        q=np.abs(Q[:,j])
        den=1.0/(1.0-(m/N)**2)
        c2=(4.0/math.pi)*np.sum(q*den*m*W)
        c3=(4.0/math.pi)*np.sum(q*den*np.abs(A)*m*m)
        row=(c2*math.sqrt(odd_tail_bound(N,4))+
             c3*math.sqrt(odd_tail_bound(N,6)))
        rows.append(float(row))
    return rows, float(math.sqrt(sum(x*x for x in rows)))


def channel_vectors(dps: int = 60):
    vals,Qmp,Lmp,Amp,Wmp=high_precision_active_basis(dps=dps)
    Q=np.array([[float(Qmp[i,j]) for j in range(4)] for i in range(10)])
    m=np.array(CORE,dtype=float)
    L=np.array([float(x) for x in Lmp])
    S=Q.T @ np.ones(len(CORE))
    T=Q.T @ (1.0/m)
    C=-S-(2.0/math.pi**2)*T
    cosine=float(np.dot(L,C)/(np.linalg.norm(L)*np.linalg.norm(C)))
    sv=np.linalg.svd(np.column_stack([L,C]),compute_uv=False)
    return L,C,cosine,sv


def report():
    L,C,cosine,sv=channel_vectors()
    print('prime channel L =',L)
    print('cusp channel C =',C)
    print('cos(angle(L,C)) =',cosine)
    print('singular values of [L C] =',sv)
    print('N / prime remainder row bounds / HS bound')
    for N in (237,301,401,501,701,1001):
        rows,hs=prime_remainder_hs_bound(N)
        print(N,rows,hs)


if __name__ == '__main__':
    report()
