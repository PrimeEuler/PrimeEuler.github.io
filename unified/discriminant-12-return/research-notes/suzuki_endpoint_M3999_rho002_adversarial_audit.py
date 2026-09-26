#!/usr/bin/env python3
"""Adversarial rho=0.02 audit using the frozen v13.818 payloads unchanged.

Audits minus negative four-plane, minus positive six-plane, and plus standard
ten-core in both parity sectors.  Every cap is deliberately wider than the
observed value so platform variation cannot turn a healthy proof into a false
failure.

This is an audit/hardening artifact.  It does not regenerate any frozen basis
or Cholesky factor and does not itself promote the rho=0.02 endpoint theorem.
"""
from __future__ import annotations

import math
import mpmath as mp
import numpy as np

from suzuki_endpoint_M3999_midpoint_effective_core import (
    endpoint_data, offdiag, pole_vector, structured_ldl, ldl_solve,
    z_source_faithful,
)
from suzuki_endpoint_M3999_rho002_minus_frozen_inputs import (
    EVEN_QNEG_HEX, EVEN_LNEG_HEX, EVEN_QPOS_HEX, EVEN_LPOS_HEX,
    EVEN_PAYLOAD_SHA256, ODD_QNEG_HEX, ODD_LNEG_HEX,
    ODD_QPOS_HEX, ODD_LPOS_HEX, ODD_PAYLOAD_SHA256,
    floats as minus_floats, verify_one as verify_minus_payload,
)
from suzuki_endpoint_M3999_rho002_plus_frozen_L0 import (
    EVEN_L0_HEX, EVEN_SHA256, ODD_L0_HEX, ODD_SHA256,
    floats as plus_floats, verify_one as verify_plus_payload,
)

RHO = 0.02
U64 = 2.0**-53
ULD = float(np.finfo(np.longdouble).eps / 2)
EPS_F = 2.1e-13
KEXP = 8
EXPLICIT_STOP = 2_000_000
Z_FAR_CAP = 8.0
REMOTE_CROSS_CAP = 20.0
REPLAY_ARITH_CAP = 1.0e-8

FACTOR_CAP = {
    (-1, "even-v"): 6.5e-11, (-1, "odd-v"): 6.5e-11,
    (+1, "even-v"): 6.8e-11, (+1, "odd-v"): 6.8e-11,
}
FINITE_CAPS = {
    ("minus-neg", "even-v"): dict(K=.21, resid=1.00e-16, ref=1.20e-16),
    ("minus-neg", "odd-v"):  dict(K=.27, resid=2.10e-16, ref=2.80e-16),
    ("minus-pos", "even-v"): dict(K=1.08, resid=1.45e-15, ref=1.20e-15),
    ("minus-pos", "odd-v"):  dict(K=.81, resid=1.25e-15, ref=1.05e-15),
    ("plus", "even-v"):      dict(K=1.11, resid=1.90e-15, ref=1.15e-15),
    ("plus", "odd-v"):       dict(K=.85, resid=1.45e-15, ref=.80e-15),
}
REMOTE_CAPS = {
    ("minus-pos", "even-v"): dict(invL=2.05, W=2.80, Hexp=.0480, Hfar=1.20e-4, Y=.225, epsY=5.0e-7),
    ("minus-pos", "odd-v"):  dict(invL=1.13, W=1.23, Hexp=.0088, Hfar=2.20e-5, Y=.100, epsY=4.0e-7),
    ("plus", "even-v"):      dict(invL=20.8, W=20.8, Hexp=.0435, Hfar=1.10e-4, Y=.215, epsY=2.0e-6),
    ("plus", "odd-v"):       dict(invL=12.4, W=12.4, Hexp=.0345, Hfar=8.50e-5, Y=.195, epsY=1.5e-6),
}
GAMMA_LOWER = {
    ("minus-pos", "even-v"): 3.18003114023348,
    ("minus-pos", "odd-v"):  3.18016610573875,
    ("plus", "even-v"):      3.39351949707118,
    ("plus", "odd-v"):       3.39366445882790,
}

def gamma_n(n, u):
    nu = n*u
    if nu >= 1:
        raise RuntimeError("gamma_n invalid")
    return nu/(1-nu)

def layout(sector):
    if sector == "even-v":
        return np.arange(5,24,2,dtype=int), np.arange(25,4000,2,dtype=int)
    return np.arange(6,25,2,dtype=int), np.arange(26,4001,2,dtype=int)

def dense_polefree(modes,z,diag):
    A=offdiag(modes,modes,z,z)
    np.fill_diagonal(A,diag)
    return A

def build_blocks(sector, sign):
    core,buffer_=layout(sector)
    modes=np.concatenate([core,buffer_])
    z,diag=endpoint_data(modes,sign=sign,rho=RHO)
    zc,zf=z[:10],z[10:]; dc,df=diag[:10],diag[10:]
    C0=offdiag(core,core,zc,zc); np.fill_diagonal(C0,dc)
    R0=offdiag(core,buffer_,zc,zf)
    p,alpha=pole_vector(modes,sector); pc,pf=p[:10],p[10:]
    C=C0+alpha*np.outer(pc,pc)
    R=R0+alpha*np.outer(pc,pf)
    A0=dense_polefree(buffer_,zf,df)
    L,D=structured_ldl(buffer_,zf,df)
    return dict(
        sector=sector, sign=sign, core=core, buffer=buffer_,
        modes=modes.astype(float), z=z, C=C, R=R, A0=A0,
        Afull=A0+alpha*np.outer(pf,pf), L=L, D=D,
        p=p, pf=pf, alpha=alpha,
    )

def factor_residual_outward(A,L,D):
    n=len(D); C=(L*D)@L.T; R=A-C
    r=np.linalg.norm(R,"fro")
    M=np.abs(L*D)@np.abs(L).T
    prod=gamma_n(n+2,U64)*np.linalg.norm(M,"fro")
    sub=U64/(1-U64)*(np.linalg.norm(A,"fro")+np.linalg.norm(C,"fro"))
    return np.nextafter(float(r+prod+sub),math.inf)

def inverse_factor_bounds_outward(L):
    n=L.shape[0]; A=np.abs(L).astype(np.longdouble)
    y=np.ones(n,dtype=np.longdouble)
    for i in range(1,n):
        s=np.dot(A[i,:i],y[:i]); g=np.longdouble(gamma_n(i,ULD))
        y[i]=np.nextafter((1+s/(1-g))/(1-np.longdouble(ULD)),np.longdouble(np.inf))
    z=np.ones(n,dtype=np.longdouble)
    for j in range(n-2,-1,-1):
        m=n-j-1; s=np.dot(A[j+1:,j],z[j+1:]); g=np.longdouble(gamma_n(m,ULD))
        z[j]=np.nextafter((1+s/(1-g))/(1-np.longdouble(ULD)),np.longdouble(np.inf))
    linf=float(np.nextafter(np.max(y),np.longdouble(np.inf)))
    lone=float(np.nextafter(np.max(z),np.longdouble(np.inf)))
    ltwo=float(np.nextafter(np.sqrt(np.longdouble(linf)*np.longdouble(lone)),np.longdouble(np.inf)))
    return linf,lone,ltwo

def vector_residual_outward(A,y,b):
    A=np.asarray(A,np.longdouble); y=np.asarray(y,np.longdouble); b=np.asarray(b,np.longdouble)
    Ay=A@y; r=b-Ay
    rp=np.sqrt(np.sum(r*r,dtype=np.longdouble))
    E=(np.longdouble(gamma_n(A.shape[1],ULD))*(np.abs(A)@np.abs(y))
       +np.longdouble(ULD)/(1-np.longdouble(ULD))*(np.abs(b)+np.abs(Ay)))
    return float(np.nextafter(rp+np.sqrt(np.sum(E*E,dtype=np.longdouble)),np.longdouble(np.inf)))

def rhs_residual_outward(A,B,Y):
    A=np.asarray(A,np.longdouble); B=np.asarray(B,np.longdouble); Y=np.asarray(Y,np.longdouble)
    AY=A@Y; R=B-AY
    rp=np.sqrt(np.sum(R*R,dtype=np.longdouble))
    E=(np.longdouble(gamma_n(A.shape[1],ULD))*(np.abs(A)@np.abs(Y))
       +np.longdouble(ULD)/(1-np.longdouble(ULD))*(np.abs(B)+np.abs(AY)))
    return float(np.nextafter(rp+np.sqrt(np.sum(E*E,dtype=np.longdouble)),np.longdouble(np.inf)))

def solve_full(block,BQ):
    X0=ldl_solve(block["L"],block["D"],BQ)
    yp=ldl_solve(block["L"],block["D"],block["pf"])
    den=1+block["alpha"]*float(block["pf"]@yp)
    if den <= 0:
        raise RuntimeError("nominal pole denominator failed")
    return X0-block["alpha"]*np.outer(yp,block["pf"]@X0)/den

def buffer_condition(block):
    fres=factor_residual_outward(block["A0"],block["L"],block["D"])
    fcap=FACTOR_CAP[(block["sign"],block["sector"])]
    if fres >= fcap:
        raise RuntimeError(("factor cap",fres,fcap))
    linf,lone,ltwo=inverse_factor_bounds_outward(block["L"])
    dmin=np.nextafter(float(np.min(block["D"])),-math.inf)
    mu0=dmin/(ltwo*ltwo)-fres
    if mu0 <= 0:
        raise RuntimeError("pole-free floor failed")
    if block["sector"]=="even-v":
        mu=mu0; denlo=1.0
    else:
        pf=block["pf"]; y=ldl_solve(block["L"],block["D"],pf)
        ry=vector_residual_outward(block["A0"],y,pf)
        inv0=1/mu0; yerr=inv0*ry
        qhat=np.longdouble(pf.astype(np.longdouble))@np.longdouble(y.astype(np.longdouble))
        qround=gamma_n(len(pf),ULD)*float(np.sum(np.abs(pf.astype(np.longdouble)*y.astype(np.longdouble)),dtype=np.longdouble))
        qupper=float(qhat)+qround+np.linalg.norm(pf)*yerr
        denlo=1-2*qupper
        if denlo <= 0:
            raise RuntimeError("odd pole denominator failed")
        yupper=np.linalg.norm(y)+yerr
        mu=1/(inv0+2*yupper*yupper/denlo)
    if mu-EPS_F <= 0:
        raise RuntimeError("exact buffer floor failed")
    return dict(factor=fres,factor_cap=fcap,linf=linf,lone=lone,ltwo=ltwo,dmin=dmin,mu0=mu0,mu=mu,mu_exact=mu-EPS_F,denlo=denlo)

def reference_defect(C,R,Q,Y,Lref,negative=False):
    C=np.asarray(C,np.longdouble); R=np.asarray(R,np.longdouble)
    Q=np.asarray(Q,np.longdouble); Y=np.asarray(Y,np.longdouble); Lref=np.asarray(Lref,np.longdouble)
    BQ=R.T@Q; CQ=C@Q; core=Q.T@CQ; tail=BQ.T@Y
    Bhat=core-tail
    if negative:
        Bhat=-Bhat
    Bref=Lref@Lref.T
    D=Bhat-Bref
    dp=np.sqrt(np.sum(D*D,dtype=np.longdouble))
    EBQ=np.longdouble(gamma_n(10,ULD))*(np.abs(R).T@np.abs(Q))
    ECQ=np.longdouble(gamma_n(10,ULD))*(np.abs(C)@np.abs(Q))
    Ecore=np.longdouble(gamma_n(10,ULD))*(np.abs(Q).T@np.abs(CQ))+np.abs(Q).T@ECQ
    Etail=np.longdouble(gamma_n(Y.shape[0],ULD))*(np.abs(BQ).T@np.abs(Y))+EBQ.T@np.abs(Y)
    Eref=np.longdouble(gamma_n(Lref.shape[0],ULD))*(np.abs(Lref)@np.abs(Lref).T)
    Esub=np.longdouble(ULD)/(1-np.longdouble(ULD))*(np.abs(core)+np.abs(tail)+np.abs(Bref))
    ee=np.sqrt(np.sum((Ecore+Etail+Eref+Esub)**2,dtype=np.longdouble))
    return float(np.nextafter(dp+ee,np.longdouble(np.inf)))

def source_schur_bound(eps,K,mu,q2):
    q=math.sqrt(q2)
    return (q2*eps + 2*K*q*eps/(mu-eps) + q2*eps*eps/(mu-eps)
            + K*K*eps/(mu*(mu-eps)))

def audit_subspace(kind,block,Q,Lref,negative=False):
    key=(kind,block["sector"]); cap=FINITE_CAPS[key]
    bc=buffer_condition(block)
    BQ=block["R"].T@Q; Y=solve_full(block,BQ)
    Kactual=float(np.linalg.norm(BQ,"fro"))
    residual=rhs_residual_outward(block["Afull"],BQ,Y)
    ref=reference_defect(block["C"],block["R"],Q,Y,Lref,negative)
    if Kactual >= cap["K"] or residual >= cap["resid"] or ref >= cap["ref"]:
        raise RuntimeError(("finite cap failed",key,Kactual,residual,ref))
    q2=max(float(np.linalg.norm(Q,2)**2),1.00000000000001)
    lmin=float(np.linalg.eigvalsh(Lref@Lref.T)[0])
    es=source_schur_bound(EPS_F,cap["K"],bc["mu"],q2)
    er=cap["K"]/bc["mu"]*cap["resid"]
    et=cap["ref"]+es+er
    sch=Q.T@block["C"]@Q-BQ.T@Y
    graph=Q.T@block["C"]@Q-BQ.T@Y-Y.T@BQ+Y.T@block["Afull"]@Y
    disc=float(np.linalg.norm(graph-sch,2))
    gbound=np.linalg.norm(Y,2)*cap["resid"]+5e-15
    if disc >= gbound:
        raise RuntimeError(("graph check failed",key,disc,gbound))
    return dict(
        kind=kind,sector=block["sector"],block=block,Q=Q,L0=Lref,Y=Y,
        buffer=bc,Kactual=Kactual,Kcap=cap["K"],residual=residual,resid_cap=cap["resid"],
        ref=ref,ref_cap=cap["ref"],lmin=lmin,invL=float(np.linalg.norm(np.linalg.inv(Lref),2)),
        eps_source=es,eps_solve=er,eps_total=et,
        normalized_lower=1-et/lmin,raw_margin=lmin-et,
        graph_discrepancy=disc,graph_bound=gbound,
    )

def zeta3_interval(M=20000):
    iv=mp.iv; s=iv.mpf(0)
    for k in range(1,M+1):
        x=iv.mpf(k); s+=1/x**3
    lo=1/(2*iv.mpf(M+1)**2); hi=1/(2*iv.mpf(M)**2)
    return iv.mpf([s.a+lo.a,s.b+hi.b])

def tail_floor_interval(sign,sector):
    iv=mp.iv; iv.dps=80
    N=4001 if sector=="even-v" else 4002
    n=iv.mpf(N); pi=iv.pi; s2=n**-2+1/(2*n)
    c=2/pi**3+6/pi**4; alpha=2*c/pi
    cdiag=2/pi**2+2/pi**3+2/pi**4+6/pi**5
    cusp=(2/pi**2*s2 + 2*alpha*iv.sqrt(pi**2/12*(n**-6+1/(10*n**5)))
          + cdiag*iv.sqrt(n**-4+1/(6*n**3)))
    q=2/pi; z3=zeta3_interval(); m4=z3*q**3/(4*(1-q)**3); cr=iv.mpf(19)/12+4*m4
    arch=4*cr/pi**2*s2
    coeff=iv.mpf("0.98" if sign==-1 else "1.02")
    out=coeff*(iv.log(n/4)-pi/2)-iv.mpf("2.05")-cusp-arch
    if sector=="odd-v":
        sh=(iv.exp(iv.mpf(".5"))-iv.exp(-iv.mpf(".5")))/2
        out-=32*sh**2/pi**2*s2
    return out

def tail_z(ns,sign):
    return z_source_faithful(ns)+sign*RHO*math.pi/2

def dressed(audit):
    W=np.vstack([audit["Q"],-audit["Y"]])
    b=audit["block"]
    return dict(audit=audit,block=b,L0=audit["L0"],W=W,pW=b["p"]@W)

def direct_rows(p,ns):
    b=p["block"]; ns=np.asarray(ns,float); zn=tail_z(ns,b["sign"])
    den=ns[:,None]**2-b["modes"][None,:]**2
    A0=(2/math.pi)*(zn[:,None]*b["modes"][None,:]-ns[:,None]*b["z"][None,:])/den
    pn,_=pole_vector(ns,b["sector"])
    return A0@p["W"]+b["alpha"]*pn[:,None]*p["pW"][None,:]

def moments(p):
    b=p["block"]; j=b["modes"].astype(np.longdouble); W=p["W"].astype(np.longdouble); z=b["z"].astype(np.longdouble)
    aa=[]; bb=[]
    for k in range(KEXP):
        aa.append(np.sum((j**(2*k+1))[:,None]*W,axis=0))
        bb.append(np.sum((z*j**(2*k))[:,None]*W,axis=0))
    return np.array(aa),np.array(bb)

def expanded_rows(p,ns,aa,bb):
    b=p["block"]; nn=np.asarray(ns,np.longdouble)
    zn=tail_z(np.asarray(ns,float),b["sign"]).astype(np.longdouble)
    R=np.zeros((len(nn),p["W"].shape[1]),dtype=np.longdouble); pi=np.longdouble(math.pi)
    for k in range(KEXP):
        R+=(np.longdouble(2)/pi)*(zn[:,None]*aa[k][None,:]/nn[:,None]**(2*k+2)-bb[k][None,:]/nn[:,None]**(2*k+1))
    pn,_=pole_vector(np.asarray(ns,float),b["sector"])
    R+=np.longdouble(b["alpha"])*pn.astype(np.longdouble)[:,None]*p["pW"].astype(np.longdouble)[None,:]
    return np.asarray(R,float)

def normalized_gram(p):
    sec=p["block"]["sector"]; start=4001 if sec=="even-v" else 4002; direct_stop=16001 if sec=="even-v" else 16000
    d=p["W"].shape[1]; G=np.zeros((d,d))
    for st in range(start,direct_stop+1,2000):
        en=min(st+1998,direct_stop); ns=np.arange(st,en+1,2,float)
        R=direct_rows(p,ns); G+=R.T@R
    aa,bb=moments(p); st=direct_stop+2
    while st<=EXPLICIT_STOP:
        en=min(st+199998,EXPLICIT_STOP)
        if (en-st)%2: en-=1
        ns=np.arange(st,en+1,2,float)
        R=expanded_rows(p,ns,aa,bb); G+=R.T@R; st=en+2
    H=np.linalg.solve(p["L0"],G)@np.linalg.inv(p["L0"].T)
    return (H+H.T)/2

def prove_far_generator():
    iv=mp.iv; iv.dps=80
    qs=[iv.mpf(2),iv.mpf(3),iv.mpf(4),iv.mpf(5),iv.mpf(7)]
    ls=[iv.log(2),iv.log(3),iv.log(2),iv.log(5),iv.log(7)]
    wsum=sum(l/iv.sqrt(q) for l,q in zip(ls,qs))
    n=iv.mpf(2_000_001); y=n*iv.pi/4
    upper=(2*wsum+iv.pi/2+1/y+4/(n*iv.pi)*iv.exp(-1)/(1-iv.exp(-4))+iv.mpf(".02")*iv.pi/2)
    if not upper < iv.mpf(8):
        raise RuntimeError(("far Z bound",upper))
    return upper

def far_envelope(p):
    b=p["block"]; T=np.linalg.inv(p["L0"].T); W=p["W"]@T
    pW=b["p"]@W; modes=b["modes"]; z=b["z"]
    if b["sector"]=="even-v":
        N=2_000_001.; g=math.cosh(.5)
    else:
        N=2_000_002.; g=math.sinh(.5)
    r=np.max(modes)/N
    lead=-(2/math.pi)*(z@W)+b["alpha"]*(4*g/math.pi)*pW
    B=(2/math.pi)*Z_FAR_CAP/(1-r*r)*np.sum(np.abs(modes[:,None]*W),axis=0)
    C=((2/math.pi)/(1-r*r)*np.sum(np.abs((modes*modes*z)[:,None]*W),axis=0)
       +abs(b["alpha"])*(4*g/math.pi**3)*np.abs(pW))
    S=lambda power:N**(-power)+1/(2*(power-1)*N**(power-1))
    root=np.linalg.norm(lead)*math.sqrt(S(2))+np.linalg.norm(B)*math.sqrt(S(4))+np.linalg.norm(C)*math.sqrt(S(6))
    return root*root,float(np.linalg.norm(np.linalg.inv(p["L0"]),2)),float(np.linalg.norm(W,2))


def common_cross_cap_check():
    """Re-derive the crude common remote cross cap 20."""
    pi=math.pi
    s2=1.5
    c=2/pi**3+6/pi**4
    alpha=2*c/pi
    cdiag=2/pi**2+2/pi**3+2/pi**4+6/pi**5
    cusp=(2/pi**2*s2
          +2*alpha*math.sqrt(pi**2/12*(1+1/10))
          +cdiag*math.sqrt(1+1/6))
    q=2/pi
    m4=float(mp.zeta(3))*q**3/(4*(1-q)**3)
    cr=19/12+4*m4
    arch=4*cr/pi**2*s2
    hilbert=1.02*pi/2
    prime=2.05
    pole_even=(16/3)*math.cosh(.5)**2
    pole_odd=(16/3)*math.sinh(.5)**2
    even=hilbert+prime+cusp+arch+pole_even
    odd=hilbert+prime+cusp+arch+pole_odd
    if even >= REMOTE_CROSS_CAP or odd >= REMOTE_CROSS_CAP:
        raise RuntimeError(("remote cross cap failed",even,odd))
    return even,odd

def audit_remote(a):
    key=(a["kind"],a["sector"]); cap=REMOTE_CAPS[key]; fcap=FINITE_CAPS[key]
    p=dressed(a); H=normalized_gram(p); lam=float(np.linalg.eigvalsh(H)[-1])
    far,invL,Wnorm=far_envelope(p)
    if lam>=cap["Hexp"] or far>=cap["Hfar"] or invL>=cap["invL"] or Wnorm>=cap["W"]:
        raise RuntimeError(("remote cap failed",key,lam,far,invL,Wnorm))
    giv=tail_floor_interval(a["block"]["sign"],a["sector"]); glow=GAMMA_LOWER[key]
    if not giv > mp.iv.mpf(str(glow)):
        raise RuntimeError(("gamma cap failed",key,giv))
    mu=a["buffer"]["mu"]
    dx=(EPS_F/(mu-EPS_F)+EPS_F*fcap["K"]/(mu*(mu-EPS_F))+fcap["resid"]/mu)*cap["invL"]
    epsY=REMOTE_CROSS_CAP*dx+EPS_F*cap["W"]+REPLAY_ARITH_CAP
    if epsY>=cap["epsY"]:
        raise RuntimeError(("epsY cap failed",key,epsY))
    if math.sqrt(cap["Hexp"]+cap["Hfar"]) >= cap["Y"]:
        raise RuntimeError(("Y point-norm cap failed",key))
    hupper=cap["Hexp"]+cap["Hfar"]+2*cap["Y"]*cap["epsY"]+cap["epsY"]**2
    terminal=glow*a["normalized_lower"]; margin=terminal-hupper
    return dict(lam=lam,Hexp_cap=cap["Hexp"],far=far,Hfar_cap=cap["Hfar"],invL=invL,invL_cap=cap["invL"],
                Wnorm=Wnorm,Wcap=cap["W"],gamma=giv,gamma_lower=glow,dx=dx,epsY=epsY,epsY_cap=cap["epsY"],
                Hupper=hupper,terminal=terminal,margin=margin,normalized=a["normalized_lower"]-hupper/glow)

def headroom(cap,actual):
    return 100*(cap/actual-1)

def main():
    verify_minus_payload("even-v",EVEN_QNEG_HEX,EVEN_LNEG_HEX,EVEN_QPOS_HEX,EVEN_LPOS_HEX,EVEN_PAYLOAD_SHA256)
    verify_minus_payload("odd-v",ODD_QNEG_HEX,ODD_LNEG_HEX,ODD_QPOS_HEX,ODD_LPOS_HEX,ODD_PAYLOAD_SHA256)
    verify_plus_payload("even-v",EVEN_L0_HEX,EVEN_SHA256)
    verify_plus_payload("odd-v",ODD_L0_HEX,ODD_SHA256)

    fm={
        "even-v":(minus_floats(EVEN_QNEG_HEX),minus_floats(EVEN_LNEG_HEX),minus_floats(EVEN_QPOS_HEX),minus_floats(EVEN_LPOS_HEX)),
        "odd-v":(minus_floats(ODD_QNEG_HEX),minus_floats(ODD_LNEG_HEX),minus_floats(ODD_QPOS_HEX),minus_floats(ODD_LPOS_HEX)),
    }
    fp={"even-v":plus_floats(EVEN_L0_HEX),"odd-v":plus_floats(ODD_L0_HEX)}
    blocks={(s,sec):build_blocks(sec,s) for s in (-1,+1) for sec in ("even-v","odd-v")}

    rows={}
    for sec in ("even-v","odd-v"):
        Qn,Ln,Qp,Lp=fm[sec]
        rows[("minus-neg",sec)]=audit_subspace("minus-neg",blocks[(-1,sec)],Qn,Ln,True)
        rows[("minus-pos",sec)]=audit_subspace("minus-pos",blocks[(-1,sec)],Qp,Lp,False)
        rows[("plus",sec)]=audit_subspace("plus",blocks[(+1,sec)],np.eye(10),fp[sec],False)

    zupper=prove_far_generator()
    cross=common_cross_cap_check()
    print("far generator upper interval =",zupper)
    print("remote cross component totals =",cross)

    remote={}
    for key in (("minus-pos","even-v"),("minus-pos","odd-v"),("plus","even-v"),("plus","odd-v")):
        remote[key]=audit_remote(rows[key])

    print("\nFINITE AUDIT")
    for key,r in rows.items():
        print("\n",key)
        print("factor",r["buffer"]["factor"],"cap",r["buffer"]["factor_cap"],"headroom%",headroom(r["buffer"]["factor_cap"],r["buffer"]["factor"]))
        print("mu_nom",r["buffer"]["mu"],"mu_exact",r["buffer"]["mu_exact"],"pole_den",r["buffer"]["denlo"])
        print("K",r["Kactual"],"cap",r["Kcap"],"headroom%",headroom(r["Kcap"],r["Kactual"]))
        print("residual",r["residual"],"cap",r["resid_cap"],"headroom%",headroom(r["resid_cap"],r["residual"]))
        print("reference",r["ref"],"cap",r["ref_cap"],"headroom%",headroom(r["ref_cap"],r["ref"]))
        print("lmin",r["lmin"],"eps_total",r["eps_total"],"normalized",r["normalized_lower"],"raw",r["raw_margin"])
        print("graph discrepancy",r["graph_discrepancy"],"bound",r["graph_bound"])

    print("\nREMOTE AUDIT")
    for key,r in remote.items():
        print("\n",key)
        print("H explicit",r["lam"],"cap",r["Hexp_cap"],"headroom%",headroom(r["Hexp_cap"],r["lam"]))
        print("H far",r["far"],"cap",r["Hfar_cap"],"headroom%",headroom(r["Hfar_cap"],r["far"]))
        print("invL",r["invL"],"cap",r["invL_cap"],"headroom%",headroom(r["invL_cap"],r["invL"]))
        print("Wnorm",r["Wnorm"],"cap",r["Wcap"],"headroom%",headroom(r["Wcap"],r["Wnorm"]))
        print("gamma",r["gamma"],"lower",r["gamma_lower"])
        print("derived epsY",r["epsY"],"cap",r["epsY_cap"])
        print("H upper",r["Hupper"],"terminal",r["terminal"],"margin",r["margin"],"normalized",r["normalized"])

    assert rows[("minus-neg","even-v")]["raw_margin"]>0.0026617994
    assert rows[("minus-neg","odd-v")]["raw_margin"]>0.0039857058
    assert remote[("minus-pos","even-v")]["margin"]>3.131
    assert remote[("minus-pos","odd-v")]["margin"]>3.171
    assert remote[("plus","even-v")]["margin"]>3.349
    assert remote[("plus","odd-v")]["margin"]>3.359

    print("\nPASS: adversarial rho=0.02 cap audit")
    print("Frozen payloads unchanged; theorem promotion remains a separate gate.")

if __name__=="__main__":
    main()
