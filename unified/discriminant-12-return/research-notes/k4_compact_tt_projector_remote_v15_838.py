#!/usr/bin/env python3
"""v15.838: TT projector of a 3D compact canonical-matter stress is nonlocal.

One real canonical scalar Cauchy datum chi0=w(r)cos(2x+y+1.4z),
chi_dot0=-chi0 on a coasting FLRW slice. C7 spherical cutoff centered
at (6,0,0) radius 2.5, periodic spatial box side 24. Receiver is
(0,0,0), outside matter support by a coordinate distance >=3.5.

At tau=1, anisotropic spatial stress S_ij=partial_i chi0 partial_j chi0.
Compute its full 3D Fourier TT projector, inverse-transform and evaluate
at the receiver. TT is nonlocal: its nonzero remote value is NOT a
physical acausal arrival or the complete gravitational Riemann tensor.
"""
import numpy as np
from numpy.fft import fftn,ifftn,fftfreq

def compute(N):
    length=24.0; dx=length/N
    q=(np.arange(N)-N//2)*dx
    x=q[:,None,None];y=q[None,:,None];z=q[None,None,:]
    X=x-6.0;Y=y;Z=z
    r=np.sqrt(X*X+Y*Y+Z*Z)
    radius=2.5;u=r/radius
    bump=np.where(u<1,(1-u*u)**8,0.0)
    bump_dr_over_r=np.where(u<1,-16*(1-u*u)**7/radius**2,0.0)
    arg=2*x+y+1.4*z
    cos=np.cos(arg);sin=np.sin(arg)
    grad=[bump_dr_over_r*X*cos-2*bump*sin,
          bump_dr_over_r*Y*cos-bump*sin,
          bump_dr_over_r*Z*cos-1.4*bump*sin]
    stress=np.array([[grad[i]*grad[j] for j in range(3)] for i in range(3)])
    receiver=N//2
    assert np.array_equal(stress[:,:,receiver,receiver,receiver],np.zeros((3,3)))
    kk=2*np.pi*fftfreq(N,d=dx)
    kvals=[kk[:,None,None],kk[None,:,None],kk[None,None,:]]
    k2=sum(k*k for k in kvals)
    inv=np.zeros_like(k2)
    np.divide(1.0,k2,out=inv,where=k2!=0)
    P=np.array([[(1.0 if i==j else 0.0)-kvals[i]*kvals[j]*inv
                for j in range(3)] for i in range(3)])
    Shat=fftn(stress,axes=(-3,-2,-1))
    projected=np.einsum('iaxyz,abxyz,jbxyz->ijxyz',P,Shat,P,optimize=True)
    ptr=np.einsum('abxyz,baxyz->xyz',P,Shat,optimize=True)
    TT=projected-0.5*P*ptr
    # k=0 has no distinguished wave direction; choose zero TT mean.
    TT[:,:,0,0,0]=0
    norm=np.max(abs(Shat))
    assert np.max(abs(np.trace(TT,axis1=0,axis2=1)))/norm<1e-12
    assert np.max(abs(kvals[0]*TT[0,1]+kvals[1]*TT[1,1]+kvals[2]*TT[2,1]))/norm<1e-12
    field=ifftn(TT,axes=(-3,-2,-1)).real
    value=field[:,:,receiver,receiver,receiver]
    return float(np.linalg.norm(value)),value

if __name__=='__main__':
    vals=[]
    for n in (96,112,128):
        norm,matrix=compute(n)
        vals.append(norm)
        print(f'N={n}: local stress 0, TT receiver Frobenius norm={norm:.15g}')
    assert min(vals)>1e-3
    assert max(vals)-min(vals)<5e-7
    print('PASS compact canonical scalar stress has nonlocal TT projection')
    print('PASS TT transverse/traceless, 96^3/112^3/128^3 refinement')
    print('NOTE: TT projection is not a complete causal detector/Riemann signal')
