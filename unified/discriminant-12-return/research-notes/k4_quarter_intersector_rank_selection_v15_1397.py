#!/usr/bin/env python3
"""v15.1397 conditional common-diagonal SU2 EM-quarter tensor-rank
selection. No actual physical inter-sector operator supplied."""
from sympy import Rational
for D in range(2,13):
 j=Rational(D-1,2);J=Rational(2*D-1,2)
 low=[K for K in (0,1,2) if (J-j)<=K<=(J+j) and (J-j-K).is_integer]
 same_center=(2*(J-j)).is_even
 assert same_center==(D%2==0)
 if D==2:assert low==[1,2]
 if D==3:assert low==[]
 if D==4:assert low==[2]
 if D>=5:assert low==[]
 print(dict(D=D,spin_EM=str(j),spin_q2=str(J),min_tensor_rank=str(J-j),
            same_SU2_center=same_center,allowed_low_ranks=low))
print("PASS conditional SU2 common-action selection: rank0 forbidden; rank1 only D2; rank2 D2,D4; odd D incompatible integer-rank operators")
print("OPEN actual common SU2, proper physical carrier and interaction strength")
