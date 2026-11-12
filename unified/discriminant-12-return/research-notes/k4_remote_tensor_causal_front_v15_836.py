#!/usr/bin/env python3
"""v15.836: full-spectrum localized K4 FREE tensor master causal propagation.

eta_solid=3/4, a=tau/sqrt3, gamma''+3gamma'/tau+
[3k^2+8eta/3]gamma/tau²=0. For s=ln(tau), gamma=tau^-1 u,
u_ss-3u_xx+u=0. Initial C7 bump at x=5, radius 2, u_s(0)=0.
Full electric tensor R^x_(0x0)=-(gamma''+2gamma'/tau)/2
=-tau^-3(u_ss-u_s)/2. Compare full reconstruction with one Fourier mode.

One-dimensional propagation: transverse extent is unbounded; this is
NOT a 3D compact canonical matter emitter, nor a photon interferometer.
"""
import numpy as np
from numpy.fft import fft,ifft,fftfreq
L=32.
R=2.
xc=5.
receiver=0.
front=(xc-R)/np.sqrt(3)
def evaluate(N,ss=(0.,.5,1.,1.5,2.,2.35)):
    x=np.arange(N)*L/N
    rr=(x-xc+L/2)%L-L/2
    bump=np.where(np.abs(rr)<R,(1-(rr/R)**2)**8,0.)
    init=fft(bump)
    k=2*np.pi*fftfreq(N,d=L/N)
    omega=np.sqrt(3*k*k+1.)
    out=[]
    for s in ss:
        co=np.cos(omega*s)
        si=np.sin(omega*s)
        u=ifft(init*co).real
        us=ifft(-init*omega*si).real
        uss=ifft(-init*omega**2*co).real
        gamma=np.exp(-s)*u
        Rfull=-np.exp(-3*s)*(uss-us)/2
        m=4
        isolated=init[m]*co[m]/N*np.exp(-s)
        out.append((s,gamma[0],Rfull[0],isolated))
    return out
r1024=evaluate(1024)
r2048=evaluate(2048)
assert abs(front-np.sqrt(3))<1e-14
for (s,u,R0,one),(s2,u2,R2,one2) in zip(r1024,r2048):
    assert s==s2
    if s<front-.05:
        assert abs(u)<3e-8 and abs(u2)<3e-8
        assert abs(R0)<5e-7 and abs(R2)<5e-7,(s,R0,R2)
    assert abs(u-u2)<1e-6
    assert abs(R0-R2)<2e-4,(s,R0,R2)
assert abs(r2048[-2][1])>1e-12 or abs(r2048[-1][1])>1e-10
assert abs(r2048[1][3])>1e-7
print("K4 free tensor causal front log_tau=",front,"cosmic tau=",np.exp(front))
for row in r2048:
    print("s, receiver full gamma, full electric Riemann, isolated Fourier mode",row)
print("PASS full spectrum: receiver quiet before front, tidal field after front")
print("PASS one globally nonlocal Fourier mode wrongly appears before front")
print("SCOPE: FREE one-dimensional tensor master, not sourced 3D emitter/detector")
