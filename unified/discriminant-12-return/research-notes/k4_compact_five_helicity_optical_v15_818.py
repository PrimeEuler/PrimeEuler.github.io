#!/usr/bin/env python3
"""v15.818: same compact positive-energy canonical matter -> 5 K4 modes
-> 5 finite-arm coasting optical signals. Initial-value model, not a
calibrated or remote detector, and no novel Cone-only interaction.
"""
import numpy as np
from numpy.fft import fftn,ifftn,fftfreq
from scipy.integrate import solve_ivp,quad
from scipy.interpolate import CubicSpline
SQ=np.sqrt
K=np.array([2.,0.,1.]);k=SQ(5.);n=K/k
E=np.array([1.,0.,-2.])/k;B=np.array([0.,1.,0.]);hc=1/SQ(3.)
def source_and_modes(N=64,ns=31,R=10.,end=1.35):
    L=8*np.pi;dx=L/N;x=(np.arange(N)-N//2)*dx
    xx=x[:,None,None];yy=x[None,:,None];zz=x[None,None,:]
    h=np.where(abs(x)<R,(1-(x/R)**2)**8,0.)
    window=h[:,None,None]*h[None,:,None]*h[None,None,:]
    chi0=window*(np.cos(2*xx)+np.cos(zz)+SQ(2)*(np.cos(xx+yy)+np.cos(xx-yy+zz)))
    cf=fftn(chi0);q=2*np.pi*fftfreq(N,d=dx)
    qx=q[:,None,None];qy=q[None,:,None];qz=q[None,None,:]
    w2=3*(qx*qx+qy*qy+qz*qz)-1;w=SQ(w2.astype(complex))
    coef=lambda z:fftn(z)[8,0,4]/np.sum(window*window)
    ts=np.linspace(1,end,ns);values=[];wr=[]
    for t in ts:
        c=np.cos(w*np.log(t));si=np.sin(w*np.log(t))
        Z=cf*c/t;Zd=cf*(-c-w*si)/t**2
        Zdd=cf*((2-w2)*c+3*w*si)/t**3
        fd=ifftn(Zd).real;fdd=ifftn(Zdd).real
        gx=ifftn(1j*qx*Z).real;gy=ifftn(1j*qy*Z).real;gz=ifftn(1j*qz*Z).real
        gdx=ifftn(1j*qx*Zd).real;gdy=ifftn(1j*qy*Zd).real;gdz=ifftn(1j*qz*Zd).real
        ge=(gx-2*gz)/k;gb=gy
        gde=(gdx-2*gdz)/k;gdb=gdy
        a=t/SQ(3.);grad2=gx*gx+gy*gy+gz*gz
        rho=(fd*fd+grad2/a**2)/2
        ptr=(3*fd*fd-grad2/a**2)/2
        jphi=a**3*coef(rho);jpsi=a**3*coef(ptr)
        rdot=fd*fdd+(gx*gdx+gy*gdy+gz*gdz)/a**2-grad2/(a*a*t)
        jpdt=3*jphi/t+a**3*coef(rdot)
        m=coef(fd*(2*gx+gz));md=coef(fdd*(2*gx+gz)+fd*(2*gdx+gdz))
        jb=-1j*a*a*m;jbd=-1j*a*a*(2*m/t+md)
        wr.append(t*jpdt+SQ(3.)*jb+jpsi)
        js=[a*a*coef(fd*g) for g in (ge,gb)]
        jds=[a*a*coef(2*fd*g/t+fdd*g+fd*gd) for g,gd in ((ge,gde),(gb,gdb))]
        pit=[coef((ge*ge-gb*gb)/(2*a*a)),coef(ge*gb/(a*a))]
        values.append([jphi,jpsi,jb,jbd,js[0],jds[0],js[1],jds[1],*pit])
    val=np.array(values)
    assert np.max(np.abs(wr))<1e-6
    ss=[CubicSpline(ts,val[:,i]) for i in range(10)]
    eta=.75;k2=5.;dv=4+3*k2
    betaS=(8*eta*(1+k2)-3*k2)/3
    betaV=2*eta*dv/3;betaT=3*k2+8*eta/3
    assert (betaT-betaV)/(betaV-betaS)==3
    def scalar(t,y):
        jp,jpr,jb,jbd=[g(t) for g in ss[:4]]
        f=3*SQ(3)*jpr/(2*k2*t**3)-9*(t*jbd+jb)/(2*k2**2*t**3)
        return [y[1],-3*y[1]/t-betaS*y[0]/t**2+f]
    def vector(h):
        def fun(t,y):
            j,jd=ss[4+2*h](t),ss[5+2*h](t)
            bv=4*t/(SQ(3)*dv);kv=2*t**3*k2/(3*SQ(3)*dv)
            return [y[1],-3*y[1]/t-betaV*y[0]/t**2-bv*(j/t+jd)/kv]
        return fun
    def tensor(h):
        def fun(t,y):
            return [y[1],-3*y[1]/t-betaT*y[0]/t**2-2*ss[8+h](t)]
        return fun
    funcs=[scalar,vector(0),vector(1),tensor(0),tensor(1)]
    modes=[]
    for fun in funcs:
        sol=solve_ivp(fun,(1.,end),[0.+0j,0.+0j],t_eval=ts,
                      rtol=1e-10,atol=1e-11,method="DOP853")
        assert sol.success;modes.append(sol.y)
    output=[]
    for i,t in enumerate(ts):
        p,pd=modes[0][:,i];pdd=scalar(t,[p,pd])[1]
        jp,jpr,jb,jbd=val[i,:4]
        phi=(t*t*pdd+2*t*pd)/(3*(1+k2))+SQ(3)*(jp+jpr)/(2*t*(1+k2))-3*jbd/(2*k2*(1+k2))
        psi=(k2*p-t*pd)/(3*(1+k2))+SQ(3)*jp/(2*t*(1+k2))+3*jb/(2*k2*t*(1+k2))
        shifts=[];gammas=[]
        for h in range(2):
            v,vd=modes[h+1][:,i];j=val[i,4+2*h]
            av=t*dv/(6*SQ(3));bv=4*t/(SQ(3)*dv)
            shifts.append(bv*vd-j/av)
            gammas.append(modes[h+3][0,i])
        output.append([t,phi,psi,*shifts,*gammas])
    hist=np.array(output)
    print("N",N,"Ward",np.max(np.abs(wr)),"V/T modes",
          *[modes[h][0,-1] for h in (1,2,3,4)])
    assert min(abs(modes[h][0,-1]) for h in (1,2,3,4))>1e-7
    return hist
def detector(hist,d=.075,eta_e=.08):
    eta=SQ(3)*np.log(hist[:,0].real)
    assert eta[-1]>eta_e+2*d
    fphi,fpsi,fve,fvb,fplus,fcross=[
        CubicSpline(eta,hist[:,i]) for i in range(1,7)]
    arms=[n,E,B,(n+E)/SQ(2),(n-E)/SQ(2),
          (n+B)/SQ(2),(n-B)/SQ(2),(E+B)/SQ(2),(E-B)/SQ(2)]
    def Q(fn,lo,hi):
        return quad(lambda z:np.real(fn(z)),lo,hi,epsabs=1e-10)[0]+1j*quad(
            lambda z:np.imag(fn(z)),lo,hi,epsabs=1e-10)[0]
    def single(u,sector):
        lam=np.dot(K,u);ue=np.dot(E,u);ub=np.dot(B,u)
        def vals(s):
            ph=fphi(s) if sector in (0,5) else 0
            ps=fpsi(s) if sector in (0,5) else 0
            v=ue*fve(s) if sector in (1,5) else 0
            v+=ub*fvb(s) if sector in (2,5) else 0
            H=(ue*ue-ub*ub)*fplus(s) if sector in (3,5) else 0
            H+=2*ue*ub*fcross(s) if sector in (4,5) else 0
            vd=(ue*fve(s,1) if sector in (1,5) else 0)
            vd+=(ub*fvb(s,1) if sector in (2,5) else 0)
            return ph,ps,v,vd,H
        O=Q(lambda z:(lambda v:-v[0]-v[1]-v[2]+v[4]/2)(
              vals(eta_e+z))*np.exp(1j*lam*z),0,d)
        I=Q(lambda z:(lambda v:-v[0]-v[1]+v[2]+v[4]/2)(
              vals(eta_e+d+z))*np.exp(1j*lam*(d-z)),0,d)
        def mforce(s):
            ph,ps,v,vd,H=vals(s)
            return -1j*lam*ph+vd+hc*v
        def sh(t):
            return Q(lambda s:(1-np.exp(-hc*(t-s)))/hc*mforce(s),0,t)
        M=2*np.exp(1j*lam*d)*sh(eta_e+d)-sh(eta_e)-sh(eta_e+2*d)
        clock=Q(lambda s:np.exp(hc*s)/SQ(3)*vals(s)[0],eta_e,eta_e+2*d)
        return np.exp(hc*(eta_e+2*d))/SQ(3)*(O+I+M)+clock
    response=np.array([[single(u,j) for j in range(6)]for u in arms])
    assert np.max(abs(response[:,:5].sum(axis=1)-response[:,5]))<2e-9
    return np.array([response[i]-response[j] for i,j in
        ((0,1),(1,2),(3,4),(5,6),(7,8))])
if __name__=="__main__":
    r48=detector(source_and_modes(48,21))
    r64=detector(source_and_modes(64,31))
    delta=np.max(abs(r48-r64))
    print("48-grid response",r48)
    print("64-grid response",r64)
    print("max refinement discrepancy",delta)
    assert delta<2e-5
    assert abs(r64[3,2])>1e-6 and abs(r64[4,4])>1e-6
    print("PASS: same compact canonical matter -> five K4 sourced optical helicities")
    print("SCOPE: initial-value Fourier mode, no new Cone coupling or remote calibrated detector")
