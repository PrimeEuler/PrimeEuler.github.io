#!/usr/bin/env python3
"""Outward finite-side certificate for the frozen rho=0.10 M3999 six-planes.

This certifies only the finite M=3999/4000 Schur solves on the exact frozen
six-dimensional dyadic coordinate spaces.  The remote residual Gram is handled
separately.

Arithmetic model
----------------
* midpoint source data / structured LDL are binary64;
* completed factorization and six-RHS residuals are replayed in x86
  longdouble (64-bit significand here);
* all dot products receive standard gamma_n outward envelopes;
* exact-vs-nominal source-operator uncertainty uses the validated v13.357
  dimension-free 2e-13 bound;
* an extra 1e-14 is reserved for the explicit rho B_sm shift and rank-one pole
  scalar evaluation, giving eps_F = 2.1e-13.

Frozen inputs
-------------
Q and L0 are exact IEEE-754 dyadics from
suzuki_endpoint_M3999_frozen_six_direction_inputs.py.  Rank(Q)=6 and
det(L0)!=0 are exact.

For each parity:
1. reconstruct the nominal endpoint buffer and structured pole-free LDL;
2. certify a pole-free buffer floor from d_min, ||L^-1|| and the global
   factorization residual;
3. for odd-v, propagate the corrected negative rank-one pole with a
   residual-certified Sherman-Morrison bound;
4. solve only the six frozen RHS B_Q=F_FC Q and bound the residual outward;
5. compare the approximate restricted Schur matrix with the exact dyadic
   reference L0 L0^T;
6. propagate exact-vs-nominal operator uncertainty into the frozen restriction.

The output C_lower is a rigorous finite-side bound for

    C = L0^{-1} (Q^T S_exact Q) L0^{-T}.

It does NOT include the infinite remote-tail Schur correction.
"""
from __future__ import annotations

from fractions import Fraction
import math
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data,
    offdiag,
    pole_vector,
    structured_ldl,
    ldl_solve,
)
from suzuki_endpoint_M3999_frozen_six_direction_inputs import (
    EVEN_Q_HEX,
    EVEN_L0_HEX,
    ODD_Q_HEX,
    ODD_L0_HEX,
    floats,
)


U64 = 2.0**-53
ULD = float(np.finfo(np.longdouble).eps/2)
EPS_SOURCE = 2.0e-13
EPS_ENDPOINT_EXTRA = 1.0e-14
EPS_F = EPS_SOURCE + EPS_ENDPOINT_EXTRA

# Conservative frozen-space coupling caps obtained by outward Frobenius
# evaluation of B_Q = F_FC Q.
KQ_CAP = {
    "even-v": 0.788,
    "odd-v": 0.772,
}

# Conservative outward six-RHS residual caps from the longdouble replay.
SOLVE_RESIDUAL_CAP = {
    "even-v": 1.29e-15,
    "odd-v": 1.93e-15,
}

# Conservative outward reference-formation defects
# || Bhat - L0 L0^T || before solve/source perturbations.
REFERENCE_DEFECT_CAP = {
    "even-v": 1.11e-15,
    "odd-v": 1.29e-15,
}


def gamma_n(n: int, u: float) -> float:
    nu=n*u
    if nu>=1:
        raise RuntimeError("gamma_n invalid")
    return nu/(1.0-nu)


def fraction_matrix(hex_rows):
    return [
        [Fraction.from_float(float.fromhex(x)) for x in row]
        for row in hex_rows
    ]


def exact_gram_gershgorin(qhex,lhex):
    Q=fraction_matrix(qhex)
    L=fraction_matrix(lhex)

    # exact Q^T Q
    Gq=[[sum(Q[k][i]*Q[k][j] for k in range(10))
         for j in range(6)] for i in range(6)]
    q_upper=max(
        Gq[i][i]+sum(abs(Gq[i][j]) for j in range(6) if j!=i)
        for i in range(6)
    )

    # exact L0 L0^T
    Gl=[[sum(L[i][k]*L[j][k] for k in range(6))
         for j in range(6)] for i in range(6)]
    l_lower=min(
        Gl[i][i]-sum(abs(Gl[i][j]) for j in range(6) if j!=i)
        for i in range(6)
    )

    qf=np.nextafter(float(q_upper),math.inf)
    lf=np.nextafter(float(l_lower),-math.inf)
    return qf,lf


def dense_polefree(modes,z,diag):
    A=offdiag(modes,modes,z,z)
    np.fill_diagonal(A,diag)
    return A


def factor_residual_outward(A,L,D):
    """Bound ||A - L D L^T||_2 by an outward Frobenius bound."""
    n=len(D)

    C=(L*D)@L.T
    R=A-C
    r_fro=np.linalg.norm(R,"fro")

    # Matrix-product backward error:
    # |fl((L D)L^T) - (L D)L^T| <= gamma_{n+2}|LD||L|^T.
    M=np.abs(L*D)@np.abs(L).T
    prod=gamma_n(n+2,U64)*np.linalg.norm(M,"fro")

    # Final subtraction roundoff.
    sub=(
        U64/(1-U64)
        *(np.linalg.norm(A,"fro")+np.linalg.norm(C,"fro"))
    )

    upper=r_fro+prod+sub
    return np.nextafter(float(upper),math.inf), {
        "point_fro":float(r_fro),
        "product_round":float(prod),
        "subtraction_round":float(sub),
    }


def inverse_factor_bounds_outward(L):
    """Outward 1/inf/2 bounds for the exact binary64 unit-lower L."""
    n=L.shape[0]
    A=np.abs(L).astype(np.longdouble)

    y=np.ones(n,dtype=np.longdouble)
    for i in range(1,n):
        s=np.dot(A[i,:i],y[:i])
        g=np.longdouble(gamma_n(i,ULD))
        val=(np.longdouble(1)+s/(1-g))/(1-np.longdouble(ULD))
        y[i]=np.nextafter(val,np.longdouble(np.inf))

    z=np.ones(n,dtype=np.longdouble)
    for j in range(n-2,-1,-1):
        m=n-j-1
        s=np.dot(A[j+1:,j],z[j+1:])
        g=np.longdouble(gamma_n(m,ULD))
        val=(np.longdouble(1)+s/(1-g))/(1-np.longdouble(ULD))
        z[j]=np.nextafter(val,np.longdouble(np.inf))

    linf=float(np.nextafter(np.max(y),np.longdouble(np.inf)))
    lone=float(np.nextafter(np.max(z),np.longdouble(np.inf)))
    l2=float(np.nextafter(
        np.sqrt(np.longdouble(linf)*np.longdouble(lone)),
        np.longdouble(np.inf),
    ))
    return linf,lone,l2


def vector_residual_outward(A,y,b):
    """Outward Euclidean residual for exact binary64 A,y,b."""
    A=np.asarray(A,dtype=np.longdouble)
    y=np.asarray(y,dtype=np.longdouble)
    b=np.asarray(b,dtype=np.longdouble)

    Ay=A@y
    r=b-Ay
    r_point=np.sqrt(np.sum(r*r,dtype=np.longdouble))

    E=(
        np.longdouble(gamma_n(A.shape[1],ULD))
        *(np.abs(A)@np.abs(y))
        +np.longdouble(ULD)/(1-np.longdouble(ULD))
        *(np.abs(b)+np.abs(Ay))
    )
    e=np.sqrt(np.sum(E*E,dtype=np.longdouble))
    return float(np.nextafter(r_point+e,np.longdouble(np.inf)))


def six_rhs_residual_outward(A,B,Y):
    """Outward Frobenius bound, hence 2-norm bound, for B-A Y."""
    A=np.asarray(A,dtype=np.longdouble)
    B=np.asarray(B,dtype=np.longdouble)
    Y=np.asarray(Y,dtype=np.longdouble)

    AY=A@Y
    R=B-AY
    rp=np.sqrt(np.sum(R*R,dtype=np.longdouble))

    E=(
        np.longdouble(gamma_n(A.shape[1],ULD))
        *(np.abs(A)@np.abs(Y))
        +np.longdouble(ULD)/(1-np.longdouble(ULD))
        *(np.abs(B)+np.abs(AY))
    )
    ee=np.sqrt(np.sum(E*E,dtype=np.longdouble))
    return float(np.nextafter(rp+ee,np.longdouble(np.inf)))


def reference_formation_outward(C,R,Q,Y,L0):
    """Outward Frobenius bound for Bhat - L0 L0^T."""
    C=np.asarray(C,dtype=np.longdouble)
    R=np.asarray(R,dtype=np.longdouble)
    Q=np.asarray(Q,dtype=np.longdouble)
    Y=np.asarray(Y,dtype=np.longdouble)
    L0=np.asarray(L0,dtype=np.longdouble)

    BQ=R.T@Q
    CQ=C@Q
    core=Q.T@CQ
    tail=BQ.T@Y
    Bhat=core-tail
    Bref=L0@L0.T
    D=Bhat-Bref
    dp=np.sqrt(np.sum(D*D,dtype=np.longdouble))

    EBQ=np.longdouble(gamma_n(10,ULD))*(np.abs(R).T@np.abs(Q))
    ECQ=np.longdouble(gamma_n(10,ULD))*(np.abs(C)@np.abs(Q))
    Ecore=(
        np.longdouble(gamma_n(10,ULD))*(np.abs(Q).T@np.abs(CQ))
        +np.abs(Q).T@ECQ
    )
    Etail=(
        np.longdouble(gamma_n(Y.shape[0],ULD))*(np.abs(BQ).T@np.abs(Y))
        +EBQ.T@np.abs(Y)
    )
    Eref=np.longdouble(gamma_n(6,ULD))*(np.abs(L0)@np.abs(L0).T)
    Esub=(
        np.longdouble(ULD)/(1-np.longdouble(ULD))
        *(np.abs(core)+np.abs(tail)+np.abs(Bref))
    )
    E=Ecore+Etail+Eref+Esub
    ee=np.sqrt(np.sum(E*E,dtype=np.longdouble))
    return float(np.nextafter(dp+ee,np.longdouble(np.inf)))


def schur_source_perturbation(eps,K,mu,qnorm2):
    """Fixed-Q block resolvent perturbation bound."""
    q=math.sqrt(qnorm2)
    if mu<=eps:
        raise RuntimeError("buffer perturbation exceeds floor")
    return (
        qnorm2*eps
        +2*K*q*eps/(mu-eps)
        +qnorm2*eps*eps/(mu-eps)
        +K*K*eps/(mu*(mu-eps))
    )


def one_sector(sector):
    if sector=="even-v":
        core=np.arange(5,24,2,dtype=int)
        buffer_=np.arange(25,4000,2,dtype=int)
        Q=floats(EVEN_Q_HEX)
        L0=floats(EVEN_L0_HEX)
        qhex,lhex=EVEN_Q_HEX,EVEN_L0_HEX
    elif sector=="odd-v":
        core=np.arange(6,25,2,dtype=int)
        buffer_=np.arange(26,4001,2,dtype=int)
        Q=floats(ODD_Q_HEX)
        L0=floats(ODD_L0_HEX)
        qhex,lhex=ODD_Q_HEX,ODD_L0_HEX
    else:
        raise ValueError(sector)

    modes=np.concatenate([core,buffer_])
    z,diag=endpoint_data(modes)
    zc,zf=z[:10],z[10:]
    dc,df=diag[:10],diag[10:]

    C0=offdiag(core,core,zc,zc)
    np.fill_diagonal(C0,dc)
    R0=offdiag(core,buffer_,zc,zf)

    p,alpha=pole_vector(modes,sector)
    pc,pf=p[:10],p[10:]

    C=C0+alpha*np.outer(pc,pc)
    R=R0+alpha*np.outer(pc,pf)

    # Pole-free nominal buffer and its structured factor.
    A0=dense_polefree(buffer_,zf,df)
    L,D=structured_ldl(buffer_,zf,df)

    factor_resid,factor_parts=factor_residual_outward(A0,L,D)
    linf,lone,l2=inverse_factor_bounds_outward(L)

    dmin=np.nextafter(float(np.min(D)),-math.inf)
    mu0=dmin/(l2*l2)-factor_resid
    if mu0<=0:
        raise RuntimeError("pole-free nominal floor did not certify")

    # Nominal full-buffer conditioning.
    if sector=="even-v":
        # +2 pp^T can only improve the floor.
        mu_nom=mu0
        pole_aux={"den_lower":1.0}
    else:
        # -2 pp^T: residual-certified Sherman-Morrison inverse bound.
        y=ldl_solve(L,D,pf)
        ry=vector_residual_outward(A0,y,pf)
        inv0=1.0/mu0
        yerr=inv0*ry

        pnorm=np.linalg.norm(pf)
        yhat_norm=np.linalg.norm(y)
        qhat=np.longdouble(pf.astype(np.longdouble))@np.longdouble(y.astype(np.longdouble))
        qround=gamma_n(len(pf),ULD)*float(
            np.sum(
                np.abs(pf.astype(np.longdouble)*y.astype(np.longdouble)),
                dtype=np.longdouble,
            )
        )
        qupper=float(qhat)+qround+pnorm*yerr
        den_lower=1.0-2.0*qupper
        if den_lower<=0:
            raise RuntimeError("negative-pole Sherman denominator failed")

        y_upper=yhat_norm+yerr
        invfull=inv0+2.0*y_upper*y_upper/den_lower
        mu_nom=1.0/invfull
        pole_aux={
            "y_residual":ry,
            "q_upper":qupper,
            "den_lower":den_lower,
            "invfull_upper":invfull,
        }

    mu_exact=mu_nom-EPS_F
    if mu_exact<=0:
        raise RuntimeError("exact endpoint buffer floor failed")

    # Frozen six RHS.
    BQ=R.T@Q
    X0=ldl_solve(L,D,BQ)
    yp=ldl_solve(L,D,pf)
    q=float(pf@yp)
    den=1.0+alpha*q
    Y=X0-alpha*np.outer(yp,pf@X0)/den

    Afull=A0+alpha*np.outer(pf,pf)
    solve_resid=six_rhs_residual_outward(Afull,BQ,Y)

    # Independent coupling cap check.
    BQld=BQ.astype(np.longdouble)
    KQ_fro=float(np.sqrt(np.sum(BQld*BQld,dtype=np.longdouble)))
    K=KQ_CAP[sector]
    if not KQ_fro<K:
        raise RuntimeError("frozen coupling cap failed")

    # Frozen exact-coordinate bounds.
    qnorm2,l0min=exact_gram_gershgorin(qhex,lhex)

    ref_defect=reference_formation_outward(C,R,Q,Y,L0)

    # Check the rounded caps used by the scalar certificate.
    if solve_resid>SOLVE_RESIDUAL_CAP[sector]:
        raise RuntimeError(("solve residual cap failed",solve_resid))
    if ref_defect>REFERENCE_DEFECT_CAP[sector]:
        raise RuntimeError(("reference defect cap failed",ref_defect))

    eps_source=schur_source_perturbation(
        EPS_F,K,mu_nom,qnorm2
    )
    eps_solve=K/mu_nom*SOLVE_RESIDUAL_CAP[sector]
    eps_total=(
        REFERENCE_DEFECT_CAP[sector]
        +eps_solve
        +eps_source
    )

    eta=eps_total/l0min
    C_lower=1.0-eta
    raw_margin=l0min-eps_total

    return {
        "sector":sector,
        "factor_residual":factor_resid,
        "factor_parts":factor_parts,
        "dmin":dmin,
        "linv_inf":linf,
        "linv_one":lone,
        "linv_two":l2,
        "mu_polefree_nominal":mu0,
        "mu_full_nominal":mu_nom,
        "mu_full_exact":mu_exact,
        "pole_aux":pole_aux,
        "solve_residual":solve_resid,
        "solve_residual_cap":SOLVE_RESIDUAL_CAP[sector],
        "KQ_fro":KQ_fro,
        "KQ_cap":K,
        "qnorm2_upper":qnorm2,
        "L0L0T_min_lower":l0min,
        "reference_defect":ref_defect,
        "reference_defect_cap":REFERENCE_DEFECT_CAP[sector],
        "eps_source":eps_source,
        "eps_solve":eps_solve,
        "eps_total":eps_total,
        "eta":eta,
        "C_lower":C_lower,
        "raw_margin":raw_margin,
    }


def report():
    print("Frozen rho=0.10 M3999 finite six-plane outward certificate")
    print("EPS_SOURCE =",EPS_SOURCE)
    print("EPS_ENDPOINT_EXTRA =",EPS_ENDPOINT_EXTRA)
    print("EPS_F =",EPS_F)

    rows=[]
    for sector in ("even-v","odd-v"):
        row=one_sector(sector)
        rows.append(row)
        print("\nsector =",sector)
        for k,v in row.items():
            if k not in ("sector","factor_parts","pole_aux"):
                print(k,"=",v)
        print("factor_parts =",row["factor_parts"])
        print("pole_aux =",row["pole_aux"])

    even,odd=rows

    assert even["mu_full_exact"]>0.0022693
    assert odd["mu_full_exact"]>0.0018213

    assert even["solve_residual"]<1.29e-15
    assert odd["solve_residual"]<1.93e-15

    assert even["C_lower"]>0.99999920
    assert odd["C_lower"]>0.99999994

    assert even["raw_margin"]>0.03216488
    assert odd["raw_margin"]>0.65981367

    print("\nPASS: both frozen six-direction finite solves certified")
    print(
        "Guardrail: finite-side certificate only; remote residual-Gram "
        "outward certification remains separate."
    )


if __name__=="__main__":
    report()
