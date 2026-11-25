#!/usr/bin/env python3
"""v15.1488: fine-resolution nonlinear Einstein-H2 constraint solve
does NOT preserve Einstein/GH constraints when Fourier truncated to
coarse grid; even when reinflated to fine grid. Strict negative.
"""
from scipy.signal import resample
from k4_gh_3d_unrestricted_einstein_h2_fixed_v15_1485 import GHGrid,initial
def resize(a,M):
 for axis in (-3,-2,-1):
  a=resample(a,M,axis=axis)
 return a.real
def test(N):
 coarse=initial(N);fine=initial(2*N)
 down=tuple(resize(x,N) for x in fine)
 up=tuple(resize(x,2*N) for x in down)
 gr0=GHGrid(N);gr1=GHGrid(2*N)
 def monitor(label,grid,y):
  gh,gtt=grid.rhs(y,True);h,m=grid.adm(y)
  print(dict(N=N,case=label,GH=gh,H=h,M=m,inverse_gtt=gtt),flush=True)
  assert gtt<0
  return h,m
 monitor("native",gr0,coarse)
 direct=monitor("direct_fine",gr1,fine)
 truncated=monitor("fine_to_coarse",gr0,down)
 monitor("fine_to_coarse_to_fine",gr1,up)
 assert truncated[1]>1000*direct[1]
if __name__=="__main__":
 for n in (16,24):test(n)
 print("PASS NEGATIVE: projecting fine nonlinear Einstein-H2 Cauchy solution loses constraints")
 print("NEXT solve projected nonlinear constraints in a consistent spectral state space")
