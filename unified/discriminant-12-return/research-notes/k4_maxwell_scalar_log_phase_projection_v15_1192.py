#!/usr/bin/env python3
"""v15.1192 source-first *kinematic* Maxwell/K4 scalar gate.
Exactly checks conformal Maxwell plane-wave stress harmonic, spatial SVT
projectors and necessary coasting log-time phase matching. The proposed
driven response is conditional because the archived J_B-only reduction
omits Maxwell spatial-metric stress sources. No quarter q2 interaction.
"""
import sympy as s
eta,q,k=s.symbols('eta q k',positive=True,real=True)
nuS2=(8*eta-3)*(1+k*k)/3
nuV2=8*eta/s.Integer(3)+2*eta*k*k-1
nuT2=8*eta/s.Integer(3)+3*k*k-1
omega2=12*q*q
sq=s.solve(s.factor(nuS2.subs(k,2*q)-omega2),q*q)[0]
vq=s.solve(s.factor(nuV2.subs(k,2*q)-omega2),q*q)[0]
assert s.simplify(sq-(8*eta-3)/(16*(3-2*eta)))==0
assert s.simplify(vq-(8*eta-3)/(12*(3-2*eta)))==0
assert s.simplify(nuT2.subs(k,2*q)-omega2-(8*eta-3)/3)==0
assert sq.subs(eta,s.Rational(3,4))==s.Rational(1,8)
assert vq.subs(eta,s.Rational(3,4))==s.Rational(1,6)
for ev in (s.Rational(2,5),s.Rational(3,4),s.Integer(1)):
    assert sq.subs(eta,ev)>0
rho=s.symbols('rho',positive=True)
n=s.Matrix([0,0,1]);I=s.eye(3);S=rho*(n*n.T);Pr=I-n*n.T
assert s.simplify(Pr*S*Pr-Pr*s.trace(Pr*S)/2)==s.zeros(3)
assert Pr*S*n==s.zeros(3,1)
scalarproj=n*n.T-I/3
assert s.simplify(s.trace(scalarproj*S)-s.Rational(2,3)*rho)==0
tau,z=s.symbols('tau z',positive=True)
xi=s.sqrt(3)*s.log(tau)
phase=q*(z-xi)
assert s.simplify(tau*s.diff(phase,tau)+s.sqrt(3)*q)==0
a=s.symbols('a',positive=True)
assert s.simplify(a**4*a**(-5)-1/a)==0
ell,w,J0=s.symbols('ell w J0',real=True,positive=True)
JB=J0*s.exp(-ell)*s.cos(w*ell)
F=s.simplify(-s.Rational(9,2)/k**4*(s.diff(JB,ell)+JB))
assert s.simplify(F-9*J0*w*s.exp(-ell)*s.sin(w*ell)/(2*k**4))==0
print('PASS scalar phase-match q²=',sq,'vector kinematic q²=',vq)
print('PASS aligned Maxwell stress scalar=2rho/3, vector=TT=0')
print('PASS redshifting conditional JB model has exp(-ell) forcing')
print('OPEN full source-first Maxwell scalar ADM constraints and physical detector')
