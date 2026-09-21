#!/usr/bin/env python3
"""Exact Dyson-matrix-log magnetic Floquet coefficients through g^10."""
import sympy as s
t,u=s.symbols('t u', real=True); I=s.I; pi=s.pi
Jx=s.Matrix([[0,s.Rational(1,2)],[s.Rational(1,2),0]])
Jp=s.Matrix([[0,1],[0,0]]); Jm=Jp.T
Aop=-I*(-s.Rational(1,2)*Jx-s.Rational(1,4)*(s.exp(2*I*t)*Jp+s.exp(-2*I*t)*Jm))
N=10; U=[s.eye(2)]
for n in range(1,N+1):
    M=Aop.subs(t,u)*U[-1].subs(t,u)
    U.append(M.applyfunc(lambda x:s.simplify(s.integrate(s.expand(x),(u,0,t)))))
X=[s.zeros(2)]+[s.simplify(U[n].subs(t,pi)) for n in range(1,N+1)]
L=[s.zeros(2) for _ in range(N+1)]; P=X[:]
for k in range(1,N+1):
    for n in range(1,N+1):
        L[n]+=s.Rational((-1)**(k+1),k)*P[n]
    Q=[s.zeros(2) for _ in range(N+1)]
    for n in range(1,N+1):
        for a in range(1,n):
            Q[n]+=P[a]*X[n-a]
    P=Q
for n in range(1,N+1):
    H=s.simplify(I*L[n]/pi)
    hx=s.factor(s.simplify(H[0,1]+H[1,0]))
    hy=s.factor(s.simplify(I*(H[0,1]-H[1,0])))
    hz=s.factor(s.simplify(H[0,0]-H[1,1]))
    if hx!=0 or hy!=0 or hz!=0:
        print("Floquet",n,"hx=",hx,"hy=",hy,"hz=",hz)
