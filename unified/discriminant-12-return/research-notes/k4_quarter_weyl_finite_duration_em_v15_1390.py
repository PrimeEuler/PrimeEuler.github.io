#!/usr/bin/env python3
"""Gravity v15.1390: finite-time Gaussian-envelope Maxwell source.
Phase-matched vs detuned retarded free Maxwell response. Prescribed
envelope, NOT a self-consistent finite-energy H2/TT wave packet.
"""
from math import sqrt,pi
import numpy as np
from scipy.integrate import solve_ivp
omega=1.;J0=.02j
def run(width,k):
 left=-8*width;right=8*width
 def source(t):return -J0*np.exp(-1j*omega*t-t*t/(2*width*width))
 def rhs(t,y):return np.array([y[1],-k*k*y[0]+source(t)])
 sol=solve_ivp(rhs,(left,right),np.array([0j,0j]),method='DOP853',rtol=2e-12,atol=1e-14)
 assert sol.success
 amp=np.sqrt(2*pi)*width
 imin=amp*np.exp(-.5*width**2*(k-omega)**2)
 iplus=amp*np.exp(-.5*width**2*(k+omega)**2)
 A=J0/(2j*k)*(np.exp(-1j*k*right)*imin-np.exp(1j*k*right)*iplus)
 V=J0/(2j*k)*(-1j*k*np.exp(-1j*k*right)*imin-1j*k*np.exp(1j*k*right)*iplus)
 err=float(np.max(abs(np.array([A,V])-sol.y[:,-1])))
 E=.5*(abs(sol.y[1,-1])**2+k*k*abs(sol.y[0,-1])**2)
 predicted=abs(J0)**2*(imin**2+iplus**2)/4
 assert err<2e-11 and abs(E-predicted)<2e-12
 return dict(width=width,k=k,post_pulse_energy=float(E),analytic_energy=float(predicted),ode_error=err)
if __name__=='__main__':
 rows=[]
 for width in (.5,1.,2.,3.):
  on=run(width,1.);off=run(width,sqrt(3.))
  ratio=on['post_pulse_energy']/off['post_pulse_energy']
  print(dict(width=width,on_shell_energy=on['post_pulse_energy'],off_shell_energy=off['post_pulse_energy'],ratio=ratio,max_error=max(on['ode_error'],off['ode_error'])),flush=True)
  rows.append(ratio)
 assert all(rows[i+1]>rows[i] for i in range(3))
 print('PASS finite-duration source leaves free EM oscillations and favors phase matching')
 print('OPEN true localized self-consistent H2+TT packet and full stress exchange')
