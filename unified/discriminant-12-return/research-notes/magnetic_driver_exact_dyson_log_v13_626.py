#!/usr/bin/env python3
"""Exact Dyson/log derivation of magnetic-driver Floquet coefficients through g^6."""
import sympy as s
t,u=s.symbols('t u', real=True); I=s.I
Jx=s.Matrix([[0,s.Rational(1,2)],[s.Rational(1,2),0]])
Jp=s.Matrix([[0,1],[0,0]]); Jm=Jp.T
A=-I*(-s.Rational(1,2)*Jx-s.Rational(1,4)*(s.exp(2*I*t)*Jp+s.exp(-2*I*t)*Jm))
N=6; U=[s.eye(2)]
for n in range(1,N+1):
    M=A.subs(t,u)*U[-1].subs(t,u)
    U.append(M.applyfunc(lambda x:s.simplify(s.integrate(x,(u,0,t)))))
X=[s.zeros(2)]+[s.simplify(U[n].subs(t,s.pi)) for n in range(1,N+1)]
L=[s.zeros(2) for _ in range(N+1)]; P=X[:]
for k in range(1,N+1):
    for n in range(1,N+1): L[n]+=s.Rational((-1)**(k+1),k)*P[n]
    Q=[s.zeros(2) for _ in range(N+1)]
    for n in range(1,N+1):
        for a in range(1,n): Q[n]+=P[a]*X[n-a]
    P=Q
for n in range(1,N+1):
    H=s.simplify(I*L[n]/s.pi)
    hx=s.simplify(H[0,1]+H[1,0]); hz=s.simplify(H[0,0]-H[1,1])
    if hx!=0 or hz!=0: print(n,hx,hz)
print("Expected: 1:-1/2; 2:-1/16 z; 3:+1/128 x; 4:-1/256 z; 5:+3/4096 x; 6:-61/393216 z")
