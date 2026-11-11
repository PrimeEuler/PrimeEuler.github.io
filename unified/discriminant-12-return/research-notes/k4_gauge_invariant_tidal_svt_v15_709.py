#!/usr/bin/env python3
"""v15.709: exact local linearized gauge-invariant tidal R0i0j SVT response.

Fourier phase exp(-i omega t+i k z); local flat metric, not full K4 FLRW.
Scalar Newtonian-gauge potentials Phi,Psi; metric TT plus/cross P,C;
vector shift Vx,Vy and vector shear Hx,Hy. Riemann invariant under
linearized diffeomorphisms but potential ratios need sourced constraints.
"""
import sympy as s
w,k=s.symbols("omega k",real=True,nonzero=True)
Phi,Psi,P,C,Vx,Vy,Hx,Hy=s.symbols("Phi Psi P C V_x V_y H_x H_y")
h=s.zeros(4)
h[0,0]=-2*Phi
for i in (1,2,3):h[i,i]=-2*Psi
h[1,1]+=P;h[2,2]-=P
h[1,2]=h[2,1]=C
h[0,1]=h[1,0]=Vx;h[0,2]=h[2,0]=Vy
h[1,3]=h[3,1]=Hx;h[2,3]=h[3,2]=Hy
q=s.Matrix([-w,0,0,k])
def tidal(metric):
    return s.Matrix(3,3,lambda i,j:s.simplify((
        -q[0]*q[i+1]*metric[0,j+1]-q[j+1]*q[0]*metric[i+1,0]
        +q[0]**2*metric[i+1,j+1]+q[i+1]*q[j+1]*metric[0,0])/2))
E=tidal(h)
expected=s.Matrix([
[-w*w*Psi+w*w*P/2,w*w*C/2,(w*k*Vx+w*w*Hx)/2],
[w*w*C/2,-w*w*Psi-w*w*P/2,(w*k*Vy+w*w*Hy)/2],
[(w*k*Vx+w*w*Hx)/2,(w*k*Vy+w*w*Hy)/2,-w*w*Psi-k*k*Phi]])
assert (E-expected).applyfunc(s.simplify)==s.zeros(3)
xi=s.Matrix(s.symbols("xi0:4"))
dh=s.I*(q*xi.T+xi*q.T)
assert tidal(dh)==s.zeros(3)
lamT=-w*w*Psi
lamL=-w*w*Psi-k*k*Phi
assert s.simplify(lamL/lamT-1-k*k*Phi/(w*w*Psi))==0
assert s.simplify(E[0,2].subs(Hx,-k*Vx/w))==0
assert s.simplify((lamL/lamT).subs({Phi:0})-1)==0
assert s.simplify((lamL/lamT).subs({Phi:Psi})-(1+k*k/(w*w)))==0
print("PASS: local tidal R0i0j gauge-invariant under arbitrary linearized diffeomorphism")
print("PASS: scalar tide depends on Phi/Psi; vector tide on k V+omega H")
