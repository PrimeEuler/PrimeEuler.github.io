#!/usr/bin/env python3
"""Gravity v15.1175: source K4 SVT spectrum does not select quarter-carrier gaps.
K4 frozen local WKB: omegaT²=m²+p², omegaV²=m²+2eta*p²/3,
omegaS²=m²+(-1/3+8eta/9)*p². At shared physical p and eta all
square-frequency gaps are common to every abstract ladder rung.
The 1/4-intermediate compensation factor a_k is not common for D>=3.
A discrete rung->p_k mapping and carrier/action are not supplied.
"""
import sympy as s
eta,p,m=s.symbols("eta p m",positive=True,real=True)
T=m*m+p*p
V=m*m+s.Rational(2,3)*eta*p*p
S=m*m+(-s.Rational(1,3)+s.Rational(8,9)*eta)*p*p
DT=s.simplify(T-V)
DV=s.simplify(V-S)
assert s.simplify(DT-3*DV)==0
assert s.simplify(DT.subs(p,0))==0
assert s.simplify(DV.subs(p,0))==0
assert s.simplify(DT.subs(eta,s.Rational(3,2)))==0
assert s.simplify(DV.subs(eta,s.Rational(3,2)))==0
assert s.simplify(s.diff(DT,p)-2*p*(1-2*eta/3))==0
for d in range(2,12):
    a2=[s.Rational(2*j-1,2)*(d-j+s.Rational(1,2)) for j in range(1,d)]
    assert (len(set(a2))==1)==(d==2)
    if d==3: assert a2==[s.Rational(5,4),s.Rational(9,4)]
    if d in (3,5,8):print("D",d,"a_k squared:",a2)
a=s.symbols("a",positive=True)
p2_needed=s.simplify(a/((3-2*eta)/9))
assert s.simplify(DV.subs(p*p,p2_needed)-a)==0
print("PASS K4 fixed-p squared-frequency gap ratio 3 and physical endpoint nulls")
print("PASS required odd-carrier rung factors not common for D>=3")
print("NEGATIVE: rung-to-momentum and a physical quarter carrier not selected")
