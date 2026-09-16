#!/usr/bin/env python3
"""Entrywise weighted propagation of M16001 displacement arithmetic radii.

Unlike the coarse max-entry guard, this recomputes the v13.521 primitive
roundoff formula rowwise and contracts each actual FF entry radius against
|X_jr|.  No empirical discrepancy or fitted multiplier is used.
"""
import numpy as np
from suzuki_M16001_even_index3_anisotropic_tail_split import source_data_stop, finite_solve_stop, PI
LD=np.longdouble; U=LD(2)**LD(-64)
def g(k):
    ku=LD(k)*U; return ku/(1-ku)
def radii_vec(m,zm,n,zn,pi):
    p=n*zm; q=m*zn; num=p-q
    ep=g(1)*np.abs(p); eq=g(1)*np.abs(q); enum=ep+eq+g(1)*(np.abs(p)+np.abs(q))
    n2=n*n; m2=m*m; den=n2-m2
    en2=g(1)*np.abs(n2); em2=g(1)*np.abs(m2); eden=en2+em2+g(1)*(np.abs(n2)+np.abs(m2))
    ad=np.abs(den)
    quot=np.divide(num,den,out=np.zeros_like(num),where=den!=0)
    safe=np.where(den!=0,ad-eden,LD(1))
    equot=np.where(den!=0,enum/safe+np.abs(num)*eden/(ad*safe)+g(1)*np.abs(quot),LD(0))
    k=LD(2)/pi; ek=g(1)*abs(k); val=-k*quot
    rad=abs(k)*equot+np.abs(quot)*ek+ek*equot+g(1)*np.abs(val)
    return rad

def main():
    modes,Z,diag0,c=source_data_stop(); _,_,_,X,_=finite_solve_stop()
    F=modes[10:].astype(LD); ZF=Z[10:].astype(LD); X=np.asarray(X,dtype=LD); pi=LD(PI)
    N=len(F); E=np.zeros((N,10),dtype=LD); ax=np.abs(X)
    maxrad=LD(0)
    for i in range(N):
        rad=radii_vec(F[i],ZF[i],F,ZF,pi); rad[i]=LD(0)
        maxrad=max(maxrad,np.max(rad)); E[i,:]=rad@ax
    # FC displacement and pole arithmetic are tiny relative to FF; use their
    # independently audited uniform maxima conservatively.
    rho_fc=LD('4.848047102922417e-19')+LD('1.9322245000793252e-20')+LD('1.937913948121446246e-20')
    E+=rho_fc
    # Charge formation of each rowwise weighted reduction conservatively with gamma_N.
    E+=g(N)*E
    sq=np.sum(E*E,dtype=LD); sq_hi=sq+g(1)*sq+g(N*10)*sq
    hi=np.nextafter(np.sqrt(sq_hi),LD(np.inf),dtype=LD)
    print('entrywise recomputed max FF radius =',maxrad)
    print('max weighted residual-entry primitive increment =',np.max(E))
    print('OUTWARD entrywise-weighted known-primitive Frobenius increment <=',hi)
    print('FAIL-CLOSED remainder: diag_payload_conversion, source_payload_conversion, X_payload_conversion')
if __name__=='__main__': main()
