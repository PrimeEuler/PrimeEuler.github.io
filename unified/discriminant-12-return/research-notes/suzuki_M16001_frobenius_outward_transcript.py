#!/usr/bin/env python3
"""Outward arithmetic for the complete 79,910-entry residual Frobenius norm.

This closes only the final reduction/sqrt stage.  It regenerates the v13.514
entrywise residual R and arithmetic envelope E, then charges:
  t_k=(|R_k|+E_k)^2,
  T=sum_{k=1}^{79910} t_k,
  sqrt(T).
The square products and full accumulation use standard gamma bounds.  The final
sqrt is enclosed by one correctly-rounded-operation relative charge gamma_1.
Primitive matrix/pole/payload formation radii from later gates must be folded
into E before this becomes the final theorem residual certificate.
"""
from __future__ import annotations
import numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import source_data_stop, finite_solve_stop, off_block, PI
LD=np.longdouble; U=LD(2)**LD(-64)
def gamma(k):
    ku=LD(k)*U
    if ku>=1: raise ArithmeticError
    return ku/(1-ku)

def report(chunk=128):
    modes,Z,diag0,c=source_data_stop(); _,_,_,X,_=finite_solve_stop()
    low,high=modes[:10],modes[10:]; ZC,ZF=Z[:10],Z[10:]; cC,cF=c[:10],c[10:]
    AFC=off_block(high,ZF,low,ZC)+2*np.outer(cF,cC)
    N=len(high); M=N*10
    h=high.astype(LD); z=ZF.astype(LD); cc=cF.astype(LD); xd=X.astype(LD)
    rhs=AFC.astype(LD); dg=diag0[10:].astype(LD); pi=LD(PI)
    cx=np.sum(cc[:,None]*xd,axis=0,dtype=LD)
    cx_abs=np.sum(np.abs(cc[:,None]*xd),axis=0,dtype=LD); cx_rad=gamma(N)*cx_abs
    # Accumulate midpoint t values and their multiplication radii separately.
    tsum=LD(0); square_rad_sum=LD(0); point2=LD(0)
    for s in range(0,N,chunk):
        e=min(N,s+chunk); m=h[s:e,None]; n=h[None,:]
        with np.errstate(divide='ignore',invalid='ignore'):
            A=-(LD(2)/pi)*(n*z[s:e,None]-m*z[None,:])/(n*n-m*m)
        for ii,row in enumerate(range(s,e)): A[ii,row]=dg[row]
        for r in range(10):
            prod=A*xd[None,:,r]; sm=np.sum(prod,axis=1,dtype=LD); ab=np.sum(np.abs(prod),axis=1,dtype=LD)
            dr=gamma(N)*ab; pole=2*cc[s:e]*cx[r]
            er=dr+2*np.abs(cc[s:e])*cx_rad[r]+gamma(3)*(np.abs(sm)+np.abs(pole))
            val=sm+pole; er+=gamma(1)*(np.abs(val)+np.abs(rhs[s:e,r]))
            R=val-rhs[s:e,r]; y=np.abs(R)+er
            # Charge y addition itself; er already bounds prior arithmetic.
            y_rad=gamma(1)*(np.abs(R)+er)
            yup=y+y_rad
            t=yup*yup
            tr=gamma(1)*t
            tsum += np.sum(t,dtype=LD)
            square_rad_sum += np.sum(tr,dtype=LD)
            point2 += np.sum(R*R,dtype=LD)
    # Treat the complete reduction as one M-term nonnegative sum; this is more
    # conservative than the actual chunk tree and therefore independent of it.
    sum_rad=gamma(M)*tsum
    Tupper=tsum+square_rad_sum+sum_rad
    root=np.sqrt(Tupper)
    root_upper=root*(LD(1)+gamma(1))
    print('N =',N,' entries =',M)
    print('u =',U)
    print('gamma_79910 =',gamma(M))
    print('point Frobenius =',np.sqrt(point2))
    print('midpoint sum of charged squares =',tsum)
    print('sum square-product radii =',square_rad_sum)
    print('full 79910-term accumulation radius =',sum_rad)
    print('T upper =',Tupper)
    print('sqrt midpoint =',root)
    print('sqrt rounding charge =',root*gamma(1))
    print('OUTWARD FROBENIUS BOUND =',root_upper)
    print('FAIL-CLOSED: this value closes the Frobenius arithmetic stage conditional on the E payload supplied above; primitive displacement/pole/payload radii must be merged into E for the final residual certificate.')
if __name__=='__main__': report()
