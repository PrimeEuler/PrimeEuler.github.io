#!/usr/bin/env python3
"""Gravity v15.1264: homogeneous periodic-cell Maxwell + K4 solid linear
Bianchi-I shear and Hamiltonian-compatible isotropic perturbation.
Free Maxwell is evolved spectrally from original v15.1078 stream function,
with an explicit discrete divergence projection. Spatial means via Parseval.
This is a DECLARED PERIODIC CELL, not the gravity of an isolated packet.
"""
import numpy as np
import sympy as sp
from math import pi,sqrt
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp

def exact_solid():
    b1,b2,b3,C,eta,a,eps,x,y=sp.symbols('b1 b2 b3 C eta a eps x y',positive=True)
    bs=[b1,b2,b3]
    F=C*sp.prod(bs)**sp.Rational(1,3)*(1+eta*(sum(b*b for b in bs)/sum(bs)**2-sp.Rational(1,3)))
    vals={bs[j]:sp.exp(-2*eps*([x,y,-x-y][j]))/a**2 for j in range(3)}
    pressures=[-F+2*b*sp.diff(F,b) for b in bs]
    slopes=[sp.factor(sp.diff(p.subs(vals),eps).subs(eps,0)) for p in pressures]
    assert slopes==[-8*C*eta*x/(9*a*a),-8*C*eta*y/(9*a*a),8*C*eta*(x+y)/(9*a*a)]
    assert sp.simplify(sum(pressures)+F)==0
    return slopes

def run(N=48,nt=41,end=1.2):
    L=4*pi
    x=(np.arange(N)-N//2)*(L/N)
    X=x[:,None,None]; Y=x[None,:,None]; Z=x[None,None,:]
    f=lambda u:np.where(np.abs(u)<1,(1-u*u)**3,0.)
    fp=lambda u:np.where(np.abs(u)<1,-6*u*(1-u*u)**2,0.)
    E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),-fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    h=np.fft.fftn(E0,axes=(1,2,3))
    q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),indexing='ij'))
    k=np.sqrt(np.sum(q*q,axis=0))
    unit=np.zeros_like(q); np.divide(q,k,out=unit,where=k>0)
    h-=unit*np.einsum('i...,i...->...',unit,h)
    curl=1j*np.cross(q,h,axis=0)
    times=np.linspace(1,end,nt)
    r=[]; anis=[]
    for t in times:
        xi=sqrt(3)*np.log(t)
        fac=np.zeros_like(k)
        np.divide(np.sin(k*xi),k,out=fac,where=k>0)
        EH=h*np.cos(k*xi)
        BH=-curl*fac
        Eflat=EH.reshape(3,-1); Bflat=BH.reshape(3,-1)
        E2=(Eflat@Eflat.conj().T).real/N**6
        B2=(Bflat@Bflat.conj().T).real/N**6
        rho=np.trace(E2+B2)/2
        Tij=rho*np.eye(3)-E2-B2
        Pi=Tij-rho*np.eye(3)/3
        r.append(rho);anis.append(Pi)
    r=np.array(r);anis=np.array(anis)
    R0=r[0]
    drift=float(np.max(np.abs(r-R0))/R0)
    assert drift<2e-12
    rho_exact=float(sp.N(sp.Rational(16777216,694386693)/sp.pi**3))
    assert abs(R0-rho_exact)/rho_exact<0.025
    assert max(abs(anis[:,i,j]).max() for i in range(3) for j in range(3) if i!=j)<1e-11
    assert abs(np.trace(anis[0]))<1e-13
    assert np.max(abs(anis[0]/R0-np.diag([4,-14,10])/15))<0.01
    pi_spl=CubicSpline(times,anis[:,[0,1,2],[0,1,2]],axis=0)
    eta=.75; mass=8*eta/3
    def rhs(t,y):
        beta=y[:3];vel=y[3:]
        return np.r_[vel,-3*vel/t-mass*beta/t**2+9*pi_spl(t)/t**4]
    sol=solve_ivp(rhs,(1,end),np.zeros(6),dense_output=True,rtol=1e-12,atol=1e-15)
    assert sol.success
    # Hamiltonian correction, kappa*C=1, u(1)=0.
    def u(t):return 1.5*R0*(t-1)/t**2
    def up(t):return 1.5*R0*(2-t)/t**3
    def upp(t):return 1.5*R0*(2*t-6)/t**4
    def ham(t):return 6*up(t)/t+6*u(t)/t**2-9*R0/t**4
    def iso(t):return -(upp(t)+2*up(t)/t)
    assert abs(ham(1))<1e-13 and abs(ham(end))<1e-13
    assert abs(iso(end)-3*R0/end**4)<1e-13
    bet,vel=np.split(sol.y[:,-1],2)
    acc=rhs(end,sol.y[:,-1])[3:]
    tidalSTF=-(acc+2*vel/end)
    eqres=acc+3*vel/end+mass*bet/end**2-9*anis[-1].diagonal()/end**4
    assert max(abs(eqres))<2e-14
    assert abs(bet.sum())<1e-12 and abs(vel.sum())<1e-12
    assert abs(tidalSTF.sum())<1e-12
    tide=np.diag(np.full(3,iso(end))+tidalSTF)
    assert abs(np.trace(tide)-9*R0/end**4)<1e-12
    result={'N':N,'mean_conformal_energy':float(R0),'energy_drift':drift,
            'initial_Pi_over_R':(anis[0].diagonal()/R0).tolist(),
            'final_Pi':anis[-1].diagonal().tolist(),
            'beta':bet.tolist(),'beta_dot':vel.tolist(),
            'u':float(u(end)),'homogeneous_tide':np.diag(tide).tolist(),
            'tidal_trace':float(np.trace(tide)),
            'hamiltonian_residual':float(ham(end))}
    print(result,flush=True)
    return result

if __name__=='__main__':
    print('PASS K4 stress exact shear derivative',exact_solid())
    a=[run(N) for N in (32,48,64,80)]
    assert abs(a[-1]['tidal_trace']-a[-2]['tidal_trace'])<2e-5
    assert abs(a[-1]['beta'][0]-a[-2]['beta'][0])<2e-5
    assert abs(a[-1]['mean_conformal_energy']-a[-2]['mean_conformal_energy'])<1e-6
    print('PASS periodic-cell linear homogeneous Maxwell-K4 Bianchi I')
    print('OPEN isolated boundary, full 3D metric, causal photon-mirror-clock')
