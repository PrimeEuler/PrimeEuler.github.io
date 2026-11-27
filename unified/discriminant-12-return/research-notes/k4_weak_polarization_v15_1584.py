import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy.integrate import solve_ivp

def matrices(n):
    # midpoint quadrature within each control cell, exact Volterra moments
    t=(np.arange(4*n)+.5)/(4*n); a=np.arange(n)/n; b=np.minimum(t[:,None],(np.arange(n)+1)/n); b=np.maximum(b,a)
    M2=(b**3-a**3)/3; M1=(b**2-a**2)/2
    A=-2*(M1-M2/t[:,None]); B=-2*M2/t[:,None]**2
    K=(A.T@B-B.T@A)/(8*len(t)); H=B.T@((t*(1-t))[:,None]*B)/(4*len(t))
    return K,H

def values(z,K,H):return float(np.imag(np.vdot(z,K@z))),float(np.real(np.vdot(z,H@z)))

def optimize(n,budget):
    K,H=matrices(n); t=(np.arange(n)+.5)/n
    def fg(x):
        z=np.exp(1j*x); p,d=values(z,K,H)
        gp=2*np.real(np.conj(1j*z)*(-1j*K@z)); gd=2*np.real(np.conj(1j*z)*(H@z))
        if d>budget: return -p*budget/d,-budget*(gp*d-p*gd)/d**2
        return -p,-gp
    best=None
    for f in (2,5,8,12,18):
        r=minimize(fg,f*t,jac=True,method='L-BFGS-B',options={'maxiter':1000,'ftol':1e-14,'gtol':1e-9})
        if best is None or r.fun<best.fun:best=r
    z=np.exp(1j*best.x); p,d=values(z,K,H); z*=min(1,np.sqrt(budget/d)); p,d=values(z,K,H)
    def steady(f):
        p,d=values(np.exp(1j*f*t),K,H);return p*min(1,budget/d)
    rr=minimize_scalar(lambda f:-steady(f),bounds=(0,16),method='bounded')
    print(n,budget,'candidate',p,d,'steady',-rr.fun,'rate',rr.x,'success',best.success,flush=True)
    return z,p,d

def replay(z,eta):
    n=len(z); y=np.r_[np.zeros(4),np.eye(2).ravel()]
    for i,e in enumerate(z):
        R=eta*np.array([[e.real,e.imag],[e.imag,-e.real]])
        def rhs(t,y):return np.r_[y[4:],(-R@y[:4].reshape(2,2)).ravel()]
        y=solve_ivp(rhs,(i/n,(i+1)/n),y,rtol=1e-11,atol=1e-13).y[:,-1]
    D=y[:4].reshape(2,2); return np.arctan2(D[1,0]-D[0,1],np.trace(D))/eta**2,(1-np.sqrt(np.linalg.det(D)))/eta**2
if __name__=='__main__':
    for n in (16,32,64):
        z,p,d=optimize(n,.003)
    for eta in (.2,.1,.05):print('replay',eta,replay(z,eta),'leading',p,d,flush=True)
