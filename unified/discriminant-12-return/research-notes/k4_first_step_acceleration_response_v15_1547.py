import numpy as np
import sympy as s
D,k,d=s.symbols('D k d', real=True)
f=lambda k:k*(D-k)
assert s.expand(f(k+d/2)-(f(k)+f(k+d))/2-d*d/4)==0
for N in range(1,33):
 j=N/2;m=np.arange(N+1)-j
 Z=np.diag(m);P=np.diag(np.sqrt((N-np.arange(N))*(np.arange(N)+1)),-1)
 X=(P+P.T)/2;Y=(P-P.T)/(2j) # 2j Python imaginary literal
 I=np.eye(N+1);T=X@X+Y@Y
 assert np.allclose(T,np.diag(fnum:=(m+j+.5)*(N+1-(m+j+.5))-.25),atol=1e-12)
 assert np.allclose(T[0,0],N/2) and np.allclose(T[-1,-1],N/2)
 assert np.allclose(X@Y-Y@X,1j*Z,atol=1e-12)
 # Distinct diagonal energy gaps are possible despite unchanged transition geometry
 H=Z@Z+.37*Z
 assert np.allclose(H@Z-Z@H,0)
 # Ground-state response of H=-omega Z-a mu X
 for omega,mu in [(1.,1.),(2.,1.),(1.,.5)]:
  eps=1e-3
  em=np.linalg.eigvalsh(-omega*Z+eps*mu*X)[0]
  e0=np.linalg.eigvalsh(-omega*Z)[0]
  ep=np.linalg.eigvalsh(-omega*Z-eps*mu*X)[0]
  chi=-(ep+em-2*e0)/eps**2
  assert abs(chi-j*mu**2/omega)<1e-5
print('PASS 32 spin shells, exact midpoint identity, endpoint transverse moment, 96 response regressions')
for omega,mu in [(1,1),(2,1),(1,.5)]:print('j=1/2, omega, mu, chi:',omega,mu,.5*mu**2/omega)
