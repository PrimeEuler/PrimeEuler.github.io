#!/usr/bin/env python3
"""Gravity v15.1271: Maxwell full four-current stress Ward, spectral aliasing gate.
Independent compact-source reproducer; no changes to archived parents.
"""
import numpy as np
from math import sqrt,pi

def run(N,oversample=2,cutoff=False):
    L=4*pi; t=1.08; dx=L/N; x=(np.arange(N)-N//2)*dx
    X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
    f=lambda u:np.where(abs(u)<1,(1-u*u)**3,0.)
    fp=lambda u:np.where(abs(u)<1,-6*u*(1-u*u)**2,0.)
    e0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),-fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    freq=np.fft.fftfreq(N,d=dx)*2*pi
    q=np.array(np.meshgrid(freq,freq,freq,indexing='ij'))
    k=np.sqrt(np.sum(q*q,axis=0))
    n=np.zeros_like(q);np.divide(q,k,out=n,where=k>0)
    h=np.fft.fftn(e0,axes=(1,2,3))
    h-=n*np.einsum('i...,i...->...',n,h)
    nyq=np.any(abs(q)==N/2*2*pi/L,axis=0);h[:,nyq]=0
    if cutoff:
        keep=np.all(abs(q*L/(2*pi))<N/3,axis=0);h[:,~keep]=0
    c=1j*np.cross(q,h,axis=0);xi=sqrt(3)*np.log(t)
    sinc=np.zeros_like(k);np.divide(np.sin(k*xi),k,out=sinc,where=k>0)
    Ehat=h*np.cos(k*xi);Bhat=-c*sinc
    Ehd=-h*k*np.sin(k*xi)*sqrt(3)/t
    Bhd=-c*np.cos(k*xi)*sqrt(3)/t
    M=N*oversample
    def inv(v):
        if M!=N:
            pad=[(0,0)]*(v.ndim-3)+[((M-N)//2,(M-N)//2)]*3
            v=np.fft.ifftshift(np.pad(np.fft.fftshift(v,axes=(-3,-2,-1)),pad),
                               axes=(-3,-2,-1))*(M/N)**3
        return np.fft.ifftn(v,axes=(-3,-2,-1))
    Ec=inv(Ehat);Bc=inv(Bhat)
    E=Ec.real;B=Bc.real;Ed=inv(Ehd).real;Bd=inv(Bhd).real
    rho=np.einsum('i...,i...->...',E,E)/2+np.einsum('i...,i...->...',B,B)/2
    rhod=np.einsum('i...,i...->...',E,Ed)+np.einsum('i...,i...->...',B,Bd)
    F=np.cross(E,B,axis=0)
    Fd=np.cross(Ed,B,axis=0)+np.cross(E,Bd,axis=0)
    eye=np.eye(3)[:,:,None,None,None]
    T=eye*rho-np.einsum('i...,j...->ij...',E,E)-np.einsum('i...,j...->ij...',B,B)
    fft=lambda v:np.fft.fftn(v,axes=(-3,-2,-1))/M**3
    freqM=np.fft.fftfreq(M,d=L/M)*2*pi
    Q=np.array(np.meshgrid(freqM,freqM,freqM,indexing='ij'))
    energy=fft(rhod)+sqrt(3)/t*1j*np.einsum('j...,j...->...',Q,fft(F))
    mom=fft(Fd)+sqrt(3)/t*1j*np.einsum('j...,ij...->i...',Q,fft(T))
    mask=np.all(abs(Q*L/(2*pi))<N/3,axis=0) if cutoff else np.ones((M,M,M),bool)
    row=dict(N=N,method=('cutoff' if cutoff else 'full')+'-'+str(oversample),
             rho=float(rho.mean()),energy=float(abs(energy).max()),
             momentum=float(abs(mom).max()),
             energy_kept=float(abs(energy[mask]).max()),
             momentum_kept=float(abs(mom[:,mask]).max()),
             max_imag=float(max(abs(Ec.imag).max(),abs(Bc.imag).max())))
    if oversample==2 or cutoff:
        assert row['energy_kept']<2e-12
        assert row['momentum_kept']<2e-12
    print(row,flush=True)
    return row

if __name__=='__main__':
    for N in (16,24,32,40,48):
        raw=run(N,1,False)
        full=run(N,2,False)
        band=run(N,1,True)
        assert raw['energy']>1e-6 and raw['momentum']>1e-6
        assert full['energy']<2e-12 and full['momentum']<2e-12
        assert band['energy_kept']<2e-12 and band['momentum_kept']<2e-12
    print('PASS Maxwell 4-stress conservation: full dealiased / retained 2/3 band')
    print('OPEN Einstein+K4 gravitational constraint closure, metric and causal detector')
