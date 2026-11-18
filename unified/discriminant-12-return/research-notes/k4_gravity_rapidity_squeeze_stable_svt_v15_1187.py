#!/usr/bin/env python3
"""Gravity v15.1187: frozen K4 stable mode flow versus SO(1,1) boost.
Conditional extension of archived local SVT coasting equations; no
new derived physical quarter carrier or gravity coupling claimed.
Reference: v14.935, v15.706, v15.1183-1186.
"""
import sympy as s
w,t,eta=s.symbols('w t eta',positive=True,real=True)
M=s.Matrix([[s.cos(w*t),s.sin(w*t)/w],[-w*s.sin(w*t),s.cos(w*t)]])
Boost=s.diag(s.exp(eta),s.exp(-eta))
assert s.simplify(M.det()-1)==0
assert s.simplify(s.trace(M)-2*s.cos(w*t))==0
assert s.simplify(Boost.det()-1)==0
assert s.simplify(s.trace(Boost)-2*s.cosh(eta))==0
A=s.Matrix([[0,1],[-w*w,0]])
B=s.diag(1,-1)
assert s.simplify(A*A+w*w*s.eye(2))==s.zeros(2)
assert B*B==s.eye(2)
G=s.diag(w*w,1)
assert A.T*G+G*A==s.zeros(2)
assert s.simplify(Boost.T*G*Boost-G)[0,0]==w*w*(s.exp(2*eta)-1)
g=s.symbols('g',real=True)
J=s.Matrix([[0,1],[-1,0]])
assert J*s.Matrix([[0,g],[g,0]])==s.diag(g,-g)
# Coasting extension hypothesis: q''+3H q'+omega² q=0 with H=1/tau.
# u=a^(3/2)q -> u''+[omega²-(3/2)Hdot-(9/4)H²]u=0.
tau,k,ep=s.symbols('tau k ep',positive=True,real=True)
for c2 in [s.Integer(1),s.Rational(2,3)*ep,-s.Rational(1,3)+s.Rational(8,9)*ep]:
    omega2=(s.Rational(8,3)*ep+3*c2*k**2)/tau**2
    eff=s.simplify(omega2-s.Rational(3,4)/tau**2)
    Om=s.sqrt(s.Rational(8,3)*ep+3*c2*k**2-s.Rational(3,4))/tau
    assert s.simplify(Om**2-eff)==0
    assert s.simplify(s.diff(Om,tau)/(2*Om)+1/(2*tau))==0
    for eps in [s.Rational(1,2),s.Integer(1),s.Rational(3,2)]:
        assert eff.subs({ep:eps,tau:1,k:1})>0
# Canonical instantaneous mode a=(sqrt(Om)u+i p/sqrt(Om))/sqrt(2)
u,p,Om,dOm=s.symbols('u p Om dOm',real=True)
am=(s.sqrt(Om)*u+s.I*p/s.sqrt(Om))/s.sqrt(2)
astar=(s.sqrt(Om)*u-s.I*p/s.sqrt(Om))/s.sqrt(2)
dot=s.diff(am,u)*p+s.diff(am,p)*(-Om**2*u)+s.diff(am,Om)*dOm
assert s.simplify(dot+s.I*Om*am-dOm/(2*Om)*astar)==0
print("PASS stable oscillator generator differs from boost generator")
print("PASS conditional K4 coasting oscillator Omega=Lambda/tau and squeeze=-H/2")
print("NEGATIVE no K4-sourced quarter-specific boost/EM coupling")
