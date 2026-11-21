#!/usr/bin/env python3
"""v15.1277: sourced initial-slice scalar Einstein constraints, k>0.
Original compact Maxwell field, Nyquist-clean transverse projection, 2N
dealiased stress, v15.729 K4 scalar Bardeen transfer at P=Pdot=0.
Not full time-dependent ADM or vector/TT closure."""
import numpy as np
from math import pi

def run(N=24):
    L=4*pi
    x=(np.arange(N)-N//2)*L/N
    X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
    f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
    fp=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
    E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),
        -fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    freq=np.fft.fftfreq(N,d=L/N)*2*pi
    K=np.array(np.meshgrid(freq,freq,freq,indexing='ij'))
    k2=(K*K).sum(axis=0);k=np.sqrt(k2)
    n=np.zeros_like(K);np.divide(K,k,out=n,where=k>0)
    H=np.fft.fftn(E0,axes=(1,2,3))
    H-=n*np.einsum('i...,i...->...',n,H)
    H[:,np.any(abs(K)==N/2*2*pi/L,axis=0)]=0
    M=2*N
    def padded(v):
        pads=[(0,0)]*(v.ndim-3)+[(N//2,N//2)]*3
        return np.fft.ifftshift(np.pad(np.fft.fftshift(v,axes=(-3,-2,-1)),pads),axes=(-3,-2,-1))*8
    E=np.fft.ifftn(padded(H),axes=(1,2,3)).real
    rho=(E*E).sum(axis=0)/2
    ft=lambda x:np.fft.fftn(x,axes=(-3,-2,-1))/M**3
    R=ft(rho)
    Tij=np.eye(3)[:,:,None,None,None]*rho-np.einsum('i...,j...->ij...',E,E)
    Th=ft(Tij)
    idx=np.mod(np.rint(np.fft.fftfreq(N)*N).astype(int),M)
    take=lambda z:z[...,idx[:,None,None],idx[None,:,None],idx[None,None,:]]
    r=take(R);T=take(Th)
    Tnn=np.einsum('i...,ij...,j...->...',n,T,n)
    valid=(k2>0)&np.all(abs(K)<N/2*2*pi/L,axis=0)
    Pdd=np.zeros_like(r)
    np.divide(9*(3*Tnn-r),2*k2,out=Pdd,where=valid)
    JBdot=-3*k2*Tnn
    Phi=np.zeros_like(r);Psi=np.zeros_like(r);Psidot=np.zeros_like(r)
    Phi[valid]=(Pdd[valid]/3-3*r[valid]-3*JBdot[valid]/(2*k2[valid]))/(1+k2[valid])
    Psi[valid]=-3*r[valid]/(2*(1+k2[valid]))
    Psidot[valid]=(-Pdd[valid]/3+3*r[valid]+3*JBdot[valid]/(2*k2[valid]))/(1+k2[valid])
    Q=Psidot+Phi
    # Independently derived metric-to-Einstein operators v15.1276.
    G00=6*(k2*Psi+Q)
    G0long=-2j*k*Q
    Gshear=3*k2*(Psi-Phi)
    # Maxwell and solid combined, at tau=1, P=Pdot=0.
    S00=-9*r-6*Psi
    Sshear=9*(r-3*Tnn)/2
    errs=(float(abs((G00-S00)[valid]).max()),
          float(abs(G0long[valid]).max()),
          float(abs((Gshear-Sshear)[valid]).max()))
    maxwell_only=float(abs((G00+9*r)[valid]).max())
    out={'N':N,'modes':int(valid.sum()),'rho_mean':float(r[0,0,0].real),
         'Hamiltonian':errs[0],'longitudinal_momentum':errs[1],
         'scalar_spatial_shear':errs[2],
         'negative_Maxwell_only_Hamiltonian':maxwell_only}
    assert max(errs)<3e-12 and maxwell_only>1e-8,out
    print(out,flush=True)
    return out

if __name__=='__main__':
    for N in (16,24,32,40,48):run(N)
    print('PASS initial nonzero scalar Hamiltonian, longitudinal momentum and shear')
    print('OPEN time propagation, transverse vector/tensor and remaining Einstein equations')
