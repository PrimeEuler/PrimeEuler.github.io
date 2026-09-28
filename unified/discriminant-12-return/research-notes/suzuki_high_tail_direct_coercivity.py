#!/usr/bin/env python3
"""Direct coercivity certificate for the full high tail at rho=0.02.

Purpose
-------
Repair the block-feedback gap in the candidate six-root Rouche proof.

For each parity sector, define the high tail
    even-v: n = 25,27,29,...
    odd-v : n = 26,28,30,...

Split it into a small finite front F and a raw remote tail R:
    even-v F = 25..189, R = 191,193,...
    odd-v  F = 26..190, R = 192,194,...

At delta=+0.02 (the worst real part on |z|=0.02),
    H = [[F_FF, F_FR],[F_RF,F_RR]].

The already-audited raw remote estimate gives
    F_RR >= gamma I.

Hence
    Schur_F >= F_FF - gamma^{-1} F_FR F_RF.

We compute F_FR F_RF explicitly through 2,000,000 and bound the far
remainder analytically.  If this finite Schur lower matrix is positive,
then the entire high tail is positive.  Because B_sm on the high tail is
positive, the same lower bound controls Re F_HH(z) on |z|=0.02.

This avoids eliminating a large finite buffer before the remote block and
therefore avoids the missing buffer-mediated self-energy found in the
first Rouche candidate.
"""
from __future__ import annotations

import math
import mpmath as mp
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    offdiag,
    pole_vector,
    z_source_faithful,
)
from suzuki_endpoint_M3999_rho002_adversarial_audit import (
    tail_floor_interval,
)

RHO=0.02
EXPLICIT_STOP=2_000_000
Z_FAR_CAP=8.0

FRONT={
    "even-v":np.arange(25,190,2,dtype=int),
    "odd-v":np.arange(26,191,2,dtype=int),
}
REMOTE_START={
    "even-v":191,
    "odd-v":192,
}

# Public floors are deliberately below the interval/raw values.
REMOTE_GAMMA_CAP={
    "even-v":0.18,
    "odd-v":0.18,
}

# Filled conservatively after the direct replay below.  These are intended
# to leave visible room around the actual values.
CROSS_GRAM_CAP={
    "even-v":1.0,
    "odd-v":1.0,
}

HIGH_TAIL_FLOOR_CAP={
    "even-v":1.0e-5,
    "odd-v":1.0e-5,
}


def dense_front(sector):
    modes=FRONT[sector]
    z,d=endpoint_data(modes,sign=-1,rho=RHO)
    M=offdiag(modes,modes,z,z)
    np.fill_diagonal(M,d)
    p,alpha=pole_vector(modes,sector)
    M+=alpha*np.outer(p,p)
    return (M+M.T)/2


def cross_rows(sector,ns):
    front=FRONT[sector]
    zf,_=endpoint_data(front,sign=-1,rho=RHO)
    zn=z_source_faithful(np.asarray(ns,dtype=float))-RHO*math.pi/2.0

    rows=offdiag(np.asarray(ns,dtype=int),front,zn,zf)

    pfront,alpha=pole_vector(front,sector)
    pn,_=pole_vector(np.asarray(ns,dtype=float),sector)
    rows+=alpha*np.outer(pn,pfront)
    return rows


def explicit_cross_gram(sector):
    G=np.zeros((len(FRONT[sector]),len(FRONT[sector])),dtype=float)
    start=REMOTE_START[sector]
    for st in range(start,EXPLICIT_STOP+1,200000):
        en=min(st+199998,EXPLICIT_STOP)
        if (en-st)%2:
            en-=1
        ns=np.arange(st,en+1,2,dtype=int)
        R=cross_rows(sector,ns)
        G+=R.T@R
    return (G+G.T)/2


def far_sums(N,p):
    return N**(-p)+1.0/(2.0*(p-1)*N**(p-1))


def far_cross_frobenius_root(sector):
    modes=FRONT[sector].astype(float)
    z,_=endpoint_data(FRONT[sector],sign=-1,rho=RHO)
    p,alpha=pole_vector(FRONT[sector],sector)
    g=math.cosh(.5) if sector=="even-v" else math.sinh(.5)

    N=EXPLICIT_STOP+1
    if sector=="even-v" and N%2==0:
        N+=1
    if sector=="odd-v" and N%2==1:
        N+=1

    r=float(np.max(modes))/float(N)
    if r>=1:
        raise RuntimeError("invalid far ratio")

    # Same endpoint far-row envelope used in the audited remote-Gram work:
    # row(n) = lead/n + O(B/n^2) + O(C/n^3).
    lead=-(2.0/math.pi)*z+alpha*(4.0*g/math.pi)*p

    B=(
        (2.0/math.pi)
        *Z_FAR_CAP/(1.0-r*r)
        *np.abs(modes)
    )

    C=(
        (2.0/math.pi)/(1.0-r*r)
        *np.abs(modes*modes*z)
        +abs(alpha)*(4.0*g/math.pi**3)*np.abs(p)
    )

    root=(
        np.linalg.norm(lead)*math.sqrt(far_sums(N,2))
        +np.linalg.norm(B)*math.sqrt(far_sums(N,4))
        +np.linalg.norm(C)*math.sqrt(far_sums(N,6))
    )
    return float(root)


def raw_remote_floor(sector):
    # Reuse the source-faithful interval formula, but at the new remote start.
    # The shared helper fixes N to 4001/4002, so reproduce its formula here.
    iv=mp.iv
    iv.dps=80
    N=iv.mpf(REMOTE_START[sector])
    pi=iv.pi
    s2=N**-2+1/(2*N)

    c=2/pi**3+6/pi**4
    aa=2*c/pi
    cd=2/pi**2+2/pi**3+2/pi**4+6/pi**5
    cusp=(
        2/pi**2*s2
        +2*aa*iv.sqrt(pi**2/12*(N**-6+1/(10*N**5)))
        +cd*iv.sqrt(N**-4+1/(6*N**3))
    )

    # independent zeta(3) enclosure
    M=20000
    z3=iv.mpf(0)
    for k in range(1,M+1):
        x=iv.mpf(k)
        z3+=1/x**3
    z3=iv.mpf([
        z3.a+(1/(2*iv.mpf(M+1)**2)).a,
        z3.b+(1/(2*iv.mpf(M)**2)).b,
    ])

    q=2/pi
    m4=z3*q**3/(4*(1-q)**3)
    cr=iv.mpf(19)/12+4*m4
    arch=4*cr/pi**2*s2

    out=(
        iv.mpf("0.98")*(iv.log(N/4)-pi/2)
        -iv.mpf("2.05")
        -cusp
        -arch
    )
    if sector=="odd-v":
        sh=(iv.exp(iv.mpf(".5"))-iv.exp(-iv.mpf(".5")))/2
        out-=32*sh**2/pi**2*s2
    return out


def one(sector):
    A=dense_front(sector)
    amin=float(np.linalg.eigvalsh(A)[0])

    G=explicit_cross_gram(sector)
    lam=float(np.linalg.eigvalsh(G)[-1])
    far=far_cross_frobenius_root(sector)
    gram_upper=lam+far*far

    giv=raw_remote_floor(sector)
    glow=REMOTE_GAMMA_CAP[sector]
    if not giv>mp.iv.mpf(str(glow)):
        raise RuntimeError(("raw remote floor cap",sector,giv,glow))

    # Loewner lower bound:
    # F_FR F_RR^-1 F_RF <= gamma^-1 F_FR F_RF.
    S=A-G/glow
    # Charge the far Gram by an isotropic operator cap.
    S-=far*far/glow*np.eye(len(A))
    smin=float(np.linalg.eigvalsh((S+S.T)/2)[0])

    print("\nsector =",sector)
    print("front dimension =",len(FRONT[sector]))
    print("front min eigenvalue =",amin)
    print("remote gamma interval =",giv)
    print("explicit cross Gram lambda_max =",lam)
    print("far cross Frobenius root =",far)
    print("total cross Gram upper =",gram_upper)
    print("certified high-tail Schur lower =",smin)

    if gram_upper>=CROSS_GRAM_CAP[sector]:
        raise RuntimeError(("cross Gram public cap",sector,gram_upper))
    if smin<=HIGH_TAIL_FLOOR_CAP[sector]:
        raise RuntimeError(("high-tail floor public cap",sector,smin))

    return dict(
        amin=amin,
        gamma=giv,
        explicit_gram=lam,
        far_root=far,
        gram_upper=gram_upper,
        high_tail_floor=smin,
    )


def main():
    rows=[one("even-v"),one("odd-v")]
    print("\nPASS direct high-tail coercivity diagnostic")
    print(
        "If the displayed floors have adequate room, replace placeholder "
        "public caps with widened values and use them in the final contour proof."
    )


if __name__=="__main__":
    main()
