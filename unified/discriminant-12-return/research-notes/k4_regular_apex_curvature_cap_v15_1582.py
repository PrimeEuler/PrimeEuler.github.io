import numpy as np
from scipy.integrate import solve_ivp, simpson
from scipy.optimize import minimize_scalar

def cap(t,k):
    z=k*t
    if z<1e-4: return z*z/3
    return np.log(np.sinh(z)/np.sin(z))
def bound(eta,delta):
    k=np.sqrt(eta); total=cap(1,k); d=delta/(1+delta); sinc=np.sin(k)/k
    def f(a): return cap(a,k)+total-cap(1-a,k)+np.sqrt(8*d/sinc*np.log((1-a)/a))
    res=minimize_scalar(f,bounds=(1e-9,.499999999),method='bounded',options={'xatol':1e-12})
    return min(total,res.fun)
worst=np.zeros(3); count=0
for eta in (.1,.3,.6,1.):
 for omega in (0.,1.,3.,6.):
  for profile in (0,1,2):
   def R(t):
    p=2*omega*t; amp=eta*[1.,t,np.sin(np.pi*t)**2][profile]
    return amp*np.array([[np.cos(p),np.sin(p)],[np.sin(p),-np.cos(p)]])
   def rhs(t,y):
    D,V=y.reshape(2,2,2); return np.stack((V,-R(t)@D)).ravel()
   t=np.linspace(0,1,2001); s=solve_ivp(rhs,(0,1),np.stack((np.zeros((2,2)),np.eye(2))).ravel(),t_eval=t,rtol=2e-12,atol=2e-14)
   D,V=s.y.T.reshape(-1,2,2,2).transpose(1,0,2,3); B=V[1:]@np.linalg.inv(D[1:]); ev=np.linalg.eigvalsh(B); w=np.r_[0,ev[:,1]-ev[:,0]]
   k=np.sqrt(eta); lo=k/np.tan(k*t[1:]); hi=k/np.tanh(k*t[1:]); rho=np.sqrt(np.maximum(0,np.linalg.det(D))); L=simpson(w,x=t); delta=1/rho[-1]-1
   psi=np.arctan2(D[-1,1,0]-D[-1,0,1],np.trace(D[-1])); lmax=bound(eta,max(0,delta)); pmax=np.log(np.cosh(lmax/2))
   worst=np.maximum(worst,[max(np.max(lo-ev[:,0]),np.max(ev[:,1]-hi)),L-lmax,abs(psi)-pmax]);count+=1
   assert np.min(rho[1:])>0 and L<=lmax+1e-8 and abs(psi)<=pmax+1e-8
   assert np.max(lo-ev[:,0])<1e-8 and np.max(ev[:,1]-hi)<1e-8
   if omega==3 and profile==0: print(eta,delta,L,psi,lmax,pmax)
print('PASS',count,'max positive violations',worst)
