#!/usr/bin/env python3
"""v15.708: conservation guarantees linear metric source gauge invariance.

Fourier convention exp(-i omega t+i k z), q_mu=(-omega,0,0,k).
T^{mu nu} is a kinematically conserved rank-one-stress completion.
It need not be a realizable positive-energy localized source on K4 FLRW.
"""
import sympy as s
k,w=s.symbols("k omega",nonzero=True,real=True)
x,y,z=s.symbols("x y z",real=True)
S=s.Matrix([[x*x,x*y,x*z],[x*y,y*y,y*z],[x*z,y*z,z*z]])
T=s.zeros(4)
for i in range(3):
    for j in range(3): T[i+1,j+1]=S[i,j]
for j in range(3): T[0,j+1]=T[j+1,0]=k*T[3,j+1]/w
T[0,0]=k*k*T[3,3]/(w*w)
q=s.Matrix([-w,0,0,k])
xi=s.Matrix(s.symbols("xi0:4"))
assert (q.T*T).applyfunc(s.simplify)==s.zeros(1,4)
pure_gauge=q*xi.T+xi*q.T
assert s.simplify(s.trace(pure_gauge*T))==0
print("PASS: flat local Fourier stress conservation and gauge-invariant metric-source contraction")
