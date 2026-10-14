#!/usr/bin/env python3
"""Exact rectangular channels for a finite component at any global offset.

Allows disjoint compact components/chunks to retain their own dyadic scale,
instead of padding a million-coordinate vector to the front lift's scale.
"""
from fractions import Fraction as F
from suzuki_exact_integer_source_action import convolution
from suzuki_compact_action_self_diagonal import compensate_self
def channels(x,zx,start,input_offset,first,count,bits=256):
 m=len(x);assert len(zx)==m and m>0 and first>=0 and count>0 and input_offset>=0
 scale=1<<bits;last=first+count-1;shift=input_offset+m-1
 h=[0 if q==shift else scale//(2*(q-shift)) for q in range(last+m)]
 g=[scale//(2*(q+input_offset+start)) for q in range(last+m)]
 tx=convolution(x,h,first+m-1,count);tz=convolution(zx,h,first+m-1,count)
 hx=convolution(x[::-1],g,first+m-1,count);hz=convolution(zx[::-1],g,first+m-1,count)
 return [a+b for a,b in zip(tz,hz)],[a-b for a,b in zip(tx,hx)]
def verify():
 checked=0;bits=18;scale=1<<bits;c=F(2,3)
 for start in (1,2):
  for m in (3,6,9):
   for offset in (0,7,14):
    for first in (0,m,2*m):
     x=[(-1)**j*(j+2) for j in range(m)];z=[j-4 for j in range(m)];u,v=channels(x,[a*b for a,b in zip(x,z)],start,offset,first,m+3,bits)
     for r,i in enumerate(range(first,first+m+3)):
      n=2*i+start;zo=F(i+3,7);point=c*(zo*F(v[r],scale)-F(u[r],scale))/2
      if offset<=i<offset+m:point=compensate_self(point,c,zo,z[i-offset],x[i-offset],F(scale//(2*n),scale))
      direct=sum(c*(zo*(2*(offset+j)+start)-n*z[j])*x[j]/(n*n-(2*(offset+j)+start)**2) for j in range(m) if i!=offset+j)
      assert abs(point-direct)<=F(50,scale)*sum(abs(a) for a in x);checked+=1
 return checked
if __name__=='__main__':print({'independent_original_physical_kernel_rows_verified':verify(),'includes_before_inside_after_support':True,'both_parities':True})
