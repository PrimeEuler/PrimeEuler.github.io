#!/usr/bin/env python3
import numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import source_data_stop, finite_solve_stop, off_block, PI
from suzuki_M16001_frobenius_outward_accumulation import outward_frobenius
LD=np.longdouble; U=LD(2)**LD(-64)
def gamma(k):
    ku=LD(k)*U; return ku/(1-ku)
def main(chunk=128):
    modes,Z,diag0,c=source_data_stop(); _,_,_,X,_=finite_solve_stop()
    low,high=modes[:10],modes[10:]; ZC,ZF=Z[:10],Z[10:]; cC,cF=c[:10],c[10:]
    AFC=off_block(high,ZF,low,ZC)+2*np.outer(cF,cC); N=len(high)
    h=high.astype(LD); z=ZF.astype(LD); cc=cF.astype(LD); xd=X.astype(LD)
    rhs=AFC.astype(LD); dg=diag0[10:].astype(LD); pi=LD(PI)
    cx=np.sum(cc[:,None]*xd,axis=0,dtype=LD); cx_abs=np.sum(np.abs(cc[:,None]*xd),axis=0,dtype=LD); cx_rad=gamma(N)*cx_abs
    RR=[]; EE=[]
    for s in range(0,N,chunk):
        e=min(N,s+chunk); m=h[s:e,None]; n=h[None,:]
        with np.errstate(divide='ignore',invalid='ignore'):
            A=-(LD(2)/pi)*(n*z[s:e,None]-m*z[None,:])/(n*n-m*m)
        for ii,row in enumerate(range(s,e)): A[ii,row]=dg[row]
        R=np.empty((e-s,10),dtype=LD); E=np.empty_like(R)
        for r in range(10):
            prod=A*xd[None,:,r]; sm=np.sum(prod,axis=1,dtype=LD); ab=np.sum(np.abs(prod),axis=1,dtype=LD); dr=gamma(N)*ab
            pole=2*cc[s:e]*cx[r]
            er=dr+2*np.abs(cc[s:e])*cx_rad[r]+gamma(3)*(np.abs(sm)+np.abs(pole))
            val=sm+pole; er+=gamma(1)*(np.abs(val)+np.abs(rhs[s:e,r]))
            R[:,r]=val-rhs[s:e,r]; E[:,r]=er
        RR.append(R); EE.append(E)
    R=np.vstack(RR); E=np.vstack(EE)
    print('legacy point Frobenius =',np.sqrt(np.sum(R*R,dtype=LD)))
    print('legacy uncharged envelope =',np.sqrt(np.sum((np.abs(R)+E)**2,dtype=LD)))
    hi=outward_frobenius(R,E)
    print('CERTIFIED-ARITHMETIC-STAGE RESIDUAL <=',hi)
if __name__=='__main__': main()
