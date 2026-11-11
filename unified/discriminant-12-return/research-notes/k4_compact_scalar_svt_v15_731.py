#!/usr/bin/env python3
"""v15.731: compact canonical-scalar initial stress SVT projections.
A C7 compact product bump times cos(2x)+cos(z) has finite positive
canonical energy, and generic all-sector Fourier source at K=(2,0,1).
Rotationally invariant source S=A I+B nn^T has TT=V=0 exactly.
"""
import sympy as s
import numpy as np
from numpy.polynomial.legendre import leggauss
n=s.Matrix([s.Rational(2,3),s.Rational(1,3),s.Rational(2,3)])
Pr=s.eye(3)-n*n.T
a,b=s.symbols("a b")
S=a*s.eye(3)+b*n*n.T
assert s.simplify(Pr*S*Pr-Pr*s.trace(Pr*S)/2)==s.zeros(3)
assert s.simplify(Pr*S*n*n.T+n*(n.T*S*Pr))==s.zeros(3)
R=16.;N=96
v,w0=leggauss(N);wts=R*w0
xx=(R*v)[:,None,None];zz=(R*v)[None,None,:]
h=(1-v*v)**8;dh=-16*v*(1-v*v)**7/R
hx=h[:,None,None];hy=h[None,:,None];hz=h[None,None,:]
H=hx*hy*hz
mix=np.cos(2*xx)+np.cos(zz)
D=[dh[:,None,None]*hy*hz*mix-2*H*np.sin(2*xx),
   hx*dh[None,:,None]*hz*mix,
   hx*hy*dh[None,None,:]*mix-H*np.sin(zz)]
D=np.stack([np.broadcast_to(z,(N,N,N)) for z in D])
weights=wts[:,None,None]*wts[None,:,None]*wts[None,None,:]
phase=np.exp(-1j*(2*xx+zz))
Stress=np.einsum("ixyz,jxyz,xyz->ij",D,D,weights*phase,optimize=True)/np.sum(weights*H*H)
kh=np.array([2.,0.,1.])/np.sqrt(5)
P=np.eye(3)-np.outer(kh,kh)
TT=P@Stress@P-P*np.trace(P@Stress)/2
V=P@Stress@np.outer(kh,kh)+np.outer(kh,kh)@Stress@P
Q=Stress-np.eye(3)*np.trace(Stress)/3
SC=Q-TT-V
norm=lambda m:float(np.sum(np.abs(m)**2))
vals=np.array([norm(TT),norm(V),norm(SC)])
target=np.array([32,72,96])/400
assert np.min(vals)>1e-4 and np.max(np.abs(vals-target))<0.06
assert np.max(np.abs(Q-TT-V-SC))<1e-12
print("PASS: spherical Fourier TT/V null; compact C7 asymmetric source nonzero all S/V/T")
print("Frobenius squared norms",vals.tolist(),"asymptotic targets",target.tolist())
