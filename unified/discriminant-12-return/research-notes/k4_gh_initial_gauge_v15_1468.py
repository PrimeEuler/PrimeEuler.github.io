#!/usr/bin/env python3
"""v15.1468: harmonic gauge initial-data closure on a nontrivial
3+1 conformal metric and extrinsic-curvature slice.
Checks complete contracted 4D Christoffel. No Einstein time evolution.
"""
import numpy as np
def check(N=24):
 x=np.arange(N)*2*np.pi/N
 X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
 psi=3e-6*(np.cos(X)+.7*np.sin(2*Y)+.3*np.sin(X+Y))
 k=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=1/N)]*3),indexing='ij'))
 grad=lambda f:np.array([np.fft.ifftn(1j*k[i]*np.fft.fftn(f)).real for i in range(3)])
 g=np.exp(2*psi); gp=grad(psi);H=.005259956
 K=-H*np.eye(3)[:,:,None,None,None]*g
 K[0,1]+=(1e-5*np.sin(Z))*g
 K[1,0]+=(1e-5*np.sin(Z))*g
 trK=sum(K[i,i]/g for i in range(3))
 adot=-trK;bdot=-gp/g
 spacetime=np.zeros((4,4,N,N,N));inverse=np.zeros_like(spacetime)
 spacetime[0,0]=-1;inverse[0,0]=-1
 for i in range(3):
  spacetime[i+1,i+1]=g;inverse[i+1,i+1]=1/g
 dg=np.zeros((4,4,4,N,N,N))
 dg[0,0,0]=-2*adot
 for i in range(3):
  dg[0,0,i+1]=g*bdot[i];dg[0,i+1,0]=g*bdot[i]
  for j in range(3):
   dg[0,i+1,j+1]=-2*K[i,j]
   dg[i+1,j+1,j+1]=2*g*gp[i]
 Gamma=np.zeros((4,4,4,N,N,N))
 for a in range(4):
  for m in range(4):
   for n in range(4):
    for ell in range(4):
     Gamma[a,m,n]+=.5*inverse[a,ell]*(dg[m,ell,n]+dg[n,ell,m]-dg[ell,m,n])
 contracted=np.zeros((4,N,N,N))
 for a in range(4):
  for m in range(4):
   for n in range(4):contracted[a]+=inverse[m,n]*Gamma[a,m,n]
 maximum=float(np.max(abs(contracted)))
 assert maximum<3e-15
 print(dict(N=N,K_trace=float(trK.mean()),max_harmonic_gauge_violation=maximum,
    max_spatial_gauge_velocity=float(np.max(abs(bdot)))),flush=True)
 return maximum
if __name__=='__main__':
 for n in (12,16,24):check(n)
 print('PASS full contracted spacetime Christoffel harmonic initial constraints')
 print('OPEN nonlinear generalized-harmonic time evolution and ADM constraint propagation')
