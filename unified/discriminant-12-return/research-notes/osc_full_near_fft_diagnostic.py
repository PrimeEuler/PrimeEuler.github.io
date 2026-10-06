#!/usr/bin/env python3
"""Full-near-block FFT diagnostic for the N=32000 oscillatory remainder.

Diagnostic only.  This fixes the J=300 truncation blind spot by solving the
entire paired bare near block
    even: 32001,32003,...,63999
    odd : 32002,32004,...,64000
with the validated FFT Toeplitz/Hankel raw matvec.

For each requested J prefix it reports
  * ||w_e||, ||w_o||, product,
  * bare paired Rosc quadratic form,
  * A_e*|qf| / promoted primary finite margin,
where both solves use the paired RHS u_j=1/n_j as in v14.069.

No theorem claim: the operator is the bare near-block compression, not the
full infinite remote Schur operator, and arch evaluation is the validated
vectorized midpoint recurrence.
"""
from __future__ import annotations
import argparse, json, math
import numpy as np
from scipy.sparse.linalg import LinearOperator, cg

from suzuki_remote_fft_matvec_validation import (
    fft_offdiag, arch_diag_vector,
)
from suzuki_endpoint_M3999_midpoint_effective_core import (
    cusp_diag, prime_diag, z_source_faithful, pole_vector,
)

N=32000
A_E=1200.4587051950723327
M_PRIMARY=1.8869797018800170e-5
E0=0.37474310047
C_D=-32*math.cosh(1)/math.pi**2 + 16*E0/math.pi**2

def payload(modes,sector):
    modes=np.asarray(modes,dtype=int)
    z=z_source_faithful(modes)
    diag=cusp_diag(modes)+prime_diag(modes)+arch_diag_vector(modes)
    p,alpha=pole_vector(modes,sector)
    p=np.asarray(p,dtype=float)
    def mv(x):
        x=np.asarray(x,dtype=float)
        return fft_offdiag(modes,z,x)+diag*x+alpha*p*float(p@x)
    return mv

def solve(modes,sector,u):
    mv=payload(modes,sector)
    op=LinearOperator((len(modes),len(modes)),matvec=mv,dtype=float)
    it=[0]
    x,info=cg(op,u,rtol=2e-12,atol=0.0,maxiter=5000,
              callback=lambda _:it.__setitem__(0,it[0]+1))
    if info!=0:
        raise RuntimeError((sector,len(modes),"cg",info))
    res=float(np.linalg.norm(mv(x)-u))
    return x,mv,it[0],res

def one(J):
    n=N+1+2*np.arange(J,dtype=int)
    m=n+1
    u=1.0/n.astype(float)
    we,mve,ite,re=solve(n,"even-v",u)
    wo,mvo,ito,ro=solve(m,"odd-v",u)
    delta=mvo(we)-mve(we)-C_D*u*float(u@we)
    qf=float(wo@delta)
    prod=float(np.linalg.norm(wo)*np.linalg.norm(we))
    return {
      "J":J,
      "n_first":int(n[0]),"n_last":int(n[-1]),
      "m_first":int(m[0]),"m_last":int(m[-1]),
      "cg_iters_even":ite,"cg_iters_odd":ito,
      "residual_even":re,"residual_odd":ro,
      "norm_we":float(np.linalg.norm(we)),
      "norm_wo":float(np.linalg.norm(wo)),
      "norm_product":prod,
      "Rosc_bare_qf":qf,
      "A_e_abs_qf":A_E*abs(qf),
      "A_e_abs_qf_over_Mprimary":A_E*abs(qf)/M_PRIMARY,
      "effective_constant_absqf_over_normprod":abs(qf)/prod,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--J",type=int,nargs="+",default=[300,1000,4000,16000])
    a=ap.parse_args()
    rows=[]
    for J in a.J:
        row=one(J)
        rows.append(row)
        print(json.dumps(row,indent=2),flush=True)
    print("GUARDRAIL: midpoint/bare finite-near diagnostic only; not theorem evidence.")

if __name__=="__main__":
    main()
