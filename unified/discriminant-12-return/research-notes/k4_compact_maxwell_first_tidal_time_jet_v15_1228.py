#!/usr/bin/env python3
"""v15.1228: exact compact Maxwell initial K4 scalar tidal time jet.

Original v15.1078 Maxwell Cauchy field: conformal E even in eta,
B odd, so energy/pressure trace even, longitudinal momentum flux odd.
Use v15.728-729 traceful K4 scalar equations, v15.787 metric Riemann,
and physical signed (+---) Maxwell sources of v15.1226.
All formulae at tau0=1, nonzero longitudinal Fourier k, P=Pdot=0.
This is NOT a full 3D Maxwell evolution or causal photon detector.
"""
import sympy as s
t,k,eta,J=s.symbols('tau k eta J',positive=True,real=True)
P=s.Function('P')(t)
jp,js,jb=(s.Function(x)(t) for x in ('Jphi','Jpsi','JB'))
beta=(8*eta*(1+k*k)-3*k*k)/3
forcing=3*s.sqrt(3)*js/(2*k*k*t**3)-9*(t*s.diff(jb,t)+jb)/(2*k**4*t**3)
Pdd=-3*s.diff(P,t)/t-beta*P/t**2+forcing
Pddd=s.diff(Pdd,t).subs(s.diff(P,t,2),Pdd)
Phi=(t*t*s.diff(P,t,2)+2*t*s.diff(P,t))/(3*(1+k*k))
Phi+=s.sqrt(3)*(jp+js)/(2*t*(1+k*k))-3*s.diff(jb,t)/(2*k*k*(1+k*k))
S=-3*k*k*Phi/t**2
# All time derivatives are established before substituting source values.
# Jphi=Jpsi=J/t*f(sqrt3 log t), f(0)=1,f'(0)=0,f''(0)=-k².
# JB(t)=t^-1*M(sqrt3 log t), M odd from Maxwell E-even/B-odd.
# Therefore JB''(1)=-3 JB'(1), with JB'(1)=sqrt3 k² J.
jet={s.diff(jp,t,2):(2-3*k*k)*J,
     s.diff(js,t,2):(2-3*k*k)*J,
     s.diff(jb,t,2):-3*s.sqrt(3)*k*k*J,
     s.diff(jp,t):-J,s.diff(js,t):-J,
     s.diff(jb,t):s.sqrt(3)*k*k*J,
     jp:J,js:J,jb:s.Integer(0),P:0,s.diff(P,t):0}
def initial(expr):
    return s.factor(expr.subs(s.diff(P,t,3),Pddd)
                        .subs(s.diff(P,t,2),Pdd).xreplace(jet).subs(t,1))
S0=initial(S)
S1=initial(s.diff(S,t))
assert s.simplify(S0-3*s.sqrt(3)*J*(k*k+2)/(2*(1+k*k)))==0
assert s.simplify(S1+3*s.sqrt(3)*J*(7*k*k+10)/(2*(1+k*k)))==0
assert s.simplify(S1/S0+(7*k*k+10)/(k*k+2))==0
assert s.simplify(initial(Pdd)+3*s.sqrt(3)*J/k**2)==0
assert s.simplify(initial(Pddd)-21*s.sqrt(3)*J/k**2)==0
# Einstein Ricci trace for Maxwell: Aiso(t)=rho_EM(t)/3.
# At initial slice the conformal energy has zero first derivative,
# physical rho_EM=a^-4 rho_conf => Aiso'(1)=-4 Aiso(1).
assert s.simplify(s.diff(t**(-4),t).subs(t,1)+4)==0
# Real-space inverse Fourier, signed J(z)=-sqrt3 R0 g(z),
# S0(z)=-9 R0/2[g+(Y*g)], S1(z)=+9 R0/2[7g+3(Y*g)],
# g=(1-z²)^6 for |z|<=1, Y=exp(-|z|)/2.
u=s.symbols('u',nonnegative=True)
g=(1-u*u)**6
G=s.integrate(g,(u,0,1))
Y0=s.integrate(s.exp(-u)*g,(u,0,1))
Ybar=s.integrate((1-s.exp(-1)*s.cosh(u))*g,(u,0,1))
Scenter=-s.Rational(9,2)*(1+Y0)
Sbar=-s.Rational(9,2)*(G+Ybar)
Scenter1=s.Rational(9,2)*(7+3*Y0)
Sbar1=s.Rational(9,2)*(7*G+3*Ybar)
Acenter=3
Abar=3*G
D0=s.factor(Abar-Acenter+2*Sbar/3+Scenter/3)
D1=s.factor((-12*G+12)+2*Sbar1/3+Scenter1/3)
assert G==s.Rational(1024,3003)
assert abs(float(s.N(D0,25))+5.553305386874816)<1e-12
assert abs(float(s.N(D1,25))-28.72884722955552)<1e-12
assert abs(float(s.N(D1/D0,25))+5.173287839969305)<1e-12
print('PASS compact Maxwell parity/source second jet and K4 Riemann STF first jet')
print('Pdd=',initial(Pdd),'Pddd=',initial(Pddd))
print('S(1)=',S0,'Sdot(1)=',S1)
print('PASS Yukawa Sdot(z)=9/2[7g+3Y*g] at R0=1,c=1')
print('spatial proxy start=',s.N(D0,16))
print('spatial proxy initial slope=',s.N(D1,16))
print('OPEN full 3D/zero-mode K4 response, causal photon-mirror-clock readout')
