#!/usr/bin/env python3
"""v15.1273: compare native vs 2N-dealiased Maxwell rho/flux/stress modes.
Same v15.1078 compact source and v15.1267 Nyquist rule. No parent edits.
"""
import numpy as np
from math import pi,sqrt

def run(N,tau=1.08):
    L=4*pi; x=(np.arange(N)-N//2)*L/N
    X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
    f=lambda u:np.where(abs(u)<1,(1-u*u)**3,0.)
    fp=lambda u:np.where(abs(u)<1,-6*u*(1-u*u)**2,0.)
    E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),-fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    freq=np.fft.fftfreq(N,d=L/N)*2*pi
    q=np.array(np.meshgrid(freq,freq,freq,indexing='ij'))
    k=np.sqrt(np.sum(q*q,axis=0));n=np.zeros_like(q)
    np.divide(q,k,out=n,where=k>0)
    h=np.fft.fftn(E0,axes=(1,2,3))
    h-=n*np.einsum('i...,i...->...',n,h)
    h[:,np.any(abs(q)==N/2*2*pi/L,axis=0)]=0
    curl=1j*np.cross(q,h,axis=0)
    xi=sqrt(3)*np.log(tau)
    sinc=np.zeros_like(k);np.divide(np.sin(k*xi),k,out=sinc,where=k>0)
    Eh=h*np.cos(k*xi);Bh=-curl*sinc
    def stress(M):
        def inv(v):
            if M!=N:
                pad=[(0,0)]*(v.ndim-3)+[((M-N)//2,(M-N)//2)]*3
                v=np.fft.ifftshift(np.pad(np.fft.fftshift(v,axes=(-3,-2,-1)),pad),
                                   axes=(-3,-2,-1))*(M/N)**3
            return np.fft.ifftn(v,axes=(-3,-2,-1)).real
        E=inv(Eh);B=inv(Bh)
        rho=np.sum(E*E+B*B,axis=0)/2
        F=np.cross(E,B,axis=0)
        T=np.eye(3)[:,:,None,None,None]*rho-np.einsum('i...,j...->ij...',E,E)-np.einsum('i...,j...->ij...',B,B)
        ft=lambda z:np.fft.fftn(z,axes=(-3,-2,-1))/M**3
        return ft(rho),ft(F),ft(T)
    A=stress(N);D=stress(2*N)
    signed=np.rint(np.fft.fftfreq(N)*N).astype(int)
    ind=np.mod(signed,2*N)
    ok=np.abs(signed)<N/2
    mask=ok[:,None,None]&ok[None,:,None]&ok[None,None,:]
    low=np.abs(signed)<N/3
    lmask=low[:,None,None]&low[None,:,None]&low[None,None,:]
    fixed=np.abs(signed)<=2
    fmask=fixed[:,None,None]&fixed[None,:,None]&fixed[None,None,:]
    rows=[]
    for name,a,d in zip(('rho','flux','stress'),A,D):
        d=d[...,ind[:,None,None],ind[None,:,None],ind[None,None,:]]
        scale=float(abs(d[...,mask]).max())
        delta=abs(a-d)
        rows.append(dict(sector=name,max_abs=float(delta[...,mask].max()),
                         lowband_relative=float(delta[...,lmask].max()/scale),
                         fixed_relative=float(delta[...,fmask].max()/scale)))
    mean=float(abs(A[0][0,0,0]-D[0][0,0,0]))
    assert mean<1e-12
    assert all(z['max_abs']>1e-8 for z in rows)
    result=dict(N=N,tau=tau,mean_error=mean,sectors=rows)
    print(result,flush=True)
    return result

if __name__=='__main__':
    [run(N) for N in (16,24,32,40,48)]
    print('PASS nonzero-band source incompatibility, mean preserved')
    print('OPEN full dealiased Einstein-K4 SVT metric/constraint replay')
