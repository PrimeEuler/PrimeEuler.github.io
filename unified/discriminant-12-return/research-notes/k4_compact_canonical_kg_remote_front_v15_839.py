#!/usr/bin/env python3
"""v15.839: full-spectrum 3D compact canonical scalar at remote receiver.

On a=tau/sqrt3, initial chi=w_R cos(2x+y+1.4z), chi_dot=-chi.
With s=log(tau), each Fourier component evolves EXACTLY as
chi_k=tau^-1 cos(sqrt(3|k|^2-1)*s) chi_k(0).
A smooth C7 ball radius 2.5 at (6,0,0), periodic box L=32,
receiver (0,0,0) has source-free past through s<3.5/sqrt3.
Check complete inverse FFT of chi, spatial derivatives, chi_dot and
positive canonical local energy density at two spatial resolutions.
No sourced K4 Einstein/solid metric, no optical remote receiver yet.
"""
import numpy as np
from numpy.fft import fftn,ifftn,fftfreq

def evaluate(N, s_values=(0.5,1.0,1.5,1.9,2.5,3.0)):
    length=32.0;dx=length/N
    c=(np.arange(N)-N//2)*dx
    X=c[:,None,None]-6.;Y=c[None,:,None];Z=c[None,None,:]
    radius=2.5
    r2=(X*X+Y*Y+Z*Z)/radius**2
    bump=np.where(r2<1,(1-r2)**8,0.)
    chi0=bump*np.cos(2*(X+6.)+Y+1.4*Z)
    chihat=fftn(chi0)
    kk=2*np.pi*fftfreq(N,d=dx)
    kx=kk[:,None,None];ky=kk[None,:,None];kz=kk[None,None,:]
    omega=np.sqrt((3*(kx*kx+ky*ky+kz*kz)-1).astype(complex))
    i=N//2
    assert chi0[i,i,i]==0.
    result={}
    for s in s_values:
        tau=np.exp(s)
        cosine=np.cos(omega*s);sine=np.sin(omega*s)
        fieldhat=chihat*cosine/tau
        veloc_hat=chihat*(-cosine-omega*sine)/tau**2
        field=ifftn(fieldhat)[i,i,i]
        velocity=ifftn(veloc_hat)[i,i,i]
        gradient=np.array([ifftn(1j*k*fieldhat)[i,i,i]
                           for k in (kx,ky,kz)])
        rho=(abs(velocity)**2+3*np.sum(abs(gradient)**2)/tau**2)/2
        result[s]=(abs(field),float(rho))
        print(f'N={N} log_tau={s}: |chi|={abs(field):.11g}, rho={rho:.11g}')
    return result

if __name__=='__main__':
    front=3.5/np.sqrt(3.)
    assert 2.<front<2.1
    r128=evaluate(128)
    r160=evaluate(160)
    for s in (0.5,1.,1.5,1.9):
        assert r128[s][0]<1e-7
        assert r160[s][0]<1e-8
        assert r160[s][1]<2e-13
    for s in (2.5,3.0):
        assert r160[s][0]>1e-5
        assert r160[s][1]>1e-10
        assert abs(r160[s][0]-r128[s][0])<2e-8
        assert abs(r160[s][1]-r128[s][1])<5e-11
    print('PASS 3D compact positive-energy KG matter prefront quiet and postfront nonzero')
    print('PASS exact Fourier evolution and 128^3/160^3 receiver convergence')
    print('FRONT s=',front,'tau=',np.exp(front))
    print('SCOPE: physical local scalar stress ONLY; gravitational receiver open')
