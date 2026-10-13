#!/usr/bin/env python3
"""Remove the artificial Hankel self term before adding the raw diagonal."""
from fractions import Fraction as F
def compensate_self(point,c,z_output,z_input,x,reciprocal_self):
 return point+c*(z_output+z_input)*reciprocal_self*x/2
def verify():
 checked=0
 for start in (1,2):
  for m in (3,6,9):
   x=[F((-1)**j*(j+2),17) for j in range(m)]
   z=[F(j-4,5) for j in range(m)];c=F(2,3)
   for i in range(m+3):
    n=2*i+start;zo=F(i+3,7)
    T=lambda j: F(0) if i==j else F(1,2*(i-j))
    H=lambda j: F(1,2*(i+j+start))
    u=sum((T(j)+H(j))*z[j]*x[j] for j in range(m))
    v=sum((T(j)-H(j))*x[j] for j in range(m))
    point=c*(zo*v-u)/2
    if i<m:point=compensate_self(point,c,zo,z[i],x[i],H(i))
    direct=sum(c*F(zo*(2*j+start)-n*z[j],n*n-(2*j+start)**2)*x[j] for j in range(m) if i!=j)
    assert point==direct;checked+=1
 return checked
if __name__=='__main__':
 print({'exact_original_offdiagonal_kernel_rows_verified':verify(),'both_parities':True,'overlapping_and_disjoint_outputs':True})
