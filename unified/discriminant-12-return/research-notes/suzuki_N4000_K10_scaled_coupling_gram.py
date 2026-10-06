#!/usr/bin/env python3
"""Scaled K=10 far-coupling Gram at frozen N=4000, tail n>=16000.

For n>=16000 and finite m<=4000,

  B(n,m) =
    sum_{j=0}^{10} [ z_n/n^(2j+2) * a_j(m)
                    +1/n^(2j+1) * b_j(m) ]
    + alpha p_n p_m + geometric remainder,

with
  a_j=(2/pi)m^(2j+1),
  b_j=-(2/pi)z_m m^(2j).

Raw high-order coefficient columns are enormous.  Scale each coefficient
column by an upper l2 norm s_i of its corresponding remote scalar function.
Then the normalized remote scalar functions have l2 norm <=1 and the finite
coefficient columns are moderate.

Compute the 23x23 correlated matrix
  M_scaled = W_scaled^T A_N^{-1} W_scaled
using the frozen six-plane LDDD/Feshbach architecture.  No global inverse is
formed.

This is a midpoint/certificate-target payload for the final signed remote
Woodbury solve.  Outward source/arithmetic radii are not promoted here.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import mpmath as mp
import numpy as np

from suzuki_M3999_frozen_p4_source_capacity_midpoint import (
    frozen_protected_basis,full_source_matrix,
)
from suzuki_ldd_refined_capacity_bracket import (
    build_double_complement,dd_matrix_to_mp,dd_project,
    mp_inverse_split,solve_correction,
)
from suzuki_ldd_source_operator import (
    LD,add as dd_add,dot_columns as dd_dot_columns,
    hp_parity_data_ld as hp_parity_data,ldd_to_mpf,
    matvec as dd_matvec,norm2 as dd_norm2,split_mpf_ld,sub as dd_sub,
)

HERE=Path(__file__).resolve().parent
OUT=HERE/"N4000_K10_scaled_coupling_gram_result.json"
N=4000
DPS=180
K=10
FAR_START={"even-v":16001,"odd-v":16002}

def modes_for(sector):
    return np.arange(1 if sector=="even-v" else 2,N+1,2,dtype=int)

def psum_bound(n0,p):
    # same-parity sum n^-p
    n=mp.mpf(n0)
    return n**(-p)+n**(-(p-1))/(2*(p-1))

def scales(sector):
    n0=FAR_START[sector]
    with mp.workdps(DPS):
        out=[]
        names=[]
        for j in range(K+1):
            sa=8*mp.sqrt(psum_bound(n0,4*j+4))
            sb=mp.sqrt(psum_bound(n0,4*j+2))
            out.extend([sa,sb])
            names.extend([f"a{j}: z/n^{2*j+2}",f"b{j}: 1/n^{2*j+1}"])
        g=mp.cosh(mp.mpf(".5")) if sector=="even-v" else mp.sinh(mp.mpf(".5"))
        alpha=mp.mpf(2 if sector=="even-v" else -2)
        sp=abs(alpha)*(4*g/mp.pi)*mp.sqrt(psum_bound(n0,2))
        out.append(sp);names.append("pole: alpha*p_n")
        return names,out

def channel_matrix(data,modes,sector,names,ss):
    q=len(ss)
    Bh=np.empty((len(modes),q),dtype=LD)
    Bl=np.empty_like(Bh)
    with mp.workdps(DPS):
        c=mp.mpf(2)/mp.pi
        for i,m0 in enumerate(modes):
            m=mp.mpf(int(m0))
            z=ldd_to_mpf(data.z_hi[i],data.z_lo[i])
            p=ldd_to_mpf(data.pole_hi[i],data.pole_lo[i])
            vals=[]
            for j in range(K+1):
                vals.append(c*m**(2*j+1)*ss[2*j])
                vals.append(-c*z*m**(2*j)*ss[2*j+1])
            vals.append(p*ss[-1])
            for j,v in enumerate(vals):
                Bh[i,j],Bl[i,j]=split_mpf_ld(v)
    return Bh,Bl

def residuals(data,P,Gih,Gil,Xh,Xl,Bh,Bl):
    AXh,AXl=dd_matvec(data,Xh,Xl)
    Rh,Rl=dd_sub(AXh,AXl,Bh,Bl)
    Rh,Rl=dd_project(P,Gih,Gil,Rh,Rl)
    return Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(Bh.shape[1])]

def graph_residuals(data,P,Gih,Gil,Yh,Yl):
    Wh,Wl=dd_sub(P,np.zeros_like(P,dtype=LD),Yh,Yl)
    AWh,AWl=dd_matvec(data,Wh,Wl)
    Rh,Rl=dd_project(P,Gih,Gil,AWh,AWl)
    return Wh,Wl,AWh,AWl,Rh,Rl,[dd_norm2(Rh[:,j],Rl[:,j]) for j in range(6)]

def one_sector(sector):
    modes=modes_for(sector)
    P,_=frozen_protected_basis(sector,modes)
    Gh,Gl=dd_dot_columns(P,None,P,None)
    Gih,Gil,Gi_mp=mp_inverse_split(Gh,Gl,DPS)
    Gi=np.array([[float(Gi_mp[i,j]) for j in range(6)] for i in range(6)])

    data=hp_parity_data(modes,sector,dps=DPS,arch_terms=200,correction_terms=50)
    names,ss=scales(sector)
    Bh,Bl=channel_matrix(data,modes,sector,names,ss)
    Bfloat=np.asarray(Bh+Bl,dtype=float)

    A,_=full_source_matrix(modes,sector)
    op,proj,gamma,evals,Y0,x0,initial=build_double_complement(
        A,P,Gi,Bfloat[:,0],rtol=2e-14
    )
    Yh=Y0.astype(LD);Yl=np.zeros_like(Yh,dtype=LD)
    Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)

    Xh=np.empty_like(Bh);Xl=np.zeros_like(Bl)
    for j in range(Bh.shape[1]):
        if j==0:
            x=x0
        else:
            x=solve_correction(op,proj,proj(Bfloat[:,j]),rtol=2e-14)
        Xh[:,j]=np.asarray(x,dtype=LD)
    Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    hist=[]
    for step in range(2):
        Wh,Wl,AWh,AWl,RYh,RYl,ny=graph_residuals(
            data,P,Gih,Gil,Yh,Yl
        )
        RXh,RXl,nx=residuals(data,P,Gih,Gil,Xh,Xl,Bh,Bl)
        hist.append({"graph":ny,"targets":nx})
        print(sector,"step",step,"graph",max(ny),"targets",max(nx),flush=True)
        if step==0:
            for j in range(6):
                d=solve_correction(op,proj,RYh[:,j]+RYl[:,j],rtol=2e-14)
                Yh[:,j],Yl[:,j]=dd_add(
                    Yh[:,j],Yl[:,j],d,np.zeros_like(d,dtype=LD)
                )
            for j in range(Bh.shape[1]):
                d=solve_correction(op,proj,-(RXh[:,j]+RXl[:,j]),rtol=2e-14)
                Xh[:,j],Xl[:,j]=dd_add(
                    Xh[:,j],Xl[:,j],d,np.zeros_like(d,dtype=LD)
                )
            Yh,Yl=dd_project(P,Gih,Gil,Yh,Yl)
            Xh,Xl=dd_project(P,Gih,Gil,Xh,Xl)

    Wh,Wl,AWh,AWl,RYh,RYl,ny=graph_residuals(data,P,Gih,Gil,Yh,Yl)
    RXh,RXl,nx=residuals(data,P,Gih,Gil,Xh,Xl,Bh,Bl)
    Sh,Sl=dd_dot_columns(Wh,Wl,AWh,AWl)
    gh,gl=dd_dot_columns(Wh,Wl,Bh,Bl)
    hh,hl=dd_dot_columns(Bh,Bl,Xh,Xl)

    with mp.workdps(DPS):
        S=dd_matrix_to_mp(Sh,Sl);S=(S+S.T)/2
        g=dd_matrix_to_mp(gh,gl)
        h=dd_matrix_to_mp(hh,hl);h=(h+h.T)/2
        Sinvg=mp.matrix(6,len(ss))
        for j in range(len(ss)):
            sol=mp.lu_solve(S,g[:,j])
            for i in range(6): Sinvg[i,j]=sol[i]
        M=h+g.T*Sinvg;M=(M+M.T)/2
        vals,_=mp.eigsy(M)
        maxabs=max(abs(M[i,j]) for i in range(len(ss)) for j in range(len(ss)))
        trace=mp.fsum(M[i,i] for i in range(len(ss)))

    row={
      "sector":sector,"dimension":len(modes),"far_start":FAR_START[sector],
      "channel_names":names,
      "scales":[mp.nstr(s,50) for s in ss],
      "complement_floor_midpoint":gamma,
      "max_graph_residual":max(ny),"max_target_residual":max(nx),
      "M_scaled_eigenvalues":[mp.nstr(vals[i],50) for i in range(len(ss))],
      "M_scaled_trace":mp.nstr(trace,60),
      "M_scaled_max_abs_entry":mp.nstr(maxabs,60),
      "M_scaled":[[mp.nstr(M[i,j],50) for j in range(len(ss))] for i in range(len(ss))],
      "guardrail":"Arch200 midpoint scaled Gram; outward target pending."
    }
    print(sector,"trace",row["M_scaled_trace"],"maxabs",row["M_scaled_max_abs_entry"],flush=True)
    return row

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sector",choices=["even-v","odd-v"],required=True)
    a=ap.parse_args()
    row=one_sector(a.sector)
    OUT.write_text(json.dumps({"rows":[row]},indent=2,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
