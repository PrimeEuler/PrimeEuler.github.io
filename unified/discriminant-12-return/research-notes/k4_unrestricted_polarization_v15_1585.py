import numpy as np
from scipy.optimize import minimize, brentq
from scipy.integrate import solve_ivp

def matrices(n,q=8):
    t=(np.arange(q*n)+.5)/(q*n); a=np.arange(n)/n
    b=np.maximum(a,np.minimum(t[:,None],(np.arange(n)+1)/n))
    M2=(b**3-a**3)/3; M1=(b**2-a**2)/2
    A=-2*(M1-M2/t[:,None]); B=-2*M2/t[:,None]**2
    return -1j*(A.T@B-B.T@A)/(8*len(t)), B.T@((t*(1-t))[:,None]*B)/(4*len(t))

def run(n,budget):
    K,H=matrices(n); t=(np.arange(n)+.5)/n; scale=1000
    def unpack(x):return x[:n]+1j*x[n:]
    def val(x,M):
        z=unpack(x); w=M@z
        return np.vdot(z,w).real,np.r_[2*w.real,2*w.imag]
    def obj(x):
        p,g=val(x,K); return -scale*p,-scale*g
    def con(x):return np.r_[1-abs(unpack(x))**2,scale*(budget-val(x,H)[0])]
    def jac(x):return np.vstack([np.c_[-2*np.diag(x[:n]),-2*np.diag(x[n:])],-scale*val(x,H)[1]])
    best=None
    for f in (2,5,9,15):
        z=np.exp(1j*f*t); z*=min(1,np.sqrt(budget/np.vdot(z,H@z).real)); x=np.r_[z.real,z.imag]
        r=minimize(obj,x,jac=True,constraints={'type':'ineq','fun':con,'jac':jac},method='SLSQP',options={'ftol':1e-11,'maxiter':500})
        if min(con(r.x))>=-1e-8 and (best is None or r.fun<best.fun):best=r
    z=unpack(best.x); p=val(best.x,K)[0]; h=val(best.x,H)[0]
    angle=np.diff(np.unwrap(np.angle(z))[[0,-1]])[0]*90/np.pi
    print(n,budget,p,h,angle,abs(z).min(),best.success,flush=True)
    return z

def certificate(z,budget):
    n=len(z); K,H=matrices(n); a=abs(z); free=a<1-1e-5
    w=K@z; v=H@z
    lam=np.vdot(v[free],w[free]).real/np.vdot(v[free],v[free]).real
    mu=np.maximum(0,np.real(np.conj(z)*(w-lam*v))); mu[free]=0
    S=lam*H+np.diag(mu)-K
    eig=np.linalg.eigvalsh(S)[0]; shift=max(0,-eig); upper=lam*budget+sum(mu)+n*shift
    print('dual',n,lam,eig,upper,'gap',upper-np.vdot(z,w).real,'res',np.max(abs(S@z)),flush=True)
    print('samples',[(round((i+.5)/n,3),round(a[i],5),round((np.unwrap(np.angle(z))[i]-np.angle(z[0]))*90/np.pi,4)) for i in np.linspace(0,n-1,9).astype(int)],flush=True)

def replay(z,eta):
    y=np.r_[np.zeros(4),np.eye(2).ravel()]; n=len(z)
    for j,e in enumerate(z):
        R=eta*np.array([[e.real,e.imag],[e.imag,-e.real]])
        def rhs(t,y):return np.r_[y[4:],(-R@y[:4].reshape(2,2)).ravel()]
        y=solve_ivp(rhs,(j/n,(j+1)/n),y,rtol=1e-11,atol=1e-13).y[:,-1]
    D=y[:4].reshape(2,2)
    return np.arctan2(D[1,0]-D[0,1],np.trace(D))/eta**2,(1-np.sqrt(np.linalg.det(D)))/eta**2

if __name__=='__main__':
    for b in (.001,.002,.003,.004,.005):run(32,b)
    for n in (32,64,128):
        z=run(n,.003); certificate(z,.003)
    for eta in (.2,.1,.05):
        p,d=replay(z,eta)
        a=1 if d<=.003 else brentq(lambda a:replay(a*z,eta)[1]-.003,.99,1)-1e-8
        print('nonlinear',eta,p,d,a,replay(a*z,eta),flush=True)
