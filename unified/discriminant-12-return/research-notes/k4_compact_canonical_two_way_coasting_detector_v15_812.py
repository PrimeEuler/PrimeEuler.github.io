#!/usr/bin/env python3
"""v15.812: physical compact canonical source to FLRW two-way detector via
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
        results.append([t,ws,wv,wt,p,fv,gt,phi,psi,B,a*bdot])
    results=np.array(results)
    assert np.max(abs(results[:,1:4].imag))<1e-8
    assert min(abs(results[-1,1:4]))>1e-4
    print("N",N,"source samples",samples,"Ward max",np.max(np.abs(ward)))
    print("t=1 Weyl S/V/T",results[0,1:4])
    print("t=end Weyl S/V/T",results[-1,1:4])
    print("t=end displacement S/V/T",results[-1,4:])
    return results

if False and __name__=="__main__":
    r48=trial(48,21)
    r64=trial(64,31)
    assert np.max(abs(r48[-1,1:4]-r64[-1,1:4]))<5e-7
    assert np.max(abs(r48[0,1:4]-r64[0,1:4]))<5e-7
    print("PASS: same compact canonical source, 3 gauge-invariant K4 electric-Weyl channels")
    print("PASS: 48^3 vs 64^3 convergence; pressure Ward and mode-gap 3 controls")

# --- Additive v15.812 detector: all metric histories come from same
# physical, compact positive-energy canonical scalar and sourced K4 modes.
from scipy.integrate import quad

def detector(history,eta_e=.08,d=.075):
    eta=np.sqrt(3)*np.log(history[:,0].real)
    assert eta_e+2*d < eta[-1]
    ph=CubicSpline(eta,history[:,7])
    ps=CubicSpline(eta,history[:,8])
    bv=CubicSpline(eta,history[:,9])
    bv_eta=CubicSpline(eta,history[:,10])
    tt=CubicSpline(eta,history[:,6])
    a0=1/np.sqrt(3);hc=1/np.sqrt(3)
    n=np.array([2.,0.,1.])/np.sqrt(5)
    e=np.array([1.,0.,-2.])/np.sqrt(5)
    b=np.array([0.,1.,0.])
    arms=[n,e,b,(n+e)/np.sqrt(2),(n-e)/np.sqrt(2)]
    K=np.array([2.,0.,1.])
    def complex_quad(fn,a,b):
        return quad(lambda z:np.real(fn(z)),a,b,epsabs=2e-10)[0]+1j*quad(
            lambda z:np.imag(fn(z)),a,b,epsabs=2e-10)[0]
    def arm(u,sector):
        lam=np.dot(K,u);eu=np.dot(e,u);bu=np.dot(b,u)
        def modes(s):
            if sector=="S":return ph(s),ps(s),0,0,0
            if sector=="V":return 0,0,eu*bv(s),eu*bv_eta(s),0
            if sector=="T":return 0,0,0,0,(eu**2-bu**2)*tt(s)
            return ph(s),ps(s),eu*bv(s),eu*bv_eta(s),(eu**2-bu**2)*tt(s)
        def photon(s,back=False):
            p,pss,v,vd,H=modes(s)
            return -p-pss+(v if back else -v)+H/2
        O=complex_quad(lambda x:photon(eta_e+x)*np.exp(1j*lam*x),0,d)
        I=complex_quad(lambda x:photon(eta_e+d+x,True)*
            np.exp(1j*lam*(d-x)),0,d)
        def force(s):
            p,pss,v,vd,H=modes(s)
            return -1j*lam*p+vd+hc*v
        def shift(t):
            return complex_quad(lambda s:(1-np.exp(-hc*(t-s)))/hc*
                                force(s),0,t)
        M=2*np.exp(1j*lam*d)*shift(eta_e+d) -shift(eta_e)-shift(eta_e+2*d)
        clock=complex_quad(lambda s:a0*np.exp(hc*s)*modes(s)[0],
                           eta_e,eta_e+2*d)
        return a0*np.exp(hc*(eta_e+2*d))*(O+I+M)+clock
    arm_results=np.array([[arm(u,sector)
        for sector in ("S","V","T","All")] for u in arms])
    # Linear-response additivity of all three physically sourced sectors.
    assert np.max(abs(arm_results[:,:3].sum(axis=1)-arm_results[:,3]))<1e-9
    diff=np.array([arm_results[0]-arm_results[1],
                   arm_results[1]-arm_results[2],
                   arm_results[3]-arm_results[4]])
    assert abs(diff[1,0])<1e-9
    assert abs(diff[2,0])<1e-9 and abs(diff[2,2])<1e-9
    return diff

if __name__=="__main__":
    d48=detector(trial(48,21))
    d64=detector(trial(64,31))
    delta=np.max(abs(d48-d64))
    print("48^3 differential [n-e,e-b,rot+-rot-] / [S,V,T,All]",d48)
    print("64^3 differential [n-e,e-b,rot+-rot-] / [S,V,T,All]",d64)
    print("max refinement discrepancy",delta)
    assert delta<2e-5
    assert min(abs(d64[:,3]))>1e-5
    print("PASS source-consistent compact canonical matter -> FLRW two-way photon/mirror/clock differential detector")
    print("SCOPE: constrained initial-value source and comoving Fourier component, NOT calibrated astrophysical measurement")
