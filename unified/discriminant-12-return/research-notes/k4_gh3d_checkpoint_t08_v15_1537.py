#!/usr/bin/env python3
"""v15.1537: checkpointed unrestricted GH Einstein-H2 evolution to .08.
Run four times with --steps 5, using the same fresh checkpoint path.
Use OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1.
After step 20 run with --steps 0 --offgrid for independent 64^3 monitors.
"""
import argparse
from pathlib import Path
import numpy as np
from scipy.signal import resample
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial,rk4

def monitor(grid,y):
 g,p,_,_=y
 inv=np.moveaxis(np.linalg.inv(np.moveaxis(g,(0,1),(-2,-1))),(-2,-1),(0,1))
 d=np.concatenate((p[None],grid.grad(g)),axis=0)
 C=np.einsum('ma...,nb...,nab...->m...',inv,inv,d,optimize=True)
 trace=np.einsum('ab...,nab...->n...',inv,d,optimize=True)
 C-=.5*np.einsum('mn...,n...->m...',inv,trace,optimize=True)
 H,M=grid.adm(y)
 tt=float(np.max(inv[0,0]))
 assert tt<0
 return dict(GH=float(np.max(abs(C))),H=H,M=M,gtt=tt)

def upsample(y,N):
 out=[]
 for a in y:
  for axis in (-3,-2,-1):a=resample(a,N,axis=axis)
  out.append(a.real)
 return tuple(out)

if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--N',type=int,default=32)
 p.add_argument('--steps',type=int,default=5)
 p.add_argument('--path',type=Path,default=Path('gate1537_state.npz'))
 p.add_argument('--offgrid',action='store_true')
 a=p.parse_args()
 grid=GHGrid(a.N)
 if a.path.exists():
  with np.load(a.path) as f:
   assert int(f['N'])==a.N
   start=int(f['step'])
   y=tuple(f[k].copy() for k in ('g','p','phi','Pi'))
 else:
  start=0
  y=initial(a.N)
 for i in range(start,start+a.steps):
  y=rk4(y,.004,grid.rhs)
  tmp=a.path.with_suffix('.tmp.npz')
  np.savez(tmp,N=a.N,step=i+1,g=y[0],p=y[1],phi=y[2],Pi=y[3])
  tmp.replace(a.path)
  print('saved',i+1,flush=True)
 print('time',.004*(start+a.steps),'native',monitor(grid,y),flush=True)
 if a.offgrid:
  print('offgrid',monitor(GHGrid(2*a.N),upsample(y,2*a.N)),flush=True)
