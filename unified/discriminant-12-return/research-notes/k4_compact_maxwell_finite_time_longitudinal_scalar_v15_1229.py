#!/usr/bin/env python3
"""Gravity v15.1229: genuine 3D compact free Maxwell -> K4 longitudinal scalar.

E0=(d_y phi,-d_x phi,0), B0=0; phi=f(x)f(y/2)f(z),
f(s)=(1-s*s)^3 on |s|<1, zero outside (v15.1078).
E(ξ)=cos(|q|ξ)E0, B(ξ)=-sin(|q|ξ)/|q| curl E0.
Use FLRW conformal ξ=sqrt(3)log(tau), a=tau/sqrt(3).
All source Fourier coefficients are spatial *means* (FFT / N^3).
Evolve Maxwell exactly in Fourier time and project longitudinal k=1.
Then integrate complete K4 pressure-corrected scalar P ODE with its actual
Maxwell rho, Tzz. Reconstruct sourced Phi_N and scalar full Fermi
electric-Riemann STF; Einstein Ricci trace Aiso=rho_phys/3.
This is NOT full 3D sourced K4 gravity, nor a causal optical detector.
"""
import numpy as np
from math import sqrt,pi
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp

def run(N,nt=23,verbose=True):
    L=4*pi
    dx=L/N
    coord=(np.arange(N)-N//2)*dx
    x=coord[:,None,None];y=coord[None,:,None];z=coord[None,None,:]
    def f(u):return np.where(abs(u)<1,(1-u*u)**3,0.)
    def fp(u):return np.where(abs(u)<1,-6*u*(1-u*u)**2,0.)
    ex,ey,ez=np.broadcast_arrays(.5*f(x)*fp(y/2)*f(z),
                                 -fp(x)*f(y/2)*f(z),
                                 np.zeros((N,N,N)))
    EH=np.fft.fftn(np.array([ex,ey,ez]),axes=(1,2,3))
    frequency=np.fft.fftfreq(N,d=dx)*2*pi
    Q=np.array(np.meshgrid(frequency,frequency,frequency,indexing='ij'))
    mod=np.sqrt(np.sum(Q*Q,axis=0))
    curl=1j*np.array([Q[1]*EH[2]-Q[2]*EH[1],
                       Q[2]*EH[0]-Q[0]*EH[2],
                       Q[0]*EH[1]-Q[1]*EH[0]])
    # k=1 corresponds to FFT integer mode n=2 for L=4*pi.
    k=1.;mode=2; eta=.75
    beta=(8*eta*(1+k*k)-3*k*k)/3
    taus=np.linspace(1.,1.2,nt)
    rows=[]
    for tau in taus:
        xi=sqrt(3)*np.log(tau)
        fac=np.zeros_like(mod)
        np.divide(np.sin(mod*xi),mod,out=fac,where=mod>0)
        E=np.fft.ifftn(EH*np.cos(mod*xi),axes=(1,2,3)).real
        B=np.fft.ifftn(-curl*fac,axes=(1,2,3)).real
        rho=np.sum(E*E+B*B,axis=0)/2
        tzz=rho-E[2]**2-B[2]**2
        fluxz=E[0]*B[1]-E[1]*B[0]
        rows.append([np.fft.fftn(field)[0,0,mode]/N**3
                     for field in (rho,tzz,fluxz)])
    rows=np.array(rows)
    assert np.max(abs(rows[:,0].imag))<1.e-12
    assert np.max(abs(rows[:,1].imag))<1.e-12
    assert np.max(abs(rows[:,2].real))<1.e-12
    r,tt,sz=rows.T
    # Maxwell FLRW test-stress Ward: d_xi r=-ik sz; d_xi sz=-ik tt.
    xi=sqrt(3)*np.log(taus)
    dr=CubicSpline(xi,r).derivative()(xi)
    ds=CubicSpline(xi,sz).derivative()(xi)
    errrho=float(max(abs(dr[2:-2]+1j*k*sz[2:-2]))/max(abs(r)))
    errmom=float(max(abs(ds[2:-2]+1j*k*tt[2:-2]))/max(abs(r)))
    rsp=CubicSpline(taus,r.real)
    tsp=CubicSpline(taus,tt.real)
    ssp=CubicSpline(taus,sz.imag)
    def accel(t,p,pdot):
        return -3*pdot/t-beta*p/t**2+9*(3*tsp(t)-rsp(t))/(2*k*k*t**4)
    def ode(t,u):return [u[1],accel(t,*u)]
    sol=solve_ivp(ode,(1.,1.2),(0.,0.),dense_output=True,
                  rtol=2e-11,atol=2e-13)
    assert sol.success
    def tide(t):
        p,pdot=sol.sol(t)
        pdd=accel(t,p,pdot)
        rho,tzz,flux=rsp(t),tsp(t),1j*ssp(t)
        # Signed ADM: Jphi=Jpsi=-sqrt3*rho/tau,
        # JB=-i sqrt3 k flux/tau,
        # JBdot=(-3k²*Tzz+i sqrt3 k flux)/tau².
        jbprime=(-3*k*k*tzz+1j*sqrt(3)*k*flux)/t**2
        jphi=-sqrt(3)*rho/t
        phi=((t*t*pdd+2*t*pdot)/3 +
             sqrt(3)*jphi/t-3*jbprime/(2*k*k))/(1+k*k)
        return float(np.real(-3*k*k*phi/t**2)),float(3*rho/t**4)
    stf0,a0=tide(1.)
    stf1,a1=tide(1.2)
    init_exact=-9*r[0].real*(k*k+2)/(2*(k*k+1))
    slope_exact=9*r[0].real*(7*k*k+10)/(2*(k*k+1))
    assert abs(stf0-init_exact)<1e-12
    assert abs(a0-3*r[0].real)<1e-12
    assert abs(tsp(1)-rsp(1))<1e-12
    assert abs(sz[0])<1e-12
    assert errrho<6e-4 and errmom<6e-4
    result=dict(N=N,k=k,eta=eta,rho_fourier_init=r[0].real,
                stf0=stf0,stf_slope_exact=slope_exact,stf_final=stf1,
                isotropic_final=a1,energy_ward_rel=errrho,
                momentum_ward_rel=errmom)
    if verbose: print(result)
    return result

if __name__=='__main__':
    runs=[run(N) for N in (48,64,80)]
    assert runs[2]['energy_ward_rel']<runs[1]['energy_ward_rel']<runs[0]['energy_ward_rel']
    assert runs[2]['momentum_ward_rel']<runs[1]['momentum_ward_rel']<runs[0]['momentum_ward_rel']
    # Empirical convergence across two coarse-resolution pairs only.
    assert abs(runs[2]['stf_final']-runs[1]['stf_final'])<1.e-5
    assert abs(runs[1]['stf_final']-runs[0]['stf_final'])<3.e-5
    assert abs(runs[2]['isotropic_final']-runs[1]['isotropic_final'])<1.e-6
    print('PASS finite-time free Maxwell source, Ward convergence, K4 scalar integration')
    print('OPEN full 3D K4 S/V/T and k=0, optical endpoint/mirror/clock detector')
