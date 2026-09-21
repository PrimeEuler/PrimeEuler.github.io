#!/usr/bin/env python3
"""Exact normalization test for the frozen M16001 six-plane P=Q L0^{-T}."""
from fractions import Fraction
from suzuki_M16001_exact_basis_certificate import Q_HEX,L0_HEX,fhex,lower_solve

def main():
    Q=[[fhex(x) for x in r] for r in Q_HEX]
    L=[[fhex(x) for x in r] for r in L0_HEX]
    P=[lower_solve(L,r) for r in Q]
    G=[[sum(P[r][i]*P[r][j] for r in range(10)) for j in range(6)] for i in range(6)]
    D=[[G[i][j]-(1 if i==j else 0) for j in range(6)] for i in range(6)]
    exact=all(x==0 for row in D for x in row)
    print("M16001 exact P normalization test")
    print("P^T P == I6 exactly:", "PASS" if exact else "FAIL")
    nz=[(i,j,x) for i,row in enumerate(D) for j,x in enumerate(row) if x]
    print("nonzero entries in P^T P-I6 =",len(nz))
    if nz:
        i,j,x=max(nz,key=lambda t: abs(t[2]))
        print("largest exact discrepancy at",i,j)
        print("numerator =",x.numerator)
        print("denominator =",x.denominator)
        print("decimal approx =",float(x))
    if exact:
        print("P NORMALIZATION GATE: CLOSED")
    else:
        print("P NORMALIZATION GATE: OPEN -- certify six-plane orthonormalization or metric")
if __name__=="__main__": main()
