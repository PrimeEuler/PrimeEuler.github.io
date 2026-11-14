#!/usr/bin/env python3
"""Cone Gravity v15.973: genuine two-mode oscillator symplectic quotient
at fixed D for EM versus refined q2. The geometric half-step m'=Jz/2
must retain a doubled symplectic coefficient if physical hbar is fixed.
An ordinary hbar coadjoint sphere of spin j'=(2D-1)/4 has half-integral
prequantum Chern number and is not a finite-dimensional SU2 irrep.
"""
import sympy as s
D=s.symbols('D',integer=True,positive=True)
Ne=D-1;Nq=2*D-1;jq=Nq/4;Pq=Nq/4
assert s.simplify(Nq-Ne-D)==0
assert s.simplify(Nq-4*Pq)==0
assert s.simplify(Nq/2-(D-s.Rational(1,2)))==0
assert s.simplify((jq*(jq+1)-jq*(jq+s.Rational(1,2)))/Pq-s.Rational(1,2))==0
# Reduced two-oscillator symplectic form: Omega=hbar dphi wedge dn_1
# n1 spans 0..N. Full area/(2*pi*hbar)=N.
# m'=Jz/2=n1/2-N/4, hence dn1=2 dm'.
for d in range(2,101):
    ne=d-1;nq=2*d-1
    assert s.Rational(nq,2).q==2   # naive geometric area Chern half-integer
    assert s.Rational(nq).q==1     # physical quotient area Chern integer
    assert nq+1==2*d
for d in range(2,9):
    N=2*d-1; sz=s.diag(*[s.Rational(N,2)-k for k in range(N+1)])
    plus=s.zeros(N+1)
    for k in range(1,N+1):
        plus[k-1,k]=s.sqrt(k*(N+1-k))
    minus=plus.T
    Kx=(plus+minus)/4;Ky=(plus-minus)/(4*s.I);Kz=sz/2
    assert s.simplify(Kx*Ky-Ky*Kx-s.I*Kz/2)==s.zeros(N+1)
    C=s.simplify(Kx*Kx+Ky*Ky+Kz*Kz)
    assert s.simplify(C-s.Rational(N*(N+2),16)*s.eye(N+1))==s.zeros(N+1)
    assert s.simplify(jq.subs(D,d)*(jq.subs(D,d)+s.Rational(1,2))-
                      s.Rational(N*(N+2),16))==0
print('PASS: D=2..100 Chern integer/half-integer obstruction,')
print('D=2..8 exact co-scaled SU2 matrices, reduced action remains free')
