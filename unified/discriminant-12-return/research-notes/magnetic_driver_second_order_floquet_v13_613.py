#!/usr/bin/env python3
"""Check second-order kick and cubic van-Vleck Hamiltonian against exact spin-1/2 dynamics."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
Jx,Jy,Jz=sx/2,sy/2,sz/2
Jp=Jx+1j*Jy; Jm=Jx-1j*Jy

def exact(g,t,w=1.0):
    def rhs(s,y):
        U=y.reshape(2,2)
        H=-g/2*Jx-g/4*(np.exp(2j*w*s)*Jp+np.exp(-2j*w*s)*Jm)
        return (-1j*H@U).ravel()
    return solve_ivp(rhs,(0,t),np.eye(2,dtype=complex).ravel(),rtol=3e-13,atol=3e-15,method="DOP853").y[:,-1].reshape(2,2)

def approx(g,t,w=1.0):
    nu=2*w
    def K(s):
        K1=1j*g/(8*w)*(np.exp(1j*nu*s)*Jp-np.exp(-1j*nu*s)*Jm)
        K2=g*g/(16*w*w)*np.sin(nu*s)*Jz
        return K1+K2
    HF=(-g/2+g**3/(128*w*w))*Jx+g*g/(16*w)*Jz
    return expm(-1j*K(t))@expm(-1j*HF*t)@expm(1j*K(0))

t=1.234
print("g,Frobenius_error,error/g^3")
for g in (0.04,0.02,0.01):
    err=np.linalg.norm(exact(g,t)-approx(g,t))
    print(f"{g:.8g},{err:.12g},{err/g**3:.12g}")
