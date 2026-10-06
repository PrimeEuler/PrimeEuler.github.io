#!/usr/bin/env python3
"""Coarse fail-closed certificate target for the finite shell 16000 -> 32000.

This deliberately does NOT use common-mode source-gradient cancellation.
Instead it asks whether the shell sign survives if the certified global
relative operator radius theta_p is paid independently at both cutoffs.

If A_true is a relative-theta perturbation of the represented positive
operator in energy geometry, then
  (1-theta) A <= A_true <= (1+theta) A
implies for C=(f^T A^{-1}f)^(-1)
  |log(C_true/C)| <= -log(1-theta).
Two cutoffs therefore cost 2[-log(1-theta)] in log(C_N/C_M).

The public finite-solve cap contributes 2[-log(1-Rcap)] as in v14.052/058.
This script is a CERTIFICATE TARGET ONLY until the already-promoted theta
(and negligible source-vector representation charge) are shown to transport
through M=32000.  No infinite-tail inference is made.
"""
from decimal import Decimal,getcontext
getcontext().prec=80

RCAP=Decimal("1e-7")
THETA_E=Decimal("3.899270146651301e-6")
THETA_O=Decimal("9.69258681013552e-11")

# Fixed full-lattice FFT 16k/32k midpoint capacities.
C16_E=Decimal("7.499901498486917e-30")
C32_E=Decimal("7.485609640013522e-30")
C16_O=Decimal("2.1622076013239955e-25")
C32_O=Decimal("2.158138843073839e-25")

def neglog1m(x):
    s=Decimal(0); p=x
    for k in range(1,30):
        s += p/Decimal(k); p*=x
    return s

def expm1_up(x):
    # Conservative for the tiny positive x used here.
    # exp(x)-1 <= x+x^2 for x<1e-5.
    return x+x*x

def one(C16,C32,theta):
    eta=C16/C32-Decimal(1)
    Lsrc=Decimal(2)*neglog1m(theta)
    Lsolve=Decimal(2)*neglog1m(RCAP)
    L=Lsrc+Lsolve
    R=(Decimal(1)+eta)*expm1_up(L)
    return eta,Lsrc,Lsolve,L,R

e=one(C16_E,C32_E,THETA_E)
o=one(C16_O,C32_O,THETA_O)
mid=o[0]-e[0]
W=e[4]+o[4]
lo=mid-W; hi=mid+W

print("even eta,Lsrc,Lsolve,L,R =",*e)
print("odd  eta,Lsrc,Lsolve,L,R =",*o)
print("E_16k_32k_mid =",mid)
print("coarse half-width =",W)
print("conditional interval =",lo,hi)
if not hi < 0:
    raise RuntimeError(("coarse shell target does not preserve negative sign",lo,hi))
print("PASS (conditional target): 16k->32k shell remains strictly negative even without common-mode source cancellation.")
print("GUARDRAIL: requires audit that the global theta/source-representation hypotheses transport through 32k; midpoint/stabilization is not an infinite-tail proof.")
