#!/usr/bin/env python3
"""v15.1353: independent all-ten 4D Einstein residual from a shared
Maxwell+K4 four-metric. Requires the additive v15.1351 metric reproducer
in this same research-notes directory; no historical source modified."""
import numpy as np
from math import pi,sqrt
from pathlib import Path
import importlib.util
root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("metric_core",root/"k4_independent_adm_momentum_v15_1351.py")
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
assemble=core.assemble

def maxwell_tensor(N,t,amplitude):
    L=4*pi;x=(np.arange(N)-N//2)*L/N
    X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
    f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
    fp=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
    E0=amplitude*np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),-fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing='ij'))
    k=np.sqrt(np.sum(q*q,axis=0));n=np.zeros_like(q)
    np.divide(q,k,out=n,where=k>0)
    H=np.fft.fftn(E0,axes=(1,2,3))
    H-=n*np.einsum('i...,i...->...',n,H)
    H[:,np.any(abs(q)==N/2*2*pi/L,axis=0)]=0
    curl=1j*np.cross(q,H,axis=0);M=2*N
    def padded(z):
        pad=[(0,0)]*(z.ndim-3)+[(N//2,N//2)]*3
        w=np.fft.ifftshift(np.pad(np.fft.fftshift(z,axes=(-3,-2,-1)),pad),axes=(-3,-2,-1))*8
        return np.fft.ifftn(w,axes=(-3,-2,-1)).real
    xi=sqrt(3)*np.log(t);sn=np.zeros_like(k)
    np.divide(np.sin(k*xi),k,out=sn,where=k>0)
    E=padded(H*np.cos(k*xi));B=padded(-curl*sn)
    rho=np.sum(E*E+B*B,axis=0)/2
    I=np.eye(3)[:,:,None,None,None]
    Tij=I*rho-np.einsum('i...,j...->ij...',E,E)-np.einsum('i...,j...->ij...',B,B)
    th=np.fft.fftn(Tij,axes=(-3,-2,-1))/M**3
    ids=np.mod(np.rint(np.fft.fftfreq(N)*N).astype(int),M)
    th=th[...,ids[:,None,None],ids[None,:,None],ids[None,None,:]]
    mask=np.any(abs(q)==N/2*2*pi/L,axis=0)
    th[:,:,mask]=0
    return np.fft.ifftn(N**3*th,axes=(-3,-2,-1)).real

def probe_spatial(N=12,t=1.08,dt=.004,nt=13,amplitude=.1):
    hist=[assemble(N,nt=nt,tf=t+j*dt,amplitude=amplitude) for j in (-2,-1,0,1,2)]
    a=t/sqrt(3);adot=1/sqrt(3);H=1/t
    q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=4*pi/N)*2*pi]*3),indexing='ij'))
    I=np.eye(3)
    fft=lambda z:np.fft.fftn(z,axes=(-3,-2,-1))/N**3
    ift=lambda z:np.fft.ifftn(z*N**3,axes=(-3,-2,-1)).real
    def spatial(z,i):return ift(1j*q[i]*fft(z))
    def perturb(h,tt):
        aa=tt/sqrt(3)
        out=np.zeros((4,4,N,N,N))
        out[0,0]=h["g00"]+1
        out[0,1:]=h["g0i"];out[1:,0]=h["g0i"]
        out[1:,1:]=h["gij"]-aa**2*I[:,:,None,None,None]
        return out
    ph=[perturb(h,t+j*dt) for j,h in zip((-2,-1,0,1,2),hist)]
    def gamma(p,dp,tt):
        aa=tt/sqrt(3);ap=1/sqrt(3);hh=1/tt
        out=np.zeros((4,4,4,N,N,N))
        out[0,0,0]=-.5*dp[0,0]
        for i in range(3):
            ii=i+1
            out[0,0,ii]=out[0,ii,0]=-.5*spatial(p[0,0],i)+hh*p[0,ii]
            out[ii,0,0]=(2*dp[0,ii]-spatial(p[0,0],i))/(2*aa**2)
            for j in range(3):
                jj=j+1
                out[0,ii,jj]=-.5*(spatial(p[0,jj],i)+spatial(p[0,ii],j)-dp[ii,jj])+aa*ap*p[0,0]*I[i,j]
                out[ii,0,jj]=out[ii,jj,0]=(dp[ii,jj]+spatial(p[0,ii],j)-spatial(p[0,jj],i))/(2*aa**2)-ap*p[ii,jj]/aa**3
                for ell in range(3):
                    ll=ell+1
                    out[ii,jj,ll]=(spatial(p[ii,ll],j)+spatial(p[ii,jj],ell)-spatial(p[jj,ll],i))/(2*aa**2)-hh*p[0,ii]*I[j,ell]
        return out
    td=[None,(ph[2]-ph[0])/(2*dt),(ph[3]-ph[1])/(2*dt),(ph[4]-ph[2])/(2*dt),None]
    dm=gamma(ph[1],td[1],t-dt);dc=gamma(ph[2],td[2],t);dp=gamma(ph[3],td[3],t+dt)
    dgd=(dp-dm)/(2*dt)
    assert abs(dc-dc.swapaxes(1,2)).max()<1e-12
    C=np.zeros((4,4,4))
    for i in range(3):
        C[0,i+1,i+1]=a*adot
        C[i+1,0,i+1]=C[i+1,i+1,0]=H
    dr=np.zeros((4,4,N,N,N))
    for mu in range(4):
      for nu in range(4):
        z=np.zeros((N,N,N))
        for alpha in range(4):
          z+=(dgd[alpha,mu,nu] if alpha==0 else spatial(dc[alpha,mu,nu],alpha-1))
          z-=(dgd[alpha,mu,alpha] if nu==0 else spatial(dc[alpha,mu,alpha],nu-1))
          for lam in range(4):
            z+=dc[alpha,alpha,lam]*C[lam,mu,nu]+C[alpha,alpha,lam]*dc[lam,mu,nu]
            z-=dc[alpha,nu,lam]*C[lam,mu,alpha]+C[alpha,nu,lam]*dc[lam,mu,alpha]
        dr[mu,nu]=z
    s=ph[2][1:,1:]/a**2
    dscalar=-dr[0,0]+np.einsum('ii...->...',dr[1:,1:])/a**2-2*np.einsum('ii...->...',s)/t**2
    geom=dr[1:,1:]/a**2-2*s/t**2-I[:,:,None,None,None]*dscalar/2
    # Compute 00 and 0i from the *same* independently constructed
    # 4D linearized Christoffel/Ricci tensor; not the ADM or mode equations.
    # Background R00=0, Rij=2/3 deltaij for a=t/sqrt3.
    geom00=-dr[0,0]-dscalar/2
    geom0i=-dr[0,1:]+2*ph[2][0,1:]/t**2
    mid=hist[2]
    k2=np.sum(q*q,axis=0);k=np.sqrt(k2)
    n=np.zeros_like(q);np.divide(q,k,out=n,where=k>0)
    Fhat=n*mid["Fn"]+mid["Fperp"]
    MaxwellMom=ift(3*sqrt(3)*Fhat/t**3)
    SolidMom=ift(-2j*q*mid["p"][1]/3+2*(mid["v"][1]-sqrt(3)*mid["Bv"]/t)/3)
    Psi=ift(mid["psi"])
    Pgrad=ift(k2*mid["p"][0])
    SolidEnergy=(-6*mid["u"]+6*Psi-2*Pgrad)/t**2
    MaxwellEnergy=9*(ift(mid["r"])+mid["mean"])/t**4
    resid00=geom00+MaxwellEnergy+SolidEnergy
    resid0i=geom0i-MaxwellMom-SolidMom
    em=9*maxwell_tensor(N,t,amplitude)/t**4
    P=mid["p"][0];v=mid["v"][0]
    Dhat=(-fft(s)-2*np.einsum('i...,j...->ij...',q,q)*P
      -1j*(np.einsum('i...,j...->ij...',q,v)+np.einsum('i...,j...->ij...',v,q)))
    trD=np.einsum('ii...->...',Dhat)
    solid=ift((Dhat-2*I[:,:,None,None,None]*trD/3)/t**2)
    stress=em+solid
    res=geom-stress
    row=dict(N=N,dt=dt,t=t,nt=nt,max_geom=float(abs(geom).max()),
        max_matter=float(abs(stress).max()),max_residual=float(abs(res).max()),
        relative=float(abs(res).max()/max(abs(stress).max(),1e-30)),
        no_solid=float(abs(geom-em).max()),no_maxwell=float(abs(geom-solid).max()),
        residual_sym=float(abs(res-res.swapaxes(0,1)).max()),
        max_scalar_trace_residual=float(abs(np.einsum('ii...->...',res)).max()))
    row.update(max_00=float(abs(resid00).max()),max_0i=float(abs(resid0i).max()),
       relative_00=float(abs(resid00).max()/max(abs(MaxwellEnergy+SolidEnergy).max(),1e-30)),
       relative_0i=float(abs(resid0i).max()/max(abs(MaxwellMom+SolidMom).max(),1e-30)),
       no_Maxwell_00=float(abs(geom00+SolidEnergy).max()),
       no_solid_00=float(abs(geom00+MaxwellEnergy).max()),
       no_Maxwell_0i=float(abs(geom0i-SolidMom).max()),
       no_solid_0i=float(abs(geom0i-MaxwellMom).max()))
    assert max(row["relative_00"],row["relative_0i"],row["relative"])<.001,row
    for source in ("Maxwell","solid"):
        assert row["no_"+source+"_00"]>10*row["max_00"],row
        assert row["no_"+source+"_0i"]>10*row["max_0i"],row
    assert row["relative"]<.001,row
    assert row["no_solid"]>10*row["max_residual"],row
    assert row["no_maxwell"]>10*row["max_residual"],row
    print(row,flush=True)
    return row

if __name__=="__main__":
    a=probe_spatial(12,dt=.006)
    b=probe_spatial(12,dt=.003)
    probe_spatial(16,dt=.004)
    c=probe_spatial(24,dt=.003)
    d=probe_spatial(24,dt=.0015)
    for x,y in ((a,b),(c,d)):
        for key in ("max_00","max_0i","max_residual"):
            assert 3.8<x[key]/y[key]<4.2,(key,x[key]/y[key])
    print("PASS independent 4D Einstein 00, three 0i, six spatial equations")
    print("OPEN continuum, nonlinear gravity, causal optical experiment, quarter-grid selector")
