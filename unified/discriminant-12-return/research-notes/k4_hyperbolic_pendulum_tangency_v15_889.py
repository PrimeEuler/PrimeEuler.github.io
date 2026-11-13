#!/usr/bin/env python3
"""Gravity v15.889 hyperbolic restoring oscillator control; no physical selector assumed."""
import sympy as s
import numpy as np
from scipy.integrate import quad
u=s.symbols("u")
assert s.series(s.cosh(u)-1,u,0,6).removeO()==u**2/2+u**4/24
assert s.Rational(3,8)*s.Rational(1,6)==s.Rational(1,16)
def T_over_T0(A):
    def f(theta):
        if abs(theta-np.pi/2)<1e-7: return np.sqrt(2/np.cosh(A))
        return A*np.cos(theta)/np.sqrt(np.cosh(A)-np.cosh(A*np.sin(theta)))
    return 4/np.sqrt(2)*quad(f,0,np.pi/2,epsabs=1e-11)[0]/(2*np.pi)
values=[(A,T_over_T0(A)) for A in (.1,.5,1.,2.)]
assert all(values[i][1]>values[i+1][1] for i in range(3))
assert abs(values[0][1]-(1-.1**2/16))<1e-6
M,L,V,c,h=s.symbols("M L V c h",positive=True)
w=s.sqrt(V/(M*L**2))
assert s.simplify(w.subs(V,M**3*c**4*L**2/h**2)-M*c**2/h)==0
print("PASS: V=V0(cosh(q/ell)-1); omega0=sqrt(V0/(m ell^2)); omega/omega0=1+A^2/16+O(A^4)")
for A,T in values: print(f"A={A:g}, T/T0={T:.12f}, omega/omega0={1/T:.12f}")
print("PASS: matching Compton frequency requires independent parameter relation")
