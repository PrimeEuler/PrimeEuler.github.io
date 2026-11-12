#!/usr/bin/env python3
"""v15.788: reexecute frozen v15.750 compact canonical scalar K4 evolution via
exact Fourier-mode propagation; source scalar/vector/tensor constrained
K4 modes and evaluate all three electric Weyl components. Initial-value
model, not cosmological detector/observable calibration. All source
coefficients arise from the same positive-local-energy scalar field.
"""
import numpy as np
from numpy.fft import fftn,ifftn,fftfreq
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline

def trial(N=64,samples=31,R=7.,end=1.35):
    L=8*np.pi;dx=L/N
    x=(np.arange(N)-N//2)*dx
    xx=x[:,None,None];zz=x[None,None,:]
    h=np.where(abs(x)<R,(1-(x/R)**2)**8,0.)
    w=h[:,None,None]*h[None,:,None]*h[None,None,:]
    c=w*(np.cos(2*xx)+np.cos(zz));cf=fftn(c)
    q=2*np.pi*fftfreq(N,d=dx)
    qx=q[:,None,None];qy=q[None,:,None];qz=q[None,None,:]
    om2=3*(qx*qx+qy*qy+qz*qz)-1
    om=np.sqrt(om2.astype(complex))
    # L=8pi: actual K=(2,0,1) is FFT bin (8,0,4), NOT (2,0,1).
    binK=(int(round(2*L/(2*np.pi))),0,int(round(L/(2*np.pi))))
    scale=np.sum(w*w)
    coeff=lambda value:fftn(value)[binK]/scale
    times=np.linspace(1,end,samples)
    rows=[];vrows=[];trows=[];ward=[]
    for t in times:
        co=np.cos(om*np.log(t));sn=np.sin(om*np.log(t))
        c0=ifftn(cf*co).real/t
        ct=ifftn(cf*(-co-om*sn)).real/t**2
        ctt=ifftn(cf*((2-om2)*co+3*om*sn)).real/t**3
        gx=ifftn(cf*co*1j*qx).real/t
        gy=ifftn(cf*co*1j*qy).real/t
        gz=ifftn(cf*co*1j*qz).real/t
        gxt=ifftn(cf*(-co-om*sn)*1j*qx).real/t**2
        gyt=ifftn(cf*(-co-om*sn)*1j*qy).real/t**2
        gzt=ifftn(cf*(-co-om*sn)*1j*qz).real/t**2
        a=t/np.sqrt(3)
        grad2=gx*gx+gy*gy+gz*gz
        rho=(ct*ct+grad2/a**2)/2
        ptr=(3*ct*ct-grad2/a**2)/2
        jphi=a**3*coeff(rho);jpsi=a**3*coeff(ptr)
        rhodot=ct*ctt+(gx*gxt+gy*gyt+gz*gzt)/a**2-grad2/(a*a*t)
        jphidot=3*jphi/t+a**3*coeff(rhodot)
        kg=2*gx+gz;kgt=2*gxt+gzt
        mom=coeff(ct*kg);momdot=coeff(ctt*kg+ct*kgt)
        jb=-1j*a*a*mom
        jbd=-1j*a*a*(2*mom/t+momdot)
        ward.append(t*jphidot+np.sqrt(3)*jb+jpsi)
        ge=(gx-2*gz)/np.sqrt(5)
        get=(gxt-2*gzt)/np.sqrt(5)
        jv=a*a*coeff(ct*ge)
        jvd=a*a*coeff(2*ct*ge/t+ctt*ge+ct*get)
        pit=coeff((ge*ge-gy*gy)/(2*a*a))
        rows.append([jphi,jpsi,jb,jbd])
        vrows.append([jv,jvd]);trows.append(pit)
    rows=np.array(rows);vrows=np.array(vrows);trows=np.array(trows)
    assert np.max(abs(rows.imag))<1e-8
    assert np.max(np.abs(ward))<1e-6
    ss=[CubicSpline(times,rows[:,i].real) for i in range(4)]
    vs=[CubicSpline(times,vrows[:,i]) for i in range(2)]
    ts=CubicSpline(times,trows)
    k2=5.;eta=.75;k=np.sqrt(k2);dv=4+3*k2
    bs=(8*eta*(1+k2)-3*k2)/3
    bv=2*eta*dv/3;bt=3*k2+8*eta/3
    assert (bt-bv)/(bv-bs)==3
    def scalar(t,y):
        jp,js,jb,jbd=[f(t) for f in ss]
        force=3*np.sqrt(3)*js/(2*k2*t**3)-9*(t*jbd+jb)/(2*k2**2*t**3)
        return [y[1],-3*y[1]/t-bs*y[0]/t**2+force]
    def vector(t,y):
        j,jd=[f(t) for f in vs]
        b=4*t/(np.sqrt(3)*dv)
        mass=2*t**3*k2/(3*np.sqrt(3)*dv)
        return [y[1],-3*y[1]/t-bv*y[0]/t**2-b*(j/t+jd)/mass]
    def tensor(t,y):
        return [y[1],-3*y[1]/t-bt*y[0]/t**2-2*ts(t)]
    def solve(fn,complex_data=False):
        z=np.array([0j,0j]) if complex_data else [0.,0.]
        out=solve_ivp(fn,(1.,end),z,t_eval=times,rtol=1e-10,
                      atol=1e-11,method="DOP853")
        assert out.success
        return out.y
    sy=solve(scalar);vy=solve(vector,True);ty=solve(tensor,True)
    results=[]
    for i,t in enumerate(times):
        p,pd=sy[:,i];pdd=scalar(t,[p,pd])[1]
        jp,js,jb,jbd=rows[i];a=t/np.sqrt(3)
        phi=(t*t*pdd+2*t*pd)/(3*(1+k2))+(np.sqrt(3)*(jp+js)/(2*t*(1+k2)))-3*jbd/(2*k2*(1+k2))
        psi=(k2*p-t*pd)/(3*(1+k2))+np.sqrt(3)*jp/(2*t*(1+k2))+3*jb/(2*k2*t*(1+k2))
        ws=k2*(phi+psi)/(2*a*a)
        fv,fvd=vy[:,i];fdd=vector(t,[fv,fvd])[1]
        j,jd=vrows[i];av=t*dv/(6*np.sqrt(3));b=4*t/(np.sqrt(3)*dv)
        B=b*fvd-j/av
        bdot=b*fvd/t+b*fdd-jd/av+j/(av*t)
        wv=-1j*k*bdot/(4*a)
        gt,gtd=ty[:,i];gdd=tensor(t,[gt,gtd])[1]
        wt=(t*t*gdd+t*gtd-3*k2*gt)/(12*a*a)
        fullS=-k2*phi/(a*a)
        fullV=-1j*k*(bdot+B/t)/(2*a)
        fullT=-(gdd+2*gtd/t)/2
        results.append([t,ws,wv,wt,fullS,fullV,fullT,p,fv,gt])
    results=np.array(results)
    assert np.max(abs(results[:,1:7].imag))<1e-8
    assert min(abs(results[-1,4:7]))>1e-4
    print("N",N,"source samples",samples,"Ward max",np.max(np.abs(ward)))
    print("t=1 Weyl vs full Fermi S/V/T",results[0,1:7])
    print("t=end Weyl vs full Fermi S/V/T",results[-1,1:7])
    print("t=end displacement S/V/T",results[-1,7:])
    return results

if __name__=="__main__":
    r48=trial(48,21)
    r64=trial(64,31)
    assert np.max(abs(r48[-1,1:7]-r64[-1,1:7]))<2e-6
    assert np.max(abs(r48[0,1:7]-r64[0,1:7]))<2e-6
    print("PASS: same compact canonical source, 3 full Fermi electric-Riemann channels")
    print("PASS: 48^3 vs 64^3 convergence; Weyl/Ricci distinction and pressure Ward")
