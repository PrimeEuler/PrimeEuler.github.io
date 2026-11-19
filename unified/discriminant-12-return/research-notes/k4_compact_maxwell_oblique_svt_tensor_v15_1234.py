#!/usr/bin/env python3
"""Gravity v15.1234: original compact 3D Maxwell field, oblique K=(1,0,1)
SVT projectors and conditional sourced K4 tensor-plus full electric Riemann.
The scalar and vector *metric* solutions are not computed. Physical source
has zero initial magnetic field; FFT spatial sampling of the C2 bump
is not exactly divergence-free in every discrete high-frequency bin.
"""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp
from math import sqrt,pi

def run(N,nt=17):
    L=4*pi
    x=(np.arange(N)-N//2)*L/N
    X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
    f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
    fp=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
    initial=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),
        -fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    h=np.fft.fftn(initial,axes=(1,2,3))
    freq=np.fft.fftfreq(N,d=L/N)*2*pi
    q=np.array(np.meshgrid(freq,freq,freq,indexing='ij'))
    om=np.sqrt(np.sum(q*q,axis=0))
    # Exact analytic divergence-free continuum; finite sampled FFT has
    # alias errors, so only assert small selected Fourier-bin divergence.
    assert np.abs(np.sum(q*h,axis=0)[2,0,2])/np.max(np.abs(h))<1e-10
    curl=1j*np.cross(q,h,axis=0)
    kv=np.array([1.,0.,1.]);k=np.linalg.norm(kv);n=kv/k
    e=np.array([1.,0.,-1.])/sqrt(2);b=np.array([0.,1.,0.])
    assert max(abs(n@e),abs(n@b),abs(e@b))<1e-14
    idx=(2,0,2);ts=np.linspace(1.,1.2,nt);rows=[]
    ft=lambda arr:np.fft.fftn(arr)[idx]/N**3
    for t in ts:
        xi=sqrt(3)*np.log(t)
        fac=np.zeros_like(om)
        np.divide(np.sin(om*xi),om,out=fac,where=om>0)
        E=np.fft.ifftn(h*np.cos(om*xi),axes=(1,2,3)).real
        B=np.fft.ifftn(-curl*fac,axes=(1,2,3)).real
        rho=np.sum(E*E+B*B,axis=0)/2
        flux=np.cross(E,B,axis=0)
        stress=-(np.einsum('i...,j...->ij...',E,E)
                +np.einsum('i...,j...->ij...',B,B))
        stress+=np.eye(3)[:,:,None,None,None]*rho[None,None,:,:,:]
        R=ft(rho);F=np.array([ft(flux[j]) for j in range(3)])
        T=np.array([[ft(stress[i,j]) for j in range(3)] for i in range(3)])
        assert abs(np.trace(T)-R)<1.e-12
        scalar=n@T@n-np.trace(T)/3
        vec=np.array([e@F,b@F])
        plus=(e@T@e-b@T@b)/2
        cross=e@T@b
        rows.append((R,F,T,scalar,vec,plus,cross))
    # Independent approximate FLRW/conformal Maxwell Ward test of stress,
    # using cubic-spline derivatives rather than Maxwell evolution formulas.
    xi=sqrt(3)*np.log(ts)
    R=np.array([v[0] for v in rows])
    F=np.array([v[1] for v in rows])
    T=np.array([v[2] for v in rows])
    dr=CubicSpline(xi,R).derivative()(xi)
    df=CubicSpline(xi,F,axis=0).derivative()(xi)
    er=float(max(abs(dr[2:-2]+1j*F[2:-2]@kv))/max(abs(R)))
    em=float(np.max(abs(df[2:-2]+1j*np.einsum('j,tij->ti',kv,T[2:-2])))/max(abs(R)))
    assert abs(rows[0][4][0])<1e-13
    assert max(abs(v[4][1]) for v in rows)<1e-12
    assert max(abs(v[6]) for v in rows)<1e-12
    plus=np.array([v[5].real for v in rows])
    spl=CubicSpline(ts,plus)
    eta=.75;ksq=2.;beta=3*ksq+8*eta/3
    # Archive v15.750 tensor (+) response, kappa=1:
    # gamma_ddot+3gamma_dot/t+beta gamma/t²=-2 Pi_plus,
    # physical Pi_plus=(9/t^4)*conformal Pi_plus.
    def rhs(t,u):
        return [u[1],-3*u[1]/t-beta*u[0]/t**2-18*spl(t)/t**4]
    sol=solve_ivp(rhs,(1.,1.2),(0.,0.),rtol=1e-11,atol=1e-14,dense_output=True)
    assert sol.success
    gamma,gd=sol.sol(1.2)
    gdd=rhs(1.2,[gamma,gd])[1]
    tide=-(gdd+2*gd/1.2)/2
    assert abs(9*plus[0]+rhs(1.,[0.,0.])[1]/2)<1e-14
    result={'N':N,'scalar_0':rows[0][3].real,
            'scalar_at_1p2':rows[-1][3].real,
            'vector_1_at_1p2_imag':rows[-1][4][0].imag,
            'tensor_plus_at_1p2':rows[-1][5].real,
            'tensor_cross_max':float(max(abs(v[6]) for v in rows)),
            'gamma_at_1p2':float(gamma),
            'tensor_full_tide_at_1p2':float(tide),
            'ward_energy':er,'ward_momentum':em}
    print(result)
    return result

if __name__=='__main__':
    a=[run(N) for N in (32,48,64)]
    assert abs(a[-1]['gamma_at_1p2']-a[-2]['gamma_at_1p2'])<5e-7
    assert abs(a[-1]['tensor_full_tide_at_1p2']-a[-2]['tensor_full_tide_at_1p2'])<2e-5
    assert a[-1]['ward_energy']<a[-2]['ward_energy']<a[0]['ward_energy']
    assert a[-1]['ward_momentum']<a[-2]['ward_momentum']<a[0]['ward_momentum']
    print('PASS compact Maxwell oblique SVT stress plus conditional K4 tensor full Riemann')
    print('OPEN scalar/vector metric response, all 3D K4 modes, zero-mode, causal optics')
