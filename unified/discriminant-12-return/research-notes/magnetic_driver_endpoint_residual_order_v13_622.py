#!/usr/bin/env python3
"""Residual-order test for the v13.617 magnetic-driver endpoint laws."""
import numpy as np
from scipy.integrate import solve_ivp
pi=np.pi
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
Jx,Jy,Jz=sx/2,sy/2,sz/2; Jp=Jx+1j*Jy; Jm=Jx-1j*Jy
down=np.array([0,1],complex)

def U(g,t):
    def rhs(s,y):
        M=y.reshape(2,2)
        H=-g/2*Jx-g/4*(np.exp(2j*s)*Jp+np.exp(-2j*s)*Jm)
        return (-1j*H@M).ravel()
    return solve_ivp(rhs,(0,t),np.eye(2,dtype=complex).ravel(),
                     rtol=2e-13,atol=2e-15,method="DOP853").y[:,-1].reshape(2,2)

print("eps,j,phase_res/eps^5,inversion_res/eps^6")
for eps in (.20,.10,.05):
    half=U(eps,pi/eps)@down
    dphi_half=(np.angle(half[0])-np.angle(half[1])-pi/2+pi)%(2*pi)-pi
    full=U(eps,2*pi/eps)@down
    p=abs(full[0])**2
    for j in (.5,1.,1.5):
        phase=2*j*dphi_half
        cphi=j*(50-3*pi)/3072
        rphi=phase-j*eps/4-cphi*eps**3
        infid=1-p**(2*j)
        cp=j*(pi*pi+152-16*j)/32768
        rp=infid-j*eps**2/32-cp*eps**4
        print(f"{eps:.2f},{j:g},{rphi/eps**5:.12g},{rp/eps**6:.12g}")
