#!/usr/bin/env python3
"""v15.928: q=2 weighted null-shell maps: exact raising covariance.
Geometric maps, not a derived physical EM or gravitational dipole.
Confirmed with SymPy in current container on L=2..40; independent
linear nullspaces and two-sided no-go checked L=2..10.
"""
import sympy as s

def J(L):
    z=s.zeros(L+1)
    for i in range(L-1):
        z[i+2,i]=s.sqrt(s.Rational((L-i)*(i+2),4))
    return z

def weighted(L,kind,seed):
    c=[s.Integer(0)]*(L+1)
    c[seed]=s.Integer(1)
    for i in range(seed,L-1,2):
        ratio=(s.Rational(L+1-i,L-i) if kind=='A'
               else s.Rational(i+3,i+2))
        c[i+2]=s.simplify(c[i]*s.sqrt(ratio))
    U=s.zeros(L+2,L+1)
    for i,v in enumerate(c):
        U[i+int(kind=='B'),i]=v
    return U

for L in range(2,41):
    src,tgt=J(L),J(L+1)
    M=s.diag(*[-s.Rational(L,4)+s.Rational(i,2)
               for i in range(L+1)])
    Mp=s.diag(*[-s.Rational(L+1,4)+s.Rational(i,2)
                for i in range(L+2)])
    for U,q in [(weighted(L,'A',L%2),-s.Rational(1,4)),
                (weighted(L,'B',0),s.Rational(1,4)),
                (weighted(L,'B',1),s.Rational(1,4))]:
        assert U!=s.zeros(L+2,L+1)
        assert tgt*U==U*src
        assert Mp*U-U*M==q*U
        assert tgt.T*U!=U*src.T
for L in range(2,11):
    src,tgt=J(L),J(L+1)
    for shift,dim in [(0,1),(1,2)]:
        cs=s.symbols('c:'+str(L+1))
        U=s.zeros(L+2,L+1)
        for i,v in enumerate(cs): U[i+shift,i]=v
        first=list(tgt*U-U*src)
        assert len(s.linear_eq_to_matrix(first,cs)[0].nullspace())==dim
        both=first+list(tgt.T*U-U*src.T)
        assert len(s.linear_eq_to_matrix(both,cs)[0].nullspace())==0
print('PASS: 39 q=2 shells, 3 raising-compatible families, full two-sided obstruction')
