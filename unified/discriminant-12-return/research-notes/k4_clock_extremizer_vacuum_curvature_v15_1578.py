import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

def run(e,d):
 C=(1-e)*(1+d)
 def K(c): return (C*e/c-1+C*C/c)/C
 def j(x,c): return 1+K(c)*x-x*x/c
 def residual(c): return np.log(e)+quad(lambda x:x/(c*j(x,c)),0,C,epsabs=1e-11)[0]
 c=brentq(residual,1e-8,100,xtol=1e-14)
 L=quad(lambda x:2/(np.sqrt(c)*j(x,c)),0,C,epsabs=1e-11)[0]
 R0=np.arcsinh(L/np.pi); g=1/np.tanh(R0); kk=K(c)
 def mat(phi):return np.array([[np.cos(phi),np.sin(phi)],[np.sin(phi),-np.cos(phi)]])
 def quantities(u,l):
  x=C-u; J=j(x,c); a=2/(np.sqrt(c)*J); b=x/(c*J); phi=np.pi/2-g*l
  N=mat(phi); M=mat(phi+np.pi/2)
  B=b*np.eye(2)+a*N/2
  R=(-kk/np.sqrt(c)*N+2*g/c*M)/J**2
  return a,b,B,R
 def rhs(u,y):
  l=y[0]; D=y[1:].reshape(2,2); a,b,B,R=quantities(u,l)
  return np.r_[a,(B@D).ravel()]
 t=np.linspace(0,C,201)
 sol=solve_ivp(rhs,(0,C),np.r_[0,(e*np.eye(2)).ravel()],t_eval=t,rtol=2e-11,atol=2e-13)
 def rhs2(u,y):
  l=y[0]; D=y[1:5].reshape(2,2); V=y[5:].reshape(2,2); a,b,B,R=quantities(u,l)
  return np.r_[a,V.ravel(),(-R@D).ravel()]
 D0=e*np.eye(2); V0=quantities(0,0)[2]@D0
 s2=solve_ivp(rhs2,(0,C),np.r_[0,D0.ravel(),V0.ravel()],t_eval=t,rtol=2e-11,atol=2e-13)
 err=0.; trace=0.; detmin=1.
 for u,y in zip(t,sol.y.T):
  l=y[0]; D=y[1:].reshape(2,2); q=D.T@D/np.linalg.det(D); angle=l/np.sinh(R0); ch=np.cosh(R0); sh=np.sinh(R0)
  T=ch*ch-sh*sh*np.cos(angle); X=ch*sh*(1-np.cos(angle)); Y=sh*np.sin(angle)
  qref=np.array([[T+X,Y],[Y,T-X]])
  err=max(err,np.max(abs(q-qref))); trace=max(trace,abs(np.trace(quantities(u,l)[3]))); detmin=min(detmin,np.linalg.det(D))
 D=sol.y[1:,-1].reshape(2,2); psi=np.arctan2(D[1,0]-D[0,1],np.trace(D)); expected=-np.pi*(np.cosh(R0)-1)/2 # path goes clockwise around center
 ode=np.max(abs(sol.y[1:]-s2.y[1:5])); end=abs(np.linalg.det(D)-1)
 assert err<1e-8 and ode<1e-8 and end<1e-8 and abs(psi-expected)<1e-8 and trace<1e-12
 print(f'e={e} d={d} c={c:.12g} L={L:.12g} K={kk:.12g} endpoint_R={np.linalg.norm(quantities(C,L)[3],2):.9g} q_err={err:.3g} ode_err={ode:.3g} det_err={end:.3g} psi={psi:.9g} min_det={detmin:.5g}')
for e,d in [(.1,.05),(.1,.2),(.3,.05),(.5,.01),(.5,.2)]:run(e,d)
