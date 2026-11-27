import numpy as np
from scipy.optimize import least_squares
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import CubicSpline
from k4_switching_v15_1594 import test

def solve(n,seed=None):
 xg,wg=leggauss(5); u=np.linspace(0,1,n+1)
 def calc(x,detail=False):
  c,A,lam=x[-3:]; ph=np.r_[-np.pi/2,x[:-3]]; spl=CubicSpline(u,ph)
  edges=np.r_[c*u,.5,1-c*u[::-1]]
  lo,hi=edges[:-1],edges[1:]; t=(lo[:,None]+(hi-lo)[:,None]*(xg+1)/2).ravel(); w=((hi-lo)[:,None]*wg/2).ravel()
  def E(t):
   v=np.minimum(t,1-t); z=np.empty(len(t),complex); outer=v<c; z[outer]=np.exp(1j*spl(v[outer]/c)); z[~outer]=A/(16*(v[~outer]*(1-v[~outer]))**2)*np.exp(1j*np.log(v[~outer]/(1-v[~outer]))/lam); return np.where(t>.5,z.conj(),z)
  z=E(t)
  def fields(s):
   S=np.asarray(s)[:,None,None]; cuts=np.sort(np.concatenate([np.broadcast_to(edges,(len(s),len(edges))),np.asarray(s)[:,None]],axis=1),axis=1); l0=cuts[:,:-1,None]; h0=cuts[:,1:,None]; R=l0+(h0-l0)*(xg+1)/2; W=(h0-l0)*wg/2; Z=E(R.ravel()).reshape(R.shape); m=np.maximum(S,R); l=np.minimum(S,R); k=l*(m-l)*(1-m)/2*np.sign(R-S); h=l*l*(1-m)**2/2
   return tuple(np.sum(M*W*Z,axis=(1,2)) for M in (-1j*k-lam*h,h,-1j*k))
  s=c*u[1:-1]; F,_,_=fields(s); phase=np.exp(1j*spl(u[1:-1])); f=np.imag(F*phase.conj())/(s*(c-s)**2)
  ff=fields(np.array([c,(c+.5)/2,.5]))[0]; _,hh,qq=fields(t); H=np.vdot(z,w*hh).real; P=np.vdot(z,w*qq).real
  res=np.r_[f,100*(ph[-1]-np.log(c/(1-c))/lam),1e4*ff[0].real,1e4*ff[0].imag,1e4*ff[-1].real,1e4*(H-.003)]
  if detail:
   ss=np.linspace(c*.001,c*.999,500); fs=fields(ss)[0]; zs=E(ss); print(n,c,A,lam,P,H,'res',max(abs(res)),'minmu',min((fs*zs.conj()).real),'freeF',max(abs(fields(np.linspace(c,1-c,101))[0])),'outer imag',max(abs((fs*zs.conj()).imag)),flush=True)
   S=t[:,None]; R=t[None,:]; m=np.maximum(S,R); l=np.minimum(S,R); k=l*(m-l)*(1-m)/2*np.sign(R-S); h=l*l*(1-m)**2/2
   g=fields(t)[0]; mu=np.where(np.minimum(t,1-t)<c,np.maximum(0,(g*z.conj()).real),0); W=np.sqrt(w); dual=np.diag(mu)+(W[:,None]*(lam*h+1j*k))*W[None,:]; eig=np.linalg.eigvalsh(dual)[0]
   print('dual sampled',eig,'unshifted upper',lam*.003+w@mu,'shifted upper',lam*.003+w@mu+max(0,-eig),'edge amplitude',A/(16*(c*(1-c))**2),flush=True)
  return res
 if seed is None:
  z,_=test(32,13); tt=(np.arange(32)+.5)/32; x=np.r_[np.interp(.40625*u[1:],tt,np.angle(z)),.40625,.62545,1.3432]
 else:
  old=seed; x=np.r_[np.interp(u[1:],np.linspace(0,1,len(old)-2),np.r_[-np.pi/2,old[:-3]]),old[-3:]]
 r=least_squares(calc,x,bounds=(np.r_[np.full(n,-3),.37,.5,1.1],np.r_[np.zeros(n),.44,.8,1.6]),xtol=1e-12,ftol=1e-12,gtol=1e-12,max_nfev=150);calc(r.x,True);return r.x

if __name__=='__main__':
 seed=None
 for n in (12,24,48):seed=solve(n,seed)
