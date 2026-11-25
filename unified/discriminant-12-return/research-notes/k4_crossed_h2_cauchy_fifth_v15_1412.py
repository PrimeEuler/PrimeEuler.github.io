#!/usr/bin/env python3
"""v15.1412: exact fifth-order inhomogeneous sigma wave solution with
ZERO Cauchy correction at t=0. Subtract homogeneous evolution of the
previous particular solution's initial values and time derivative.
Tests 16/24/32 spatial Fourier grids; full interacting EFT not solved.
"""
import sympy as s
import numpy as np
A,B,a,b=s.symbols('A B a b',real=True)
u5=-a**3*b**2*s.sin(A)**3*s.sin(B)**2/6
v5=-a**2*b**3*s.sin(A)**2*s.sin(B)**3/6
f=[s.lambdify((A,B,a,b),z,'numpy') for z in (u5,v5)]
ft=[s.lambdify((A,B,a,b),s.diff(z,A)+s.diff(z,B),'numpy') for z in (u5,v5)]
forces=[s.lambdify((A,B,a,b),2*a**3*b**2*s.sin(A)**2*s.sin(B)*s.cos(A)*s.cos(B),'numpy'),
s.lambdify((A,B,a,b),2*a**2*b**3*s.sin(A)*s.sin(B)**2*s.cos(A)*s.cos(B),'numpy')]
def trial(N=32,amp=.3,t=.7,h=.001):
    axis=np.arange(N)*2*np.pi/N
    X,Y=np.meshgrid(axis,axis,indexing='ij')
    kx,ky=np.meshgrid(np.fft.fftfreq(N,d=1/N),np.fft.fftfreq(N,d=1/N),indexing='ij')
    k=np.sqrt(kx*kx+ky*ky)
    def corrected(time,velocity=False):
        aa=time-X;bb=time-Y
        trig=np.cos(k*time)
        sinus=np.where(k>0,np.sin(k*time)/np.where(k>0,k,1),time)
        out=[]
        for j in range(2):
            f0=np.fft.fft2(f[j](-X,-Y,amp,amp))
            d0=np.fft.fft2(ft[j](-X,-Y,amp,amp))
            H=(-k*np.sin(k*time)*f0+trig*d0) if velocity else (trig*f0+sinus*d0)
            particular=(ft[j] if velocity else f[j])(aa,bb,amp,amp)
            out.append(particular-np.fft.ifft2(H).real)
        return out
    zero=corrected(0)+corrected(0,True)
    assert max(np.max(abs(z)) for z in zero)<1e-14
    fields=corrected(t)
    errors=[]
    for j in range(2):
        lap=np.fft.ifft2(-k*k*np.fft.fft2(fields[j])).real
        d2=(corrected(t+h)[j]-2*fields[j]+corrected(t-h)[j])/h**2
        expected=forces[j](t-X,t-Y,amp,amp)
        err=np.max(abs(-d2+lap-expected))/np.max(abs(expected))
        errors.append(float(err))
        assert err<3e-5
    print(dict(N=N,amplitude=amp,time=t,peak_correction=float(max(np.max(abs(z)) for z in fields)),
               max_PDE_relative_residual=max(errors),initial_Cauchy_peak=float(max(np.max(abs(z)) for z in zero))),flush=True)
    return fields
if __name__=='__main__':
    for n in (16,24,32):trial(n)
    print('PASS zero-initial-data fifth-order correction and independently evaluated inhomogeneous wave PDE')
    print('OPEN complete nonlinear target sigma, Weyl+Maxwell+Einstein backreaction, quarter coupling')
