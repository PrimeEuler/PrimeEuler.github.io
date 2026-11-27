import numpy as np
from scipy.optimize import root
from scipy.linalg import solve
from numpy.polynomial.legendre import leggauss

def matrices(n,q=4):
    x,w=leggauss(q); a=np.arange(n)/n; h=1/n
    u=a[:,None]+h*(x+1)/2; w=w*h/2
    S=u[:,None,:,None]; R=u[None,:,None,:]; m=np.maximum(S,R); l=np.minimum(S,R)
    k=l*(m-l)*(1-m)/2*np.sign(R-S); d=l*l*(1-m)**2/2
    K=np.einsum('ijab,a,b->ij',k,w,w); H=np.einsum('ijab,a,b->ij',d,w,w)
    r=u; s=a[:,None,None]+(r-a[:,None])[:,:,None]*(x+1)/2
    diag=np.sum(s*s*(1-r[:,:,None])**2/2*w[None,:,None]*(r-a[:,None])[:,:,None]*(w/h)[None,None,:],axis=(1,2))*2
    np.fill_diagonal(H,diag); np.fill_diagonal(K,0)
    return -1j*K,H

def test(n,m,b=.003,seed=None):
    Q,H=matrices(n); t=(np.arange(n)+.5)/n; p=t*(1-t)
    a=np.r_[np.arange(m),np.arange(n-m,n)]; f=np.arange(m,n-m)
    def calc(x):
        lam=x[-1]; L=Q-lam*H; z=np.zeros(n,complex)
        z[a]=np.exp(1j*np.r_[x[:-1],-x[:-1][::-1]])
        z[f]=solve(L[np.ix_(f,f)],-L[np.ix_(f,a)]@z[a],assume_a='her')
        return z,L@z,lam
    def fun(x):
        z,g,lam=calc(x)
        return np.r_[np.imag(np.conj(z[:m])*g[:m])*n*1000,1000*(np.vdot(z,H@z).real-b)]
    x=np.r_[np.linspace(-np.pi/2,-.28,m),1.343]
    if seed is not None:
        ts=(np.arange(len(seed))+.5)/len(seed)
        x[:-1]=np.interp(t[:m],ts,np.unwrap(np.angle(seed)))
    rr=root(fun,x,tol=1e-10); z,g,lam=calc(rr.x)
    mu=np.real(np.conj(z)*g); C=p[f]**2*z[f]*np.exp(-1j*np.log(t[f]/(1-t[f]))/lam)
    S=lam*H+np.diag(np.where(np.isin(np.arange(n),a),mu,0))-Q
    print(n,m,rr.success,'res',max(abs(fun(rr.x))),'lambda',lam,'P',np.vdot(z,Q@z).real,'maxfree',max(abs(z[f])),'minmu',min(mu[a]),'eig',np.linalg.eigvalsh(S)[0], 'edge',abs(z[f[:5]]),'Cerr',max(abs(C-C.mean()))/abs(C.mean()),flush=True)
    if max(abs(z))<1+1e-8 and min(mu[a])>=-1e-12:
        trim=max(1,len(f)//4); cc=C[trim:-trim].mean()
        print('central',abs(cc)*16,'edge extrapolation',abs(cc)/((m/n)*(1-m/n))**2,'central relative error',max(abs(C[trim:-trim]-cc))/abs(cc),'phase step deg',np.angle(z[m]/z[m-1])*90/np.pi,flush=True)
    return z,mu

if __name__=='__main__':
    seed,_=test(32,13); new=seed
    for n in (64,128,256):
        for m in range(round(.407*n)-1,round(.407*n)+2):
            z,mu=test(n,m,seed=seed)
            if max(abs(z))<1+1e-8 and min(mu[:m])>=-1e-12: new=z
        if len(new)==n:seed=new
