#!/usr/bin/env python3
import numpy as np
from scipy.integrate import solve_ivp

def jmats(j):
    m=np.arange(-j,j+1); d=len(m)
    Jz=np.diag(m); Jp=np.zeros((d,d),complex)
    for k,mm in enumerate(m[:-1]):
        Jp[k+1,k]=np.sqrt((j-mm)*(j+mm+1))
    Jm=Jp.T; Jx=(Jp+Jm)/2
    return Jx,Jz,Jp,Jm

def run(j,eps,n=20001):
    g=eps; w=1.; T=2*np.pi/g
    Jx,Jz,Jp,Jm=jmats(j); d=Jx.shape[0]
    psi0=np.zeros(d,complex); psi0[0]=1
    def rhs(t,y):
        H=-g/2*Jx-g/4*(np.exp(2j*w*t)*Jp+np.exp(-2j*w*t)*Jm)
        return -1j*H@y
    ts=np.linspace(0,T,n)
    sol=solve_ivp(rhs,(0,T),psi0,t_eval=ts,rtol=2e-11,atol=2e-13,method="DOP853")
    ex=sol.y.T
    lam,V=np.linalg.eigh(Jx); c=V.conj().T@psi0
    rw=np.array([V@(np.exp(1j*g*lam*t/2)*c) for t in ts])
    pe=np.abs(ex)**2; pr=np.abs(rw)**2
    maxpop=np.max(np.abs(pe-pr))
    inv=1-pe[-1,-1]
    mid=n//2
    phase=np.unwrap(np.angle(ex[mid]/rw[mid]))
    spread=phase.max()-phase.min()
    return maxpop,spread,inv

print("eps,j,max_population_error,phase_spread_Tpi_over_2,inversion_infidelity")
for eps in (0.02,0.05,0.10,0.20):
    for j in (0.5,1.0,1.5):
        vals=run(j,eps)
        print(f"{eps:.2f},{j:g},"+",".join(f"{x:.12g}" for x in vals))
