import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
I=np.eye(2); Z=np.zeros((2,2)); J=np.block([[Z,I],[-I,Z]])
def R(theta,k):return k*np.array([[np.cos(2*theta),np.sin(2*theta)],[np.sin(2*theta),-np.cos(2*theta)]])
def L(r):return np.block([[Z,I],[-r,Z]])
def angle(d):return np.arctan2(d[1,0]-d[0,1],np.trace(d))
worst=np.zeros(4); count=0
for k in (.25,.5,1.,2.):
 for theta in (.2,np.pi/8,np.pi/4):
  a,b=R(0,k),R(theta,k)
  for h in (.1,.3,.5):
   sa,sb=expm(h*L(a)),expm(h*L(b)); s=sb@sa; d=s[:2,2:]; v=s[2:,2:]; rev=(sa@sb)[:2,2:]
   optical=v@np.linalg.inv(d)
   init=np.vstack([Z,I]).ravel()
   for r in (a,b):init=solve_ivp(lambda t,y:(L(r)@y.reshape(4,2)).ravel(),(0,h),init,rtol=1e-12,atol=1e-14).y[:,-1]
   worst=np.maximum(worst,[np.max(abs(d-rev.T)),np.max(abs(optical-optical.T)),np.max(abs(s.T@J@s-J)),np.max(abs(init.reshape(4,2)-s[:,2:]))]);count+=1
   assert np.linalg.det(d)>0
assert max(worst)<1e-10
print(count,worst)
a,b=R(0,1),R(np.pi/4,1)
for h in (.05,.1,.2,.5):
 d=(expm(h*L(b))@expm(h*L(a)))[:2,2:]; pred=h**4*(b@a-a@b)[1,0]/24
 print(h,angle(d),pred,angle(d)/pred,np.linalg.det(d))
