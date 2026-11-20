#!/usr/bin/env python3
"""Gravity v15.1262: all nonzero FFT modes of compact Maxwell source
to ordinary K4 scalar/vector/tensor full electric Riemann, real space.

The k=0 source/background is deliberately EXCLUDED; this is the
mean-subtracted perturbation, NOT a solved FLRW background response.
No causal photon/mirror/clock detector and no quarter-grid coupling.
Physical original source v15.1078; K4 equations v15.728/729,
v15.710/721, v15.750, curvature v15.787, sign repair v15.1226.
"""
import numpy as np
from scipy.interpolate import CubicSpline
from math import sqrt, pi

def run(N=32,nt=9,tf=1.08):
    L=4*pi
    dx=L/N
    x=(np.arange(N)-N//2)*dx
    X=x[:,None,None]; Y=x[None,:,None]; Z=x[None,None,:]
    f=lambda u:np.where(abs(u)<1,(1-u*u)**3,0.)
    fp=lambda u:np.where(abs(u)<1,-6*u*(1-u*u)**2,0.)
    E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),
        -fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    freq=np.fft.fftfreq(N,dx)*2*pi
    K=np.array(np.meshgrid(freq,freq,freq,indexing='ij'))
    k2=np.sum(K*K,axis=0); k=np.sqrt(k2); nz=k2>0
    invk=np.zeros_like(k); invk[nz]=1/k[nz]
    n=K*invk
    Eh=np.fft.fftn(E0,axes=(1,2,3))
    # Grid sampling introduces alias-related Gauss errors; project the
    # sampled initial E onto discrete transverse Fourier subspace.
    Eh-=n*np.einsum('i...,i...->...',n,Eh)
    curl=1j*np.cross(K,Eh,axis=0)
    delta=np.eye(3)[:,:,None,None,None]
    nn=np.einsum('i...,j...->ij...',n,n)
    projector=delta-nn
    fft=lambda a:np.fft.fftn(a,axes=tuple(range(a.ndim-3,a.ndim)))/N**3
    def source(t):
        xi=sqrt(3)*np.log(t)
        fac=np.zeros_like(k)
        np.divide(np.sin(k*xi),k,out=fac,where=nz)
        E=np.fft.ifftn(Eh*np.cos(k*xi),axes=(1,2,3)).real
        B=np.fft.ifftn(-curl*fac,axes=(1,2,3)).real
        rho=np.sum(E*E+B*B,axis=0)/2
        flux=np.cross(E,B,axis=0)
        Tij=-(np.einsum('i...,j...->ij...',E,E)
              +np.einsum('i...,j...->ij...',B,B))+delta*rho
        r=fft(rho); F=fft(flux); T=fft(Tij)
        Fn=np.einsum('i...,i...->...',n,F)
        Fperp=F-n*Fn
        Tnn=np.einsum('i...,ij...,j...->...',n,T,n)
        Tn=np.einsum('ij...,j...->i...',T,n)
        Tnperp=Tn-n*Tnn
        Tperp=np.einsum('ia...,ab...,bj...->ij...',projector,T,projector)
        PiTT=Tperp-projector*np.einsum('ij...,ij...->...',projector,T)/2
        return r,Fn,Fperp,Tnn,Tnperp,PiTT
    times=np.linspace(1.,tf,nt)
    series=[source(t) for t in times]
    spl=[CubicSpline(times,np.stack([v[i] for v in series]),axis=0)
         for i in range(6)]
    eta=.75
    betaS=(8*eta*(1+k2)-3*k2)/3
    betaV=2*eta*(4+3*k2)/3
    betaT=3*k2+8*eta/3
    den=4+3*k2
    P=np.zeros((2,N,N,N),complex)
    V=np.zeros((2,3,N,N,N),complex)
    T=np.zeros((2,3,3,N,N,N),complex)
    def deriv(t,P,V,T):
        r,Fn,Fperp,Tnn,Tnperp,PiTT=(s(t) for s in spl)
        sourceS=np.zeros_like(r)
        np.divide(9*(3*Tnn-r),2*k2*t**4,out=sourceS,where=nz)
        Pdd=-3*P[1]/t-betaS*P[0]/t**2+sourceS
        sourceV=np.zeros_like(Tnperp)
        np.divide(-18j*Tnperp,k*t**4,out=sourceV,where=nz)
        Vdd=-3*V[1]/t-betaV*V[0]/t**2+sourceV
        Tdd=-3*T[1]/t-betaT*T[0]/t**2-18*PiTT/t**4
        return (np.stack([P[1],Pdd]),
                np.stack([V[1],Vdd]),
                np.stack([T[1],Tdd]))
    for i in range(nt-1):
        t=times[i]; h=times[i+1]-t
        u=(P,V,T)
        a=deriv(t,*u)
        b=deriv(t+h/2,*(x+h*y/2 for x,y in zip(u,a)))
        c=deriv(t+h/2,*(x+h*y/2 for x,y in zip(u,b)))
        d=deriv(t+h,*(x+h*y for x,y in zip(u,c)))
        for x,aa,bb,cc,dd in zip(u,a,b,c,d):
            x+=(h/6)*(aa+2*bb+2*cc+dd)
    t=tf
    r,Fn,Fperp,Tnn,Tnperp,PiTT=source(t)
    Pdd,Vdd,Tdd=(v[1] for v in deriv(t,P,V,T))
    JBdot=(-3*k2*Tnn+1j*sqrt(3)*k*Fn)/t**2
    Jphi=-sqrt(3)*r/t
    quotient=np.zeros_like(JBdot)
    np.divide(JBdot,2*k2,out=quotient,where=nz)
    Phi=((t*t*Pdd+2*t*P[1])/3+sqrt(3)*Jphi/t-3*quotient)/(1+k2)
    S=-3*k2*Phi/t**2
    Aiso=3*r/t**4
    Bv=4*t*V[1]/(sqrt(3)*den)+18*Fperp/(t*t*den)
    FperpDot=-1j*sqrt(3)*k*Tnperp/t
    BvDot=4*(V[1]+t*Vdd)/(sqrt(3)*den)+18*(FperpDot/t**2-2*Fperp/t**3)/den
    vTide=-1j*k*(BvDot+Bv/t)/(2*t/sqrt(3))
    tensorTide=-(Tdd+2*T[1]/t)/2
    Ehat=Aiso*delta+S*(nn-delta/3)
    Ehat+=np.einsum('i...,j...->ij...',n,vTide)
    Ehat+=np.einsum('i...,j...->ij...',vTide,n)
    Ehat+=tensorTide
    # k=0 is a change in homogeneous cosmological background, and must
    # not be passed through k>0 scalar/vector constraints.
    Ehat[:,:,0,0,0]=0
    Ehat=(Ehat+np.swapaxes(Ehat,0,1))/2
    # FFT Nyquist modes otherwise violate Hermitian conjugate pairing.
    ix=np.mod(-np.arange(N),N)
    partner=np.conj(Ehat[:,:,ix,:,:][:,:,:,ix,:][:,:,:,:,ix])
    Ehat=(Ehat+partner)/2
    complexField=np.fft.ifftn(N**3*Ehat,axes=(2,3,4))
    Er=complexField.real
    rho=np.fft.ifftn(N**3*r).real
    expected=9*(rho-rho.mean())/t**4
    resid=float(np.max(abs(np.trace(Er,axis1=0,axis2=1)-expected)))
    imag=float(np.max(abs(complexField.imag)))
    gauss=float(np.max(abs(np.einsum('i...,i...->...',K,Eh)))/np.max(abs(Eh)))
    center=Er[(slice(None),slice(None),N//2,N//2,N//2)]
    assert resid<3e-12 and imag<3e-12 and gauss<3e-12
    assert np.max(abs(Er-np.swapaxes(Er,0,1)))<3e-12
    result=dict(N=N,t=tf,center=center.tolist(),
                trace=float(np.trace(center)),rho_center=float(rho[N//2,N//2,N//2]),
                rho_mean=float(rho.mean()),trace_resid=resid,
                max_imag=imag,gauss_resid=gauss)
    print(result,flush=True)
    return result
if __name__=='__main__':
    for N in [32,40,48]:run(N)
    print('PASS all nonzero FFT modes to mean-subtracted local full electric Riemann')
    print('OPEN homogeneous FLRW response, converged continuum, optical detector')
