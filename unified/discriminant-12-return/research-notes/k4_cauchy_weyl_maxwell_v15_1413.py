#!/usr/bin/env python3
"""Gravity v15.1413: Cauchy-initialized fifth-order H2 crossed waves
drive TT Weyl-Maxwell source. Fourier grid, time finite differences,
transverse mode and Maxwell energy-work test. Requires numpy/scipy/sympy
and previous committed v15.1412 and v15.1411 reproducers.
No Einstein/sigma backreaction or physical quarter-grid selector.
"""
import numpy as np
from functools import lru_cache
from scipy.integrate import solve_ivp,simpson
from scipy.interpolate import CubicSpline
from k4_crossed_h2_cauchy_fifth_v15_1412 import f,ft
from k4_crossed_h2_corrected_weyl_current_v15_1411 import riemann,eta
@lru_cache(None)
def setup(N,a):
    axis=np.arange(N)*2*np.pi/N
    X,Y=np.meshgrid(axis,axis,indexing="ij")
    k=np.fft.fftfreq(N,d=1/N)
    kx,ky=np.meshgrid(k,k,indexing="ij")
    w=np.hypot(kx,ky)
    p=[np.fft.fft2(z(-X,-Y,a,a)) for z in f]
    vel=[np.fft.fft2(z(-X,-Y,a,a)) for z in ft]
    return X,Y,kx,ky,w,p,vel
def phi(t,N,a,kind):
    X,Y,kx,ky,w,p,vel=setup(N,a)
    base=np.array([a*np.sin(t-X),a*np.sin(t-Y)])
    if kind in ("leading","metric"):return base
    ans=[]
    for j in range(2):
        special=f[j](t-X,t-Y,a,a)
        if kind=="particular":ans.append(special);continue
        ffree=np.cos(w*t)*p[j]+np.where(w>0,np.sin(w*t)/np.where(w>0,w,1),t)*vel[j]
        ans.append(special-np.fft.ifft2(ffree).real)
    return base+np.array(ans)
def derivatives(z,N,a):
    _,_,kx,ky,*_=setup(N,a)
    zz=np.fft.fft2(z)
    return np.fft.ifft2(1j*kx*zz).real,np.fft.ifft2(1j*ky*zz).real
def area(t,N,a,kind,h=2e-4):
    p=phi(t,N,a,kind)
    g=np.zeros((2,4,N,N))
    dp=(phi(t+h,N,a,kind)-phi(t-h,N,a,kind))/(2*h)
    for j in range(2):
        g[j,0]=dp[j]
        g[j,1],g[j,2]=derivatives(p[j],N,a)
    B=np.einsum("i...,j...->ij...",g[0],g[1])-np.einsum("i...,j...->ij...",g[1],g[0])
    return B if kind=="leading" else B/np.sqrt(1+p[0]**2+p[1]**2)
def K(t,z,N,a,kind):
    B=area(t,N,a,kind)
    return np.einsum("ijrs,rs...->ij...",riemann(t,z),np.einsum("ir,js,rs...->ij...",eta,eta,B))
def current(t,N,a,kind,z=.26,h=4e-4):
    def raised(tt,zz):
        H=K(tt,zz,N,a,kind)
        return np.einsum("ir,js,rs...->ij...",eta,eta,H)
    now=raised(t,z)
    J=-(raised(t+h,z)[0]-raised(t-h,z)[0]+raised(t,z+h)[3]-raised(t,z-h)[3])/(2*h)
    for nu in range(4):
        dx=derivatives(now[1,nu],N,a)[0]
        dy=derivatives(now[2,nu],N,a)[1]
        J[nu]-=dx+dy
    return J
def transverse(t,N,a,kind,h=4e-4):
    J=current(t,N,a,kind,h=h)
    j=np.fft.fft2(J[1:],axes=(-2,-1))[:,1,1]/N**2
    q=np.array([1.,1.,-1.])
    return j-q*(q@j)/(q@q)
def response(N=16,a=.3,g=.05):
    ts=np.linspace(0,1.2,25)
    vals=np.array([transverse(float(t),N,a,"cauchy") for t in ts])
    drive=CubicSpline(ts,vals,axis=0)
    def ode(t,y):return np.r_[y[3:],-3*y[:3]-g*drive(t)]
    sol=solve_ivp(ode,(0,1.2),np.zeros(6,complex),method="DOP853",rtol=1e-11,atol=1e-17,dense_output=True)
    assert sol.success
    E=(np.sum(abs(sol.y[3:,-1])**2)+3*np.sum(abs(sol.y[:3,-1])**2))/2
    sample=np.linspace(0,1.2,1201);Y=sol.sol(sample)
    work=-simpson(np.real(np.sum(np.conj(Y[3:])*g*drive(sample).T,axis=0)),x=sample)
    if g:assert abs(E-work)/E<2e-6
    return float(E),float(work)
if __name__=="__main__":
    for N in (16,24,32):
        out={q:float(np.linalg.norm(transverse(.7,N,.3,q))) for q in ("leading","metric","particular","cauchy")}
        print("CURRENT",N,out,flush=True)
        assert out["cauchy"]>0 and abs(out["cauchy"]-.065074595)<1e-6
    for h in (.0016,.0008,.0004,.0002):
        print("DERIVATIVE",h,float(np.linalg.norm(transverse(.7,24,.3,"cauchy",h))),flush=True)
    for g in (.05,.025,0.):
        E,W=response(g=g);print("MAXWELL",g,E,W,flush=True)
    print("PASS Cauchy-derived nonzero transverse Weyl current and sourced EM work identity")
    print("OPEN full Einstein+Maxwell+sigma backreaction and physical quarter selector")
