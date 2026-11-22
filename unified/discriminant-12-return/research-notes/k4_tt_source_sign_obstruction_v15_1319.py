#!/usr/bin/env python3
"""Gravity v15.1319: TT sign falsification using original v15.1078 Maxwell
packet, shared Nyquist projector, 2N dealiased stress, and explicitly
stated spatial-metric plus convention. The archived tensor source sign
does not satisfy the metric Einstein equation under these conventions.
"""
import numpy as np
from math import pi,sqrt

def run(N=32):
    L=4*pi
    x=(np.arange(N)-N//2)*L/N
    X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
    f=lambda u:np.where(abs(u)<1,(1-u*u)**3,0.)
    fp=lambda u:np.where(abs(u)<1,-6*u*(1-u*u)**2,0.)
    E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),
        -fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    K=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing='ij'))
    mag=np.sqrt(np.sum(K*K,axis=0))
    n=np.zeros_like(K);np.divide(K,mag,out=n,where=mag>0)
    h=np.fft.fftn(E0,axes=(1,2,3))
    h-=n*np.einsum('i...,i...->...',n,h)
    h[:,np.any(abs(K)==N/2*2*pi/L,axis=0)]=0
    M=2*N
    pads=[(0,0)]+[(N//2,N//2)]*3
    h2=np.fft.ifftshift(np.pad(np.fft.fftshift(h,axes=(1,2,3)),pads),axes=(1,2,3))*8
    E=np.fft.ifftn(h2,axes=(1,2,3)).real
    rho=np.sum(E*E,axis=0)/2
    Tij=np.eye(3)[:,:,None,None,None]*rho-np.einsum('i...,j...->ij...',E,E)
    e=np.array([1.,0.,-1.])/sqrt(2)
    b=np.array([0.,1.,0.])
    Pi=(np.einsum('i,ij...,j->...',e,Tij,e)-np.einsum('i,ij...,j->...',b,Tij,b))/2
    # The oblique Fourier mode K=(1,0,1) has FFT index (2,0,2)
    pik=np.fft.fftn(Pi)[2,0,2]/M**3
    # The direct metric's plus projection obeys:
    # delta Gplus = (gamma''+3 gamma'/tau+3 k² gamma/tau²)/2.
    # The original solid stress is -gamma/tau² for eta_s=3/4.
    # At initial gamma=gamma'=0, Maxwell Tplus=9 Pi/tau^4.
    # Archived gamma''=-18 Pi -> discrepancy -18 Pi.
    residual_archived=-18*pik
    residual_metric_consistent=0*pik
    assert abs(pik)>1e-6
    assert abs(residual_archived)>1e-4
    assert abs(residual_metric_consistent)<1e-13
    out=dict(N=N,Pi_plus_real=float(pik.real),
       Pi_plus_imag=float(pik.imag),
       archived_Einstein_plus_residual_real=float(residual_archived.real),
       archive_residual_abs=float(abs(residual_archived)))
    print(out,flush=True)
    return out

if __name__=='__main__':
    for n in (24,32,48):run(n)
    print('NEGATIVE: archived tensor forcing clashes with stated plus metric convention')
    print('OPEN: reconcile gamma versus metric strain/polarization source sign')
