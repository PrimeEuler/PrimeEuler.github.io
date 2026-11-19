#!/usr/bin/env python3
"""Gravity v15.1235: single oblique Fourier mode, genuine compact Maxwell
source -> constrained scalar, vector and tensor K4 full electric Riemann.

Source: frozen v15.1078 compact divergence-free 3D Maxwell Cauchy data.
Archived operators: scalar v15.728-729, vector v15.710/721,
tensor v15.750, Riemann v15.787. Initial K4 propagating P,f,gamma and
time derivatives zero; nondynamical metric constraints NOT zero.
Output E_ij is one Fourier coefficient; add its -K conjugate in real space.
Not full 3D gravity, k=0, or a photon/mirror/clock detector.
"""
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp
from math import sqrt,pi

def run(N,nt=23,verbose=True):
    L=4*pi
    x=(np.arange(N)-N//2)*L/N
    X=x[:,None,None];Y=x[None,:,None];Z=x[None,None,:]
    f=lambda v:np.where(abs(v)<1,(1-v*v)**3,0.)
    fp=lambda v:np.where(abs(v)<1,-6*v*(1-v*v)**2,0.)
    E0=np.array(np.broadcast_arrays(.5*f(X)*fp(Y/2)*f(Z),
        -fp(X)*f(Y/2)*f(Z),np.zeros((N,N,N))))
    Eh=np.fft.fftn(E0,axes=(1,2,3))
    q=np.array(np.meshgrid(*([np.fft.fftfreq(N,d=L/N)*2*pi]*3),
                           indexing='ij'))
    om=np.sqrt(np.sum(q*q,axis=0))
    curl=1j*np.cross(q,Eh,axis=0)
    K=np.array([1.,0.,1.]); k=np.linalg.norm(K); k2=k*k
    n=K/k; e=np.array([1.,0.,-1.])/sqrt(2)
    b=np.array([0.,1.,0.]); idx=(2,0,2)
    assert abs(n@e)<1e-14 and abs(n@b)<1e-14 and abs(e@b)<1e-14
    ft=lambda field:np.fft.fftn(field)[idx]/N**3
    ts=np.linspace(1.,1.2,nt)
    mat=[]
    for t in ts:
        xi=sqrt(3)*np.log(t)
        sinc=np.zeros_like(om)
        np.divide(np.sin(om*xi),om,out=sinc,where=om>0)
        E=np.fft.ifftn(Eh*np.cos(om*xi),axes=(1,2,3)).real
        B=np.fft.ifftn(-curl*sinc,axes=(1,2,3)).real
        rho=np.sum(E*E+B*B,axis=0)/2
        flux=np.cross(E,B,axis=0)
        stress=-(np.einsum('i...,j...->ij...',E,E)
                 +np.einsum('i...,j...->ij...',B,B))
        stress+=np.eye(3)[:,:,None,None,None]*rho[None,None,...]
        T=np.array([[ft(stress[i,j]) for j in range(3)]
                    for i in range(3)])
        F=np.array([ft(flux[j]) for j in range(3)])
        assert abs(np.trace(T)-ft(rho))<1e-12
        mat.append([ft(rho),n@F,n@T@n,e@F,e@T@n,
                    (e@T@e-b@T@b)/2,b@F,e@T@b])
    mat=np.array(mat)
    R,Fl,Tnn,Fe,Tne,Pt,Fb,Pcross=mat.T
    assert np.max(abs(Fb))<1e-12 and np.max(abs(Pcross))<1e-12
    rr=CubicSpline(ts,R.real); nn=CubicSpline(ts,Tnn.real)
    ln=CubicSpline(ts,Fl.imag); ef=CubicSpline(ts,Fe.imag)
    nt=CubicSpline(ts,Tne.real); TT=CubicSpline(ts,Pt.real)
    eta=.75
    betaS=(8*eta*(1+k2)-3*k2)/3
    betaV=2*eta*(4+3*k2)/3
    betaT=3*k2+8*eta/3
    def scalar_force(t):return 9*(3*nn(t)-rr(t))/(2*k2*t**4)
    # J_V=-sqrt3 F_e/t and b_V J_V=-4 F_e/(4+3k²).
    # Maxwell F_e,xi=-i k T_ne removes numerical differentiation:
    def vector_force_im(t):return -18*nt(t)/(k*t**4)
    def tensor_force(t):return -18*TT(t)/t**4
    def rhs(t,y):
        p,pd,v,vd,g,gd=y
        return [pd,-3*pd/t-betaS*p/t**2+scalar_force(t),
                vd,-3*vd/t-betaV*v/t**2+vector_force_im(t),
                gd,-3*gd/t-betaT*g/t**2+tensor_force(t)]
    sol=solve_ivp(rhs,(1.,1.2),np.zeros(6),rtol=1e-11,
                  atol=1e-14,dense_output=True)
    assert sol.success
    def curvature(t):
        p,pd,v,vd,g,gd=sol.sol(t)
        dydt=rhs(t,[p,pd,v,vd,g,gd])
        pdd,vdd,gdd=dydt[1],dydt[3],dydt[5]
        # Signed Maxwell sources v15.1226:
        # Jphi=Jpsi=-sqrt3*R/t, JB=-i sqrt3*k*Fl/t
        # JB'=(-3*k²*Tnn+i sqrt3*k*Fl)/t².
        Jphi=-sqrt(3)*rr(t)/t
        JBdot=(-3*k2*nn(t)-sqrt(3)*k*ln(t))/t**2
        phi=((t*t*pdd+2*t*pd)/3+sqrt(3)*Jphi/t
             -3*JBdot/(2*k2))/(1+k2)
        S=-3*k2*phi/t**2
        A=3*rr(t)/t**4
        den=4+3*k2
        # f=i*v, sourced vector metric shift Bv=i*B_im.
        Bim=4*t*vd/(sqrt(3)*den)+18*ef(t)/(t*t*den)
        Bimdot=(4*(vd+t*vdd)/(sqrt(3)*den)
                +18*(-sqrt(3)*k*nt(t)-2*ef(t))/(den*t**3))
        V=k*(Bimdot+Bim/t)/(2*t/sqrt(3))
        T=-(gdd+2*gd/t)/2
        Eij=(A*np.eye(3)+S*(np.outer(n,n)-np.eye(3)/3)
             +V*(np.outer(n,e)+np.outer(e,n))
             +T*(np.outer(e,e)-np.outer(b,b)))
        assert abs(np.trace(Eij)-3*A)<1e-12
        return dict(A=float(A),S=float(S),V=float(V),T=float(T),
                    E=Eij,p=float(p),v_im=float(v),gamma=float(g))
    initial=curvature(1.)
    final=curvature(1.2)
    # General initial oblique condition uses Tnn, not Tnn=R.
    source0=(1.5*(3*Tnn[0].real-R[0].real)
             +k2*(-3*R[0].real+4.5*Tnn[0].real))
    assert abs(initial['S']+3*source0/(1+k2))<1e-12
    assert abs(initial['A']-3*R[0].real)<1e-12
    result={'N':N,'S':final['S'],'V':final['V'],
            'T':final['T'],'A':final['A'],
            'p':final['p'],'v_im':final['v_im'],
            'gamma':final['gamma'],'E':final['E']}
    if verbose: print(result)
    return result

if __name__=='__main__':
    runs=[run(N) for N in (32,48,64)]
    for c in ('S','V','T','A'):
        assert abs(runs[-1][c]-runs[-2][c])<2.5e-5
    assert np.max(abs(runs[-1]['E']-runs[-2]['E']))<3e-5
    print('PASS exact Maxwell source, oblique K4 scalar/vector/tensor')
    print('PASS full local electric Riemann and Einstein Ricci trace')
    print('OPEN full 3D mode sum, homogeneous mode, optical detector, quarter action')
