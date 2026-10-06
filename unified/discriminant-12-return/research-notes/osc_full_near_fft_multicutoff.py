#!/usr/bin/env python3
"""Multicutoff full-near bare FFT oscillatory diagnostic.

Runs the complete octave N<n<=2N for N=64000 and 128000 (or supplied N),
using paired RHS u_j=1/n_j and the validated high-remote FFT operator.
Reports qf, norms, and simple scaling only. Diagnostic, not theorem evidence.
"""
from __future__ import annotations
import argparse,json,math
import numpy as np
from scipy.sparse.linalg import LinearOperator,cg
from suzuki_remote_fft_matvec_validation import fft_offdiag,arch_diag_vector
from suzuki_endpoint_M3999_midpoint_effective_core import (
    cusp_diag,prime_diag,z_source_faithful,pole_vector,
)

E0=0.37474310047
C_D=-32*math.cosh(1)/math.pi**2 + 16*E0/math.pi**2

def payload(modes,sector):
    modes=np.asarray(modes,dtype=int)
    z=z_source_faithful(modes)
    diag=cusp_diag(modes)+prime_diag(modes)+arch_diag_vector(modes)
    p,alpha=pole_vector(modes,sector);p=np.asarray(p,float)
    def mv(x):
        x=np.asarray(x,float)
        return fft_offdiag(modes,z,x)+diag*x+alpha*p*float(p@x)
    return mv

def solve(modes,sector,u):
    mv=payload(modes,sector)
    op=LinearOperator((len(modes),len(modes)),matvec=mv,dtype=float)
    c=[0]
    x,info=cg(op,u,rtol=2e-12,atol=0,maxiter=5000,
              callback=lambda _:c.__setitem__(0,c[0]+1))
    if info!=0: raise RuntimeError((sector,len(modes),info))
    return x,mv,c[0],float(np.linalg.norm(mv(x)-u))

def one(N):
    J=N//2
    n=N+1+2*np.arange(J,dtype=int)
    m=n+1
    u=1/n.astype(float)
    we,mve,ie,re=solve(n,"even-v",u)
    wo,mvo,io,ro=solve(m,"odd-v",u)
    qf=float(wo@(mvo(we)-mve(we)-C_D*u*float(u@we)))
    prod=float(np.linalg.norm(we)*np.linalg.norm(wo))
    out={
      "N":N,"J":J,
      "norm_we":float(np.linalg.norm(we)),
      "norm_wo":float(np.linalg.norm(wo)),
      "norm_product":prod,
      "Rosc_bare_qf":qf,
      "abs_qf":abs(qf),
      "effective_constant":abs(qf)/prod,
      "cg_iters_even":ie,"cg_iters_odd":io,
      "residual_even":re,"residual_odd":ro,
    }
    print(json.dumps(out,indent=2),flush=True)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--N",type=int,nargs="+",default=[64000,128000])
    a=ap.parse_args()
    rows=[one(N) for N in a.N]
    if len(rows)>1:
        for i in range(1,len(rows)):
            print("qf_ratio",rows[i]["N"],"/",rows[i-1]["N"],"=",
                  rows[i]["abs_qf"]/rows[i-1]["abs_qf"])
    print("GUARDRAIL: bare finite-octave midpoint diagnostic only.")

if __name__=="__main__":
    main()
