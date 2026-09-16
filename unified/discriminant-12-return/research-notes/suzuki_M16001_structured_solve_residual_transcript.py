#!/usr/bin/env python3
"""Source-faithful M16001 structured-solve residual transcript.

Reconstructs A_FF X-A_FC rowwise from the canonical displacement formula plus
full even PSD pole.  No dense 7991x7991 matrix is stored.  Each 7991-term dot
product is evaluated in long double and charged by
 gamma_7991 * sum_j |a_ij x_jr|.
The pole dot c_F^T X is charged the same way; final multiply/add/subtract
operations are charged explicitly.  The reported Frobenius enclosure is an
operator-norm enclosure for the residual matrix.

Source-generation uncertainty is NOT folded into this arithmetic residual; it
is handled separately by the shifted-nominal operator certificate.
"""
from __future__ import annotations
import math, numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import source_data_stop, finite_solve_stop, off_block, PI

U=np.longdouble(2.0)**np.longdouble(-64)
def gamma(k):
    ku=np.longdouble(k)*U
    return ku/(1-ku)

def report(chunk=128):
    modes,Z,diag0,c=source_data_stop()
    _,_,_,X,_=finite_solve_stop()
    low,high=modes[:10],modes[10:]
    ZC,ZF=Z[:10],Z[10:]; cC,cF=c[:10],c[10:]
    AFC=off_block(high,ZF,low,ZC)+2*np.outer(cF,cC)
    N=len(high)
    h=high.astype(np.longdouble); z=ZF.astype(np.longdouble)
    cc=cF.astype(np.longdouble); xd=X.astype(np.longdouble)
    rhs=AFC.astype(np.longdouble); dg=diag0[10:].astype(np.longdouble)
    pi=np.longdouble(PI)
    cx=np.sum(cc[:,None]*xd,axis=0,dtype=np.longdouble)
    cx_abs=np.sum(np.abs(cc[:,None]*xd),axis=0,dtype=np.longdouble)
    cx_rad=gamma(N)*cx_abs
    point2=np.longdouble(0); out2=np.longdouble(0)
    max_as=max_dr=max_re=np.longdouble(0)
    for s in range(0,N,chunk):
        e=min(N,s+chunk); m=h[s:e,None]; n=h[None,:]
        with np.errstate(divide='ignore',invalid='ignore'):
            A=-(np.longdouble(2)/pi)*(n*z[s:e,None]-m*z[None,:])/(n*n-m*m)
        for ii,row in enumerate(range(s,e)): A[ii,row]=dg[row]
        R=np.empty((e-s,10),dtype=np.longdouble)
        E=np.empty_like(R)
        for r in range(10):
            prod=A*xd[None,:,r]
            sm=np.sum(prod,axis=1,dtype=np.longdouble)
            ab=np.sum(np.abs(prod),axis=1,dtype=np.longdouble)
            dr=gamma(N)*ab
            pole=2*cc[s:e]*cx[r]
            # propagated c^T X error + rounded scale/product/add
            er=dr+2*np.abs(cc[s:e])*cx_rad[r]+gamma(3)*(np.abs(sm)+np.abs(pole))
            val=sm+pole
            er+=gamma(1)*(np.abs(val)+np.abs(rhs[s:e,r]))
            R[:,r]=val-rhs[s:e,r]; E[:,r]=er
            max_as=max(max_as,np.max(ab)); max_dr=max(max_dr,np.max(dr)); max_re=max(max_re,np.max(np.abs(R[:,r])))
        point2+=np.sum(R*R,dtype=np.longdouble)
        out2+=np.sum((np.abs(R)+E)**2,dtype=np.longdouble)
    point=np.sqrt(point2); outward=np.sqrt(out2)
    print('N =',N)
    print('u =',U)
    print('gamma_N =',gamma(N))
    print('max sum_j |A0_ij X_jr| =',max_as)
    print('max gamma_N dot charge =',max_dr)
    print('max point residual entry =',max_re)
    print('point Frobenius residual =',point)
    print('OUTWARD ||R_F||_2 <= ||R_F||_F <',outward)
    assert outward < np.longdouble('1e-14')

if __name__=='__main__': report()
