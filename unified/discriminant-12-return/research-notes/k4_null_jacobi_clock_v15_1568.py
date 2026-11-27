import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.linalg import expm
J=np.block([[np.zeros((2,2)),np.eye(2)],[-np.eye(2),np.zeros((2,2))]])
worst=np.zeros(4)
for k in (.1,.5,1,2):
 for theta in (0,.3,.8):
  O=np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
  R=O@np.diag([k,-k])@O.T
  L=np.block([[np.zeros((2,2)),np.eye(2)],[-R,np.zeros((2,2))]])
  for u in (.2,.5,1):
   S=expm(u*L); D=S[:2,2:]; V=S[2:,2:]; B=V@np.linalg.inv(D); rho=np.sqrt(np.linalg.det(D)); rp=rho*np.trace(B)/2
   shear=B-np.trace(B)*np.eye(2)/2
   f=np.sqrt(k); d=np.array([np.sin(f*u),np.sinh(f*u)])/f
   M=D.T@D/rho**2
   Mp=(V.T@D+D.T@V)/rho**2-2*rp/rho*M
   speed=np.trace(np.linalg.solve(M,Mp)@np.linalg.solve(M,Mp))/2
   rpp=rho*((np.trace(B)/2)**2-np.trace(R+B@B)/2)
   errs=[np.max(abs(S.T@J@S-J)),np.max(abs(D-O@np.diag(d)@O.T)),abs(speed-2*np.trace(shear@shear)),abs(rpp+rho*np.trace(shear@shear)/2)]
   worst=np.maximum(worst,errs)
assert max(worst)<1e-10
print('36 cases; symplectic, Jacobi, metric, focusing errors',worst)
for k in (.1,.5,1,2):
 f=np.sqrt(k)
 def rho(u):return np.sqrt(np.sin(f*u)*np.sinh(f*u))/f
 def rp(u):return rho(u)*f*(1/np.tan(f*u)+1/np.tanh(f*u))/2
 def delta(u):return f*(1/np.tan(f*u)-1/np.tanh(f*u))/2
 a,b=.1,1.
 def Xi(u):return quad(lambda x:rho(x)*delta(x)**2/rp(x),a,u,epsabs=1e-12)[0]
 clock=quad(lambda u:np.exp(Xi(u))*rp(u)/rp(a),a,b,epsabs=1e-12)[0]
 assert abs(clock-(b-a))<1e-10
 print(k,'clock',clock,'rho',rho(b),'Xi',Xi(b),'delay ratio',(b-a)*rp(a)/(rho(b)-rho(a)))
