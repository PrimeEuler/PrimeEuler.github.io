#!/usr/bin/env python3
"""v15.1455 standard vacuum linear ADM constraint propagation on flat T3:
Hdot=-2 div M, Mdot=-grad H/2, hence Hddot=Delta H.
Necessary benchmark only; no nonlinear Einstein-sigma evolution.
"""
import numpy as np
def trial(N=24,T=4):
 x=np.arange(N)*2*np.pi/N
 X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 H0=.01*(np.sin(X+2*Y)+.3*np.cos(2*X-Z))
 k=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=1/N)]*3),indexing="ij"))
 mag=np.sqrt(np.sum(k*k,axis=0));h0=np.fft.fftn(H0)
 ht=h0*np.cos(mag*T)
 H=np.fft.ifftn(ht).real
 Mhat=-.5j*k*h0*np.where(mag>0,np.sin(mag*T)/np.where(mag>0,mag,1),T)
 M=np.fft.ifftn(Mhat,axes=(-3,-2,-1)).real
 hd=np.fft.ifftn(-mag*np.sin(mag*T)*h0).real
 md=np.fft.ifftn(-.5j*k*ht,axes=(-3,-2,-1)).real
 div=np.fft.ifftn(np.sum(1j*k*np.fft.fftn(M,axes=(-3,-2,-1)),axis=0)).real
 grad=np.fft.ifftn(1j*k*np.fft.fftn(H),axes=(-3,-2,-1)).real
 e1=float(np.max(abs(hd+2*div)));e2=float(np.max(abs(md+.5*grad)))
 norm0=np.mean(H0*H0);norm=np.mean(H*H+4*np.sum(M*M,axis=0))
 err=float(abs(norm/norm0-1))
 assert e1<1e-12 and e2<1e-12 and err<1e-12
 print(dict(N=N,max_propagation_residual=max(e1,e2),norm_relative_drift=err))
if __name__=="__main__":
 for n in (16,24,32):trial(n)
 print("PASS vacuum linear ADM constraint-propagation waves; nonlinear equations open")
