#!/usr/bin/env python3
"""v15.1270: strict 2/3-band Maxwell scalar Ward projection check.
Uses v15.1078 compact E0 and shared v15.1267 Nyquist mask. Does not modify
archived parents; exact spectral evolution derivatives, dealiased quadratic
stress. Finite-grid discrete calculation, not full ADM constraint closure.
"""
import numpy as np
from math import pi,sqrt

def run(N=32,tau=1.08,padding=1):
    L=4*pi; dx=L/N; x=(np.arange(N)-N//2)*dx
    X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
    f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
    fp=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
    E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),
        -fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=dx)*2*pi]*3),indexing="ij"))
    k=np.sqrt(np.sum(q*q,axis=0))
    n=np.zeros_like(q); np.divide(q,k,out=n,where=k>0)
    h=np.fft.fftn(E0,axes=(1,2,3))
    h-=n*np.einsum("i...,i...->...",n,h)
    mask=np.any(abs(q)==N/2*2*pi/L,axis=0)
    h[:,mask]=0
    band=np.all(abs(q*L/(2*pi))<N/3,axis=0)
    h[:,~band]=0
    curl=1j*np.cross(q,h,axis=0)
    xi=sqrt(3)*np.log(tau)
    sinc=np.zeros_like(k); np.divide(np.sin(k*xi),k,out=sinc,where=k>0)
    EH=h*np.cos(k*xi); BH=-curl*sinc
    EHdot=-h*np.sin(k*xi)*k*sqrt(3)/tau
    BHdot=-curl*np.cos(k*xi)*sqrt(3)/tau
    M=padding*N
    def enlarged(v):
        if padding==1: return v
        pad=[(0,0)]*(v.ndim-3)+[((M-N)//2,(M-N)//2)]*3
        return np.fft.ifftshift(np.pad(np.fft.fftshift(v,axes=(-3,-2,-1)),pad),
                                axes=(-3,-2,-1))*(M/N)**3
    def inverse(v): return np.fft.ifftn(enlarged(v),axes=(-3,-2,-1))
    Ec=inverse(EH); Bc=inverse(BH)
    E=Ec.real; B=Bc.real
    Ed=inverse(EHdot).real; Bd=inverse(BHdot).real
    rho=np.sum(E*E+B*B,axis=0)/2
    rhod=np.sum(E*Ed+B*Bd,axis=0)
    F=np.cross(E,B,axis=0)
    fft=lambda v:np.fft.fftn(v,axes=(-3,-2,-1))/M**3
    R=fft(rho); Rd=fft(rhod); Fh=fft(F)
    qm=np.array(np.meshgrid(*([np.fft.fftfreq(M,d=L/M)*2*pi]*3),indexing="ij"))
    divF=1j*np.einsum("i...,i...->...",qm,Fh)
    cont=Rd+sqrt(3)*divF/tau
    bandout=np.all(abs(qm*L/(2*pi))<N/3,axis=0)
    Jphi=-sqrt(3)*R/tau;Jpsi=Jphi
    Jphid=-sqrt(3)*(Rd/tau-R/tau**2)
    JB=-sqrt(3)*divF/tau
    ward=tau*Jphid+sqrt(3)*JB+Jpsi
    row={"N":N,"padding":padding,"tau":tau,
         "retained_continuity_residual":float(abs(cont[bandout]).max()),
         "retained_scalar_ward_residual":float(abs(ward[bandout]).max()),
         "continuity_residual":float(abs(cont).max()),
         "scalar_ward_residual":float(abs(ward).max()),
         "max_imag":float(max(abs(Ec.imag).max(),abs(Bc.imag).max())),
         "gauss_relative":float(abs(np.einsum("i...,i...->...",q,h)).max()/abs(h).max()),
         "rho_mean":float(rho.mean())}
    assert row["max_imag"]<2e-13 and row["gauss_relative"]<3e-12
    assert row["retained_continuity_residual"]<2e-12
    assert row["retained_scalar_ward_residual"]<2e-12
    print(row,flush=True)
    return row

if __name__=="__main__":
    for N in (16,24,32,40,48):
        run(N,padding=1)
    print("PASS projected 2/3-band Maxwell scalar Ward on native grid")
    print("OPEN full metric and constraint completion; nonretained modes are not conserved")
