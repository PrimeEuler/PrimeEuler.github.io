#!/usr/bin/env python3
"""v15.716: conserved coasting FLRW Fourier anisotropic source from geometry.

This is a prescribed perturbative symmetric stress, not a derived matter
action, independently localized source, or positive-energy guarantee.
Signature (-,+,+,+), a=tau/sqrt(3), Fourier exp(i k z). The overall
signature sign flip to (+,-,-,-) leaves the Christoffel symbols unchanged.
"""
import sympy as s
t,k,sigma,rho0=s.symbols('tau k sigma rho0',positive=True,real=True)
a=t/s.sqrt(3)
coords=s.symbols('x y z')
n=s.Matrix([s.sqrt(s.Rational(1,2)),s.sqrt(s.Rational(1,3)),s.sqrt(s.Rational(1,6))])
assert (n.T*n)[0]==1
Q0=sigma*(n*n.T-s.eye(3)/3)
Q=Q0/t**2
U=s.Matrix([-s.I*k*Q0[2,j]/(2*t) for j in range(3)])
rho=-3*k*k*Q0[2,2]/(2*t*t)+rho0/t**3
T=s.zeros(4)
T[0,0]=rho
for i in range(3):
    T[0,i+1]=T[i+1,0]=U[i]/a**2
    for j in range(3):T[i+1,j+1]=Q[i,j]/a**2
g=s.diag(-1,a*a,a*a,a*a)
gi=s.diag(-1,a**-2,a**-2,a**-2)
crd=[t,*coords]
Gamma={}
for lam in range(4):
    for mu in range(4):
        for nu in range(4):
            Gamma[lam,mu,nu]=s.simplify(s.Rational(1,2)*sum(
                gi[lam,j]*(s.diff(g[j,nu],crd[mu])+s.diff(g[j,mu],crd[nu])
                -s.diff(g[mu,nu],crd[j])) for j in range(4)))
for nu in range(4):
    div=sum(s.diff(T[mu,nu],t) if mu==0 else
            (s.I*k*T[mu,nu] if mu==3 else 0) for mu in range(4))
    div+=sum(Gamma[mu,mu,lam]*T[lam,nu]+Gamma[nu,mu,lam]*T[mu,lam]
             for mu in range(4) for lam in range(4))
    assert s.simplify(div)==0,(nu,s.factor(div))
assert s.simplify(s.trace(Q*Q)-s.Rational(2,3)*sigma**2/t**4)==0
# n_z^2=1/6; all T,V,S stress projections nonzero
assert s.simplify(Q[2,2]/(sigma/t**2)+s.Rational(1,6))==0
xx,yy=Q[0,0],Q[1,1]
QT=s.Matrix([[(xx-yy)/2,Q[0,1]],[Q[0,1],-(xx-yy)/2]])
QV=s.Matrix([Q[0,2],Q[1,2]])
assert s.simplify(s.trace(QT*QT))!=0
assert s.simplify((QV.T*QV)[0])!=0
assert s.simplify(Q[2,2])!=0
print('PASS: four covariant conservation equations on coasting FLRW')
print('PASS: generic tilted stress has nonzero T,V,S projections')
print('PASS: STF source 2/3 is not a coupling; sigma and rho0 free')
print('rho=',rho,'T0z=',T[0,3],'Qzz=',Q[2,2])
