import numpy as np
from scipy.optimize import minimize
from scipy.special import exprel
from numpy.polynomial.legendre import leggauss

def solve(e,delta,n):
    v=1-(1-e)*(1-np.arange(n+1)/n)**2
    l=np.log(v[1:]/v[:-1]); dv=np.diff(v)
    g,gw=leggauss(12); nodes=v[:-1,None]+dv[:,None]*(g+1)/2
    a=np.log(nodes/v[:-1,None])/l[:,None]; weights=dv[:,None]*gw/2
    C=(1-e)*(1+delta)
    def clock(z):
        x=np.cumsum(z)-z
        f=weights*np.exp(x[:,None]+z[:,None]*a)
        cell=f.sum(axis=1)
        grad=np.cumsum(cell[::-1])[::-1]-cell+(f*a).sum(axis=1)
        return cell.sum(),grad
    def length(z):return 2*np.sqrt(l*z).sum()
    def grad(z):return np.sqrt(l/z)
    # positive increments; clock constraint convex and objective strictly concave
    z0=delta*l/l.sum()
    res=minimize(lambda z:-length(z),z0,jac=lambda z:-grad(z),bounds=[(1e-14,None)]*n,
       constraints=[{'type':'ineq','fun':lambda z:C-clock(z)[0],'jac':lambda z:-clock(z)[1]}],method='SLSQP',options={'ftol':2e-12,'maxiter':400})
    z=res.x; c,cg=clock(z); L=length(z)
    # Global upper bound within this discretization via supporting hyperplanes
    lam=np.dot(grad(z),cg)/np.dot(cg,cg)
    # Unrestricted continuum dual bound from frozen F, using convexity of exp and exact Cauchy-Schwarz.
    # For candidate clock profile Xi, C(y)>= C(z)+ integral F_z(v)*(y-y_z)dv.
    # L^2 <=4 * (C-C(z)+integral F_z*y_z) * integral 1/(v*F_z) dv,
    # which diverges at v=1 for bounded Xi_z; not used as certificate.
    assert abs(c-C)<2e-8, (res.message,c,C)
    return L,(np.hypot(np.pi,L)-np.pi)/2,z.sum(),z[-1],np.max(abs(grad(z)/cg/lam-1)),res.success
if __name__=='__main__':
 for e,d in [(.1,.05),(.1,.2),(.3,.05)]:
  for n in (16,32,64,128):
   print(e,d,n,solve(e,d,n),flush=True)

from scipy.integrate import solve_ivp
from scipy.optimize import brentq

def continuum(e,d,zmax=32,rtol=2e-11):
    C=(1-e)*(1+d)
    def run(c):
        def rhs(z,Y):
            v,W,L,clock=Y; q=np.exp(-z)
            return [C*q*q/W,-W+c/(v*C),2*np.sqrt(c)*q/(v*W),C*q]
        return solve_ivp(rhs,(0,zmax),[e,1,0,0],rtol=rtol,atol=rtol/100)
    hi=1.
    while run(hi).y[0,-1]>1:hi*=2
    c=brentq(lambda c:run(c).y[0,-1]-1,1e-12,hi,xtol=1e-13)
    v,W,L,clock=run(c).y[:,-1]
    assert abs(v-1)<1e-9 and abs(clock-C)<1e-9
    assert abs(W-c/C)<1e-8
    return c,L,(np.hypot(np.pi,L)-np.pi)/2
if __name__=='__main__':
 for e,d in [(.1,.05),(.1,.2),(.3,.05),(.5,.01),(.5,.2)]:
  a=continuum(e,d,24,2e-10); b=continuum(e,d,32,2e-12)
  assert np.max(abs(np.array(a)-b))<1e-7
  print('continuum',e,d,*b,'refinement',np.max(abs(np.array(a)-b)))
