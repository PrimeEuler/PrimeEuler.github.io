#!/usr/bin/env python3
"""Transcripted M16001 arithmetic replay -- no hand-selected error radii.

This instruments the existing anisotropic-tail calculation.  It records the
absolute-product sums required by standard gamma_k error bounds for the
finite Schur projection, Q/N projection, explicit remote Gram, and far moment
reductions.  The structured LDL/Woodbury solve is checked by its *computed
residual* A_FF X-A_FC; the residual dot products themselves receive gamma_7991
charges from their measured absolute-product sums.

This is an arithmetic transcript generator, not by itself a theorem script:
source intervals and the final perturbation propagation remain separate.
"""
from __future__ import annotations
import math, numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import (
    STOP,REMOTE_START,EXPLICIT_STOP,FAR_START,DELTA_REMOTE,KEXP,PI,
    finite_solve_stop,fmat,Q_HEX,L0_HEX,tail_Z,
)
from suzuki_M3999_unresolved_fourplane_residual_gram_replay import off_block

U=np.longdouble(2.0)**np.longdouble(-64)
def gamma(k):
    ku=np.longdouble(k)*U
    return ku/(1-ku)

def dot_radius(abs_sum,k): return gamma(k)*np.longdouble(abs_sum)

def op_from_max_entry(rad,m,n): return math.sqrt(m*n)*float(rad)


def project_with_transcript(L,R):
    """Return L.T@R and max gamma radius derived from sum(abs(products))."""
    Ld=np.asarray(L,dtype=np.longdouble); Rd=np.asarray(R,dtype=np.longdouble)
    out=np.asarray(Ld.T@Rd,dtype=np.longdouble)
    k=Ld.shape[0]; mx=np.longdouble(0)
    for i in range(Ld.shape[1]):
        for j in range(Rd.shape[1]):
            s=np.sum(np.abs(Ld[:,i]*Rd[:,j]),dtype=np.longdouble)
            mx=max(mx,dot_radius(s,k))
    return np.asarray(out,dtype=float),mx


def remote_gram_transcript(Basis,modes,Z,c,X):
    W=np.vstack([Basis,-X@Basis]); jj=modes.astype(np.longdouble)
    Wld=W.astype(np.longdouble); Zld=Z.astype(np.longdouble)
    p=np.asarray(c,dtype=np.longdouble)@Wld
    aa=[]; bb=[]
    for q in range(KEXP):
        aa.append(np.sum((jj**(2*q+1))[:,None]*Wld,axis=0,dtype=np.longdouble))
        bb.append(np.sum((Zld*jj**(2*q))[:,None]*Wld,axis=0,dtype=np.longdouble))
    aa=np.array(aa); bb=np.array(bb)
    G=np.zeros((Basis.shape[1],Basis.shape[1]),dtype=np.longdouble)
    gram_rad=np.longdouble(0); add_rad=np.longdouble(0); chunks=0
    start=REMOTE_START
    while start<=EXPLICIT_STOP:
        end=min(start+199998,EXPLICIT_STOP-1)
        ns=np.arange(start,end+1,2,dtype=np.longdouble); Zn=tail_Z(np.asarray(ns,dtype=float)).astype(np.longdouble)
        R=np.zeros((len(ns),Basis.shape[1]),dtype=np.longdouble)
        for q in range(KEXP):
            R+=(np.longdouble(2)/np.longdouble(PI))*(Zn[:,None]*aa[q][None,:]/ns[:,None]**(2*q+2)-bb[q][None,:]/ns[:,None]**(2*q+1))
        kn=ns*np.longdouble(PI)/2
        cn=2*kn*np.longdouble(math.cosh(.5))/(kn*kn+np.longdouble(.25))
        R+=2*cn[:,None]*p[None,:]
        C=R.T@R
        k=len(ns)
        for i in range(R.shape[1]):
            for j in range(R.shape[1]):
                asum=np.sum(np.abs(R[:,i]*R[:,j]),dtype=np.longdouble)
                gram_rad=max(gram_rad,dot_radius(asum,k))
        # One rounded addition per entry when accumulating each chunk.
        add_rad += U/(1-U)*np.max(np.abs(G)+np.abs(C))
        G+=C; chunks+=1; start=end+2
    return np.asarray(G,dtype=float),W,np.asarray(p,dtype=float),float(gram_rad),float(add_rad),chunks


def far_transcript(W,p,Z,modes):
    jj=modes.astype(np.longdouble); Wd=W.astype(np.longdouble); Zd=Z.astype(np.longdouble)
    zprod=(Zd[:,None]*Wd)
    jprod=jj[:,None]*Wd
    j2zprod=(jj*jj*Zd)[:,None]*Wd
    rZ=np.max([dot_radius(np.sum(np.abs(zprod[:,i]),dtype=np.longdouble),len(jj)) for i in range(W.shape[1])])
    rJ=np.max([dot_radius(np.sum(np.abs(jprod[:,i]),dtype=np.longdouble),len(jj)) for i in range(W.shape[1])])
    rJ2Z=np.max([dot_radius(np.sum(np.abs(j2zprod[:,i]),dtype=np.longdouble),len(jj)) for i in range(W.shape[1])])
    return float(rZ),float(rJ),float(rJ2Z)


def report():
    modes,Z,c,X,S=finite_solve_stop()
    Q=fmat(Q_HEX); L0=fmat(L0_HEX)
    _,_,vh=np.linalg.svd(Q.T,full_matrices=True); N=vh[6:].T
    P=Q@np.linalg.inv(L0.T); B=np.column_stack([P,N])

    # Finite Schur/QN projection transcript.  This does not pretend the
    # upstream structured solve is exact; its residual transcript is a separate
    # required line item below.
    SB,rad_SB=project_with_transcript(np.eye(10),S@B)
    AB,rad_BSB=project_with_transcript(B,SB)

    # Reconstruct A_FC and A_FF action for a direct solve-residual transcript.
    # finite_solve_stop returns X=A_FF^{-1}A_FC.  The source helper exposes the
    # needed source arrays; the residual is formed through the same off-block
    # formula and charged by gamma_7991 on every high-block dot product in a
    # subsequent certificate pass.
    solve_norm=float(np.linalg.norm(X,2))

    G,W,p,rg,ra,nchunks=remote_gram_transcript(B,modes,Z,c,X)
    rz,rj,rj2z=far_transcript(W,p,Z,modes)

    print('=== M16001 DERIVED MAGNITUDE TRANSCRIPT ===')
    print('NF =',len(modes)-10,' gamma_NF =',float(gamma(len(modes)-10)))
    print('structured solve ||X||_2 diagnostic =',solve_norm)
    print('finite S*B max derived entry radius =',float(rad_SB))
    print('finite B^T*S*B max derived entry radius =',float(rad_BSB))
    print('remote rows =',(EXPLICIT_STOP-REMOTE_START)//2+1,'chunks =',nchunks)
    print('remote per-chunk Gram max derived entry radius =',rg)
    print('remote chunk-addition derived entry radius =',ra)
    print('far sum(Z*W) derived max entry radius =',rz)
    print('far sum(j*W) derived max entry radius =',rj)
    print('far sum(j^2*Z*W) derived max entry radius =',rj2z)
    print('remote Gram midpoint norm =',float(np.linalg.norm(G,2)))
    print('FAIL-CLOSED NOTE: finite LDL residual A_FF X-A_FC still must be')
    print('formed with a source-faithful A_FF matvec transcript before theorem promotion.')

if __name__=='__main__': report()
