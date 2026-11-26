#!/usr/bin/env python3
"""Gravity v15.1505: 32^3 unrestricted nonlinear GH Einstein-H2 evolution
through T=.04: genuine independent 64^3 GH and ADM constraint reconstruction
and checkpointed RK4 half-timestep convergence. Requires Audit-confirmed
fixed v15.1485 GH solver module in the same directory.
Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1:
 python k4_gh3d_offgrid_timestep_v15_1505.py offgrid
 python k4_gh3d_offgrid_timestep_v15_1505.py first --checkpoint /tmp/cone1505.npz
 python k4_gh3d_offgrid_timestep_v15_1505.py second --checkpoint /tmp/cone1505.npz
No physical G-free or Weyl-Maxwell coupling is inferred.
"""
import argparse
from pathlib import Path
import numpy as np
from scipy.signal import resample
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial,rk4

def upsample(y,M):
 output=[]
 for arr in y:
  for axis in (-3,-2,-1):
   arr=resample(arr,M,axis=axis)
  output.append(arr.real)
 return tuple(output)

def fast_harmonic_constraint(grid,state):
 """Independent divergence-of-inverse-metric formula for all four GH components."""
 g,p,_,_=state
 inv=np.moveaxis(np.linalg.inv(np.moveaxis(g,(0,1),(-2,-1))),(-2,-1),(0,1))
 d=np.concatenate((p[None],grid.grad(g)),axis=0)
 C=np.einsum("ma...,nb...,nab...->m...",inv,inv,d,optimize=True)
 trace=np.einsum("ab...,nab...->n...",inv,d,optimize=True)
 C-=.5*np.einsum("mn...,n...->m...",inv,trace,optimize=True)
 return float(np.max(abs(C))),float(np.max(inv[0,0]))

def monitor(grid,y):
 C,tt=fast_harmonic_constraint(grid,y)
 H,M=grid.adm(y)
 assert tt<0 and np.isfinite(C+H+M)
 return dict(GH=C,H=H,M=M,max_inverse_gtt=tt)

def evolve(grid,y,dt,n):
 for _ in range(n):
  y=rk4(y,dt,grid.rhs)
 return y

def offgrid():
 grid=GHGrid(32)
 y=evolve(grid,initial(32),.004,10)
 native=monitor(grid,y)
 high=monitor(GHGrid(64),upsample(y,64))
 print("T=0.04, RK4 dt=0.004, native 32^3:",native,flush=True)
 print("T=0.04, SAME evolved state, independent off-grid 64^3:",high,flush=True)
 assert native["GH"]<3e-12 and high["GH"]<3e-12
 assert high["H"]<2e-10 and high["M"]<8e-11
 return native,high

def first(checkpoint):
 grid=GHGrid(32)
 y=evolve(grid,initial(32),.002,10)
 checkpoint.parent.mkdir(parents=True,exist_ok=True)
 np.savez_compressed(checkpoint,g=y[0],p=y[1],phi=y[2],Pi=y[3])
 result=monitor(grid,y)
 print("CHECKPOINT T=0.02, dt=0.002:",result,"saved",checkpoint,flush=True)
 return result

def second(checkpoint):
 if not checkpoint.is_file():
  raise FileNotFoundError("Run first stage before second with same checkpoint path")
 with np.load(checkpoint) as data:
  y=tuple(data[k].copy() for k in ("g","p","phi","Pi"))
 grid=GHGrid(32)
 y=evolve(grid,y,.002,10)
 result=monitor(grid,y)
 print("CHECKPOINT RESUMED T=0.04, dt=0.002:",result,flush=True)
 baseline=dict(GH=1.7127834828873593e-12,H=1.2621636521310473e-10,
               M=4.1794216010119026e-11)
 differences={key:result[key]-baseline[key] for key in ("GH","H","M")}
 print("dt=0.002 minus dt=0.004 native constraint differences:",differences,flush=True)
 assert abs(differences["GH"])<5e-14
 assert abs(differences["H"])<3e-12
 assert abs(differences["M"])<3e-13
 return result

if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("stage",choices=("offgrid","first","second"))
 p.add_argument("--checkpoint",type=Path,default=Path("/tmp/cone_gh_1505_checkpoint.npz"))
 a=p.parse_args()
 if a.stage=="offgrid":offgrid()
 elif a.stage=="first":first(a.checkpoint)
 else:second(a.checkpoint)
 print("PASS selected verification stage; complete all three stages for gate",flush=True)
