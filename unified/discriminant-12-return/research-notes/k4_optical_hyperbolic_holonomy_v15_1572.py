import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad
I=np.eye(2); Z=np.zeros((2,2))
def R(k,t):return k*np.array([[np.cos(2*t),np.sin(2*t)],[np.sin(2*t),-np.cos(2*t)]])
def L(r):return np.block([[Z,I],[-r,Z]])
def calc(S):
 D=S[:2,2:]; V=S[2:,2:]; det=np.linalg.det(D); q=D.T@D/det
 qp=(V.T@D+D.T@V)/det-q*np.trace(np.linalg.solve(D,V))
 X=(q[0,0]-q[1,1])/2; Y=q[0,1]; T=np.trace(q)/2
 xp=(qp[0,0]-qp[1,1])/2; yp=qp[0,1]
 return (X*yp-Y*xp)/(2*(T+1))
worst=0; count=0
for k in (.25,.5,1,2):
 for theta in (.2,np.pi/8,np.pi/4):
  for h in (.1,.3,.5):
   a,b=L(R(k,0)),L(R(k,theta)); sa=expm(h*a); s=expm(h*b)@sa; d=s[:2,2:]
   psi=np.arctan2(d[1,0]-d[0,1],np.trace(d))
   val=quad(lambda t:calc(expm(t*b)@sa),0,h,epsabs=1e-13)[0]
   worst=max(worst,abs(psi-val)); count+=1
   assert abs(psi-val)<1e-11
print(count,worst)
