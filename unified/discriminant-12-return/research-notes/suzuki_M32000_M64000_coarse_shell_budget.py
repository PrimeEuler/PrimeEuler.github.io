#!/usr/bin/env python3
"""Coarse fail-closed certificate target for finite shell 32000 -> 64000.

Companion to suzuki_M16000_M32000_coarse_shell_budget.py.  It intentionally
pays the global relative operator radius independently at both cutoffs.
Certificate target only until theta/source representation transport through
64k is proved.
"""
from decimal import Decimal,getcontext
getcontext().prec=80
RCAP=Decimal("1e-7")
THETA_E=Decimal("3.899270146651301e-6")
THETA_O=Decimal("9.69258681013552e-11")
C32_E=Decimal("7.485609640013522e-30")
C64_E=Decimal("7.478286766189398e-30")
C32_O=Decimal("2.158138843073839e-25")
C64_O=Decimal("2.156055288735429e-25")

def neglog1m(x):
    s=Decimal(0);p=x
    for k in range(1,30):
        s+=p/Decimal(k);p*=x
    return s

def one(C32,C64,theta):
    eta=C32/C64-Decimal(1)
    L=Decimal(2)*neglog1m(theta)+Decimal(2)*neglog1m(RCAP)
    R=(Decimal(1)+eta)*(L+L*L)
    return eta,L,R

e=one(C32_E,C64_E,THETA_E)
o=one(C32_O,C64_O,THETA_O)
mid=o[0]-e[0]; W=e[2]+o[2]
lo=mid-W; hi=mid+W
print("even eta,L,R =",*e)
print("odd eta,L,R =",*o)
print("E_32k_64k_mid =",mid)
print("coarse half-width =",W)
print("conditional interval =",lo,hi)
if not hi<0:
    raise RuntimeError(("conditional 32k->64k sign not negative",lo,hi))
print("PASS (conditional target): 32k->64k remains strictly negative.")
print("GUARDRAIL: theta/source bracket transport through 64k must be independently proved; no infinite-tail inference.")
