#!/usr/bin/env python3
"""v15.830: generic 3D pure-gauge FLRW optical time-delay test.

Passive diffeo eta_new=eta+T, x_new=x+U generates
Phi=-(T'+H*T), V_i=U_i'-partial_i T,
h_ij=-2H*T delta_ij-partial_i U_j-partial_j U_i.
Check outgoing and inbound null rays, free geodesic mirrors, clock and
the same physical emission event. Do NOT confuse an explicit pure-gauge
test with proof of arbitrary on-shell K4 gauge covariance.
"""
import numpy as np
from scipy.integrate import quad
H=1/np.sqrt(3.)
a=lambda t:np.exp(H*t)/np.sqrt(3.)
K=np.array([[2.,0.,1.],[1.,2.,-.5]])
OMEGA=np.array([1.1,.73])
TA=np.array([.17+.02j,-.09+.035j])
UA=np.array([[.12,-.06,.08],[-.05,.11,.04]],dtype=complex)

def quadrature(fn,lo,hi):
    return quad(lambda z: np.real(fn(z)),lo,hi,epsabs=5e-12)[0]+1j*quad(
        lambda z:np.imag(fn(z)),lo,hi,epsabs=5e-12)[0]

def gauge(t,x):
    t=np.asarray(t).item();x=np.asarray(x)
    phase=np.exp(-1j*OMEGA*t+1j*K@x)
    temporal=np.array([t**3,t**4])
    dtemp=np.array([3*t*t,4*t**3])
    ddtemp=np.array([6*t,12*t*t])
    z=temporal*phase
    dz=(dtemp-1j*OMEGA*temporal)*phase
    ddz=(ddtemp-2j*OMEGA*dtemp-OMEGA**2*temporal)*phase
    Tg=np.dot(TA,z);Tdt=np.dot(TA,dz)
    U=np.sum(UA*z[:,None],axis=0)
    Ud=np.sum(UA*dz[:,None],axis=0)
    Udd=np.sum(UA*ddz[:,None],axis=0)
    gradT=np.sum(1j*K*(TA*z)[:,None],axis=0)
    gradU=np.einsum('mi,mj,m->ij',UA,1j*K,z)
    return Tg,Tdt,U,Ud,Udd,gradT,gradU

def arm(u,d=.075,te=.08,return_parts=False,ignore_shear=False,
        ignore_mirrors=False,ignore_clock=False):
    u=np.asarray(u,float);u=u/np.linalg.norm(u)
    zero=np.zeros(3)
    def fields(t,x):
        T,Tdt,U,Ud,Udd,gradT,gradU=gauge(t,x)
        Phi=-Tdt-H*T
        Vu=np.dot(u,Ud-gradT)
        huu=-2*H*T-(0 if ignore_shear else 2*(u@gradU@u))
        return Phi,Vu,huu,U,Ud,Udd
    O=quadrature(lambda s:(lambda f:-f[0]-f[1]+f[2]/2)(
            fields(te+s,s*u)),0,d)
    I=quadrature(lambda s:(lambda f:-f[0]+f[1]+f[2]/2)(
            fields(te+d+s,(d-s)*u)),0,d)
    M=0 if ignore_mirrors else (
        2*np.dot(u,gauge(te+d,d*u)[2])-
        np.dot(u,gauge(te,zero)[2])-
        np.dot(u,gauge(te+2*d,zero)[2]))
    C=0 if ignore_clock else quadrature(
        lambda t:a(t)*fields(t,zero)[0],te,te+2*d)
    Te=gauge(te,zero)[0];Tr=gauge(te+2*d,zero)[0]
    event=(a(te+2*d)-a(te))*Te
    physical=a(te+2*d)*(O+I+M)+C+event
    if not any((ignore_shear,ignore_mirrors,ignore_clock)):
        assert abs(O+I+M-(Tr-Te))<2e-10
        assert abs(C+a(te+2*d)*Tr-a(te)*Te)<2e-10
        assert abs(physical)<2e-10
    if return_parts:
        return physical,np.array([O,I,M,C,event],dtype=complex)
    return physical

n=np.array([2.,0.,1.])/np.sqrt(5)
e=np.array([1.,0.,-2.])/np.sqrt(5)
b=np.array([0.,1.,0.])
arms=[n,e,b,(n+e)/np.sqrt(2),(n-e)/np.sqrt(2),
      (n+b)/np.sqrt(2),(n-b)/np.sqrt(2),
      (e+b)/np.sqrt(2),(e-b)/np.sqrt(2)]
pairs=[(0,1),(1,2),(3,4),(5,6),(7,8)]

def main():
    residuals=[];parts=[]
    for u in arms:
        val,pr=arm(u,return_parts=True)
        residuals.append(val);parts.append(pr)
    residuals=np.array(residuals);parts=np.array(parts)
    differential=lambda arr:np.array([arr[i]-arr[j] for i,j in pairs])
    assert np.max(abs(differential(residuals)))<2e-10
    assert np.max(abs(parts))>1e-4
    noshear=np.array([arm(u,ignore_shear=True) for u in arms])
    nomirror=np.array([arm(u,ignore_mirrors=True) for u in arms])
    noclock=np.array([arm(u,ignore_clock=True) for u in arms])
    assert np.max(abs(differential(noshear)))>1e-6
    assert np.max(abs(differential(nomirror)))>1e-6
    assert np.max(abs(noclock))>1e-6
    print('PASS 3D two-generator gauge, 9 physical arms; max residual',
          np.max(abs(residuals)))
    print('PASS five differential gauge nulls',differential(residuals))
    print('MISSING_SHEAR spurious differentials',differential(noshear))
    print('MISSING_MIRROR spurious differentials',differential(nomirror))
    print('MISSING_CLOCK absolute bias',noclock[0])
    unequal=[.075,.11,.09,.13,.06,.1,.08,.075,.12]
    uneq=np.array([arm(u,d=d) for u,d in zip(arms,unequal)])
    assert np.max(abs(uneq))<2e-10
    print('PASS unequal-arm event-anchored gauge null',np.max(abs(uneq)))
    for t in (.12,.27,.49):
        x=np.array([.13,-.21,.42]);dt=1e-5
        gg=gauge(t,x)
        def Phi(tt,xx):
            z=gauge(tt,xx)
            return -z[1]-H*z[0]
        def VV(tt,xx):
            z=gauge(tt,xx)
            return z[3]-z[5]
        gradPhi=np.array([(Phi(t,x+dt*np.eye(3)[i])-
            Phi(t,x-dt*np.eye(3)[i]))/(2*dt) for i in range(3)])
        vdot=(VV(t+dt,x)-VV(t-dt,x))/(2*dt)
        error=np.linalg.norm(-gradPhi+vdot+H*VV(t,x)-
                (gg[4]+H*gg[3]))
        assert error<1e-8
    print('PASS 3D geodesic forcing finite-difference identity')
if __name__=='__main__':main()
