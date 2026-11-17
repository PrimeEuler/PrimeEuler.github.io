#!/usr/bin/env python3
"""Gravity v15.1081: nonzero longitudinal Fourier TT+ source jet from compact Maxwell data.

Exact flat/conformal-Minkowski vacuum Maxwell initial data; NOT full FLRW
Einstein-K4 ADM constraints, retarded Weyl or a physically normalized source.
"""
import sympy as s

x,q,a,b,c,A,t,g,mu=s.symbols('x q a b c A t g mu',real=True)
f=(1-x*x)**3
I0=s.integrate(f**2,(x,-1,1))
I1=s.integrate(s.diff(f,x)**2,(x,-1,1))
I2=s.integrate(s.diff(f,x,2)**2,(x,-1,1))
M0=s.integrate(x*x*f**2,(x,-1,1))
M1=s.integrate(x*x*s.diff(f,x)**2,(x,-1,1))
assert (I0,I1,I2)==(s.Rational(2048,3003),s.Rational(1024,385),s.Rational(1024,35))
assert M0/I0==s.Rational(1,15)
assert M1/I1==s.Rational(3,13)

# F0(q)=int dz f(z/c)^2 e^{-iqz},
# F1(q)=int dz (d_z f(z/c))^2 e^{-iqz}.
# Their Taylor coefficients, exact through q²:
F0=c*(I0-(q*c)**2*M0/2)
F1=(I1-(q*c)**2*M1/2)/c
pref=A*A*I0*I1
P0=s.factor(pref*(b/a-a/b)*F0/2)
Pdd=s.factor(A*A*I0*I2*(a/b**3-b/a**3)*F0
          +A*A*I0*I1*(b/a-a/b)*(-2*F1-q*q*F0/2))
ratio=s.series(Pdd/P0,q,0,4).removeO().expand().collect(q)
ratio=s.factor(s.expand(ratio))
target=-22*(a*a+b*b)/(a*a*b*b)-s.Rational(78,5)/c**2+s.Rational(7,25)*q*q
assert s.simplify(ratio-target)==0
ell=s.symbols('ell',positive=True)
sample=s.factor(target.subs({a:ell,b:2*ell,c:ell}))
assert s.simplify(sample+s.Rational(431,10)/ell**2-s.Rational(7,25)*q*q)==0

# The q=0 limit is exactly the previous source derivative relative to energy.
energy=A*A*c*I0**2*I1*(a/b+b/a)/2
assert s.simplify(Pdd.subs(q,0)/energy-
(22*(a*a-b*b)/(a*a*b*b)+s.Rational(78,5)*(a*a-b*b)/(c*c*(a*a+b*b))))==0

# Independent Fourier integration by parts on f: int(ff''-f'^2) e^{-iqz}
# = -2 F1(q) -q² F0(q)/2 (boundary terms zero). Check moments to q².
base=s.integrate((f*s.diff(f,x,2)-s.diff(f,x)**2),(x,-1,1))
moment=s.integrate(x*x*(f*s.diff(f,x,2)-s.diff(f,x)**2),(x,-1,1))
assert base==-2*I1
assert moment==-2*M1+I0
assert s.simplify((c**-1)*(base-(q*c)**2*moment/2)
                  -(-2*F1-q*q*F0/2))==0

# Conditional constant-normalization canonical tensor source:
# h''+(q²+mu²)h = g[P0+Pdd*t²/2+...], h(0)=h'(0)=0.
omega2=q*q+mu*mu
jet=g*P0*t*t/2+g*(Pdd-omega2*P0)*t**4/24
source=g*(P0+Pdd*t*t/2)
assert s.expand(s.diff(jet,t,2)+omega2*jet-source).coeff(t,0)==0
assert s.expand(s.diff(jet,t,2)+omega2*jet-source).coeff(t,2)==0
assert jet.subs(t,0)==0 and s.diff(jet,t).subs(t,0)==0
print('PASS compact Maxwell nonzero-q Fourier source jet, 7/25 q² correction, conditional tensor jet')
print('Pdd(q)/P0(q)=',target,'+ O(q^4)')
print('sample a=l,b=2l,c=l:',sample,'+ O(q^4*l^2)')
