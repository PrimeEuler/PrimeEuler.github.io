import numpy as np
from scipy.linalg import expm
from k4_unrestricted_polarization_v15_1585 import run
T=np.array([[[1.,0],[0,-1]],[[0,1],[1,0]]])
def test(z,eta):
 n=len(z); I=np.eye(2); Z=np.zeros((2,2)); A=[np.block([[Z,I],[-eta*(e.real*T[0]+e.imag*T[1]),Z]]) for e in z]; X=[np.eye(4)]
 for a in A:X.append(expm(a/n)@X[-1])
 D=X[-1][:2,2:]; x=np.trace(D); y=D[1,0]-D[0,1]; psi=np.arctan2(y,x)
 def grad(W):return (x*(W[1,0]-W[0,1])-y*np.trace(W))/(x*x+y*y)
 def deficit(W):return -.5*np.sqrt(np.linalg.det(D))*np.trace(np.linalg.solve(D,W))
 g0=np.array([grad(-eta*D@t) for t in T]); g1=np.array([grad(-eta*t@D) for t in T]); rot=np.exp(2j*psi); c=lambda v:complex(*v)
 assert abs(c(g1)+rot*c(g0))<1e-14
 print('eta, psi_deg, predicted_axis_deg',eta,np.degrees(psi),90+np.degrees(psi),'endpoint_norm',np.linalg.norm(g0),'covariance_error',abs(c(g1)+rot*c(g0)))
 for eps in (1e-3,1e-5,1e-7):
  out=[]
  for s,dist,target in [(eps,eps,g0),(1-eps,eps,g1)]:
   j=min(int(s*n),n-1); F=expm(A[j]*(s-j/n))@X[j]; B=(X[-1]@np.linalg.inv(F))[:2,2:]; Ds=F[:2,2:]; W=[-eta*B@t@Ds for t in T]; g=np.array([grad(w) for w in W]); d=np.array([deficit(w) for w in W]); out.append((np.linalg.norm(g/dist-target)/np.linalg.norm(target),np.linalg.norm(d/dist)))
  print('eps',eps,'relative_rotation_errors_and_scaled_deficit',out)
if __name__=='__main__':
 z=run(32,.003)
 for eta in (.05,.2,.5,1.):test(z,eta)
