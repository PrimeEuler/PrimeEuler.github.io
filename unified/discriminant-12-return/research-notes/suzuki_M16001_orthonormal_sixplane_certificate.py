#!/usr/bin/env python3
"""Rigorous 6x6 Gram/Cholesky certificate for the frozen M16001 six-plane P.

P is reconstructed exactly from Q,L0.  G=P^T P and LDL pivots are exact
Fractions.  Cholesky R, R^{-1}, and P_perp=P R^{-1} are outward Decimal
intervals.  The certificate also combines P_perp with the independently
constructed N_perp and checks the complete 10x10 orthonormal basis.
"""
from fractions import Fraction
from pathlib import Path
import hashlib,json
from suzuki_M16001_exact_basis_certificate import Q_HEX,L0_HEX,fhex,lower_solve
from suzuki_M16001_orthonormal_nullspace_certificate import (
    PREC,I,Z,O,isum,ldl_pivots,inv_upper,matmul,transpose,fracI,
    exact_Q_N,chol_upper
)
OUT=Path(__file__).with_name("certificates"); OUT.mkdir(exist_ok=True)

def gram(A):
    return [[sum(A[r][i]*A[r][j] for r in range(len(A))) for j in range(len(A[0]))] for i in range(len(A[0]))]

def payload(name,A):
    lines=["M16001-DECIMAL-INTERVAL-MATRIX-v1",f"name={name}",f"precision={PREC}",f"rows={len(A)}",f"cols={len(A[0])}"]
    lines += [",".join(f"[{x.lo},{x.hi}]" for x in row) for row in A]
    return "\n".join(lines)+"\n"
def write_payload(name,A):
    txt=payload(name,A); p=OUT/f"M16001_{name}.interval"; p.write_text(txt,encoding="ascii",newline="\n")
    return p.name,hashlib.sha256(txt.encode("ascii")).hexdigest()

def main():
    Q=[[fhex(x) for x in r] for r in Q_HEX]; L=[[fhex(x) for x in r] for r in L0_HEX]
    P=[lower_solve(L,r) for r in Q]
    assert all(sum(P[r][k]*L[c][k] for k in range(6))==Q[r][c] for r in range(10) for c in range(6))
    G=gram(P); piv=ldl_pivots(G); assert all(x>0 for x in piv)
    R=chol_upper(G); U=inv_upper(R); Pp=matmul(fracI(P),U)
    RtR=matmul(transpose(R),R); RU=matmul(R,U); PtP=matmul(transpose(Pp),Pp)
    assert all((RtR[i][j]-I.frac(G[i][j])).contains0() for i in range(6) for j in range(6))
    assert all((RU[i][j]-(O if i==j else Z)).contains0() for i in range(6) for j in range(6))
    assert all((PtP[i][j]-(O if i==j else Z)).contains0() for i in range(6) for j in range(6))
    # Reconstruct N_perp independently using the corrected 4x4 interval path.
    Q2,N0=exact_Q_N(); GN=gram(N0); RN=chol_upper(GN); UN=inv_upper(RN); Np=matmul(fracI(N0),UN)
    cross=matmul(transpose(Pp),Np)
    assert all(cross[i][j].contains0() for i in range(6) for j in range(4))
    B=[Pp[r]+Np[r] for r in range(10)]; BtB=matmul(transpose(B),B)
    assert all((BtB[i][j]-(O if i==j else Z)).contains0() for i in range(10) for j in range(10))
    exact_gram="\n".join(f"{x.numerator}/{x.denominator}" for row in G for x in row)+"\n"
    gsha=hashlib.sha256(exact_gram.encode("ascii")).hexdigest()
    files={}
    for name,A in [("P_Gram_exact_interval",fracI(G)),("P_Cholesky_R",R),("P_Cholesky_Rinv",U),("P_perp",Pp),("B_perp",B)]:
        fn,h=write_payload(name,A); files[name]={"file":fn,"sha256":h,"shape":[len(A),len(A[0])]}
    cert={"schema":"m16001.orthonormal_sixplane.v1","precision":PREC,"G_P_exact_sha256":gsha,
          "ldl_pivots":[{"num":str(x.numerator),"den":str(x.denominator)} for x in piv],
          "payloads":files,
          "checks":{"G_P_exact_spd":True,"RtR_contains_G_P":True,"R_Rinv_contains_I6":True,
                    "PperpT_Pperp_contains_I6":True,"PperpT_Nperp_contains_zero":True,
                    "BperpT_Bperp_contains_I10":True},
          "max_width":{"R_P":str(max(x.width() for row in R for x in row)),
                       "R_P_inv":str(max(x.width() for row in U for x in row)),
                       "P_perp":str(max(x.width() for row in Pp for x in row)),
                       "B_perp":str(max(x.width() for row in B for x in row))}}
    cp=OUT/"M16001_orthonormal_sixplane_certificate.json"
    cert_txt=json.dumps(cert,indent=2,sort_keys=True)+"\\n"
    cp.write_text(cert_txt,encoding="ascii")
    cert_sha=hashlib.sha256(cert_txt.encode("ascii")).hexdigest()
    print("M16001 orthonormal six-plane certificate")
    print("exact G_P=P^T P SPD             PASS")
    print("R_P^T R_P contains exact G_P    PASS")
    print("R_P R_P^{-1} contains I6        PASS")
    print("P_perp^T P_perp contains I6     PASS")
    print("P_perp^T N_perp contains 0       PASS")
    print("B_perp^T B_perp contains I10     PASS")
    print("G_P exact SHA-256 =",gsha)
    for i,x in enumerate(piv,1): print(f"LDL pivot {i} = {x.numerator}/{x.denominator}")
    for k,v in cert["max_width"].items(): print("max interval width",k,"=",v)
    for k,v in files.items(): print(k,"SHA-256 =",v["sha256"])
    print("certificate =",cp)
    print("certificate JSON SHA-256 =",cert_sha)
    print("ORTHONORMAL SIX-PLANE CERTIFICATE: PASS")
if __name__=="__main__": main()
