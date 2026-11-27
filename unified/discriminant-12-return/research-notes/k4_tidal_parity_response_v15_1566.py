import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
N=80
a=np.diag(np.sqrt(np.arange(1,N)),1); ad=a.T
Q=(a+ad)/np.sqrt(2); P=(a-ad)/(1j*np.sqrt(2)); occ=np.arange(N)
worst=0.; ratioerr=0.; count=0
for eps in (-.75,-.3,-.05,.05,.3,.75):
 for t in (.3,1.,2.):
  U=expm(-1j*t*(P@P+(1+eps)*Q@Q)/2)
  w=np.sqrt(1+eps)
  beta2=eps**2*np.sin(w*t)**2/(4*w*w)
  vals=[np.dot(occ,abs(U[:,k])**2)-k for k in (0,1)]
  worst=max(worst,abs(vals[0]-beta2),abs(vals[1]-3*beta2))
  ratioerr=max(ratioerr,abs(vals[1]/vals[0]-3))
  count+=1
assert worst<1e-9 and ratioerr<1e-7
print('constant pulse cases',count,'max occupation error',worst,'ratio error',ratioerr)
worst=0.;count=0
for strength in (.03,.15,.4):
 for drive in (1.,2.,2.4):
  def eps(t):return strength*np.sin(drive*t)
  T=3.
  def rhs(t,s):return (np.array([[0,1],[-1-eps(t),0]])@s.reshape(2,2)).ravel()
  S=solve_ivp(rhs,(0,T),np.eye(2).ravel(),rtol=1e-11,atol=1e-13).y[:,-1].reshape(2,2)
  beta2=(np.sum(S*S)-2)/4
  # independent Schrodinger evolution of both columns, smaller cutoff adequate
  n=36; q=Q[:n,:n]; h0=np.diag(np.arange(n)+.5); v=q@q/2
  def qr(t,z):return (-1j*(h0+eps(t)*v)@z.reshape(n,2)).ravel()
  y=solve_ivp(qr,(0,T),np.eye(n,dtype=complex)[:,:2].ravel(),rtol=1e-10,atol=1e-12).y[:,-1].reshape(n,2)
  vals=np.arange(n)@abs(y)**2-np.arange(2)
  worst=max(worst,np.max(abs(vals-beta2*np.array([1,3]))));count+=1
assert worst<1e-7
print('time varying cases',count,'max occupation error',worst)
# Linear force negative control: displacement adds same occupation for each input.
for f in (.1,.4,1.):
 U=expm(-1j*(np.diag(occ+.5)-f*Q))
 vals=occ@abs(U[:,:2])**2-np.arange(2)
 assert np.max(abs(vals-f*f*(1-np.cos(1))))<1e-10
print('linear control PASS 3 cases')
