#!/usr/bin/env python3
"""Gravity Lane v15.678: anisotropic shear Maxwell polarization pump and K4 sourced tensor.
This is a conditional prescribed homogeneous shear; NOT a vacuum traveling gravitational wave.
"""
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
t=s.symbols("t",real=True)
k,eps,Omega=s.symbols("k eps Omega",positive=True,real=True)
b=s.Function("b")(t)
A=s.Function("A")(t)
for sign in (-1,1):
    weight=s.exp(2*sign*b)
    eom=s.diff(weight*s.diff(A,t),t)+k**2*weight*A
    assert s.simplify(eom/weight-s.diff(A,t,2)-2*sign*s.diff(b,t)*s.diff(A,t)-k*k*A)==0
    u=s.Function("u")(t)
    mode=s.exp(-sign*b)*u
    trans=s.simplify((eom/weight).subs(A,mode).doit()/s.exp(-sign*b))
    expected=s.diff(u,t,2)+(k*k-sign*s.diff(b,t,2)-s.diff(b,t)**2)*u
    assert s.simplify(trans-expected)==0
    eff=s.simplify((k*k-sign*s.diff(b,t,2)-s.diff(b,t)**2).subs(b,eps*s.cos(Omega*t)).doit())
    assert s.simplify(eff-(k*k+sign*eps*Omega**2*s.cos(Omega*t)-eps**2*Omega**2*s.sin(Omega*t)**2))==0
a=s.symbols("a",positive=True)
assert s.simplify(a**4*a**(-2)*a**(-2)-1)==0
tau,eta=s.symbols("tau eta",positive=True)
nu=s.sqrt(s.Rational(8,3)*eta-1)
shear=tau**(-1+s.I*nu)
assert s.simplify((s.diff(shear,tau,2)+3*s.diff(shear,tau)/tau+s.Rational(8,3)*eta*shear/tau**2)/shear)==0
assert s.simplify(nu.subs(eta,s.Rational(3,4))-1)==0
assert s.simplify(nu.subs(eta,s.Rational(3,2))-s.sqrt(3))==0
Mpl,aa,mT,field,fielddot=s.symbols("Mpl aa mT field fielddot",positive=True)
Ltensor=Mpl**2*aa**3/8*(8*fielddot**2-8*mT**2*field**2)
assert s.simplify(Ltensor-Mpl**2*aa**3*(fielddot**2-mT**2*field**2))==0
P,Q,B=s.symbols("P Q B",real=True)
H=s.exp(-2*B)*P**2/2+s.exp(2*B)*k**2*Q**2/2
assert s.simplify(s.diff(H,B)-(s.exp(2*B)*k**2*Q**2-s.exp(-2*B)*P**2))==0

def growth(e,wp,sign):
    T=2*np.pi/wp
    def rhs(time,y):
        bp=-e*wp*np.sin(wp*time)
        bpp=-e*wp*wp*np.cos(wp*time)
        w2=1-sign*bpp-bp*bp
        return (np.array([[0,1],[-w2,0]])@y.reshape(2,2)).ravel()
    sol=solve_ivp(rhs,(0,T),np.eye(2).ravel(),rtol=2e-11,atol=2e-13)
    mat=sol.y[:,-1].reshape(2,2)
    assert abs(np.linalg.det(mat)-1)<1e-8
    return np.log(max(abs(np.linalg.eigvals(mat))))/T
for e,wp in [(0,2),(.001,2),(.01,2),(.02,2),(.01,2.04),(.01,2.08)]:
    rates=[growth(e,wp,i) for i in (-1,1)]
    print(f"epsilon={e:.3f}, Omega={wp:.2f}; growth x,y={rates[0]:+.8f},{rates[1]:+.8f}")
    assert abs(rates[0]-rates[1])<1e-7
assert abs(growth(.01,2,-1)-.01)<1e-5
assert abs(growth(.01,2.04,-1))<1e-7
print("PASS v15.678: shear-Maxwell action, polarization, phase, Floquet and exact K4 coasting shear.")
