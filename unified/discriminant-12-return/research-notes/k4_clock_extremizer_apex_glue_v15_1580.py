import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import expit
I=np.eye(2)
for e,d in [(.1,.05),(.1,.2),(.3,.05),(.5,.01),(.5,.2)]:
 C=(1-e)*(1+d)
 def K(c):return (C*e/c-1+C*C/c)/C
 def j(x,c):return 1+K(c)*x-x*x/c
 c=brentq(lambda c:np.log(e)+quad(lambda x:x/(c*j(x,c)),0,C)[0],1e-8,100,xtol=1e-14)
 k=K(c); xp=(c*k+np.hypot(c*k,2*np.sqrt(c)))/2
 L=quad(lambda x:2/(np.sqrt(c)*j(x,c)),0,C)[0]; g=np.hypot(np.pi,L)/L
 eta=min((xp-C)/4,e/4)
 def a(u):return 2/(np.sqrt(c)*j(C-u,c))
 def shape(u):
  l=quad(a,0,u,epsabs=1e-13)[0]
  if u>=-eta/2:return l,a(u)
  if u<=-eta:return 0.,0.
  z=2*(u+eta)/eta
  chi=expit(1/(1-z)-1/z)
  chip=chi*(1-chi)*(1/(1-z)**2+1/z**2)*2/eta
  return chi*l,chi*a(u)+chip*l
 def rhs(u,y):
  v,vp=y[:2]; D=y[2:].reshape(2,2); l,w=shape(u); phi=np.pi/2-g*l
  N=np.array([[np.cos(phi),np.sin(phi)],[np.sin(phi),-np.cos(phi)]])
  B=vp/v*I+w*N/2
  return np.r_[vp,-v*w*w/4,(B@D).ravel()]
 sol=solve_ivp(rhs,(0,-eta),np.r_[e,1,(e*I).ravel()],rtol=2e-12,atol=2e-14,max_step=eta/100)
 assert sol.success and np.min(sol.y[0])>0
 v,vp=sol.y[:2,-1]; D=sol.y[2:,-1].reshape(2,2)
 err=np.max(abs(D-v*I)); assert err<1e-9 and vp>1
 apex=-eta-v/vp
 print(f'{e} {d} eta={eta:.10g} vertex_slope={vp:.10g} apex={apex:.10g} matching_error={err:.3g}')
