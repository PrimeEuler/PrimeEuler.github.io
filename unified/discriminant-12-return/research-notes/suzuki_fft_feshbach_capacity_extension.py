#!/usr/bin/env python3
"""Matrix-free FFT/Feshbach finite-cutoff capacity diagnostic."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,cg

from suzuki_remote_fft_matvec_validation import fft_offdiag,arch_diag_vector
from suzuki_endpoint_M3999_midpoint_effective_core import (
    z_source_faithful,cusp_diag,prime_diag,pole_vector,
)
from suzuki_M3999_frozen_p4_source_capacity_midpoint import frozen_protected_basis

BASE=4000
OUT=Path(__file__).resolve().parent/"fft_feshbach_capacity_extension_result.json"

def modes_for(sector,M):
    return np.arange(1 if sector=="even-v" else 2,M+1,2,dtype=int)

def source_rows(modes):
    n=modes.astype(float); k=n*np.pi/2
    parity=np.where(modes%2==0,1.0,-1.0)
    return k*(np.exp(-1)-parity*np.e)/(1+k*k)

def one(sector,M,rtol):
    modes=modes_for(sector,M); n=len(modes); t0=time.perf_counter()
    z=z_source_faithful(modes)
    diag=cusp_diag(modes)+prime_diag(modes)+arch_diag_vector(modes,terms=120)
    p,alpha=pole_vector(modes,sector)
    f=source_rows(modes)

    base=modes_for(sector,BASE)
    Pb,_=frozen_protected_basis(sector,base)
    P=np.zeros((n,6)); P[:len(base)]=Pb

    def proj(x): return x-P@(P.T@x)
    def A(x):
        x=np.asarray(x,float)
        return fft_offdiag(modes,z,x)+diag*x+alpha*p*float(p@x)

    AP=np.column_stack([A(P[:,j]) for j in range(6)])
    App=(P.T@AP); App=(App+App.T)/2
    E=proj(AP); fp=P.T@f; fq=proj(f)

    def D(x):
        q=proj(x)
        return proj(A(q))+P@(P.T@x)
    op=LinearOperator((n,n),matvec=D,dtype=float)

    dinv=1/np.maximum(np.abs(diag),1.0)
    def PM(x):
        q=proj(x)
        return dinv*q+P@(P.T@x)
    pre=LinearOperator((n,n),matvec=PM,dtype=float)

    rhs=np.column_stack([E,fq]); sol=np.empty_like(rhs)
    infos=[];iters=[];res=[]
    for j in range(7):
        cnt=[0]
        x,info=cg(op,rhs[:,j],M=pre,rtol=rtol,atol=0,maxiter=12000,
                  callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
        x=proj(x); rr=rhs[:,j]-D(x)
        sol[:,j]=x; infos.append(int(info));iters.append(cnt[0]);res.append(float(np.linalg.norm(rr)))
        print(sector,M,"rhs",j,"info",info,"iters",cnt[0],"res",res[-1],flush=True)
        if info: raise RuntimeError((sector,M,j,info))

    Y=sol[:,:6]; yf=sol[:,6]
    S=App-E.T@Y; S=(S+S.T)/2
    g=fp-E.T@yf; h=float(fq@yf)
    w=np.linalg.solve(S,g); G=h+float(g@w); C=1/G
    row={"sector":sector,"maxmode":M,"dimension":n,"capacity":C,"G":G,
         "S_eigenvalues":np.linalg.eigvalsh(S).tolist(),
         "max_cg_residual_l2":max(res),"cg_iters":iters,"cg_info":infos,
         "seconds":time.perf_counter()-t0,
         "guardrail":"FFT/Feshbach finite-cutoff diagnostic; outward certification pending."}
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--maxmode",type=int,required=True)
    ap.add_argument("--rtol",type=float,default=2e-12)
    a=ap.parse_args()
    row=one(a.sector,a.maxmode,a.rtol)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__": main()
