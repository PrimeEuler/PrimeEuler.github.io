#!/usr/bin/env python3
"""Gravity v15.1082: sourced coasting tensor, conformal Maxwell a^-4 and TT Weyl jet.
The full sourced ADM scalar/vector constraint reconstruction is NOT done.
"""
import sympy as s
z=s.symbols("z",real=True)
H,q,M,K,a0,P0,P2=s.symbols("H q M K a0 P0 P2",real=True)
source=2*K/a0**2*s.exp(-2*H*z)*(P0+P2*z*z/2)
coeff=s.symbols("c0:6")
h=sum(coeff[n]*z**n for n in range(6))
op=s.diff(h,z,2)+2*H*s.diff(h,z)+(q*q+M)*h-source
sol={coeff[0]:s.S.Zero,coeff[1]:s.S.Zero}
for n in range(4):
    e=s.series(op.subs(sol),z,0,n+1).removeO().expand().coeff(z,n)
    sol[coeff[n+2]]=s.factor(s.solve(e,coeff[n+2])[0])
assert s.simplify(sol[coeff[2]]-K*P0/a0**2)==0
assert s.simplify(sol[coeff[3]]+4*H*K*P0/(3*a0**2))==0
assert s.simplify(sol[coeff[4]]-K*(12*H**2*P0-(q*q+M)*P0+P2)/(12*a0**2))==0
ht=s.expand(h.subs(sol))
assert all(s.simplify(s.series(op.subs(sol),z,0,4).removeO().expand().coeff(z,n))==0 for n in range(4))
# Tensor electric Weyl formula consistent with K4 v15.722:
weyl=(s.diff(ht,z,2)-q*q*ht)*s.exp(-2*H*z)/(4*a0*a0)
wc=[s.factor(s.series(weyl,z,0,3).removeO().expand().coeff(z,i)) for i in range(3)]
assert s.simplify(wc[0]-K*P0/(2*a0**4))==0
assert s.simplify(wc[1]+3*H*K*P0/a0**4)==0
assert s.simplify(wc[2]-K*(32*H**2*P0-M*P0-2*q*q*P0+P2)/(4*a0**4))==0
psi=s.exp(H*z)*a0*ht
canonical=s.diff(psi,z,2)+(q*q+M-H*H)*psi-a0*s.exp(H*z)*source
assert all(s.simplify(s.series(canonical,z,0,4).removeO().expand().coeff(z,n))==0 for n in range(4))
zeta=s.symbols("zeta",real=True)
assert s.simplify((M-H*H).subs({H:1/s.sqrt(3),M:8*zeta/9})-(8*zeta-3)/9)==0
print("PASS coasting conformal Maxwell stress source, canonical tensor response, TT electric Weyl jet")
print("h2, h3, h4:",*[sol[coeff[i]] for i in (2,3,4)])
print("W0, W1, W2:",*wc)
