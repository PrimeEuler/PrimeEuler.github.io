#!/usr/bin/env python3
"""v15.1392: transverse Maxwell mode sourced by finite-periodic-energy
free H2/TT packets. Work-energy identity with externally prescribed
source only; no sigma/TT energy loss or total conservation demonstrated.
"""
import numpy as np
from scipy.integrate import solve_ivp,simpson
from scipy.interpolate import CubicSpline
from k4_quarter_h2_finite_packet_v15_1391 import trial
def run(N=16,g=.05):
 ts=np.linspace(-.8,.8,17);js=[];rows=[]
 for t in ts:
  row,current=trial(N=N,t=float(t),quiet=True,output_vector=True)
  js.append(current);rows.append(row)
 js=np.array(js)
 d=np.array([.5,.5,-1/np.sqrt(2)])
 assert np.max(abs(js@d))<1e-14
 spline=CubicSpline(ts,js,axis=0)
 def force(t):return g*spline(t)
 def ode(t,Y):return np.r_[Y[3:],-Y[:3]-force(t)]
 sol=solve_ivp(ode,(ts[0],ts[-1]),np.zeros(6,complex),method='DOP853',
               rtol=2e-12,atol=1e-19,dense_output=True)
 assert sol.success
 sample=np.linspace(ts[0],ts[-1],1281)
 state=sol.sol(sample);A=state[:3];V=state[3:]
 energy=.5*(sum(abs(V[:,-1])**2)+sum(abs(A[:,-1])**2))
 work=-simpson(np.real(np.sum(np.conj(V)*np.array([force(t) for t in sample]).T,axis=0)),x=sample)
 relative=abs(energy-work)/max(energy,1e-30)
 assert relative<5e-6,(energy,work,relative)
 assert np.linalg.norm(A[:,-1])>0 and np.linalg.norm(d@A)<1e-13
 row=dict(N=N,g=g,final_mode_energy=float(energy),
          integrated_external_work=float(work),work_relative_residual=float(relative),
          max_source_ward=max(r['ward_max'] for r in rows))
 print(row,flush=True)
 return row
if __name__=='__main__':
 a=run(N=12);b=run(N=16);c=run(N=16,g=.025)
 assert abs(b['final_mode_energy']/c['final_mode_energy']-4)<1e-7
 print('PASS finite-packet-source transverse Maxwell energy/work identity')
 print('OPEN coupled sigma/TT energy debit, Einstein stress and radiation detector')
