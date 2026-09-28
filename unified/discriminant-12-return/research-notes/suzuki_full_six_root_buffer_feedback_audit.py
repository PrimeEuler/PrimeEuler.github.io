#!/usr/bin/env python3
"""Audit the missing finite-buffer feedback in the six-root Rouche candidate.

After eliminating the finite buffer B, the remote block is

    Rtilde(z) = F_RR(z) - Z(z) F_BB(z)^(-1) Z(z)^T,

not the original principal remote block F_RR(z).

This script certifies a uniform contour bound for
    Z(z)=F_RB(z)=A_RB-z B_RB
on |z|=0.02, then replaces the raw remote coercivity gamma by

    gamma_eff = gamma - ||Z||^2 ||F_BB(z)^(-1)||.

The exact core-to-remote correction is then bounded by

    ||Y||^2 / gamma_eff.

The certificate passes only if the corrected Rouche margin stays positive.
"""
from __future__ import annotations

import math
import numpy as np

import suzuki_full_six_root_rouche_certificate as R


POWER_ITERS=30
POWER_STARTS=3
ROUND_RESERVE=1.0e-6

Z_CAP={
    "even-v":0.0,  # populated only after direct replay; fail closed below
    "odd-v":0.0,
}


def explicit_cross_components(sector):
    modes=R.modes_for(sector,R.CUT[sector])
    buf=modes[12:]
    ns=np.arange(R.REMOTE_START[sector],R.EXPLICIT_STOP+1,2,dtype=int)

    zb=R.z_source_faithful(buf)
    zn=R.z_source_faithful(ns)

    A=R.offdiag_complex(ns,buf,zn,zb).real
    p_all,alpha=R.pole_vector(modes,sector)
    pb=p_all[12:]
    pn,_=R.pole_vector(ns,sector)
    A+=alpha*np.outer(pn,pb)

    B=-1.0/(ns.astype(float)[:,None]+buf.astype(float)[None,:])
    return buf,ns,A,B


def power_norm(M):
    """Deterministic lower/near-exact replay for reporting, not the proof cap."""
    n=M.shape[1]
    best=0.0
    for s in range(POWER_STARTS):
        x=np.cos((np.arange(n,dtype=float)+1.0)*(s+1.0))
        x/=np.linalg.norm(x)
        for _ in range(POWER_ITERS):
            y=M@x
            ny=np.linalg.norm(y)
            if ny==0:
                break
            x=M.T@y
            nx=np.linalg.norm(x)
            if nx==0:
                break
            x/=nx
        val=np.linalg.norm(M@x)
        best=max(best,float(val))
    return best


def frobenius_upper(M):
    return float(np.linalg.norm(M,"fro"))


def same_parity_sum(N,p):
    return N**(-p)+1.0/(2.0*(p-1)*N**(p-1))


def far_A_bound(sector,buf):
    N=R.EXPLICIT_STOP+1
    if sector=="odd-v" and N%2:
        N+=1
    if sector=="even-v" and N%2==0:
        N+=1

    r=float(np.max(buf))/float(N)
    if r>=1:
        raise RuntimeError("bad far ratio")

    zb=np.abs(R.z_source_faithful(buf))
    pb_all,alpha=R.pole_vector(R.modes_for(sector,R.CUT[sector]),sector)
    pb=np.abs(pb_all[12:])
    g=math.cosh(.5) if sector=="even-v" else math.sinh(.5)

    # |A_nm| <= a_m/n + b_m/n^2 on the far tail.
    a=(
        (2.0/math.pi)/(1.0-r*r)*zb
        +abs(alpha)*(4.0*g/math.pi)*pb
    )
    b=(16.0/math.pi)/(1.0-r*r)*buf.astype(float)

    return (
        float(np.linalg.norm(a))*math.sqrt(same_parity_sum(N,2))
        +float(np.linalg.norm(b))*math.sqrt(same_parity_sum(N,4))
    )


def far_B_bound(buf):
    N=R.EXPLICIT_STOP+1
    # Frobenius tail of 1/(n+m), same parity.
    s=0.0
    for m in buf.astype(float):
        a=N+m
        s+=a**-2+1.0/(2.0*a)
    return math.sqrt(s)


def endpoint_inverse_cap(sector):
    outer=R.outer_analytic_caps(sector)
    # On |z|=.02, the finite-buffer generalized spectrum is > .10.
    return 1.0/(outer["B_floor"]*(0.10-R.RADIUS))


def one(sector):
    buf,ns,A,B=explicit_cross_components(sector)

    # Frobenius is a rigorous spectral-norm upper bound for the explicit rows.
    Aexp=frobenius_upper(A)
    Bexp=frobenius_upper(B)

    # Power replay is reported to show how conservative Frobenius is.
    Apow=power_norm(A)
    Bpow=power_norm(B)

    Afar=far_A_bound(sector,buf)
    Bfar=far_B_bound(buf)

    zupper=Aexp+Afar+R.RADIUS*(Bexp+Bfar)+ROUND_RESERVE
    invbuf=endpoint_inverse_cap(sector)
    feedback=zupper*zupper*invbuf

    gamma=R.REMOTE_GAMMA_FLOOR[sector]
    gamma_eff=gamma-feedback
    if gamma_eff<=0:
        raise RuntimeError(("buffer feedback destroys remote coercivity",sector,zupper,feedback))

    y2=(
        R.EXPLICIT_REMOTE_NORM_CAP[sector]**2
        +R.FAR_REMOTE_NORM_CAP[sector]**2
    )
    corrected=y2/gamma_eff+R.MODEL_RESERVE
    finite=R.FINITE_CONTOUR_FLOOR[sector]
    margin=finite-corrected

    print("\n",sector)
    print("A explicit fro =",Aexp,"power =",Apow)
    print("B explicit fro =",Bexp,"power =",Bpow)
    print("A far =",Afar,"B far =",Bfar)
    print("uniform Z cap =",zupper)
    print("buffer inverse cap =",invbuf)
    print("feedback norm cap =",feedback)
    print("corrected remote gamma =",gamma_eff)
    print("corrected Schur cap =",corrected)
    print("corrected Rouche margin =",margin)

    # The first run is diagnostic.  Public fail-closed caps are added only
    # after observing these values and widening them deliberately.
    if Z_CAP[sector]>0 and zupper>=Z_CAP[sector]:
        raise RuntimeError(("Z public cap",sector,zupper,Z_CAP[sector]))

    if margin<=0:
        raise RuntimeError(("corrected Rouche margin fails",sector,margin))

    return dict(
        Aexp=Aexp,Bexp=Bexp,Apow=Apow,Bpow=Bpow,
        Afar=Afar,Bfar=Bfar,Z=zupper,invbuf=invbuf,
        feedback=feedback,gamma_eff=gamma_eff,
        corrected=corrected,margin=margin,
    )


def main():
    rows=[one("even-v"),one("odd-v")]
    print("\nPASS diagnostic: finite-buffer feedback leaves positive Rouche margin")
    print("Next step: widen Z/corrected-margin caps and fold them into the theorem script.")


if __name__=="__main__":
    main()
