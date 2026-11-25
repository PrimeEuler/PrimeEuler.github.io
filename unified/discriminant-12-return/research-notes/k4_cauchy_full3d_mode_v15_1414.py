#!/usr/bin/env python3
"""v15.1414 corrective full 3D spatial Fourier projection of v15.1413.
TT Weyl carrier has ONLY z harmonics +/-1, so two orthogonal z
evaluations extract exact q_z=-1 coefficient, not a fixed-z slice.
Fixed-background sigma/TT source; not total action backreaction.
"""
import numpy as np
from scipy.integrate import solve_ivp,simpson
from scipy.interpolate import CubicSpline
from k4_cauchy_weyl_maxwell_v15_1413 import current
def full3(t,N=16,a=.3,kind="cauchy",h=4e-4):
 j0=current(t,N,a,kind,z=0,h=h)
 j90=current(t,N,a,kind,z=np.pi/2,h=h)
 # For J(z)=C*cos(z)+S*sin(z), Fourier e^(-iz) amplitude=(C+i*S)/2.
 coeff=(np.fft.fft2(j0,axes=(-2,-1))[:,1,1]+
        1j*np.fft.fft2(j90,axes=(-2,-1))[:,1,1])/(2*N*N)
 q=np.array([1.,1.,-1.])
 jt=coeff[1:]-q*(q@coeff[1:])/(q@q)
 return coeff,jt
def run(N=16,a=.3,g=.05):
 ts=np.linspace(0,1.2,25)
 samples=np.array([full3(float(t),N,a)[1] for t in ts])
 drive=CubicSpline(ts,samples,axis=0)
 def rhs(t,y):return np.r_[y[3:],-3*y[:3]-g*drive(t)]
 sol=solve_ivp(rhs,(0,1.2),np.zeros(6,complex),dense_output=True,
               rtol=1e-11,atol=1e-17,method="DOP853")
 assert sol.success
 E=float((np.sum(abs(sol.y[3:,-1])**2)+3*np.sum(abs(sol.y[:3,-1])**2))/2)
 xx=np.linspace(0,1.2,1201);Y=sol.sol(xx)
 W=float(-simpson(np.real(np.sum(np.conj(Y[3:])*g*drive(xx).T,axis=0)),x=xx))
 if g:assert abs(E-W)/E<2e-6
 print(dict(N=N,amplitude=a,coupling=g,EM_mode_energy=E,source_work=W,
       work_relative_residual=abs(E-W)/E if E else 0),flush=True)
 return E
if __name__=="__main__":
 for N in (16,24,32):
  out={z:float(np.linalg.norm(full3(.7,N,.3,z)[1]))
       for z in ("leading","metric","particular","cauchy")}
  print("CURRENT",N,out,flush=True)
  assert abs(out["cauchy"]-.035962686)<1e-6
 for h in (.0016,.0008,.0004,.0002):
  print("STEP",h,float(np.linalg.norm(full3(.7,24,.3,h=h)[1])),flush=True)
 E=run();half=run(g=.025);zero=run(g=0.);Ea=run(a=.15)
 assert abs(E/half-4)<1e-8 and zero==0 and .03<Ea/E<.09
 print("PASS full spatial q=(1,1,-1) Fourier mode and sourced Maxwell work")
 print("CORRECTION v15.1413 fixed-z source was not a q_z=-1 Fourier projection")
 print("OPEN full Einstein+sigma+Maxwell feedback and physical q2 coupling")
