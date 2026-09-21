#!/usr/bin/env python3
"""Numerically extract the next stroboscopic magnetic-driver coefficients."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import logm
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
Jx,Jy,Jz=sx/2,sy/2,sz/2; Jp=Jx+1j*Jy; Jm=Jx-1j*Jy
def floquet(g):
    T=np.pi
    def rhs(t,y):
        U=y.reshape(2,2)
        H=-g/2*Jx-g/4*(np.exp(2j*t)*Jp+np.exp(-2j*t)*Jm)
        return (-1j*H@U).ravel()
    U=solve_ivp(rhs,(0,T),np.eye(2,dtype=complex).ravel(),rtol=2e-12,atol=2e-14,method="DOP853").y[:,-1].reshape(2,2)
    H=1j*logm(U)/T
    return np.trace(H@sx).real,np.trace(H@sz).real
print("g, cubic_x, quartic_z")
for g in (.04,.02,.01):
    a,b=floquet(g)
    print(f"{g:.8g},{(a+g/2)/g**3:.12g},{(b+g*g/16)/g**4:.12g}")
print("targets: 1/128 =",1/128," ; -1/256 =",-1/256)
