#!/usr/bin/env python3
"""Gravity v15.1495: unrestricted nonlinear 3D Einstein-H2 GH evolution
through t=.04, actual Fourier-interpolated 2x off-grid constraints,
and RK4 timestep refinement. Not a claim of long-time stability.
Depends only on the Audit-confirmed repaired v15.1485 solver.
"""
from scipy.signal import resample
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial,rk4
import numpy as np

def upsample(y,n):
 out=[]
 for component in y:
  v=component
  for axis in (-3,-2,-1):
   v=resample(v,n,axis=axis)
  out.append(v.real)
 return tuple(out)

def run(N=24,dt=.004,T=.04,offgrid=False):
 grid=GHGrid(N);y=initial(N)
 c0,tt0=grid.rhs(y,True);h0,m0=grid.adm(y)
 for _ in range(round(T/dt)):
  y=rk4(y,dt,grid.rhs)
 C,gtt=grid.rhs(y,True)
 H,M=grid.adm(y)
 result=dict(N=N,dt=dt,T=T,initial_GH=c0,initial_H=h0,initial_M=m0,
             final_GH=C,final_H=H,final_M=M,inv_gtt=gtt)
 assert gtt<0 and np.isfinite(C+H+M)
 if offgrid:
  finer=GHGrid(2*N)
  u=upsample(y,2*N)
  CG,gt=finer.rhs(u,True)
  HG,MG=finer.adm(u)
  assert gt<0
  result.update(offgrid_GH=CG,offgrid_H=HG,offgrid_M=MG,
                offgrid_inv_gtt=gt)
 print(result,flush=True)
 return result
if __name__=="__main__":
 a=run(dt=.004,offgrid=True)
 b=run(dt=.002,offgrid=False)
 assert abs(a["final_H"]-b["final_H"])<1e-12
 assert abs(a["final_M"]-b["final_M"])<1e-12
 assert abs(a["final_GH"]-b["final_GH"])<1e-12
 assert a["offgrid_H"]>2*a["final_H"]
 print("PASS t=.04 real 3D evolution, off-grid and timestep checks")
 print("NEGATIVE no evidence from these checks of a 3D long-time GH constraint certificate")
 print("OPEN N32/N40 t=.04, off-grid and equal-compute temporal refinement; N32 attempt exceeded runtime")
