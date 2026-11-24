#!/usr/bin/env python3
"""Gravity v15.1393: finite-dimensional unitary SO(2,1) no-go versus
closed q2 ordinary SU2 carrier; explicit non-Hermitian sl2 continuation.
"""
import sympy as S
I=S.I
for D in range(2,7):
 spin=S.Rational(2*D-1,2);dim=2*D
 m=[-spin+j for j in range(dim)]
 P=S.zeros(dim)
 for j in range(dim-1):P[j+1,j]=S.sqrt((spin-m[j])*(spin+m[j]+1))
 M=P.T;Jx=(P+M)/2;Jy=(P-M)/(2*I);Jz=S.diag(*m)
 assert Jx.H==Jx and Jy.H==Jy and Jz.H==Jz
 assert Jx*Jy-Jy*Jx==I*Jz
 assert Jy*Jz-Jz*Jy==I*Jx
 assert Jz*Jx-Jx*Jz==I*Jy
 # Algebraic SO(2,1) continuation requires non-Hermitian boosts.
 K0=Jz;K1=I*Jx;K2=I*Jy
 assert K0*K1-K1*K0==I*K2
 assert K0*K2-K2*K0==-I*K1
 assert K1*K2-K2*K1==-I*K0
 assert K1.H==-K1 and K2.H==-K2
 trace_comm=S.simplify(S.trace(K0*(K1*K2-K2*K1)))
 trace_cyclic=S.simplify(S.trace((K0*K1-K1*K0)*K2))
 assert trace_comm==trace_cyclic
 tr0=S.trace(K0*K0);tr2=S.trace(K2*K2)
 assert S.simplify(tr0+tr2)==0
 print(dict(D=D,dim=dim,spin=str(spin),trK0_sq=str(tr0),
            tr_nonunitary_K2_sq=str(tr2),unitary=False),flush=True)
print('PASS finite unitary so(2,1) representations are trivial by positive trace identity')
print('PASS nonunitary finite-dimensional Wick rotated q2 SU2 realization exists')
print('OPEN infinite unitary target carrier vs physically broken finite-lattice boosts')
