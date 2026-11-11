#!/usr/bin/env python3
"""v15.680: exact finite 1D fixed-wall cavity/Maxwell gravitational-shear overlap tests.
The test metric and endcaps are prescribed, not covariant elastic detector engineering.
"""
import sympy as s
import numpy as np
z,K,Om,h,B0,t=s.symbols('z K Omega h B0 t',real=True)
pi=s.pi
f=s.sqrt(2/pi)*s.sin(z)
assert s.integrate(f*f,(z,0,pi))==1
assert s.integrate(s.diff(f,z)**2,(z,0,pi))==1
eps=s.symbols('eps',real=True)
a=s.Function('a')(t,z); b=s.Function('b')(t,z)
Ay=B0*z+eps*a; factor=s.exp(2*eps*b)
wave=s.diff(factor*s.diff(Ay,t),t)-s.diff(factor*s.diff(Ay,z),z)
linear=s.simplify(s.diff(wave,eps).subs(eps,0))
assert s.simplify(linear-(s.diff(a,t,2)-s.diff(a,z,2)-2*B0*s.diff(b,z)))==0
I=s.integrate(s.sin(z)*s.exp(-s.I*K*z),(z,0,pi),conds='none')
J=s.simplify(2*I/pi)
Jclosed=2/pi*(1+s.exp(-s.I*pi*K))/(1-K*K)
assert s.simplify((J-Jclosed).rewrite(s.sin))==0
assert s.limit(Jclosed,K,1)==-s.I
assert s.simplify(Jclosed.subs(K,0)-4/pi)==0
Q=s.symbols('Q',positive=True)
ratio=2*h*K*Om/s.sqrt((1-Om*Om)**2+(Om/Q)**2)
assert s.simplify(ratio.subs({K:1,Om:1})-2*h*Q)==0
J0=s.sin(pi*K)/(pi*K)
Jc=(s.sin(pi*(K-2))/(K-2)+s.sin(pi*(K+2))/(K+2))/(2*pi)
Mf=J0-Jc; Sf=J0+Jc
assert s.limit(Mf,K,0)==1 and s.limit(Sf,K,0)==1
assert s.limit(Mf,K,2)==-s.Rational(1,2)
assert s.limit(Sf,K,2)==s.Rational(1,2)
coeff=s.simplify(2*(Sf-Mf)+Om**2*Mf)
assert s.simplify(coeff.subs(Om,2)-4*J0)==0
assert s.limit(coeff.subs(Om,2),K,2)==0
assert s.limit(coeff.subs(Om,2),K,0)==4
m=s.symbols('m',positive=True)
assert s.limit(coeff.subs({Om:2,K:s.sqrt(4-m*m)})/m**2,m,0)==-s.Rational(1,2)
def jabs(k):
    if abs(k-1)<1e-9:return 1.
    return abs(complex(s.N(Jclosed.subs(K,k))))
def signal(w,q=100,hh=1e-8):
    return 2*hh*w*jabs(w)/np.sqrt((1-w*w)**2+(w/q)**2)
for w in (.95,.99,1,1.01,1.05):
    print(f'GW/EM frequency={w:.2f}: B_signal/B0={signal(w):.9e}')
print('PASS: exact cavity field source, overlap, 2:1 traveling-mode null and K4 conditional opening')
