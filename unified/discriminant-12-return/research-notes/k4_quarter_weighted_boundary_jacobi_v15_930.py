#!/usr/bin/env python3
"""v15.930: exact boundary-defect Jacobi anomaly for weighted null shifts.
Reproduces earlier quarter-grid q=2 defective J; all statements
mathematical only, not SO(3) tensors or derived field couplings.
"""
import sympy as s

def family(L):
    j=s.Rational(L,4)
    m=s.diag(*[-j+s.Rational(i,2) for i in range(L+1)])
    jp=s.zeros(L+1)
    for i in range(L-1):
        jp[i+2,i]=s.sqrt(s.Rational((L-i)*(i+2),4))
    d=jp*jp.T-jp.T*jp-2*m
    return jp,m,d

def shift(L,kind,seed):
    coeff=[s.Integer(0)]*(L+1)
    coeff[seed]=s.Integer(1)
    for i in range(seed,L-1,2):
        ratio=(s.Rational(L+1-i,L-i) if kind=='A' else s.Rational(i+3,i+2))
        coeff[i+2]=s.simplify(coeff[i]*s.sqrt(ratio))
    U=s.zeros(L+2,L+1)
    for i,c in enumerate(coeff): U[i+(kind=='B'),i]=c
    return U

for L in range(2,26):
    J,M,D=family(L)
    K,Mp,Dp=family(L+1)
    solutions=[('A',L%2),('B',0),('B',1)]
    for kind,seed in solutions:
        U=shift(L,kind,seed)
        q=s.Rational(-1 if kind=='A' else 1,4)
        assert K*U==U*J
        assert Mp*U-U*M==q*U
        lower=K.T*U-U*J.T
        boundary=Dp*U-U*D
        assert K*lower-lower*J==2*q*U+boundary
        assert boundary!=s.zeros(L+2,L+1)
        assert boundary.rank()<=2
        original_defect_sites={i for i in range(L+1) if D[i,i]!=0}
        target_defect_sites={i for i in range(L+2) if Dp[i,i]!=0}
        for row in range(L+2):
            for col in range(L+1):
                if boundary[row,col]!=0:
                    assert row in target_defect_sites or col in original_defect_sites
        assert Mp*lower-lower*M==(q-s.Integer(1))*lower
    C=[shift(L,*x) for x in solutions]
    Bs=[Dp*U-U*D for U in C]
    t=s.symbols('t0:3')
    Bsum=sum((t[i]*Bs[i] for i in range(3)),s.zeros(L+2,L+1))
    coeff=s.linear_eq_to_matrix(list(Bsum),t)[0]
    assert coeff.rank()==3
    if L in (2,3,4,5,7,12,25):
        print('L',L,'boundary ranks',[b.rank() for b in Bs],
              'combined rank',coeff.rank(),
              'D sites',[i for i in range(L+1) if D[i,i]!=0])
print('PASS: L=2..25 Jacobi identity, low-rank boundary anomaly, no constant-mix cancellation')
