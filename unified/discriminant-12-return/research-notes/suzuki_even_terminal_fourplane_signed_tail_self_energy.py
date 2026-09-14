#!/usr/bin/env python3
"""High-precision signed tail self-energy diagnostic on the stabilized even Suzuki four-plane.

Purpose
-------
The certified theorem leaves four even-sector terminal directions unresolved.
Recent diagnostics show their low-core four-plane stabilizes rapidly with cutoff.
This script asks how adding successive high-mode bands changes the finite Schur
complement on that stabilized four-plane.

For cutoffs M1<M2, Schur associativity gives

    S(M2) = S(M1) - R^* T_eff^{-1} R,

whenever the newly added effective band is positive.  Hence the exact signed
self-energy correction is negative semidefinite.  The calculation below is a
high-precision midpoint diagnostic of its size and anisotropy.

It also evaluates the exact source-faithful leading residual moment

    L = -(2/pi) sum_j Z_j w_j + (8 cosh(1/2)/pi) sum_j c_j w_j,

for the M=159 stabilized four-plane coefficients w_j.  The leading far-tail
channel is L/n, so its Gram/self-energy contribution is rank one to leading
order.  The observed dominant band-correction eigenvector is compared directly
with the normalized L vector.

Guardrail: numerical structural diagnostic only.  No exact kernel, infinite
sign, RH, or GRH claim follows.
"""
from __future__ import annotations
import mpmath as mp
import numpy as np

QS=(2,3,4,5,7)
VM=(2,3,2,5,7)
DPS=70


def h(t):
    if t == 0:
        return mp.mpf('0.25')
    return mp.e**(-t/2)/(1-mp.e**(-2*t))-1/(2*t)


def build(stop: int, dps: int=DPS):
    mp.mp.dps=dps
    modes=list(range(1,stop+1,2))
    ells=[mp.log(q) for q in QS]
    weights=[mp.log(vm)/mp.sqrt(q) for vm,q in zip(VM,QS)]
    H=[]; D=[]; Si=[]; cusp=[]; P=[]; Pd=[]; c=[]
    for n in modes:
        k=mp.mpf(n)*mp.pi/2
        H.append(mp.quad(lambda t:h(t)*mp.sin(k*t),[0,1,2]))
        D.append(-mp.quad(lambda t:h(t)*((2-t)*mp.cos(k*t)+mp.sin(k*t)/k),[0,1,2]))
        si=mp.si(mp.mpf(n)*mp.pi); ci=mp.ci(mp.mpf(n)*mp.pi)
        Si.append(si)
        cusp.append(mp.log(mp.mpf(n)/4)-ci-si/(mp.mpf(n)*mp.pi))
        P.append(mp.fsum(w*mp.sin(mp.mpf(n)*mp.pi*ell/2) for w,ell in zip(weights,ells)))
        Pd.append(-mp.fsum(w*((2-ell)*mp.cos(k*ell)+mp.sin(k*ell)/k)
                            for w,ell in zip(weights,ells)))
        c.append(2*k*mp.cosh(mp.mpf('0.5'))/(k*k+mp.mpf('0.25')))
    Z=[2*P[i]+Si[i]+2*H[i] for i in range(len(modes))]
    A=mp.matrix(len(modes))
    for i,m in enumerate(modes):
        for j,n in enumerate(modes):
            if i==j:
                val=cusp[i]+Pd[i]+D[i]
            else:
                val=-(mp.mpf(2)/mp.pi)*(mp.mpf(n)*Z[i]-mp.mpf(m)*Z[j])/mp.mpf(n*n-m*m)
            A[i,j]=val+2*c[i]*c[j]
    return modes,A,Z,c


def schur(A):
    n=A.rows
    Acc=A[:10,:10]
    if n==10:
        return Acc
    Acf=A[:10,10:n]
    Aff=A[10:n,10:n]
    S=Acc-Acf*(Aff**-1)*Acf.T
    return (S+S.T)/2


def eig4(S):
    ev,V=mp.eigsy(S)
    return [ev[i] for i in range(4)],V[:,0:4]


def report():
    cutoffs=(39,59,79,99,119,139,159)
    data={}
    for M in cutoffs:
        modes,A,Z,c=build(M)
        S=schur(A)
        data[M]=(modes,A,Z,c,S)
        ev,_=eig4(S)
        print('M =',M,'tiny Schur levels =',[mp.nstr(x,16) for x in ev])

    # Use the terminal M=159 four-plane as the fixed comparison basis.
    _,B=eig4(data[159][4])
    for a,b in zip(cutoffs[:-1],cutoffs[1:]):
        P=B.T*(data[b][4]-data[a][4])*B
        P=(P+P.T)/2
        ee,_=mp.eigsy(P)
        print('band',a,'->',b,'self-energy eigs =',[mp.nstr(ee[i],16) for i in range(4)])
        assert ee[3] < mp.mpf('1e-40') or ee[3] <= 0
        assert ee[0] < 0

    # M=159 finite-solve coefficients for the four low-core directions.
    modes,A,Z,c,S=data[159]
    Acf=A[:10,10:A.rows]
    Aff=A[10:A.rows,10:A.rows]
    Y=-(Aff**-1)*Acf.T*B
    W=mp.matrix(A.rows,4)
    for i in range(10):
        for j in range(4):
            W[i,j]=B[i,j]
    for i in range(A.rows-10):
        for j in range(4):
            W[i+10,j]=Y[i,j]

    L=[]
    for j in range(4):
        sz=mp.fsum(Z[i]*W[i,j] for i in range(A.rows))
        p=mp.fsum(c[i]*W[i,j] for i in range(A.rows))
        L.append(-(2/mp.pi)*sz+(8*mp.cosh(mp.mpf('0.5'))/mp.pi)*p)
    print('leading moment vector L =',[mp.nstr(x,18) for x in L])

    # Compare normalized leading-moment direction with dominant 139->159 band direction.
    P=B.T*(data[159][4]-data[139][4])*B
    P=(P+P.T)/2
    ee,U=mp.eigsy(P)
    u=np.array([float(U[i,0]) for i in range(4)])
    l=np.array([float(x) for x in L])
    u/=np.linalg.norm(u); l/=np.linalg.norm(l)
    overlap=abs(float(u@l))
    print('dominant self-energy / leading-moment overlap =',repr(overlap))

    assert overlap > 0.999999
    assert abs(l[3]) > 0.99999
    print('PASS: stabilized four-plane tail is negative and asymptotically rank-one in the leading 1/n channel')
    print('GUARDRAIL: midpoint structural diagnostic only; no theorem promotion')


if __name__=='__main__':
    report()
