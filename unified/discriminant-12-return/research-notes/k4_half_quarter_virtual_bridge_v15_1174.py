#!/usr/bin/env python3
"""Gravity v15.1174: conditional quarter interlayer virtual-hop gate.
Even sites k=0..D-1 are standard Schwinger Fock states; odd sites
k+1/2 are postulated intermediate carrier states, NOT standard SU2 spins.
Neighbor half-grid hops use w(x)=sqrt[x(D-x)] from the parabolic
intersection dictionary. Common odd-state gap Delta and coupling g
yield effective even-sector H=-g² V V.T/Delta (Schur, E=0).
The ratio of effective inter-even edge to canonical J+ edge is
-(g²/Delta)*sqrt[(k-1/2)(D-k+1/2)] -- nonuniform for D>=3.
"""
import sympy as s
g,Delta=s.symbols("g Delta",real=True,nonzero=True)
for d in range(2,10):
    V=s.zeros(d,d-1)
    aa=[];bb=[]
    for k in range(1,d):
        a=s.sqrt(s.Rational(2*k-1,2)*(d-k+s.Rational(1,2)))
        b=s.sqrt(k*(d-k))
        V[k-1,k-1]=a
        V[k,k-1]=b
        aa.append(a);bb.append(b)
    Heff=s.simplify(-g*g*V*V.T/Delta)
    assert Heff==Heff.T
    for k in range(1,d):
        assert s.simplify(Heff[k-1,k]+g*g*aa[k-1]*bb[k-1]/Delta)==0
        assert s.simplify(Heff[k-1,k]/bb[k-1]+g*g*aa[k-1]/Delta)==0
    for i in range(d):
        for j in range(d):
            if abs(i-j)>1: assert Heff[i,j]==0
    assert (len(set([s.simplify(a*a) for a in aa]))==1)==(d==2)
    if d==3:
        assert aa==[s.sqrt(5)/2,s.Rational(3,2)]
        assert s.simplify(aa[1]/aa[0]-3/s.sqrt(5))==0
    parity=s.diag(*([1,-1]*(d-1)+[1]))
    W=s.zeros(2*d-1)
    for k in range(1,d):
        W[2*k-2,2*k-1]=aa[k-1]
        W[2*k-1,2*k-2]=aa[k-1]
        W[2*k,2*k-1]=bb[k-1]
        W[2*k-1,2*k]=bb[k-1]
    assert parity*W+W*parity==s.zeros(2*d-1)
    assert s.simplify(parity*W**2-W**2*parity)==s.zeros(2*d-1)
    if d in (2,3,5,8):print('D',d,'extra edge ratios',aa)
print('PASS D=2..9 conditional Schur mediation, nearest neighbor, and parity')
print('NEGATIVE: no common canonical Jpm renormalization for D>=3')
print('OPEN: physical odd-carrier, energy gap and coupling from frozen K4 action')
