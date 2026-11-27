import sympy as s
import numpy as np
T,X,Y,a,b,c,d,p,q=s.symbols('T X Y a b c d p q',real=True)
S=s.Matrix([[T+X,Y],[Y,T-X]])
assert s.expand(S.det()-(T*T-X*X-Y*Y))==0
A=s.Matrix([[a,b],[c,d]])
assert s.expand((A*S*A.T).det()-A.det()**2*S.det())==0
v=s.Matrix([a,b]); w=s.Matrix([c,d])
assert s.expand((v*v.T+w*w.T).det()-(a*d-b*c)**2)==0
# rotation action on the traceless pair
R=s.Matrix([[s.cos(p),-s.sin(p)],[s.sin(p),s.cos(p)]])
B=R*S*R.T
assert s.trigsimp((B[0,0]-B[1,1])/2-X*s.cos(2*p)+Y*s.sin(2*p))==0
assert s.trigsimp(B[0,1]-X*s.sin(2*p)-Y*s.cos(2*p))==0
# fixed transverse coordinate in one extra spatial dimension
assert s.expand((T*T-X*X-Y*Y-q*q).subs(q,p)-(S.det()-p*p))==0
# rank-one null decomposition; phase controls determinant, not uniquely radius
for h in (.25,.5,2/3,1.):
 for theta in (0,np.pi/6,np.pi/4,np.pi/2):
  v=np.sqrt(2*h)*np.array([1.,0.]); w=np.sqrt(2*h)*np.array([np.cos(theta),np.sin(theta)])
  m=np.outer(v,v)+np.outer(w,w)
  assert np.isclose(np.linalg.det(m),4*h*h*np.sin(theta)**2,atol=1e-14)
print('PASS exact determinant, congruence, double-angle and transverse cut; 16 numerical decomposition checks')
