#!/usr/bin/env python3
"""Rigorous 4x4 Gram/Cholesky certificate for the exact M16001 nullspace N0.

Uses exact Fraction arithmetic for G=N0^T N0 and exact LDL pivots.  Irrational
Cholesky, inverse, and N_perp=N0 R^{-1} are enclosed by Decimal interval
arithmetic with directed rounding.  No numpy/scipy linear algebra is used.
"""
from __future__ import annotations
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
import hashlib, json
from pathlib import Path
from suzuki_M16001_exact_basis_certificate import (
    Q_HEX, L0_HEX, fhex, solve, det
)

PREC=120
OUT=Path(__file__).with_name("certificates")
OUT.mkdir(exist_ok=True)

def exact_Q_N():
    Q=[[fhex(x) for x in r] for r in Q_HEX]
    A=[[Q[col][row] for col in range(6)] for row in range(6)]
    C=[[Q[col][row] for col in range(6,10)] for row in range(6)]
    assert det(A)
    N=[[Fraction(0) for _ in range(4)] for _ in range(10)]
    for t in range(4):
        x=solve(A,[-C[r][t] for r in range(6)])
        for r in range(6): N[r][t]=x[r]
        N[6+t][t]=1
    assert all(sum(Q[r][c]*N[r][t] for r in range(10))==0 for c in range(6) for t in range(4))
    return Q,N

def gram(N):
    return [[sum(N[r][i]*N[r][j] for r in range(10)) for j in range(4)] for i in range(4)]

def ldl_pivots(A):
    n=len(A); L=[[Fraction(0) for _ in range(n)] for _ in range(n)]; D=[]
    for i in range(n):
        L[i][i]=1
        d=A[i][i]-sum(L[i][k]*L[i][k]*D[k] for k in range(i))
        D.append(d)
        for j in range(i+1,n):
            L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/d
    return D

def dec_frac(x, rounding):
    with localcontext() as c:
        c.prec=PREC; c.rounding=rounding
        return Decimal(x.numerator)/Decimal(x.denominator)

class I:
    __slots__=("lo","hi")
    def __init__(self,lo,hi=None): self.lo=lo; self.hi=lo if hi is None else hi
    @staticmethod
    def frac(x): return I(dec_frac(x,ROUND_FLOOR),dec_frac(x,ROUND_CEILING))
    def __add__(a,b):
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_FLOOR; lo=a.lo+b.lo
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING; hi=a.hi+b.hi
        return I(lo,hi)
    def __neg__(a): return I(a.hi.copy_negate(),a.lo.copy_negate())
    def __sub__(a,b): return a+(-b)
    def __mul__(a,b):
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_FLOOR
            lo=min(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING
            hi=max(a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi)
        return I(lo,hi)
    def __truediv__(a,b):
        assert not (b.lo<=0<=b.hi)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_FLOOR
            vals=[a.lo/b.lo,a.lo/b.hi,a.hi/b.lo,a.hi/b.hi]; lo=min(vals)
        with localcontext() as c:
            c.prec=PREC; c.rounding=ROUND_CEILING
            vals=[a.lo/b.lo,a.lo/b.hi,a.hi/b.lo,a.hi/b.hi]; hi=max(vals)
        return I(lo,hi)
    def sqrt(a):
        assert a.lo>0
        # Decimal.sqrt() as a bound must use the explicit local Context.
        # Step one representable value outward so containment is independent
        # of the square-root implementation's correctly-rounded midpoint.
        with localcontext() as c:
            c.prec=PREC
            lo=c.next_minus(c.sqrt(a.lo))
            hi=c.next_plus(c.sqrt(a.hi))
        return I(lo,hi)
    def contains0(a): return a.lo<=0<=a.hi
    def width(a): return a.hi-a.lo

Z=I(Decimal(0)); O=I(Decimal(1))
def isum(xs):
    s=Z
    for x in xs: s=s+x
    return s

def chol_upper(G):
    # lower Cholesky first: G=L L^T; R=L^T.
    n=4; L=[[Z for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            s=isum(L[i][k]*L[j][k] for k in range(j))
            t=I.frac(G[i][j])-s
            L[i][j]=t.sqrt() if i==j else t/L[j][j]
    return [[L[j][i] if j>=i else Z for j in range(n)] for i in range(n)]

def inv_upper(R):
    n=len(R); U=[[Z for _ in range(n)] for _ in range(n)]
    for col in range(n):
        for i in range(n-1,-1,-1):
            rhs=(O if i==col else Z)-isum(R[i][k]*U[k][col] for k in range(i+1,n))
            U[i][col]=rhs/R[i][i]
    return U

def matmul(A,B):
    return [[isum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A): return [list(x) for x in zip(*A)]
def fracI(A): return [[I.frac(x) for x in row] for row in A]

def payload(name,A):
    lines=["M16001-DECIMAL-INTERVAL-MATRIX-v1",f"name={name}",f"precision={PREC}",f"rows={len(A)}",f"cols={len(A[0])}"]
    lines += [",".join(f"[{x.lo},{x.hi}]" for x in row) for row in A]
    return "\n".join(lines)+"\n"

def write_payload(name,A):
    p=OUT/f"M16001_{name}.interval"
    txt=payload(name,A); p.write_text(txt,encoding="ascii",newline="\n")
    return p.name,hashlib.sha256(txt.encode("ascii")).hexdigest()

def main():
    Q,N0=exact_Q_N(); G=gram(N0); piv=ldl_pivots(G)
    assert all(x>0 for x in piv)
    R=chol_upper(G); U=inv_upper(R)
    Np=matmul(fracI(N0),U)
    RtR=matmul(transpose(R),R)
    RU=matmul(R,U)
    QtNp=matmul(transpose(fracI(Q)),Np)
    NtN=matmul(transpose(Np),Np)
    assert all((RtR[i][j]-I.frac(G[i][j])).contains0() for i in range(4) for j in range(4))
    assert all((RU[i][j]-(O if i==j else Z)).contains0() for i in range(4) for j in range(4))
    assert all(QtNp[i][j].contains0() for i in range(6) for j in range(4))
    assert all((NtN[i][j]-(O if i==j else Z)).contains0() for i in range(4) for j in range(4))
    files={}
    for name,A in [("N0_Gram_exact_interval",fracI(G)),("N0_Cholesky_R",R),("N0_Cholesky_Rinv",U),("N_perp",Np)]:
        fn,h=write_payload(name,A); files[name]={"file":fn,"sha256":h,"shape":[len(A),len(A[0])]}
    exact_gram_payload="\n".join("/".join((str(x.numerator),str(x.denominator))) for row in G for x in row)+"\n"
    exact_gram_sha=hashlib.sha256(exact_gram_payload.encode("ascii")).hexdigest()
    cert={
      "schema":"m16001.orthonormal_nullspace.v1","decimal_precision":PREC,
      "N0_sha256":"4531629478720802c14e36ae2775644a010b1ee50971d982214f3f5305cbf4d8",
      "G_exact_sha256":exact_gram_sha,
      "ldl_pivots":[{"num":str(x.numerator),"den":str(x.denominator)} for x in piv],
      "payloads":files,
      "checks":{"G_exact_spd":True,"RtR_contains_G":True,"R_Rinv_contains_I4":True,
                "QT_Nperp_contains_zero":True,"NperpT_Nperp_contains_I4":True},
      "max_width":{"R":str(max(x.width() for row in R for x in row)),
                   "Rinv":str(max(x.width() for row in U for x in row)),
                   "Nperp":str(max(x.width() for row in Np for x in row))}
    }
    cp=OUT/"M16001_orthonormal_nullspace_certificate.json"
    cp.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="ascii")
    print("M16001 orthonormal nullspace certificate")
    print("exact G=N0^T N0 SPD             PASS")
    print("R^T R contains exact G          PASS")
    print("R R^{-1} contains I4            PASS")
    print("Q^T N_perp contains 0           PASS")
    print("N_perp^T N_perp contains I4     PASS")
    for k,v in cert["max_width"].items(): print(f"max interval width {k:5s} =",v)
    for k,v in files.items(): print(k,"SHA-256 =",v["sha256"])
    print("certificate =",cp)
    print("ORTHONORMAL NULLSPACE CERTIFICATE: PASS")

if __name__=="__main__": main()
