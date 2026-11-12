#!/usr/bin/env python3
"""v15.817: finite-energy compact C7 four-wave canonical scalar initial data.
Five stress helicities at common K remain nonzero with cutoff gradients.
This is source-only initial-slice Fourier data, not evolved K4 detector.
"""
import numpy as np
from numpy.fft import fftn
from math import sqrt
L=8*np.pi;K=np.array([2.,0.,1.]);n=K/sqrt(5)
e=np.array([1.,0.,-2.])/sqrt(5);b=np.array([0.,1.,0.])
def compute(N,R=10.):
    x=(np.arange(N)-N//2)*L/N
    xx=x[:,None,None];yy=x[None,:,None];zz=x[None,None,:]
    u=x/R
    h=np.where(abs(u)<1,(1-u*u)**8,0.)
    hp=np.where(abs(u)<1,-16*u*(1-u*u)**7/R,0.)
    w=h[:,None,None]*h[None,:,None]*h[None,None,:]
    wx=hp[:,None,None]*h[None,:,None]*h[None,None,:]
    wy=h[:,None,None]*hp[None,:,None]*h[None,None,:]
    wz=h[:,None,None]*h[None,:,None]*hp[None,None,:]
    z=xx-yy+zz
    base=np.cos(2*xx)+np.cos(zz)+sqrt(2)*(np.cos(xx+yy)+np.cos(z))
    bx=-2*np.sin(2*xx)-sqrt(2)*(np.sin(xx+yy)+np.sin(z))
    by=-sqrt(2)*np.sin(xx+yy)+sqrt(2)*np.sin(z)
    bz=-np.sin(zz)-sqrt(2)*np.sin(z)
    g=[wx*base+w*bx,wy*base+w*by,wz*base+w*bz]
    binK=(8,0,4) # L=8pi Fourier spacing 1/4, K=(2,0,1)
    normal=np.sum(w*w)
    # At tau=1, physical orthonormal scalar stress anisotropy is 3 grad_i chi grad_j chi.
    G=np.array([[3*fftn(g[i]*g[j])[binK]/normal for j in range(3)]for i in range(3)])
    out=np.array([n@G@n-np.trace(G)/3,n@G@e,n@G@b,
                  (e@G@e-b@G@b)/2,e@G@b])
    assert np.max(np.abs(out.imag))<1e-9
    assert np.min(np.abs(out))>.1
    return out
r48=compute(48);r64=compute(64);r80=compute(80)
assert np.max(abs(r48-r80))<1e-8
assert np.max(abs(r64-r80))<1e-10
benchmark=np.array([-24/5,3/5,-3*sqrt(5)/10,-3/5,3*sqrt(5)/5])
assert np.max(abs(r80-benchmark))>.2 # finite cutoff is not the plane-wave witness
print("PASS compact C7 initial canonical source five nonzero helicities")
print("48^3",r48)
print("64^3",r64)
print("80^3",r80)
print("UNBOUNDED_PLANE_WAVE_CONTROL",benchmark)
print("SCOPE positive local KG initial energy; later on-shell evolution by Cauchy problem required")
