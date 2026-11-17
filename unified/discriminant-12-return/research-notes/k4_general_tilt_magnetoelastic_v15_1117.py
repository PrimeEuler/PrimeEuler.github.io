#!/usr/bin/env python3
"""Gravity v15.1117: fully tilted cone plane and linear elastic support
for a compact elliptic magnetic current in a 2D periodic material cell.
An explicit periodic elastic solution is not a finite isolated 3D device.
"""
import sympy as s
import numpy as np
X,Y,T,C,a,b=s.symbols("X Y T C a b",real=True)
v2=a*a+b*b
cx=-C*a/(1-v2);cy=-C*b/(1-v2)
implicit=s.expand((C-a*X-b*Y)**2-X**2-Y**2)
ell=s.expand((1-a*a)*(X-cx)**2-2*a*b*(X-cx)*(Y-cy)+(1-b*b)*(Y-cy)**2-C**2/(1-v2))
assert s.simplify(implicit+ell)==0
assert cx.subs(a,0)==0 and s.diff(C-b*Y,Y)==-b
angle,D=s.symbols("angle D",real=True)
R=s.Matrix([[s.cos(angle),-s.sin(angle)],[s.sin(angle),s.cos(angle)]])
stress=s.simplify(R*s.diag(D/2,-D/2)*R.T)
assert s.trigsimp(stress[0,0]-stress[1,1]-D*s.cos(2*angle))==0
assert s.trigsimp(2*stress[0,1]-D*s.sin(2*angle))==0
N=144;size=12.;mu=2.;lam=3.
grid=(np.arange(N)-N//2)*size/N
YY,ZZ=np.meshgrid(grid,grid,indexing="ij")
A=1.4;B=0.9;offset=.45
q=((YY-offset)/A)**2+(ZZ/B)**2
psi=np.maximum(1-q,0)**4
k=2*np.pi*np.fft.fftfreq(N,d=size/N)
ky,kz=np.meshgrid(k,k,indexing="ij");k2=ky**2+kz**2
ft=np.fft.fft2
ift=lambda z:np.fft.ifft2(z).real
ph=ft(psi)
py=ift(1j*ky*ph);pz=ift(1j*kz*ph);lap=ift(-k2*ph)
fy=-lap*py;fz=-lap*pz
fhy=ft(fy);fhz=ft(fz)
assert abs(fhy[0,0])<1e-7 and abs(fhz[0,0])<1e-7
safe=np.where(k2==0,1,k2);dot=ky*fhy+kz*fhz
uhy=(fhy-(lam+mu)/(lam+2*mu)*ky*dot/safe)/(mu*safe)
uhz=(fhz-(lam+mu)/(lam+2*mu)*kz*dot/safe)/(mu*safe)
uhy[0,0]=0;uhz[0,0]=0
uy=ift(uhy);uz=ift(uhz)
ry=mu*k2*uhy+(lam+mu)*ky*(ky*uhy+kz*uhz)-fhy
rz=mu*k2*uhz+(lam+mu)*kz*(ky*uhy+kz*uhz)-fhz
rel=np.sqrt(np.mean(ift(ry)**2+ift(rz)**2))/np.sqrt(np.mean(fy**2+fz**2))
assert rel<1e-10
eYY=ift(1j*ky*uhy);eZZ=ift(1j*kz*uhz)
eYZ=.5*(ift(1j*kz*uhy)+ift(1j*ky*uhz))
cell=(size/N)**2
Ue=np.sum(.5*lam*(eYY+eZZ)**2+mu*(eYY**2+eZZ**2+2*eYZ**2))*cell
W=.5*np.sum(uy*fy+uz*fz)*cell
assert Ue>0 and abs(Ue-W)<1e-9
Iplus=np.sum(py**2-pz**2)*cell
assert abs(Iplus)>1e-3
print("PASS general tilt plane center, spin2 orientation, elliptic magnetic pinch/elastic stress")
print("relative equilibrium residual",rel)
print("elastic strain energy",Ue,"half Lorentz force displacement work",W)
print("EM TT plus integrated",Iplus)
print("LIMIT periodic 2D cell with imposed magnetic current; not isolated 3D conductor")
