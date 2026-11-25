#!/usr/bin/env python3
"""v15.1483: two-thirds FFT-filter negative-control for unrestricted GH Einstein-H2.
Run beside committed k4_gh_3d_unrestricted_einstein_h2_v15_1481.py.
Tests five filtering strategies and independent physical and harmonic constraints.
"""
import numpy as np
from k4_gh_3d_unrestricted_einstein_h2_v15_1481 import GHGrid,initial,rk4
def cut(a,N):
 k=np.fft.fftfreq(N,d=1/N)
 X,Y,Z=np.meshgrid(k,k,k,indexing="ij")
 keep=(abs(X)<=N/3)&(abs(Y)<=N/3)&(abs(Z)<=N/3)
 return np.fft.ifftn(np.fft.fftn(a,axes=(-3,-2,-1))*keep,axes=(-3,-2,-1)).real
def run(N):
 gr=GHGrid(N);base=initial(N);rows={}
 for mode in ("native","filter_initial","filter_each_step","filter_rhs_all","filter_rhs_accelerations"):
  y=tuple(cut(v,N) for v in base) if mode in ("filter_initial","filter_each_step") else base
  h0,m0=gr.adm(y);c0=gr.rhs(y,True)[0]
  def rhs(z):
   result=gr.rhs(z)
   if mode=="filter_rhs_all":return tuple(cut(v,N) for v in result)
   if mode=="filter_rhs_accelerations":return tuple(cut(v,N) if i in (1,3) else v for i,v in enumerate(result))
   return result
  for _ in range(4):
   y=rk4(y,.004,rhs)
   if mode=="filter_each_step":y=tuple(cut(v,N) for v in y)
  h,m=gr.adm(y);c=gr.rhs(y,True)[0]
  rows[mode]=dict(initial_H=h0,initial_M=m0,initial_GH=c0,final_H=h,final_M=m,final_GH=c)
  print("N",N,mode,rows[mode],flush=True)
 assert rows["filter_initial"]["initial_M"]>1000*rows["native"]["initial_M"]
 assert rows["filter_each_step"]["final_M"]>10*rows["native"]["final_M"]
 return rows
if __name__=="__main__":
 run(16);run(24)
 print("PASS NEGATIVE: filtering full GH Einstein-H2 state damages the momentum constraint")
 print("OPEN consistent dealiasing of products and postfilter elliptic re-projection")
