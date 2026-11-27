import numpy as np
from k4_unrestricted_polarization_v15_1585 import run, matrices
from scipy.integrate import solve_ivp

def test(n,budget):
    z=run(n,budget); Q,H=matrices(n); t=(np.arange(n)+.5)/n; p=t*(1-t); f=abs(z)<.9999
    w=Q@z; v=H@z; lam=np.vdot(v[f],w[f]).real/np.vdot(v[f],v[f]).real
    C=p[f]**2*z[f]*np.exp(-1j*np.log(t[f]/(1-t[f]))/lam)
    c=C.mean()
    print('interior',n,budget,'lambda',lam,'cells',f.sum(),'range',t[f][[0,-1]],'Cabs',abs(c),'relative max error',max(abs(C-c))/abs(c),'center amplitude',16*abs(c),flush=True)
    if n==128:
        c=C[3:-3].mean()
        print('trimmed',max(abs(C[3:-3]-c))/abs(c), 'center amplitude',16*abs(c),flush=True)
    eta=.2; y=np.array([0j,0j,1+0j,0j]); Y=np.r_[np.zeros(4),np.eye(2).ravel()]; err=0; wr=0
    for j,e in enumerate(z):
        def rhs(t,y):
            a,b,ap,bp=y
            return [ap,bp,-eta*e*np.conj(b),-eta*e*np.conj(a)]
        def rhs2(t,y):
            return np.r_[y[4:],(-eta*np.array([[e.real,e.imag],[e.imag,-e.real]])@y[:4].reshape(2,2)).ravel()]
        y=solve_ivp(rhs,(j/n,(j+1)/n),y,rtol=1e-12,atol=1e-14).y[:,-1]
        Y=solve_ivp(rhs2,(j/n,(j+1)/n),Y,rtol=1e-12,atol=1e-14).y[:,-1]
        a,b,ap,bp=y; D=np.array([[(a+b).real,(b-a).imag],[(a+b).imag,(a-b).real]])
        err=max(err,np.max(abs(D-Y[:4].reshape(2,2))))
        wr=max(wr,abs(np.imag(np.conj(a)*ap-np.conj(b)*bp)))
    print('complex replay',n,'matrix error',err,'wronskian',wr,'det',abs(a)**2-abs(b)**2,'psi',np.angle(a),flush=True)
    assert err<1e-10 and wr<1e-10
if __name__=='__main__':
    for n in (32,64,128):test(n,.003)
