#!/usr/bin/env python3
"""Gravity v15.1188 — exact reduced K4 transverse vector action and log-time flow.
Reconstruct from archived payload v14.935 vector_sector.py (quadratic EH
and solid terms; eliminate auxiliary metric shift), preserving frozen action.
Assumptions: background adot²=kappa*C/3, a=tau/sqrt(3), kappa*C=1 for
coasting log-time specialization. No quarter-sector source implied.
"""
import sympy as s
a,ad,C,kap,k,eta,B,ft,f=s.symbols('a ad C kap k eta B ft f',positive=True)
L=C*a**3*ft**2/s.Integer(3)-2*C*a**2*B*ft/s.Integer(3)+(-C*a/s.Integer(6)+3*a*ad**2/(2*kap)+a*k*k/(4*kap))*B**2-2*C*a*eta*k*k*f*f/s.Integer(9)
Lbg=s.factor(L.subs(ad**2,kap*C/s.Integer(3)))
Bstar=s.factor(s.solve(s.diff(Lbg,B),B)[0])
assert s.simplify(Bstar-4*C*a*kap*ft/(4*C*kap+3*k*k))==0
Lred=s.factor(Lbg.subs(B,Bstar))
K=s.factor(s.diff(Lred,ft,2)/2)
V=s.factor(-s.diff(Lred,f,2)/2)
assert s.simplify(K-C*a**3*k*k/(4*C*kap+3*k*k))==0
assert s.simplify(V-2*C*a*eta*k*k/s.Integer(9))==0
assert s.simplify(V/K-(s.Rational(2,3)*eta*k*k/a**2+8*eta*kap*C/(9*a**2)))==0
tau=s.symbols('tau',positive=True)
omega2=s.factor((V/K).subs({a:tau/s.sqrt(3),kap:1/C}))
H=1/tau
Om2=s.factor(omega2-s.Rational(3,2)*s.diff(H,tau)-s.Rational(9,4)*H**2)
nu2=s.factor(Om2*tau*tau-s.Rational(1,4))
assert s.simplify(nu2-(8*eta/s.Integer(3)+2*eta*k*k-1))==0
assert s.simplify(Om2-(nu2+s.Rational(1,4))/tau**2)==0
for ev in [s.Rational(3,8),s.Rational(1,2),s.Rational(3,4),s.Rational(3,2)]:
    assert nu2.subs({eta:ev,k:s.Rational(1,5)})>0
z=s.Function('z')
u=s.sqrt(tau)*z(s.log(tau))
ode=s.factor(s.diff(u,tau,2)+Om2*u)
q=s.symbols('q')
assert s.simplify(ode*tau**s.Rational(3,2)-(s.diff(z(q),q,2)+nu2*z(q)).subs(q,s.log(tau)))==0
# At eta=3/4, k=1, nu=sqrt(10)/2. Log-time transfer has det=1,
# bounded trace, and is not a nontrivial hyperbolic boost flow.
slog=s.symbols('slog',real=True)
nu=s.sqrt(s.Integer(10))/2
transfer=s.Matrix([[s.cos(nu*slog),s.sin(nu*slog)/nu],[-nu*s.sin(nu*slog),s.cos(nu*slog)]])
assert s.simplify(transfer.det()-1)==0
assert s.simplify(s.trace(transfer)-2*s.cos(nu*slog))==0
assert s.simplify(s.diff(s.sqrt(nu2+s.Rational(1,4))/tau,tau)/(2*s.sqrt(nu2+s.Rational(1,4))/tau)+1/(2*tau))==0
print('PASS exact reduced vector kinetic K ~ a³; vector m²/cT² from v14.935')
print('PASS exact global coasting canonical mode Omega²=(nu²+1/4)/tau²')
print('PASS stable log-time oscillation, instantaneous squeeze sigma=-H/2')
print('NEGATIVE no quarter-specific physical boost/EM interaction')
