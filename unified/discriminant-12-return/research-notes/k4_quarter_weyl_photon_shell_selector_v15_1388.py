#!/usr/bin/env python3
"""Gravity v15.1388: vacuum photon mass-shell selector and adiabatic switch.
Fixed Weyl-H2 forced Maxwell mode: distinguish off-shell polarization
from real free modes produced by time-dependent switching.
"""
import numpy as np
from math import sqrt
from scipy.integrate import solve_ivp
j=np.ones(3)
qp=np.array([1.,1.,1.]);qm=np.array([1.,1.,-1.])
proj=lambda q:j-q*(q@j)/(q@q)
assert np.linalg.norm(proj(qp))<1e-14
assert np.allclose(proj(qm),[2/3,2/3,4/3])
assert 3**2-qp@qp==6 and 1**2-qm@qm==-2
omega=1.;k=sqrt(3);g=.02
J0=1j*g*np.linalg.norm(proj(qm))/4
def run(T):
 left=-12*T;right=12*T
 sw=lambda t:.5*(1+np.tanh(t/T))
 def rhs(t,y):return [y[1],-k*k*y[0]-J0*sw(t)*np.exp(-1j*omega*t)]
 sol=solve_ivp(rhs,(left,right),[0j,0j],rtol=2e-11,atol=1e-13,method='DOP853')
 assert sol.success
 A,V=sol.y[:,-1]
 Ap=-J0*np.exp(-1j*omega*right)/(k*k-omega*omega)
 Vp=-1j*omega*Ap
 Efree=.5*(abs(V-Vp)**2+k*k*abs(A-Ap)**2)
 Eforced=.5*(abs(Vp)**2+k*k*abs(Ap)**2)
 def FT(delta):
  z=np.pi*delta*T/2
  return z/np.sinh(z)
 cplus=abs(J0)*FT(k-omega)/(2*k*(k-omega))
 cminus=abs(J0)*FT(k+omega)/(2*k*(k+omega))
 predicted=k*k*(cplus*cplus+cminus*cminus)
 assert abs(Efree-predicted)/max(Efree,1e-30)<1e-5
 out=dict(T=T,free_energy=float(Efree),forced_energy=float(Eforced),
          free_to_forced=float(Efree/Eforced),predicted_free_energy=float(predicted))
 print(out,flush=True)
 return out
if __name__=="__main__":
 rows=[run(T) for T in (.5,1.,2.,4.,8.)]
 assert all(rows[i+1]['free_energy']<rows[i]['free_energy'] for i in range(4))
 assert rows[-1]['free_to_forced']<1e-5
 print("PASS nonradiative steady transverse Fourier branch and switching-dependent free wave")
 print("NEGATIVE perpetual driven off-shell mode != continuously emitted on-shell photons")
