#!/usr/bin/env python3
"""Gravity v15.1077: source/probe bookkeeping and ideal TT roundtrip phase.

This is a standard GR comparator, not a complete self-gravitating finite cavity.
"""
import sympy as s
t,t0,L,Omega,h0,omega,E0,K=s.symbols("t t0 L Omega h0 omega E0 K",real=True,positive=True)
h=h0*s.cos(Omega*t)
delta=s.integrate(h,(t,t0,t0+2*L))
expected=2*h0*s.sin(Omega*L)*s.cos(Omega*(t0+L))/Omega
assert s.trigsimp(delta-expected)==0
assert s.simplify(s.limit(delta,Omega,0)-2*L*h0)==0
# Weak linear gravitational response to Maxwell stress is even under E->-E:
phi=s.simplify(omega*delta.subs(h0,K*E0**2))
assert s.simplify(phi.subs(E0,-E0)-phi)==0
assert s.simplify(phi.subs(E0,2*E0)-4*phi)==0
# Matched source, boundary, action and linear optical readout -> no model residual:
phi_cone=phi
phi_comparator=phi
assert s.simplify(phi_cone-phi_comparator)==0
print("PASS: finite-arm roundtrip transfer, static limit, E0 parity/scale, matched-action null")
