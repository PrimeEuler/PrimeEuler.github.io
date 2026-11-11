#!/usr/bin/env python3
"""v15.696: exact compact-fiber source selection, local-patch/global caveat."""
import sympy as s
M=4
levels=list(range(-M,M+1))
N=len(levels)
P=s.diag(*levels)
I=s.eye(N)
def sh(q):
    a=s.zeros(N)
    for i,k in enumerate(levels):
        if k+q in levels: a[levels.index(k+q),i]=1
    return a
for q in range(-3,4):
    T=sh(q)
    assert P*T-T*P==q*T
    for i,k in enumerate(levels):
        for j,kp in enumerate(levels):
            assert T[j,i]==(1 if kp==k+q else 0)
H0=s.diag(*[s.Integer(k*k)+1 for k in levels])
assert P*H0-H0*P==s.zeros(N)
g=s.symbols("g",real=True)
V=g*(sh(1)+sh(-1))
assert V.T==V
assert P*V-V*P==g*(sh(1)-sh(-1))
assert P*V-V*P != s.zeros(N)
Qa=s.diag(0,1)
tminus=s.Matrix([[0,1],[0,0]])
tplus=tminus.T
Hint=s.kronecker_product(sh(1),tminus)+s.kronecker_product(sh(-1),tplus)
Ptot=s.kronecker_product(P,s.eye(2))+s.kronecker_product(I,Qa)
assert Ptot*Hint-Hint*Ptot==s.zeros(2*N)
assert Ptot*(g*Hint)-(g*Hint)*Ptot==s.zeros(2*N)
print("PASS: invariant fiber cannot mix k; charged q=1 harmonic shifts k, free amplitude")
print("PASS: auxiliary compensator restores total charge, but does not select g")
