#!/usr/bin/env python3
"""Exact-near matrix-free remote-Schur endpoint diagnostic.

This removes the global SVD compression from 8000<n<16000.  The exact near
coupling B is applied matrix-free through the certified/refined front response:

    x -> B F_eff^{-1} B^T x.

For odd parity, n=16000 is represented exactly as a one-row boundary block;
the K=10 separated channels start strictly above 16000.  The first acceptance
gate is rmax=16000 against the promoted v14.059 theorem midpoint.

Diagnostic only: this script does not yet provide outward FFT/K10/truncation
budgets for the infinite tail.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.sparse.linalg import cg, LinearOperator
import suzuki_M8000_remote_schur_fft_diagnostic as b

HERE=Path(__file__).resolve().parent
OUT=HERE/"M8000_remote_schur_exact_near_endpoint_result.json"
DPS=180
TARGET={
    "even-v":0.0036404008257719944,
    "odd-v":0.003617497467397701,
}

def build_front_operator(sector):
    _,modes,P,_,_=b.embedded_protected_basis(sector)
    near=b.lattice(sector,8001,16000)

    data=b.hp_parity_data(modes,sector,dps=DPS,arch_terms=200,correction_terms=50)
    names,ss=b.scales(sector)
    Tsh,Tsl=b.channel_matrix(data,modes,sector,names,ss)
    Ts=np.asarray(Tsh+Tsl,dtype=float)

    Gh,Gl=b.dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=b.mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    A,f=b.full_source_matrix(modes,sector)
    op,proj,gamma,evals,Y0,yf0,initial=b.build_double_complement(
        A,P,Gi,f,rtol=2e-14
    )

    Yh=Y0.astype(b.LD); Yl=np.zeros_like(Yh,dtype=b.LD)
    yfh=yf0.astype(b.LD); yfl=np.zeros_like(yfh,dtype=b.LD)
    Yh,Yl=b.dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=b.dd_project(P,Gih,Gil,yfh,yfl)

    Uh,Ul=b.form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n0=b.residuals_dd(data,P,Gih,Gil,Uh,Ul)
    Yh,Yl,yfh,yfl=b.refine_once(op,proj,Yh,Yl,yfh,yfl,Rh,Rl)
    Yh,Yl=b.dd_project(P,Gih,Gil,Yh,Yl)
    yfh,yfl=b.dd_project(P,Gih,Gil,yfh,yfl)
    Uh,Ul=b.form_trial(P,Yh,Yl,yfh,yfl)
    AUh,AUl,Rh,Rl,n1=b.residuals_dd(data,P,Gih,Gil,Uh,Ul)
    K=b.form_Ktilde(data,Uh,Ul,AUh,AUl,DPS)

    Wh,Wl=Uh[:,:6],Ul[:,:6]
    sh,sl=b.dd_dot_columns(Wh,Wl,AUh[:,:6],AUl[:,:6])
    with mp.workdps(DPS):
        S=b.dd_matrix_to_mp(sh,sl); S=(S+S.T)/2
        gs=-K[:6,6]; hs=-K[6,6]
        w=mp.lu_solve(S,gs)
        G=hs+(gs.T*w)[0]
        C=1/G
        coeff=[w[j] for j in range(6)]+[mp.mpf(1)]
        xh,xl=b.dd_linear_combination(Uh,Ul,coeff)
        sq=mp.sqrt(C)

    y=np.asarray(xh+xl,dtype=float)*float(sq)
    return {
        "modes":modes,"P":P,"Gih":Gih,"Gil":Gil,
        "data":data,"op":op,"proj":proj,"S":S,
        "Wh":Wh,"Wl":Wl,"near":near,"Ts":Ts,
        "scales":ss,"sqrtC":sq,"y":y,
        "front_source_residual":max(n1),
        "gamma":gamma,
    }

def front_response(st,t,counters):
    t=np.asarray(t,dtype=float)
    tp=st["proj"](t)
    x=b.solve_correction(st["op"],st["proj"],tp,rtol=2e-14)

    xh=np.asarray(x,dtype=b.LD); xl=np.zeros_like(xh,dtype=b.LD)
    xh,xl=b.dd_project(st["P"],st["Gih"],st["Gil"],xh,xl)
    th=np.asarray(t,dtype=b.LD); tl=np.zeros_like(th,dtype=b.LD)

    AXh,AXl=b.dd_matvec(st["data"],xh,xl)
    Rh,Rl=b.dd_sub(AXh,AXl,th,tl)
    Rh,Rl=b.dd_project(st["P"],st["Gih"],st["Gil"],Rh,Rl)
    r0=b.dd_norm2(Rh,Rl)

    d=b.solve_correction(
        st["op"],st["proj"],-(Rh+Rl),rtol=2e-14
    )
    xh,xl=b.dd_add(xh,xl,d,np.zeros_like(d,dtype=b.LD))
    xh,xl=b.dd_project(st["P"],st["Gih"],st["Gil"],xh,xl)

    AXh,AXl=b.dd_matvec(st["data"],xh,xl)
    Rh,Rl=b.dd_sub(AXh,AXl,th,tl)
    Rh,Rl=b.dd_project(st["P"],st["Gih"],st["Gil"],Rh,Rl)
    r1=b.dd_norm2(Rh,Rl)

    gh,gl=b.dd_dot_columns(
        st["Wh"],st["Wl"],th[:,None],tl[:,None]
    )
    with mp.workdps(DPS):
        g=b.dd_matrix_to_mp(gh,gl)
        q=mp.lu_solve(st["S"],g)
        wh,wl=b.dd_linear_combination(
            st["Wh"],st["Wl"],[q[j] for j in range(6)]
        )
    xh,xl=b.dd_add(xh,xl,wh,wl)
    counters["calls"]+=1
    counters["max_res0"]=max(counters["max_res0"],float(r0))
    counters["max_res1"]=max(counters["max_res1"],float(r1))
    if counters["calls"]<=3 or counters["calls"]%5==0:
        print("front_response",counters["calls"],"res",float(r0),"->",float(r1),flush=True)
    return np.asarray(xh+xl,dtype=float)

def build_coupling(st,sector,rmax):
    start=8001 if sector=="even-v" else 8002
    rm=np.arange(start,rmax+1,2,dtype=int)
    nr=len(st["near"])
    if nr>len(rm) or not np.array_equal(rm[:nr],st["near"]):
        raise RuntimeError("remote prefix does not match exact near lattice")

    Bnear=b.exact_cross(st["near"],st["modes"],sector)
    pos=nr
    Bbd=None
    if sector=="odd-v" and pos<len(rm) and int(rm[pos])==16000:
        Bbd=b.exact_cross(np.array([16000],dtype=int),st["modes"],sector)
        pos+=1

    far=rm[pos:]
    if len(far):
        z=b.z_source_faithful(far)
        p,_=b.pole_vector(far,sector)
        alpha=2.0 if sector=="even-v" else -2.0
        ss=[float(x) for x in st["scales"]]
        n=far.astype(float)
        cols=[]
        for j in range(11):
            cols.append(z/n**(2*j+2)/ss[2*j])
            cols.append(1.0/n**(2*j+1)/ss[2*j+1])
        cols.append(alpha*p/ss[-1])
        Phi=np.column_stack(cols)
    else:
        Phi=np.zeros((0,23),dtype=float)

    def BT(x):
        x=np.asarray(x,dtype=float)
        t=Bnear.T@x[:nr]
        q=nr
        if Bbd is not None:
            t=t+Bbd[0]*x[q]
            q+=1
        if q<len(rm):
            t=t+st["Ts"]@(Phi.T@x[q:])
        return t

    def Bv(v):
        v=np.asarray(v,dtype=float)
        out=np.zeros(len(rm),dtype=float)
        out[:nr]=Bnear@v
        q=nr
        if Bbd is not None:
            out[q]=float((Bbd@v)[0])
            q+=1
        if q<len(rm):
            out[q:]=Phi@(st["Ts"].T@v)
        return out

    return rm,BT,Bv,{"near_rows":nr,"boundary_exact":Bbd is not None,"far_rows":len(far)}

def one(sector,rmax):
    st=build_front_operator(sector)
    rm,BT,Bv,cmeta=build_coupling(st,sector,rmax)
    sq=float(st["sqrtC"])

    f=b.source_rows(rm)
    r=sq*f-Bv(st["y"])

    z=b.z_source_faithful(rm)
    p,alpha=b.pole_vector(rm,sector)
    diag=b.cusp_diag(rm)+b.prime_diag(rm)+b.arch_diag_vector(rm,terms=200)
    off=lambda x:b.fft_offdiag(rm,z,x)
    counters={"calls":0,"max_res0":0.0,"max_res1":0.0}

    def Smv(x):
        x=np.asarray(x,dtype=float)
        raw=off(x)+diag*x+alpha*p*float(p@x)
        t=BT(x)
        y=front_response(st,t,counters)
        return raw-Bv(y)

    Sop=LinearOperator((len(rm),len(rm)),matvec=Smv,dtype=float)
    dinv=1/np.maximum(np.abs(diag),1.0)
    pre=LinearOperator((len(rm),len(rm)),matvec=lambda x:dinv*x,dtype=float)
    cnt=[0]
    sol,info=cg(
        Sop,r,M=pre,rtol=2e-12,atol=0,maxiter=12000,
        callback=lambda _:cnt.__setitem__(0,cnt[0]+1)
    )
    rr=r-Smv(sol)
    eta=float(r@sol)
    target=TARGET[sector]
    row={
        "sector":sector,"rmax":rmax,"dimension":len(rm),
        "eta_exact_near_midpoint":eta,
        "eta_theorem_midpoint":target,
        "signed_error":eta-target,
        "absolute_error":abs(eta-target),
        "relative_error":abs(eta-target)/abs(target),
        "source_l2":float(np.linalg.norm(r)),
        "cg_info":int(info),"cg_iters":cnt[0],
        "cg_residual_l2":float(np.linalg.norm(rr)),
        "front_response_calls":counters["calls"],
        "front_response_max_residual_before_refine":counters["max_res0"],
        "front_response_max_residual_after_refine":counters["max_res1"],
        "front_source_residual":st["front_source_residual"],
        "front_gamma":st["gamma"],
        **cmeta,
        "guardrail":"Exact-near matrix-free endpoint diagnostic; no infinite-tail theorem claim."
    }
    print(json.dumps(row,indent=2),flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    ap.add_argument("--rmax",type=int,default=16000)
    a=ap.parse_args()
    row=one(a.sector,a.rmax)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
