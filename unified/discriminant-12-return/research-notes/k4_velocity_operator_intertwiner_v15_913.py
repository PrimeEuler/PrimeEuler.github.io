#!/usr/bin/env python3
"""Gravity v15.913: distinguish literal oscillator velocity p/M from Cone X,
and derive fixed-number-shell kinetic quadrature operators exactly.
Physical q_i,p_i are two-mode oscillator observables; Cone X has m/s units
only after a separately justified scale u. No novel gravity coupling claimed.
"""
import sympy as s

Nmax=6
states=[(a,N-a) for N in range(Nmax+1) for a in range(N+1)]
index={pair:i for i,pair in enumerate(states)}
def annihilator(mode):
    A=s.zeros(len(states))
    for col,pair in enumerate(states):
        w=list(pair)
        if w[mode]>0:
            val=s.sqrt(w[mode]);w[mode]-=1
            A[index[tuple(w)],col]=val
    return A

a,b=annihilator(0),annihilator(1)
# v_phys_i / sqrt(hbar*omega/(2*M)) = i(a_i^dagger-a_i).
v1=s.I*(a.T-a)
v2=s.I*(b.T-b)
jz=(a.T*a-b.T*b)/2
jx=(a.T*b+b.T*a)/2
for N in range(1,5):
    ids=[index[(i,N-i)] for i in range(N+1)]
    project=lambda A:A.extract(ids,ids)
    d=N+1
    assert project(v1)==s.zeros(d) and project(v2)==s.zeros(d)
    assert project(jz)==s.diag(*[s.Rational(2*i-N,2) for i in range(d)])
    # p_i = sqrt(M*hbar*omega/2)*v_i.
    # (p1²-p2²)/(2*M*hbar*omega)=(v1²-v2²)/4.
    assert project((v1*v1-v2*v2)/4)==project(jz)
    # p1*p2/(M*hbar*omega)=(v1*v2)/2.
    assert project(v1*v2/2)==project(jx)
    # Projecting the squared observable is NOT squaring its projection.
    assert project(v1*v1)!=project(v1)*project(v1)
    # No finite-dimensional exact canonical [Q,X]=i*c*I: trace obstruction.
    assert s.trace(project(jz))==0
    print("occupation",N,"dimension",d,
          "P v_i P = 0; P (K1-K2)/(hbar omega) P = Jz; "
          "P p1p2/(M hbar omega) P = Jx")
print("PASS: exact fixed-N operator projection and finite-shell no-go, N=1..4")
