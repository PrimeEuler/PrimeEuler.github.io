#!/usr/bin/env python3
"""Gravity v15.981: exact D=4 rapidity/Clebsch-Gordan 9/5
coincidence including TT polarizations; candidate node dictionary,
alternative node dictionary and D=6+ counterexamples. No sourced
boost-to-SU2 unitary intertwiner or physical G coupling.
"""
import sympy as s
from sympy.physics.wigner import clebsch_gordan as CG
D=4;j=s.Rational(3,2);J=s.Rational(7,2);k=2
ms=[-j,-s.Rational(1,2),s.Rational(1,2),j]
row=lambda q:[s.simplify(CG(j,k,J,m,q,m+q)**2) for m in ms]
axial=row(0);hp=row(2);hm=row(-2)
tt=[a+b for a,b in zip(hp,hm)]
assert axial==[s.Rational(2,7),s.Rational(18,35),s.Rational(18,35),s.Rational(2,7)]
assert hp==[s.Rational(1,35),s.Rational(1,7),s.Rational(3,7),1]
assert hm==[1,s.Rational(3,7),s.Rational(1,7),s.Rational(1,35)]
assert tt==[s.Rational(36,35),s.Rational(4,7),s.Rational(4,7),s.Rational(36,35)]
assert axial[1]/axial[0]==tt[0]/tt[1]==s.Rational(9,5)
# CHOSEN outward-edge coordinate-to-speed map, not derived dynamics.
bi=(s.Rational(1,2)+s.Rational(1,2))/D
bo=(j+s.Rational(1,2))/D
R=lambda x:(1+x)/(1-x)
assert (bi,bo)==(s.Rational(1,4),s.Rational(1,2))
assert s.simplify(R(bo)/R(bi)-s.Rational(9,5))==0
rap=s.atanh(bo)-s.atanh(bi)-s.log(s.Rational(9,5))/2
assert s.simplify(s.expand_log(rap.rewrite(s.log),force=True))==0
# Alternative state-center map beta=|m|/D does NOT give 9/5.
assert s.simplify(R(j/D)/R(s.Rational(1,2)/D))==s.Rational(77,45)
# At even D>=6, minimal allowed rank is D/2 (not rank 2).
for d in range(4,13,2):
 je=s.Rational(d-1,2);jq=s.Rational(2*d-1,2);rank=d//2
 ci=s.simplify(CG(je,rank,jq,s.Rational(1,2),0,s.Rational(1,2))**2)
 co=s.simplify(CG(je,rank,jq,je,0,je)**2)
 cgr=s.factor(ci/co)
 velocity=s.factor(3*s.Rational(d-1,d+1))
 assert (cgr==velocity)==(d==4)
 print('D',d,'rank',rank,'CG ratio',cgr,'Cayley ratio',velocity)
# There are infinitely many physical speed-pair choices with R=9/5.
b=s.symbols('b',real=True)
t=s.Rational(9,5)*(1+b)/(1-b)
bout=s.factor((t-1)/(t+1))
assert s.simplify(bout.subs(b,s.Rational(1,4))-s.Rational(1,2))==0
assert s.simplify(bout.subs(b,0)-s.Rational(2,7))==0
assert s.simplify(R(bout)/R(b)-s.Rational(9,5))==0
print('PASS D4 axial and TT 9/5, conditional edge velocities,')
print('D6+ rank-minimal counterexamples, rapidity underdetermination')
