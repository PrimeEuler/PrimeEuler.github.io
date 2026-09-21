#!/usr/bin/env python3
"""Phase extraction + source-faithful chi_-4 breakpoint comparison.

Key point: deficiency vectors determine their relative reflection phase alpha,
not the self-adjoint extension parameter theta by themselves.  For a desired
invariant boundary phase Theta, theta = Theta-alpha (mod 2pi).

For the canonical real resolvent basis used in the chi_-4 Zeeman prototype,
alpha is measured from <v_-,R v_+>; it should be zero.  Thus choosing the
Section-7 canonical invariant phase Theta=pi returns theta=pi.  This test
therefore decides whether the v13.611 box drift can be repaired by a missing
basis phase (it cannot if alpha~0).

In parallel this file constructs a source-faithful breakpoint-aware first-kind
Fredholm solve for exactly the same chi_-4 kernel, using the architecture of
suzuki_riemann_breakpoint_control.py, and compares its projective characteristic
with the Zeeman nodal compression at common (A,lambda,theta).
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
from math import cosh, sinh, pi
import numpy as np
from numpy.polynomial.legendre import Legendre, leggauss

HERE=Path(__file__).resolve().parent

def load(name,file):
    s=importlib.util.spec_from_file_location(name,HERE/file)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

fc=load("fc","suzuki_chi4_zeeman_finite_characteristic.py")
ck=load("ck2","suzuki_chi4_zeeman_kernel_compression.py")


def wrap_phase(x):
    return (x+np.pi)%(2*np.pi)-np.pi


def reflection_phase(vp,vm):
    Rvp=vp[::-1]
    c=np.vdot(Rvp,vm)
    if abs(c)==0: raise ValueError("zero reflection overlap")
    alpha=float(np.angle(c))
    resid=np.linalg.norm(vm-np.exp(1j*alpha)*Rvp)/max(np.linalg.norm(vm),1e-300)
    return alpha,float(resid)


def derived_theta(data,Theta=np.pi):
    alpha,resid=reflection_phase(data["vp"],data["vm"])
    return wrap_phase(Theta-alpha),alpha,resid


# ---------- breakpoint-aware continuous/Fredholm comparison ----------

def lobatto_nodes(degree,A):
    P=Legendre.basis(degree)
    t=np.concatenate(([-1.],P.deriv().roots(),[1.]))
    return .5*A*(t+1)


def bary_weights(x):
    return np.array([1/np.prod(x[j]-np.delete(x,j)) for j in range(len(x))])


def Lvals(nodes,bary,y):
    y=np.asarray(y); D=y[:,None]-nodes[None,:]; out=np.empty_like(D)
    for r in range(len(y)):
        k=np.where(abs(D[r])<1e-13)[0]
        if len(k): out[r]=0; out[r,k[0]]=1
        else:
            t=bary/D[r]; out[r]=t/t.sum()
    return out


def prime_breaks(A):
    # Reuse the exact chi4 prime-power enumerator and retain only nonzero terms.
    return ck.von_mangoldt_prime_powers(np.exp(2*A))


def row_breaks(x,A,pdata):
    pts={0.,float(A)}
    if 0<x<A: pts.add(float(x))
    for item in pdata:
        # v13.608 routine returns (n, coefficient) for the twisted ramp.
        n=item[0]; ell=np.log(n)
        for y in (x-ell,x+ell,ell-x):
            if 1e-13<y<A-1e-13: pts.add(float(y))
    return sorted(pts)


def Nker(A,x,y):
    return (x*x+y*y)/(4*A)-abs(x-y)/2+A/6


def parity_row(x,parity,nodes,bary,A,lam,pdata,qorder):
    gx,gw=leggauss(qorder); row=np.zeros(len(nodes))
    for l,r in zip(row_breaks(x,A,pdata)[:-1],row_breaks(x,A,pdata)[1:]):
        y=.5*(r-l)*gx+.5*(r+l); w=.5*(r-l)*gw
        L=Lvals(nodes,bary,y); kval=np.empty(len(y))
        for k,yy in enumerate(y):
            kp=float(ck.g_chi4(x-yy))-lam*Nker(A,x,yy)
            km=float(ck.g_chi4(x+yy))-lam*Nker(A,x,-yy)
            kval[k]=kp+km if parity=="e" else kp-km
        row += -(w*kval)@L
    return row


def solve_breakpoint(A,lam,degree=10,qorder=8):
    nodes=lobatto_nodes(degree,A); bary=bary_weights(nodes); m=len(nodes)
    pdata=prime_breaks(A)
    Me=np.zeros((m+1,m+1)); be=np.zeros(m+1)
    for i,x in enumerate(nodes):
        Me[i,:m]=parity_row(x,"e",nodes,bary,A,lam,pdata,qorder)
        Me[i,m]=-1; be[i]=cosh(float(x))
    Me[m,m-1]=1
    Mo=np.zeros((m+1,m+1)); bo=np.zeros(m+1); r=0
    for x in nodes[1:]:
        Mo[r,:m]=parity_row(float(x),"o",nodes,bary,A,lam,pdata,qorder)
        Mo[r,m]=-x; bo[r]=sinh(float(x)); r+=1
    Mo[r,0]=1; r+=1; Mo[r,m-1]=1
    ue,*_=np.linalg.lstsq(Me,be,rcond=None); uo,*_=np.linalg.lstsq(Mo,bo,rcond=None)
    return dict(A=A,lam=lam,nodes=nodes,bary=bary,qe=ue[:m],qo=uo[:m],
                cond_e=np.linalg.cond(Me),cond_o=np.linalg.cond(Mo),
                res_e=np.linalg.norm(Me@ue-be,np.inf),res_o=np.linalg.norm(Mo@uo-bo,np.inf))


def bp_char(s,z,theta,qorder=100):
    gx,gw=leggauss(qorder); y=.5*s["A"]*(gx+1); w=.5*s["A"]*gw
    L=Lvals(s["nodes"],s["bary"],y); qe=L@s["qe"]; qo=L@s["qo"]
    Fp=2*np.sum(w*(qe*np.cos(z*y)+1j*qo*np.sin(z*y)))
    Fm=2*np.sum(w*(qe*np.cos(z*y)-1j*qo*np.sin(z*y)))
    return (z-1j)*Fp+np.exp(1j*theta)*(z+1j)*Fm


def compare(A=2.,two_j=20,degree=10,qorder=8,zref=.5,zgrid=(1.,3.,6.,10.)):
    zd=fc.deficiency_data(two_j,A)
    theta,alpha,rres=derived_theta(zd)
    # Same finite lambda isolates discretization/carrier effects.
    bp=solve_breakpoint(A,zd["lam"],degree,qorder)
    zw0=fc.characteristic(zd,zref,theta); bw0=bp_char(bp,zref,theta)
    print(f"A={A} j={two_j/2:g} lambda={zd['lam']:.12g}")
    print(f"alpha={alpha:.3e} theta={theta:.12g} reflection_res={rres:.3e}")
    print(f"BP cond(e,o)=({bp['cond_e']:.3e},{bp['cond_o']:.3e}) residuals=({bp['res_e']:.3e},{bp['res_o']:.3e})")
    for z in zgrid:
        zr=fc.characteristic(zd,z,theta)/zw0
        br=bp_char(bp,z,theta)/bw0
        print(f"z={z:5g} Zeeman={zr!r} breakpoint={br!r} absdiff={abs(zr-br):.6e}")


if __name__=="__main__":
    for A in (1.5,2.,2.5): compare(A=A)
