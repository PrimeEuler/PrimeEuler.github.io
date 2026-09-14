#!/usr/bin/env python3
"""Source-faithful M=3999 residual-Gram replay on the unresolved even four-plane.

This diagnostic regenerates the M=3999 finite solve rather than importing scalar
transcript constants.  It uses:

* C={1,3,...,19}, F={21,23,...,3999};
* the canonical source-faithful rank-two Suzuki scalar sequence;
* weighted oscillatory quadrature for the finite archimedean H_n/diagonal;
* the exact displacement-generator LDL recurrence for the pole-free F block;
* a rank-one Woodbury update for the full even PSD pole;
* the frozen exact-dyadic 10x6 positive basis Q from v13.399;
* N=ker(Q^T), a numerical orthonormal basis for the unresolved four-plane;
* direct residual rows for 4001..16001;
* an eight-level inverse-power expansion for 16003..2,000,000;
* the same analytic B/n^2+C/n^3 remainder envelope beyond two million.

The six-plane normalized residual Gram is recomputed as a provenance regression:
its maximum eigenvalue must reproduce the final M3999 verifier checkpoint
0.17821051347430.

Status: midpoint structural replay plus use of the already-certified effective-tail
floor delta_T>0.18225976374175623.  The new four-plane residual Gram itself is
not outward-certified here.  No exact-zero, stronger inertia, RH, or GRH claim
follows.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.integrate import quad
from scipy.special import digamma, sici

PI=math.pi
QS=(2,3,4,5,7)
VM=(2,3,2,5,7)
ELLS=np.array([math.log(q) for q in QS],dtype=float)
WEIGHTS=np.array([math.log(vm)/math.sqrt(q) for vm,q in zip(VM,QS)],dtype=float)
DELTA_T=0.18225976374175623
REMOTE_START=16003
EXPLICIT_STOP=2_000_000
FAR_START=2_000_001
KEXP=8

Q_HEX=[
['0x1.a9b0106ac01e8p-4','0x1.50e85227b79f2p-5','0x1.110e340c239ffp-7','-0x1.26a56146f4c61p-9','-0x1.c3bc320065106p-12','-0x1.3ddf24d66961ap-9'],
['0x1.31614dcd93fadp-2','0x1.f5ac98952c139p-4','0x1.a3f768a3f4820p-6','-0x1.d238dc60d4bc0p-8','-0x1.5b42f56f67900p-10','-0x1.f257751033980p-8'],
['0x1.ce789977291cdp-2','0x1.9b6445cd32180p-3','0x1.710376b61e89ep-5','-0x1.b443abef4fc9cp-7','-0x1.30a7867c4bda8p-9','-0x1.c82d01295d99ep-7'],
['0x1.12868d5f20568p-1','0x1.17dbd9766c281p-2','0x1.1a23c7dfb9336p-4','-0x1.75e2ce9fbf67cp-6','-0x1.c8458b60c3edep-9','-0x1.75967d178eb3ep-6'],
['0x1.fe7099bce9880p-12','-0x1.6029608f09120p-12','-0x1.0b6cac294ebf3p-4','0x1.e3081403468f4p-3','-0x1.de674a31d9b83p-1','-0x1.092202100922cp-2'],
['0x1.78ae806502bb8p-2','0x1.73a4763af9621p-2','0x1.3eb502e4eff0dp-3','-0x1.7fefb6818df0cp-4','-0x1.ecb9b14c73288p-7','-0x1.2bf87ac4484d6p-4'],
['-0x1.ae668ca1cd0f0p-3','0x1.596694f849d90p-4','0x1.5de702d2aa8f2p-2','-0x1.a2b41e5441d46p-1','-0x1.0cbaa50837aebp-3','-0x1.6e2e1c3e46549p-2'],
['-0x1.5706bcc587e32p-2','0x1.ab01142a9e1b8p-2','0x1.49a79c77f13f3p-1','0x1.ec9bd6cef6483p-2','0x1.09f8afc5c94a0p-3','-0x1.8c7426ec776aep-3'],
['-0x1.5886f59dbcaa3p-2','0x1.70067d3c53b3dp-1','-0x1.900a8aa8bfe82p-2','-0x1.36755ea389b2ep-3','-0x1.030b5f2af21c4p-3','0x1.a98d4a3cfb6f8p-2'],
['0x1.ffa22a56bf28ep-5','-0x1.93cc3126d01fep-3','0x1.0ef7cb0da9f59p-1','-0x1.ba679d6129a27p-4','-0x1.1b6a2e159d855p-2','0x1.88dcec0ac34b7p-1'],
]
L0_HEX=[
['0x1.9be6472ce844cp-13','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['0x1.1bc7b425ec472p-43','0x1.e1d13acd74362p-7','0x0.0p+0','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.0334f3068864cp-42','-0x1.bebb714d496d0p-50','0x1.c1a4c3504ca1fp-1','0x0.0p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.8f493ba5ca6eep-42','0x1.1aa47eb676025p-48','0x1.86ea932041c6ap-52','0x1.4dfa151bb0094p+0','0x0.0p+0','0x0.0p+0'],
['-0x1.d4b7b575bf7d5p-44','0x1.a231497eb8b46p-48','0x1.80e1a99ec70cfp-52','0x1.670073992bbbdp-56','0x1.6b6c07a0eec9ap+0','0x0.0p+0'],
['0x1.e1711cbdb3146p-42','0x1.d0b5ccbc83ab6p-50','-0x1.452798c7f5298p-50','0x1.6dad86e75f51ap-53','0x1.a00d12034cd1fp-54','0x1.883bd6fde0ad5p+0'],
]


def h(t: float)->float:
    if t==0.0: return 0.25
    if abs(t)<1e-7: return 0.25-t/48.0-t*t/32.0+7.0*t**3/11520.0
    return math.exp(-t/2)/(1-math.exp(-2*t))-1/(2*t)


def arch_H(n:int)->float:
    b=n*PI/2
    return quad(h,0,2,weight='sin',wvar=b,epsabs=2e-13,epsrel=2e-13,limit=200)[0]


def arch_diag(n:int)->float:
    b=n*PI/2
    q1=quad(lambda t:h(t)*(2-t),0,2,weight='cos',wvar=b,epsabs=2e-13,epsrel=2e-13,limit=200)[0]
    q2=quad(h,0,2,weight='sin',wvar=b,epsabs=2e-13,epsrel=2e-13,limit=200)[0]
    return -(q1+q2/b)


def tail_Z(ns):
    ns=np.asarray(ns,dtype=float)
    P=np.sum(WEIGHTS[None,:]*np.sin(ns[:,None]*PI*ELLS[None,:]/2),axis=1)
    y=ns*PI/4
    ans=2*P+np.imag(digamma(0.25+1j*y))
    corr=np.zeros_like(ns)
    for k in range(20):
        a=2*k+0.5
        corr+=math.exp(-2*a)/(a*a+(ns*PI/2)**2)
    return ans+ns*PI*corr


def source_data():
    modes=np.arange(1,4000,2,dtype=int)
    H=np.array([arch_H(int(n)) for n in modes])
    D=np.array([arch_diag(int(n)) for n in modes])
    Si,Ci=sici(modes*PI)
    P=np.sum(WEIGHTS[None,:]*np.sin(modes[:,None]*PI*ELLS[None,:]/2),axis=1)
    k=modes*PI/2
    Pd=-np.sum(WEIGHTS[None,:]*((2-ELLS[None,:])*np.cos(k[:,None]*ELLS[None,:])+
                               np.sin(k[:,None]*ELLS[None,:])/k[:,None]),axis=1)
    cusp=np.log(modes/4)-Ci-Si/(modes*PI)
    Z=2*P+Si+2*H
    diag0=cusp+Pd+D
    c=2*k*math.cosh(.5)/(k*k+.25)
    return modes,Z,diag0,c


def off_block(ms,Zs,ns,Zn):
    ms=np.asarray(ms,dtype=float)[:,None]; ns=np.asarray(ns,dtype=float)[None,:]
    Zs=np.asarray(Zs)[:,None]; Zn=np.asarray(Zn)[None,:]
    return -(2/PI)*(ns*Zs-ms*Zn)/(ns**2-ms**2)


def structured_ldl_solve(diag,u,v,x,RHS):
    d=diag.astype(float).copy(); ug=u.astype(float).copy(); vg=v.astype(float).copy()
    xg=x.astype(float).copy(); B=RHS.astype(float).copy()
    N=len(d); nr=B.shape[1]; cc=2/PI
    piv=np.empty(N); Y=np.empty((N,nr)); ls=[]
    for k in range(N-1):
        a=d[0]; piv[k]=a; Y[k]=B[0]
        b=cc*(ug[0]*vg[1:]-vg[0]*ug[1:])/(xg[0]-xg[1:])
        l=b/a; ls.append(l.copy())
        B=B[1:]-l[:,None]*B[0][None,:]
        d=d[1:]-b*b/a
        ug=ug[1:]-l*ug[0]; vg=vg[1:]-l*vg[0]; xg=xg[1:]
    piv[-1]=d[0]; Y[-1]=B[0]
    X=Y/piv[:,None]
    for k in range(N-2,-1,-1): X[k]-=ls[k]@X[k+1:]
    return X,piv


def finite_solve():
    modes,Z,diag0,c=source_data(); low=modes[:10]; high=modes[10:]
    ZC,ZF=Z[:10],Z[10:]; cC,cF=c[:10],c[10:]
    A0CC=off_block(low,ZC,low,ZC); np.fill_diagonal(A0CC,diag0[:10])
    A0FC=off_block(high,ZF,low,ZC)
    ACC=A0CC+2*np.outer(cC,cC); AFC=A0FC+2*np.outer(cF,cC)
    rhs=np.column_stack([AFC,cF])
    X0,piv=structured_ldl_solve(diag0[10:],ZF,high.astype(float),high.astype(float)**2,rhs)
    X0B,U=X0[:,:10],X0[:,10]
    den=1+2*cF@U
    X=X0B-U[:,None]*(2*(cF@X0B)[None,:]/den)
    S=(ACC-AFC.T@X); S=(S+S.T)/2
    return modes,Z,c,X,S,piv


def residual_gram(Basis,modes,Z,c,X):
    W=np.vstack([Basis,-X@Basis]); jj=modes.astype(float); p=c@W
    d=Basis.shape[1]
    # direct 4001..16001
    G=np.zeros((d,d))
    for start in range(4001,16002,2000):
        stop=min(start+1998,16001); ns=np.arange(start,stop+1,2,dtype=float)
        Zn=tail_Z(ns); kn=ns*PI/2; cn=2*kn*math.cosh(.5)/(kn*kn+.25)
        den=ns[:,None]**2-jj[None,:]**2
        A0=(2/PI)*(Zn[:,None]*jj[None,:]-ns[:,None]*Z[None,:])/den
        R=A0@W+2*cn[:,None]*p[None,:]; G+=R.T@R
    # inverse-power moments
    jld=jj.astype(np.longdouble); Wld=W.astype(np.longdouble); Zld=Z.astype(np.longdouble)
    aa=[]; bb=[]
    for k in range(KEXP):
        aa.append(np.sum((jld**(2*k+1))[:,None]*Wld,axis=0))
        bb.append(np.sum((Zld*jld**(2*k))[:,None]*Wld,axis=0))
    aa=np.array(aa,dtype=np.longdouble); bb=np.array(bb,dtype=np.longdouble)
    pp=np.array(p,dtype=np.longdouble); pild=np.longdouble(PI); cosh=np.longdouble(math.cosh(.5))
    start=REMOTE_START
    while start<=EXPLICIT_STOP:
        end=min(start+199998,EXPLICIT_STOP-1); ns=np.arange(start,end+1,2,dtype=float)
        nn=ns.astype(np.longdouble); Zn=tail_Z(ns).astype(np.longdouble)
        R=np.zeros((len(ns),d),dtype=np.longdouble)
        for k in range(KEXP):
            R+=(np.longdouble(2)/pild)*(Zn[:,None]*aa[k][None,:]/nn[:,None]**(2*k+2)-
                                       bb[k][None,:]/nn[:,None]**(2*k+1))
        kn=nn*pild/2; cn=2*kn*cosh/(kn*kn+np.longdouble(.25))
        R+=2*cn[:,None]*pp[None,:]
        R=np.asarray(R,dtype=float); G+=R.T@R; start=end+2
    return G,W,p


def far_bound(W,p,Z,c,modes):
    N=float(FAR_START); rho=3999/N; jj=modes.astype(float)
    L=-(2/PI)*(Z@W)+(8*math.cosh(.5)/PI)*p
    Bc=(16/PI)/(1-rho*rho)*np.sum(np.abs(jj[:,None]*W),axis=0)
    Cc=(2/PI)/(1-rho*rho)*np.sum(np.abs((jj*jj*Z)[:,None]*W),axis=0)+(8*math.cosh(.5)/PI**3)*np.abs(p)
    def S(pw): return N**(-pw)+1/(2*(pw-1)*N**(pw-1))
    root=np.linalg.norm(L)*math.sqrt(S(2))+np.linalg.norm(Bc)*math.sqrt(S(4))+np.linalg.norm(Cc)*math.sqrt(S(6))
    return root*root,L


def report():
    modes,Z,c,X,S,piv=finite_solve()
    ev=np.linalg.eigvalsh(S)
    print('finite Schur first six =',ev[:6])
    assert abs(ev[4]-3.85764945e-8)<2e-15

    Q=np.array([[float.fromhex(x) for x in row] for row in Q_HEX])
    L0=np.array([[float.fromhex(x) for x in row] for row in L0_HEX])
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True); N=vh[6:].T

    G6,_,_=residual_gram(Q,modes,Z,c,X)
    H6=np.linalg.solve(L0,G6)@np.linalg.inv(L0.T)
    h6=np.linalg.eigvalsh((H6+H6.T)/2)[-1]
    print('six-plane H explicit through 2M =',repr(h6))
    assert abs(h6-0.17821051347430)<1e-10

    G4,W4,p4=residual_gram(N,modes,Z,c,X)
    e4,U4=np.linalg.eigh((G4+G4.T)/2)
    fb,L=far_bound(W4,p4,Z,c,modes)
    sigma_upper=(e4[-1]+fb)/DELTA_T
    print('four-plane residual-Gram eigenvalues through 2M =',e4)
    print('four-plane leading L =',L)
    print('four-plane analytic far-Gram bound =',fb)
    print('delta_T^-1 residual-Gram self-energy ceiling =',sigma_upper)
    l=L/np.linalg.norm(L); u=U4[:,-1]
    overlap=abs(float(l@u))
    print('dominant G4 / leading-L overlap =',overlap)
    print('finite N^T S N eigenvalues =',np.linalg.eigvalsh((N.T@S@N+(N.T@S@N).T)/2))

    assert e4[-1]<1.21e-13
    assert e4[-2]<9e-24
    assert fb<1.2e-15
    assert sigma_upper<6.7e-13
    assert overlap>0.999999999
    print('PASS: M3999 four-plane residual replay and six-plane provenance regression')
    print('GUARDRAIL: new four-plane quantities are midpoint diagnostics, not outward-certified signs')


if __name__=='__main__':
    report()
