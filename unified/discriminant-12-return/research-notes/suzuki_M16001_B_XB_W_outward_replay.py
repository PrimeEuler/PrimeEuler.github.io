#!/usr/bin/env python3
"""Frozen M16001 B_perp -> X B_perp -> W_perp outward replay.

Reconstructs the certified B_perp interval exactly as the six-plane checker does,
hash-matches that payload, hash-matches the frozen binary64 X candidate, embeds
every X entry as its exact dyadic Fraction, and propagates interval arithmetic
outward through X*B_perp.  It then freezes midpoint/radius payloads for B_perp,
XB_perp, and W_perp=[B_perp;-XB_perp].
"""
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from pathlib import Path
import hashlib, json
import numpy as np

from suzuki_M16001_exact_basis_certificate import Q_HEX,L0_HEX,fhex,lower_solve
from suzuki_M16001_orthonormal_nullspace_certificate import (
    PREC,I,Z,chol_upper,inv_upper,matmul,fracI,exact_Q_N
)
from suzuki_M16001_orthonormal_sixplane_certificate import gram,payload
from suzuki_M16001_even_index3_anisotropic_tail_split import finite_solve_stop

OUT=Path(__file__).with_name("certificates"); OUT.mkdir(exist_ok=True)
B_EXPECT="630ed6bd2095a0cdf570e12e3092b710fdd337ba31bd6b0ffa813edbfd363b01"
X_EXPECT="800eb3791cbf1cf803243c60954215d6ce7c2082f726c11598df6960dcb6866f"

def sha(b): return hashlib.sha256(b).hexdigest()

def reconstruct_B():
    Q=[[fhex(x) for x in r] for r in Q_HEX]
    L=[[fhex(x) for x in r] for r in L0_HEX]
    P=[lower_solve(L,r) for r in Q]
    G=gram(P); R=chol_upper(G); U=inv_upper(R); Pp=matmul(fracI(P),U)
    _,N0=exact_Q_N(); GN=gram(N0); RN=chol_upper(GN); UN=inv_upper(RN)
    Np=matmul(fracI(N0),UN)
    return [Pp[r]+Np[r] for r in range(10)]

def exact_x_intervals(X):
    return [[I.frac(Fraction.from_float(float(x))) for x in row] for row in X]

def neg(A): return [[-x for x in row] for row in A]

def midrad(x):
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_FLOOR
        mlo=(x.lo+x.hi)/Decimal(2)
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        mhi=(x.lo+x.hi)/Decimal(2)
    # Pick the upper midpoint representation and enlarge radius upward.
    m=mhi
    with localcontext() as c:
        c.prec=PREC; c.rounding=ROUND_CEILING
        r=max(m-x.lo,x.hi-m)
    assert m-r <= x.lo and m+r >= x.hi
    return m,r

def mr_payload(name,A):
    lines=["M16001-DECIMAL-MIDRAD-MATRIX-v1",f"name={name}",f"precision={PREC}",
           f"rows={len(A)}",f"cols={len(A[0])}"]
    maxr=Decimal(0)
    for row in A:
        vals=[]
        for x in row:
            m,r=midrad(x); maxr=max(maxr,r); vals.append(f"[{m},{r}]")
        lines.append(",".join(vals))
    txt="\n".join(lines)+"\n"
    return txt,maxr

def write_mr(name,A):
    txt,maxr=mr_payload(name,A)
    p=OUT/f"M16001_{name}.midrad"
    p.write_text(txt,encoding="ascii",newline="\n")
    return {"file":p.name,"sha256":sha(txt.encode("ascii")),
            "shape":[len(A),len(A[0])],"max_radius":str(maxr)}

def main():
    B=reconstruct_B()
    btxt=payload("B_perp",B).encode("ascii"); bsha=sha(btxt)
    assert bsha==B_EXPECT,(bsha,B_EXPECT)

    _,_,_,X,_=finite_solve_stop()
    X=np.ascontiguousarray(np.asarray(X,dtype=np.float64))
    xsha=sha(X.view(np.uint8))
    assert xsha==X_EXPECT,(xsha,X_EXPECT)
    assert X.shape==(7991,10) and np.all(np.isfinite(X))

    XI=exact_x_intervals(X)
    XB=matmul(XI,B)
    W=B+neg(XB)
    assert len(XB)==7991 and len(XB[0])==10
    assert len(W)==8001 and len(W[0])==10

    # Structural containment checks: top W block is B exactly; bottom is -XB.
    assert all(W[i][j].lo==B[i][j].lo and W[i][j].hi==B[i][j].hi
               for i in range(10) for j in range(10))
    assert all(W[i+10][j].lo==(-XB[i][j]).lo and W[i+10][j].hi==(-XB[i][j]).hi
               for i in range(7991) for j in range(10))

    files={}
    for name,A in [("B_perp_frozen",B),("XB_perp",XB),("W_perp",W)]:
        files[name]=write_mr(name,A)

    cert={
      "schema":"m16001.B_XB_W_outward_replay.v1",
      "precision":PREC,
      "input_hashes":{"B_perp_interval_sha256":bsha,"X_binary64_sha256":xsha},
      "shapes":{"B_perp":[10,10],"X":[7991,10],"XB_perp":[7991,10],"W_perp":[8001,10]},
      "payloads":files,
      "checks":{"B_hash_match":True,"X_hash_match":True,"X_exact_dyadic_embedding":True,
                "XB_outward_interval_matmul":True,"W_top_equals_B":True,
                "W_bottom_equals_minus_XB":True,"midrad_encloses_intervals":True}
    }
    txt=json.dumps(cert,indent=2,sort_keys=True)+"\n"
    cp=OUT/"M16001_B_XB_W_outward_replay_certificate.json"
    cp.write_text(txt,encoding="ascii",newline="\n")
    csha=sha(txt.encode("ascii"))

    print("M16001 frozen B_perp -> X B_perp -> W_perp replay")
    print("B_perp interval SHA-256 =",bsha)
    print("X binary64 SHA-256 =",xsha)
    print("B hash match                       PASS")
    print("X hash match                       PASS")
    print("X exact dyadic embedding           PASS")
    print("XB outward interval matmul         PASS")
    print("W top block equals B_perp          PASS")
    print("W bottom block equals -XB_perp     PASS")
    print("midpoint/radius enclosure          PASS")
    for k,v in files.items():
        print(k,"shape =",tuple(v["shape"]))
        print(k,"midrad SHA-256 =",v["sha256"])
        print(k,"max radius =",v["max_radius"])
    print("certificate JSON SHA-256 =",csha)
    print("FROZEN B_XB_W REPLAY: PASS")

if __name__=="__main__": main()
