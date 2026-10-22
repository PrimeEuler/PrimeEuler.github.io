#!/usr/bin/env python3
"""Source-faithful hot-bath coupled scale-versus-shape timescale gate."""
import sympy as s
T,mu,D0,q=s.symbols("T mu D0 q",positive=True)
h=-mu/(2*T)
Eh=3*D0
C_hh_avg=2*D0*mu/T
Th=2*T**2/mu
Thh=8*T**3/mu**2
LT=s.simplify(Th*Eh+s.Rational(1,2)*Thh*C_hh_avg)
CTT=s.simplify(Th**2*C_hh_avg)
C=10*D0*T/mu
assert s.simplify(LT/T-s.Rational(7,5)*C)==0
assert s.simplify(CTT/T**2-s.Rational(4,5)*C)==0
print('orbit-averaged LT =',LT)
print('orbit-averaged C_TT =',CTT)
print('drift fractional scale rate / C =',s.simplify(LT/T/C))
print('quadratic variation fractional scale rate / C =',s.simplify(CTT/T**2/C))
print('hot shape drift =', C*(3*q*q-1)/(4*q))
print('C / T =',s.simplify(C/T))
