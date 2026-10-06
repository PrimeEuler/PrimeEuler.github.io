#!/usr/bin/env python3
"""Fail-closed outward budget for the finite far shell 8000->16000.

Uses the arch-200 midpoint capacities, M8000->M16000 common-mode source
sensitivity, and the same public finite-solve cap R_cap=1e-7 already audited
for the N4000->M8000 near shell.

This is the outer-shell analogue of v14.052's budget.  It is a certificate
target until independently audited.
"""
from decimal import Decimal,getcontext
getcontext().prec=80

RCAP=Decimal("1e-7")
# Arch-200 midpoint shell etas from the successful common-mode replay.
ETA_E=Decimal("0.0036404008257719944")
ETA_O=Decimal("0.003617497467397701")
MID=ETA_O-ETA_E

# Common-mode exact-source log-ratio bounds from CI.
LSRC_E=Decimal("3.396294052838575e-10")
LSRC_O=Decimal("3.2525968022987437e-15")

# Same certified global relative operator radii used in v14.052.
THETA_E=Decimal("3.899270146651301e-6")
THETA_O=Decimal("9.69258681013552e-11")

def ln1m(x):
    # decimal series, enough for 1e-7.
    s=Decimal(0); p=x
    for k in range(1,12):
        s += p/Decimal(k); p*=x
    return s

def expm1_bound(x):
    # upward-ish conservative polynomial for tiny positive x.
    return x + x*x

def one(eta,lsrc,theta):
    lsolve=Decimal(2)*ln1m(RCAP)
    ltrial=Decimal(2)*theta*(Decimal(2)*RCAP.sqrt()+Decimal(3)*RCAP)
    L=lsolve+lsrc+ltrial
    R=(Decimal(1)+eta)*expm1_bound(L)
    return lsolve,ltrial,L,R

Ee=one(ETA_E,LSRC_E,THETA_E)
Oo=one(ETA_O,LSRC_O,THETA_O)
W=Ee[3]+Oo[3]
lo=MID-W; hi=MID+W

print("eta_e_mid =",ETA_E)
print("eta_o_mid =",ETA_O)
print("far_shell_mid =",MID)
print("even_Lsolve,Ltrial,L,R =",*Ee)
print("odd_Lsolve,Ltrial,L,R =",*Oo)
print("W_far_8k16k =",W)
print("interval =",lo,hi)
if not hi < 0:
    raise RuntimeError(("finite far shell sign not certified",lo,hi))
print("PASS: 8000->16000 finite far shell is strictly negative.")
