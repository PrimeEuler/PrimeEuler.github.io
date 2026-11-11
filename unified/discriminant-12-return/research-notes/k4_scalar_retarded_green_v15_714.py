#!/usr/bin/env python3
"""v15.714: exact retarded scalar Green function for source-compatible K4 P.

From independently reconstructed v15.713 time-dependent sourced equation,
P''+3/tau P'+[(8 eta(1+k²)-3k²)/(3tau²)]P
=-9(tau J_B'+J_B)/(2k^4 tau³), k>0.
The formal J_B is NOT a physically normalized covariant stress source.
"""
import sympy as s
eta,k,t,u,J0,r=s.symbols("eta k tau sigma J0 r",positive=True,real=True)
nu=s.symbols("nu",positive=True,real=True)
beta=1+nu*nu
G=u*u/(nu*t)*s.sin(nu*s.log(t/u))
L=lambda expr:s.simplify(s.diff(expr,t,2)+3*s.diff(expr,t)/t+beta*expr/t**2)
assert s.simplify(L(G))==0
assert s.simplify(G.subs(t,u))==0
assert s.simplify(s.diff(G,t).subs(t,u)-1)==0
assert s.simplify((8*eta*(1+k*k)-3*k*k)/3-1
  -(8*eta-3)*(1+k*k)/3)==0
# For formal J_B=J0*tau^r, forcing is -9(r+1)J0*tau^(r-3)/(2k^4).
src=-s.Rational(9,2)*(r+1)*J0*t**(r-3)/k**4
part=-s.Rational(9,2)*(r+1)*J0*t**(r-1)/(k**4*(r*r+nu*nu))
assert s.simplify(L(part)-src)==0
assert s.simplify(t*s.diff(J0/t,t)+J0/t)==0
edge=u*u/t*s.log(t/u)
Ledge=lambda expr:s.simplify(s.diff(expr,t,2)+3*s.diff(expr,t)/t+expr/t**2)
assert Ledge(edge)==0
assert s.simplify(s.diff(edge,t).subs(t,u)-1)==0
print("PASS: retarded coasting scalar kernel G=tau_prime^2 sin[nu log(tau/tau_prime)]/(nu tau)")
print("PASS: exact power-law particular response; J_B proportional 1/tau yields zero P forcing")
