#!/usr/bin/env python3
"""v15.1314: evolved k>0 Maxwell-K4 scalar Hamiltonian and momentum constraints.
Original compact source; Nyquist-clean transverse Maxwell; 2N dealiased
quadratic stress; first-order K4 displacement, Bardeen metric, FLRW Einstein
operators. These two constraints do NOT certify spatial/vector/tensor closure.
"""
import numpy as np
from scipy.interpolate import CubicSpline
from math import pi, sqrt

def run(N=16, nt=17, tf=1.08):
    L=4*pi
    x=(np.arange(N)-N//2)*L/N
    X=x[:,None,None]; Y=x[None,:,None]; Z=x[None,None,:]
    f=lambda u:np.where(abs(u)<1,(1-u*u)**3,0.)
    fp=lambda u:np.where(abs(u)<1,-6*u*(1-u*u)**2,0.)
    E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),
         -fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing="ij"))
    k2=np.sum(q*q,axis=0); k=np.sqrt(k2)
    n=np.zeros_like(q);np.divide(q,k,out=n,where=k>0)
    h=np.fft.fftn(E0,axes=(1,2,3))
    h-=n*np.einsum("i...,i...->...",n,h)
    h[:,np.any(abs(q)==N/2*2*pi/L,axis=0)]=0
    curl=1j*np.cross(q,h,axis=0)
    M=2*N
    ids=np.mod(np.rint(np.fft.fftfreq(N)*N).astype(int),M)
    inside=(k2>0)&np.all(abs(q)<N/2*2*pi/L,axis=0)
    def padded(v):
        pad=[(0,0)]*(v.ndim-3)+[(N//2,N//2)]*3
        w=np.fft.ifftshift(np.pad(np.fft.fftshift(v,axes=(-3,-2,-1)),pad),axes=(-3,-2,-1))
        return np.fft.ifftn(8*w,axes=(-3,-2,-1)).real
    def fft(v):
        w=np.fft.fftn(v,axes=(-3,-2,-1))/M**3
        return w[...,ids[:,None,None],ids[None,:,None],ids[None,None,:]]
    def source(t):
        xi=sqrt(3)*np.log(t)
        sinc=np.zeros_like(k);np.divide(np.sin(k*xi),k,out=sinc,where=k>0)
        E,B,Ed,Bd=map(padded,(h*np.cos(k*xi),-curl*sinc,
                    -h*k*np.sin(k*xi)*sqrt(3)/t,
                    -curl*np.cos(k*xi)*sqrt(3)/t))
        rho=np.sum(E*E+B*B,axis=0)/2
        rhod=np.sum(E*Ed+B*Bd,axis=0)
        F=np.cross(E,B,axis=0)
        Fd=np.cross(Ed,B,axis=0)+np.cross(E,Bd,axis=0)
        T=np.eye(3)[:,:,None,None,None]*rho-np.einsum("i...,j...->ij...",E,E)-np.einsum("i...,j...->ij...",B,B)
        r,rd,Fh,Fdh,Th=map(fft,(rho,rhod,F,Fd,T))
        Fn=np.einsum("i...,i...->...",n,Fh)
        Fnd=np.einsum("i...,i...->...",n,Fdh)
        Tnn=np.einsum("i...,ij...,j...->...",n,Th,n)
        return r,rd,Fn,Fnd,Tnn
    times=np.linspace(1,tf,nt)
    history=[source(t) for t in times]
    spl=[CubicSpline(times,np.stack([v[i] for v in history]),axis=0) for i in range(5)]
    mass=2+k2
    P=np.zeros((2,N,N,N),complex)
    def pdd(t,p,pd):
        r,_,_,_,Tnn=(s(t) for s in spl)
        force=np.zeros_like(r)
        np.divide(9*(3*Tnn-r),2*k2*t**4,out=force,where=inside)
        return -3*pd/t-mass*p/t**2+force
    def rhs(t,v):return np.stack([v[1],pdd(t,v[0],v[1])])
    def test(t,v):
        p,pd=v
        r,rd,Fn,Fnd,Tnn=source(t)
        accel=pdd(t,p,pd)
        jb=-1j*sqrt(3)*k*Fn/t
        jbd=(-3*k2*Tnn+1j*sqrt(3)*k*Fn)/t**2
        den=1+k2;safe=np.where(inside,k2,1)
        phi=((t*t*accel+2*t*pd)/3-3*r/t**2-3*jbd/(2*safe))/den
        psi=((k2*p-t*pd)/3-3*r/(2*t**2)+3*jb/(2*safe*t))/den
        jbp=-1j*sqrt(3)*k*(Fnd/t-Fn/t**2)
        psid=((k2*pd-pd-t*accel)/3-3*rd/(2*t**2)+3*r/t**3+
              3*(jbp/t-jb/t**2)/(2*safe))/den
        Q=t*psid+phi
        G00=6*(k2*psi+Q)/t**2
        G0long=-2j*k*Q/t
        # K4 solid from F=C(det B)^(1/3) and phi^I=x^I+partial^I P
        T00=-9*r/t**4-6*psi/t**2+2*k2*p/t**2
        T0long=3*sqrt(3)*Fn/t**3-2j*k*pd/3
        return [float(np.max(abs(v[inside]))) for v in (
          G00-T00,G0long-T0long,rd+1j*sqrt(3)*k*Fn/t,
          G00+9*r/t**4,G0long-3*sqrt(3)*Fn/t**3)]
    values=[test(times[0],P)]
    for j in range(nt-1):
        t=times[j];dt=times[j+1]-t
        a=rhs(t,P);b=rhs(t+dt/2,P+dt*a/2)
        c=rhs(t+dt/2,P+dt*b/2);d=rhs(t+dt,P+dt*c)
        P=P+dt*(a+2*b+2*c+d)/6
        values.append(test(times[j+1],P))
    z=np.asarray(values)
    row=dict(N=N,nt=nt,max_H00=float(z[:,0].max()),
             max_M0=float(z[:,1].max()),max_Ward=float(z[:,2].max()),
             negative_without_solid_H00=float(z[:,3].max()),
             negative_without_solid_M0=float(z[:,4].max()),
             final_max_P=float(abs(P[0][inside]).max()))
    assert max(row["max_H00"],row["max_M0"],row["max_Ward"])<3e-11
    assert row["negative_without_solid_H00"]>1e-6
    assert row["negative_without_solid_M0"]>1e-7
    print(row,flush=True)
    return row

if __name__=="__main__":
    for N in (12,16,24,32):run(N)
    for nt in (9,33):run(24,nt=nt)
    print("PASS evolved scalar Einstein 00 and longitudinal 0i constraints")
    print("OPEN spatial trace/shear, transverse-vector, TT, full metric/optics")
