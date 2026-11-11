#!/usr/bin/env python3
"""v15.724: finite-duration, fully conserved FLRW stress and three K4 tails.

A tracefree Q_ij and b in C_c^infinity(t0,t1) define a Fourier source
whose density, momentum and spatial stress ALL vanish outside support.
The pulse is prescribed, not obtained from a positive-energy matter action.
The numeric C^5 polynomial bump is a finite-regularity illustration.
"""
import sympy as s
from scipy.integrate import quad
import numpy as np
from math import sqrt
t,k=s.symbols("tau k",positive=True,real=True)
bb=s.Function("b")(t)
a=t/s.sqrt(3)
Qxx,Qxy,Qxz,Qyy,Qyz=s.symbols("Qxx Qxy Qxz Qyy Qyz")
Qzz=-Qxx-Qyy
Q=s.Matrix([[Qxx,Qxy,Qxz],[Qxy,Qyy,Qyz],[Qxz,Qyz,Qzz]])
T=s.zeros(4)
T[0,0]=-3*k*k*Qzz*bb/t**4
for i in range(3):
    T[0,i+1]=T[i+1,0]=-s.I*k*Q[2,i]*(t*s.diff(bb,t)-bb)/(a*a*t**3)
    for j in range(3):
        T[i+1,j+1]=Q[i,j]*s.diff(bb,t,2)/(a*a*t*t)
metric=s.diag(-1,a*a,a*a,a*a)
inverse=s.diag(-1,a**-2,a**-2,a**-2)
coords=[t,s.Symbol("x"),s.Symbol("y"),s.Symbol("z")]
Gamma={(l,m,n):s.simplify(sum(inverse[l,j]*(
    s.diff(metric[j,n],coords[m])+s.diff(metric[j,m],coords[n])
    -s.diff(metric[m,n],coords[j]))/2 for j in range(4)))
    for l in range(4) for m in range(4) for n in range(4)}
for nu in range(4):
    div=sum(s.diff(T[mu,nu],t) if mu==0 else
        s.I*k*T[mu,nu] if mu==3 else 0 for mu in range(4))
    div+=sum(Gamma[mu,mu,lam]*T[lam,nu]+
             Gamma[nu,mu,lam]*T[mu,lam]
             for mu in range(4) for lam in range(4))
    assert s.simplify(div)==0

JP=s.simplify(a**3*T[0,0])
JB=s.simplify(s.I*k*a**4*T[0,3])
assert s.simplify(t*s.diff(JP,t)+s.sqrt(3)*JB)==0
forcingS=s.simplify(-9*(t*s.diff(JB,t)+JB)/(2*k**4*t**3))
assert s.simplify(forcingS+3*Qzz*s.diff(bb,t,2)/(2*k*k*t*t))==0
D=4+3*k*k
Jv=s.simplify(-a**4*T[0,2])
bv=4*t/(s.sqrt(3)*D)
Kv=2*t**3*k*k/(3*s.sqrt(3)*D)
forcingV=s.simplify(-s.diff(bv*Jv,t)/Kv)
assert s.simplify(forcingV+2*s.I*Qyz*s.diff(bb,t,2)/(k*t*t))==0

# Example: compact C^5 pulse on (1,2), b=(tau-1)^6(2-tau)^6.
# This is a finite regularity numerical witness; the identities hold
# for any genuine C-infinity compact bump.
def bpp(x):
    if not 1<x<2:return 0.
    u=x-1;v=2-x
    return 30*u**4*v**6-72*u**5*v**5+30*u**6*v**4
kk=2.; eta=.75; kap=1.;tau=3.
qs=-1/6
qv=sqrt(1/18)
qt=1/12
Dnum=4+3*kk**2
nu2={"scalar":(8*eta-3)*(1+kk**2)/3,
     "vector":2*eta*Dnum/3-1,
     "tensor":3*kk**2+8*eta/3-1}
coeff={"scalar":-3*qs/(2*kk**2),
       "vector":-2j*qv/kk,
       "tensor":-2*kap*qt}
def response(name):
    nu=sqrt(nu2[name]);c=coeff[name]
    ss=quad(lambda z:bpp(z)*np.sin(nu*np.log(tau/z)),
            1,2,epsabs=1e-13)[0]
    cc=quad(lambda z:bpp(z)*np.cos(nu*np.log(tau/z)),
            1,2,epsabs=1e-13)[0]
    y=c*ss/(nu*tau)
    yp=c*(cc-ss/nu)/tau**2
    ypp=-3*yp/tau-(1+nu**2)*y/tau**2
    return y,yp,ypp
p,pd,pdd=response("scalar")
f,fd,fdd=response("vector")
g,gd,gdd=response("tensor")
an=tau/sqrt(3)
weylS=kk**2/(2*an**2)*(tau**2*pdd+tau*pd+kk**2*p)/(3*(1+kk**2))
Bdot=4/(sqrt(3)*Dnum)*(fd+tau*fdd)
weylV=-1j*kk*Bdot/(4*an)
weylT=(tau**2*gdd+tau*gd-3*kk**2*g)/(12*an**2)
assert min(abs(weylS),abs(weylV),abs(weylT))>1e-8
print("PASS: four exact FLRW covariant source conservation equations")
print("PASS: same compact stress pulse drives all three K4 mode equations")
print("PASS: nonzero postpulse electric Weyl at tau=3",weylS,weylV,weylT)
print("CAUTION: spatial Fourier mode is nonlocalized; no physical matter action")
