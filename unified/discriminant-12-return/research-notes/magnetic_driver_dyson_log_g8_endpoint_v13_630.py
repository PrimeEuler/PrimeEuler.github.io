#!/usr/bin/env python3
"""Exact Dyson/log Floquet expansion through g^8 and endpoint reduction through eps^7/eps^8."""
import sympy as s
t,u,e,j=s.symbols('t u e j', real=True); I=s.I; pi=s.pi
Jx=s.Matrix([[0,s.Rational(1,2)],[s.Rational(1,2),0]])
Jp=s.Matrix([[0,1],[0,0]]); Jm=Jp.T
Aop=-I*(-s.Rational(1,2)*Jx-s.Rational(1,4)*(s.exp(2*I*t)*Jp+s.exp(-2*I*t)*Jm))
N=8; U=[s.eye(2)]
for n in range(1,N+1):
    M=Aop.subs(t,u)*U[-1].subs(t,u)
    U.append(M.applyfunc(lambda x:s.simplify(s.integrate(s.expand(x),(u,0,t)))))
X=[s.zeros(2)]+[s.simplify(U[n].subs(t,pi)) for n in range(1,N+1)]
L=[s.zeros(2) for _ in range(N+1)]; P=X[:]
for k in range(1,N+1):
    for n in range(1,N+1): L[n]+=s.Rational((-1)**(k+1),k)*P[n]
    Q=[s.zeros(2) for _ in range(N+1)]
    for n in range(1,N+1):
        for a in range(1,n): Q[n]+=P[a]*X[n-a]
    P=Q
for n in range(1,N+1):
    H=s.simplify(I*L[n]/pi)
    hx=s.simplify(H[0,1]+H[1,0]); hz=s.simplify(H[0,0]-H[1,1])
    if hx!=0 or hz!=0: print("Floquet",n,hx,hz)
Ad=1-e**2/s.Integer(64)-3*e**4/s.Integer(2048)-341*e**6/s.Integer(3145728)
Zd=e/s.Integer(8)+e**3/s.Integer(128)+61*e**5/s.Integer(196608)+937*e**7/s.Integer(452984832)
F=s.sqrt(Ad*Ad+Zd*Zd)
ph=s.series(s.atan((Zd/F)*s.tan(pi*F/4)),e,0,9).removeO().expand()
p=s.series((Ad*Ad/F**2)*s.sin(pi*F/2)**2,e,0,10).removeO().expand()
x=s.series(1-p,e,0,10).removeO().expand()
inf=s.series(2*j*x-s.binomial(2*j,2)*x**2+s.binomial(2*j,3)*x**3-s.binomial(2*j,4)*x**4,e,0,10).removeO().expand()
print("c7 =",s.factor(2*j*ph.coeff(e,7)))
print("c8 =",s.factor(s.expand_func(inf.coeff(e,8))))
