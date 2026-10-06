#!/usr/bin/env python3
"""Well-conditioned M=8000 -> remote FFT/low-rank Schur diagnostic.

Front arithmetic (near-null) is done by the existing arch-200 LDDD/Feshbach
machinery.  The remote Schur solve is then performed in the certified
well-conditioned space.

Remote front coupling representation:
  * exact near block 8000<n<16000 compressed by deterministic rank-24 SVD;
  * n>=16000 K=10 23-channel expansion (m/n<=1/2).

The 47x47 correlated front-inverse Gram is formed in LDDD/Feshbach arithmetic.
Before applying it on the remote space, the 47 remote channel functions are QR
orthogonalized and the Gram is transformed in mpmath.  This preserves the
large 1/n/pole cancellation instead of multiplying the raw ill-scaled Gram in
binary64.

Diagnostic only: rank-24 residual, K10 geometric remainder, FFT/raw arithmetic,
and infinite truncation remain to be outward charged.
"""
from __future__ import annotations
import argparse,json,os
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg,LinearOperator,svds

for k in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[k]="1"

from suzuki_M8000_embedded_p4_ldd_capacity import embedded_protected_basis
from suzuki_M3999_frozen_p4_source_capacity_midpoint import full_source_matrix
from suzuki_M8000_mu1_full_near_triple_diagnostic import lattice,exact_cross
from suzuki_N4000_K10_scaled_coupling_gram import scales,channel_matrix
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,dd_matrix_to_mp,dd_project,form_Ktilde,form_trial,
    mp_inverse_split,refine_once,residuals_dd,solve_correction,
)
from suzuki_ldd_remote_source_lead_diagnostic import dd_linear_combination
from suzuki_ldd_source_operator import (
    LD,add as dd_add,dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,matvec as dd_matvec,
    norm2 as dd_norm2,sub as dd_sub,
)
from suzuki_remote_fft_matvec_validation import fft_offdiag,arch_diag_vector
from suzuki_endpoint_M3999_midpoint_effective_core import (
    z_source_faithful,cusp_diag,prime_diag,pole_vector,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_remote_schur_fft_diagnostic_result.json"
DPS=180; RANK=24

def source_rows(modes):
    n=np.asarray(modes,float); k=n*np.pi/2
    parity=np.where(np.asarray(modes)%2==0,1.0,-1.0)
    return k*(np.exp(-1)-parity*np.e)/(1+k*k)

def target_res(data,P,Gih,Gil,Xh,Xl,Th,Tl):
    AXh,AXl=dd_matvec(data,Xh,Xl)
    Rh,Rl=dd_sub(AXh,AXl,Th,Tl)
    Rh,Rl=dd_project(P,Gih,Gil,Rh,Rl)
    return AXh,AXl,Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(Xh.shape[1])]

def build_front(sector):
    base,modes,P,_,_=embedded_protected_basis(sector)
    near=lattice(sector,8001,16000)
    B=exact_cross(near,modes,sector)
    v0=np.linspace(1,2,min(B.shape)); v0/=np.linalg.norm(v0)
    U,s,Vt=svds(B,k=RANK,which="LM",tol=1e-11,maxiter=5000,v0=v0,solver="arpack")
    ix=np.argsort(s)[::-1]; U=U[:,ix];s=s[ix];Vt=Vt[ix]
    Tn=Vt.T*s[None,:]

    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=200,correction_terms=50)
    names,ss=scales(sector)
    Tsh,Tsl=channel_matrix(data,modes,sector,names,ss)
    Ts=np.asarray(Tsh+Tsl,dtype=float)
    T=np.column_stack([Tn,Ts])

    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])
    A,f=full_source_matrix(modes,sector)
    op,proj,gamma,evals,Y0,yf0,initial=build_double_complement(A,P,Gi,f,rtol=2e-14)

    Yh=Y0.astype(LD);Yl=np.zeros_like(Yh,dtype=LD)
    yfh=yf0.astype(LD);yfl=np.zeros_like(yfh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl); yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)
    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n0=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Yh,Yl,yfh,yfl=refine_once(op,proj,Yh,Yl,yfh,yfl,Rh,Rl)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl); yfh,yfl=dd_project(P,Gih,Gil,yfh,yfl)
    Uh,Ul=form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n1=residuals_dd(data,P,Gih,Gil,Uh,Ul)
    K=form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)

    Th=np.asarray(T,dtype=LD); Tl=np.zeros_like(Th,dtype=LD)
    X=np.empty_like(T)
    for j in range(T.shape[1]):
        X[:,j]=solve_correction(op,proj,proj(T[:,j]),rtol=2e-14)
    Xh=np.asarray(X,dtype=LD); Xl=np.zeros_like(Xh,dtype=LD)
    Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)
    AXh,AXl,TRh,TRl,tr0=target_res(data,P,Gih,Gil,Xh,Xl,Th,Tl)
    for j in range(T.shape[1]):
        d=solve_correction(op,proj,-(TRh[:,j]+TRl[:,j]),rtol=2e-14)
        Xh[:,j],Xl[:,j]=dd_add(Xh[:,j],Xl[:,j],d,np.zeros_like(d,dtype=LD))
    Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)
    AXh,AXl,TRh,TRl,tr1=target_res(data,P,Gih,Gil,Xh,Xl,Th,Tl)

    Wh,Wl=Uh[:,:6],Ul[:,:6]
    sh,sl=dd_dot_columns(Wh,Wl,AUh[:,:6],AUl[:,:6])
    gh,gl=dd_dot_columns(Wh,Wl,Th,Tl)
    hh,hl=dd_dot_columns(Th,Tl,Xh,Xl)
    with mp.workdps(DPS):
        S=dd_matrix_to_mp(sh,sl); S=(S+S.T)/2
        gt=dd_matrix_to_mp(gh,gl)
        ht=dd_matrix_to_mp(hh,hl); ht=(ht+ht.T)/2
        Z=mp.matrix(6,T.shape[1])
        for j in range(T.shape[1]):
            q=mp.lu_solve(S,gt[:,j])
            for i in range(6): Z[i,j]=q[i]
        M=ht+gt.T*Z; M=(M+M.T)/2

        gs=-K[:6,6]; hs=-K[6,6]
        w=mp.lu_solve(S,gs); G=hs+(gs.T*w)[0]; C=1/G
        coeff=[w[j] for j in range(6)]+[mp.mpf(1)]
        xh,xl=dd_linear_combination(Uh,Ul,coeff)
        sq=mp.sqrt(C)

    y=np.asarray(xh+xl,dtype=float)*float(sq)
    return {"modes":modes,"near":near,"U":U,"s":s,"T":T,"Ts":Ts,
            "names":names,"scales":ss,"M":M,"C":C,"sqrtC":sq,"y":y,
            "front_res":max(n1),"target_res":max(tr1),"gamma":gamma}

def remote_phi(st,sector,rmax):
    start=8001 if sector=="even-v" else 8002
    rm=np.arange(start,rmax+1,2,dtype=int)
    nr=len(st["near"]); q=RANK+23
    Phi=np.zeros((len(rm),q),dtype=float)
    Phi[:nr,:RANK]=st["U"]
    z=z_source_faithful(rm); p,_=pole_vector(rm,sector)
    alpha=2.0 if sector=="even-v" else -2.0
    ss=[float(x) for x in st["scales"]]
    mask=rm>=16000
    n=rm[mask].astype(float); zz=z[mask]
    cols=[]
    for j in range(11):
        cols.append(zz/n**(2*j+2)/ss[2*j])
        cols.append(1.0/n**(2*j+1)/ss[2*j+1])
    cols.append(alpha*p[mask]/ss[-1])
    Phi[np.ix_(np.where(mask)[0],np.arange(RANK,q))]=np.column_stack(cols)
    return rm,z,p,Phi

def one(sector,rmax):
    st=build_front(sector)
    rm,z,p,Phi=remote_phi(st,sector,rmax)
    nr=len(st["near"]); sq=float(st["sqrtC"])

    # Stable transformed self-energy K = R M R^T after Phi=Q R.
    Q,R=np.linalg.qr(Phi,mode="reduced")
    with mp.workdps(100):
        Rmp=mp.matrix([[mp.mpf(str(v)) for v in row] for row in R])
        Kmp=Rmp*st["M"]*Rmp.T; Kmp=(Kmp+Kmp.T)/2
        kvals,_=mp.eigsy(Kmp)
        K=np.array([[float(Kmp[i,j]) for j in range(Kmp.cols)] for i in range(Kmp.rows)])
    print(sector,"remote transformed self-energy eig range",float(kvals[0]),float(kvals[-1]),flush=True)

    # Normalized remote source residual.
    f=source_rows(rm)
    r=sq*f
    Bnear=exact_cross(st["near"],st["modes"],sector)
    r[:nr]-=Bnear@st["y"]
    csep=st["Ts"].T@st["y"]
    r[nr:]-=Phi[nr:,RANK:]@csep

    diag=cusp_diag(rm)+prime_diag(rm)+arch_diag_vector(rm,terms=120)
    off=lambda x: fft_offdiag(rm,z,x)
    _,alpha=pole_vector(rm,sector)
    def Smv(x):
        x=np.asarray(x,float)
        raw=off(x)+diag*x+alpha*p*float(p@x)
        return raw-Q@(K@(Q.T@x))
    Sop=LinearOperator((len(rm),len(rm)),matvec=Smv,dtype=float)
    dinv=1/np.maximum(np.abs(diag),1.0)
    pre=LinearOperator((len(rm),len(rm)),matvec=lambda x:dinv*x,dtype=float)
    cnt=[0]
    sol,info=cg(Sop,r,M=pre,rtol=2e-12,atol=0,maxiter=12000,
                callback=lambda _:cnt.__setitem__(0,cnt[0]+1))
    rr=r-Smv(sol)
    eta=float(r@sol)
    row={"sector":sector,"rmax":rmax,"dimension":len(rm),"eta_tail_midpoint":eta,
         "source_l2":float(np.linalg.norm(r)),"cg_info":int(info),"cg_iters":cnt[0],
         "cg_residual_l2":float(np.linalg.norm(rr)),
         "transformed_selfenergy_min_eig":float(kvals[0]),
         "transformed_selfenergy_max_eig":float(kvals[-1]),
         "front_capacity":mp.nstr(st["C"],50),
         "front_source_residual":st["front_res"],"front_target_residual":st["target_res"],
         "guardrail":"Midpoint remote Schur diagnostic; low-rank residual, K10 remainder, FFT arithmetic and truncation not outward."}
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--rmax",type=int,required=True)
    a=ap.parse_args()
    row=one(a.sector,a.rmax)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__": main()
