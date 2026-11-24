#!/usr/bin/env python3
"""Gravity v15.1385: leading fixed-background Weyl-H2 -> transverse Maxwell response.
Analytic TT metric and two free on-shell sigma waves; full nonlinear coupled
Einstein/Maxwell/sigma equations NOT solved. g_eff is freely selected.
"""
import sympy as s
import numpy as np
from math import sqrt
from scipy.integrate import quad,solve_ivp
t,x,y,z=s.symbols("t x y z",real=True);c=(t,x,y,z);sg=(-1,1,1,1)
p=s.MutableDenseMatrix(4,4,[0]*16)
p[1,1]=s.cos(t-z);p[2,2]=-p[1,1]
R={}
for i in range(4):
 for j in range(4):
  for a in range(4):
   for b in range(4):
    q=(s.diff(p[i,b],c[a],c[j])+s.diff(p[j,a],c[b],c[i])-s.diff(p[i,a],c[b],c[j])-s.diff(p[j,b],c[a],c[i]))/2
    if q!=0:R[i,j,a,b]=s.trigsimp(q)
u=s.sin(t-x);v=s.sin(t-y)
B={(a,b):s.diff(u,c[a])*s.diff(v,c[b])-s.diff(u,c[b])*s.diff(v,c[a]) for a in range(4) for b in range(4)}
K={(i,j):s.trigsimp(sum(R.get((i,j,a,b),0)*sg[a]*sg[b]*B[a,b] for a in range(4) for b in range(4))) for i in range(4) for j in range(4)}
J=[s.trigsimp(-sum(sg[a]*sg[j]*s.diff(K[a,j],c[a]) for a in range(4))) for j in range(4)]
f=s.sin(2*t-x-y)*s.cos(t-z)
assert all(s.trigsimp(s.expand_trig(j-f))==0 for j in J)
assert s.trigsimp(sum(s.diff(J[i],c[i]) for i in range(4)))==0
assert s.trigsimp(f-(s.sin(3*t-x-y-z)+s.sin(t-x-y+z))/2)==0
q0=np.array([1.,1.,1.]);q1=np.array([1.,1.,-1.]);j=np.ones(3)
project=lambda q:j-q*(q@j)/(q@q)
assert np.linalg.norm(project(q0))<1e-14
assert np.linalg.norm(project(q1)-[2/3,2/3,4/3])<1e-14
def response(time,g_eff=.02):
 q=q1;omega=1.;k2=q@q;kn=sqrt(k2)
 J0=1j*g_eff*project(q)/4
 A=-J0/(k2-omega**2)*(np.exp(-1j*omega*time)-np.cos(kn*time)+1j*omega/kn*np.sin(kn*time))
 Ad=-J0/(k2-omega**2)*(-1j*omega*np.exp(-1j*omega*time)+kn*np.sin(kn*time)+1j*omega*np.cos(kn*time))
 def green(i):
  fun=lambda s:-np.sin(kn*(time-s))/kn*J0[i]*np.exp(-1j*omega*s)
  return quad(lambda s:fun(s).real,0,time,epsabs=2e-13)[0]+1j*quad(lambda s:fun(s).imag,0,time,epsabs=2e-13)[0]
 Ai=np.array([green(i) for i in range(3)])
 def rhs(tt,state):return np.r_[state[3:],-k2*state[:3]-J0*np.exp(-1j*omega*tt)]
 sol=solve_ivp(rhs,(0,time),np.zeros(6,complex),rtol=2e-12,atol=1e-14)
 assert sol.success
 errG=float(max(abs(A-Ai)));errO=float(max(abs(A-sol.y[:3,-1])))
 energy=float((np.vdot(Ad,Ad)+k2*np.vdot(A,A)).real/2)
 assert max(errG,errO)<2e-11 and abs(q@A)<2e-15
 return dict(time=time,g_eff=g_eff,mode_amplitude=float(np.linalg.norm(A)),mode_energy=energy,
             green_error=errG,ode_error=errO)
if __name__=="__main__":
 print("PASS exact source conservation and q=(1,1,1) longitudinal null; q=(1,1,-1) transverse nonzero")
 for time in (.3,.7,1.1):print(response(time))
 a=response(.7,.02);b=response(.7,.01);c=response(.7,0.)
 assert abs(a["mode_amplitude"]/b["mode_amplitude"]-2)<1e-12
 assert abs(a["mode_energy"]/b["mode_energy"]-4)<1e-11
 assert c["mode_amplitude"]<1e-14 and c["mode_energy"]<1e-14
 print("PASS analytic retarded Green/ODE sourced transverse EM response")
 print("NEGATIVE arbitrary g_eff and target normalization; no Cone-only force")
 print("OPEN sigma/Maxwell/Einstein coupled backreaction and detector readout")
