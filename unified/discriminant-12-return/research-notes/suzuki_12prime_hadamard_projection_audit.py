#!/usr/bin/env python3
"""M=3999 label-blind Hadamard projection-retention audit.

Uses the same 12-prime source sample and canonical B0 whitening as
suzuki_ray_alignment_expanded_blind.py.  For each source and unit-core star,
the three normalized leading-singular edge contributions are embedded as a
four-residue vector with zero at the star center, then transformed by H4/2.
The three nonprincipal coordinates are concatenated across the four stars.

Finite binary64 diagnostic only. Arithmetic character names are intentionally
not used in the decision statistics. No theorem/asymptotic/RH promotion.
"""
from math import exp,log,pi,sqrt,acos
import argparse
import numpy as np
from scipy.integrate import quad_vec
from scipy.special import sici
from scipy.linalg import cholesky,solve_triangular
from scipy.sparse.linalg import svds
from scipy.stats import pearsonr,spearmanr

CLASSES=(1,5,7,11)
BASE_QS=(2,3,4,5,7)
EXP_QS=(5,7,11,13,17,19,23,29,31,37,41,43)
H4=np.array([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],float)

def h(t):
    if t==0:return .25
    if abs(t)<1e-7:return .25-t/48-t*t/32+7*t**3/11520
    return exp(-t/2)/(1-exp(-2*t))-1/(2*t)

def core(n):
    while n%2==0:n//=2
    while n%3==0:n//=3
    return n%12

def make_matrix(modes,k,Z,d):
    m=modes[:,None]; n=modes[None,:]; den=n*n-m*m
    num=n*Z[:,None]-m*Z[None,:]; np.fill_diagonal(den,1)
    A=-(2/pi)*num/den; np.fill_diagonal(A,d)
    return .5*(A+A.T)

def source_matrix(q,modes,k):
    La=log(2) if q==4 else log(q); ell=log(q); w=La/sqrt(q)
    Z=2*w*np.sin(modes*pi*ell/2)
    d=-w*((2-ell)*np.cos(k*ell)+np.sin(k*ell)/k)
    return make_matrix(modes,k,Z,d)

def delta57(x):
    a,b,c=x
    return 4*(a-b)*c/(3*np.dot(x,x))

def audit(M=3999):
    modes=np.arange(22,M+1,2,dtype=float); k=modes*pi/2
    H,_=quad_vec(lambda t:h(float(t))*np.sin(k*t),0,2,epsabs=1e-11,epsrel=1e-11)
    arch,_=quad_vec(lambda t:-h(float(t))*((2-t)*np.cos(k*t)+np.sin(k*t)/k),0,2,epsabs=1e-11,epsrel=1e-11)
    Si,Ci=sici(modes*pi); cusp=np.log(modes/4)-Ci-Si/(modes*pi)
    B=make_matrix(modes,k,Si+2*H,cusp+arch)-.53*np.eye(len(modes))
    for q in BASE_QS:B+=source_matrix(q,modes,k)
    labels=np.array([core(int(n)) for n in modes])
    I={r:np.where(labels==r)[0] for r in CLASSES}
    L={r:cholesky(B[np.ix_(I[r],I[r])],lower=True,check_finite=False) for r in CLASSES}
    def wb(X,r,s):
        y=solve_triangular(L[r],X,lower=True,check_finite=False)
        return solve_triangular(L[s],y.T,lower=True,check_finite=False).T
    rays={}; projected={}; D={}
    for q in EXP_QS:
        Cq=source_matrix(q,modes,k); f=[]; px=[]; ds=[]
        for r in CLASSES:
            outer=[s for s in CLASSES if s!=r]
            blocks=[wb(Cq[np.ix_(I[r],I[s])],r,s) for s in outer]
            W=np.concatenate(blocks,axis=1)
            U,S,Vh=svds(W,k=1,which='LM',tol=1e-10,maxiter=5000)
            u=U[:,0].copy(); v=Vh[0].copy(); j=int(np.argmax(np.abs(u)))
            if u[j]<0:u=-u;v=-v
            vals={}; off=0
            for s,Q in zip(outer,blocks):
                n=Q.shape[1]; z=float((u@Q@v[off:off+n])/S[0]); vals[s]=z; f.append(z); off+=n
            residue=np.array([vals.get(s,0.) for s in CLASSES])
            x=(H4@residue/2)[1:]
            px.extend(x); ds.append(delta57(x))
        rays[q]=np.array(f)/np.linalg.norm(f)
        projected[q]=np.array(px)/np.linalg.norm(px)
        D[q]=np.array(ds)
    pairs=[]; full=[]; proj=[]
    for i,q in enumerate(EXP_QS):
        for r in EXP_QS[i+1:]:
            pairs.append((q,r))
            full.append(acos(float(np.clip(rays[q]@rays[r],-1,1)))*180/pi)
            proj.append(acos(float(np.clip(projected[q]@projected[r],-1,1)))*180/pi)
    full=np.array(full); proj=np.array(proj)
    def top3(V,q):
        z=[]
        for r in EXP_QS:
            if r!=q:z.append((acos(float(np.clip(V[q]@V[r],-1,1))),r))
        return {r for _,r in sorted(z)[:3]}
    js=[]
    for q in EXP_QS:
        A=top3(rays,q); B3=top3(projected,q); J=len(A&B3)/len(A|B3); js.append(J)
        print('TOP3',q,sorted(A),sorted(B3),format(J,'.17g'))
    print('PEARSON',format(pearsonr(full,proj).statistic,'.17g'))
    print('SPEARMAN',format(spearmanr(full,proj).statistic,'.17g'))
    print('MEAN_TOP3_JACCARD',format(float(np.mean(js)),'.17g'))
    for idx in np.argsort(full)[:5]:
        q,r=pairs[idx]
        print('CLOSE',q,r,'FULL',format(full[idx],'.17g'),'PROJECTED',format(proj[idx],'.17g'),'DELTA_NORM',format(float(np.linalg.norm(D[q]-D[r])),'.17g'))
    for q in EXP_QS:print('DELTA57_BY_STAR',q,*[format(z,'.17g') for z in D[q]])
    print('PASS_GEOMETRY_RETENTION',spearmanr(full,proj).statistic>=.80 and np.mean(js)>=.60)
    print('guardrail: finite binary64 M=%d; label-blind decision statistics; no theorem promotion'%M)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--M',type=int,default=3999)
    audit(ap.parse_args().M)
