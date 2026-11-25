#!/usr/bin/env python3
"""Gravity v15.1415: fully coupled flat-target 1+1D Maxwell/sigma surrogate
with frozen tidal coefficient. Preliminary comparator for curved H2 v1416,
not full Weyl tensor, Einstein metric or derived Cone-gravity coupling.
L=1/2(At²-Ax²+ut²-ux²+vt²-vx²)+g At(ut vx-ux vt).
"""
import numpy as np
from scipy.integrate import solve_ivp
def run(N=32,g=.12,T=3.):
 x=2*np.pi*np.arange(N)/N
 k=np.fft.fftfreq(N,d=1/N)
 Dx=lambda v:np.fft.ifft(1j*k*np.fft.fft(v)).real
 def velocities(z):
  A,u,v,pA,pu,pv=z.reshape(6,N)
  Ax,ux,vx=map(Dx,(A,u,v))
  det=1-g*g*(ux*ux+vx*vx)
  assert np.min(det)>.9
  At=(pA-g*vx*pu+g*ux*pv)/det
  ut=pu-g*vx*At;vt=pv+g*ux*At
  return At,ut,vt,Ax,ux,vx,det
 def ode(t,z):
  At,ut,vt,Ax,ux,vx,_=velocities(z)
  return np.array([At,ut,vt,Dx(Ax),Dx(ux+g*At*vt),Dx(vx-g*At*ut)]).ravel()
 def energy(z):
  At,ut,vt,Ax,ux,vx,det=velocities(z)
  return np.mean((At**2+Ax**2+ut**2+ux**2+vt**2+vx**2)/2
    +g*At*(ut*vx-ux*vt))
 A=np.zeros_like(x);u=.16*np.sin(x);v=.13*np.sin(2*x+.3)
 At=np.zeros_like(x);ut=.16*np.cos(x);vt=-.13*np.cos(2*x+.3)
 ux,vx=Dx(u),Dx(v)
 z=np.array([A,u,v,g*(ut*vx-ux*vt),ut,vt]).ravel()
 sol=solve_ivp(ode,(0,T),z,method="DOP853",rtol=2e-10,
               atol=3e-12,dense_output=True)
 assert sol.success
 E=np.array([energy(sol.sol(t)) for t in np.linspace(0,T,25)])
 relative=float(np.max(abs(E-E[0]))/E[0])
 rms=float(np.sqrt(np.mean(sol.y[:N,-1]**2)))
 assert relative<3e-8
 out=dict(N=N,g=g,energy_initial=float(E[0]),
     relative_energy_drift=relative,EM_field_rms=rms)
 print(out,flush=True)
 return out
if __name__=="__main__":
 a=run();b=run(g=.06);zero=run(g=0);fine=run(N=48)
 assert zero["EM_field_rms"]==0
 assert 1.9<a["EM_field_rms"]/b["EM_field_rms"]<2.1
 assert abs(a["EM_field_rms"]-fine["EM_field_rms"])<2e-7
 print("PASS flat-target preliminary coupled energy/no-coupling comparator")
 print("OPEN physically complete curved H2/Weyl/EH EFT")
