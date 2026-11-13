#!/usr/bin/env python3
"""Gravity v15.911. Full velocity-ladder population under H=hbar*g*Jx.
u is m/s; tau=g*t. Curvature weighting below is a hypothetical comparator,
not a derived Cone correction or a derived physical clock.
"""
import math
import numpy as np
from scipy.linalg import expm

def ops(D):
    jp=np.zeros((D,D),dtype=complex)
    for a in range(D-1):
        jp[a+1,a]=math.sqrt((a+1)*(D-1-a))
    jm=jp.conj().T
    return (jp+jm)/2,(jp-jm)/(2j),np.diag(np.arange(D)-(D-1)/2)

def prob(D,a,tau,axis="x"):
    jx,jy,jz=ops(D)
    h={"x":jx,"y":jy,"none":np.zeros_like(jx)}[axis]
    return np.abs(expm(-1j*tau*h)[:,a])**2

for D in (2,3,4,5,7,10):
    jx,jy,jz=ops(D); initial=D-2 if D>2 else 1
    assert np.max(abs(jx@jy-jy@jx-1j*jz))<1e-12
    velocity_u=np.arange(D)-(D-2)/2
    m=initial-(D-1)/2
    for tau in np.linspace(0,2*np.pi,51):
        px,py=prob(D,initial,tau),prob(D,initial,tau,"y")
        assert abs(px.sum()-1)<1e-12
        assert np.max(abs(px-py))<1e-12
        assert abs(np.dot(velocity_u,px)-(0.5+m*np.cos(tau)))<2e-12
    assert np.max(abs(prob(D,initial,2*np.pi)-np.eye(D)[:,initial]))<1e-12

D=5; initial=3
for tau in (0,np.pi/4,np.pi/2,np.pi,2*np.pi):
    p=prob(D,initial,tau)
    print("tau=",tau,"p=",np.round(p,10),"mean X/u=",float(np.dot(np.arange(D)-1.5,p)))
ref=np.array([.25,.25,0,.25,.25])
assert np.max(abs(prob(5,3,np.pi/2)-ref))<1e-12
assert np.max(abs(prob(5,3,np.pi)-np.array([0,1,0,0,0])))<1e-12
# Non-SU(2) curvature-link perturbation is an arbitrary comparator.
jx,_,_=ops(5); pert=jx.copy(); epsilon=.15
for a in range(4):
    link=math.sqrt((a+1)*(4-a))
    factor=1+epsilon*(1/link-.5)
    pert[a+1,a]*=factor; pert[a,a+1]*=factor
p_pert=abs(expm(-1j*np.pi/2*pert)[:,3])**2
assert abs(p_pert.sum()-1)<1e-12 and max(abs(p_pert-ref))>1e-6
print("hypothetical epsilon",epsilon,"central-node probability",p_pert[2])
print("PASS finite D=2,3,4,5,7,10; SU2 Jx/Jy equality, 2pi revival, dark node; perturbed control differs")
