#!/usr/bin/env python3
"""v15.732: compact canonical scalar Cauchy stress -> sourced K4 scalar Weyl.
C7 compact packet w_R(cos2x+cos z), chidot=-chi at tau=1. Full
cutoff gradients, KG chi_ddot, stress pressure/energy/momentum derivative,
and exact pressure-corrected K4 scalar ADM/Weyl are included. This is
initial-slice constrained curvature, not a retarded strain measurement.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
def evaluate(R,N):
 v,ww=leggauss(N);x=R*v;weights=R*ww
 xx=x[:,None,None];zz=x[None,None,:]
 h=(1-v*v)**8
 hp=-16*v*(1-v*v)**7/R
 hpp=(-16*(1-v*v)**7+224*v*v*(1-v*v)**6)/R**2
 hx=h[:,None,None];hy=h[None,:,None];hz=h[None,None,:]
 w=hx*hy*hz
 wx=hp[:,None,None]*hy*hz
 wy=hx*hp[None,:,None]*hz
 wz=hx*hy*hp[None,None,:]
 lapw=hpp[:,None,None]*hy*hz+hx*hpp[None,:,None]*hz+hx*hy*hpp[None,None,:]
 mix=np.cos(2*xx)+np.cos(zz)
 phi=w*mix
 gx=wx*mix-2*w*np.sin(2*xx)
 gy=wy*mix
 gz=wz*mix-w*np.sin(zz)
 lap=lapw*mix-4*wx*np.sin(2*xx)-2*wz*np.sin(zz)-4*w*np.cos(2*xx)-w*np.cos(zz)
 grad2=gx*gx+gy*gy+gz*gz
 kg=2*gx+gz
 rho=(phi*phi+3*grad2)/2
 ptr=(3*phi*phi-3*grad2)/2
 volume=weights[:,None,None]*weights[None,:,None]*weights[None,None,:]
 phase=np.exp(-1j*(2*xx+zz))
 volnorm=np.sum(volume*w*w)
 fourier=lambda val:np.sum(volume*phase*val)/volnorm
 a=1/np.sqrt(3);K2=5.
 JP=a**3*fourier(rho)
 JS=a**3*fourier(ptr)
 # T^(0i)=-chidot grad_i/a², and iK.a^4 T^(0i) defines J_B.
 JB=1j*a*a*fourier(phi*kg)
 # From KG, chi_ddot=3chi+3Delta chi and grad(chidot)=-grad chi.
 JBdot=-1j*a*a*fourier((2*phi+3*lap)*kg)
 Pddot=3*np.sqrt(3)*JS/(2*K2)-9*(JBdot+JB)/(2*K2**2)
 PhiN=Pddot/(3*(1+K2))+np.sqrt(3)*(JP+JS)/(2*(1+K2))-3*JBdot/(2*K2*(1+K2))
 PsiN=np.sqrt(3)*JP/(2*(1+K2))+3*JB/(2*K2*(1+K2))
 W=K2*(PhiN+PsiN)/(2*a*a)
 assert np.min(rho)>-1e-12
 return {"JP":JP,"JS":JS,"JB":JB,"JBdot":JBdot,
         "Pddot":Pddot,"PhiN":PhiN,"PsiN":PsiN,"W":W}
small=evaluate(16.,96)
large=evaluate(32.,144)
target=83/120
for radius,d in ((16,small),(32,large)):
 print("R",radius,"Pddot",d["Pddot"],"W",d["W"],
       "abs_error_from_plane_wave",abs(d["W"]-target))
 assert abs(d["W"].imag)<1e-9
 assert d["W"].real>0.65
 assert abs(d["Pddot"]-9/25)<1e-7
assert abs(large["W"]-target)<abs(small["W"]-target)/3.8
assert abs(large["W"]-target)<0.009
print("PASS: compact positive-energy canonical scalar sources nonzero gauge-invariant K4 scalar Weyl")
print("PASS: full cutoff gradients included, convergence toward W=83/120 plane-wave result")
