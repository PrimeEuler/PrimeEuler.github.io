#!/usr/bin/env python3
"""v15.701: Hopf charge-one bundle carrier vs sourced Taub-NUT interaction.

North and south local normalized C2 columns are conventional Hopf maps:
 u_N = (cos(theta/2), exp(i phi) sin(theta/2))
 u_S = (exp(-i phi) cos(theta/2), sin(theta/2))
They differ by the degree-one transition exp(i phi), yielding a unit
first-Chern number; the global rank-one projector is patch invariant.

This is an existence construction for a globally well-defined two-component
charged bundle carrier. It is NOT a physical Taub-NUT sourced action, and an
arbitrary coupling g still multiplies any hypothetical interaction.
"""
import sympy as s
th, ph = s.symbols("theta phi", real=True)
c, v = s.cos(th/2), s.sin(th/2)
uN = s.Matrix([c, s.exp(s.I*ph)*v])
uS = s.Matrix([s.exp(-s.I*ph)*c, v])
dag = lambda u: s.conjugate(u).T
zero2 = s.zeros(2)
assert (dag(uN)*uN-s.eye(1)).applyfunc(s.simplify) == s.zeros(1)
assert (dag(uS)*uS-s.eye(1)).applyfunc(s.simplify) == s.zeros(1)
assert (uN-s.exp(s.I*ph)*uS).applyfunc(s.simplify) == s.zeros(2,1)

AN=s.simplify((-s.I*dag(uN)*uN.diff(ph))[0])
AS=s.simplify((-s.I*dag(uS)*uS.diff(ph))[0])
assert s.simplify(AN-(1-s.cos(th))/2) == 0
assert s.simplify(AS+(1+s.cos(th))/2) == 0
assert s.simplify(AN-AS-1) == 0
F=s.diff(AN,th)
assert s.simplify(F-s.sin(th)/2) == 0
assert s.simplify(s.integrate(F,(th,0,s.pi))-1) == 0

PN=uN*dag(uN)
PS=uS*dag(uS)
assert (PN-PS).applyfunc(s.simplify) == zero2
# Factorized idempotency uses u_N^dagger u_N=1, avoiding brittle
# structural equality in expanded trigonometric expressions.
assert (uN*(dag(uN)*uN)*dag(uN)-PN).applyfunc(s.simplify)==zero2
assert s.simplify(s.trace(PN)-1)==0
# Each candidate scalar component has a pole zero: the pair has no
# simultaneous zero; a globally nonzero scalar L1 section is forbidden.
assert s.simplify(uN[1].subs(th,0))==0
assert s.simplify(uS[0].subs(th,s.pi))==0

g=s.symbols("g",positive=True, real=True)
assert (dag(g*uN)*(g*uN)-s.Matrix([[g*g]])).applyfunc(s.simplify)==s.zeros(1)
print("PASS: transition exp(i phi), Chern number +1, patch-invariant projector")
print("PASS: two-component charge-one carrier normalized, source coupling g free")
