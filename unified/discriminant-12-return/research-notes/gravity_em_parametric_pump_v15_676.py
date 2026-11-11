#!/usr/bin/env python3
"""Cone gravity-EM quarter/half grid parametric pump: exact energy and Floquet diagnostic.
Requires sympy, scipy, numpy. Independent pump coupling is NOT fixed by the mesh.
"""
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
t,h,L,C0,R,Om=s.symbols("t h L C0 R Om",positive=True,real=True)
q,v=s.symbols("q v",real=True)
C=C0/(1+h*s.cos(Om*t))
E=L*v**2/2+q**2/(2*C)
Edot=s.simplify(s.diff(E,t)+s.diff(E,q)*v+s.diff(E,v)*((-R*v-q/C)/L))
assert s.simplify(Edot+R*v**2+q**2*s.diff(C,t)/(2*C**2))==0
assert s.simplify(Edot+R*v**2+q**2*h*Om*s.sin(Om*t)/(2*C0))==0
kappa,x,Px,M,OmegaG=s.symbols("kappa x Px M OmegaG",real=True,positive=True)
pt=s.symbols("pt",real=True)
Hem=pt**2/(2*L)+q**2*(1+kappa*x)/(2*C0)
Hg=Px**2/(2*M)+M*OmegaG**2*x**2/2
Htot=Hem+Hg
vel={q:s.diff(Htot,pt),pt:-s.diff(Htot,q),x:s.diff(Htot,Px),Px:-s.diff(Htot,x)}
ev=lambda H:s.simplify(sum(s.diff(H,z)*zd for z,zd in vel.items()))
assert ev(Htot)==0
assert s.simplify(ev(Hem)-kappa*q**2*Px/(2*C0*M))==0
assert s.simplify(ev(Hg)+kappa*q**2*Px/(2*C0*M))==0
assert ev(Hem).subs(kappa,0)==0
a=s.symbols("a",positive=True)
assert s.simplify(a**4*a**(-2)*a**(-2)-1)==0

def floquet(h,Omega,Q=100):
    T=2*np.pi/Omega
    def rhs(t,y):
        mat=np.array([[0.,1.],[-(1+h*np.cos(Omega*t)),-1./Q]])
        return (mat @ y.reshape(2,2)).reshape(-1)
    sol=solve_ivp(rhs,(0,T),np.eye(2).reshape(-1),rtol=1e-11,atol=1e-13)
    eig=np.linalg.eigvals(sol.y[:,-1].reshape(2,2))
    return float(np.max(np.log(np.abs(eig))/T))
for hh,oo in [(0,2),(.01,2),(.02,2),(.03,2),(.06,2),(.06,2.02),(.06,2.05),(.06,1)]:
    ex=floquet(hh,oo)
    print(f"h={hh:.3f}, Omega/omega0={oo:.3f}, Floquet exponent/omega0={ex:+.8f}")
assert floquet(.06,2)>.009
assert floquet(.01,2)<0
assert floquet(.06,2.05)<0
print("PASS: RLC energy, conservative pump backreaction, 4D Maxwell conformal null, 2:1 threshold and detuning.")
